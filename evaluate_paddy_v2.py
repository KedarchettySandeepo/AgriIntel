from pathlib import Path
from collections import defaultdict
import csv

import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO


# ============================================================
# AI CROP DISEASE DETECTOR - PADDY V2 EVALUATION
# ============================================================

print("=" * 75)
print("AI CROP DISEASE DETECTOR - PADDY V2 EVALUATION")
print("=" * 75)


# ============================================================
# PATHS
# ============================================================

MODEL_PATH = Path(
    r"runs\classify\runs\crop_disease_classifier_v2-6\weights\best.pt"
)

PADDY_DATASET = Path(
    r"dataset\raw\paddy"
)

RESULTS_CSV = Path("paddy_v2_evaluation_results.csv")
CONFUSION_MATRIX = Path("paddy_confusion_matrix.png")


# ============================================================
# CHECK PATHS
# ============================================================

if not MODEL_PATH.exists():
    print("\n❌ MODEL NOT FOUND")
    print(f"Expected: {MODEL_PATH}")
    raise SystemExit

if not PADDY_DATASET.exists():
    print("\n❌ PADDY DATASET NOT FOUND")
    print(f"Expected: {PADDY_DATASET}")
    raise SystemExit


# ============================================================
# LOAD MODEL
# ============================================================

print("\nLoading model...")

model = YOLO(str(MODEL_PATH))

print("✅ Model loaded successfully.")

# Model classes
model_names = model.names

if isinstance(model_names, list):
    model_names = {
        i: name for i, name in enumerate(model_names)
    }

print(f"\nTotal model classes: {len(model_names)}")


# ============================================================
# FIND PADDY CLASSES
# ============================================================

paddy_model_classes = {}

for class_id, class_name in model_names.items():

    if str(class_name).startswith("Paddy___"):
        condition = str(class_name).split("___", 1)[1]
        paddy_model_classes[condition] = class_id


print("\nPaddy classes in model:")
print("-" * 75)

for condition, class_id in sorted(
    paddy_model_classes.items(),
    key=lambda x: x[1]
):
    print(f"{class_id:02d} : Paddy___{condition}")


print(f"\nTotal Paddy classes: {len(paddy_model_classes)}")


# ============================================================
# FIND DATASET FOLDERS
# ============================================================

dataset_folders = sorted(
    [
        folder
        for folder in PADDY_DATASET.iterdir()
        if folder.is_dir()
    ]
)

print("\nPaddy dataset folders:")
print("-" * 75)

for folder in dataset_folders:
    print(f"📁 {folder.name}")


# ============================================================
# IMAGE EXTENSIONS
# ============================================================

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp"
}


# ============================================================
# COLLECT IMAGES
# ============================================================

samples = []

for folder in dataset_folders:

    folder_name = folder.name

    if "___" not in folder_name:
        print(
            f"\n⚠️ Skipping folder with unexpected name: "
            f"{folder_name}"
        )
        continue

    crop, condition = folder_name.split("___", 1)

    if crop.lower() != "paddy":
        continue

    for image_path in folder.rglob("*"):

        if image_path.suffix.lower() in IMAGE_EXTENSIONS:

            samples.append(
                {
                    "image": image_path,
                    "actual": condition,
                    "folder": folder_name
                }
            )


print("\n" + "=" * 75)
print("DATASET SUMMARY")
print("=" * 75)

print(f"Total Paddy images: {len(samples)}")


# ============================================================
# CLASS COUNTS
# ============================================================

actual_counts = defaultdict(int)

for sample in samples:
    actual_counts[sample["actual"]] += 1


print("\nImages per class:")
print("-" * 75)

for condition in sorted(actual_counts):
    print(
        f"{condition:<35} : "
        f"{actual_counts[condition]}"
    )


# ============================================================
# EVALUATION
# ============================================================

print("\n" + "=" * 75)
print("STARTING PADDY EVALUATION")
print("=" * 75)

print("\nThis may take some time...\n")


correct = 0
total = len(samples)

results = []

confusion = defaultdict(lambda: defaultdict(int))

for index, sample in enumerate(samples, start=1):

    image_path = sample["image"]
    actual = sample["actual"]

    try:

        prediction = model.predict(
            source=str(image_path),
            verbose=False
        )[0]

        probs = prediction.probs

        predicted_class_id = int(probs.top1)

        predicted_full_name = str(
            model_names[predicted_class_id]
        )

        if "___" in predicted_full_name:
            predicted_crop, predicted_condition = (
                predicted_full_name.split("___", 1)
            )
        else:
            predicted_crop = "Unknown"
            predicted_condition = predicted_full_name

        confidence = float(probs.top1conf)

        is_correct = (
            predicted_crop.lower() == "paddy"
            and predicted_condition == actual
        )

        if is_correct:
            correct += 1

        confusion[actual][predicted_condition] += 1

        results.append(
            {
                "image": str(image_path),
                "actual": actual,
                "predicted": predicted_condition,
                "confidence": confidence * 100,
                "correct": is_correct
            }
        )

    except Exception as error:

        print(
            f"\n⚠️ Error processing:"
            f"\n{image_path}"
            f"\n{error}"
        )

    # Progress
    if index % 100 == 0 or index == total:

        accuracy = (
            correct / index * 100
            if index > 0
            else 0
        )

        print(
            f"Processed {index}/{total} | "
            f"Accuracy: {accuracy:.2f}%"
        )


