from pathlib import Path
from collections import defaultdict
from ultralytics import YOLO
from PIL import Image
import csv

# =========================
# CONFIG
# =========================

MODEL_PATH = Path(
    "runs/classify/runs/classify/crop_disease_classifier_v4-2/weights/best.pt"
)

TEST_DIR = Path("dataset/classification_v3/test")

OUTPUT_CSV = Path("v3_test_detailed_results.csv")

# =========================
# LOAD MODEL
# =========================

print("Loading V3 model...")
model = YOLO(str(MODEL_PATH))

# =========================
# STORAGE
# =========================

class_total = defaultdict(int)
class_correct = defaultdict(int)

crop_total = defaultdict(int)
crop_correct = defaultdict(int)

all_results = []

total = 0
correct = 0

# =========================
# EVALUATE
# =========================

print("\nEvaluating V3 test dataset...\n")

for class_dir in sorted(TEST_DIR.iterdir()):

    if not class_dir.is_dir():
        continue

    true_class = class_dir.name
    crop = true_class.split("___")[0]

    images = list(class_dir.glob("*"))

    print(f"{true_class}: {len(images)} images")

    for image_path in images:

        try:
            result = model.predict(
                source=str(image_path),
                verbose=False
            )[0]

            predicted_index = int(result.probs.top1)
            confidence = float(result.probs.top1conf)

            predicted_class = model.names[predicted_index]

            is_correct = predicted_class == true_class

            total += 1

            if is_correct:
                correct += 1

            class_total[true_class] += 1

            if is_correct:
                class_correct[true_class] += 1

            crop_total[crop] += 1

            if is_correct:
                crop_correct[crop] += 1

            all_results.append({
                "image": image_path.name,
                "true_class": true_class,
                "predicted_class": predicted_class,
                "confidence": confidence,
                "correct": is_correct
            })

        except Exception as e:
            print(f"ERROR: {image_path} -> {e}")

# =========================
# OVERALL
# =========================

overall_accuracy = correct / total if total else 0

print("\n" + "=" * 70)
print("V3 TEST RESULTS")
print("=" * 70)

print(f"Total images : {total}")
print(f"Correct      : {correct}")
print(f"Incorrect    : {total - correct}")
print(f"Top-1        : {overall_accuracy * 100:.2f}%")

# =========================
# CROP RESULTS
# =========================

print("\n" + "=" * 70)
print("CROP-LEVEL ACCURACY")
print("=" * 70)

for crop in sorted(crop_total):

    acc = crop_correct[crop] / crop_total[crop] * 100

    print(
        f"{crop:20s} "
        f"{crop_correct[crop]:5d}/{crop_total[crop]:5d} "
        f"{acc:7.2f}%"
    )

# =========================
# CLASS RESULTS
# =========================

print("\n" + "=" * 70)
print("CLASS-LEVEL ACCURACY")
print("=" * 70)

class_accuracy = {}

for cls in sorted(class_total):

    acc = class_correct[cls] / class_total[cls] * 100

    class_accuracy[cls] = acc

    print(
        f"{cls:60s} "
        f"{class_correct[cls]:4d}/{class_total[cls]:4d} "
        f"{acc:7.2f}%"
    )

# =========================
# WHEAT
# =========================

print("\n" + "=" * 70)
print("WHEAT RESULTS")
print("=" * 70)

wheat_total = 0
wheat_correct = 0

for cls in sorted(class_total):

    if cls.startswith("Wheat___"):

        wheat_total += class_total[cls]
        wheat_correct += class_correct[cls]

        print(
            f"{cls.replace('Wheat___', ''):25s} "
            f"{class_correct[cls]:4d}/{class_total[cls]:4d} "
            f"{class_accuracy[cls]:7.2f}%"
        )

wheat_accuracy = wheat_correct / wheat_total * 100

print(
    f"\nWheat overall: "
    f"{wheat_correct}/{wheat_total} "
    f"= {wheat_accuracy:.2f}%"
)

# =========================
# PADDY
# =========================

print("\n" + "=" * 70)
print("PADDY RESULTS")
print("=" * 70)

paddy_total = 0
paddy_correct = 0

for cls in sorted(class_total):

    if cls.startswith("Paddy___"):

        paddy_total += class_total[cls]
        paddy_correct += class_correct[cls]

        print(
            f"{cls.replace('Paddy___', ''):30s} "
            f"{class_correct[cls]:4d}/{class_total[cls]:4d} "
            f"{class_accuracy[cls]:7.2f}%"
        )

paddy_accuracy = paddy_correct / paddy_total * 100

print(
    f"\nPaddy overall: "
    f"{paddy_correct}/{paddy_total} "
    f"= {paddy_accuracy:.2f}%"
)

# =========================
# WEAKEST CLASSES
# =========================

print("\n" + "=" * 70)
print("LOWEST ACCURACY CLASSES")
print("=" * 70)

for cls, acc in sorted(class_accuracy.items(), key=lambda x: x[1])[:10]:

    print(
        f"{cls:60s} {acc:7.2f}%"
    )

# =========================
# SAVE CSV
# =========================

with open(
    OUTPUT_CSV,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.DictWriter(
        f,
        fieldnames=[
            "image",
            "true_class",
            "predicted_class",
            "confidence",
            "correct"
        ]
    )

    writer.writeheader()
    writer.writerows(all_results)

print("\nDetailed results saved to:")
print(OUTPUT_CSV.resolve())

print("\nEvaluation complete.")
