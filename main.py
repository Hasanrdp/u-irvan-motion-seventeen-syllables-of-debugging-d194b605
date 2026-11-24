#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging (5-7-5, three lines) to /output/entry.txt.
Deterministic: the same bytes on every run, no network, no randomness.
"""

import os

HAIKU = (
    "breakpoint set, breath held\n"
    "the code strolls past, unbothered\n"
    "the bug has moved house"
)

# The house gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space. The haiku is three lines, 5-7-5.
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    lines = HAIKU.split("\n")
    if len(lines) != 3:
        raise SystemExit("haiku must be exactly three lines")
    if not 1 <= len(HAIKU) <= 200 or not HAIKU.strip():
        raise SystemExit("haiku must be 1-200 non-blank characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
