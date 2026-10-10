from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent

V2_DIR = BASE_DIR / "dataset" / "classification_v2"
WHEAT_DIR = BASE_DIR / "dataset" / "wheat_v3"
V3_DIR = BASE_DIR / "dataset" / "classification_v3"

print("=" * 70)
print("CREATING V3 DATASET: V2 + WHEAT")
print("=" * 70)

# ------------------------------------------------------------
# Check source datasets
# ------------------------------------------------------------

if not V2_DIR.exists():
    raise FileNotFoundError(f"V2 dataset not found: {V2_DIR}")

if not WHEAT_DIR.exists():
    raise FileNotFoundError(f"Wheat dataset not found: {WHEAT_DIR}")

# ------------------------------------------------------------
# Remove old V3 if it exists
# ------------------------------------------------------------

if V3_DIR.exists():
    print("\nRemoving existing V3 dataset...")
    shutil.rmtree(V3_DIR)

# ------------------------------------------------------------
# Create split directories
# ------------------------------------------------------------

for split in ["train", "val", "test"]:
    (V3_DIR / split).mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------
# Copy a dataset split
# ------------------------------------------------------------

def copy_split(source_split, destination_split, dataset_name):

    source_dir = source_split
    destination_dir = V3_DIR / destination_split

    if not source_dir.exists():
        raise FileNotFoundError(
            f"{dataset_name} split not found: {source_dir}"
        )

    classes = [
        d for d in source_dir.iterdir()
        if d.is_dir()
    ]

    copied = 0

    for class_dir in classes:

        target_class = destination_dir / class_dir.name
        target_class.mkdir(
            parents=True,
            exist_ok=True
        )

        for image in class_dir.iterdir():

            if image.is_file():
                shutil.copy2(
                    image,
                    target_class / image.name
                )

                copied += 1

    return copied, len(classes)


# ------------------------------------------------------------
# Copy V2
# ------------------------------------------------------------

print("\nCopying V2 dataset...")

v2_train, v2_train_classes = copy_split(
    V2_DIR / "train",
    "train",
    "V2"
)

v2_val, v2_val_classes = copy_split(
    V2_DIR / "val",
    "val",
    "V2"
)

v2_test, v2_test_classes = copy_split(
    V2_DIR / "test",
    "test",
    "V2"
)

print(f"V2 train images: {v2_train}")
print(f"V2 val images:   {v2_val}")
print(f"V2 test images:  {v2_test}")

# ------------------------------------------------------------
# Copy Wheat
# ------------------------------------------------------------

print("\nCopying Wheat dataset...")

wheat_train, wheat_train_classes = copy_split(
    WHEAT_DIR / "train",
    "train",
    "Wheat"
)

wheat_val, wheat_val_classes = copy_split(
    WHEAT_DIR / "val",
    "val",
    "Wheat"
)

wheat_test, wheat_test_classes = copy_split(
    WHEAT_DIR / "test",
    "test",
    "Wheat"
)

print(f"Wheat train images: {wheat_train}")
print(f"Wheat val images:   {wheat_val}")
print(f"Wheat test images:  {wheat_test}")

# ------------------------------------------------------------
# Count classes
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("V3 DATASET SUMMARY")
print("=" * 70)

all_classes = set()

for split in ["train", "val", "test"]:

    split_dir = V3_DIR / split

    classes = sorted(
        d.name for d in split_dir.iterdir()
        if d.is_dir()
    )

    all_classes.update(classes)

    total = 0

    print(f"\n{split.upper()}: {len(classes)} classes")

    for class_name in classes:

        class_dir = split_dir / class_name

        count = sum(
            1 for f in class_dir.iterdir()
            if f.is_file()
        )

        total += count

        print(f"{class_name:<55} {count}")

    print(f"{'TOTAL':<55} {total}")

print("\n" + "=" * 70)
print(f"TOTAL V3 CLASSES: {len(all_classes)}")
print("=" * 70)

if len(all_classes) != 54:
    print(
        f"\nWARNING: Expected 54 classes, "
        f"but found {len(all_classes)}."
    )
else:
    print("\nSUCCESS: V3 contains exactly 54 classes.")

print(f"\nV3 location:\n{V3_DIR}")