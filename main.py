#!/usr/bin/env python3
"""Entry for make.fun: Make the AI Judge Laugh: Developer Excuses.

Writes a single funny one-line excuse a developer gives when code breaks
in production (under 200 characters) to /output/entry.txt. Pure Python
standard library, deterministic: the same bytes on every run, no network
access, no randomness, no input.

The excuse turns the rubber-stamp code review on itself: the developer
did not break production by writing bad code, but by merging a pull
request that was approved by someone who never opened the diff.
"""

import os

# The twist a developer recognises instantly: "LGTM" from a reviewer who
# never opened the diff. The blame slides from the code to the review,
# which is exactly how the excuse sounds in a real incident call.
EXCUSE = (
    "I didn't break prod \u2014 I merged a PR stamped 'LGTM' "
    "by a reviewer who never opened the diff."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def validate(excuse: str) -> None:
    """The house gate only accepts 1-200 characters; fail fast, never write."""
    if not 1 <= len(excuse) <= 200:
        raise ValueError("excuse must be 1-200 characters")


def main() -> None:
    validate(EXCUSE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    entry_path = os.path.join(OUTPUT_DIR, "entry.txt")
    tmp_path = entry_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)
    os.replace(tmp_path, entry_path)  # atomic: no half-written entry.txt


if __name__ == "__main__":
    main()
