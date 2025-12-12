[![HF Dataset](https://img.shields.io/badge/HF-Dataset-yellow)](https://huggingface.co/datasets/Yukyin/moodtrace-20d)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

# MoodTrace Benchmark (v0.1)

MoodTrace is a longitudinal emotion dialogue benchmark scaffold.

This package provides:
- `load_dataset(name, data_path=..., max_records=...)` to load a pair-level JSONL dataset
- `EmotionalEval(model).evaluate(ds)` to run a minimal **stats-only** evaluation (no LLM calls in v0.1)

## Install

```bash
pip install -e .
```

## Quickstart (recommended: env var)

1) Point to your local JSONL file:

```bash
export MOODTRACE_DATA_PATH=/path/to/all_clean.jsonl
```

2) Run:

```bash
python -c "from moodtrace_benchmark import load_dataset, EmotionalEval; ds=load_dataset('MoodTrace-20D'); print(EmotionalEval('mock').evaluate(ds))"
```

## Alternative: pass `data_path` explicitly

```bash
python -c "from moodtrace_benchmark import load_dataset, EmotionalEval; ds=load_dataset('MoodTrace-20D', data_path='/path/to/all_clean.jsonl'); print(EmotionalEval('mock').evaluate(ds))"
```

## Notes

- Dataset name: `MoodTrace-20D`
- Input format: JSONL, one record per line (pair-level).
- v0.1 only computes dataset statistics. Future versions will add model generation + LLM-judge metrics (e.g., empathy, actionability).
