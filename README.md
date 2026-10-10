# 🌱 AgriIntel — AI-Powered Crop Disease Detection & Agricultural Intelligence

AgriIntel is a full-stack, responsible agricultural intelligence system that unites **deep learning computer vision** with **verified botanical knowledge** and **real-time agricultural extension research**.

It allows farmers, agronomists, and extension field agents to photograph a crop leaf, receive an immediate statistical classification across 54 trained crop-disease categories, review structured botanical symptoms and recommended cultural actions, and explore live research publications from trusted extension bodies (ICAR, TNAU, IRRI, FAO) using SerpApi.

---

## 📸 System Architecture & Workflow

```text
               Crop / Leaf Photograph (User Upload / Camera)
                                    │
                                    ▼
                     ┌──────────────────────────────┐
                     │ Preprocessing & Quality Gate │
                     │  (MIME, Size, Res: 224x224)  │
                     └──────────────┬───────────────┘
                                    │
                                    ▼
                     ┌──────────────────────────────┐
                     │   Ultralytics YOLO (v4.2)    │
                     │  GPU Inference (RTX 3050)    │
                     └──────────────┬───────────────┘
                                    │
             ┌──────────────────────┴──────────────────────┐
             │                                             │
             ▼                                             ▼
   Top-1 & Top-3 Candidates                     Uncertainty & Rejection Guard
   (Confidence Probability %)                   - Low Confidence (< 45%)
             │                                  - Ambiguous Multi-Crop Margin
             │                                  - Unsupported Crop Flag
             │                                             │
             ▼                                             ▼
   ┌───────────────────┐                         ┌───────────────────────────┐
   │ Verified Guidance │                         │ Transparent Rejection Box │
   │ Database (54 Cls) │                         │ (Protects against false   │
   │ Symptoms, Actions │                         │  diagnoses on out-of-     │
   │ & Prevention      │                         │  distribution foliage)    │
   └─────────┬─────────┘                         └───────────────────────────┘
             │
             ▼
   ┌───────────────────────────────────────────────┐
   │ Agricultural Research Explorer (SerpApi)     │
   │ Real-time ICAR / TNAU / IRRI extension papers │
   └───────────────────────────────────────────────┘
```

---

## 🌿 Model Scope & Boundary Safeguards

AgriIntel values transparency and ethical AI principles. Computer vision models must never pretend to support crops they were not trained to recognize.

### 16 Supported Crops (54 Trained Classes)
1. **Apple** (4): Apple Scab, Black Rot, Cedar Apple Rust, Healthy
2. **Blueberry** (1): Healthy
3. **Cherry** (2): Powdery Mildew, Healthy
4. **Corn (Maize)** (4): Gray Leaf Spot, Common Rust, Northern Leaf Blight, Healthy
5. **Grape** (4): Black Rot, Esca (Black Measles), Isariopsis Leaf Blight, Healthy
6. **Orange / Citrus** (1): Huanglongbing (Citrus Greening)
7. **Paddy / Rice** (10): Bacterial Leaf Blight, Bacterial Leaf Streak, Bacterial Panicle Blight, Blast, Brown Spot, Dead Heart (Stem Borer), Downy Mildew, Hispa, Normal (Healthy), Tungro
8. **Peach** (2): Bacterial Spot, Healthy
9. **Bell Pepper** (2): Bacterial Spot, Healthy
10. **Potato** (3): Early Blight, Late Blight, Healthy
11. **Raspberry** (1): Healthy
12. **Soybean** (1): Healthy
13. **Squash** (1): Powdery Mildew
14. **Strawberry** (2): Leaf Scorch, Healthy
15. **Tomato** (10): Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites (Two-Spotted), Target Spot, Yellow Leaf Curl Virus (TYLCV), Mosaic Virus (ToMV), Healthy
16. **Wheat** (6): Healthy, Leaf Rust, Powdery Mildew, Septoria Blotch, Stem Rust, Yellow / Stripe Rust

### Explicitly Unsupported Crops (Automated Rejection)
The model was **not trained** on crops such as:
- **Cotton**, **Chilli**, **Groundnut**, **Mango**, **Banana**, **Pigeon Pea**, **Sugarcane**, **Onion**, **Coffee**, **Tea**, **Mustard**.

**Uncertainty Policy:** If an image has low confidence (`< 45%`), ambiguous top margins, or belongs to an unsupported crop, AgriIntel displays an explicit safeguard notification:
> *"This image may belong to a crop or condition outside the model's 16 supported classes. Please upload a clearer leaf image or consult a local agricultural expert."*

