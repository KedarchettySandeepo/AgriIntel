from pathlib import Path
import pandas as pd
import shutil

# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

RAW_DIR = BASE_DIR / "dataset" / "raw"
IMAGE_DIR = RAW_DIR / "wfd_extracted" / "wfd_dataset"

ANNOTATION_FILE = RAW_DIR / "wfd_data.csv"
TRAIN_FILE = RAW_DIR / "wfd_train.csv"
VALID_FILE = RAW_DIR / "wfd_valid.csv"
TEST_FILE = RAW_DIR / "wfd_test.csv"

OUTPUT_DIR = BASE_DIR / "dataset" / "wheat_v3"

# ============================================================
# LABEL MAPPING
# ============================================================

LABEL_MAP = {
    "healthy": "Wheat___healthy",
    "leaf_rust": "Wheat___leaf_rust",
    "stem_rust": "Wheat___stem_rust",
    "yellow_rust": "Wheat___yellow_rust",
    "powdery_mildew": "Wheat___powdery_mildew",
    "septoria": "Wheat___septoria",
}

DISEASE_COLUMNS = list(LABEL_MAP.keys())

# ============================================================
# CHECK FILES
# ============================================================

required_files = [
    ANNOTATION_FILE,
    TRAIN_FILE,
    VALID_FILE,
    TEST_FILE,
]

for file in required_files:
    if not file.exists():
        raise FileNotFoundError(f"Missing file: {file}")

if not IMAGE_DIR.exists():
    raise FileNotFoundError(f"Image directory not found: {IMAGE_DIR}")

print("=" * 70)
print("WHEAT V3 DATASET PREPARATION")
print("=" * 70)

# ============================================================
# LOAD ANNOTATIONS
# ============================================================

annotations = pd.read_csv(ANNOTATION_FILE)

print(f"\nTotal annotation records: {len(annotations)}")

print("\nAnnotation columns:")
print(list(annotations.columns))

# ============================================================
# LOAD OFFICIAL SPLITS
# ============================================================

train_df = pd.read_csv(TRAIN_FILE)
valid_df = pd.read_csv(VALID_FILE)
test_df = pd.read_csv(TEST_FILE)

print(f"\nOfficial split sizes:")
print(f"Train:      {len(train_df)}")
print(f"Validation: {len(valid_df)}")
print(f"Test:       {len(test_df)}")

# ============================================================
# NORMALIZE IMAGE NAMES
# ============================================================

def normalize_name(name):
    """
    WFD annotation sometimes contains source prefixes such as:
    Orlova_0000000001ffffff.jpg

    The actual extracted image is:
    0000000001ffffff.jpg

    Therefore we use the final 16-character hexadecimal ID.
    """

    name = Path(str(name)).name

    if "_" in name:
        parts = name.split("_")

        # If final part looks like an image filename,
        # use the final component.
        candidate = parts[-1]

        if candidate.lower().endswith(".jpg"):
            return candidate

    return name


annotations["image_name"] = annotations["img"].apply(normalize_name)

# ============================================================
# FIND ACTUAL IMAGE FILES
# ============================================================

image_files = {
    p.name: p
    for p in IMAGE_DIR.rglob("*.jpg")
}

print(f"\nImages found on disk: {len(image_files)}")

# ============================================================
# CHECK LABELS
# ============================================================

annotations["label_count"] = annotations[DISEASE_COLUMNS].sum(axis=1)

# Images containing only one disease/healthy label
single_label = annotations[
    annotations["label_count"] == 1
].copy()

# Images with multiple labels
multi_label = annotations[
    annotations["label_count"] > 1
].copy()

# Images without one of our six target labels
zero_target = annotations[
    annotations["label_count"] == 0
].copy()

print("\nAnnotation filtering:")
print(f"Total images:              {len(annotations)}")
print(f"Single-label images:       {len(single_label)}")
print(f"Multi-label images:        {len(multi_label)}")
print(f"No target label:           {len(zero_target)}")

# ============================================================
# DETERMINE CLASS
# ============================================================

