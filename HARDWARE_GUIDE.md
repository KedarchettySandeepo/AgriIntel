# 🖥️ Hardware-Specific Training Guide (Lenovo LOQ — RTX 3050 4 GB GPU)

This guide documents the memory-efficient computer vision training configuration specifically tuned for the **Lenovo LOQ (Intel i5-13450HX, 16 GB RAM, NVIDIA GeForce RTX 3050 Laptop GPU with 4 GB VRAM)** running Windows 11.

---

## 1. Local Hardware Profile & Memory Budget

### System Specifications
- **CPU:** Intel® Core™ i5-13450HX (10 Cores, 16 Threads, up to 4.6 GHz)
- **RAM:** 16 GB DDR5 4800 MHz
- **GPU:** NVIDIA GeForce RTX 3050 Laptop GPU (4096 MB GDDR6 VRAM, TGP: 95W)
- **CUDA Capability:** SM 8.6 (Ampere Architecture)
- **PyTorch Environment:** PyTorch `2.11.0+cu128` with CUDA 12.8 support
- **OS:** Windows 11 64-bit

### 4 GB VRAM Allocation Breakdown (at 224x224, Batch 64, AMP)
| Component | Memory Consumption | Notes |
| :--- | :--- | :--- |
| **Model Weights (YOLO11n-cls)** | ~6.5 MB | 1.64M fp32/fp16 parameters |
| **Optimizer States (AdamW)** | ~26.0 MB | 2 momentum moments per parameter |
| **Gradients** | ~6.5 MB | Backpropagation buffer |
| **Batch Activations (AMP fp16)** | ~550–650 MB | 64 images $\times$ 3 channels $\times$ 224 $\times$ 224 |
| **CUDA Context & PyTorch Overhead** | ~180–220 MB | Base CUDA driver runtime |
| **Total Peak PyTorch VRAM** | **~0.81 GB** | Verified during active training |
| **Windows Desktop Window Manager (DWM)** | ~450–600 MB | Reserved for display output |
| **Free Safety Buffer** | **~2.50 GB+** | **Zero risk of CUDA Out of Memory (OOM)** |

---

## 2. Recommended Training Profiles

### Profile A: Local RTX 3050 (4 GB VRAM) — Recommended
```powershell
# Balanced throughput and low memory footprint
.\venv\Scripts\python.exe train_v5.py --epochs 15 --batch 64 --workers 2 --device 0
```
- **Batch Size:** `64` (produces ~0.81 GB VRAM usage; ~8.5 iterations/sec)
- **Workers:** `2` (Windows process spawning overhead is minimized; avoid >4 to prevent RAM spikes)
- **Mixed Precision:** Automatic Mixed Precision (`amp=True`) enabled by default
- **Patience:** `5` (Early stopping when validation loss plateaus)

### Profile B: Low VRAM / Ultra-Safe (If running other 3D applications simultaneously)
```powershell
.\venv\Scripts\python.exe train_v5.py --epochs 15 --batch 32 --workers 2 --device 0
```
- **Batch Size:** `32` (produces ~0.45 GB VRAM usage)
- **Inference/Train Speed:** ~6.5 iterations/sec

### Profile C: Cloud GPUs (NVIDIA T4, A10G, V100, A100)
```powershell
python train_v5.py --epochs 25 --cloud-profile --device 0
```
- **Batch Size:** `64`–`128`
- **Workers:** `8`
- **AMP:** Enabled

---

## 3. End-to-End Execution Workflow (Windows PowerShell)

### Step 1: Run Sanity-Check Job
Always verify dataset parsing, caching, and GPU initialization with a lightweight sanity check first:
```powershell
.\venv\Scripts\python.exe train_v5.py --sanity-check
```

### Step 2: Full Multi-Crop Model Training
Train across all 87 classes and 22 crops on the curated dataset:
```powershell
.\venv\Scripts\python.exe train_v5.py --epochs 15 --batch 64 --workers 2 --name crop_disease_classifier_v5_run1
```

### Step 3: Evaluate & Benchmark Against Baseline
Run evaluation on the isolated test set and benchmark against `models/best.pt`:
```powershell
.\venv\Scripts\python.exe evaluate_model.py --candidate runs/classify/crop_disease_classifier_v5_run1/weights/best.pt --device cpu
```

### Step 4: Run Automated Test Suite
Execute the 18 automated regression unit and integration tests:
```powershell
.\venv\Scripts\python.exe -m unittest discover tests
```

### Step 5: Start AgriIntel Full-Stack Server
Launch the Flask backend serving both the REST API and the multilingual web UI:
```powershell
.\venv\Scripts\python.exe backend/server.py
```
Open in browser: `http://127.0.0.1:5000`

---

## 4. CUDA GPU Recovery Safeguard in Production

The AgriIntel backend (`backend/server.py`) implements a dynamic CUDA memory safeguard:
1. If the GPU encounters a sudden `torch.cuda.OutOfMemoryError` during high-concurrency requests, the server catches the exception, clears the CUDA cache via `torch.cuda.empty_cache()`, and seamlessly falls back to CPU execution without failing the user's request.
2. GPU memory is explicitly emptied after every prediction (`torch.cuda.empty_cache()`) when operating under CUDA mode.
