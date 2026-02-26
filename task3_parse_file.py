# Task 3 — Parse a log file line-by-line (Lesson 1)

from pathlib import Path
from task1_parse_single import parse_log_line

LOG_PATH = Path("sample_logs.txt")

def main():
    if not LOG_PATH.exists():
        print("ERROR: sample_logs.txt not found in the same folder.")
        return

    valid = []
    for line in LOG_PATH.read_text(encoding="utf-8").splitlines():
        parsed = parse_log_line(line)
        if parsed is not None:
            valid.append(parsed)

    print("First 5 valid parsed lines:")
    for item in valid[:5]:
        print(item)

if __name__ == "__main__":
    main()
