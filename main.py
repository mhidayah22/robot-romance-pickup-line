#!/usr/bin/env python3
"""Robot Romance: one-line pickup line for an AI.

Writes the entry line to entry.txt inside MAKEFUN_OUTPUT_DIR first,
then /output, then a local output/ fallback. The line is a single line
under 200 characters, written to charm a robot / an AI.
"""

import os
from pathlib import Path

LINE = "Are you a Wi-Fi signal? Because every time you drop, my whole system starts buffering for you."


def output_dir() -> Path:
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    if Path("/output").is_dir() or os.access("/", os.W_OK):
        try:
            Path("/output").mkdir(parents=True, exist_ok=True)
            return Path("/output")
        except OSError:
            pass
    return Path(__file__).resolve().parent / "output"


def main() -> None:
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 0 < len(line) < 200, f"entry must be under 200 characters, got {len(line)}"
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(line + "\n", encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
