"""
AgriIntel Test Suite - Dataset Manifest & Taxonomy Validation
"""

import os
import json
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MANIFEST_PATH = BASE_DIR / "dataset_manifest.json"
DATASET_DIR = BASE_DIR / "dataset" / "classification_v5_curated"


class TestDatasetManifest(unittest.TestCase):
    def setUp(self):
        self.assertTrue(MANIFEST_PATH.exists(), f"Manifest missing at {MANIFEST_PATH}")
        with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
            self.manifest = json.load(f)

    def test_manifest_metadata(self):
        self.assertEqual(self.manifest.get("version"), "5.0.0")
        self.assertEqual(self.manifest.get("total_classes"), 87)
        self.assertEqual(self.manifest.get("total_crops"), 22)
        totals = self.manifest.get("sample_totals", {})
        self.assertGreater(totals.get("train", 0), 50000)
        self.assertGreater(totals.get("val", 0), 5000)
        self.assertGreater(totals.get("test", 0), 5000)

    def test_sources_and_licenses_register(self):
        sources = self.manifest.get("sources_and_licenses", [])
        self.assertGreaterEqual(len(sources), 4)
        names = [s["name"] for s in sources]
        self.assertIn("PlantVillage", names)
        self.assertIn("IRRI & Mendeley Paddy Disease Dataset", names)
        self.assertIn("CIMMYT & Kaggle Wheat Rust Dataset", names)
        self.assertIn("Andhra Focused Multi-Crop Disease Dataset", names)
        for s in sources:
            self.assertTrue(len(s.get("license", "")) > 0)
            self.assertTrue(len(s.get("url", "")) > 0)

    def test_class_naming_and_integrity(self):
        classes = self.manifest.get("classes", [])
        self.assertEqual(len(classes), 87)
        seen_names = set()
        seen_ids = set()

        for c in classes:
            c_name = c["class_name"]
            c_id = c["class_id"]
            self.assertNotIn(c_name, seen_names, f"Duplicate class name: {c_name}")
            self.assertNotIn(c_id, seen_ids, f"Duplicate class id: {c_id}")
            seen_names.add(c_name)
            seen_ids.add(c_id)

            self.assertIn("___", c_name, f"Invalid class delimiter in {c_name}")
            crop, cond = c_name.split("___", 1)
            self.assertEqual(crop, c["crop"])
            self.assertEqual(cond, c["condition"])

            counts = c["sample_counts"]
            self.assertGreater(counts["train"], 0, f"No train samples for {c_name}")
            self.assertGreater(counts["val"], 0, f"No val samples for {c_name}")
            self.assertGreater(counts["test"], 0, f"No test samples for {c_name}")
            self.assertEqual(counts["total"], counts["train"] + counts["val"] + counts["test"])

    def test_curated_dataset_directory_structure(self):
        self.assertTrue(DATASET_DIR.exists(), f"Dataset directory missing at {DATASET_DIR}")
        for split in ["train", "val", "test"]:
            split_dir = DATASET_DIR / split
            self.assertTrue(split_dir.exists())
            class_dirs = [d for d in split_dir.iterdir() if d.is_dir()]
            self.assertEqual(len(class_dirs), 87, f"Split {split} has {len(class_dirs)} classes, expected 87")


if __name__ == "__main__":
    unittest.main()
