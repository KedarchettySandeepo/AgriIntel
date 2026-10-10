import os
import shutil
import random

# ============================================================
# AI CROP DISEASE DETECTOR - DATASET V2
# Existing 38 classes + 10 Paddy classes = 48 classes
# ============================================================

SOURCE_EXISTING = r"dataset\classification"
SOURCE_PADDY = r"dataset\raw\paddy"

OUTPUT = r"dataset\classification_v2"

# Reproducible split
random.seed(42)

SPLITS = {
    "train": 0.80,
    "val": 0.10,
    "test": 0.10
}

print("=" * 70)
print("AI CROP DISEASE DETECTOR - DATASET V2")
print("=" * 70)

# ------------------------------------------------------------
# Check existing dataset
# ------------------------------------------------------------

if not os.path.exists(SOURCE_EXISTING):
    print("ERROR: Existing classification dataset not found:")
    print(SOURCE_EXISTING)
    raise SystemExit

if not os.path.exists(SOURCE_PADDY):
    print("ERROR: Paddy dataset not found:")
    print(SOURCE_PADDY)
    raise SystemExit

# ------------------------------------------------------------
# Create output folders
# ------------------------------------------------------------

for split in SPLITS:
    os.makedirs(os.path.join(OUTPUT, split), exist_ok=True)

print("\nOutput:")
print(OUTPUT)

# ------------------------------------------------------------
# STEP 1: Copy existing 38 classes
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("COPYING EXISTING 38 CLASSES")
print("=" * 70)

existing_classes = []

for split in ["train", "val", "test"]:

    source_split = os.path.join(SOURCE_EXISTING, split)

    if not os.path.exists(source_split):
        print(f"WARNING: Missing split: {source_split}")
        continue

    for class_name in os.listdir(source_split):

        source_class = os.path.join(source_split, class_name)

        if not os.path.isdir(source_class):
            continue

        if class_name not in existing_classes:
            existing_classes.append(class_name)

        destination_class = os.path.join(
            OUTPUT,
            split,
            class_name
        )

        os.makedirs(destination_class, exist_ok=True)

        files = [
            f for f in os.listdir(source_class)
            if os.path.isfile(os.path.join(source_class, f))
        ]

        for filename in files:

            source_file = os.path.join(
                source_class,
                filename
            )

            destination_file = os.path.join(
                destination_class,
                filename
            )

            if not os.path.exists(destination_file):
                shutil.copy2(
                    source_file,
                    destination_file
                )

print(f"\nExisting classes found: {len(existing_classes)}")

# ------------------------------------------------------------
# STEP 2: Split Paddy dataset 80/10/10
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("ADDING PADDY CLASSES")
print("=" * 70)

paddy_classes = []

for class_name in sorted(os.listdir(SOURCE_PADDY)):

    source_class = os.path.join(
        SOURCE_PADDY,
        class_name
    )

    if not os.path.isdir(source_class):
        continue

    paddy_classes.append(class_name)

    files = [
        f for f in os.listdir(source_class)
        if os.path.isfile(os.path.join(source_class, f))
    ]

    random.shuffle(files)

    total = len(files)

    train_end = int(total * 0.80)
    val_end = train_end + int(total * 0.10)

    train_files = files[:train_end]
    val_files = files[train_end:val_end]
    test_files = files[val_end:]

    split_files = {
        "train": train_files,
        "val": val_files,
        "test": test_files
    }

    print(f"\n{class_name}")
    print(f"  Total: {total}")
    print(f"  Train: {len(train_files)}")
    print(f"  Val:   {len(val_files)}")
    print(f"  Test:  {len(test_files)}")

    for split, selected_files in split_files.items():

        destination_class = os.path.join(
            OUTPUT,
            split,
            class_name
        )

        os.makedirs(
            destination_class,
            exist_ok=True
        )

        for filename in selected_files:

            source_file = os.path.join(
                source_class,
                filename
            )

            destination_file = os.path.join(
                destination_class,
                filename
            )

            shutil.copy2(
                source_file,
                destination_file
            )

# ------------------------------------------------------------
# STEP 3: Summary
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("DATASET V2 COMPLETE")
print("=" * 70)

print(f"\nExisting classes : {len(existing_classes)}")
print(f"Paddy classes    : {len(paddy_classes)}")
print(f"TOTAL CLASSES    : {len(existing_classes) + len(paddy_classes)}")

print("\nClass list:")

all_classes = sorted(
    set(existing_classes + paddy_classes)
)

for i, class_name in enumerate(all_classes):
    print(f"{i:02d}. {class_name}")

print("\nImages by split:")

for split in ["train", "val", "test"]:

    split_dir = os.path.join(
        OUTPUT,
        split
    )

    image_count = 0

    for root, dirs, files in os.walk(split_dir):
        image_count += len(files)

    print(f"{split:5s}: {image_count} images")

print("\nDataset V2 location:")
print(OUTPUT)

print("\nIMPORTANT:")
print("Your original dataset/classification was NOT modified.")
print("Your existing Model V1 was NOT modified.")

print("\nNext step:")
print("Train the new 48-class Model V2.")