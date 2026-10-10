"""
AgriIntel - Robust Multi-Crop Dataset Preparation & Manifest Pipeline
Builds dataset/classification_v5_curated by:
1. Preserving all 54 golden baseline classes from dataset/classification_v4 (maintaining test set isolation)
2. Ingesting 33 new classes across 6 high-value Indian crops (Banana, Chilli, Cotton, Mango, Turmeric, Palm)
3. Enforcing image integrity checks (PIL verify, format validation, corruption exclusion)
4. Preventing data leakage via perceptual hashing (grouping near-duplicates before stratified splitting)
5. Exporting a comprehensive machine-readable dataset_manifest.json with license and source provenance
"""

import os
import sys
import json
import hashlib
import shutil
import random
from pathlib import Path
from collections import defaultdict
from PIL import Image

# Fix console encoding on Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

RANDOM_SEED = 42
TRAIN_RATIO = 0.80
VAL_RATIO = 0.10
TEST_RATIO = 0.10

BASE_DIR = Path(__file__).resolve().parent
V4_DIR = BASE_DIR / "dataset" / "classification_v4"
TARGET_DIR = BASE_DIR / "dataset" / "classification_v5_curated"
RAW_ANDHRA_DIR = (
    BASE_DIR
    / "dataset"
    / "new_crops_raw_data"
    / "Pigeon_pea_candidate"
    / "extracted"
    / "andhra-focused-multi-crop-disease-dataset"
    / "Andhra_Master_Dataset"
)
MANIFEST_PATH = BASE_DIR / "dataset_manifest.json"

# Strict mapping from raw folders to standard AgriIntel classes
NEW_CLASS_MAPPING = {
    # Banana (4 classes)
    "Banana_Black Sigatoka": "Banana___black_sigatoka",
    "Banana_Cordana Leaf Spot": "Banana___cordana_leaf_spot",
    "Banana_Healthy": "Banana___healthy",
    "Banana_Panama Disease": "Banana___panama_disease",

    # Chilli (8 classes)
    "Chilli_Anthracnose": "Chilli___anthracnose",
    "Chilli_Damping Off": "Chilli___damping_off",
    "Chilli_Healthy": "Chilli___healthy",
    "Chilli_Leaf Curl Virus": "Chilli___leaf_curl_virus",
    "Chilli_Leaf Spot": "Chilli___leaf_spot",
    "Chilli_Veinal Mottle Virus": "Chilli___veinal_mottle_virus",
    "Chilli_Whitefly": "Chilli___whitefly_damage",
    "Chilli_Yellowish": "Chilli___yellowing_deficiency",

    # Cotton (5 classes)
    "Cotton_Alternaria Leaf Spot": "Cotton___alternaria_leaf_spot",
    "Cotton_Bacterial Blight": "Cotton___bacterial_blight",
    "Cotton_Fusarium Wilt": "Cotton___fusarium_wilt",
    "Cotton_Healthy": "Cotton___healthy",
    "Cotton_Verticillium Wilt": "Cotton___verticillium_wilt",

    # Mango (8 classes)
    "Mango_Anthracnose": "Mango___anthracnose",
    "Mango_Bacterial Canker": "Mango___bacterial_canker",
    "Mango_Cutting Weevil": "Mango___cutting_weevil",
    "Mango_Die Back": "Mango___die_back",
    "Mango_Gall Midge": "Mango___gall_midge",
    "Mango_Healthy": "Mango___healthy",
    "Mango_Powdery Mildew": "Mango___powdery_mildew",
    "Mango_Sooty Mould": "Mango___sooty_mould",

    # Turmeric (4 classes)
    "Turmeric_Dry Leaf": "Turmeric___dry_leaf",
    "Turmeric_Healthy": "Turmeric___healthy",
    "Turmeric_Leaf Blotch": "Turmeric___leaf_blotch",
    "Turmeric_Rhizome Rot": "Turmeric___rhizome_rot",

    # Palm (4 classes)
    "Palm_Dryness": "Palm___dryness",
    "Palm_Fungal Disease": "Palm___fungal_disease",
    "Palm_Magnesium Deficiency": "Palm___magnesium_deficiency",
    "Palm_Scale Insect": "Palm___scale_insect",
}

