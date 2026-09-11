# ML Programming Top 10

<p align="center">
  <img src="https://img.shields.io/badge/10-Languages-blue" alt="10 languages" />
  <img src="https://img.shields.io/badge/1200-Benchmark%20Rows-orange" alt="1200 benchmark rows" />
  <img src="https://img.shields.io/badge/Train%2FVal%2FTest-Splits-green" alt="Train validation test" />
  <img src="https://img.shields.io/badge/Assembly%2BBinary-Included-purple" alt="assembly and binary included" />
</p>

A large-scale multilingual programming corpus for LLM and ML training, built for realistic software generation, code understanding, and low-level reasoning across the most widely used languages.

This repository combines:

- high-level language examples
- complete project-style bundles
- low-level assembly and binary samples
- benchmark splits for training, validation, and testing
- realistic and synthetic examples for safer, broader model learning

## Why this corpus exists

The goal is to train models that can:

- generate working code across major languages
- understand project structure beyond single snippets
- reason about system-level concepts like memory, syscalls, and binaries
- handle low-level artifacts without producing brittle or false-positive examples
- work from start-to-finish project patterns, not just toy examples

## Languages included

| Language | Strength in training | Notes |
| --- | --- | --- |
| Python | General-purpose ML and scripting | Easy to read and highly practical |
| JavaScript | Web and runtime logic | Strong for client-side and scripting tasks |
| TypeScript | Typed application generation | Excellent for production-scale app patterns |
| Java | Structured enterprise code | Great for object-oriented patterns |
| C# | .NET and app development | Useful for clean software architecture examples |
| C++ | Systems and performance code | Strong for memory and binary concepts |
| Go | Cloud-native tooling | Clean concurrency and CLI patterns |
| Rust | Safe systems programming | Great for low-level reliability examples |
| PHP | Web backend patterns | Useful for server-side logic |
| Ruby | Scripting and web development | Good for expressive automation examples |

## Repository structure

```text
ml_programming_top10/
├── README.md
├── run_dataset.cmd
├── validate_large_corpus_v2.py
├── generate_dataset.py
├── generate_extended_low_level_dataset.py
├── generate_large_corpus.py
├── generate_large_corpus_v2.py
├── generate_multilingual_benchmark.py
├── data/
│   ├── manifest.json
│   └── programming_top10_with_assembly_and_binary.csv
├── low_level_data/
│   ├── manifest.json
│   └── low_level_training_dataset.csv
├── large_training_corpus/
│   ├── manifest.json
│   └── large_llm_training_corpus.csv
├── large_training_corpus_v2/
│   ├── manifest.json
│   └── large_project_training_corpus.csv
├── project_examples/
│   ├── python/
│   ├── javascript/
│   ├── java/
│   ├── csharp/
│   ├── cpp/
│   ├── go/
│   ├── rust/
│   ├── typescript/
│   ├── php/
│   └── ruby/
├── project_bundles_v2/
│   ├── python/
│   ├── javascript/
│   ├── java/
│   ├── csharp/
│   ├── cpp/
│   ├── go/
│   ├── rust/
│   ├── typescript/
│   ├── php/
│   └── ruby/
├── multilingual_benchmark/
│   ├── manifest.json
│   ├── multilingual_benchmark.csv
│   ├── train.csv
│   ├── validation.csv
│   ├── test.csv
│   ├── multilingual_benchmark.jsonl
│   ├── train.jsonl
│   ├── validation.jsonl
│   └── test.jsonl
└── multilingual_benchmark_bundles/
    ├── python/
    ├── javascript/
    ├── java/
    ├── csharp/
    ├── cpp/
    ├── go/
    ├── rust/
    ├── typescript/
    ├── php/
    └── ruby/
```

## Dataset suites included

### 1. Core corpus
The base multilingual dataset includes programming examples, low-level patterns, and assembly/binary references across all 10 languages.

### 2. Low-level training data
Targeted data for:

- memory behavior
- syscall patterns
- binary structures
- assembly logic
- low-level operational reasoning

### 3. Large project corpus
Expands from isolated snippets into realistic project layout patterns such as:

- CLI tools
- parsing logic
- API clients
- data pipelines
- filesystem operations
- system utilities

### 4. Benchmark-grade corpus
The benchmark set includes a 1200-record multilingual corpus with a clean split:

- train: 840
- validation: 180
- test: 180

This makes it suitable for training and evaluation pipelines that need consistent language coverage and repeatable benchmarks.

## Example project bundle structure

Each language bundle includes a small realistic project structure, often containing:

```text
project/
├── README.md
├── main.{ext}
├── helpers.{ext}
├── assembly_example.asm
├── binary_example.txt
├── config/
├── data/
├── tests/
└── app/
```

This is designed to teach models how full software starts, evolves, and is organized, rather than only isolated functions.

## What makes this useful for LLM/ML training

- language diversity across 10 major ecosystems
- low-level reasoning alongside application-level tasks
- assembly and binary examples included for each language path
- realistic and synthetic samples blended for broader coverage
- full corpora and benchmark splits ready for data pipelines

## Quick start

From the project folder, run:

```bash
python generate_multilingual_benchmark.py
```

Or use the Windows launcher:

```cmd
run_dataset.cmd
```

## Notes

This project is intended for research, experimentation, and model training workflows. It emphasizes practical, operational code patterns with mixed organic and synthetic content to reduce false positives while preserving realism.

## License and usage

Use this dataset for educational, research, and model-training exploration. If you build on it in a downstream project, keep references and documentation clear about the source corpus and any modifications you make.

---

Built for code generation, systems reasoning, and multilingual model training.
