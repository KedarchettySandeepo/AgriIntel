import os
import json
import struct
import subprocess
import sys

PARQUET_FILES = [
    r"dataset\raw\paddy_download\train-00000-of-00002.parquet",
    r"dataset\raw\paddy_download\train-00001-of-00002.parquet",
]

OUTPUT_DIR = r"dataset\raw\paddy"

print("=" * 60)
print("PADDY DATASET EXTRACTION")
print("=" * 60)

# Check files
for file in PARQUET_FILES:
    if not os.path.exists(file):
        print(f"ERROR: File not found:")
        print(file)
        sys.exit(1)

print("\nBoth Parquet files found.")

# We need pyarrow for reading Parquet.
try:
    import pyarrow.parquet as pq
except ImportError:
    print("\nPyArrow is not installed.")
    print("Installing pyarrow...")
    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        "pyarrow"
    ])
    import pyarrow.parquet as pq

print("PyArrow is ready.")

os.makedirs(OUTPUT_DIR, exist_ok=True)

total = 0

for parquet_file in PARQUET_FILES:

    print("\nReading:")
    print(parquet_file)

    table = pq.read_table(parquet_file)

    print("Rows:", table.num_rows)
    print("Columns:", table.column_names)

    # Convert columns to Python objects
    columns = table.column_names

    image_column = None
    label_column = None

    for col in columns:
        if col.lower() == "image":
            image_column = col

        if col.lower() == "label":
            label_column = col

    if image_column is None or label_column is None:
        print("\nERROR: Could not find image/label columns.")
        print("Available columns:", columns)
        sys.exit(1)

    images = table[image_column]
    labels = table[label_column]

    for i in range(table.num_rows):

        image_data = images[i].as_py()
        label = labels[i].as_py()

        # Image column is normally a dictionary:
        # {"bytes": ..., "path": ...}
        if isinstance(image_data, dict):
            image_bytes = image_data.get("bytes")
            image_path = image_data.get("path")
        else:
            image_bytes = None
            image_path = None

        # Convert label number to readable class
        label_names = {
            0: "bacterial_leaf_blight",
            1: "bacterial_leaf_streak",
            2: "bacterial_panicle_blight",
            3: "blast",
            4: "brown_spot",
            5: "dead_heart",
            6: "downy_mildew",
            7: "hispa",
            8: "normal",
            9: "tungro",
        }

        class_name = label_names.get(
            label,
            f"class_{label}"
        )

        folder_name = f"Paddy___{class_name}"

        class_dir = os.path.join(
            OUTPUT_DIR,
            folder_name
        )

        os.makedirs(class_dir, exist_ok=True)

        # Determine extension
        extension = ".jpg"

        if image_path:
            ext = os.path.splitext(image_path)[1]
            if ext:
                extension = ext

        filename = f"paddy_{total:05d}{extension}"

        output_file = os.path.join(
            class_dir,
            filename
        )

        if image_bytes:
            with open(output_file, "wb") as f:
                f.write(image_bytes)

        total += 1

        if total % 500 == 0:
            print(f"Extracted {total} images...")

print("\n" + "=" * 60)
print("EXTRACTION COMPLETE")
print("=" * 60)
print(f"Total images extracted: {total}")
print(f"Output folder: {OUTPUT_DIR}")

print("\nClasses created:")

for folder in sorted(os.listdir(OUTPUT_DIR)):
    folder_path = os.path.join(OUTPUT_DIR, folder)

    if os.path.isdir(folder_path):
        count = len([
            f for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
        ])

        print(f"{folder}: {count} images")