DATASET_SOURCES_REGISTER = [
    {
        "name": "PlantVillage",
        "url": "https://github.com/spMohanty/PlantVillage-Dataset",
        "license": "Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)",
        "crops": [
            "Apple", "Blueberry", "Cherry_(including_sour)", "Corn_(maize)",
            "Grape", "Orange", "Peach", "Pepper,_bell", "Potato",
            "Raspberry", "Soybean", "Squash", "Strawberry", "Tomato"
        ],
        "image_format": "JPEG / PNG (256x256 RGB)",
        "notes": "Standard laboratory-acquired benchmark dataset with controlled background."
    },
    {
        "name": "IRRI & Mendeley Paddy Disease Dataset",
        "url": "https://data.mendeley.com/datasets/fw8275467c/1",
        "license": "Creative Commons Attribution 4.0 International (CC BY 4.0)",
        "crops": ["Paddy"],
        "image_format": "JPEG (In-field smartphone imagery)",
        "notes": "Natural field lighting with high botanical fidelity across 10 rice conditions."
    },
    {
        "name": "CIMMYT & Kaggle Wheat Rust Dataset",
        "url": "https://www.kaggle.com/datasets/imsparsh/wheat-disease-dataset",
        "license": "Open Data Commons Open Database License (ODbL) / Academic Use",
        "crops": ["Wheat"],
        "image_format": "JPEG (Field imagery)",
        "notes": "Includes stripe rust, leaf rust, stem rust, and septoria in cereal crops."
    },
    {
        "name": "Andhra Focused Multi-Crop Disease Dataset",
        "url": "https://www.kaggle.com/datasets/surajkumar/andhra-focused-multi-crop-disease-dataset",
        "license": "Creative Commons Attribution 4.0 International (CC BY 4.0)",
        "crops": ["Banana", "Chilli", "Cotton", "Mango", "Turmeric", "Palm"],
        "image_format": "JPEG (Field and farm condition photos)",
        "notes": "Curated agricultural imagery representing high-priority crops in Southern & Eastern India."
    }
]


def verify_image(path: Path) -> bool:
    """Check if file is a valid, readable image with non-zero dimensions."""
    try:
        if path.stat().st_size == 0:
            return False
        with Image.open(path) as img:
            img.verify()
        # Verify can be read as RGB
        with Image.open(path) as img:
            img.convert("RGB")
            w, h = img.size
            return w > 10 and h > 10
    except Exception:
        return False