# ============================================================
# FINAL ACCURACY
# ============================================================

overall_accuracy = (
    correct / total * 100
    if total > 0
    else 0
)


# ============================================================
# PER-CLASS ACCURACY
# ============================================================

per_class = {}

for condition in sorted(actual_counts):

    class_total = sum(
        confusion[condition].values()
    )

    class_correct = confusion[condition][condition]

    class_accuracy = (
        class_correct / class_total * 100
        if class_total > 0
        else 0
    )

    per_class[condition] = {
        "total": class_total,
        "correct": class_correct,
        "accuracy": class_accuracy
    }


# ============================================================
# PRINT FINAL RESULTS
# ============================================================

print("\n")
print("=" * 75)
print("FINAL PADDY V2 RESULTS")
print("=" * 75)

print(f"\nTotal Paddy images : {total}")
print(f"Correct predictions: {correct}")
print(f"Wrong predictions  : {total - correct}")
print(f"Paddy Accuracy     : {overall_accuracy:.2f}%")


print("\n")
print("=" * 75)
print("PER-CLASS ACCURACY")
print("=" * 75)

for condition, data in per_class.items():

    print(
        f"{condition:<35} "
        f"{data['correct']:>4}/{data['total']:<4} "
        f"{data['accuracy']:>7.2f}%"
    )


# ============================================================
# MISCLASSIFICATIONS
# ============================================================

wrong_predictions = [
    result
    for result in results
    if not result["correct"]
]

print("\n")
print("=" * 75)
print("MISCLASSIFICATIONS")
print("=" * 75)

print(
    f"\nTotal misclassified images: "
    f"{len(wrong_predictions)}"
)

if len(wrong_predictions) > 0:

    print("\nFirst 30 mistakes:")
    print("-" * 75)

    for result in wrong_predictions[:30]:

        print(
            f"\nActual    : {result['actual']}"
            f"\nPredicted : {result['predicted']}"
            f"\nConfidence: {result['confidence']:.2f}%"
            f"\nImage     : {result['image']}"
        )

else:

    print("\n🎉 No misclassified images!")


# ============================================================
# SAVE CSV
# ============================================================

with open(
    RESULTS_CSV,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "image",
            "actual",
            "predicted",
            "confidence",
            "correct"
        ]
    )

    writer.writeheader()

    writer.writerows(results)


print(
    f"\n📄 Detailed results saved to:"
    f"\n{RESULTS_CSV}"
)


# ============================================================
# CONFUSION MATRIX
# ============================================================

conditions = sorted(actual_counts.keys())

matrix = np.zeros(
    (len(conditions), len(conditions)),
    dtype=int
)

condition_to_index = {
    condition: index
    for index, condition in enumerate(conditions)
}


for actual in conditions:

    for predicted, count in confusion[actual].items():

        if predicted in condition_to_index:

            row = condition_to_index[actual]
            col = condition_to_index[predicted]

            matrix[row, col] = count


# ============================================================
# DRAW CONFUSION MATRIX
# ============================================================

fig_size = max(10, len(conditions) * 0.8)

plt.figure(
    figsize=(fig_size, fig_size)
)

plt.imshow(matrix)

plt.title(
    "Paddy Disease Classification - Confusion Matrix"
)

plt.xlabel("Predicted Class")
plt.ylabel("Actual Class")

plt.xticks(
    range(len(conditions)),
    conditions,
    rotation=90
)

plt.yticks(
    range(len(conditions)),
    conditions
)

# Add values
for i in range(len(conditions)):

    for j in range(len(conditions)):

        value = matrix[i, j]

        if value > 0:

            plt.text(
                j,
                i,
                str(value),
                ha="center",
                va="center"
            )


plt.colorbar()

plt.tight_layout()

plt.savefig(
    CONFUSION_MATRIX,
    dpi=200,
    bbox_inches="tight"
)

plt.close()


print(
    f"📊 Confusion matrix saved to:"
    f"\n{CONFUSION_MATRIX}"
)


# ============================================================
# TOP CONFUSION PAIRS
# ============================================================

confusion_pairs = []

for actual in conditions:

    for predicted in conditions:

        if actual != predicted:

            count = confusion[actual][predicted]

            if count > 0:

                confusion_pairs.append(
                    (
                        count,
                        actual,
                        predicted
                    )
                )


confusion_pairs.sort(
    reverse=True
)


print("\n")
print("=" * 75)
print("MOST COMMON MISCLASSIFICATIONS")
print("=" * 75)

if confusion_pairs:

    for count, actual, predicted in confusion_pairs[:10]:

        print(
            f"{actual} → {predicted} : "
            f"{count} images"
        )

else:

    print("\nNo confusion between classes.")


# ============================================================
# COMPLETE
# ============================================================

print("\n")
print("=" * 75)
print("PADDY EVALUATION COMPLETE")
print("=" * 75)

print(
    f"\nFinal Paddy Accuracy: "
    f"{overall_accuracy:.2f}%"
)

print("\nFiles generated:")

print(f"  📄 {RESULTS_CSV}")
print(f"  📊 {CONFUSION_MATRIX}")

print("\n")