---

## ⚡ Technical Specifications

- **Operating System:** Windows 11
- **Python Version:** Python 3.11 (Virtual Environment: `venv`)
- **Deep Learning Framework:** PyTorch 2.11.0 with CUDA 12.8 support
- **Hardware Acceleration:** NVIDIA GeForce RTX 3050 Laptop GPU (4 GB VRAM)
- **Computer Vision Model:** Ultralytics YOLO Classification v4.2 Checkpoint:
  `runs\classify\runs\classify\crop_disease_classifier_v4-2\weights\best.pt`
- **Training Dataset:** `dataset\classification_v4` (~54,153 train images, ~6,898 val images, ~6,953 test images across 54 classes)
- **Backend Server:** Flask with Flask-CORS and static asset routing
- **Frontend Architecture:** Vanilla HTML5, CSS3, and JavaScript (ES6+), optimized for responsive desktop, tablet, and mobile viewing
- **Multilingual Support:** English, Hindi (हिन्दी), and Odia (ଓଡ଼ିଆ)
- **Voice Accessibility:** Built-in Web Speech API synthesis
- **Web Search Engine:** SerpApi Google Search API with agricultural domain scoring

---

## 🚀 Running AgriIntel Locally

### 1. Environment & API Setup
Ensure `SERPAPI_KEY` is configured in your `.env` file in the project root:
```env
SERPAPI_KEY=your_actual_serpapi_key_here
```

### 2. Start the Flask Application
Run the backend server using the virtual environment:
```powershell
.\venv\Scripts\python.exe backend\server.py
```

The application will start at:
- **Web Interface:** `http://127.0.0.1:5000`
- **API Health:** `http://127.0.0.1:5000/api/health`
- **API Classes:** `http://127.0.0.1:5000/api/classes`

---

## 📡 REST API Documentation

### `GET /api/health`
Returns system status, device specifications, model load state, and CUDA GPU memory stats.
```json
{
  "success": true,
  "status": "online",
  "service": "AgriIntel AI Crop Intelligence",
  "model_loaded": true,
  "device": "cuda:0",
  "device_name": "NVIDIA GeForce RTX 3050 Laptop GPU",
  "classes_count": 54,
  "supported_crops_count": 16
}
```

### `GET /api/classes`
Returns the 54 model classes grouped by crop, supported crops list, and unsupported crop examples.
```json
{
  "success": true,
  "total_classes": 54,
  "supported_crops": ["Apple", "Blueberry", "..."],
  "unsupported_crops_examples": ["Cotton", "Chilli", "..."],
  "crops": { "Tomato": [...], "Paddy": [...] }
}
```

### `POST /api/diagnose`
Accepts a multipart form upload containing an `image` file and optional `crop_hint`.
**Form Parameters:**
- `image`: File (JPEG, PNG, WebP up to 15 MB)
- `crop_hint`: (Optional) e.g., `"Tomato"`, `"Auto-detect"`, `"Cotton"`
- `include_search`: `"true"` or `"false"`

**Response Payload:**
- `prediction`: Top-1 predicted class, crop display name, condition display name, confidence percentage, confidence tier (`high`, `medium`, `low`).
- `top_predictions`: List of Top-3 candidates with their individual confidence probabilities.
- `uncertainty`: `{ is_uncertain: bool, rejection_reason: str, rejection_message: str }`
- `information`: Verified botanical overview, typical visible symptoms, recommended next steps (farmer actions), and preventive practices.
- `disclaimer`: Preliminary diagnosis advisory warning.
- `agricultural_sources`: Web citations from SerpApi.

### `POST /api/agricultural-search`
Accepts a JSON payload to query agricultural research independently.
**Request Body:**
```json
{
  "crop": "Tomato",
  "disease": "Early blight",
  "category": "management",
  "query": "organic control India"
}
```
**Response:**
Returns ranked citations with `title`, `link`, `snippet`, `domain`, and `trust_badge` (`Official Research / University`, `Academic / Extension`, `Agricultural Reference`).

---

## ⚠️ Important Agricultural Advisory Disclaimer

> [!IMPORTANT]
> **Preliminary AI Screening:**
> Predictions generated by AgriIntel are statistical probability estimates derived from automated computer vision. They are intended solely as early-warning screening aids and **must not replace an in-person diagnostic evaluation** by a certified agricultural extension officer, university agronomist, or local Krishi Vigyan Kendra (KVK).
> 
> **Never apply synthetic chemical pesticides or commercial treatments based solely on an automated AI prediction.** Always consult official product labels and regional university advisories.
