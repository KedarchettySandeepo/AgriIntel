"""
AgriIntel - Safe Model Training Script for YOLO v5 Classifier
Trains on dataset/classification_v5_curated with 87 classes across 22 crops.
Designed for NVIDIA GeForce RTX 3050 Laptop GPU (4 GB VRAM) with mixed precision.
"""

import sys
import argparse
from pathlib import Path

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

import torch
from ultralytics import YOLO

DATASET_PATH = Path("dataset/classification_v5_curated")
BASELINE_CHECKPOINT = Path(r"runs\classify\runs\classify\crop_disease_classifier_v4-2\weights\best.pt")
OUTPUT_PROJECT = Path("runs/classify")
OUTPUT_NAME = "crop_disease_classifier_v5"


def train_v5(epochs=25, batch_size=32, imgsz=224, workers=2, device="0", resume=False):
    print("=" * 65)
    print("      🌱 AGRIINTEL - YOLO V5 CLASSIFIER TRAINING")
    print("=" * 65)

    if not DATASET_PATH.exists():
        print(f"Error: Curated dataset '{DATASET_PATH}' does not exist.")
        print("Please run: python prepare_v5_dataset.py first.")
        sys.exit(1)

    # Verify CUDA availability
    cuda_available = torch.cuda.is_available()
    device_name = torch.cuda.get_device_name(0) if cuda_available else "CPU"
    print(f"Compute Device: {device_name} (Requested: {device})")
    print(f"Dataset Path:   {DATASET_PATH.resolve()}")
    print(f"Image Size:     {imgsz}x{imgsz}")
    print(f"Batch Size:     {batch_size} (tuned for 4 GB VRAM)")
    print(f"Epochs:         {epochs}")
    print(f"Output Target:  {OUTPUT_PROJECT / OUTPUT_NAME}")
    print("-" * 65)

    # Initialize model: Start from YOLOv8n-cls pretrained weights for fine-tuning
    print("[Training] Initializing YOLO classification model...")
    model = YOLO("yolov8n-cls.pt")

    # Launch training with automatic mixed precision (AMP) to preserve VRAM
    results = model.train(
        data=str(DATASET_PATH.resolve()),
        epochs=epochs,
        imgsz=imgsz,
        batch=batch_size,
        workers=workers,
        device=device if cuda_available else "cpu",
        project=str(OUTPUT_PROJECT),
        name=OUTPUT_NAME,
        exist_ok=True,
        amp=True,
        patience=5,
        save=True,
        verbose=True
    )

    print("\n" + "=" * 65)
    print("  ✓ TRAINING COMPLETE")
    print(f"  Weights saved to: {OUTPUT_PROJECT / OUTPUT_NAME / 'weights' / 'best.pt'}")
    print("=" * 65)
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train AgriIntel v5 Crop Disease Classifier")
    parser.add_argument("--epochs", type=int, default=25, help="Number of training epochs")
    parser.add_argument("--batch", type=int, default=32, help="Batch size (default: 32 for 4GB VRAM)")
    parser.add_argument("--imgsz", type=int, default=224, help="Input image dimension (default: 224)")
    parser.add_argument("--device", type=str, default="0", help="CUDA device index or 'cpu'")
    parser.add_argument("--workers", type=int, default=2, help="DataLoader workers")

    args = parser.parse_args()
    train_v5(
        epochs=args.epochs,
        batch_size=args.batch,
        imgsz=args.imgsz,
        workers=args.workers,
        device=args.device
    )
