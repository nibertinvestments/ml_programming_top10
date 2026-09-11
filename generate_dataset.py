from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

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

EXAMPLES = {
    "Python": {
        "code_organic": "def add(a, b):\n    return a + b\n\n\nprint(add(2, 3))\n",
        "code_synthetic": "def normalize(value):\n    return max(0, min(value, 100))\n\n\nprint(normalize(42))\n",
        "assembly": "section .text\n    global _start\n_start:\n    mov eax, 1\n    mov ebx, 42\n    int 0x80\n",
        "binary": "31 c0 31 db b0 01 40 89 c3 80 3d 2a 00 00 00 00 0f 05"
    },
    "JavaScript": {
        "code_organic": "const total = items.reduce((sum, item) => sum + item.price, 0);\nconsole.log('Total:', total);\n",
        "code_synthetic": "function formatAmount(value) {\n  return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value);\n}\nconsole.log(formatAmount(42.5));\n",
        "assembly": "section .text\n    global _start\n_start:\n    mov rax, 60\n    mov rdi, 0\n    syscall\n",
        "binary": "48 83 ec 08 48 89 5c 24 08 48 89 74 24 10 48 8b 5c 24 08 48 83 c4 08 c3"
    },
    "Java": {
        "code_organic": "public class Main {\n    public static void main(String[] args) {\n        int total = 0;\n        for (int i = 1; i <= 5; i++) total += i;\n        System.out.println(total);\n    }\n}\n",
        "code_synthetic": "public class TaxCalculator {\n    public static double applyVAT(double amount, double taxRate) {\n        return amount * (1 + taxRate);\n    }\n}\n",
        "assembly": "section .text\n    global main\nmain:\n    mov eax, 1\n    xor ebx, ebx\n    int 0x80\n",
        "binary": "55 48 89 e5 48 83 ec 10 89 7d fc 8b 45 fc 83 c0 01 89 45 fc eb e7 8b 45 fc 5d c3"
    },
    "C#": {
        "code_organic": "using System;\n\nclass Program {\n    static void Main() {\n        Console.WriteLine(\"Hello, C#!\");\n    }\n}\n",
        "code_synthetic": "public static class StringHelper {\n    public static string Truncate(string input, int maxLength) => input.Length <= maxLength ? input : input[..maxLength];\n}\n",
        "assembly": "section .text\n    global _start\n_start:\n    mov eax, 60\n    xor edi, edi\n    syscall\n",
        "binary": "48 31 c0 48 31 ff 48 c7 c0 3c 00 00 00 0f 05"
    },
    "C++": {
        "code_organic": "#include <iostream>\nint main() {\n    int sum = 0;\n    for (int i = 1; i <= 10; ++i) sum += i;\n    std::cout << sum << std::endl;\n    return 0;\n}\n",
        "code_synthetic": "std::string toTitle(std::string text) {\n    if (text.empty()) return text;\n    text[0] = std::toupper(static_cast<unsigned char>(text[0]));\n    return text;\n}\n",
        "assembly": "section .text\n    global main\nmain:\n    mov eax, 0\n    ret\n",
        "binary": "55 48 89 e5 48 83 ec 10 89 7d fc 8b 45 fc 83 c0 01 89 45 fc eb e7 8b 45 fc 5d c3"
    },
    "Go": {
        "code_organic": "package main\n\nimport \"fmt\"\n\nfunc main() {\n    fmt.Println(\"hello from Go\")\n}\n",
        "code_synthetic": "package main\n\nfunc add(a, b int) int {\n    return a + b\n}\n",
        "assembly": "section .text\n    global main\nmain:\n    mov eax, 0\n    ret\n",
        "binary": "48 83 ec 08 48 89 5c 24 08 48 83 c4 08 c3"
    },
    "Rust": {
        "code_organic": "fn main() {\n    let numbers = [1, 2, 3, 4, 5];\n    let sum: i32 = numbers.iter().sum();\n    println!(\"{sum}\");\n}\n",
        "code_synthetic": "fn square(x: i32) -> i32 { x * x }\nfn main() { println!(\"{}\", square(7)); }\n",
        "assembly": "section .text\n    global main\nmain:\n    mov eax, 0\n    ret\n",
        "binary": "48 83 ec 08 48 89 5c 24 08 48 83 c4 08 c3"
    },
    "TypeScript": {
        "code_organic": "const values: number[] = [1, 2, 3, 4];\nconst total = values.reduce((sum, value) => sum + value, 0);\nconsole.log(total);\n",
        "code_synthetic": "function clamp(value: number, min: number, max: number): number {\n  return Math.min(Math.max(value, min), max);\n}\nconsole.log(clamp(8, 0, 10));\n",
        "assembly": "section .text\n    global _start\n_start:\n    xor eax, eax\n    ret\n",
        "binary": "31 c0 c3 90 90 90 90"
    },
    "PHP": {
        "code_organic": "<?php\n\n$items = [10, 20, 30];\n$sum = array_sum($items);\necho $sum;\n",
        "code_synthetic": "<?php\nfunction greet(string $name): string {\n    return \"Hello, {$name}!\";\n}\necho greet('Ada');\n",
        "assembly": "section .text\n    global _start\n_start:\n    mov eax, 60\n    xor edi, edi\n    syscall\n",
        "binary": "48 31 c0 48 31 ff 48 c7 c0 3c 00 00 00 0f 05"
    },
    "Ruby": {
        "code_organic": "numbers = [1, 2, 3, 4, 5]\nputs numbers.sum\n",
        "code_synthetic": "def full_name(first, last)\n  \"#{first} #{last}\"\nend\nputs full_name('Ada', 'Lovelace')\n",
        "assembly": "section .text\n    global _start\n_start:\n    mov eax, 1\n    mov ebx, 0\n    int 0x80\n",
        "binary": "b8 01 00 00 00 bb 00 00 00 00 cd 80"
    },
}

