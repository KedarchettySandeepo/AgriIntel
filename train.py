from pathlib import Path
from ultralytics import YOLO
import multiprocessing


def main():

    # Project location
    BASE = Path(__file__).resolve().parent

    # Dataset location
    DATASET = BASE / "dataset" / "classification"

    print("=" * 60)
    print("AI CROP DISEASE DETECTOR")
    print("=" * 60)

    print(f"Dataset: {DATASET}")
    print("Classes: 38")
    print("Training started...")
    print()

    # Load YOLO classification model
    model = YOLO("yolo11n-cls.pt")

    # Train model
    results = model.train(
        data=str(DATASET),
        epochs=30,
        imgsz=224,
        batch=32,

        # Windows-safe setting
        workers=0,

        project=str(BASE / "runs"),
        name="crop_disease_classifier",

        pretrained=True,
        patience=5,

        # Use NVIDIA GPU
        device=0
    )

    print()
    print("=" * 60)
    print("TRAINING COMPLETED")
    print("=" * 60)

    print()
    print("Best model:")
    print(
        BASE
        / "runs"
        / "crop_disease_classifier"
        / "weights"
        / "best.pt"
    )


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()