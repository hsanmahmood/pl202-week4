# pl202-week4

NV24212 Hasan Mahmood | 11.CCP

## Description

A log parsing toolkit for a cloud operations scenario. Parses log lines in the format `timestamp | level | service | message`, handles invalid/malformed lines, and exports results to JSON.

- **Task 1** — Parse a single log line into a tuple
- **Task 2** — Parse a list of log lines, skipping invalid ones
- **Task 3** — Read and parse a log file, print first 5 valid entries
- **Task 4** — Count total, valid, and invalid format lines
- **Task 5** — Export parsed log data to JSON

---

## Quiz Revision Notes

### 1. String Stripping (`str.strip()`)
- `strip()` removes leading and trailing whitespace (spaces, tabs, newlines)
- Always strip the whole line first before doing anything else
- After splitting, strip each individual field too
- An empty string after stripping means the line is invalid

```python
line = line.strip()          # "  hello  \n" -> "hello"
if not line:                 # empty string is falsy
    return None
```

### 2. String Splitting (`str.split()`)
- `split('|')` splits a string into a list using `|` as the delimiter
- The number of parts tells you if the format is valid
- `"A | B | C | D".split('|')` gives `['A ', ' B ', ' C ', ' D ']` (4 parts)
- `"NO PIPES HERE".split('|')` gives `['NO PIPES HERE']` (1 part — invalid)

```python
parts = line.split('|')
```

### 3. List Comprehension for Stripping Parts
- After splitting, each part may have extra spaces
- Use a list comprehension to strip all parts at once

```python
parts = [p.strip() for p in parts]
```

### 4. Validating Field Count
- The log format requires exactly 4 fields: timestamp, level, service, message
- If `len(parts) != 4`, the line is invalid — return `None`
- Too few fields (e.g. `"INVALID|TOO|FEW"` → 3 parts) = invalid
- Too many fields (e.g. `"A | B | C | D | EXTRA"` → 5 parts) = invalid

### 5. Returning a Tuple
- `tuple(parts)` converts a list to a tuple
- Tuples are immutable (cannot be changed after creation)
- A valid return looks like: `('2026-02-05 08:11:20', 'ERROR', 'db', 'DB timeout')`
- Invalid lines return `None`

### 6. Tuple Unpacking
- You can unpack a tuple into individual variables:

```python
timestamp, level, service, message = parsed
```

### 7. File Reading (`pathlib` / `open()`)
- `Path("file.txt").read_text(encoding="utf-8")` reads the entire file as a string
- `.splitlines()` splits text into a list of lines (without `\n`)
- Process each line in a `for` loop

```python
for line in Path("file.txt").read_text(encoding="utf-8").splitlines():
    parsed = parse_log_line(line)
```

### 8. Filtering Invalid Lines
- When `parse_log_line()` returns `None`, skip that line
- Use `if parsed is not None` or `if parsed is None: continue`

```python
if parsed is not None:
    valid.append(parsed)
```

### 9. Counting with Accumulators
- Use counter variables initialized to 0
- Increment inside a loop based on conditions

```python
total = 0
valid = 0
invalid = 0
for line in lines:
    total += 1
    if parse_log_line(line) is None:
        invalid += 1
    else:
        valid += 1
```

### 10. JSON Export (`json` module)
- `json.dumps(data, indent=2)` converts a Python object to a JSON string
- Export a list of dictionaries, each with keys: timestamp, level, service, message
- `Path("out.json").write_text(...)` writes the JSON string to a file

```python
import json
output = []
output.append({
    "timestamp": timestamp,
    "level": level,
    "service": service,
    "message": message
})
Path("out.json").write_text(json.dumps(output, indent=2), encoding="utf-8")
```

### Key Concepts Summary
| Concept | Python Feature |
|---|---|
| Remove whitespace | `str.strip()` |
| Split by delimiter | `str.split('|')` |
| Check field count | `len(parts) != 4` |
| Return structured data | `tuple()` |
| Skip bad data | `return None` / `if x is None` |
| Read a file | `Path.read_text()` / `open()` |
| Export to JSON | `json.dumps()` |
| List comprehension | `[p.strip() for p in parts]` |

