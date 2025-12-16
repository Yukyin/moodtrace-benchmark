[![HF Dataset](https://img.shields.io/badge/HF-Dataset-yellow)](https://huggingface.co/datasets/Yukyin/moodtrace-20d)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

# MoodTrace Benchmark (v1.0)

MoodTrace is a longitudinal emotion dialogue benchmark scaffold.

This package provides:
- `load_dataset(name, data_path=..., max_records=...)` to load a pair-level JSONL dataset
- `EmotionalEval(model).evaluate(ds)` to run a minimal **stats-only** evaluation (no LLM calls in v1.0)

Dataset: https://huggingface.co/datasets/Yukyin/moodtrace-20d

## Install

```bash
pip install git+https://github.com/Yukyin/moodtrace-benchmark.git
```

## Quickstart (recommended: env var)

1) Point to your local JSONL file (download from the HF dataset repo):

```bash
export MOODTRACE_DATA_PATH=/absolute/path/to/all.jsonl
# or: /absolute/path/to/train.jsonl
# or: /absolute/path/to/valid.jsonl
# or: /absolute/path/to/test.jsonl

```

2) Run:

```bash
python - << 'PY'
from moodtrace_benchmark import load_dataset, EmotionalEval

ds = load_dataset("MoodTrace-20D")
print(EmotionalEval("mock").evaluate(ds))
PY
```

## Alternative: pass `data_path` explicitly

```bash
python - << 'PY'
from moodtrace_benchmark import load_dataset, EmotionalEval

ds = load_dataset("MoodTrace-20D", data_path="/absolute/path/to/all.jsonl")
print(EmotionalEval("mock").evaluate(ds))
PY
```

## Notes

- Dataset name: `MoodTrace-20D`
- Input format: JSONL, one record per line (pair-level).
- v1.0 only computes dataset statistics. Future versions will add model generation + LLM-judge metrics (e.g., empathy, actionability).

## Citation

```bibtex
@misc{moodtrace2025,
  title        = {MoodTrace Benchmark v1.0},
  author       = {Yuyan Chen},
  year         = {2025},
  howpublished = {\url{https://github.com/Yukyin/moodtrace-benchmark}},
  note         = {Dataset: \url{https://huggingface.co/datasets/Yukyin/moodtrace-20d}},
  version      = {v1.0}
}

