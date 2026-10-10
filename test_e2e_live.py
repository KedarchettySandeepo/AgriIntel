"""
AgriIntel - Comprehensive End-to-End Test Suite
Runs all unit tests, model verification, live Flask test client endpoints,
sample diagnostics across baseline and new crops, and safety guardrails.
"""

import sys
import io
import json
import time
import unittest
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent
TEST_DIR = BASE_DIR / "dataset" / "classification_v5_curated" / "test"

print("=" * 70)
print("     🌾 AGRIINTEL - COMPREHENSIVE END-TO-END TEST SUITE")
print("=" * 70)

# -----------------------------------------------------------------------------
# 1. Run All Unit & Integration Tests in tests/
# -----------------------------------------------------------------------------
print("\n[PHASE 1] Running Automated Unit & Integration Tests (tests/)...")
loader = unittest.TestLoader()
suite = loader.discover("tests")
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

if not result.wasSuccessful():
    print("❌ Unit test failures encountered!")
    sys.exit(1)
print(f"✓ All {result.testsRun} automated unit tests PASSED successfully!\n")

# -----------------------------------------------------------------------------
# 2. Test Live Flask Server with Flask Test Client
# -----------------------------------------------------------------------------
print("[PHASE 2] Initializing Live Flask Test Client & Model Pipeline...")
from backend.server import app

client = app.test_client()

# A. Health Check
print("\n--- Test 2.1: /api/health ---")
resp = client.get("/api/health")
assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"
health_data = json.loads(resp.data)
print(f"  Status Code: {resp.status_code}")
print(f"  Model Loaded: {health_data['model_loaded']}")
print(f"  Model Path:   {health_data['model_path']}")
print(f"  Total Classes: {health_data['classes_count']}")
print(f"  Supported Crops: {health_data['supported_crops_count']}")
assert health_data["classes_count"] == 87, f"Expected 87 classes, got {health_data['classes_count']}"
assert health_data["supported_crops_count"] == 22, f"Expected 22 crops, got {health_data['supported_crops_count']}"
print("  ✓ Health Check Passed!")

# B. Classes Catalog
print("\n--- Test 2.2: /api/classes ---")
resp = client.get("/api/classes")
assert resp.status_code == 200
classes_data = json.loads(resp.data)
print(f"  Total Classes: {classes_data['total_classes']}")
print(f"  Supported Crops Count: {len(classes_data['supported_crops'])}")
print(f"  Expanded Crops Count:  {len(classes_data['expanded_knowledge_crops'])}")
assert classes_data["total_classes"] == 87
assert len(classes_data["supported_crops"]) == 22
print("  ✓ Classes Catalog Passed!")

# C. Diagnostics on Standard Frontend Samples
print("\n--- Test 2.3: /api/diagnose with Standard Frontend Samples ---")
samples_to_test = [
    ("Tomato Early Blight", "frontend/samples/tomato_early_blight.jpg", {}),
    ("Paddy Bacterial Blight", "frontend/samples/paddy_bacterial_blight.jpg", {}),
    ("Wheat Yellow Rust", "frontend/samples/wheat_yellow_rust.jpg", {}),
    ("Apple Healthy", "frontend/samples/apple_healthy.jpg", {}),
]

for label, img_rel_path, extra_data in samples_to_test:
    img_path = BASE_DIR / img_rel_path
    assert img_path.exists(), f"Sample not found: {img_path}"
    with open(img_path, "rb") as f:
        data = {"image": (io.BytesIO(f.read()), img_path.name), "include_search": "false"}
        data.update(extra_data)
        t0 = time.time()
        resp = client.post("/api/diagnose", data=data, content_type="multipart/form-data")
        lat_ms = (time.time() - t0) * 1000.0

    assert resp.status_code == 200, f"Failed on {label}: {resp.status_code}"
    diag = json.loads(resp.data)
    pred = diag["prediction"]
    unc = diag["uncertainty"]
    top3 = diag["top_predictions"]
    print(f"  [{label}] -> {pred['class_name']} ({pred['confidence']}%) in {lat_ms:.1f}ms")
    print(f"      Top-3: {[c['class_name'] + ' (' + str(c['confidence']) + '%)' for c in top3]}")
    print(f"      Uncertain: {unc['is_uncertain']}, Pathogen: {diag['information'].get('pathogen_type')}")
    assert "class_name" in pred
    assert len(top3) >= 1
print("  ✓ Standard Samples Diagnostics Passed!")

# D. Diagnostics on Newly Ingested High-Value Regional Crops (Test Set)
print("\n--- Test 2.4: /api/diagnose with New Regional Crops (Chilli, Mango, Banana, Cotton, Turmeric) ---")
new_crop_samples = []

def get_first_image(directory):
    for f in directory.iterdir():
        if f.is_file() and f.suffix.lower() in {".jpg", ".jpeg", ".png"}:
            return f
    return None

chilli_dir = TEST_DIR / "Chilli___anthracnose"
if chilli_dir.exists():
    img = get_first_image(chilli_dir)
    if img: new_crop_samples.append(("Chilli Anthracnose", img))

mango_dir = TEST_DIR / "Mango___anthracnose"
if mango_dir.exists():
    img = get_first_image(mango_dir)
    if img: new_crop_samples.append(("Mango Anthracnose", img))

banana_dir = TEST_DIR / "Banana___black_sigatoka"
if banana_dir.exists():
    img = get_first_image(banana_dir)
    if img: new_crop_samples.append(("Banana Black Sigatoka", img))

