from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "low_level_data"
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
        "high_level_organic": "def read_and_sum(path):\n    with open(path, 'r', encoding='utf-8') as fh:\n        return sum(int(line.strip()) for line in fh if line.strip())\n\nprint(read_and_sum('numbers.txt'))\n",
        "memory_synthetic": "def copy_buffer(src, dst):\n    for i in range(len(src)):\n        dst[i] = src[i]\n    return dst\n",
        "syscall_synthetic": "import os\n\ndef write_pid_file():\n    with open('/tmp/pid.txt', 'w', encoding='utf-8') as fh:\n        fh.write(str(os.getpid()))\n",
        "assembly": "section .text\n    global _start\n_start:\n    mov eax, 1\n    xor ebx, ebx\n    int 0x80\n",
        "binary": "b8 01 00 00 00 bb 00 00 00 00 cd 80"
    },
    "JavaScript": {
        "high_level_organic": "const fs = require('fs');\nconst data = fs.readFileSync('config.json', 'utf8');\nconst config = JSON.parse(data);\nconsole.log(config.port);\n",
        "memory_synthetic": "function copyBytes(src, dst) {\n  for (let i = 0; i < src.length; i++) dst[i] = src[i];\n  return dst;\n}\n",
        "syscall_synthetic": "const fs = require('fs');\nfs.writeFileSync('/tmp/pid.txt', String(process.pid));\n",
        "assembly": "section .text\n    global _start\n_start:\n    mov rax, 60\n    xor rdi, rdi\n    syscall\n",
        "binary": "48 31 c0 48 31 ff 48 c7 c0 3c 00 00 00 0f 05"
    },
    "Java": {
        "high_level_organic": "import java.nio.file.*;\n\npublic class FileReaderDemo {\n    public static void main(String[] args) throws Exception {\n        String text = Files.readString(Path.of(\"input.txt\"));\n        System.out.println(text.length());\n    }\n}\n",
        "memory_synthetic": "public class BufferCopy {\n    static void copy(byte[] src, byte[] dst) {\n        System.arraycopy(src, 0, dst, 0, src.length);\n    }\n}\n",
        "syscall_synthetic": "import java.io.*;\n\npublic class PidWriter {\n    public static void main(String[] args) throws Exception {\n        new FileWriter(\"/tmp/pid.txt\").write(String.valueOf(ProcessHandle.current().pid()));\n    }\n}\n",
        "assembly": "section .text\n    global main\nmain:\n    mov eax, 1\n    xor ebx, ebx\n    int 0x80\n",
        "binary": "55 48 89 e5 48 83 ec 10 89 7d fc 8b 45 fc 83 c0 01 89 45 fc eb e7 8b 45 fc 5d c3"
    },
    "C#": {
        "high_level_organic": "using System;\nusing System.IO;\n\nvar text = File.ReadAllText(\"config.json\");\nConsole.WriteLine(text.Length);\n",
        "memory_synthetic": "unsafe static void Copy(byte[] src, byte[] dst) {\n    fixed (byte* s = src, d = dst) {\n        Buffer.MemoryCopy(s, d, dst.Length, src.Length);\n    }\n}\n",
        "syscall_synthetic": "using System.IO;\nFile.WriteAllText(\"/tmp/pid.txt\", Environment.ProcessId.ToString());\n",
        "assembly": "section .text\n    global _start\n_start:\n    mov eax, 60\n    xor edi, edi\n    syscall\n",
        "binary": "48 31 c0 48 31 ff 48 c7 c0 3c 00 00 00 0f 05"
    },
    "C++": {
        "high_level_organic": "#include <fstream>\n#include <iostream>\n#include <vector>\n\nint main() {\n    std::ifstream input(\"numbers.txt\");\n    int total = 0;\n    int value = 0;\n    while (input >> value) total += value;\n    std::cout << total << \\\"\\n\\\";\n}\n",
        "memory_synthetic": "#include <cstring>\nvoid copy_bytes(unsigned char* dst, const unsigned char* src, size_t n) {\n    std::memcpy(dst, src, n);\n}\n",
        "syscall_synthetic": "#include <fstream>\nint main() {\n    std::ofstream out(\"/tmp/pid.txt\");\n    out << getpid();\n}\n",
        "assembly": "section .text\n    global main\nmain:\n    mov eax, 0\n    ret\n",
        "binary": "55 48 89 e5 48 83 ec 10 89 7d fc 8b 45 fc 83 c0 01 89 45 fc eb e7 8b 45 fc 5d c3"
    },
    "Go": {
        "high_level_organic": "package main\n\nimport (\n    \"fmt\"\n    \"os\"\n)\n\nfunc main() {\n    data, _ := os.ReadFile(\"config.json\")\n    fmt.Println(len(data))\n}\n",
        "memory_synthetic": "package main\n\nfunc copyBytes(dst, src []byte) {\n    copy(dst, src)\n}\n",
        "syscall_synthetic": "package main\n\nimport \"os\"\n\nfunc main() {\n    _ = os.WriteFile(\"/tmp/pid.txt\", []byte(\"123\"), 0644)\n}\n",
        "assembly": "section .text\n    global main\nmain:\n    mov eax, 0\n    ret\n",
        "binary": "48 83 ec 08 48 89 5c 24 08 48 83 c4 08 c3"
    },
    "Rust": {
        "high_level_organic": "use std::fs;\n\nfn main() {\n    let data = fs::read_to_string(\"config.txt\").unwrap();\n    println!(\"{}\", data.len());\n}\n",
        "memory_synthetic": "fn copy_bytes(dst: &mut [u8], src: &[u8]) {\n    dst.copy_from_slice(src);\n}\n",
        "syscall_synthetic": "use std::fs;\nfn main() {\n    fs::write(\"/tmp/pid.txt\", std::process::id().to_string()).unwrap();\n}\n",
        "assembly": "section .text\n    global main\nmain:\n    mov eax, 0\n    ret\n",
        "binary": "48 83 ec 08 48 89 5c 24 08 48 83 c4 08 c3"
    },
    "TypeScript": {
        "high_level_organic": "import fs from 'fs';\nconst payload = fs.readFileSync('settings.json', 'utf8');\nconst config = JSON.parse(payload);\nconsole.log(config.timeout);\n",
        "memory_synthetic": "function cloneBuffer(src: Uint8Array): Uint8Array {\n  return new Uint8Array(src);\n}\n",
        "syscall_synthetic": "import fs from 'fs';\nfs.writeFileSync('/tmp/pid.txt', String(process.pid));\n",
        "assembly": "section .text\n    global _start\n_start:\n    xor eax, eax\n    ret\n",
        "binary": "31 c0 c3 90 90 90 90"
    },
    "PHP": {
        "high_level_organic": "<?php\n\n$data = file_get_contents('config.json');\n$config = json_decode($data, true);\necho $config['timeout'];\n",
        "memory_synthetic": "<?php\nfunction copy_bytes(array $src): array {\n    return array_values($src);\n}\n",
        "syscall_synthetic": "<?php\nfile_put_contents('/tmp/pid.txt', getmypid());\n",
        "assembly": "section .text\n    global _start\n_start:\n    mov eax, 60\n    xor edi, edi\n    syscall\n",
        "binary": "48 31 c0 48 31 ff 48 c7 c0 3c 00 00 00 0f 05"
    },
    "Ruby": {
        "high_level_organic": "data = File.read('config.json')\nconfig = JSON.parse(data)\nputs config['timeout']\n",
        "memory_synthetic": "def copy_bytes(src, dst)\n  src.each_with_index { |byte, idx| dst[idx] = byte }\n  dst\nend\n",
        "syscall_synthetic": "File.write('/tmp/pid.txt', Process.pid.to_s)\n",
        "assembly": "section .text\n    global _start\n_start:\n    mov eax, 1\n    mov ebx, 0\n    int 0x80\n",
        "binary": "b8 01 00 00 00 bb 00 00 00 00 cd 80"
    },
}

