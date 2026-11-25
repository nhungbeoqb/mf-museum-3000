#!/usr/bin/env python3
"""Museum of the Year 3000 — writes the museum label to /output/entry.txt.

Chosen label (v1): the year-3000 curator misreads a password sticky note
as the lock itself — a true, absurd fact about what the thing was for.
"""

import os

ENTRY = (
    "Sticky note, c. 2024. The lock itself. "
    "Humans wrote the secret on it, then stuck it to the door it opened."
)


def main() -> None:
    text = ENTRY.strip()
    # Gate self-check, mirroring the scorer: UTF-8, 1-200 chars, not blank.
    # Single line only: no embedded newline, so the label reads as one line.
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and re-verify: what the grader sees is what we checked.
    with open("/output/entry.txt", encoding="utf-8") as f:
        round_tripped = f.read()
    assert round_tripped == text, "round-trip mismatch"
    assert 1 <= len(round_tripped) <= 200
    print(f"wrote /output/entry.txt ({len(round_tripped)} chars)")


if __name__ == "__main__":
    main()
