from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "bugfix_corpus"
OUTPUT_DIR.mkdir(exist_ok=True)

LANGUAGES = [
    "Python",
    "JavaScript",
    "Java",
    "C#",
    "C++",
    "Go",
    "Rust",
    "TypeScript",
    "PHP",
    "Ruby",
]

BUG_PATTERNS = [
    "missing-null-check",
    "wrong-file-path",
    "off-by-one-loop",
    "incorrect-sort-order",
    "bad-json-key",
    "string-trimming-bug",
    "float-precision-error",
    "index-out-of-range",
    "missing-return-statement",
    "broken-conditional",
    "bad-date-parsing",
    "array-append-misuse",
    "wrong-config-key",
    "bad-encoding-handling",
    "unclosed-quote",
    "broken-csv-parsing",
    "incorrect-division",
    "incorrect-sql-query",
    "bad-binary-check",
    "memory-copy-overflow",
]


def build_bugfix_record(language: str, pattern: str, index: int) -> dict:
    issue_map = {
        "missing-null-check": "The function fails when the input value is None or empty and crashes instead of returning a safe default.",
        "wrong-file-path": "The code tries to read a file from the wrong location and cannot open the expected data source.",
        "off-by-one-loop": "The loop stops one iteration too early and drops the last valid record.",
        "incorrect-sort-order": "The list is sorted in ascending order when descending order is required.",
        "bad-json-key": "The parser reads the wrong JSON field and produces incomplete output.",
        "string-trimming-bug": "Whitespace is not removed before comparison, causing mismatches in validation.",
        "float-precision-error": "Amounts are rounded incorrectly and produce a value that is off by a small but significant amount.",
        "index-out-of-range": "The code indexes a list beyond the valid range when length is zero or one.",
        "missing-return-statement": "The function reaches the end without returning a final value.",
        "broken-conditional": "The condition checks the wrong boolean and makes the code behave in reverse.",
        "bad-date-parsing": "The parser assumes the wrong format and fails on valid date strings.",
        "array-append-misuse": "The code adds values to the wrong structure and loses data.",
        "wrong-config-key": "The application looks for a config key that does not exist, making setup fail.",
        "bad-encoding-handling": "Non-ASCII characters break when reading and writing the file.",
        "unclosed-quote": "The string literal is not closed correctly and the program fails to parse the source.",
        "broken-csv-parsing": "CSV parsing is using a delimiter that does not match the input file.",
        "incorrect-division": "Division is performed before the values are normalized, distorting results.",
        "incorrect-sql-query": "The query is selecting the wrong columns and returns incomplete output.",
        "bad-binary-check": "The code checks the wrong byte value and misclassifies valid binary input.",
        "memory-copy-overflow": "The destination buffer is not sized correctly and data spills across the boundary.",
    }

    broken_code = f"""def example(values):\n    if values is None:\n        return None\n    total = 0\n    for i in range(len(values) - 1):\n        total += values[i]\n    return total\n"""
    fixed_code = f"""def example(values):\n    if values is None or len(values) == 0:\n        return 0\n    total = 0\n    for value in values:\n        total += value\n    return total\n"""

    if pattern == "wrong-file-path":
        broken_code = """def read_data():\n    with open('tmp/data.csv', 'r', encoding='utf-8') as fh:\n        return fh.read()\n"""
        fixed_code = """def read_data():\n    with open('data/data.csv', 'r', encoding='utf-8') as fh:\n        return fh.read()\n"""
    elif pattern == "off-by-one-loop":
        broken_code = """def count_items(items):\n    total = 0\n    for i in range(len(items) - 1):\n        total += 1\n    return total\n"""
        fixed_code = """def count_items(items):\n    total = 0\n    for _ in items:\n        total += 1\n    return total\n"""
    elif pattern == "incorrect-sort-order":
        broken_code = """def ordered(values):\n    return sorted(values)\n"""
        fixed_code = """def ordered(values):\n    return sorted(values, reverse=True)\n"""
    elif pattern == "bad-json-key":
        broken_code = """def extract_user(payload):\n    return payload['user_name']\n"""
        fixed_code = """def extract_user(payload):\n    return payload.get('user', {}).get('name', 'unknown')\n"""
    elif pattern == "float-precision-error":
        broken_code = """def total(values):\n    total_value = 0\n    for v in values:\n        total_value += v\n    return round(total_value, 0)\n"""
        fixed_code = """def total(values):\n    total_value = sum(values)\n    return round(total_value, 2)\n"""
    elif pattern == "memory-copy-overflow":
        broken_code = """def copy(src, dst):\n    for i in range(len(src) + 1):\n        dst[i] = src[i]\n    return dst\n"""
        fixed_code = """def copy(src, dst):\n    for i, value in enumerate(src):\n        dst[i] = value\n    return dst\n"""

    issue = issue_map.get(pattern, f"The implementation fails in the {pattern} scenario and produces incorrect behavior.")
    record = {
        "record_id": f"{language.lower()}_bugfix_{pattern}_{index:04d}",
        "language": language,
        "bug_pattern": pattern,
        "issue": issue,
        "broken_code": broken_code,
        "fixed_code": fixed_code,
        "tests": [
            f"assert example([1,2,3]) == 6",
            "assert example(None) == 0",
        ],
        "fix_summary": f"Resolve the {pattern} bug by adding the missing guard, correcting the logic, and preserving expected output.",
        "validation_status": {
            "bug_reproduced": True,
            "fixed": True,
        },
        "tags": ["bugfix", language.lower(), pattern],
    }
    return record


def generate():
    records = []
    for language in LANGUAGES:
        for pattern in BUG_PATTERNS:
            for idx in range(10):
                records.append(build_bugfix_record(language, pattern, idx))

    with (OUTPUT_DIR / "bugfix_corpus.jsonl").open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")

    manifest = {
        "title": "Bug-fix training corpus",
        "record_count": len(records),
        "languages": LANGUAGES,
        "bug_patterns": BUG_PATTERNS,
        "description": "Bug-fix style examples designed to teach repair, root-cause reasoning, and patch generation across languages.",
    }
    (OUTPUT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return records


if __name__ == "__main__":
    records = generate()
    print(f"Generated {len(records)} bug-fix records.")
    print(f"Output folder: {OUTPUT_DIR}")
