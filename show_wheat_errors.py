from pathlib import Path
import csv
import shutil

CSV_FILE = Path("v3_test_detailed_results.csv")
TEST_DIR = Path("dataset/classification_v3/test")
OUTPUT_DIR = Path("wheat_errors")

OUTPUT_DIR.mkdir(exist_ok=True)

with open(CSV_FILE, encoding="utf-8") as f:
    reader = csv.DictReader(f)

    count = 0

    for row in reader:

        true_class = row["true_class"]
        predicted_class = row["predicted_class"]

        if not true_class.startswith("Wheat___"):
            continue

        if true_class == predicted_class:
            continue

        image_name = row["image"]

        source = TEST_DIR / true_class / image_name

        if not source.exists():
            continue

        # Make a folder based on actual -> predicted
        folder_name = (
            true_class.replace("Wheat___", "")
            + "_TO_"
            + predicted_class.replace("Wheat___", "")
        )

        destination_dir = OUTPUT_DIR / folder_name
        destination_dir.mkdir(parents=True, exist_ok=True)

        destination = destination_dir / image_name

        shutil.copy2(source, destination)

        count += 1

print(f"Copied {count} Wheat error images.")
print(f"Location: {OUTPUT_DIR.resolve()}")