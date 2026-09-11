from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CSV_PATH = ROOT / "large_training_corpus_v2" / "large_project_training_corpus.csv"
JSONL_PATH = ROOT / "large_training_corpus_v2" / "large_project_training_corpus.jsonl"
BUNDLE_DIR = ROOT / "project_bundles_v2"

assert CSV_PATH.exists(), f"Missing CSV: {CSV_PATH}"
assert JSONL_PATH.exists(), f"Missing JSONL: {JSONL_PATH}"
assert BUNDLE_DIR.exists(), f"Missing bundles folder: {BUNDLE_DIR}"

with CSV_PATH.open("r", encoding="utf-8", newline="") as csv_file:
    rows = list(csv.DictReader(csv_file))

assert len(rows) > 250, f"Expected more than 250 rows, got {len(rows)}"

language_counts = {}
for row in rows:
    language_counts[row["language"]] = language_counts.get(row["language"], 0) + 1
    assert row["valid"] in {"True", "False", "true", "false"} or row["valid"] is True
    assert row["text"].strip(), f"Empty text for {row['dataset_id']}"
    assert row["labels"].strip(), f"Missing labels for {row['dataset_id']}"

# JSONL validation
with JSONL_PATH.open("r", encoding="utf-8") as jsonl_file:
    jsonl_rows = [json.loads(line) for line in jsonl_file if line.strip()]

assert len(jsonl_rows) == len(rows), f"JSONL row count mismatch: {len(jsonl_rows)} vs {len(rows)}"

# Bundle validation
bundle_dirs = sorted(p for p in BUNDLE_DIR.iterdir() if p.is_dir())
assert len(bundle_dirs) == 10, f"Expected 10 bundles, found {len(bundle_dirs)}"
for bundle in bundle_dirs:
    required = ["README.md", "app", "helpers", "config", "data", "tests", "assembly_example.asm", "binary_example.txt"]
    for item in required:
        if item.endswith(".md") or item.endswith(".asm") or item.endswith(".txt"):
            assert (bundle / item).exists(), f"Missing {bundle / item}"
        else:
            assert (bundle / item).exists(), f"Missing bundle item {bundle / item}"

print(f"Validated {len(rows)} CSV records and {len(jsonl_rows)} JSONL records.")
print(f"Language counts: {language_counts}")
print(f"Bundle directories: {len(bundle_dirs)}")
