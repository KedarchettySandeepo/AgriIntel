"""
AgriIntel Test Suite - Model Loading, Preprocessing & Inference Architecture
"""

import sys
import unittest
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "backend"))

from ultralytics import YOLO

BASELINE_PATH = BASE_DIR / "models" / "best.pt"


class TestModelPipeline(unittest.TestCase):
    def setUp(self):
        self.assertTrue(BASELINE_PATH.exists(), f"Baseline model not found at {BASELINE_PATH}")
        self.model = YOLO(str(BASELINE_PATH))

    def test_model_loading_and_architecture(self):
        self.assertEqual(self.model.task, "classify")
        self.assertGreaterEqual(len(self.model.names), 54)
        # Check model names are strings
        for k, v in self.model.names.items():
            self.assertIsInstance(k, int)
            self.assertIsInstance(v, str)
            self.assertTrue(len(v) > 0)

    def test_image_preprocessing_and_inference(self):
        # Create a standard 224x224 RGB image
        img = Image.new("RGB", (224, 224), color=(34, 139, 34))
        results = self.model.predict(source=img, device="cpu", verbose=False)
        self.assertEqual(len(results), 1)
        res = results[0]
        self.assertIsNotNone(res.probs)

        probs = res.probs
        top1_idx = int(probs.top1)
        top1_conf = float(probs.top1conf)
        self.assertIn(top1_idx, self.model.names)
        self.assertGreaterEqual(top1_conf, 0.0)
        self.assertLessEqual(top1_conf, 1.0)

    def test_non_square_and_grayscale_images(self):
        # Grayscale image (should be safely handled)
        gray_img = Image.new("L", (150, 300), color=128).convert("RGB")
        results = self.model.predict(source=gray_img, device="cpu", verbose=False)
        self.assertEqual(len(results), 1)
        probs = results[0].probs
        self.assertIsNotNone(probs.top1)

        # Small image (50x50)
        small_img = Image.new("RGB", (50, 50), color=(200, 50, 50))
        results_small = self.model.predict(source=small_img, device="cpu", verbose=False)
        self.assertEqual(len(results_small), 1)
        self.assertIsNotNone(results_small[0].probs.top1)


if __name__ == "__main__":
    unittest.main()
