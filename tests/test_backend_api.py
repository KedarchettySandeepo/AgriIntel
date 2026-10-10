"""
AgriIntel Test Suite - Backend Flask API Endpoints & Robustness Validation
Tests all endpoints using Flask's test_client:
- /api/health
- /api/classes
- /api/diagnose (valid images, invalid extensions, empty files, unsupported crops, uncertainty)
- /api/agricultural-search
"""

import io
import sys
import unittest
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "backend"))

# Import Flask app from backend/server.py
from server import app


class TestBackendAPI(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_health_endpoint(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data.get("success"))
        self.assertEqual(data.get("status"), "online")
        self.assertTrue(data.get("model_loaded"))
        self.assertGreaterEqual(data.get("classes_count", 0), 54)
        self.assertIn("supported_crops", data)
        self.assertIn("device", data)

    def test_classes_endpoint(self):
        response = self.client.get("/api/classes")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data.get("success"))
        self.assertGreaterEqual(data.get("total_classes", 0), 54)
        self.assertIn("crops", data)
        self.assertIn("vision_model_crops", data)
        self.assertIn("knowledge_catalog", data)
        self.assertGreater(len(data.get("knowledge_catalog", [])), 50)

    def test_diagnose_missing_image(self):
        response = self.client.post("/api/diagnose", data={})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertFalse(data.get("success"))
        self.assertIn("error", data)

    def test_diagnose_invalid_extension(self):
        data = {
            "image": (io.BytesIO(b"fake txt content"), "test.txt")
        }
        response = self.client.post("/api/diagnose", data=data, content_type="multipart/form-data")
        self.assertEqual(response.status_code, 400)
        res = response.get_json()
        self.assertFalse(res.get("success"))
        self.assertIn("Unsupported file extension", res.get("error", ""))

    def test_diagnose_empty_file(self):
        data = {
            "image": (io.BytesIO(b""), "empty.jpg")
        }
        response = self.client.post("/api/diagnose", data=data, content_type="multipart/form-data")
        self.assertEqual(response.status_code, 400)
        res = response.get_json()
        self.assertFalse(res.get("success"))

    def test_diagnose_valid_sample_image(self):
        sample_path = BASE_DIR / "frontend" / "samples" / "tomato_early_blight.jpg"
        if not sample_path.exists():
            # Generate a synthetic 224x224 RGB JPEG
            img = Image.new("RGB", (224, 224), color=(73, 109, 137))
            buf = io.BytesIO()
            img.save(buf, format="JPEG")
            img_bytes = buf.getvalue()
        else:
            with open(sample_path, "rb") as f:
                img_bytes = f.read()

        data = {
            "image": (io.BytesIO(img_bytes), "sample.jpg"),
            "include_search": "false"
        }
        response = self.client.post("/api/diagnose", data=data, content_type="multipart/form-data")
        self.assertEqual(response.status_code, 200)
        res = response.get_json()
        self.assertTrue(res.get("success"))
        self.assertIn("prediction", res)
        self.assertIn("class_name", res["prediction"])
        self.assertIn("confidence", res["prediction"])
        self.assertIn("top_predictions", res)
        self.assertEqual(len(res["top_predictions"]), 3)
        self.assertIn("uncertainty", res)
        self.assertIn("is_uncertain", res["uncertainty"])
        self.assertIn("information", res)
        self.assertIn("disclaimer", res)

    def test_diagnose_unsupported_crop_hint(self):
        sample_path = BASE_DIR / "frontend" / "samples" / "apple_healthy.jpg"
        if sample_path.exists():
            with open(sample_path, "rb") as f:
                img_bytes = f.read()
        else:
            img = Image.new("RGB", (224, 224), color=(100, 150, 50))
            buf = io.BytesIO()
            img.save(buf, format="JPEG")
            img_bytes = buf.getvalue()

        data = {
            "image": (io.BytesIO(img_bytes), "apple.jpg"),
            "crop_hint": "Betel Vine",
            "include_search": "false"
        }
        response = self.client.post("/api/diagnose", data=data, content_type="multipart/form-data")
        self.assertEqual(response.status_code, 200)
        res = response.get_json()
        self.assertTrue(res.get("success"))
        # Should trigger uncertainty guardrail due to unsupported crop hint
        self.assertTrue(res["uncertainty"]["is_uncertain"])
        self.assertIn("Betel Vine", res["uncertainty"]["rejection_reason"])

    def test_agricultural_search_endpoint(self):
        payload = {
            "crop": "Tomato",
            "disease": "Early Blight",
            "category": "prevention"
        }
        response = self.client.post("/api/agricultural-search", json=payload)
        self.assertEqual(response.status_code, 200)
        res = response.get_json()
        self.assertIn("success", res)
        self.assertIn("sources", res)


if __name__ == "__main__":
    unittest.main()
