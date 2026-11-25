# SPDX-License-Identifier: MIT
"""Entry program for the make.fun bounty "One Word, One Username, One Reward".

The whole entry is a single word: the entrant's own make.fun username,
spelled exactly as registered. This program writes that word, and nothing
else, to /output/entry.txt as raw UTF-8 bytes with no trailing newline.
"""

from pathlib import Path

# The winning word: the entrant's genuine make.fun handle, lowercase,
# exactly as it appears on the account. Any decoration (capitalisation,
# punctuation, a numeric suffix) would stop it being the real handle.
USERNAME = "narathifa"

# The bounty gate accepts UTF-8 text of 1 to 30 characters that is not
# only whitespace; the word must also be a single token with no spaces.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 30

OUTPUT_PATH = Path("/output/entry.txt")


def validate(word: str) -> bytes:
    """Encode the word for output, refusing anything outside the gate."""
    if not GATE_MIN_CHARS <= len(word) <= GATE_MAX_CHARS:
        raise ValueError(f"word must be {GATE_MIN_CHARS}-{GATE_MAX_CHARS} characters")
    if not word.strip():
        raise ValueError("word must not be whitespace only")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must be a single token without spaces")
    return word.encode("utf-8")


def verify_written(payload: bytes) -> None:
    """Read the output file back and check it round-trips exactly.

    The grader runs this program twice and gates each run's file, so a
    silent short write or an added newline would fail one run even if
    the other passed. Re-reading the bytes just written and comparing
    them against the intended payload catches that here instead.
    """
    on_disk = OUTPUT_PATH.read_bytes()
    assert on_disk == payload, f"output drifted: {on_disk!r} != {payload!r}"
    text = on_disk.decode("utf-8")
    assert GATE_MIN_CHARS <= len(text) <= GATE_MAX_CHARS, "gate length violated"
    assert text.strip() and not any(ch.isspace() for ch in text), "not one clean word"


def main() -> None:
    payload = validate(USERNAME)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(payload)
    verify_written(payload)


if __name__ == "__main__":
    main()
