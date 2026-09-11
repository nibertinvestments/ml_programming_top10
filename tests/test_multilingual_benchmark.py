import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "generate_multilingual_benchmark.py"


def load_benchmark_module():
    spec = importlib.util.spec_from_file_location("generate_multilingual_benchmark", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_multilingual_benchmark_generates_expected_outputs():
    module = load_benchmark_module()

    assert len(module.LANGUAGES) == 10
    assert len(module.CATEGORIES) >= 15
    assert len(module.records) > 1000

    assert (module.OUTPUT_DIR / "multilingual_benchmark.csv").exists()
    assert (module.OUTPUT_DIR / "multilingual_benchmark.jsonl").exists()

    for split_name in ("train", "validation", "test"):
        assert (module.OUTPUT_DIR / f"{split_name}.csv").exists()
        assert (module.OUTPUT_DIR / f"{split_name}.jsonl").exists()

    manifest = json.loads((module.OUTPUT_DIR / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["record_count"] == len(module.records)
    assert manifest["train_count"] + manifest["validation_count"] + manifest["test_count"] == manifest["record_count"]
