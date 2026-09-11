# ML Programming Top 10

![ML Programming Top 10 banner](assets/hero-banner.svg)

![10 Languages](https://img.shields.io/badge/10-Languages-blue)
![10k+ Task Records](https://img.shields.io/badge/10k%2B-Task%20Records-orange)
![Train%2FVal%2FTest](https://img.shields.io/badge/Train%2FVal%2FTest-Splits-green)
![Assembly + Binary](https://img.shields.io/badge/Assembly%2BBinary-Included-purple)
![Release v1.1.0](https://img.shields.io/badge/Release-v1.1.0-9cf)

A multilingual programming dataset and benchmark suite for LLM and ML training. This repository is designed to teach models how to write, debug, refactor, explain, and reason about code in real-world project patterns across the most common programming languages.

The corpus includes:

- high-quality multilingual programming tasks
- project-style file layouts and project scaffolding patterns
- assembly and binary references for low-level reasoning
- benchmark train/validation/test splits
- task-driven examples for generation, repair, debugging, and refactoring
- a mixed synthetic and realistic dataset strategy for broader learning coverage

This repository is optimized for discovery in searches for: machine learning dataset, LLM training data, multilingual programming dataset, code generation dataset, AI training data, programming benchmark, multilingual code corpus, assembly dataset, and binary learning data.

## Why this corpus matters

Most code datasets are built around snippets. This project is built around the way software is actually created and reviewed: tasks, project structure, edge cases, repair workflows, and reasoning across languages.

It is useful for training models that need to:

- generate working code across multiple languages
- understand folder layouts, filesystems, and project conventions
- debug broken behavior and repair code systematically
- explain logic and refactor patterns clearly
- work with low-level memory, assembly, and binary concepts
- evaluate performance on benchmark splits that mirror real task flows

## Languages included

- Python
- JavaScript
- Java
- C#
- C++
- Go
- Rust
- TypeScript
- PHP
- Ruby

## Current dataset suite

### 1. 10k multilingual task corpus

The main training corpus is a large, structured JSONL set with 10,000 records spanning the 10 languages and multiple task types.

Included task modes:

- generate
- repair
- refactor
- debug
- explain

This corpus is useful for training models on instruction-following, code synthesis, and code reasoning behavior.

### 2. Bug-fix corpus

A dedicated repair-focused dataset built around broken examples, fix expectations, and validation-oriented prompts.

### 3. Benchmark splits

The repository includes benchmark-ready data splits for reproducible evaluation:

- train: 8400
- validation: 1800
- test: 1800

### 4. Low-level and binary reasoning data

The project includes low-level tasks centered on:

- memory behavior
- syscall-like patterns
- assembly-oriented examples
- binary-style control-flow understanding
- system-level reasoning without relying on brittle false-positive samples

## Repository structure

```text
ml_programming_top10/
├── README.md
├── pytest.ini
├── run_dataset.cmd
├── generate_dataset.py
├── generate_extended_low_level_dataset.py
├── generate_large_corpus.py
├── generate_large_corpus_v2.py
├── generate_multilingual_benchmark.py
├── generate_task_corpus.py
├── generate_10k_multilingual_corpus.py
├── generate_bugfix_corpus.py
├── generate_benchmark_splits.py
├── TASK_CORPUS_PLAN.md
├── .vscode/
│   └── settings.json
├── assets/
│   └── hero-banner.svg
├── data/
├── low_level_data/
├── large_training_corpus/
├── large_training_corpus_v2/
├── project_examples/
├── project_bundles_v2/
├── multilingual_benchmark/
├── multilingual_benchmark_bundles/
├── task_corpus/
├── task_corpus_10k/
├── bugfix_corpus/
├── benchmark_splits/
├── tests/
└── .github/
```

## Core generation scripts

- `generate_10k_multilingual_corpus.py` — builds the 10k multilingual task corpus
- `generate_task_corpus.py` — generates a task-oriented corpus with prompt and validation metadata
- `generate_bugfix_corpus.py` — produces a targeted repair dataset
- `generate_benchmark_splits.py` — creates train/validation/test partitions
- `generate_multilingual_benchmark.py` — builds benchmark-quality multilingual outputs
- `generate_extended_low_level_dataset.py` — creates low-level reasoning examples
- `generate_large_corpus.py` and `generate_large_corpus_v2.py` — scale corpus generation and project-style examples

## Example project layout

Each generated sample is designed to resemble a small but real project:

```text
project/
├── README.md
├── main.{ext}
├── helpers.{ext}
├── assembly_example.asm
├── binary_example.txt
├── tests/
├── data/
├── config/
└── app/
```

This makes the corpus more useful for models that need to reason across real software structures instead of isolated snippets.

## Quick start

Run the 10k corpus generator:

```bash
python generate_10k_multilingual_corpus.py
```

Generate benchmark splits:

```bash
python generate_benchmark_splits.py
```

Or use the Windows launcher:

```cmd
run_dataset.cmd
```

## Why this works for LLM and ML workflows

- broad language coverage across major ecosystems
- task-driven prompts for generation, repair, and reasoning
- structured metadata for validation and benchmarking
- strong low-level coverage including assembly and binary concepts
- project-aware layouts to better simulate real-world engineering tasks
- balanced mix of realistic and synthetic examples for broader model coverage

## Usage notes

This repository is intended for research, experimentation, benchmarking, and model training. The data is designed to be practical and operational while reducing false positives by combining realistic app patterns with synthetic coverage when useful.

---

Built for code generation, systems reasoning, multilingual AI training, and robust benchmark evaluation.
