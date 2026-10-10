"""
AgriIntel - Safe & Reproducible Multi-Crop YOLO Classification Training (v5)
Fine-tunes YOLO11n-cls on dataset/classification_v5_curated across 87 classes.
Hardware optimized for:
  - Local GPU: NVIDIA GeForce RTX 3050 Laptop GPU (4 GB VRAM, batch=32, AMP=True)
  - Cloud GPU: NVIDIA T4 / A10G / V100 / A100 (batch=64/128, workers=8)
"""

import sys
import argparse
from pathlib import Path

# Fix console encoding on Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

import torch
from ultralytics import YOLO

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DATASET = BASE_DIR / "dataset" / "classification_v5_curated"
PRETRAINED_WEIGHTS = BASE_DIR / "yolo11n-cls.pt"
OUTPUT_PROJECT = BASE_DIR / "runs" / "classify"
OUTPUT_NAME = "crop_disease_classifier_v5"


def train_classifier(
    data_path: Path,
    epochs: int = 15,
    batch_size: int = 32,
    imgsz: int = 224,
    workers: int = 2,
    device: str = "0",
    patience: int = 5,
    seed: int = 42,
    resume: bool = False,
    name: str = OUTPUT_NAME,
    fraction: float = 1.0,
):
    print("=" * 70)
    print("      🌱 AGRIINTEL - MULTI-CROP CLASSIFIER TRAINING (v5)")
    print("=" * 70)

    if not data_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at: {data_path}\n"
            "Please run: python prepare_v5_pipeline.py first."
        )

    # CUDA Hardware Detection & Diagnostics
    cuda_available = torch.cuda.is_available()
    if cuda_available and device != "cpu":
        dev_idx = 0 if device == "0" else int(device)
        gpu_name = torch.cuda.get_device_name(dev_idx)
        vram_gb = torch.cuda.get_device_properties(dev_idx).total_memory / (1024 ** 3)
        print(f"Device:         CUDA ({gpu_name}) - Total VRAM: {vram_gb:.2f} GB")
        use_amp = True
        actual_device = device
    else:
        print("Device:         CPU (Warning: training on CPU will be slower)")
        use_amp = False
        actual_device = "cpu"

    print(f"Dataset Path:   {data_path.resolve()}")
    print(f"Pretrained:     {PRETRAINED_WEIGHTS.resolve()}")
    print(f"Image Size:     {imgsz}x{imgsz}")
    print(f"Batch Size:     {batch_size} (Tuned for VRAM stability)")
    print(f"Epochs:         {epochs} (Early stopping patience: {patience})")
    print(f"Workers:        {workers}")
    print(f"Dataset Frac:   {fraction * 100:.1f}%")
    print(f"Random Seed:    {seed}")
    print(f"Output Target:  {OUTPUT_PROJECT / name}")
    print("-" * 70)

    # Initialize model from pretrained weights for transfer learning
    if resume:
        ckpt_path = OUTPUT_PROJECT / name / "weights" / "last.pt"
        if not ckpt_path.exists():
            raise FileNotFoundError(f"Cannot resume: Checkpoint not found at {ckpt_path}")
        print(f"[Training] Resuming from checkpoint: {ckpt_path}")
        model = YOLO(str(ckpt_path))
    else:
        print(f"[Training] Loading pretrained YOLO11n-cls weights: {PRETRAINED_WEIGHTS}")
        model = YOLO(str(PRETRAINED_WEIGHTS))

    # Launch Ultralytics classifier training
    results = model.train(
        data=str(data_path.resolve()),
        epochs=epochs,
        imgsz=imgsz,
        batch=batch_size,
        workers=workers,
        device=actual_device,
        project=str(OUTPUT_PROJECT),
        name=name,
        exist_ok=True,
        amp=use_amp,
        patience=patience,
        save=True,
        save_period=-1,
        seed=seed,
        deterministic=True,
        verbose=True,
        fraction=fraction,
        resume=resume,
    )

    best_weight = OUTPUT_PROJECT / name / "weights" / "best.pt"
    print("\n" + "=" * 70)
    print("      ✓ TRAINING COMPLETE")
    print(f"  Best Model Checkpoint: {best_weight}")
    print("=" * 70)
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AgriIntel v5 Model Training")
    parser.add_argument("--data", type=str, default=str(DEFAULT_DATASET), help="Path to classification dataset")
    parser.add_argument("--epochs", type=int, default=15, help="Number of epochs (default: 15)")
    parser.add_argument("--batch", type=int, default=32, help="Batch size (default: 32 for RTX 3050 4GB)")
    parser.add_argument("--imgsz", type=int, default=224, help="Image resolution dimension")
    parser.add_argument("--workers", type=int, default=2, help="DataLoader workers (default: 2 for Windows stability)")
    parser.add_argument("--device", type=str, default="0", help="CUDA device index or 'cpu'")
    parser.add_argument("--patience", type=int, default=5, help="Early stopping patience")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility")
    parser.add_argument("--resume", action="store_true", help="Resume training from last.pt")
    parser.add_argument("--name", type=str, default=OUTPUT_NAME, help="Run name directory")
    parser.add_argument("--sanity-check", action="store_true", help="Run 1-epoch sanity check with small fraction")
    parser.add_argument("--cloud-profile", action="store_true", help="Use cloud GPU profile (batch 64, workers 8)")

    args = parser.parse_args()

    batch_size = args.batch
    workers = args.workers
    epochs = args.epochs
    fraction = 1.0
    run_name = args.name

    if args.cloud_profile:
        batch_size = 64
        workers = 8
        print("[Profile] Cloud GPU profile activated: batch=64, workers=8")

    if args.sanity_check:
        epochs = 1
        fraction = 0.05
        run_name = "crop_disease_classifier_sanity_check"
        print("[Sanity Check] Running 1-epoch verification job on 5% dataset fraction...")

    train_classifier(
        data_path=Path(args.data),
        epochs=epochs,
        batch_size=batch_size,
        imgsz=args.imgsz,
        workers=workers,
        device=args.device,
        patience=args.patience,
        seed=args.seed,
        resume=args.resume,
        name=run_name,
        fraction=fraction,
    )
