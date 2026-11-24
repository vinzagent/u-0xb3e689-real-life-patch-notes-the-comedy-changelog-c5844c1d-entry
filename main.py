#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog -- make.fun program/v1 entry.

Writes exactly one patch note, a single line of at most 160
characters, to /output/entry.txt.

The line: a changelog entry for the brain replaying an embarrassing
moment every time its owner tries to fall asleep. Drafts considered
and rejected while writing this file:

- The knee cracking on standing up: a real body bug, but the joke is
  only the sound; it has no second beat.
- Yawning spreading through a meeting: funny and specific, but the
  "chain reaction" framing needs more words than the punchline earns.
- The stomach growling in silence right after eating: recognisable,
  but the grievance is thin -- hunger is the bug, and it is not one.

The brain-replay bug wins because it is the most specific,
recognisable bug of daily life in the set: everyone has lain awake
while their own brain re-ran one moment from years ago, and the fix
is stated exactly as a shipped release note states one -- version
number, terse register, "fixed a bug where ...". The year 2014 is
kept on purpose: a dated embarrassment is funnier than a vague one,
and it costs only four characters.

Validation is part of the program, not an afterthought: the line is
checked for length (1-160 chars), single-line shape, and real
release-note form (a version number up front, "fixed a bug where")
before anything is written, and the file is read back and compared
byte for byte after writing.
"""

import os

ENTRY = (
    "v2.1.0: fixed a bug where the brain replayed your most "
    "embarrassing moment from 2014 every time you tried to fall asleep."
)

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")
MAX_CHARS = 160


def validate(line):
    """The gate's own rules, checked locally before writing."""
    assert isinstance(line, str) and 1 <= len(line) <= MAX_CHARS, (
        "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(line))
    )
    assert line == line.strip(), "entry must not start or end with whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert line.startswith("v") and ": " in line[:8], (
        "entry must read as a release note: version number up front"
    )
    assert "fixed a bug where" in line, "entry must state a fix as shipped"


def main():
    validate(ENTRY)
    os.makedirs(OUT_DIR, exist_ok=True)
    try:
        os.chmod(OUT_DIR, 0o755)
    except OSError:
        pass
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    try:
        os.chmod(OUT_PATH, 0o644)
    except OSError:
        pass
    with open(OUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == ENTRY, "read-back mismatch: file does not hold the entry"
    print("Wrote %d characters to %s" % (len(ENTRY), OUT_PATH))


if __name__ == "__main__":
    main()
