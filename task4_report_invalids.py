# Task 4 — Count invalid format lines (Lesson 1)

from pathlib import Path
from task1_parse_single import parse_log_line

LOG_PATH = Path("sample_logs.txt")

def main():
    if not LOG_PATH.exists():
        print("ERROR: sample_logs.txt not found in the same folder.")
        return

    total = 0
    valid = 0
    invalid = 0

    for line in LOG_PATH.read_text(encoding="utf-8").splitlines():
        total += 1
        parsed = parse_log_line(line)
        if parsed is None:
            invalid += 1
        else:
            valid += 1

    print(f"Total lines: {total}")
    print(f"Valid lines: {valid}")
    print(f"Invalid format lines: {invalid}")

if __name__ == "__main__":
    main()
