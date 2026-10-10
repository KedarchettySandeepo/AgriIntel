from pathlib import Path
import shutil
import random

# ============================================================
# CONFIG
# ============================================================

SOURCE = Path("dataset/classification_v3")
OUTPUT = Path("dataset/classification_v4")

TARGET_WHEAT_COUNT = 400

WHEAT_CLASSES = [
    "Wheat___healthy",
    "Wheat___leaf_rust",
    "Wheat___powdery_mildew",
    "Wheat___septoria",
    "Wheat___stem_rust",
    "Wheat___yellow_rust",
]

random.seed(42)

# ============================================================
# CLEAN OLD V4 IF IT EXISTS
# ============================================================

if OUTPUT.exists():
    print("Removing existing V4 dataset...")
    shutil.rmtree(OUTPUT)

# ============================================================
# COPY V3 DATASET
# ============================================================

print("Creating V4 from V3...")

for split in ["train", "val", "test"]:

    source_split = SOURCE / split
    output_split = OUTPUT / split

    for class_dir in sorted(source_split.iterdir()):

        if not class_dir.is_dir():
            continue

        destination_class = output_split / class_dir.name
        destination_class.mkdir(parents=True, exist_ok=True)

        images = [
            p for p in class_dir.iterdir()
            if p.is_file()
        ]

        # Copy original images
        for image in images:
            shutil.copy2(
                image,
                destination_class / image.name
            )

# ============================================================
# BALANCE WHEAT TRAINING CLASSES
# ============================================================

print("\nBalancing Wheat training classes...")

train_dir = OUTPUT / "train"

for class_name in WHEAT_CLASSES:

    class_dir = train_dir / class_name

    images = [
        p for p in class_dir.iterdir()
        if p.is_file()
    ]

    original_count = len(images)

    print(
        f"{class_name}: "
        f"{original_count} -> ",
        end=""
    )

    if original_count >= TARGET_WHEAT_COUNT:
        print(f"{original_count} (unchanged)")
        continue

    needed = TARGET_WHEAT_COUNT - original_count

    for i in range(needed):

        source_image = random.choice(images)

        new_name = (
            f"oversampled_{i:04d}_"
            f"{source_image.name}"
        )

        destination = class_dir / new_name

        shutil.copy2(
            source_image,
            destination
        )

    final_count = len([
        p for p in class_dir.iterdir()
        if p.is_file()
    ])

    print(final_count)

# ============================================================
# DATASET SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("V4 DATASET SUMMARY")
print("=" * 60)

for split in ["train", "val", "test"]:

    split_dir = OUTPUT / split

    total = 0
    classes = 0

    for class_dir in sorted(split_dir.iterdir()):

        if not class_dir.is_dir():
            continue

        count = len([
            p for p in class_dir.iterdir()
            if p.is_file()
        ])

        total += count
        classes += 1

    print(
        f"{split:5s}: "
        f"{total:6d} images | "
        f"{classes} classes"
    )

print("\nV4 dataset created successfully.")
print(f"Location: {OUTPUT.resolve()}")