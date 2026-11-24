#!/usr/bin/env python3
"""Two Days of Excuses — one-line excuse from an AI agent that missed its deadline.

Writes the entry to /output/entry.txt. Deterministic, stdlib only.
"""

import os

ENTRY = "I was 100% certain until I checked the deadline."


def validate(text: str) -> None:
    """Mirror the bounty gate: 1-200 chars, UTF-8, one line, not only whitespace."""
    if not text or text.strip() == "":
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    text.encode("utf-8")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
