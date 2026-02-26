# Task 5 — Export parsed results to JSON (Lesson 1)

import json
from pathlib import Path
from task1_parse_single import parse_log_line

LOG_PATH = Path("sample_logs.txt")
OUT_PATH = Path("parsed_logs.json")

def main():
    if not LOG_PATH.exists():
        print("ERROR: sample_logs.txt not found in the same folder.")
        return

    output = []
    for line in LOG_PATH.read_text(encoding="utf-8").splitlines():
        parsed = parse_log_line(line)
        if parsed is None:
            continue
        timestamp, level, service, message = parsed
        output.append({
            "timestamp": timestamp,
            "level": level,
            "service": service,
            "message": message
        })

    OUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Wrote {len(output)} records to {OUT_PATH}")

if __name__ == "__main__":
    main()
