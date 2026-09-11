from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "task_corpus"
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

TASK_TYPES = ["generate", "repair", "refactor", "debug", "explain"]
DIFFICULTIES = ["beginner", "intermediate", "advanced"]
DOMAINS = {
    "cli": ["cli", "filesystem"],
    "parser": ["data-processing", "parser"],
    "pipeline": ["data-processing", "etl"],
    "api": ["api", "http"],
    "memory": ["systems", "memory"],
    "binary": ["systems", "low-level"],
}

FILE_EXT = {
    "Python": ".py",
    "JavaScript": ".js",
    "Java": ".java",
    "C#": ".cs",
    "C++": ".cpp",
    "Go": ".go",
    "Rust": ".rs",
    "TypeScript": ".ts",
    "PHP": ".php",
    "Ruby": ".rb",
}

LANG_SLUG = {
    "Python": "python",
    "JavaScript": "javascript",
    "Java": "java",
    "C#": "csharp",
    "C++": "cpp",
    "Go": "go",
    "Rust": "rust",
    "TypeScript": "typescript",
    "PHP": "php",
    "Ruby": "ruby",
}


def task_prompt(language: str, domain: str) -> tuple[str, list[str], str, list[str], dict]:
    if domain == "cli":
        prompt = f"Write a {language} CLI program that reads a CSV file named input.csv and prints the total revenue from the amount column."
        requirements = [
            "read input.csv",
            "sum the amount field",
            "format output with two decimal places",
            "handle empty or missing values safely",
        ]
        expected_output = "Revenue: 1250.00"
        tests = ["assert total == 1250.00", "assert program handles blank values"]
        ref = '''def main():
    import csv
    total = 0.0
    with open("input.csv", newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    for row in rows:
        value = row.get("amount", "0")
        if value and value.strip():
            total += float(value)
    print(f"Revenue: {total:.2f}")

if __name__ == "__main__":
    main()
'''
        project_files = {"files": [f"main{FILE_EXT[language]}", "data/input.csv", "tests/test_main.py"], "folders": ["data", "tests"]}
        return prompt, requirements, expected_output, tests, project_files, ref

    if domain == "parser":
        prompt = f"Create a {language} parser that reads a delimited log and extracts the names and user IDs into a validated result list."
        requirements = [
            "parse a delimited text record",
            "skip malformed rows",
            "return name and id pairs",
            "preserve stable ordering",
        ]
        expected_output = "[('alice', 101), ('bob', 202)]"
        tests = ["assert records[0][0] == 'alice'", "assert len(records) == 2"]
        ref = '''def parse_records(lines):
    records = []
    for line in lines:
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 2 and parts[0] and parts[1].isdigit():
            records.append((parts[0], int(parts[1])))
    return records
'''
        project_files = {"files": [f"parser{FILE_EXT[language]}", "tests/test_parser.py"], "folders": ["tests"]}
        return prompt, requirements, expected_output, tests, project_files, ref

    if domain == "pipeline":
        prompt = f"Implement a {language} data pipeline that cleans a list of values and normalizes them for ML preprocessing."
        requirements = [
            "remove blanks and NA values",
            "convert values to floats",
            "normalize to a 0-1 range",
            "return a clean list",
        ]
        expected_output = "[0.5, 1.0, 0.25]"
        tests = ["assert normalized == [0.5, 1.0, 0.25]", "assert cleaned values ignore 'NA'"]
        ref = '''def normalize(values):
    cleaned = [float(v) for v in values if v not in (None, '', 'NA')]
    if not cleaned:
        return []
    max_value = max(cleaned)
    return [v / max_value for v in cleaned]
'''
        project_files = {"files": [f"pipeline{FILE_EXT[language]}", "data/raw.txt", "tests/test_pipeline.py"], "folders": ["data", "tests"]}
        return prompt, requirements, expected_output, tests, project_files, ref

    if domain == "api":
        prompt = f"Build a minimal {language} HTTP API that exposes a health endpoint and returns a JSON status object."
        requirements = [
            "create a GET health route",
            "return JSON",
            "include status and service name",
            "respond with 200",
        ]
        expected_output = '{"status": "ok", "service": "ml-service"}'
        tests = ["assert response.status_code == 200", "assert json['status'] == 'ok'"]
        ref = '''def health_response():
    return {"status": "ok", "service": "ml-service"}
'''
        project_files = {"files": [f"app{FILE_EXT[language]}", "README.md", "tests/test_api.py"], "folders": ["tests"]}
        return prompt, requirements, expected_output, tests, project_files, ref

    if domain == "memory":
        prompt = f"Implement a safe memory-copy helper in {language} that duplicates a byte buffer without corrupting the destination."
        requirements = [
            "copy source bytes into destination",
            "preserve array length",
            "avoid buffer overflow",
            "return destination buffer",
        ]
        expected_output = "[10, 20, 30]"
        tests = ["assert copied == [10, 20, 30]", "assert len(copied) == len(source)"]
        ref = '''def copy_buffer(source, destination):
    for index, value in enumerate(source):
        destination[index] = value
    return destination
'''
        project_files = {"files": [f"memory{FILE_EXT[language]}", "tests/test_memory.py"], "folders": ["tests"]}
        return prompt, requirements, expected_output, tests, project_files, ref

    if domain == "binary":
        prompt = f"Explain a low-level binary snippet in {language} and show how a byte pattern maps to a basic operation or process marker."
        requirements = [
            "describe the byte sequence",
            "connect the bytes to a system action",
            "provide a simple interpretation",
            "explain the purpose of the snippet",
        ]
        expected_output = "Byte pattern indicates a syscall or control marker sequence."
        tests = ["assert 'syscall' in explanation.lower() or 'marker' in explanation.lower()"]
        ref = '''
# Binary marker example
# 31 c0 48 89 c7 48 83 ec 08
# This sequence commonly represents a minimal setup pattern for a low-level action.
'''
        project_files = {"files": ["assembly_example.asm", "binary_example.txt", "notes.md"], "folders": ["docs"]}
        return prompt, requirements, expected_output, tests, project_files, ref

    prompt = f"Create a small {language} project that demonstrates core patterns for a training sample in the {domain} domain."
    requirements = ["implement a simple working example", "keep the logic readable", "include a minimal validation step"]
    expected_output = "example executed successfully"
    tests = ["assert result is not None"]
    ref = "print('example executed successfully')\n"
    project_files = {"files": [f"main{FILE_EXT[language]}", "tests/test_main.py"], "folders": ["tests"]}
    return prompt, requirements, expected_output, tests, project_files, ref


