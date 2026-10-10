# 📊 AgriIntel Model Evaluation & Comparison Report

**Generated:** 2026-10-10 19:50:33
**Evaluation Device:** 0
**Test Set Location:** `C:\Users\LOQ\Desktop\AI-Crop-Disease-Detector\dataset\classification_v5_curated\test`

## 1. Executive Summary & Architectural Benchmark

| Metric | Baseline Model (`models/best.pt`) | Candidate Model (54 Shared Classes) | Candidate Model (All 87 Classes) |
| :--- | :--- | :--- | :--- |
| **Model Architecture** | YOLO11n-cls (54 classes) | YOLO11n-cls (87 classes) | YOLO11n-cls (87 classes) |
| **Total Supported Classes** | 54 | 87 | 87 |
| **Total Supported Crops** | 16 | 22 | 22 |
| **Test Samples Evaluated** | 6953 | 6953 | 8257 |
| **Top-1 Accuracy** | **97.51%** | **93.48%** | **93.71%** |
| **Top-3 Accuracy** | 99.35% | 98.37% | 98.55% |
| **Macro-F1 Score** | **0.9552** | **0.9013** | **0.8902** |
| **Macro-Precision** | 0.9573 | 0.9069 | 0.8909 |
| **Macro-Recall** | 0.9551 | 0.9018 | 0.8949 |
| **Inference Latency (Mean)** | 11.4 ms | 10.8 ms | 12.8 ms |
| **Inference Latency (p95)** | 82.11 ms | 78.54 ms | 96.46 ms |
| **Model Artifact Size** | 3.17 MB | 3.25 MB | 3.25 MB |

## 2. Performance by Crop (Candidate Model - 87 Classes)

| Crop | Test Samples | Correct Predictions | Top-1 Accuracy |
| :--- | :--- | :--- | :--- |
| **Apple** | 319 | 316 | **99.06%** |
| **Banana** | 187 | 180 | **96.26%** |
| **Blueberry** | 151 | 151 | **100.00%** |
| **Cherry_(including_sour)** | 192 | 192 | **100.00%** |
| **Chilli** | 349 | 325 | **93.12%** |
| **Corn_(maize)** | 388 | 370 | **95.36%** |
| **Cotton** | 250 | 233 | **93.20%** |
| **Grape** | 409 | 407 | **99.51%** |
| **Mango** | 403 | 402 | **99.75%** |
| **Orange** | 552 | 552 | **100.00%** |
| **Paddy** | 1048 | 853 | **81.39%** |
| **Palm** | 32 | 15 | **46.88%** |
| **Peach** | 267 | 267 | **100.00%** |
| **Pepper,_bell** | 250 | 249 | **99.60%** |
| **Potato** | 216 | 209 | **96.76%** |
| **Raspberry** | 38 | 38 | **100.00%** |
| **Soybean** | 509 | 505 | **99.21%** |
| **Squash** | 184 | 184 | **100.00%** |
| **Strawberry** | 159 | 159 | **100.00%** |
| **Tomato** | 1825 | 1762 | **96.55%** |
| **Turmeric** | 83 | 83 | **100.00%** |
| **Wheat** | 446 | 286 | **64.13%** |

## 3. Confidence Calibration & Uncertainty Rejection Analysis

- **Mean Confidence on Correct Diagnoses:** `94.3%`
- **Mean Confidence on Erroneous Diagnoses:** `55.4%`
- **Calibrated Threshold:** Predictions with `confidence < 0.45` or ambiguous margin `< 0.15` across disparate crops are routed to the Uncertainty Guardrail.

## 4. Top Per-Class Performance Summary (Full 87-Class Model)

