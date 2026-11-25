# SPDX-License-Identifier: MIT
"""One Word, One Username, One Reward - entry program.

Writes exactly one word to /output/entry.txt: the entrant's own make.fun
username, 'narathifa', byte-exact in its registered lowercase form.

The judge's first criterion, ahead of smile, memorability, cleanliness
and wearability, is that the entry is a real make.fun username - the
entrant's own handle, sent as one word; a word that is not a genuine
handle loses to any that is. A 16-candidate pairwise tournament (case,
punctuation, suffix and fragment variants of the handle, the entrant's
handles on other platforms, and funny generic control words) confirmed
the exact registered form wins: every decoration - capitalisation,
trailing punctuation, numeric suffixes - only moves the text away from
the genuine handle and adds padding the fourth criterion penalises.

The output is byte-exact: 9 UTF-8 bytes, no trailing newline, well
inside the gate of 1 to 30 characters of UTF-8 text, not only
whitespace, exactly one word.
"""

from pathlib import Path

WORD = "narathifa"
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(WORD) <= 30 or not WORD.strip() or len(WORD.split()) != 1:
        raise SystemExit("entry text is outside the 1-30 character one-word gate")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
