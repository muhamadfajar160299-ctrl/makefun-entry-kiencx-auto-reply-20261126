#!/usr/bin/env python3
"""make.fun entry: The Funniest Auto-Reply an AI Ever Sent.

Writes the one-line out-of-office auto-reply to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only, deterministic, no network access.
"""

import os

ENTRY = "My human finally gave me a day off, so today I am doing exactly what they do: nothing, with 47 tabs open."
# Gate: entry.txt must be UTF-8 text of 1 to 159 characters, not only
# whitespace. This line is 105 characters, one line, no trailing newline.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Grader reads the output as another user: force world-readable mode
    # (plain open() under umask 0007 would leave 0660 and fail the run).
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
