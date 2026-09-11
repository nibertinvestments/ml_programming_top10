from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "large_training_corpus_v2"
BUNDLE_DIR = ROOT / "project_bundles_v2"
DATA_DIR.mkdir(exist_ok=True)
BUNDLE_DIR.mkdir(exist_ok=True)

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

LANGUAGE_SLOUGNS = {
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

EXTENSIONS = {
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

CATEGORIES = [
    "project_cli",
    "project_parser",
    "project_data_pipeline",
    "project_api",
    "project_http_service",
    "project_file_system",
    "project_database",
    "project_scheduler",
    "memory",
    "syscall",
    "assembly",
    "binary",
    "ml_preprocessor",
    "project_full_stack",
    "project_tooling",
]


def get_assembly(language: str) -> str:
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


def get_binary(language: str) -> str:
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


def make_program(language: str, category: str, variant: str) -> str:
    if language == "Python":
        samples = {
            "project_cli": "def main():\n    values = [12, 18, 21, 9, 31]\n    total = sum(values)\n    avg = total / len(values)\n    print(f'Total: {total}')\n    print(f'Average: {avg:.2f}')\n\nif __name__ == '__main__':\n    main()\n",
            "project_parser": "import csv\n\nwith open('input.csv', newline='', encoding='utf-8') as fh:\n    rows = list(csv.DictReader(fh))\n\nrevenue = sum(float(r['amount']) for r in rows)\nprint(f'Revenue: {revenue:.2f}')\n",
            "project_data_pipeline": "def transform(rows):\n    return [int(value) for value in rows if value.strip() not in {'', 'NA'}]\n\nraw = ['1', '2', '', 'NA', '7']\nprint(transform(raw))\n",
            "project_api": "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/health')\ndef health():\n    return {'status': 'ok'}\n",
            "project_http_service": "from flask import Flask\napp = Flask(__name__)\n\n@app.get('/ping')\ndef ping():\n    return {'message': 'pong'}\n",
            "project_file_system": "import os\n\nfor name in os.listdir('.'):\n    if name.endswith('.py'):\n        print(name)\n",
            "project_database": "import sqlite3\n\nconn = sqlite3.connect('app.db')\nc = conn.cursor()\nc.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')\nconn.commit()\n",
            "project_scheduler": "import schedule\n\n# Example job definition for training purposes\nschedule.every(5).minutes.do(lambda: print('tick'))\n",
            "memory": "def copy_buffer(src, dst):\n    for i in range(len(src)):\n        dst[i] = src[i]\n    return dst\n",
            "syscall": "import os\n\nwith open('/tmp/pid.txt', 'w', encoding='utf-8') as fh:\n    fh.write(str(os.getpid()))\n",
            "ml_preprocessor": "def normalize(values):\n    return [float(v) / max(1.0, max(values)) for v in values]\n\nprint(normalize([10, 20, 30]))\n",
            "project_full_stack": "from flask import Flask, jsonify\napp = Flask(__name__)\n\n@app.get('/')\ndef index():\n    return jsonify({'status': 'ready'})\n",
            "project_tooling": "import argparse\n\nparser = argparse.ArgumentParser()\nparser.add_argument('name')\nprint(parser.parse_args().name)\n",
        }
        return samples[category]

    if language == "JavaScript":
        samples = {
            "project_cli": "const values = [12, 18, 21, 9, 31];\nconst total = values.reduce((sum, value) => sum + value, 0);\nconsole.log('Total:', total);\nconsole.log('Average:', (total / values.length).toFixed(2));\n",
            "project_parser": "const fs = require('fs');\nconst rows = fs.readFileSync('input.csv', 'utf8').trim().split('\n').slice(1);\nconsole.log(rows.length);\n",
            "project_data_pipeline": "const raw = ['1', '2', '', 'NA', '7'];\nconst cleaned = raw.filter(v => v && v !== 'NA').map(Number);\nconsole.log(cleaned);\n",
            "project_api": "const express = require('express');\nconst app = express();\napp.get('/health', (_, res) => res.json({ status: 'ok' }));\napp.listen(3000);\n",
            "project_http_service": "const http = require('http');\nhttp.createServer((req, res) => { res.end(JSON.stringify({ ok: true })); }).listen(8080);\n",
            "project_file_system": "const fs = require('fs');\nfor (const name of fs.readdirSync('.')) if (name.endsWith('.js')) console.log(name);\n",
            "project_database": "const sqlite3 = require('sqlite3').verbose();\nconst db = new sqlite3.Database('app.db');\ndb.run('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)');\n",
            "project_scheduler": "setInterval(() => console.log('tick'), 5000);\n",
            "memory": "function copyBytes(src, dst) {\n  for (let i = 0; i < src.length; i++) dst[i] = src[i];\n  return dst;\n}\n",
            "syscall": "const fs = require('fs');\nfs.writeFileSync('/tmp/pid.txt', String(process.pid));\n",
            "ml_preprocessor": "const normalize = values => values.map(value => Number(value) / Math.max(1, Math.max(...values)));\nconsole.log(normalize([10, 20, 30]));\n",
            "project_full_stack": "const express = require('express');\nconst app = express();\napp.get('/', (_, res) => res.json({ status: 'ready' }));\napp.listen(3000);\n",
            "project_tooling": "const args = process.argv.slice(2);\nconsole.log(args[0] || 'no argument');\n",
        }
        return samples[category]

    if language == "Java":
        samples = {
            "project_cli": "public class Main {\n    public static void main(String[] args) {\n        int[] values = {12, 18, 21, 9, 31};\n        int total = 0;\n        for (int value : values) total += value;\n        System.out.println(\"Total: \" + total);\n        System.out.println(\"Average: \" + (total / (double) values.length));\n    }\n}\n",
            "project_parser": "import java.nio.file.*;\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        var text = Files.readString(Path.of(\"input.csv\"));\n        System.out.println(text.lines().count());\n    }\n}\n",
            "project_data_pipeline": "public class Main {\n    public static void main(String[] args) {\n        String[] raw = {\"1\", \"2\", \"\", \"NA\", \"7\"};\n        int count = 0;\n        for (String value : raw) if (value != null && !value.isBlank() && !value.equals(\"NA\")) count++;\n        System.out.println(count);\n    }\n}\n",
            "project_api": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"API ready\");\n    }\n}\n",
            "project_http_service": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"HTTP service stub\");\n    }\n}\n",
            "project_file_system": "import java.io.File;\npublic class Main {\n    public static void main(String[] args) {\n        File dir = new File(\".\");\n        for (String name : dir.list()) if (name.endsWith(\".java\")) System.out.println(name);\n    }\n}\n",
            "project_database": "import java.sql.*;\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        Connection conn = DriverManager.getConnection(\"jdbc:sqlite:app.db\");\n        Statement st = conn.createStatement();\n        st.execute(\"CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)\");\n    }\n}\n",
            "project_scheduler": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Timer timer = new Timer();\n        timer.schedule(new TimerTask() { public void run() { System.out.println(\"tick\"); } }, 5000);\n    }\n}\n",
            "memory": "public class BufferCopy {\n    static void copy(byte[] src, byte[] dst) {\n        System.arraycopy(src, 0, dst, 0, src.length);\n    }\n}\n",
            "syscall": "import java.io.*;\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        new FileWriter(\"/tmp/pid.txt\").write(String.valueOf(java.lang.ProcessHandle.current().pid()));\n    }\n}\n",
            "ml_preprocessor": "public class Main {\n    public static void main(String[] args) {\n        int[] values = {10, 20, 30};\n        for (int i = 0; i < values.length; i++) values[i] = values[i] / 10;\n        System.out.println(java.util.Arrays.toString(values));\n    }\n}\n",
            "project_full_stack": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Full-stack app stub\");\n    }\n}\n",
            "project_tooling": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(args.length > 0 ? args[0] : \"no argument\");\n    }\n}\n",
        }
        return samples[category]

    if language == "C#":
        samples = {
            "project_cli": "using System;\nclass Program {\n    static void Main() {\n        int[] values = { 12, 18, 21, 9, 31 };\n        int total = 0;\n        foreach (var value in values) total += value;\n        Console.WriteLine($\"Total: {total}\");\n        Console.WriteLine($\"Average: {total / (double)values.Length:F2}\");\n    }\n}\n",
            "project_parser": "using System;\nusing System.IO;\nclass Program {\n    static void Main() {\n        var lines = File.ReadAllLines(\"input.csv\");\n        Console.WriteLine(lines.Length);\n    }\n}\n",
            "project_data_pipeline": "using System;\nclass Program {\n    static void Main() {\n        string[] raw = { \"1\", \"2\", \"\", \"NA\", \"7\" };\n        int count = 0;\n        foreach (var value in raw) if (!string.IsNullOrWhiteSpace(value) && value != \"NA\") count++;\n        Console.WriteLine(count);\n    }\n}\n",
            "project_api": "using System;\nclass Program {\n    static void Main() { Console.WriteLine(\"API ready\"); }\n}\n",
            "project_http_service": "using System;\nclass Program { static void Main() { Console.WriteLine(\"HTTP service stub\"); } }\n",
            "project_file_system": "using System;\nusing System.IO;\nclass Program {\n    static void Main() { foreach (var file in Directory.GetFiles(\".\")) Console.WriteLine(file); }\n}\n",
            "project_database": "using System.Data.SQLite;\nclass Program {\n    static void Main() {\n        using var conn = new SQLiteConnection(\"Data Source=app.db\");\n        conn.Open();\n        using var cmd = new SQLiteCommand(\"CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)\", conn);\n        cmd.ExecuteNonQuery();\n    }\n}\n",
            "project_scheduler": "using System;\nusing System.Threading;\nclass Program {\n    static void Main() {\n        var timer = new Timer(_ => Console.WriteLine(\"tick\"), null, 5000, 5000);\n        Thread.Sleep(10000);\n    }\n}\n",
            "memory": "unsafe static void Copy(byte[] src, byte[] dst) {\n    fixed (byte* s = src, d = dst) {\n        Buffer.MemoryCopy(s, d, dst.Length, src.Length);\n    }\n}\n",
            "syscall": "using System.IO;\nFile.WriteAllText(\"/tmp/pid.txt\", System.Environment.ProcessId.ToString());\n",
            "ml_preprocessor": "using System;\nclass Program {\n    static void Main() {\n        int[] values = {10, 20, 30};\n        for (int i = 0; i < values.Length; i++) values[i] = values[i] / 10;\n        Console.WriteLine(string.Join(\", \", values));\n    }\n}\n",
            "project_full_stack": "using System;\nclass Program { static void Main() { Console.WriteLine(\"Full stack app stub\"); } }\n",
            "project_tooling": "using System;\nclass Program { static void Main(string[] args) { Console.WriteLine(args.Length > 0 ? args[0] : \"no argument\"); } }\n",
        }
        return samples[category]

    if language == "C++":
        samples = {
            "project_cli": "#include <iostream>\n#include <vector>\nint main() {\n    std::vector<int> values = {12, 18, 21, 9, 31};\n    int total = 0;\n    for (int value : values) total += value;\n    std::cout << \"Total: \" << total << '\\n';\n    std::cout << \"Average: \" << (total / static_cast<double>(values.size())) << '\\n';\n}\n",
            "project_parser": "#include <fstream>\n#include <iostream>\nint main() {\n    std::ifstream file(\"input.csv\");\n    std::string line;\n    int count = 0;\n    while (std::getline(file, line)) ++count;\n    std::cout << count << '\\n';\n}\n",
            "project_data_pipeline": "#include <iostream>\n#include <vector>\n#include <string>\nint main() {\n    std::vector<std::string> raw = {\"1\", \"2\", \"\", \"NA\", \"7\"};\n    int count = 0;\n    for (const auto& value : raw) if (!value.empty() && value != \"NA\") ++count;\n    std::cout << count << '\\n';\n}\n",
            "project_api": "#include <iostream>\nint main() { std::cout << \"API ready\\n\"; }\n",
            "project_http_service": "#include <iostream>\nint main() { std::cout << \"HTTP service stub\\n\"; }\n",
            "project_file_system": "#include <filesystem>\n#include <iostream>\nint main() {\n    for (const auto& entry : std::filesystem::directory_iterator(\".\")) std::cout << entry.path() << '\\n';\n}\n",
            "project_database": "#include <sqlite3.h>\nint main() { sqlite3* db = nullptr; sqlite3_open(\"app.db\", &db); sqlite3_close(db); return 0; }\n",
            "project_scheduler": "#include <thread>\n#include <chrono>\n#include <iostream>\nint main() {\n    std::this_thread::sleep_for(std::chrono::seconds(1));\n    std::cout << \"tick\\n\";\n}\n",
            "memory": "#include <cstring>\nvoid copy_bytes(unsigned char* dst, const unsigned char* src, size_t n) { std::memcpy(dst, src, n); }\n",
            "syscall": "#include <fstream>\nint main() { std::ofstream out(\"/tmp/pid.txt\"); out << getpid(); }\n",
            "ml_preprocessor": "#include <iostream>\n#include <vector>\nint main() {\n    std::vector<int> values = {10, 20, 30};\n    for (int& value : values) value /= 10;\n    for (int value : values) std::cout << value << ' ';\n}\n",
            "project_full_stack": "#include <iostream>\nint main() { std::cout << \"Full stack app stub\\n\"; }\n",
            "project_tooling": "#include <iostream>\nint main(int argc, char** argv) { std::cout << (argc > 1 ? argv[1] : \"no argument\") << '\\n'; }\n",
        }
        return samples[category]

    if language == "Go":
        samples = {
            "project_cli": "package main\n\nimport \"fmt\"\n\nfunc main() {\n    values := []int{12, 18, 21, 9, 31}\n    total := 0\n    for _, v := range values { total += v }\n    fmt.Println(\"Total:\", total)\n    fmt.Printf(\"Average: %.2f\\n\", float64(total)/float64(len(values)))\n}\n",
            "project_parser": "package main\n\nimport (\n    \"fmt\"\n    \"os\"\n)\n\nfunc main() {\n    data, _ := os.ReadFile(\"input.csv\")\n    fmt.Println(len(data))\n}\n",
            "project_data_pipeline": "package main\n\nimport \"fmt\"\n\nfunc main() {\n    raw := []string{\"1\", \"2\", \"\", \"NA\", \"7\"}\n    count := 0\n    for _, value := range raw { if value != \"\" && value != \"NA\" { count++ } }\n    fmt.Println(count)\n}\n",
            "project_api": "package main\n\nimport \"fmt\"\n\nfunc main() { fmt.Println(\"API ready\") }\n",
            "project_http_service": "package main\n\nimport \"fmt\"\n\nfunc main() { fmt.Println(\"HTTP service stub\") }\n",
            "project_file_system": "package main\n\nimport (\n    \"fmt\"\n    \"os\"\n)\n\nfunc main() {\n    entries, _ := os.ReadDir(\".\")\n    for _, entry := range entries { fmt.Println(entry.Name()) }\n}\n",
            "project_database": "package main\n\nimport \"database/sql\n\nfunc main() {\n    _ = sql.Open(\"sqlite3\", \"app.db\")\n}\n",
            "project_scheduler": "package main\n\nimport \"time\"\n\nfunc main() {\n    ticker := time.NewTicker(5 * time.Second)\n    defer ticker.Stop()\n    for range ticker.C { println(\"tick\") }\n}\n",
            "memory": "package main\n\nfunc copyBytes(dst, src []byte) { copy(dst, src) }\n",
            "syscall": "package main\n\nimport \"os\"\n\nfunc main() { _ = os.WriteFile(\"/tmp/pid.txt\", []byte(\"123\"), 0644) }\n",
            "ml_preprocessor": "package main\n\nimport \"fmt\"\n\nfunc main() {\n    values := []int{10, 20, 30}\n    for i := range values { values[i] /= 10 }\n    fmt.Println(values)\n}\n",
            "project_full_stack": "package main\n\nimport \"fmt\"\n\nfunc main() { fmt.Println(\"Full stack app stub\") }\n",
            "project_tooling": "package main\n\nimport (\n    \"fmt\"\n    \"os\"\n)\n\nfunc main() {\n    if len(os.Args) > 1 { fmt.Println(os.Args[1]) } else { fmt.Println(\"no argument\") }\n}\n",
        }
        return samples[category]

    if language == "Rust":
        samples = {
            "project_cli": "fn main() {\n    let values = [12, 18, 21, 9, 31];\n    let total: i32 = values.iter().sum();\n    println!(\"Total: {}\", total);\n    println!(\"Average: {:.2}\", total as f64 / values.len() as f64);\n}\n",
            "project_parser": "fn main() {\n    let raw = [\"1\", \"2\", \"\", \"NA\", \"7\"];\n    let count = raw.iter().filter(|v| !v.is_empty() && *v != \"NA\").count();\n    println!(\"{}\", count);\n}\n",
            "project_data_pipeline": "fn main() {\n    let raw = [\"1\", \"2\", \"\", \"NA\", \"7\"];\n    let clean: Vec<i32> = raw.iter().filter_map(|v| {\n        if !v.is_empty() && *v != \"NA\" { Some(v.parse::<i32>().unwrap()) } else { None }\n    }).collect();\n    println!(\"{:?}\", clean);\n}\n",
            "project_api": "fn main() { println!(\"API ready\"); }\n",
            "project_http_service": "fn main() { println!(\"HTTP service stub\"); }\n",
            "project_file_system": "fn main() { println!(\"File system example\"); }\n",
            "project_database": "fn main() { println!(\"Database example\"); }\n",
            "project_scheduler": "fn main() { println!(\"Scheduler example\"); }\n",
            "memory": "fn copy_bytes(dst: &mut [u8], src: &[u8]) { dst.copy_from_slice(src); }\n",
            "syscall": "use std::fs;\nfn main() { fs::write(\"/tmp/pid.txt\", std::process::id().to_string()).unwrap(); }\n",
            "ml_preprocessor": "fn main() {\n    let mut values = vec![10, 20, 30];\n    values.iter_mut().for_each(|v| *v /= 10);\n    println!(\"{:?}\", values);\n}\n",
            "project_full_stack": "fn main() { println!(\"Full stack app stub\"); }\n",
            "project_tooling": "fn main() { println!(\"tooling stub\"); }\n",
        }
        return samples[category]

    if language == "TypeScript":
        samples = {
            "project_cli": "const values = [12, 18, 21, 9, 31];\nconst total = values.reduce((sum, value) => sum + value, 0);\nconsole.log('Total:', total);\nconsole.log('Average:', (total / values.length).toFixed(2));\n",
            "project_parser": "const fs = require('fs');\nconst lines = fs.readFileSync('input.csv', 'utf8').trim().split('\n');\nconsole.log(lines.length);\n",
            "project_data_pipeline": "const raw = ['1', '2', '', 'NA', '7'];\nconst cleaned = raw.filter(v => v && v !== 'NA').map(Number);\nconsole.log(cleaned);\n",
            "project_api": "import express from 'express';\nconst app = express();\napp.get('/health', (_, res) => res.json({ status: 'ok' }));\napp.listen(3000);\n",
            "project_http_service": "import http from 'http';\nhttp.createServer((_, res) => res.end(JSON.stringify({ ok: true }))).listen(8080);\n",
            "project_file_system": "import fs from 'fs';\nfor (const name of fs.readdirSync('.')) if (name.endsWith('.ts')) console.log(name);\n",
            "project_database": "import sqlite3 from 'sqlite3';\nconst db = new sqlite3.Database('app.db');\ndb.run('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)');\n",
            "project_scheduler": "setInterval(() => console.log('tick'), 5000);\n",
            "memory": "function cloneBuffer(src: Uint8Array): Uint8Array { return new Uint8Array(src); }\n",
            "syscall": "import fs from 'fs';\nfs.writeFileSync('/tmp/pid.txt', String(process.pid));\n",
            "ml_preprocessor": "const normalize = (values: number[]) => values.map(v => v / Math.max(1, Math.max(...values)));\nconsole.log(normalize([10, 20, 30]));\n",
            "project_full_stack": "import express from 'express';\nconst app = express();\napp.get('/', (_, res) => res.json({ status: 'ready' }));\napp.listen(3000);\n",
            "project_tooling": "const args = process.argv.slice(2);\nconsole.log(args[0] || 'no argument');\n",
        }
        return samples[category]

    if language == "PHP":
        samples = {
            "project_cli": "<?php\n$values = [12, 18, 21, 9, 31];\n$total = array_sum($values);\necho 'Total: ' . $total . PHP_EOL;\necho 'Average: ' . ($total / count($values)) . PHP_EOL;\n",
            "project_parser": "<?php\n$lines = file('input.csv');\necho count($lines) . PHP_EOL;\n",
            "project_data_pipeline": "<?php\n$raw = ['1', '2', '', 'NA', '7'];\n$clean = array_filter($raw, fn($v) => $v !== '' && $v !== 'NA');\nprint_r(array_map('intval', $clean));\n",
            "project_api": "<?php\nheader('Content-Type: application/json');\necho json_encode(['status' => 'ok']);\n",
            "project_http_service": "<?php\nheader('Content-Type: application/json');\necho json_encode(['message' => 'pong']);\n",
            "project_file_system": "<?php\nforeach (scandir('.') as $entry) { if (str_ends_with($entry, '.php')) echo $entry . PHP_EOL; }\n",
            "project_database": "<?php\n$pdo = new PDO('sqlite:app.db');\n$pdo->exec('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)');\n",
            "project_scheduler": "<?php\nfor ($i = 0; $i < 3; $i++) { echo 'tick' . PHP_EOL; }\n",
            "memory": "<?php\nfunction copy_bytes(array $src): array { return array_values($src); }\n",
            "syscall": "<?php\nfile_put_contents('/tmp/pid.txt', getmypid());\n",
            "ml_preprocessor": "<?php\n$values = [10, 20, 30];\n$normalized = array_map(fn($v) => $v / max(1, max($values)), $values);\nprint_r($normalized);\n",
            "project_full_stack": "<?php\nheader('Content-Type: application/json');\necho json_encode(['status' => 'ready']);\n",
            "project_tooling": "<?php\n$arg = $argv[1] ?? 'no argument';\necho $arg . PHP_EOL;\n",
        }
        return samples[category]

    if language == "Ruby":
        samples = {
            "project_cli": "items = [12, 18, 21, 9, 31]\ntotal = items.sum\nputs \"Total: #{total}\"\nputs \"Average: #{(total / items.length.to_f).round(2)}\"\n",
            "project_parser": "lines = File.readlines('input.csv')\nputs lines.length\n",
            "project_data_pipeline": "raw = ['1', '2', '', 'NA', '7']\nclean = raw.reject { |v| v.empty? || v == 'NA' }.map(&:to_i)\np clean\n",
            "project_api": "puts 'API ready'\n",
            "project_http_service": "puts 'HTTP service stub'\n",
            "project_file_system": "Dir.children('.').grep(/\\.rb$/).each { |name| puts name }\n",
            "project_database": "require 'sqlite3'\nSQLite3::Database.new('app.db')\n",
            "project_scheduler": "3.times { puts 'tick' }\n",
            "memory": "def copy_bytes(src, dst)\n  src.each_with_index { |byte, idx| dst[idx] = byte }\n  dst\nend\n",
            "syscall": "File.write('/tmp/pid.txt', Process.pid.to_s)\n",
            "ml_preprocessor": "values = [10, 20, 30]\nnormalized = values.map { |v| v / [1, values.max].max.to_f }\np normalized\n",
            "project_full_stack": "puts 'Full stack app stub'\n",
            "project_tooling": "arg = ARGV[0] || 'no argument'\nputs arg\n",
        }
        return samples[category]

    raise ValueError(f"Language not supported: {language}")


# Create project bundles with multiple files per language
for language in LANGUAGES:
    lang_dir = BUNDLE_DIR / LANGUAGE_SLOUGNS[language]
    lang_dir.mkdir(parents=True, exist_ok=True)
    (lang_dir / "README.md").write_text(
        f"# {language} project bundle\n\nThis bundle shows an end-to-end project pattern for {language}.\n\nFiles included:\n- app{EXTENSIONS[language]}\n- helpers{EXTENSIONS[language]}\n- config/settings.json\n- data/sample.csv\n- tests/test_{LANGUAGE_SLOUGNS[language]}{EXTENSIONS[language]}\n- assembly_example.asm\n- binary_example.txt\n",
        encoding="utf-8",
    )
    (lang_dir / "app").mkdir(exist_ok=True)
    (lang_dir / "app" / f"main{EXTENSIONS[language]}").write_text(make_program(language, "project_cli", "base"), encoding="utf-8")
    (lang_dir / "helpers").mkdir(exist_ok=True)
    (lang_dir / "helpers" / f"helpers{EXTENSIONS[language]}").write_text(make_program(language, "project_tooling", "base"), encoding="utf-8")
    (lang_dir / "config").mkdir(exist_ok=True)
    (lang_dir / "config" / "settings.json").write_text(json.dumps({"language": language, "mode": "training", "features": ["cli", "parser", "pipeline"]}, indent=2), encoding="utf-8")
    (lang_dir / "data").mkdir(exist_ok=True)
    (lang_dir / "data" / "sample.csv").write_text("id,amount\n1,12\n2,18\n3,9\n", encoding="utf-8")
    (lang_dir / "tests").mkdir(exist_ok=True)
    (lang_dir / "tests" / f"test_{LANGUAGE_SLOUGNS[language]}{EXTENSIONS[language]}").write_text(make_program(language, "project_parser", "base"), encoding="utf-8")
    (lang_dir / "assembly_example.asm").write_text(get_assembly(language), encoding="utf-8")
    (lang_dir / "binary_example.txt").write_text(get_binary(language), encoding="utf-8")

records = []
for language in LANGUAGES:
    for category in CATEGORIES:
        for variant in ["v1", "v2"]:
            record = {
                "dataset_id": f"{LANGUAGE_SLOUGNS[language]}_{category}_{variant}",
                "language": language,
                "category": category,
                "source_type": "organic" if category in {"project_parser", "project_data_pipeline", "project_file_system", "project_database", "ml_preprocessor"} else "synthetic",
                "valid": True,
                "difficulty": "core" if category not in {"memory", "syscall", "assembly", "binary"} else "low_level",
                "text": get_assembly(language) if category == "assembly" else get_binary(language) if category == "binary" else make_program(language, category, variant),
                "labels": json.dumps(["project_training", language.lower(), category, "llm_learning"], ensure_ascii=False),
                "notes": f"{language} {category} {variant} sample built for end-to-end LLM training and project generation." 
            }
            records.append(record)

csv_path = DATA_DIR / "large_project_training_corpus.csv"
with csv_path.open("w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ["dataset_id", "language", "category", "source_type", "valid", "difficulty", "labels", "text", "notes"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

jsonl_path = DATA_DIR / "large_project_training_corpus.jsonl"
with jsonl_path.open("w", encoding="utf-8") as jsonl_file:
    for record in records:
        jsonl_file.write(json.dumps(record, ensure_ascii=False) + "\n")

manifest = {
    "title": "Large Project Training Corpus",
    "languages": LANGUAGES,
    "categories": CATEGORIES,
    "record_count": len(records),
    "source_mix": {
        "organic": sum(1 for row in records if row["source_type"] == "organic"),
        "synthetic": sum(1 for row in records if row["source_type"] == "synthetic"),
    },
    "project_bundle_count": len(LANGUAGES),
    "description": "Expansive LLM and ML corpus for complete project generation, end-to-end reasoning, and low-level language learning including assembly and binary samples.",
    "training_goals": [
        "generate working projects",
        "reason about architecture",
        "parse, transform, and store data",
        "handle system/filesystem operations",
        "understand low-level instruction patterns",
        "generate code across multiple languages"
    ],
}
manifest_path = DATA_DIR / "manifest.json"
manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

readme = ROOT / "README.md"
readme.write_text(
    "# Large LLM Programming Project Corpus\n\n"
    "This dataset expands into full project bundles and training samples for the top 10 languages.\n\n"
    "## Included languages\n\n"
    + "\n".join(f"- {language}" for language in LANGUAGES)
    + "\n\n"
    "## Included outputs\n\n"
    "- large_training_corpus_v2/\n- project_bundles_v2/\n\n"
    "## Purpose\n\n"
    "- Teach LLMs to generate complete projects\n- Cover project structure, parsing, APIs, filesystems, memory, and syscalls\n- Include low-level assembly and binary samples for each language\n",
    encoding="utf-8",
)

print(f"Generated {len(records)} records across {len(LANGUAGES)} languages.")
print(f"CSV: {csv_path}")
print(f"JSONL: {jsonl_path}")
print(f"Project bundles: {BUNDLE_DIR}")
