from pathlib import Path
from ultralytics import YOLO
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import csv
from collections import Counter


# ============================================================
# AI CROP DISEASE DETECTOR - EXTERNAL TEST V2
# ============================================================

print("=" * 70)
print("        AI CROP DISEASE DETECTOR - EXTERNAL TEST V2")
print("=" * 70)


# ------------------------------------------------------------
# MODEL PATH
# ------------------------------------------------------------

MODEL_PATH = Path(
    r"runs\classify\runs\crop_disease_classifier_v2-6\weights\best.pt"
)


if not MODEL_PATH.exists():
    print("\n❌ MODEL NOT FOUND")
    print("Expected:")
    print(MODEL_PATH)
    input("\nPress Enter to exit...")
    raise SystemExit


# ------------------------------------------------------------
# LOAD MODEL
# ------------------------------------------------------------

print("\nLoading V2 model...")

model = YOLO(str(MODEL_PATH))

print("✅ Model loaded successfully.")
print(f"Total classes: {len(model.names)}")


# ------------------------------------------------------------
# IMAGE FOLDER SELECTION
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("SELECT EXTERNAL TEST IMAGE FOLDER")
print("=" * 70)

print("""
Put NEW images that were NOT used during training/testing
inside a folder.

Recommended structure:

external_test/
    Apple/
        image1.jpg
        image2.jpg
    Paddy/
        image1.jpg
        image2.jpg
    Tomato/
        image1.jpg
        image2.jpg
    Corn/
        image1.jpg
        image2.jpg

You can also simply select one folder containing images.
""")


root = tk.Tk()
root.withdraw()

folder = filedialog.askdirectory(
    title="Select External Test Image Folder"
)

root.destroy()


if not folder:
    print("\n❌ No folder selected.")
    input("\nPress Enter to exit...")
    raise SystemExit


folder_path = Path(folder)

print("\nSelected folder:")
print(folder_path)


# ------------------------------------------------------------
# FIND IMAGES
# ------------------------------------------------------------

extensions = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp"
}

image_files = [
    p for p in folder_path.rglob("*")
    if p.is_file() and p.suffix.lower() in extensions
]

image_files.sort()


if not image_files:
    print("\n❌ No images found.")
    input("\nPress Enter to exit...")
    raise SystemExit


print(f"\nImages found: {len(image_files)}")


# ------------------------------------------------------------
# RESULTS
# ------------------------------------------------------------

results_data = []

prediction_counter = Counter()


# ------------------------------------------------------------
# PROCESS IMAGES
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("RUNNING EXTERNAL TEST")
print("=" * 70)

for index, image_path in enumerate(image_files, start=1):

    try:

        result = model.predict(
            source=str(image_path),
            verbose=False
        )[0]

        probs = result.probs

        top1_index = int(probs.top1)

        confidence = float(probs.top1conf)

        class_name = model.names[top1_index]

        # --------------------------------------------
        # Split crop and condition
        # --------------------------------------------

        if "___" in class_name:

            crop, condition = class_name.split("___", 1)

        else:

            crop = class_name
            condition = "Unknown"

        # --------------------------------------------
        # Ground truth from folder name
        # --------------------------------------------

        relative_parts = image_path.relative_to(
            folder_path
        ).parts

        if len(relative_parts) > 1:
            actual_crop = relative_parts[0]
        else:
            actual_crop = "Unknown"

        # --------------------------------------------
        # Crop comparison
        # --------------------------------------------

        crop_match = False

        if actual_crop != "Unknown":

            actual_clean = actual_crop.lower().replace(
                "_", " "
            )

            predicted_clean = crop.lower().replace(
                "_", " "
            )

            # Paddy / Rice treated as same crop
            if (
                ("paddy" in actual_clean or "rice" in actual_clean)
                and
                ("paddy" in predicted_clean or "rice" in predicted_clean)
            ):
                crop_match = True

            elif actual_clean in predicted_clean or predicted_clean in actual_clean:
                crop_match = True

        prediction_counter[class_name] += 1

        results_data.append({
            "Image": str(image_path),
            "Actual Crop": actual_crop,
            "Predicted Crop": crop,
            "Condition": condition,
            "Confidence": round(confidence * 100, 2),
            "Crop Match": crop_match
        })

        print(
            f"[{index:4}/{len(image_files)}] "
            f"{image_path.name:35} -> "
            f"{crop} | {condition} | "
            f"{confidence * 100:.2f}%"
        )

    except Exception as e:

        print(
            f"[{index:4}/{len(image_files)}] "
            f"❌ {image_path.name} -> {e}"
        )


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

total = len(results_data)

crop_matches = sum(
    1 for r in results_data
    if r["Crop Match"]
)

if total > 0:
    crop_accuracy = crop_matches / total * 100
else:
    crop_accuracy = 0


print("\n" + "=" * 70)
print("EXTERNAL TEST RESULTS")
print("=" * 70)

print(f"\nTotal images tested : {total}")

print(
    f"Crop recognition    : "
    f"{crop_accuracy:.2f}%"
)


# ------------------------------------------------------------
# PREDICTION DISTRIBUTION
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("PREDICTION DISTRIBUTION")
print("=" * 70)

for class_name, count in prediction_counter.most_common():

    print(
        f"{class_name:55} : {count}"
    )


# ------------------------------------------------------------
# SAVE CSV
# ------------------------------------------------------------

output_file = Path("external_test_results.csv")

with open(
    output_file,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "Image",
            "Actual Crop",
            "Predicted Crop",
            "Condition",
            "Confidence",
            "Crop Match"
        ]
    )

    writer.writeheader()

    writer.writerows(results_data)


# ------------------------------------------------------------
# FINAL INFORMATION
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("RESULTS SAVED")
print("=" * 70)

print(f"\nCSV file:")
print(output_file.resolve())

print("\nExternal testing completed.")

input("\nPress Enter to exit...")