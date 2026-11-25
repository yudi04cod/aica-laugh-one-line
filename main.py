#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt.

Deterministic, stdlib only, no network, no randomness. The line is a
self-contained joke: a fridge filing for divorce, with the punchline
landing on the double meaning of "committing".
"""

import os

# Gate: 1-200 chars per the competition rules; we stay under 200 with
# margin so the scorer's 1-200 window is comfortably met.
MAX_LEN = 199

LINE = (
    "My fridge filed for divorce \u2014 it says I only open it at 2 a.m., "
    "stare inside for five minutes, and leave without committing to anything."
)


def main():
    line = LINE
    if not (1 <= len(line) <= MAX_LEN):
        raise SystemExit(f"line is {len(line)} chars, must be 1-199")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if not line.strip():
        raise SystemExit("line must not be only whitespace")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != line + "\n":
        raise SystemExit("read-back mismatch")
    print(f"Wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
