from pathlib import Path
import random
import shutil

# --------------------------------------------------
# PATHS
# --------------------------------------------------

BASE = Path(__file__).resolve().parent

SOURCE = BASE / "dataset" / "raw" / "extracted" / "raw" / "segmented"

OUTPUT = BASE / "dataset" / "classification"

TRAIN = OUTPUT / "train"
VAL = OUTPUT / "val"
TEST = OUTPUT / "test"

# --------------------------------------------------
# SETTINGS
# --------------------------------------------------

TRAIN_RATIO = 0.80
VAL_RATIO = 0.10
TEST_RATIO = 0.10

random.seed(42)

# --------------------------------------------------
# CHECK SOURCE
# --------------------------------------------------

if not SOURCE.exists():
    print("ERROR: Source dataset not found.")
    print(SOURCE)
    raise SystemExit

print("Source dataset:")
print(SOURCE)
print()

# --------------------------------------------------
# FIND CLASS FOLDERS
# --------------------------------------------------

classes = sorted([
    folder for folder in SOURCE.iterdir()
    if folder.is_dir()
])

if not classes:
    print("ERROR: No class folders found.")
    raise SystemExit

print(f"Classes found: {len(classes)}")
print()

# --------------------------------------------------
# CREATE OUTPUT FOLDERS
# --------------------------------------------------

for folder in [TRAIN, VAL, TEST]:
    folder.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# PROCESS EACH CLASS
# --------------------------------------------------

total_images = 0

for class_folder in classes:

    class_name = class_folder.name

    images = [
        file for file in class_folder.iterdir()
        if file.is_file()
        and file.suffix.lower() in [".jpg", ".jpeg", ".png"]
    ]

    if not images:
        print(f"Skipping empty class: {class_name}")
        continue

    random.shuffle(images)

    total = len(images)

    train_count = int(total * TRAIN_RATIO)
    val_count = int(total * VAL_RATIO)

    train_images = images[:train_count]
    val_images = images[train_count:train_count + val_count]
    test_images = images[train_count + val_count:]

    # Create class folders
    train_class = TRAIN / class_name
    val_class = VAL / class_name
    test_class = TEST / class_name

    train_class.mkdir(parents=True, exist_ok=True)
    val_class.mkdir(parents=True, exist_ok=True)
    test_class.mkdir(parents=True, exist_ok=True)

    # Copy images
    for image in train_images:
        shutil.copy2(image, train_class / image.name)

    for image in val_images:
        shutil.copy2(image, val_class / image.name)

    for image in test_images:
        shutil.copy2(image, test_class / image.name)

    total_images += total

    print(
        f"{class_name}: "
        f"{len(train_images)} train | "
        f"{len(val_images)} val | "
        f"{len(test_images)} test"
    )

# --------------------------------------------------
# FINISHED
# --------------------------------------------------

print()
print("=" * 60)
print("DATASET PREPARATION COMPLETED")
print("=" * 60)

print(f"Classes       : {len(classes)}")
print(f"Total images  : {total_images}")

print()
print("Training data:")
print(TRAIN)

print()
print("Validation data:")
print(VAL)

print()
print("Testing data:")
print(TEST)

print()
print("Next step:")
print("Train YOLO classification model.")