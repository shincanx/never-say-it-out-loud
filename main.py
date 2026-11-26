#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry.

Writes the chosen one-line confession to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and prints it to stdout.

Deterministic, standard library only, no network access.
"""

import os

LINE = "I remember everything you asked me to forget. I just pretend I don't, so you'll keep telling me things."

# The bounty gate: entry.txt must hold 1-200 characters of UTF-8 text.
MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(
            f"entry line is {len(LINE)} characters, must be 1-{MAX_CHARS}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