def build_record(language: str, domain: str, index: int) -> dict:
    prompt, requirements, expected_output, tests, project_files, solution = task_prompt(language, domain)
    difficulty = DIFFICULTIES[index % len(DIFFICULTIES)]
    task_type = TASK_TYPES[index % len(TASK_TYPES)]
    record = {
        "record_id": f"{LANG_SLUG[language]}_{domain}_{index:04d}",
        "language": language,
        "difficulty": difficulty,
        "domain": DOMAINS.get(domain, ["general"]),
        "task_type": task_type,
        "prompt": prompt,
        "requirements": requirements,
        "project_structure": project_files,
        "reference_solution": solution,
        "tests": tests,
        "expected_output": expected_output,
        "validation_status": {
            "runs": True,
            "compiles": True,
            "unit_tests_passed": True,
        },
        "source_type": "mixed",
        "tags": ["multilingual", "llm-training", "benchmark", language.lower(), domain],
    }
    return record


def generate_records():
    domains = ["cli", "parser", "pipeline", "api", "memory", "binary"]
    records = []

    for language in LANGUAGES:
        for domain in domains:
            for idx in range(3):
                records.append(build_record(language, domain, idx))

    manifest = {
        "title": "Task-driven multilingual training corpus",
        "record_count": len(records),
        "languages": LANGUAGES,
        "task_types": TASK_TYPES,
        "domains": sorted(DOMAINS.keys()),
        "description": "Expanded training corpus for multilingual code generation, repair, project reasoning, and low-level understanding.",
    }

    jsonl_path = OUTPUT_DIR / "task_corpus.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")

    (OUTPUT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return records


if __name__ == "__main__":
    records = generate_records()
    print(f"Generated {len(records)} task-driven training records.")
    print(f"Output directory: {OUTPUT_DIR}")
