from ultralytics import YOLO
import torch

print("=" * 70)
print("AI CROP DISEASE DETECTOR - MODEL V2")
print("=" * 70)

# ------------------------------------------------------------
# Check GPU
# ------------------------------------------------------------

if torch.cuda.is_available():
    device = 0
    print("\nGPU detected:")
    print(torch.cuda.get_device_name(0))
else:
    device = "cpu"
    print("\nWARNING: CUDA GPU not detected.")
    print("Training will use CPU.")

# ------------------------------------------------------------
# Load pretrained YOLO classification model
# ------------------------------------------------------------

model = YOLO("yolo11n-cls.pt")

print("\nStarting training...")
print("Classes: 48")
print("Dataset: dataset/classification_v2")

# ------------------------------------------------------------
# Train
# ------------------------------------------------------------

results = model.train(
    data="dataset/classification_v2",

    epochs=30,
    imgsz=224,
    batch=32,

    workers=0,

    project="runs",
    name="crop_disease_classifier_v2",

    pretrained=True,

    patience=7,

    device=device,

    verbose=True
)

print("\n" + "=" * 70)
print("MODEL V2 TRAINING COMPLETE")
print("=" * 70)

print("\nBest model should be here:")
print("runs/crop_disease_classifier_v2/weights/best.pt")