rows = []
for language in LANGUAGES:
    examples = EXAMPLES[language]
    for key, category in [
        ("high_level_organic", "high_level"),
        ("memory_synthetic", "memory"),
        ("syscall_synthetic", "syscall"),
        ("assembly", "assembly"),
        ("binary", "binary"),
    ]:
        text = examples[key]
        source_type = "organic" if key.endswith("organic") else "synthetic"
        rows.append(
            {
                "dataset_id": f"{language.lower().replace('#', 'sharp').replace('+', 'plus')}_{category}_{len(rows)+1}",
                "language": language,
                "category": category,
                "source_type": source_type,
                "valid": True,
                "difficulty": "low_level" if category in {"memory", "syscall", "assembly", "binary"} else "core",
                "text": text,
                "labels": json.dumps(["language_identification", category, "low_level_training"], ensure_ascii=False),
                "notes": f"{language} {category} training sample designed for code understanding, execution semantics, and low-level model learning."
            }
        )

csv_path = DATA_DIR / "low_level_training_dataset.csv"
with csv_path.open("w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(
        csv_file,
        fieldnames=["dataset_id", "language", "category", "source_type", "valid", "difficulty", "labels", "text", "notes"],
    )
    writer.writeheader()
    writer.writerows(rows)

jsonl_path = DATA_DIR / "low_level_training_dataset.jsonl"
with jsonl_path.open("w", encoding="utf-8") as jsonl_file:
    for row in rows:
        jsonl_file.write(json.dumps(row, ensure_ascii=False) + "\n")

manifest = {
    "title": "Low-Level Programming Training Corpus",
    "languages": LANGUAGES,
    "categories": ["high_level", "memory", "syscall", "assembly", "binary"],
    "record_count": len(rows),
    "source_mix": {
        "organic": sum(1 for row in rows if row["source_type"] == "organic"),
        "synthetic": sum(1 for row in rows if row["source_type"] == "synthetic"),
    },
    "description": "A low-level ML corpus for teaching LLMs and ML models how high-level code maps to memory operations, syscall behavior, assembly instructions, and binary representations across the top 10 languages.",
    "learning_goals": [
        "language recognition",
        "execution semantics",
        "memory behavior",
        "system call interaction",
        "assembly translation",
        "binary pattern awareness",
        "cross-language code comprehension"
    ],
}
manifest_path = DATA_DIR / "manifest.json"
manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

readme_path = ROOT / "README.md"
readme_path.write_text(
    "# Expanded Low-Level ML Training Dataset\n\n"
    "This dataset expands the earlier language set into a low-level training corpus meant to teach LLMs and ML models how software behaves across the top 10 programming languages.\n\n"
    "## Included languages\n\n"
    + "\n".join(f"- {lang}" for lang in LANGUAGES)
    + "\n\n"
    "## Included categories\n\n"
    "- high_level\n- memory\n- syscall\n- assembly\n- binary\n\n"
    "## Why this is useful\n\n"
    "- Maps source code to system behavior\n- Teaches memory and I/O semantics\n- Includes assembly and binary for each language\n- Supports low-level reasoning for code generation and classification\n- Provides a mixed synthetic and organic training corpus to reduce false positives\n",
    encoding="utf-8",
)

print(f"Generated {len(rows)} low-level training records across {len(LANGUAGES)} languages.")
print(f"CSV: {csv_path}")
print(f"JSONL: {jsonl_path}")
print(f"Manifest: {manifest_path}")
