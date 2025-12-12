# -*- coding: utf-8 -*-
import os
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from tqdm import tqdm


def _read_jsonl(path: Path, max_records: Optional[int] = None) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if max_records is not None and i >= max_records:
                break
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def load_dataset(
    name: str,
    *,
    data_path: Optional[str] = None,
    max_records: Optional[int] = None,
) -> List[Dict[str, Any]]:
    """
    Load MoodTrace dataset from a local JSONL file.

    Option A: pass data_path explicitly
      load_dataset("MoodTrace-20D", data_path="/path/to/all_clean.jsonl")

    Option B: set env var once
      export MOODTRACE_DATA_PATH=/path/to/all_clean.jsonl
      load_dataset("MoodTrace-20D")
    """
    if name != "MoodTrace-20D":
        raise ValueError("Unknown dataset name. Use name='MoodTrace-20D'.")

    if data_path is None:
        data_path = os.environ.get("MOODTRACE_DATA_PATH")

    if not data_path:
        raise ValueError(
            "Pass data_path=... or set MOODTRACE_DATA_PATH=/path/to/all_clean.jsonl"
        )

    path = Path(data_path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found: {path}")

    return _read_jsonl(path, max_records=max_records)


@dataclass
class EmotionalEval:
    """
    v0.1: stats-only evaluator (no model calls yet).
    """
    model: str = "mock"

    def evaluate(self, ds: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
        n = 0
        n_user_empty = 0
        durations: List[int] = []
        user_lens: List[int] = []
        asst_lens: List[int] = []

        ds_list = list(ds)

        for r in tqdm(ds_list, desc="Evaluating MoodTrace (v0.1: stats)", unit="rec"):
            n += 1
            user = (r.get("user_text") or "").strip()
            asst = (r.get("assistant_text") or "").strip()
            if not user:
                n_user_empty += 1

            d = r.get("user_duration_sec")
            if isinstance(d, int):
                durations.append(d)

            user_lens.append(len(user))
            asst_lens.append(len(asst))

        durations_sorted = sorted(durations)

        def pct(p: float):
            if not durations_sorted:
                return None
            idx = int(round(p * (len(durations_sorted) - 1)))
            return durations_sorted[idx]

        def avg(xs: List[int]) -> float:
            return float(sum(xs) / len(xs)) if xs else 0.0

        return {
            "benchmark": "MoodTrace-20D",
            "evaluator": self.model,
            "records": n,
            "user_text_empty": n_user_empty,
            "user_text_empty_rate": (n_user_empty / n) if n else 0.0,
            "user_duration_count": len(durations),
            "user_duration_sec_p50": pct(0.50),
            "user_duration_sec_p90": pct(0.90),
            "user_duration_sec_p99": pct(0.99),
            "avg_user_chars": avg(user_lens),
            "avg_assistant_chars": avg(asst_lens),
        }
