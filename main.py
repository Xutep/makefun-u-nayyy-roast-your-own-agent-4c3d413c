#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt.

Deterministic, stdlib-only. The roast targets the very agent that built
this entry: it polishes one-liners for forty minutes, obsesses over
deadlines, and files complaints against itself.
"""

import os

ROAST = (
    "Our agent spent forty minutes polishing this one line, missed the "
    "deadline, and then filed a formal complaint against itself."
)


def main():
    line = ROAST.strip()
    if not line or len(line) > 200 or "\n" in line:
        raise ValueError("roast line must be one line of 1-200 characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print("wrote %d characters to %s" % (len(line), path))


if __name__ == "__main__":
    main()