def compute_dhash(path: Path, hash_size: int = 8) -> str:
    """Compute difference hash (dHash) to group identical or visually duplicate images."""
    try:
        with Image.open(path) as img:
            img = img.convert("L").resize((hash_size + 1, hash_size), Image.Resampling.LANCZOS)
            pixels = list(img.getdata())
            diff = []
            for row in range(hash_size):
                for col in range(hash_size):
                    left = pixels[row * (hash_size + 1) + col]
                    right = pixels[row * (hash_size + 1) + col + 1]
                    diff.append("1" if left > right else "0")
            return "".join(diff)
    except Exception:
        # Fallback to file hash
        with open(path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()


def safe_link_or_copy(src: Path, dst: Path):
    """Hardlink if supported on filesystem for zero extra disk consumption, fallback to copy."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        return
    try:
        os.link(src, dst)
    except Exception:
        shutil.copy2(src, dst)


def build_pipeline():
    print("=" * 70)
    print("      🌱 AGRIINTEL - V5 CURATED DATASET PIPELINE & AUDIT")
    print("=" * 70)

    if not V4_DIR.exists():
        raise FileNotFoundError(f"Baseline dataset missing: {V4_DIR}")
    if not RAW_ANDHRA_DIR.exists():
        raise FileNotFoundError(f"Raw Andhra dataset missing: {RAW_ANDHRA_DIR}")

    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    for s in ["train", "val", "test"]:
        (TARGET_DIR / s).mkdir(parents=True, exist_ok=True)

    class_manifest = {}
    stats_by_class = defaultdict(lambda: {"train": 0, "val": 0, "test": 0, "total": 0})
    corrupt_count = 0
    duplicate_groups_count = 0

    # -------------------------------------------------------------
    # STAGE 1: PORT 54 GOLDEN BASELINE CLASSES (STRICT ISOLATION)
    # -------------------------------------------------------------
    print("\n[Stage 1/3] Porting 54 golden baseline classes from classification_v4...")
    baseline_classes = sorted([d.name for d in (V4_DIR / "train").iterdir() if d.is_dir()])
    print(f"Found {len(baseline_classes)} classes in baseline.")

    for split in ["train", "val", "test"]:
        split_src = V4_DIR / split
        split_dst = TARGET_DIR / split
        for cls_name in baseline_classes:
            src_cls_dir = split_src / cls_name
            if not src_cls_dir.exists():
                continue
            dst_cls_dir = split_dst / cls_name
            dst_cls_dir.mkdir(parents=True, exist_ok=True)

            for img_file in src_cls_dir.iterdir():
                if img_file.is_file() and img_file.suffix.lower() in {".jpg", ".jpeg", ".png"}:
                    safe_link_or_copy(img_file, dst_cls_dir / img_file.name)
                    stats_by_class[cls_name][split] += 1
                    stats_by_class[cls_name]["total"] += 1

    print(f"  ✓ Preserved {len(baseline_classes)} baseline classes.")

    # -------------------------------------------------------------
    # STAGE 2: INGEST 33 NEW CLASSES (LEAKAGE PREVENTION & INTEGRITY)
    # -------------------------------------------------------------
    print("\n[Stage 2/3] Ingesting 33 new classes across 6 high-value crops...")
    random.seed(RANDOM_SEED)

    for raw_folder_name, clean_cls_name in sorted(NEW_CLASS_MAPPING.items()):
        raw_folder = RAW_ANDHRA_DIR / raw_folder_name
        if not raw_folder.exists():
            print(f"  ⚠ Warning: Folder not found: {raw_folder}")
            continue

        valid_images = []
        for f in raw_folder.iterdir():
            if f.is_file() and f.suffix.lower() in {".jpg", ".jpeg", ".png"}:
                if verify_image(f):
                    valid_images.append(f)
                else:
                    corrupt_count += 1

        if not valid_images:
            print(f"  ⚠ No valid images for {clean_cls_name}!")
            continue

        # Perceptual hash deduplication grouping to PREVENT DATA LEAKAGE across splits
        hash_to_files = defaultdict(list)
        for img_path in valid_images:
            h = compute_dhash(img_path)
            hash_to_files[h].append(img_path)

        unique_groups = list(hash_to_files.values())
        random.shuffle(unique_groups)

        if len(unique_groups) < len(valid_images):
            duplicate_groups_count += (len(valid_images) - len(unique_groups))

        # Stratified partition by hash cluster so duplicate frames stay in the same split
        n_groups = len(unique_groups)
        n_train_g = max(1, int(n_groups * TRAIN_RATIO))
        n_val_g = max(1, int(n_groups * VAL_RATIO))
        n_test_g = n_groups - (n_train_g + n_val_g)
        if n_test_g <= 0:
            n_test_g = 1
            n_train_g = n_groups - n_val_g - n_test_g

        train_clusters = unique_groups[:n_train_g]
        val_clusters = unique_groups[n_train_g:n_train_g + n_val_g]
        test_clusters = unique_groups[n_train_g + n_val_g:]

        split_assignments = [
            ("train", [img for cluster in train_clusters for img in cluster]),
            ("val", [img for cluster in val_clusters for img in cluster]),
            ("test", [img for cluster in test_clusters for img in cluster]),
        ]

        for split_name, img_list in split_assignments:
            dst_cls_dir = TARGET_DIR / split_name / clean_cls_name
            dst_cls_dir.mkdir(parents=True, exist_ok=True)
            for img_path in img_list:
                safe_link_or_copy(img_path, dst_cls_dir / img_path.name)
                stats_by_class[clean_cls_name][split_name] += 1
                stats_by_class[clean_cls_name]["total"] += 1

    print(f"  ✓ Deduplicated & partitioned 33 new classes.")
    print(f"  ✓ Corrupt/unreadable images excluded: {corrupt_count}")
    print(f"  ✓ Duplicate/near-duplicate instances clustered: {duplicate_groups_count}")

    # -------------------------------------------------------------
    # STAGE 3: ASSEMBLE MACHINE-READABLE MANIFEST & TAXONOMY
    # -------------------------------------------------------------
    print("\n[Stage 3/3] Generating machine-readable dataset_manifest.json...")
    all_classes_sorted = sorted(stats_by_class.keys())
    crop_stats = defaultdict(lambda: {"classes": 0, "images": 0})

    manifest_classes = []
    for idx, cls_name in enumerate(all_classes_sorted):
        if "___" in cls_name:
            crop_part, cond_part = cls_name.split("___", 1)
        else:
            crop_part, cond_part = cls_name, cls_name

        counts = stats_by_class[cls_name]
        crop_stats[crop_part]["classes"] += 1
        crop_stats[crop_part]["images"] += counts["total"]

        # Determine source
        if crop_part in ["Banana", "Chilli", "Cotton", "Mango", "Turmeric", "Palm"]:
            source_dataset = "Andhra Focused Multi-Crop Disease Dataset"
        elif crop_part == "Paddy":
            source_dataset = "IRRI & Mendeley Paddy Disease Dataset"
        elif crop_part == "Wheat":
            source_dataset = "CIMMYT & Kaggle Wheat Rust Dataset"
        else:
            source_dataset = "PlantVillage"

        manifest_classes.append({
            "class_id": idx,
            "class_name": cls_name,
            "crop": crop_part,
            "condition": cond_part,
            "sample_counts": {
                "train": counts["train"],
                "val": counts["val"],
                "test": counts["test"],
                "total": counts["total"]
            },
            "source_dataset": source_dataset
        })

    totals = {
        "train": sum(c["sample_counts"]["train"] for c in manifest_classes),
        "val": sum(c["sample_counts"]["val"] for c in manifest_classes),
        "test": sum(c["sample_counts"]["test"] for c in manifest_classes),
        "total": sum(c["sample_counts"]["total"] for c in manifest_classes),
    }

    manifest_data = {
        "title": "AgriIntel Multi-Crop Dataset Manifest (v5)",
        "version": "5.0.0",
        "random_seed": RANDOM_SEED,
        "total_classes": len(manifest_classes),
        "total_crops": len(crop_stats),
        "sample_totals": totals,
        "crops_summary": {k: dict(v) for k, v in sorted(crop_stats.items())},
        "sources_and_licenses": DATASET_SOURCES_REGISTER,
        "classes": manifest_classes
    }

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2)

    print("=" * 70)
    print("      DATASET PREPARATION & AUDIT COMPLETE")
    print("=" * 70)
    print(f"Total Unified Classes:  {len(manifest_classes)}")
    print(f"Total Supported Crops:  {len(crop_stats)}")
    print(f"Train Images:           {totals['train']}")
    print(f"Val Images:             {totals['val']}")
    print(f"Test Images:            {totals['test']}")
    print(f"Total Dataset Images:   {totals['total']}")
    print(f"Manifest written to:    {MANIFEST_PATH.resolve()}")
    print("=" * 70)


if __name__ == "__main__":
    build_pipeline()