cotton_dir = TEST_DIR / "Cotton___alternaria_leaf_spot"
if cotton_dir.exists():
    img = get_first_image(cotton_dir)
    if img: new_crop_samples.append(("Cotton Alternaria Leaf Spot", img))

turmeric_dir = TEST_DIR / "Turmeric___leaf_spot"
if turmeric_dir.exists():
    img = get_first_image(turmeric_dir)
    if img: new_crop_samples.append(("Turmeric Leaf Spot", img))

for label, img_file in new_crop_samples:
    with open(img_file, "rb") as f:
        data = {"image": (io.BytesIO(f.read()), img_file.name), "include_search": "false"}
        t0 = time.time()
        resp = client.post("/api/diagnose", data=data, content_type="multipart/form-data")
        lat_ms = (time.time() - t0) * 1000.0

    assert resp.status_code == 200, f"Failed on {label}: {resp.status_code}"
    diag = json.loads(resp.data)
    pred = diag["prediction"]
    print(f"  [{label}] -> {pred['class_name']} ({pred['confidence']}%) in {lat_ms:.1f}ms")
    print(f"      Symptoms count: {len(diag['information'].get('symptoms', []))}")
    print(f"      Next steps count: {len(diag['information'].get('recommended_next_steps', []))}")
    assert len(diag["information"].get("symptoms", [])) > 0
    assert len(diag["information"].get("recommended_next_steps", [])) > 0
print("  ✓ New Regional Crop Diagnostics Passed!")

# E. Safety Guardrails: Crop-Hint Mismatch & Unsupported Crop
print("\n--- Test 2.5: Safety Guardrails & Uncertainty Rejection ---")
# 1. Crop Hint Mismatch: Tomato leaf with Cotton hint
tomato_img = BASE_DIR / "frontend/samples/tomato_early_blight.jpg"
with open(tomato_img, "rb") as f:
    data = {
        "image": (io.BytesIO(f.read()), "tomato.jpg"),
        "crop_hint": "Cotton",
        "include_search": "false"
    }
    resp = client.post("/api/diagnose", data=data, content_type="multipart/form-data")
assert resp.status_code == 200
diag = json.loads(resp.data)
print(f"  Crop-Hint Mismatch (Tomato leaf + 'Cotton' hint):")
print(f"    Predicted Crop: {diag['prediction']['crop']}")
print(f"    Crop Hint:      {data['crop_hint']}")
print(f"    Uncertainty:    {diag['uncertainty']['is_uncertain']}")
print(f"    Rejection Note: {diag['uncertainty']['rejection_message'][:70]}...")
assert diag["uncertainty"]["is_uncertain"] is True
assert ("diagnosed" in diag["uncertainty"]["rejection_message"].lower() or 
        "not match" in str(diag["uncertainty"]["rejection_reason"]).lower())
print("    ✓ Crop-Hint Mismatch Guardrail Verified!")

# 2. Unsupported / Knowledge-Only Crop Hint: Tomato leaf with 'Groundnut' hint
with open(tomato_img, "rb") as f:
    data = {
        "image": (io.BytesIO(f.read()), "tomato.jpg"),
        "crop_hint": "Groundnut",
        "include_search": "false"
    }
    resp = client.post("/api/diagnose", data=data, content_type="multipart/form-data")
assert resp.status_code == 200
diag = json.loads(resp.data)
print(f"\n  Knowledge-Base-Only Crop Hint ('Groundnut'):")
print(f"    Uncertainty:    {diag['uncertainty']['is_uncertain']}")
print(f"    Rejection Note: {diag['uncertainty']['rejection_message'][:80]}...")
assert diag["uncertainty"]["is_uncertain"] is True
assert ("knowledge base" in diag["uncertainty"]["rejection_message"].lower() or
        "queued" in diag["uncertainty"]["rejection_message"].lower() or
        "unsupported" in diag["uncertainty"]["rejection_message"].lower())
print("    ✓ Unsupported Crop Guardrail Verified!")

# 3. Invalid File Upload
resp = client.post("/api/diagnose", data={"crop_hint": "Tomato"}, content_type="multipart/form-data")
assert resp.status_code == 400
print(f"\n  Missing File Upload Status: {resp.status_code} (Properly Rejected)")
print("    ✓ Invalid Input Guardrail Verified!")

# F. Agricultural Search Endpoint Compatibility
print("\n--- Test 2.6: /api/agricultural-search Endpoint ---", flush=True)
resp = client.post(
    "/api/agricultural-search",
    json={"crop": "Tomato", "disease": "Early Blight", "category": "prevention"}
)
assert resp.status_code == 200
search_data = json.loads(resp.data)
print(f"  Search Success: {search_data.get('success')}", flush=True)
print(f"  Results Count: {len(search_data.get('sources', []))}", flush=True)
print("  ✓ Agricultural Search Endpoint Verified!", flush=True)

# G. Static Frontend Serving
print("\n--- Test 2.7: Frontend Static Asset Serving ---", flush=True)
resp = client.get("/")
assert resp.status_code == 200
assert b"AgriIntel" in resp.data
print("  Static Index Serving: 200 OK (Contains 'AgriIntel')", flush=True)
print("  ✓ Frontend Serving Verified!", flush=True)

print("\n" + "=" * 70, flush=True)
print("     🎉 ALL END-TO-END TESTS COMPLETED SUCCESSFULLY (100% PASS)!", flush=True)
print("=" * 70, flush=True)