def get_class(row):
    active = [
        col
        for col in DISEASE_COLUMNS
        if int(row[col]) == 1
    ]

    if len(active) != 1:
        return None

    return LABEL_MAP[active[0]]


single_label["class_name"] = single_label.apply(
    get_class,
    axis=1
)

# ============================================================
# REMOVE RECORDS WITHOUT MATCHING IMAGE
# ============================================================

single_label["image_path"] = single_label["image_name"].map(
    image_files
)

missing_images = single_label[
    single_label["image_path"].isna()
]

print(f"\nSingle-label records with missing images: {len(missing_images)}")

single_label = single_label[
    single_label["image_path"].notna()
].copy()

# ============================================================
# CREATE SPLIT LOOKUP
# ============================================================

def build_split_lookup(df):
    result = set()

    for name in df["img"]:
        result.add(normalize_name(name))

    return result


train_names = build_split_lookup(train_df)
valid_names = build_split_lookup(valid_df)
test_names = build_split_lookup(test_df)

print("\nOfficial split records:")
print(f"Train: {len(train_names)}")
print(f"Valid: {len(valid_names)}")
print(f"Test:  {len(test_names)}")

# ============================================================
# CREATE OUTPUT DIRECTORIES
# ============================================================

if OUTPUT_DIR.exists():
    print("\nRemoving previous Wheat V3 dataset...")
    shutil.rmtree(OUTPUT_DIR)

for split in ["train", "val", "test"]:
    for class_name in LABEL_MAP.values():
        (OUTPUT_DIR / split / class_name).mkdir(
            parents=True,
            exist_ok=True
        )

# ============================================================
# COPY FUNCTION
# ============================================================

stats = {
    "train": {},
    "val": {},
    "test": {},
}

def copy_records(records, split):
    copied = 0
    skipped = 0

    for _, row in records.iterrows():

        image_name = row["image_name"]
        source = image_files.get(image_name)

        if source is None:
            skipped += 1
            continue

        class_name = row["class_name"]

        if not class_name:
            skipped += 1
            continue

        destination_dir = (
            OUTPUT_DIR
            / split
            / class_name
        )

        destination = destination_dir / image_name

        shutil.copy2(source, destination)

        stats[split][class_name] = (
            stats[split].get(class_name, 0) + 1
        )

        copied += 1

    return copied, skipped


# ============================================================
# SPLIT DATA
# ============================================================

train_records = single_label[
    single_label["image_name"].isin(train_names)
]

valid_records = single_label[
    single_label["image_name"].isin(valid_names)
]

test_records = single_label[
    single_label["image_name"].isin(test_names)
]

print("\nFiltered records:")
print(f"Train: {len(train_records)}")
print(f"Valid: {len(valid_records)}")
print(f"Test:  {len(test_records)}")

# ============================================================
# COPY
# ============================================================

train_copied, train_skipped = copy_records(
    train_records,
    "train"
)

valid_copied, valid_skipped = copy_records(
    valid_records,
    "val"
)

test_copied, test_skipped = copy_records(
    test_records,
    "test"
)

# ============================================================
# PRINT RESULTS
# ============================================================

print("\n" + "=" * 70)
print("WHEAT V3 DATASET CREATED")
print("=" * 70)

print(f"\nTrain images copied:      {train_copied}")
print(f"Validation images copied: {valid_copied}")
print(f"Test images copied:       {test_copied}")

print("\nSkipped:")
print(f"Train: {train_skipped}")
print(f"Valid: {valid_skipped}")
print(f"Test:  {test_skipped}")

print("\nClass distribution:")

for split in ["train", "val", "test"]:

    print(f"\n{split.upper()}")

    total = 0

    for class_name in LABEL_MAP.values():

        count = stats[split].get(class_name, 0)

        print(
            f"{class_name:<35} {count}"
        )

        total += count

    print(f"{'TOTAL':<35} {total}")

print("\nOutput directory:")
print(OUTPUT_DIR)

print("\nDone.")