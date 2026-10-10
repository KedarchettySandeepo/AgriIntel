"""
AgriIntel - Safe Dataset Preparation Pipeline for v5 Classifier
Creates dataset/classification_v5_curated combining:
- 54 golden classes from dataset/classification_v4 (read-only baseline, all 5 wheat classes preserved)
- 33 new classes across 6 high-value crops (Banana, Chilli, Cotton, Mango, Turmeric, Palm)
Total: 87 classes across 22 crops.
"""

import os
import sys
import shutil
import random
from pathlib import Path
from collections import defaultdict

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Random seed for reproducible stratified train/val/test splits
RANDOM_SEED = 42
TRAIN_RATIO = 0.80
VAL_RATIO = 0.10
TEST_RATIO = 0.10

V4_DIR = Path("dataset/classification_v4")
V5_DIR = Path("dataset/classification_v5_curated")
RAW_ANDHRA_DIR = Path("dataset/new_crops_raw_data/Pigeon_pea_candidate/extracted/andhra-focused-multi-crop-disease-dataset/Andhra_Master_Dataset")

# Map raw folder names to clean model class names
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


def safe_link_or_copy(src: Path, dst: Path):
    """Link file if supported by OS/filesystem, otherwise copy."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        return
    try:
        os.link(src, dst)  # Hardlink: instantaneous and zero disk footprint
    except Exception:
        shutil.copy2(src, dst)


def prepare_curated_v5(dry_run: bool = False):
    print("=" * 65)
    print("      🌱 AGRIINTEL - SAFE V5 DATASET CURATION PIPELINE")
    print("=" * 65)

    if not V4_DIR.exists():
        raise FileNotFoundError(f"Golden baseline dataset '{V4_DIR}' not found!")

    if not RAW_ANDHRA_DIR.exists():
        raise FileNotFoundError(f"Raw source directory '{RAW_ANDHRA_DIR}' not found!")

    print(f"[1/4] Baseline dataset: {V4_DIR}")
    print(f"[2/4] Raw images:       {RAW_ANDHRA_DIR}")
    print(f"[3/4] Target curated:   {V5_DIR}")
    print(f"[4/4] Dry run mode:     {dry_run}")
    print("-" * 65)

    # Step 1: Copy/link 54 baseline classes from v4
    print("[Pipeline] Stage 1: Porting 54 baseline classes from classification_v4...")
    baseline_stats = defaultdict(int)
    for split in ["train", "val", "test"]:
        split_src = V4_DIR / split
        split_dst = V5_DIR / split
        if not split_src.exists():
            continue

        for cls_dir in split_src.iterdir():
            if not cls_dir.is_dir():
                continue
            images = [f for f in cls_dir.iterdir() if f.is_file() and f.suffix.lower() in {".jpg", ".jpeg", ".png"}]
            baseline_stats[cls_dir.name] += len(images)
            if not dry_run:
                target_cls_dir = split_dst / cls_dir.name
                target_cls_dir.mkdir(parents=True, exist_ok=True)
                for img_file in images:
                    safe_link_or_copy(img_file, target_cls_dir / img_file.name)

    print(f"  ✓ Preserved {len(baseline_stats)} baseline classes from v4 (including Wheat & Paddy)")

    # Step 2: Stratified split and integrate 33 new classes
    print("\n[Pipeline] Stage 2: Ingesting 33 new classes across 6 crops...")
    random.seed(RANDOM_SEED)
    new_stats = {}

    for raw_folder_name, clean_class_name in sorted(NEW_CLASS_MAPPING.items()):
        raw_folder_path = RAW_ANDHRA_DIR / raw_folder_name
        if not raw_folder_path.exists():
            print(f"  ⚠ Warning: Folder not found: {raw_folder_path}")
            continue

        images = [f for f in raw_folder_path.iterdir() if f.is_file() and f.suffix.lower() in {".jpg", ".jpeg", ".png"}]
        random.shuffle(images)
        total_imgs = len(images)
        if total_imgs == 0:
            continue

        n_train = max(1, int(total_imgs * TRAIN_RATIO))
        n_val = max(1, int(total_imgs * VAL_RATIO))
        n_test = total_imgs - (n_train + n_val)
        if n_test <= 0:
            n_test = 1
            n_train = total_imgs - n_val - n_test

        train_imgs = images[:n_train]
        val_imgs = images[n_train:n_train + n_val]
        test_imgs = images[n_train + n_val:]

        new_stats[clean_class_name] = {
            "total": total_imgs,
            "train": len(train_imgs),
            "val": len(val_imgs),
            "test": len(test_imgs)
        }

        if not dry_run:
            for split_name, split_set in [("train", train_imgs), ("val", val_imgs), ("test", test_imgs)]:
                target_dir = V5_DIR / split_name / clean_class_name
                target_dir.mkdir(parents=True, exist_ok=True)
                for img_path in split_set:
                    safe_link_or_copy(img_path, target_dir / img_path.name)

    print(f"  ✓ Processed {len(new_stats)} new disease classes ({sum(s['total'] for s in new_stats.values())} images)")

    # Step 3: Verification & Summary
    total_classes = len(baseline_stats) + len(new_stats)
    print("\n" + "=" * 65)
    print("      DATASET CURATION SUMMARY")
    print("=" * 65)
    print(f"Baseline Classes (v4):   {len(baseline_stats)} classes")
    print(f"New Ingested Classes:    {len(new_stats)} classes")
    print(f"Total Combined Classes:  {total_classes} classes across 22 crops")
    print(f"Location:                {V5_DIR.resolve()}")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    import sys
    dry_mode = "--dry-run" in sys.argv
    prepare_curated_v5(dry_run=dry_mode)
