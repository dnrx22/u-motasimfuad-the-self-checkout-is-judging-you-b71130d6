#!/usr/bin/env python3
"""One line: a funny remark from a judgmental self-checkout machine.

Deterministic, stdlib only, no network. Writes exactly one line to
entry.txt in MAKEFUN_OUTPUT_DIR (or /output if unset) and prints it.
"""

import os
import sys

LINE = "Unexpected item in bagging area: twelve yoghurts and absolutely nothing to go with them."


def main() -> int:
    line = LINE
    if not line or not line.strip():
        print("error: line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: line is {len(line)} characters, over the 200 limit", file=sys.stderr)
        return 1
    words = line.split()
    if len(words) > 20:
        print(f"error: line is {len(words)} words, over the 20-word limit", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
