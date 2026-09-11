# Task-Driven LLM Training Corpus Plan

This document defines the next generation of the dataset: a task-based multilingual corpus designed for code generation, debugging, repair, and project-level reasoning.

## 1. Goal

The current corpus is strong on breadth and project-style examples. The next step is to convert it into a task-grounded dataset so models learn not just code syntax, but how to:

- understand requirements
- plan a project structure
- write working code
- validate outputs
- repair failing implementations
- reason across files and modules

## 2. Dataset structure

Each record should include:

- `record_id`
- `language`
- `difficulty`
- `domain`
- `task_type`
- `prompt`
- `requirements`
- `project_structure`
- `reference_solution`
- `tests`
- `expected_output`
- `validation_status`
- `source_type`
- `tags`

Example record:

```json
{
  "record_id": "python_cli_000123",
  "language": "Python",
  "difficulty": "intermediate",
  "domain": ["cli", "data-processing"],
  "task_type": "generate",
  "prompt": "Write a CLI that reads input.csv and prints the sum of the amount column.",
  "requirements": [
    "read a CSV file",
    "sum the amount column",
    "print a formatted total",
    "handle missing values"
  ],
  "project_structure": {
    "files": ["main.py", "data/input.csv", "tests/test_main.py"]
  },
  "reference_solution": "def main():\n    ...",
  "tests": ["assert total == 1250.00"],
  "expected_output": "Revenue: 1250.00",
  "validation_status": {
    "runs": true,
    "compiles": true,
    "unit_tests_passed": true
  },
  "source_type": "mixed",
  "tags": ["multilingual", "benchmark", "cli", "csv"]
}
```

## 3. Three-tier corpus model

### Tier 1: Snippet corpus

Purpose: teach syntax, common APIs, and language idioms.

Includes:

- utility functions
- file I/O
- parsing examples
- sorting and filtering
- CLI arguments
- memory and syscall primitives
- assembly and binary references

### Tier 2: Project bundle corpus

Purpose: teach file structure, architecture, and multi-file reasoning.

Includes:

- README files
- app modules
- helper files
- tests
- config folders
- data directories

### Tier 3: Task-completion benchmark corpus

Purpose: train the model to understand prompts, requirements, and end-to-end correctness.

Includes:

- prompt + requirements
- test harness or assertions
- reference output
- project scaffold
- repair and bug-fix tasks

## 4. Recommended record mix

For the next expansion, aim for:

- 40% project-style tasks
- 30% snippet and utility tasks
- 15% bug-fix and repair tasks
- 10% systems and low-level reasoning
- 5% explanation and documentation tasks

## 5. Expansion roadmap

### Phase 1: 10,000-record foundation

- 1,000 records per language across 10 languages
- benchmark categories for CLI, parser, API, pipeline, memory, file-system, scheduler

### Phase 2: 25,000 realistic coding tasks

- bug fix tasks
- refactorings
- project scaffolds
- parsing and validation tasks

### Phase 3: 50,000 systems and low-level tasks

- assembly and binary reasoning
- memory layout
- syscall semantics
- disassembly explanation
- optimization tasks

### Phase 4: 100,000 benchmark set

- train/validation/test splits
- no-overlap filtering
- difficulty labeling
- domain balancing
- validation report generation

## 6. Why this matters

This version makes the repo more useful for actual LLM training because it teaches:

- planning before coding
- project-aware code generation
- validation and verification
- debugging and repair flows
- low-level and language-specific reasoning

That is the gap between a broad code corpus and an effective coding model dataset.

## 7. Next implementation

The repository now includes a generator for task-driven training records in `generate_task_corpus.py`.

This script produces structured JSONL and manifest output under `task_corpus/` and is designed to expand toward the full benchmark-level dataset described above.
