from ultralytics import YOLO
from pathlib import Path
from collections import defaultdict
import numpy as np

# ============================================================
# AI CROP DISEASE DETECTOR - MODEL V2 EVALUATION
# ============================================================

MODEL_PATH = r"runs\classify\runs\crop_disease_classifier_v2-6\weights\best.pt"
TEST_DIR = r"dataset\classification_v2\test"

print("=" * 70)
print("AI CROP DISEASE DETECTOR - MODEL V2 EVALUATION")
print("=" * 70)

# ------------------------------------------------------------
# Load model
# ------------------------------------------------------------

print("\nLoading model...")

model = YOLO(MODEL_PATH)

print("Model loaded successfully.")
print(f"Total classes: {len(model.names)}")

# ------------------------------------------------------------
# Collect test images
# ------------------------------------------------------------

test_path = Path(TEST_DIR)

if not test_path.exists():
    print("\nERROR: Test dataset not found:")
    print(TEST_DIR)
    raise SystemExit

image_extensions = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp"
}

images = []

for class_dir in sorted(test_path.iterdir()):

    if not class_dir.is_dir():
        continue

    for image_file in class_dir.iterdir():

        if image_file.suffix.lower() in image_extensions:

            images.append(
                (
                    image_file,
                    class_dir.name
                )
            )

print(f"\nTest images found: {len(images)}")

# ------------------------------------------------------------
# Create class mapping
# ------------------------------------------------------------

class_to_index = {}

for index, class_name in model.names.items():
    class_to_index[class_name] = index

# ------------------------------------------------------------
# Evaluation variables
# ------------------------------------------------------------

correct_top1 = 0
correct_top5 = 0

class_total = defaultdict(int)
class_correct = defaultdict(int)

paddy_total = 0
paddy_correct = 0

# ------------------------------------------------------------
# Predict
# ------------------------------------------------------------

print("\nStarting evaluation...")
print("This may take some time.\n")

for count, (image_path, true_class) in enumerate(images, start=1):

    # Skip classes that aren't in model
    if true_class not in class_to_index:
        print(
            f"WARNING: Class not found in model: {true_class}"
        )
        continue

    true_index = class_to_index[true_class]

    results = model.predict(
        source=str(image_path),
        verbose=False
    )

    probs = results[0].probs

    top1_index = int(probs.top1)

    top5_indices = probs.top5

    # -------------------------------
    # Top-1
    # -------------------------------

    is_top1_correct = (
        top1_index == true_index
    )

    if is_top1_correct:
        correct_top1 += 1
        class_correct[true_class] += 1

    # -------------------------------
    # Top-5
    # -------------------------------

    if true_index in top5_indices:
        correct_top5 += 1

    class_total[true_class] += 1

    # -------------------------------
    # Paddy
    # -------------------------------

    if true_class.startswith("Paddy___"):

        paddy_total += 1

        if is_top1_correct:
            paddy_correct += 1

    # -------------------------------
    # Progress
    # -------------------------------

    if count % 250 == 0 or count == len(images):

        top1_so_far = (
            correct_top1 / count * 100
        )

        top5_so_far = (
            correct_top5 / count * 100
        )

        print(
            f"Processed {count}/{len(images)} "
            f"| Top-1: {top1_so_far:.2f}% "
            f"| Top-5: {top5_so_far:.2f}%"
        )

# ------------------------------------------------------------
# Overall results
# ------------------------------------------------------------

total_evaluated = sum(class_total.values())

overall_top1 = (
    correct_top1 / total_evaluated * 100
)

overall_top5 = (
    correct_top5 / total_evaluated * 100
)

# ------------------------------------------------------------
# Paddy results
# ------------------------------------------------------------

if paddy_total > 0:

    paddy_accuracy = (
        paddy_correct / paddy_total * 100
    )

else:

    paddy_accuracy = 0

# ------------------------------------------------------------
# Print overall results
# ------------------------------------------------------------

print("\n")
print("=" * 70)
print("FINAL MODEL V2 RESULTS")
print("=" * 70)

print(
    f"\nTotal test images : {total_evaluated}"
)

print(
    f"Top-1 Accuracy    : {overall_top1:.2f}%"
)

print(
    f"Top-5 Accuracy    : {overall_top5:.2f}%"
)

print(
    f"Paddy Test Images : {paddy_total}"
)

print(
    f"Paddy Accuracy    : {paddy_accuracy:.2f}%"
)

# ------------------------------------------------------------
# Per-class accuracy
# ------------------------------------------------------------

print("\n")
print("=" * 70)
print("PER-CLASS ACCURACY")
print("=" * 70)

results_by_crop = defaultdict(list)

for class_name in sorted(class_total):

    total = class_total[class_name]
    correct = class_correct[class_name]

    accuracy = (
        correct / total * 100
    )

    crop = (
        class_name.split("___")[0]
        if "___" in class_name
        else class_name
    )

    results_by_crop[crop].append(
        (
            class_name,
            total,
            correct,
            accuracy
        )
    )

for crop in sorted(results_by_crop):

    print(f"\n--- {crop} ---")

    for (
        class_name,
        total,
        correct,
        accuracy
    ) in results_by_crop[crop]:

        condition = (
            class_name.split("___", 1)[1]
            if "___" in class_name
            else class_name
        )

        print(
            f"{condition:55s} "
            f"{correct:4d}/{total:4d} "
            f"{accuracy:6.2f}%"
        )

# ------------------------------------------------------------
# Save results to text file
# ------------------------------------------------------------

output_file = "v2_evaluation_results.txt"

with open(output_file, "w", encoding="utf-8") as f:

    f.write("AI CROP DISEASE DETECTOR - MODEL V2\n")
    f.write("=" * 60 + "\n\n")

    f.write(
        f"Total test images: {total_evaluated}\n"
    )

    f.write(
        f"Top-1 Accuracy: {overall_top1:.2f}%\n"
    )

    f.write(
        f"Top-5 Accuracy: {overall_top5:.2f}%\n"
    )

    f.write(
        f"Paddy Test Images: {paddy_total}\n"
    )

    f.write(
        f"Paddy Accuracy: {paddy_accuracy:.2f}%\n\n"
    )

    f.write("PER-CLASS ACCURACY\n")
    f.write("=" * 60 + "\n\n")

    for crop in sorted(results_by_crop):

        f.write(f"\n--- {crop} ---\n")

        for (
            class_name,
            total,
            correct,
            accuracy
        ) in results_by_crop[crop]:

            f.write(
                f"{class_name}: "
                f"{correct}/{total} "
                f"({accuracy:.2f}%)\n"
            )

print("\n")
print("=" * 70)
print(f"Results saved to: {output_file}")
print("=" * 70)

print("\nEvaluation complete.")
