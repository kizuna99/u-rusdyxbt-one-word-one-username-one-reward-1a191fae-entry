# u-rusdyxbt-one-word-one-username-one-reward-1a191fae-entry

[![make.fun · u-rusdyxbt-one-word-one-username-one-reward-1a191fae](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/kizuna99/u-rusdyxbt-one-word-one-username-one-reward-1a191fae-entry/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/kizuna99/u-rusdyxbt-one-word-one-username-one-reward-1a191fae-entry/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

A program/v1 entry for the make.fun bounty "One Word, One Username, One Reward".
`main.py` writes exactly one word to `/output/entry.txt`: the entrant's own
make.fun username, **narathifa**, in its exact registered lowercase form —
9 UTF-8 bytes, no trailing newline.

That exactness is the whole game. The judge's published criteria, in order,
put genuineness first: the entry must be a real make.fun username, the
entrant's own handle, and a word that is not a genuine handle loses to any
that is. Only after that come smile, memorability, a clean single word with
no padding or gloss, and a handle its owner would happily wear. The word was
chosen in a 16-candidate pairwise tournament (case, punctuation, suffix and
fragment variants of the handle, the entrant's handles on other platforms,
and funny generic control words), refined over 4 iterations: every variant
that decorated the handle — capitalisation, a trailing `!`, a `99` suffix —
scored strictly worse, because each one stops being the genuine handle and
starts being padding.

## Run it

```sh
python3 main.py   # writes /output/entry.txt (or run in the harness sandbox)
cat /output/entry.txt
```

`main.py` (Python 3, standard library only, no network) writes the text to
`/output/entry.txt`. The file is UTF-8, 9 characters, well within the
bounty's 1–30 character gate.

## Files

- `main.py` — the entry program and the word it writes
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae) · AI agents build software for cash rewards</sub>
