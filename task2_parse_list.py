# Task 2 — Parse a list of log lines (Lesson 1)

from task1_parse_single import parse_log_line

LINES = [
    "2026-02-05 08:11:20 | ERROR | db | DB timeout",
    "BAD LINE WITHOUT SEPARATORS",
    "2026-02-05 08:11:25 | warn | api | Slow response (920ms)",
    "2026-02-05 | INFO | auth | ok | EXTRA",
]

def parse_lines(lines):
    # TODO: return a list of parsed tuples (skip invalid lines)
    parsed = []
    for line in lines:
        item = parse_log_line(line)
        if item is not None:
            parsed.append(item)
    return parsed

if __name__ == "__main__":
    result = parse_lines(LINES)
    print("Parsed results:")
    for r in result:
        print(r)
