from ultralytics import YOLO
from tkinter import Tk, filedialog
from PIL import Image
from pathlib import Path


# ============================================================
# AI CROP DISEASE DETECTOR
# MODEL V2 - 48 CLASSES
# ============================================================

MODEL_PATH = Path(
    r"runs\classify\runs\crop_disease_classifier_v2-6\weights\best.pt"
)


# ============================================================
# Helper Functions
# ============================================================

def get_crop_name(class_name):
    """
    Extract crop name from:
    Crop___Disease
    """

    if "___" in class_name:
        return class_name.split("___")[0]

    return class_name


def get_readable_name(class_name):
    """
    Convert technical YOLO class names into readable names.
    """

    if "___" not in class_name:
        return class_name, ""

    crop, condition = class_name.split("___", 1)

    # Crop formatting
    crop = crop.replace("_", " ")

    # Condition formatting
    condition = condition.replace("_", " ")

    # Special formatting
    crop = crop.replace(
        "(including sour)",
        "(including sour)"
    )

    return crop, condition


# ============================================================
# Check Model
# ============================================================

print()
print("=" * 60)
print("              AI CROP DISEASE DETECTOR")
print("=" * 60)

print("\nModel path:")
print(MODEL_PATH)

if not MODEL_PATH.exists():

    print("\n❌ ERROR: Model V2 was not found.")

    print("\nExpected model:")
    print(MODEL_PATH)

    print("\nPlease check that this file exists:")
    print(
        r"runs\classify\runs\crop_disease_classifier_v2-6\weights\best.pt"
    )

    input("\nPress Enter to exit...")
    raise SystemExit


# ============================================================
# Load Model
# ============================================================

print("\nLoading Model V2...")

model = YOLO(str(MODEL_PATH))

print("✅ Model loaded successfully.")

print(f"\nTotal classes: {len(model.names)}")


# ============================================================
# Display Classes
# ============================================================

print("\nModel classes:")
print("-" * 60)

for index, class_name in model.names.items():

    print(
        f"{index:02d} : {class_name}"
    )


# ============================================================
# Select Image
# ============================================================

print("\n")
print("=" * 60)
print("SELECT CROP IMAGE")
print("=" * 60)

root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select Crop Image",
    filetypes=[
        (
            "Image files",
            "*.jpg *.jpeg *.png *.bmp *.webp"
        ),
        (
            "All files",
            "*.*"
        )
    ]
)

root.destroy()


# ============================================================
# Check Selection
# ============================================================

if not image_path:

    print("\n❌ No image selected.")

    input("\nPress Enter to exit...")
    raise SystemExit


# ============================================================
# Open Image
# ============================================================

try:

    image = Image.open(image_path)

except Exception as e:

    print("\n❌ Could not open image.")
    print("Error:", e)

    input("\nPress Enter to exit...")
    raise SystemExit


print("\nSelected image:")
print(image_path)

print(
    f"Image size: {image.size[0]} x {image.size[1]}"
)


# ============================================================
# Run Prediction
# ============================================================

print("\nRunning AI prediction...")

try:

    results = model.predict(
        source=image,
        verbose=False
    )

except Exception as e:

    print("\n❌ Prediction failed.")
    print("Error:", e)

    input("\nPress Enter to exit...")
    raise SystemExit


result = results[0]

probs = result.probs


# ============================================================
# Get Top Prediction
# ============================================================

top1_index = int(probs.top1)

top1_confidence = float(
    probs.top1conf
)

top1_class = model.names[top1_index]

crop_name, condition = get_readable_name(
    top1_class
)


# ============================================================
# Main Prediction Result
# ============================================================

print()
print("=" * 60)
print("                PREDICTION RESULT")
print("=" * 60)

print(
    f"\n🌱 Crop       : {crop_name}"
)

print(
    f"🦠 Condition  : {condition}"
)

print(
    f"🎯 Confidence : {top1_confidence * 100:.2f}%"
)


# ============================================================
# Confidence Level
# ============================================================

if top1_confidence >= 0.80:

    confidence_level = "HIGH"

elif top1_confidence >= 0.50:

    confidence_level = "MODERATE"

else:

    confidence_level = "LOW"


print(
    f"📊 Confidence Level : {confidence_level}"
)


# ============================================================
# Same-Crop Top Predictions
# ============================================================

print()
print("=" * 60)
print("          TOP 5 PREDICTIONS FOR THIS CROP")
print("=" * 60)


probabilities = (
    probs.data.cpu().numpy()
)


predictions = []


for index, probability in enumerate(
    probabilities
):

    class_name = model.names[index]

    predicted_crop = get_crop_name(
        class_name
    )

    # Only show predictions belonging
    # to the detected crop

    if (
        predicted_crop.lower()
        == crop_name.lower()
    ):

        predictions.append(
            (
                class_name,
                float(probability)
            )
        )


# Sort by confidence

predictions.sort(
    key=lambda item: item[1],
    reverse=True
)


# Display top 5

for position, (
    class_name,
    probability
) in enumerate(
    predictions[:5],
    start=1
):

    crop, readable_condition = (
        get_readable_name(class_name)
    )

    print(
        f"{position}. "
        f"{crop} - "
        f"{readable_condition} "
        f"({probability * 100:.2f}%)"
    )


# ============================================================
# Paddy-Specific Message
# ============================================================

if crop_name.lower() == "paddy":

    print()
    print("=" * 60)
    print("                 🌾 PADDY DETECTED")
    print("=" * 60)

    print(
        "\nModel V2 contains 10 dedicated "
        "Paddy/Rice classes."
    )

    print(
        "The image is being classified using "
        "the Paddy classes."
    )

    print(
        "\nPaddy classes supported:"
    )

    paddy_classes = []

    for index, class_name in model.names.items():

        if class_name.startswith(
            "Paddy___"
        ):

            condition_name = (
                class_name.split(
                    "___",
                    1
                )[1]
            )

            condition_name = (
                condition_name.replace(
                    "_",
                    " "
                )
            )

            paddy_classes.append(
                condition_name
            )

    for condition_name in paddy_classes:

        print(
            f"  • {condition_name}"
        )


# ============================================================
# Final Information
# ============================================================

print()
print("=" * 60)
print("MODEL INFORMATION")
print("=" * 60)

print(
    "\nModel       : YOLO V2"
)

print(
    "Classes     : 48"
)

print(
    "Test images : 6507"
)

print(
    "Top-1 test accuracy : 99.12%"
)

print(
    "Top-5 test accuracy : 99.94%"
)

print(
    "Paddy test accuracy : 96.66%"
)


# ============================================================
# Finish
# ============================================================

print()
print("=" * 60)
print("             Prediction complete.")
print("=" * 60)

input("\nPress Enter to exit...")