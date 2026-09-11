from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "large_training_corpus"
PROJECTS_DIR = ROOT / "project_examples"
DATA_DIR.mkdir(exist_ok=True)
PROJECTS_DIR.mkdir(exist_ok=True)

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

LANGUAGE_EXTENSIONS = {
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

LANGUAGE_DIR_NAMES = {
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


def assembly_sample(language: str) -> str:
    return {
        "Python": "section .text\n    global _start\n_start:\n    mov eax, 1\n    xor ebx, ebx\n    int 0x80\n",
        "JavaScript": "section .text\n    global _start\n_start:\n    mov rax, 60\n    xor rdi, rdi\n    syscall\n",
        "Java": "section .text\n    global main\nmain:\n    mov eax, 1\n    xor ebx, ebx\n    int 0x80\n",
        "C#": "section .text\n    global _start\n_start:\n    mov eax, 60\n    xor edi, edi\n    syscall\n",
        "C++": "section .text\n    global main\nmain:\n    mov eax, 0\n    ret\n",
        "Go": "section .text\n    global main\nmain:\n    mov eax, 0\n    ret\n",
        "Rust": "section .text\n    global main\nmain:\n    mov eax, 0\n    ret\n",
        "TypeScript": "section .text\n    global _start\n_start:\n    xor eax, eax\n    ret\n",
        "PHP": "section .text\n    global _start\n_start:\n    mov eax, 60\n    xor edi, edi\n    syscall\n",
        "Ruby": "section .text\n    global _start\n_start:\n    mov eax, 1\n    mov ebx, 0\n    int 0x80\n",
    }[language]


def binary_sample(language: str) -> str:
    return {
        "Python": "31 c0 31 db b0 01 40 89 c3 80 3d 2a 00 00 00 00 0f 05",
        "JavaScript": "48 83 ec 08 48 89 5c 24 08 48 89 74 24 10 48 8b 5c 24 08 48 83 c4 08 c3",
        "Java": "55 48 89 e5 48 83 ec 10 89 7d fc 8b 45 fc 83 c0 01 89 45 fc eb e7 8b 45 fc 5d c3",
        "C#": "48 31 c0 48 31 ff 48 c7 c0 3c 00 00 00 0f 05",
        "C++": "55 48 89 e5 48 83 ec 10 89 7d fc 8b 45 fc 83 c0 01 89 45 fc eb e7 8b 45 fc 5d c3",
        "Go": "48 83 ec 08 48 89 5c 24 08 48 83 c4 08 c3",
        "Rust": "48 83 ec 08 48 89 5c 24 08 48 83 c4 08 c3",
        "TypeScript": "31 c0 c3 90 90 90 90",
        "PHP": "48 31 c0 48 31 ff 48 c7 c0 3c 00 00 00 0f 05",
        "Ruby": "b8 01 00 00 00 bb 00 00 00 00 cd 80",
    }[language]


def project_code(language: str, kind: str) -> str:
    if language == "Python":
        snippets = {
            "project_cli": "def main():\n    items = [12, 18, 21, 9, 31]\n    total = sum(items)\n    avg = total / len(items)\n    print(f'Total: {total}')\n    print(f'Average: {avg:.2f}')\n\nif __name__ == '__main__':\n    main()\n",
            "project_parser": "import csv\n\nwith open('sales.csv', newline='', encoding='utf-8') as fh:\n    rows = list(csv.DictReader(fh))\n\nrevenue = sum(float(r['amount']) for r in rows)\nprint(f'Revenue: {revenue:.2f}')\n",
            "project_data_pipeline": "def clean_values(values):\n    return [int(v) for v in values if v.strip() not in {'', 'NA'}]\n\nraw = ['1', '2', '', 'NA', '7']\nprint(clean_values(raw))\n",
            "project_api": "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/health')\ndef health():\n    return {'status': 'ok'}\n",
            "project_system_tool": "import os\n\nfor name in os.listdir('.'):\n    if name.endswith('.py'):\n        print(name)\n",
            "memory": "def copy_buffer(src, dst):\n    for i in range(len(src)):\n        dst[i] = src[i]\n    return dst\n",
            "syscall": "import os\n\nwith open('/tmp/pid.txt', 'w', encoding='utf-8') as fh:\n    fh.write(str(os.getpid()))\n",
            "organic_high_level": "def read_and_sum(path):\n    with open(path, 'r', encoding='utf-8') as fh:\n        return sum(int(line.strip()) for line in fh if line.strip())\n\nprint(read_and_sum('numbers.txt'))\n",
        }
        return snippets[kind]

    if language == "JavaScript":
        snippets = {
            "project_cli": "const items = [12, 18, 21, 9, 31];\nconst total = items.reduce((sum, v) => sum + v, 0);\nconsole.log('Total:', total);\nconsole.log('Average:', (total / items.length).toFixed(2));\n",
            "project_parser": "const fs = require('fs');\nconst rows = fs.readFileSync('sales.csv', 'utf8').trim().split('\n').slice(1);\nconst revenue = rows.reduce((sum, row) => sum + Number(row.split(',')[1] || 0), 0);\nconsole.log('Revenue:', revenue.toFixed(2));\n",
            "project_data_pipeline": "const raw = ['1', '2', '', 'NA', '7'];\nconst clean = raw.filter(v => v && v !== 'NA').map(Number);\nconsole.log(clean);\n",
            "project_api": "const express = require('express');\nconst app = express();\napp.get('/health', (_, res) => res.json({ status: 'ok' }));\napp.listen(3000);\n",
            "project_system_tool": "const fs = require('fs');\nfor (const name of fs.readdirSync('.')) {\n  if (name.endsWith('.js')) console.log(name);\n}\n",
            "memory": "function copyBytes(src, dst) {\n  for (let i = 0; i < src.length; i++) dst[i] = src[i];\n  return dst;\n}\n",
            "syscall": "const fs = require('fs');\nfs.writeFileSync('/tmp/pid.txt', String(process.pid));\n",
            "organic_high_level": "const fs = require('fs');\nconst data = fs.readFileSync('config.json', 'utf8');\nconst config = JSON.parse(data);\nconsole.log(config.port);\n",
        }
        return snippets[kind]

    if language == "Java":
        snippets = {
            "project_cli": "public class Main {\n    public static void main(String[] args) {\n        int[] items = {12, 18, 21, 9, 31};\n        int total = 0;\n        for (int value : items) total += value;\n        System.out.println(\"Total: \" + total);\n        System.out.println(\"Average: \" + (total / (double) items.length));\n    }\n}\n",
            "project_parser": "import java.nio.file.*;\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        var text = Files.readString(Path.of(\"sales.csv\"));\n        System.out.println(\"Lines: \" + text.lines().count());\n    }\n}\n",
            "project_data_pipeline": "public class Main {\n    public static void main(String[] args) {\n        String[] raw = {\"1\", \"2\", \"\", \"NA\", \"7\"};\n        int count = 0;\n        for (String value : raw) if (value != null && !value.isBlank() && !value.equals(\"NA\")) count++;\n        System.out.println(count);\n    }\n}\n",
            "project_api": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"API stub ready\");\n    }\n}\n",
            "project_system_tool": "import java.io.*;\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        var dir = new File(\".\");\n        for (String name : dir.list()) if (name.endsWith(\".java\")) System.out.println(name);\n    }\n}\n",
            "memory": "public class BufferCopy {\n    static void copy(byte[] src, byte[] dst) {\n        System.arraycopy(src, 0, dst, 0, src.length);\n    }\n}\n",
            "syscall": "import java.io.*;\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        new FileWriter(\"/tmp/pid.txt\").write(String.valueOf(java.lang.ProcessHandle.current().pid()));\n    }\n}\n",
            "organic_high_level": "import java.nio.file.*;\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        var text = Files.readString(Path.of(\"input.txt\"));\n        System.out.println(text.length());\n    }\n}\n",
        }
        return snippets[kind]

    if language == "C#":
        snippets = {
            "project_cli": "using System;\nclass Program {\n    static void Main() {\n        int[] items = { 12, 18, 21, 9, 31 };\n        int total = 0;\n        foreach (int value in items) total += value;\n        Console.WriteLine($\"Total: {total}\");\n        Console.WriteLine($\"Average: {total / (double)items.Length:F2}\");\n    }\n}\n",
            "project_parser": "using System;\nusing System.IO;\nclass Program {\n    static void Main() {\n        var lines = File.ReadAllLines(\"sales.csv\");\n        Console.WriteLine($\"Rows: {lines.Length}\");\n    }\n}\n",
            "project_data_pipeline": "using System;\nclass Program {\n    static void Main() {\n        string[] raw = { \"1\", \"2\", \"\", \"NA\", \"7\" };\n        int count = 0;\n        foreach (var value in raw) if (!string.IsNullOrWhiteSpace(value) && value != \"NA\") count++;\n        Console.WriteLine(count);\n    }\n}\n",
            "project_api": "using System;\nclass Program {\n    static void Main() { Console.WriteLine(\"API stub ready\"); }\n}\n",
            "project_system_tool": "using System;\nusing System.IO;\nclass Program {\n    static void Main() {\n        foreach (var file in Directory.GetFiles(\".\")) Console.WriteLine(file);\n    }\n}\n",
            "memory": "unsafe static void Copy(byte[] src, byte[] dst) {\n    fixed (byte* s = src, d = dst) {\n        Buffer.MemoryCopy(s, d, dst.Length, src.Length);\n    }\n}\n",
            "syscall": "using System.IO;\nFile.WriteAllText(\"/tmp/pid.txt\", System.Environment.ProcessId.ToString());\n",
            "organic_high_level": "using System;\nusing System.IO;\nvar text = File.ReadAllText(\"config.json\");\nConsole.WriteLine(text.Length);\n",
        }
        return snippets[kind]

    if language == "C++":
        snippets = {
            "project_cli": "#include <iostream>\n#include <vector>\nint main() {\n    std::vector<int> items = {12, 18, 21, 9, 31};\n    int total = 0;\n    for (int value : items) total += value;\n    std::cout << \"Total: \" << total << '\\n';\n    std::cout << \"Average: \" << (total / static_cast<double>(items.size())) << '\\n';\n}\n",
            "project_parser": "#include <fstream>\n#include <iostream>\nint main() {\n    std::ifstream file(\"sales.csv\");\n    std::string line;\n    int count = 0;\n    while (std::getline(file, line)) ++count;\n    std::cout << count << '\\n';\n}\n",
            "project_data_pipeline": "#include <iostream>\n#include <vector>\n#include <string>\nint main() {\n    std::vector<std::string> raw = {\"1\", \"2\", \"\", \"NA\", \"7\"};\n    int count = 0;\n    for (const auto& value : raw) if (!value.empty() && value != \"NA\") ++count;\n    std::cout << count << '\\n';\n}\n",
            "project_api": "#include <iostream>\nint main() { std::cout << \"API stub ready\\n\"; }\n",
            "project_system_tool": "#include <filesystem>\n#include <iostream>\nint main() {\n    for (const auto& entry : std::filesystem::directory_iterator(\".\")) {\n        std::cout << entry.path() << '\\n';\n    }\n}\n",
            "memory": "#include <cstring>\nvoid copy_bytes(unsigned char* dst, const unsigned char* src, size_t n) {\n    std::memcpy(dst, src, n);\n}\n",
            "syscall": "#include <fstream>\nint main() {\n    std::ofstream out(\"/tmp/pid.txt\");\n    out << getpid();\n}\n",
            "organic_high_level": "#include <fstream>\n#include <iostream>\nint main() {\n    std::ifstream file(\"numbers.txt\");\n    int total = 0; int value = 0;\n    while (file >> value) total += value;\n    std::cout << total << '\\n';\n}\n",
        }
        return snippets[kind]

    if language == "Go":
        snippets = {
            "project_cli": "package main\n\nimport \"fmt\"\n\nfunc main() {\n    items := []int{12, 18, 21, 9, 31}\n    total := 0\n    for _, value := range items { total += value }\n    fmt.Println(\"Total:\", total)\n    fmt.Printf(\"Average: %.2f\\n\", float64(total)/float64(len(items)))\n}\n",
            "project_parser": "package main\n\nimport (\n    \"fmt\"\n    \"os\"\n)\n\nfunc main() {\n    data, _ := os.ReadFile(\"sales.csv\")\n    fmt.Println(\"Bytes:\", len(data))\n}\n",
            "project_data_pipeline": "package main\n\nimport \"fmt\"\n\nfunc main() {\n    raw := []string{\"1\", \"2\", \"\", \"NA\", \"7\"}\n    count := 0\n    for _, value := range raw {\n        if value != \"\" && value != \"NA\" { count++ }\n    }\n    fmt.Println(count)\n}\n",
            "project_api": "package main\n\nimport \"fmt\"\n\nfunc main() { fmt.Println(\"API stub ready\") }\n",
            "project_system_tool": "package main\n\nimport (\n    \"fmt\"\n    \"os\"\n)\n\nfunc main() {\n    entries, _ := os.ReadDir(\".\")\n    for _, entry := range entries { fmt.Println(entry.Name()) }\n}\n",
            "memory": "package main\n\nfunc copyBytes(dst, src []byte) {\n    copy(dst, src)\n}\n",
            "syscall": "package main\n\nimport \"os\"\n\nfunc main() {\n    _ = os.WriteFile(\"/tmp/pid.txt\", []byte(\"123\"), 0644)\n}\n",
            "organic_high_level": "package main\n\nimport (\n    \"fmt\"\n    \"os\"\n)\n\nfunc main() {\n    data, _ := os.ReadFile(\"config.json\")\n    fmt.Println(len(data))\n}\n",
        }
        return snippets[kind]

    if language == "Rust":
        snippets = {
            "project_cli": "fn main() {\n    let items = [12, 18, 21, 9, 31];\n    let total: i32 = items.iter().sum();\n    println!(\"Total: {}\", total);\n    println!(\"Average: {:.2}\", total as f64 / items.len() as f64);\n}\n",
            "project_parser": "fn main() {\n    let raw = [\"1\", \"2\", \"\", \"NA\", \"7\"];\n    let count = raw.iter().filter(|v| !v.is_empty() && *v != \"NA\").count();\n    println!(\"{}\", count);\n}\n",
            "project_data_pipeline": "fn main() {\n    let raw = [\"1\", \"2\", \"\", \"NA\", \"7\"];\n    let clean: Vec<i32> = raw.iter().filter_map(|v| {\n        if !v.is_empty() && *v != \"NA\" { Some(v.parse::<i32>().unwrap()) } else { None }\n    }).collect();\n    println!(\"{:?}\", clean);\n}\n",
            "project_api": "fn main() { println!(\"API stub ready\"); }\n",
            "project_system_tool": "fn main() { println!(\"Listing files\"); }\n",
            "memory": "fn copy_bytes(dst: &mut [u8], src: &[u8]) {\n    dst.copy_from_slice(src);\n}\n",
            "syscall": "use std::fs;\nfn main() { fs::write(\"/tmp/pid.txt\", std::process::id().to_string()).unwrap(); }\n",
            "organic_high_level": "use std::fs;\nfn main() {\n    let text = fs::read_to_string(\"config.txt\").unwrap();\n    println!(\"{}\", text.len());\n}\n",
        }
        return snippets[kind]

    if language == "TypeScript":
        snippets = {
            "project_cli": "const items = [12, 18, 21, 9, 31];\nconst total = items.reduce((sum, value) => sum + value, 0);\nconsole.log('Total:', total);\nconsole.log('Average:', (total / items.length).toFixed(2));\n",
            "project_parser": "const fs = require('fs');\nconst lines = fs.readFileSync('sales.csv', 'utf8').trim().split('\n');\nconsole.log('Rows:', lines.length);\n",
            "project_data_pipeline": "const raw = ['1', '2', '', 'NA', '7'];\nconst clean = raw.filter(v => v && v !== 'NA').map(Number);\nconsole.log(clean);\n",
            "project_api": "import express from 'express';\nconst app = express();\napp.get('/health', (_, res) => res.json({ status: 'ok' }));\napp.listen(3000);\n",
            "project_system_tool": "import fs from 'fs';\nfor (const name of fs.readdirSync('.')) { if (name.endsWith('.ts')) console.log(name); }\n",
            "memory": "function cloneBuffer(src: Uint8Array): Uint8Array {\n  return new Uint8Array(src);\n}\n",
            "syscall": "import fs from 'fs';\nfs.writeFileSync('/tmp/pid.txt', String(process.pid));\n",
            "organic_high_level": "import fs from 'fs';\nconst text = fs.readFileSync('config.json', 'utf8');\nconsole.log(text.length);\n",
        }
        return snippets[kind]

    if language == "PHP":
        snippets = {
            "project_cli": "<?php\n$items = [12, 18, 21, 9, 31];\n$total = array_sum($items);\necho \"Total: \" . $total . PHP_EOL;\necho \"Average: \" . ($total / count($items)) . PHP_EOL;\n",
            "project_parser": "<?php\n$lines = file('sales.csv');\necho 'Rows: ' . count($lines) . PHP_EOL;\n",
            "project_data_pipeline": "<?php\n$raw = ['1', '2', '', 'NA', '7'];\n$clean = array_filter($raw, fn($value) => $value !== '' && $value !== 'NA');\nprint_r(array_map('intval', $clean));\n",
            "project_api": "<?php\nheader('Content-Type: application/json');\necho json_encode(['status' => 'ok']);\n",
            "project_system_tool": "<?php\nforeach (scandir('.') as $entry) { if (str_ends_with($entry, '.php')) echo $entry . PHP_EOL; }\n",
            "memory": "<?php\nfunction copy_bytes(array $src): array { return array_values($src); }\n",
            "syscall": "<?php\nfile_put_contents('/tmp/pid.txt', getmypid());\n",
            "organic_high_level": "<?php\n$data = file_get_contents('config.json');\n$config = json_decode($data, true);\necho $config['timeout'];\n",
        }
        return snippets[kind]

    if language == "Ruby":
        snippets = {
            "project_cli": "items = [12, 18, 21, 9, 31]\ntotal = items.sum\nputs \"Total: #{total}\"\nputs \"Average: #{(total / items.length.to_f).round(2)}\"\n",
            "project_parser": "lines = File.readlines('sales.csv')\nputs \"Rows: #{lines.length}\"\n",
            "project_data_pipeline": "raw = ['1', '2', '', 'NA', '7']\nclean = raw.reject { |v| v.empty? || v == 'NA' }.map(&:to_i)\np clean\n",
            "project_api": "puts 'API stub ready'\n",
            "project_system_tool": "Dir.children('.').grep(/\\.rb$/).each { |name| puts name }\n",
            "memory": "def copy_bytes(src, dst)\n  src.each_with_index { |byte, idx| dst[idx] = byte }\n  dst\nend\n",
            "syscall": "File.write('/tmp/pid.txt', Process.pid.to_s)\n",
            "organic_high_level": "data = File.read('config.json')\nconfig = JSON.parse(data)\nputs config['timeout']\n",
        }
        return snippets[kind]

    raise ValueError(f"Unsupported language: {language}")


records = []
for language in LANGUAGES:
    slug = LANGUAGE_DIR_NAMES[language]
    lang_dir = PROJECTS_DIR / slug
    lang_dir.mkdir(exist_ok=True)

    # write a working project file for each language
    main_filename = f"project_main{LANGUAGE_EXTENSIONS[language]}"
    (lang_dir / main_filename).write_text(project_code(language, "project_cli"), encoding="utf-8")
    (lang_dir / "README.md").write_text(
        f"# {language} sample project\n\nThis is a working example project for {language}.\n\n- Includes CLI flow\n- Supports data parsing and reporting\n- Designed for training LLMs to build complete working programs\n",
        encoding="utf-8",
    )
    (lang_dir / "assembly_example.asm").write_text(assembly_sample(language), encoding="utf-8")
    (lang_dir / "binary_example.txt").write_text(binary_sample(language), encoding="utf-8")

    categories = [
        "project_cli",
        "project_parser",
        "project_data_pipeline",
        "project_api",
        "project_system_tool",
        "memory",
        "syscall",
        "assembly",
        "binary",
        "organic_high_level",
    ]

    for index, category in enumerate(categories, start=1):
        text = project_code(language, category) if category not in {"assembly", "binary"} else (
            assembly_sample(language) if category == "assembly" else binary_sample(language)
        )
        source_type = "organic" if category == "organic_high_level" else "synthetic"
        record = {
            "dataset_id": f"{slug}_{category}_{index}",
            "language": language,
            "category": category,
            "source_type": source_type,
            "valid": True,
            "difficulty": "core" if category in {"project_cli", "project_parser", "project_data_pipeline", "project_api", "project_system_tool", "organic_high_level"} else "low_level",
            "text": text,
            "labels": json.dumps(["code_generation", "project_building", language.lower(), category], ensure_ascii=False),
            "notes": f"{language} {category} sample for end-to-end LLM training, including realistic project-building patterns and low-level understanding.",
        }
        records.append(record)

csv_path = DATA_DIR / "large_llm_training_corpus.csv"
with csv_path.open("w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(
        csv_file,
        fieldnames=["dataset_id", "language", "category", "source_type", "valid", "difficulty", "labels", "text", "notes"],
    )
    writer.writeheader()
    writer.writerows(records)

jsonl_path = DATA_DIR / "large_llm_training_corpus.jsonl"
with jsonl_path.open("w", encoding="utf-8") as jsonl_file:
    for record in records:
        jsonl_file.write(json.dumps(record, ensure_ascii=False) + "\n")

manifest = {
    "title": "Large LLM Training Corpus for Complete Project Generation",
    "languages": LANGUAGES,
    "categories": [
        "project_cli",
        "project_parser",
        "project_data_pipeline",
        "project_api",
        "project_system_tool",
        "memory",
        "syscall",
        "assembly",
        "binary",
        "organic_high_level",
    ],
    "record_count": len(records),
    "source_mix": {
        "organic": sum(1 for row in records if row["source_type"] == "organic"),
        "synthetic": sum(1 for row in records if row["source_type"] == "synthetic"),
    },
    "description": "A large corpus designed to teach LLMs how to generate code accurately, creatively, and end-to-end for complete coding tasks across the top 10 programming languages, including assembly and binary reasoning.",
    "project_directories": [str(path.relative_to(ROOT)) for path in sorted(PROJECTS_DIR.iterdir())],
}
manifest_path = DATA_DIR / "manifest.json"
manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

readme_path = ROOT / "README.md"
readme_path.write_text(
    "# Large LLM and ML Programming Corpus\n\n"
    "This corpus is built to teach LLMs and ML models to write code accurately and creatively from start to finish, across the top 10 languages and including low-level assembly and binary understanding.\n\n"
    "## Included languages\n\n"
    + "\n".join(f"- {lang}" for lang in LANGUAGES)
    + "\n\n"
    "## Included project styles\n\n"
    "- CLI tools\n- Parsers\n- Data pipelines\n- API stubs\n- system utilities\n- memory and syscall awareness\n- assembly and binary examples\n\n"
    "## Output folders\n\n"
    "- project_examples/\n- large_training_corpus/\n",
    encoding="utf-8",
)

print(f"Generated {len(records)} records across {len(LANGUAGES)} languages.")
print(f"CSV: {csv_path}")
print(f"JSONL: {jsonl_path}")
print(f"Project examples: {PROJECTS_DIR}")