| Class Name | Support | Precision | Recall | F1 Score |
| :--- | :--- | :--- | :--- | :--- |
| `Orange___Haunglongbing_(Citrus_greening)` | 552 | 0.998 | 1.000 | **0.999** |
| `Tomato___Tomato_Yellow_Leaf_Curl_Virus` | 537 | 0.996 | 0.989 | **0.993** |
| `Soybean___healthy` | 509 | 1.000 | 0.992 | **0.996** |
| `Peach___Bacterial_spot` | 231 | 0.996 | 1.000 | **0.998** |
| `Tomato___Bacterial_spot` | 214 | 0.975 | 0.925 | **0.950** |
| `Tomato___Late_blight` | 192 | 0.926 | 0.974 | **0.949** |
| `Squash___Powdery_mildew` | 184 | 1.000 | 1.000 | **1.000** |
| `Tomato___Septoria_leaf_spot` | 178 | 0.945 | 0.961 | **0.953** |
| `Paddy___normal` | 177 | 0.872 | 0.921 | **0.896** |
| `Paddy___blast` | 175 | 0.848 | 0.829 | **0.838** |
| `Tomato___Spider_mites Two-spotted_spider_mite` | 169 | 0.971 | 0.982 | **0.977** |
| `Apple___healthy` | 165 | 0.988 | 0.994 | **0.991** |
| `Paddy___hispa` | 160 | 0.833 | 0.812 | **0.823** |
| `Tomato___healthy` | 160 | 0.988 | 1.000 | **0.994** |
| `Blueberry___healthy` | 151 | 0.993 | 1.000 | **0.997** |
| `Pepper,_bell___healthy` | 149 | 0.987 | 1.000 | **0.993** |
| `Paddy___dead_heart` | 145 | 0.939 | 0.959 | **0.949** |
| `Tomato___Target_Spot` | 141 | 0.877 | 0.965 | **0.919** |
| `Grape___Esca_(Black_Measles)` | 139 | 0.993 | 0.986 | **0.989** |
| `Corn_(maize)___Common_rust_` | 120 | 0.984 | 0.992 | **0.988** |
| `Grape___Black_rot` | 118 | 0.983 | 1.000 | **0.992** |
| `Corn_(maize)___healthy` | 117 | 0.983 | 0.992 | **0.987** |
| `Strawberry___Leaf_scorch` | 112 | 1.000 | 1.000 | **1.000** |
| `Wheat___yellow_rust` | 111 | 0.813 | 0.549 | **0.656** |
| `Paddy___tungro` | 110 | 0.630 | 0.791 | **0.702** |
| `Wheat___stem_rust` | 110 | 0.748 | 0.700 | **0.723** |
| `Grape___Leaf_blight_(Isariopsis_Leaf_Spot)` | 109 | 1.000 | 1.000 | **1.000** |
| `Cherry_(including_sour)___Powdery_mildew` | 106 | 1.000 | 1.000 | **1.000** |
| `Wheat___leaf_rust` | 104 | 0.664 | 0.760 | **0.709** |
| `Pepper,_bell___Bacterial_spot` | 101 | 0.980 | 0.990 | **0.985** |
| `Potato___Early_blight` | 100 | 1.000 | 1.000 | **1.000** |
| `Potato___Late_blight` | 100 | 0.969 | 0.940 | **0.954** |
| `Tomato___Early_blight` | 100 | 0.966 | 0.850 | **0.904** |
| `Corn_(maize)___Northern_Leaf_Blight` | 99 | 0.889 | 0.970 | **0.927** |
| `Paddy___brown_spot` | 97 | 0.846 | 0.680 | **0.754** |
| `Tomato___Leaf_Mold` | 96 | 0.978 | 0.938 | **0.957** |
| `Cherry_(including_sour)___healthy` | 86 | 1.000 | 1.000 | **1.000** |
| `Apple___Apple_scab` | 63 | 1.000 | 0.968 | **0.984** |
| `Apple___Black_rot` | 63 | 1.000 | 1.000 | **1.000** |
| `Paddy___downy_mildew` | 62 | 0.586 | 0.548 | **0.567** |
| `Wheat___healthy` | 60 | 0.735 | 0.417 | **0.532** |
| `Chilli___veinal_mottle_virus` | 57 | 1.000 | 1.000 | **1.000** |
| `Mango___anthracnose` | 53 | 0.982 | 1.000 | **0.991** |
| `Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot` | 52 | 0.929 | 0.750 | **0.830** |
| `Banana___black_sigatoka` | 51 | 0.927 | 1.000 | **0.962** |
| `Banana___healthy` | 51 | 0.979 | 0.902 | **0.939** |
| `Banana___panama_disease` | 51 | 0.962 | 1.000 | **0.981** |
| `Mango___gall_midge` | 51 | 1.000 | 0.980 | **0.990** |
| `Chilli___leaf_curl_virus` | 50 | 0.861 | 0.740 | **0.796** |
| `Chilli___whitefly_damage` | 50 | 0.960 | 0.960 | **0.960** |
| `Cotton___alternaria_leaf_spot` | 50 | 0.938 | 0.900 | **0.918** |
| `Cotton___bacterial_blight` | 50 | 0.917 | 0.880 | **0.898** |
| `Cotton___fusarium_wilt` | 50 | 0.907 | 0.980 | **0.942** |
| `Cotton___healthy` | 50 | 1.000 | 1.000 | **1.000** |
| `Cotton___verticillium_wilt` | 50 | 0.882 | 0.900 | **0.891** |
| `Mango___bacterial_canker` | 50 | 0.980 | 1.000 | **0.990** |
| `Mango___die_back` | 50 | 1.000 | 1.000 | **1.000** |
| `Mango___healthy` | 50 | 0.980 | 1.000 | **0.990** |
| `Mango___powdery_mildew` | 50 | 1.000 | 1.000 | **1.000** |
| `Mango___sooty_mould` | 50 | 1.000 | 1.000 | **1.000** |
| `Chilli___leaf_spot` | 49 | 1.000 | 0.939 | **0.968** |
| `Chilli___yellowing_deficiency` | 49 | 0.774 | 0.980 | **0.865** |
| `Mango___cutting_weevil` | 49 | 0.961 | 1.000 | **0.980** |
| `Paddy___bacterial_leaf_blight` | 49 | 0.612 | 0.612 | **0.612** |
| `Chilli___anthracnose` | 47 | 1.000 | 1.000 | **1.000** |
| `Strawberry___healthy` | 47 | 1.000 | 1.000 | **1.000** |
| `Grape___healthy` | 43 | 1.000 | 1.000 | **1.000** |
| `Paddy___bacterial_leaf_streak` | 38 | 0.789 | 0.789 | **0.789** |
| `Raspberry___healthy` | 38 | 1.000 | 1.000 | **1.000** |
| `Tomato___Tomato_mosaic_virus` | 38 | 0.974 | 1.000 | **0.987** |
| `Peach___healthy` | 36 | 0.973 | 1.000 | **0.986** |
| `Wheat___powdery_mildew` | 36 | 0.527 | 0.806 | **0.637** |
| `Paddy___bacterial_panicle_blight` | 35 | 0.879 | 0.829 | **0.853** |
| `Banana___cordana_leaf_spot` | 34 | 0.970 | 0.941 | **0.955** |
| `Chilli___healthy` | 30 | 0.833 | 0.833 | **0.833** |
| `Apple___Cedar_apple_rust` | 28 | 1.000 | 1.000 | **1.000** |
| `Wheat___septoria` | 25 | 0.395 | 0.600 | **0.476** |
| `Turmeric___dry_leaf` | 21 | 1.000 | 1.000 | **1.000** |
| `Turmeric___healthy` | 21 | 1.000 | 1.000 | **1.000** |
| `Turmeric___leaf_blotch` | 21 | 1.000 | 1.000 | **1.000** |
| `Turmeric___rhizome_rot` | 20 | 1.000 | 1.000 | **1.000** |
| `Chilli___damping_off` | 17 | 0.944 | 1.000 | **0.971** |
| `Potato___healthy` | 16 | 1.000 | 0.938 | **0.968** |
| `Palm___scale_insect` | 15 | 0.522 | 0.800 | **0.632** |
| `Palm___dryness` | 7 | 0.273 | 0.429 | **0.333** |
| `Palm___magnesium_deficiency` | 7 | 0.000 | 0.000 | **0.000** |
| `Palm___fungal_disease` | 3 | 0.000 | 0.000 | **0.000** |