rows = []
for language in LANGUAGES:
    examples = EXAMPLES[language]
    for category, source_name in [
        ("code", "code_organic"),
        ("code", "code_synthetic"),
        ("assembly", "assembly"),
        ("binary", "binary"),
    ]:
        text = examples[source_name]
        source_type = "organic" if source_name.endswith("organic") else "synthetic"
        rows.append(
            {
                "language": language,
                "category": category,
                "source_type": source_type,
                "dataset_id": f"{language.lower().replace('#', 'sharp').replace('+', 'plus')}_{category}_{len(rows) + 1}",
                "text": text,
                "valid": True,
                "notes": f"{language} {category} sample generated for ML training; Assembly and Binary are included per language."
            }
        )

csv_path = DATA_DIR / "programming_top10_with_assembly_and_binary.csv"
with csv_path.open("w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(
        csv_file,
        fieldnames=["dataset_id", "language", "category", "source_type", "valid", "text", "notes"],
    )
    writer.writeheader()
    writer.writerows(rows)

jsonl_path = DATA_DIR / "programming_top10_with_assembly_and_binary.jsonl"
with jsonl_path.open("w", encoding="utf-8") as jsonl_file:
    for row in rows:
        jsonl_file.write(json.dumps(row, ensure_ascii=False) + "\n")

manifest = {
    "title": "Programming Top 10 with Assembly and Binary",
    "languages": LANGUAGES,
    "categories": ["code", "assembly", "binary"],
    "record_count": len(rows),
    "source_mix": {
        "organic": sum(1 for row in rows if row["source_type"] == "organic"),
        "synthetic": sum(1 for row in rows if row["source_type"] == "synthetic"),
    },
    "description": "A mixed synthetic/organic dataset for ML training on the top 10 programming languages, with Assembly and Binary samples included for every language.",
}
manifest_path = DATA_DIR / "manifest.json"
manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

readme_path = ROOT / "README.md"
readme_path.write_text(
    "# Programming Top 10 ML Dataset\n\n"
    "This dataset contains the top 10 programming languages with Assembly and Binary samples included for each language.\n\n"
    "## Included Languages\n\n"
    + "\n".join(f"- {lang}" for lang in LANGUAGES)
    + "\n\n"
    "## Files\n\n"
    "- data/programming_top10_with_assembly_and_binary.csv\n"
    "- data/programming_top10_with_assembly_and_binary.jsonl\n"
    "- data/manifest.json\n\n"
    "## Notes\n\n"
    "- Mixed organic and synthetic examples were used to reduce false positives and stay suitable for model training.\n"
    "- Each language has code, assembly, and binary samples so the dataset is balanced for classification and code similarity tasks.\n",
    encoding="utf-8",
)

print(f"Generated {len(rows)} records across {len(LANGUAGES)} languages.")
print(f"CSV: {csv_path}")
print(f"JSONL: {jsonl_path}")
print(f"Manifest: {manifest_path}")
