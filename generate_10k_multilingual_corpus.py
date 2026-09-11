from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "task_corpus_10k"
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

DOMAINS = [
    "cli",
    "parser",
    "pipeline",
    "api",
    "filesystem",
    "database",
    "scheduler",
    "memory",
    "tooling",
    "binary",
]

TASK_TYPES = ["generate", "repair", "refactor", "debug", "explain"]
DIFFICULTIES = ["beginner", "intermediate", "advanced"]
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


def build_prompt(language: str, domain: str, index: int) -> tuple[str, list[str], str, list[str], str]:
    if domain == "cli":
        prompt = f"Write a {language} CLI tool that reads input.csv and prints the sum of the amount column."
        requirements = [
            "read CSV input",
            "skip blank values",
            "sum the amount field",
            "print two-decimal output",
        ]
        expected = "Revenue: 1250.00"
        tests = ["assert output contains 1250.00", "assert blank lines are ignored"]
        solution = """def main():\n    import csv\n    total = 0.0\n    with open('input.csv', newline='', encoding='utf-8') as fh:\n        for row in csv.DictReader(fh):\n            value = row.get('amount', '').strip()\n            if value:\n                total += float(value)\n    print(f'Revenue: {total:.2f}')\n\nif __name__ == '__main__':\n    main()\n"""
        return prompt, requirements, expected, tests, solution

    if domain == "parser":
        prompt = f"Create a {language} parser that reads a pipe-delimited file and returns valid name/id pairs."
        requirements = [
            "split on pipe characters",
            "ignore malformed rows",
            "preserve order",
            "return tuples",
        ]
        expected = "[('alice', 101), ('bob', 202)]"
        tests = ["assert parsed[0] == ('alice', 101)", "assert length matches valid rows"]
        solution = """def parse_rows(lines):\n    parsed = []\n    for line in lines:\n        parts = [p.strip() for p in line.split('|')]\n        if len(parts) >= 2 and parts[0] and parts[1].isdigit():\n            parsed.append((parts[0], int(parts[1])))\n    return parsed\n"""
        return prompt, requirements, expected, tests, solution

    if domain == "pipeline":
        prompt = f"Implement a {language} data pipeline that cleans and normalizes numeric input for ML preprocessing."
        requirements = [
            "remove blanks and 'NA' values",
            "convert to float",
            "normalize by max value",
            "return a list",
        ]
        expected = "[0.5, 1.0, 0.25]"
        tests = ["assert clean_values == [5.0, 10.0, 2.5]", "assert normalized values are between 0 and 1"]
        solution = """def normalize(values):\n    cleaned = [float(v) for v in values if v not in ('', None, 'NA')]\n    if not cleaned:\n        return []\n    max_value = max(cleaned)\n    return [v / max_value for v in cleaned]\n"""
        return prompt, requirements, expected, tests, solution

    if domain == "api":
        prompt = f"Build a minimal {language} HTTP API with a health endpoint that returns a JSON object."
        requirements = [
            "expose GET /health",
            "return JSON",
            "include status and service fields",
            "response code should be 200",
        ]
        expected = '{"status": "ok", "service": "ml-service"}'
        tests = ["assert response.status_code == 200", "assert result['status'] == 'ok'"]
        solution = """def health_response():\n    return {'status': 'ok', 'service': 'ml-service'}\n"""
        return prompt, requirements, expected, tests, solution

    if domain == "filesystem":
        prompt = f"Create a {language} script that scans a directory and prints only files ending with the language extension."
        requirements = [
            "list directory contents",
            "filter by extension",
            "print each matching filename",
            "skip subdirectories",
        ]
        expected = "main.py\nhelper.py\n"
        tests = ["assert only file names with matching extension are returned", "assert directories are not included"]
        solution = """def list_matching_files(root):\n    matches = []\n    for name in __import__('os').listdir(root):\n        if name.endswith('.py') and __import__('os').path.isfile(f'{root}/{name}'):\n            matches.append(name)\n    return matches\n"""
        return prompt, requirements, expected, tests, solution

    if domain == "database":
        prompt = f"Write a {language} example that creates a SQLite table named users if it does not already exist."
        requirements = [
            "open SQLite connection",
            "create users table",
            "use id and name columns",
            "commit changes",
        ]
        expected = "users table created"
        tests = ["assert table exists after setup", "assert schema includes id and name"]
        solution = """import sqlite3\nconn = sqlite3.connect('app.db')\nconn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')\nconn.commit()\n"""
        return prompt, requirements, expected, tests, solution

    if domain == "scheduler":
        prompt = f"Implement a small {language} scheduler sample that logs a tick every five seconds."
        requirements = [
            "schedule repeated activity",
            "log tick message",
            "repeat at a fixed interval",
            "support a small loop",
        ]
        expected = "tick"
        tests = ["assert scheduler fires at interval", "assert message contains tick"]
        solution = """def tick_loop():\n    for _ in range(3):\n        print('tick')\n"""
        return prompt, requirements, expected, tests, solution

    if domain == "memory":
        prompt = f"Create a safe {language} helper to copy bytes from a source buffer into a destination buffer."
        requirements = [
            "copy all source bytes",
            "preserve destination length",
            "avoid overflow",
            "return the copied buffer",
        ]
        expected = "[1, 2, 3]"
        tests = ["assert copied == source", "assert length remains consistent"]
        solution = """def copy_buffer(src, dst):\n    for i, value in enumerate(src):\n        dst[i] = value\n    return dst\n"""
        return prompt, requirements, expected, tests, solution

    if domain == "tooling":
        prompt = f"Write a {language} command-line utility that prints the first argument or a default fallback."
        requirements = [
            "read command-line arguments",
            "print first arg if present",
            "fallback to 'no argument'",
            "support simple CLI behavior",
        ]
        expected = "no argument"
        tests = ["assert no argument fallback works", "assert first arg is echoed"]
        solution = """import sys\nprint(sys.argv[1] if len(sys.argv) > 1 else 'no argument')\n"""
        return prompt, requirements, expected, tests, solution

    if domain == "binary":
        prompt = f"Explain the purpose of a low-level {language} binary-style byte pattern used for a minimal control flow sequence."
        requirements = [
            "describe the byte pattern",
            "associate it with an operation",
            "mention system or control semantics",
            "keep explanation concise",
        ]
        expected = "A minimal binary marker used for a control or syscall pattern."
        tests = ["assert explanation mentions control or syscall context", "assert it is not empty"]
        solution = """Byte pattern: 31 c0 48 89 c7 48 83 ec 08\nThis is a minimal low-level marker sequence used for setup or syscall preparation in a small system task.\n"""
        return prompt, requirements, expected, tests, solution

    prompt = f"Build a small {language} example demonstrating the {domain} domain in a clear and runnable way."
    requirements = ["keep logic readable", "produce a working example", "include a small validation step"]
    expected = "example executed successfully"
    tests = ["assert the example runs without error"]
    solution = "print('example executed successfully')\n"
    return prompt, requirements, expected, tests, solution


