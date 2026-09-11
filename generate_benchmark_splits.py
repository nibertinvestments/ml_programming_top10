from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SPLIT_DIR = ROOT / "benchmark_splits"
SPLIT_DIR.mkdir(exist_ok=True)

DEFAULT_INPUTS = [
    ROOT / "task_corpus_10k" / "task_corpus_10k.jsonl",
    ROOT / "bugfix_corpus" / "bugfix_corpus.jsonl",
]


def load_records(paths):
    records = []
    for path in paths:
        if path.exists():
            with path.open("r", encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if line:
                        records.append(json.loads(line))
    return records


def make_splits(records):
    random.seed(42)
    records = list(records)
    random.shuffle(records)

    total = len(records)
    train_count = int(total * 0.7)
    val_count = int(total * 0.15)
    test_count = total - train_count - val_count

    train = records[:train_count]
    val = records[train_count:train_count + val_count]
    test = records[train_count + val_count:]

    for name, subset in [("train", train), ("validation", val), ("test", test)]:
        path = SPLIT_DIR / f"{name}.jsonl"
        with path.open("w", encoding="utf-8") as fh:
            for item in subset:
                fh.write(json.dumps(item, ensure_ascii=False) + "\n")

    manifest = {
        "title": "Benchmark train-validation-test split",
        "record_count": total,
        "train_count": len(train),
        "validation_count": len(val),
        "test_count": test_count,
        "split_strategy": "fixed_seed_random_shuffle_70_15_15",
        "seed": 42,
        "generated_from": [str(path) for path in DEFAULT_INPUTS if path.exists()],
    }
    (SPLIT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return train, val, test


if __name__ == "__main__":
    records = load_records(DEFAULT_INPUTS)
    if not records:
        raise FileNotFoundError("No records were found. Generate at least one corpus before creating benchmark splits.")

    train, val, test = make_splits(records)
    print(f"Generated {len(train)} train, {len(val)} validation, and {len(test)} test records.")
    print(f"Output folder: {SPLIT_DIR}")
