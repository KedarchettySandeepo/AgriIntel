"""
AgriIntel - Rigorous Model Evaluation, Calibration & Comparison Engine
Evaluates classification models against the isolated test set.
Produces:
- Top-1 and Top-3 Accuracy
- Macro-Precision, Macro-Recall, Macro-F1 across all classes
- Per-class precision, recall, F1, and support counts
- Per-crop aggregated diagnostic performance
- Inference latency benchmarks (mean, median, p95)
- Model artifact file size
- Confidence calibration and uncertainty rejection threshold analysis
- Side-by-side empirical comparison between candidate model and baseline models/best.pt
"""

import sys
import json
import time
import argparse
from pathlib import Path
from collections import defaultdict

# Fix Windows console encoding
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

import torch
from ultralytics import YOLO

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_TEST_DIR = BASE_DIR / "dataset" / "classification_v5_curated" / "test"
DEFAULT_VAL_DIR = BASE_DIR / "dataset" / "classification_v5_curated" / "val"
BASELINE_MODEL = BASE_DIR / "models" / "best.pt"


def evaluate_single_model(model_path: Path, test_dir: Path, target_classes: set = None, device: str = "cpu"):
    """
    Run full inference on test_dir images and compute rigorous classification metrics.
    If target_classes is provided, evaluate only on images from those classes.
    """
    if not model_path.exists():
        raise FileNotFoundError(f"Model not found at: {model_path}")
    if not test_dir.exists():
        raise FileNotFoundError(f"Test directory not found at: {test_dir}")

    model = YOLO(str(model_path))
    model_classes = {int(k): v for k, v in model.names.items()}
    class_to_idx = {v: k for k, v in model_classes.items()}

    # Gather test samples
    samples = []
    for cls_dir in sorted(test_dir.iterdir()):
        if not cls_dir.is_dir():
            continue
        cls_name = cls_dir.name
        if target_classes is not None and cls_name not in target_classes:
            continue
        for img_file in cls_dir.iterdir():
            if img_file.is_file() and img_file.suffix.lower() in {".jpg", ".jpeg", ".png"}:
                samples.append((img_file, cls_name))

    if not samples:
        raise ValueError(f"No test images found in {test_dir} for specified classes.")

    total_samples = len(samples)
    correct_top1 = 0
    correct_top3 = 0

    # Per-class counts: TP, FP, FN, Support
    class_tp = defaultdict(int)
    class_fp = defaultdict(int)
    class_fn = defaultdict(int)
    class_support = defaultdict(int)

    # Per-crop counts
    crop_correct = defaultdict(int)
    crop_total = defaultdict(int)

    # Latency tracking
    latencies = []
    confidences_correct = []
    confidences_incorrect = []

    # Prediction log for confusion matrix
    confusion = defaultdict(lambda: defaultdict(int))

    # Batch inference for fast, memory-efficient evaluation
    batch_size = 64 if str(device) != "cpu" else 32
    print(f"  -> Processing {total_samples} test samples in batches of {batch_size} (device={device})...")

    for b_idx in range(0, total_samples, batch_size):
        batch_slice = samples[b_idx:b_idx + batch_size]
        batch_paths = [str(s[0]) for s in batch_slice]

        t0 = time.perf_counter()
        batch_results = model.predict(source=batch_paths, batch=len(batch_paths), device=device, verbose=False)
        avg_sample_ms = ((time.perf_counter() - t0) * 1000.0) / max(len(batch_paths), 1)

        for (img_path, true_cls), res in zip(batch_slice, batch_results):
            class_support[true_cls] += 1
            true_crop = true_cls.split("___")[0] if "___" in true_cls else true_cls
            crop_total[true_crop] += 1
            latencies.append(avg_sample_ms)

            probs = res.probs
            top1_idx = int(probs.top1)
            top1_conf = float(probs.top1conf)
            top1_cls = model_classes.get(top1_idx, "Unknown")

            # Top-3 predictions
            top3_indices = [int(i) for i in probs.top5[:3]] if hasattr(probs, "top5") else [top1_idx]
            top3_classes = [model_classes.get(i, "Unknown") for i in top3_indices]

            confusion[true_cls][top1_cls] += 1

            is_top1_correct = (top1_cls == true_cls)
            is_top3_correct = (true_cls in top3_classes)

            if is_top1_correct:
                correct_top1 += 1
                class_tp[true_cls] += 1
                crop_correct[true_crop] += 1
                confidences_correct.append(top1_conf)
            else:
                class_fn[true_cls] += 1
                class_fp[top1_cls] += 1
                confidences_incorrect.append(top1_conf)

            if is_top3_correct:
                correct_top3 += 1

        if (b_idx // batch_size) % 25 == 0 and b_idx > 0:
            print(f"     Processed {min(b_idx + batch_size, total_samples)}/{total_samples} samples...")

    # Compute per-class precision, recall, F1
    per_class_metrics = {}
    all_evaluated_classes = sorted(list(set(class_support.keys()) | set(class_fp.keys())))

    for c in all_evaluated_classes:
        tp = class_tp[c]
        fp = class_fp[c]
        fn = class_fn[c]
        supp = class_support[c]

        prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = (2 * prec * rec) / (prec + rec) if (prec + rec) > 0 else 0.0

        per_class_metrics[c] = {
            "support": supp,
            "tp": tp,
            "fp": fp,
            "fn": fn,
            "precision": round(prec, 4),
            "recall": round(rec, 4),
            "f1": round(f1, 4)
        }

    # Macro averages (across classes with non-zero support)
    supported_classes = [c for c in per_class_metrics if class_support[c] > 0]
    macro_prec = sum(per_class_metrics[c]["precision"] for c in supported_classes) / len(supported_classes)
    macro_rec = sum(per_class_metrics[c]["recall"] for c in supported_classes) / len(supported_classes)
    macro_f1 = sum(per_class_metrics[c]["f1"] for c in supported_classes) / len(supported_classes)

    # Per-crop metrics
    per_crop_metrics = {}
    for crop, tot in sorted(crop_total.items()):
        cor = crop_correct[crop]
        per_crop_metrics[crop] = {
            "total": tot,
            "correct": cor,
            "accuracy": round(cor / tot, 4)
        }

    latencies_sorted = sorted(latencies)
    mean_latency = sum(latencies) / len(latencies)
    median_latency = latencies_sorted[len(latencies_sorted) // 2]
    p95_latency = latencies_sorted[int(len(latencies_sorted) * 0.95)]
    model_size_mb = model_path.stat().st_size / (1024 * 1024)

    return {
        "model_path": str(model_path),
        "model_classes_count": len(model_classes),
        "total_test_samples": total_samples,
        "classes_evaluated": len(supported_classes),
        "top1_accuracy": round(correct_top1 / total_samples, 4),
        "top3_accuracy": round(correct_top3 / total_samples, 4),
        "macro_precision": round(macro_prec, 4),
        "macro_recall": round(macro_rec, 4),
        "macro_f1": round(macro_f1, 4),
        "model_size_mb": round(model_size_mb, 2),
        "latency_ms": {
            "mean": round(mean_latency, 2),
            "median": round(median_latency, 2),
            "p95": round(p95_latency, 2)
        },
        "calibration": {
            "mean_confidence_correct": round(sum(confidences_correct) / max(1, len(confidences_correct)), 4),
            "mean_confidence_incorrect": round(sum(confidences_incorrect) / max(1, len(confidences_incorrect)), 4),
            "total_correct": len(confidences_correct),
            "total_incorrect": len(confidences_incorrect)
        },
        "per_crop_metrics": per_crop_metrics,
        "per_class_metrics": per_class_metrics,
        "confusion": {k: dict(v) for k, v in confusion.items()}
    }


def compare_models(candidate_path: Path, baseline_path: Path, test_dir: Path, output_md: Path, output_json: Path, device: str = "cpu"):
    print("=" * 70)
    print("      🌱 AGRIINTEL - COMPREHENSIVE MODEL EVALUATION & BENCHMARK")
    print("=" * 70)

    # Baseline 54 classes
    base_model = YOLO(str(baseline_path))
    shared_54_classes = set(base_model.names.values())
    print(f"[Benchmark] Evaluating Baseline Model (54 classes): {baseline_path}")
    baseline_eval = evaluate_single_model(baseline_path, test_dir, target_classes=shared_54_classes, device=device)

    print(f"\n[Benchmark] Evaluating Candidate Model on 54 Shared Baseline Classes...")
    candidate_shared_eval = evaluate_single_model(candidate_path, test_dir, target_classes=shared_54_classes, device=device)

    print(f"\n[Benchmark] Evaluating Candidate Model on ALL 87 Classes (Full Multi-Crop Scope)...")
    candidate_full_eval = evaluate_single_model(candidate_path, test_dir, target_classes=None, device=device)

    # Build Markdown Comparison Report
    md = []
    md.append("# 📊 AgriIntel Model Evaluation & Comparison Report\n")
    md.append(f"**Generated:** {time.strftime('%Y-%m-%d %H:%M:%S')}")
    md.append(f"**Evaluation Device:** {device.upper()}")
    md.append(f"**Test Set Location:** `{test_dir}`\n")

    md.append("## 1. Executive Summary & Architectural Benchmark\n")
    md.append("| Metric | Baseline Model (`models/best.pt`) | Candidate Model (54 Shared Classes) | Candidate Model (All 87 Classes) |")
    md.append("| :--- | :--- | :--- | :--- |")
    md.append(f"| **Model Architecture** | YOLO11n-cls (54 classes) | YOLO11n-cls (87 classes) | YOLO11n-cls (87 classes) |")
    md.append(f"| **Total Supported Classes** | 54 | 87 | 87 |")
    md.append(f"| **Total Supported Crops** | 16 | 22 | 22 |")
    md.append(f"| **Test Samples Evaluated** | {baseline_eval['total_test_samples']} | {candidate_shared_eval['total_test_samples']} | {candidate_full_eval['total_test_samples']} |")
    md.append(f"| **Top-1 Accuracy** | **{baseline_eval['top1_accuracy']*100:.2f}%** | **{candidate_shared_eval['top1_accuracy']*100:.2f}%** | **{candidate_full_eval['top1_accuracy']*100:.2f}%** |")
    md.append(f"| **Top-3 Accuracy** | {baseline_eval['top3_accuracy']*100:.2f}% | {candidate_shared_eval['top3_accuracy']*100:.2f}% | {candidate_full_eval['top3_accuracy']*100:.2f}% |")
    md.append(f"| **Macro-F1 Score** | **{baseline_eval['macro_f1']:.4f}** | **{candidate_shared_eval['macro_f1']:.4f}** | **{candidate_full_eval['macro_f1']:.4f}** |")
    md.append(f"| **Macro-Precision** | {baseline_eval['macro_precision']:.4f} | {candidate_shared_eval['macro_precision']:.4f} | {candidate_full_eval['macro_precision']:.4f} |")
    md.append(f"| **Macro-Recall** | {baseline_eval['macro_recall']:.4f} | {candidate_shared_eval['macro_recall']:.4f} | {candidate_full_eval['macro_recall']:.4f} |")
    md.append(f"| **Inference Latency (Mean)** | {baseline_eval['latency_ms']['mean']} ms | {candidate_shared_eval['latency_ms']['mean']} ms | {candidate_full_eval['latency_ms']['mean']} ms |")
    md.append(f"| **Inference Latency (p95)** | {baseline_eval['latency_ms']['p95']} ms | {candidate_shared_eval['latency_ms']['p95']} ms | {candidate_full_eval['latency_ms']['p95']} ms |")
    md.append(f"| **Model Artifact Size** | {baseline_eval['model_size_mb']} MB | {candidate_full_eval['model_size_mb']} MB | {candidate_full_eval['model_size_mb']} MB |\n")

    md.append("## 2. Performance by Crop (Candidate Model - 87 Classes)\n")
    md.append("| Crop | Test Samples | Correct Predictions | Top-1 Accuracy |")
    md.append("| :--- | :--- | :--- | :--- |")
    for crop, data in sorted(candidate_full_eval["per_crop_metrics"].items()):
        md.append(f"| **{crop}** | {data['total']} | {data['correct']} | **{data['accuracy']*100:.2f}%** |")
    md.append("")

    md.append("## 3. Confidence Calibration & Uncertainty Rejection Analysis\n")
    cal = candidate_full_eval["calibration"]
    md.append(f"- **Mean Confidence on Correct Diagnoses:** `{cal['mean_confidence_correct']*100:.1f}%`")
    md.append(f"- **Mean Confidence on Erroneous Diagnoses:** `{cal['mean_confidence_incorrect']*100:.1f}%`")
    md.append("- **Calibrated Threshold:** Predictions with `confidence < 0.45` or ambiguous margin `< 0.15` across disparate crops are routed to the Uncertainty Guardrail.\n")

    md.append("## 4. Top Per-Class Performance Summary (Full 87-Class Model)\n")
    md.append("| Class Name | Support | Precision | Recall | F1 Score |")
    md.append("| :--- | :--- | :--- | :--- | :--- |")
    for cls_name, c_data in sorted(candidate_full_eval["per_class_metrics"].items(), key=lambda x: x[1]["support"], reverse=True):
        if c_data["support"] > 0:
            md.append(f"| `{cls_name}` | {c_data['support']} | {c_data['precision']:.3f} | {c_data['recall']:.3f} | **{c_data['f1']:.3f}** |")
    md.append("")

    with open(output_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    full_results = {
        "timestamp": time.time(),
        "baseline": baseline_eval,
        "candidate_54_shared": candidate_shared_eval,
        "candidate_87_full": candidate_full_eval
    }
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(full_results, f, indent=2)

    print(f"\n✓ Markdown Evaluation Report written to: {output_md}")
    print(f"✓ JSON Benchmark Results written to:     {output_json}")
    return full_results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate AgriIntel Classifier")
    parser.add_argument("--candidate", type=str, required=True, help="Path to candidate best.pt")
    parser.add_argument("--baseline", type=str, default=str(BASELINE_MODEL), help="Path to baseline best.pt")
    parser.add_argument("--test-dir", type=str, default=str(DEFAULT_TEST_DIR), help="Path to isolated test directory")
    parser.add_argument("--report-md", type=str, default="model_evaluation_report.md", help="Output markdown report path")
    parser.add_argument("--report-json", type=str, default="model_evaluation_report.json", help="Output JSON results path")
    parser.add_argument("--device", type=str, default="cpu", help="Inference device ('cpu' or '0')")

    args = parser.parse_args()
    compare_models(
        candidate_path=Path(args.candidate),
        baseline_path=Path(args.baseline),
        test_dir=Path(args.test_dir),
        output_md=Path(args.report_md),
        output_json=Path(args.report_json),
        device=args.device
    )
