from ultralytics import YOLO
from tkinter import Tk, filedialog
from PIL import Image
import os


# ============================================================
# AI CROP DISEASE DETECTOR - MODEL V2
# 48 Classes
# ============================================================

MODEL_PATH = r"runs\classify\runs\crop_disease_classifier_v2-6\weights\best.pt"


# ============================================================
# Helper functions
# ============================================================

def get_crop_name(class_name):
    """Extract crop name from YOLO class name."""
    if "___" in class_name:
        return class_name.split("___")[0]

    return class_name


def get_readable_name(class_name):
    """Convert technical class name into readable text."""

    if "___" in class_name:
        crop, condition = class_name.split("___", 1)

        crop = crop.replace("_", " ")
        condition = condition.replace("_", " ")

        return crop, condition

    return class_name, ""


# ============================================================
# Check model
# ============================================================

if not os.path.exists(MODEL_PATH):

    print("=" * 60)
    print("MODEL V2 NOT FOUND")
    print("=" * 60)

    print("\nExpected model:")
    print(MODEL_PATH)

    print("\nTraining may still be running.")
    print("Run this program after Model V2 training finishes.")

    input("\nPress Enter to exit...")
    raise SystemExit


# ============================================================
# Load model
# ============================================================

print("=" * 60)
print("AI CROP DISEASE DETECTOR - MODEL V2")
print("=" * 60)

print("\nLoading model...")

model = YOLO(MODEL_PATH)

print("Model loaded successfully.")

print(f"\nTotal classes: {len(model.names)}")

print("\nClasses:")

for index, name in model.names.items():
    print(f"{index:02d} : {name}")


# ============================================================
# Select image
# ============================================================

root = Tk()
root.withdraw()

print("\nSelect a crop image...")

image_path = filedialog.askopenfilename(
    title="Select Crop Image",
    filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.bmp *.webp"),
        ("All files", "*.*")
    ]
)

root.destroy()


if not image_path:

    print("\nNo image selected.")
    input("Press Enter to exit...")
    raise SystemExit


# ============================================================
# Open image
# ============================================================

image = Image.open(image_path)

print("\nSelected image:")
print(image_path)

print(f"Image size: {image.size}")


# ============================================================
# Prediction
# ============================================================

print("\nRunning AI prediction...")

results = model.predict(
    source=image,
    verbose=False
)

result = results[0]

probs = result.probs


# ============================================================
# Top prediction
# ============================================================

top1_index = int(probs.top1)

top1_confidence = float(probs.top1conf)

top1_class = model.names[top1_index]

crop_name, condition = get_readable_name(top1_class)


# ============================================================
# Main result
# ============================================================

print("\n")
print("=" * 60)
print("PREDICTION RESULT")
print("=" * 60)

print(f"\n🌱 Crop       : {crop_name}")

print(f"🦠 Condition  : {condition}")

print(f"🎯 Confidence : {top1_confidence * 100:.2f}%")


# ============================================================
# Confidence interpretation
# ============================================================

if top1_confidence >= 0.80:

    confidence_level = "HIGH"

elif top1_confidence >= 0.50:

    confidence_level = "MODERATE"

else:

    confidence_level = "LOW"


print(f"📊 Confidence Level : {confidence_level}")


# ============================================================
# Same-crop predictions
# ============================================================

print("\n")
print("=" * 60)
print("TOP 5 PREDICTIONS FOR THIS CROP")
print("=" * 60)


# Get all probabilities

probabilities = probs.data.cpu().numpy()

predictions = []

for index, probability in enumerate(probabilities):

    class_name = model.names[index]

    predicted_crop = get_crop_name(class_name)

    if predicted_crop.lower() == crop_name.lower():

        predictions.append(
            (
                class_name,
                float(probability)
            )
        )


# Sort highest probability first

predictions.sort(
    key=lambda x: x[1],
    reverse=True
)


# Display top 5

for position, (class_name, probability) in enumerate(
    predictions[:5],
    start=1
):

    crop, readable_condition = get_readable_name(
        class_name
    )

    print(
        f"{position}. "
        f"{crop} - {readable_condition} "
        f"({probability * 100:.2f}%)"
    )


# ============================================================
# Paddy detection message
# ============================================================

if crop_name.lower() == "paddy":

    print("\n")
    print("=" * 60)
    print("🌾 PADDY DETECTED")
    print("=" * 60)

    print(
        "The V2 model contains dedicated Paddy/Rice classes."
    )

    print(
        "This image is being classified using the Paddy "
        "classes rather than being forced into Corn."
    )


# ============================================================
# Finish
# ============================================================

print("\n")
print("=" * 60)
print("Prediction complete.")
print("=" * 60)

input("\nPress Enter to exit...")