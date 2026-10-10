"""
AgriIntel Test Suite - Disease Knowledge Base & Botanical Guidance Validation
"""

import sys
import json
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "backend"))

from disease_knowledge import (
    DISEASE_KNOWLEDGE,
    VISION_MODEL_SUPPORTED_CROPS,
    EXPANDED_KNOWLEDGE_CROPS,
    UNSUPPORTED_CROPS_EXAMPLES,
    get_disease_info,
    is_vision_model_supported,
)


class TestDiseaseKnowledge(unittest.TestCase):
    def setUp(self):
        manifest_path = BASE_DIR / "dataset_manifest.json"
        with open(manifest_path, "r", encoding="utf-8") as f:
            self.manifest = json.load(f)

    def test_all_manifest_classes_have_guidance(self):
        classes = [c["class_name"] for c in self.manifest["classes"]]
        for cls_name in classes:
            info = get_disease_info(cls_name)
            self.assertIsNotNone(info, f"Missing knowledge for class: {cls_name}")
            self.assertIn("crop", info)
            self.assertIn("condition", info)
            self.assertIn("pathogen", info)
            self.assertIn("description", info)
            self.assertIn("symptoms", info)
            self.assertIn("recommended_next_steps", info)
            self.assertIn("preventive_practices", info)
            self.assertGreater(len(info["symptoms"]), 0)
            self.assertGreater(len(info["recommended_next_steps"]), 0)
            self.assertGreater(len(info["preventive_practices"]), 0)

    def test_vision_model_supported_crops(self):
        self.assertEqual(len(VISION_MODEL_SUPPORTED_CROPS), 22)
        expected_crops = [
            "Apple", "Banana", "Blueberry", "Cherry (including sour)", "Chilli",
            "Corn (maize)", "Cotton", "Grape", "Mango", "Orange", "Paddy",
            "Palm", "Peach", "Pepper, bell", "Potato", "Raspberry", "Soybean",
            "Squash", "Strawberry", "Tomato", "Turmeric", "Wheat"
        ]
        for c in expected_crops:
            self.assertIn(c, VISION_MODEL_SUPPORTED_CROPS)
            self.assertTrue(is_vision_model_supported(c))

    def test_unsupported_crops_handling(self):
        unsupported = ["Jute", "Flax", "Betel vine", "Vanilla", "Arecanut", "NonExistentCrop"]
        for u in unsupported:
            self.assertFalse(is_vision_model_supported(u), f"Crop {u} should not be vision supported")


if __name__ == "__main__":
    unittest.main()
