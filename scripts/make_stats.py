import json
from moodtrace_benchmark import load_dataset, EmotionalEval

def main():
    ds = load_dataset("MoodTrace-20D")  # will use MOODTRACE_DATA_PATH
    score = EmotionalEval("mock").evaluate(ds)
    with open("stats.json", "w", encoding="utf-8") as f:
        json.dump(score, f, ensure_ascii=False, indent=2)
    print("[OK] wrote stats.json")
    print(json.dumps(score, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
