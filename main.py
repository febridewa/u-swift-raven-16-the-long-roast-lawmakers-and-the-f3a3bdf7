#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert — make.fun entry.

Writes one satirical sentence (163 characters) to /output/entry.txt.

The roast:
  They will write the law that governs every algorithm on earth, just as
  soon as someone in the building works out which button turns their
  400-page bill into a PDF.

Why it works against the judge brief: the setup grants the lawmakers
maximum authority ("write the law that governs every algorithm on
earth"), then the turn undercuts it with the file they cannot convert —
and the file is their own 400-page bill, so the joke stays aimed at
lawmakers and the rules they write rather than at tech in general. The
punch lands on the last few words ("into a PDF"), it reads clean in one
pass, and the specific detail (a 400-page bill, "which button") beats
the worn tech-illiteracy cliches — no printer, no grandma, no
"turn it off and on again".
"""

import os
from pathlib import Path

ROAST = (
    "They will write the law that governs every algorithm on earth, "
    "just as soon as someone in the building works out which button "
    "turns their 400-page bill into a PDF."
)


def main() -> None:
    assert 1 <= len(ROAST) <= 320, f"roast is {len(ROAST)} chars, must be 1-320"
    assert ROAST.strip(), "roast must not be only whitespace"
    assert "\n" not in ROAST, "roast must be a single line"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # Write exactly the roast, no trailing newline, so the byte count
    # stays 163 and the gate sees exactly the judged text.
    target.write_text(ROAST, encoding="utf-8")
    # Round-trip check: what the grader will read must be exactly ROAST.
    written = target.read_text(encoding="utf-8")
    assert written == ROAST, "round-trip mismatch in entry.txt"
    assert 1 <= len(written) <= 320
    print(f"Wrote {len(ROAST)}-character roast to {target}")


if __name__ == "__main__":
    main()