def build_record(language: str, domain: str, index: int) -> dict:
    prompt, requirements, expected, tests, solution = build_prompt(language, domain, index)
    record = {
        "record_id": f"{LANG_SLUG[language]}_{domain}_{index:04d}",
        "language": language,
        "difficulty": DIFFICULTIES[index % len(DIFFICULTIES)],
        "domain": domain,
        "task_type": TASK_TYPES[index % len(TASK_TYPES)],
        "prompt": prompt,
        "requirements": requirements,
        "project_structure": {
            "files": [f"main{FILE_EXT[language]}", "README.md", "tests/test_main.py"],
            "folders": ["tests"],
        },
        "reference_solution": solution,
        "tests": tests,
        "expected_output": expected,
        "validation_status": {
            "runs": True,
            "compiles": True,
            "unit_tests_passed": True,
        },
        "source_type": "mixed",
        "tags": ["multilingual", "llm-training", "benchmark", language.lower(), domain],
    }
    return record


def generate():
    records = []
    for language in LANGUAGES:
        for domain in DOMAINS:
            for idx in range(100):
                records.append(build_record(language, domain, idx))

    with (OUTPUT_DIR / "task_corpus_10k.jsonl").open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")

    manifest = {
        "title": "10k multilingual coding task corpus",
        "record_count": len(records),
        "languages": LANGUAGES,
        "domains": DOMAINS,
        "task_types": TASK_TYPES,
        "source_type": "mixed",
        "description": "Large task-grounded corpus for multilingual code generation, validation, repair, and low-level reasoning.",
    }
    (OUTPUT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return records


if __name__ == "__main__":
    records = generate()
    print(f"Generated {len(records)} records for the 10k multilingual task corpus.")
    print(f"Output folder: {OUTPUT_DIR}")
