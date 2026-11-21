# Stillwater

![Python](https://img.shields.io/badge/python-3.13-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)

Stillwater is a tiny Python program that writes one short calming passage — 251 characters about a tide coming in, light changing on the water, and a day quietly letting go. It was written word by word for a slow reading pace: concrete images, gentle rhythm, and a thought that keeps growing after the last line.

## The passage

> A tide is coming in so slowly that you could watch it all afternoon and still miss the moment it arrives. The light keeps changing on the water, and nothing here asks you to hurry. Only the slow pull, the long gold evening, the day quietly letting go.

## How it works

`main.py` holds the passage as a single constant and writes it, unchanged, to `/output/entry.txt`. Before writing it checks the length against the 1–280 character window and refuses to write anything outside it, so the output is always valid by construction. There are no dependencies, no network calls, and no randomness — the same run always produces the same file.

## Run it

```sh
python3 main.py
```

For a local test without touching `/output`, set `STILLWATER_OUTPUT`:

```sh
STILLWATER_OUTPUT=/tmp/entry.txt python3 main.py
```

## Results

- Output: exactly 251 characters, verified on every run
- Runtime: under a second, Python 3.13 standard library only
- Deterministic: identical output on every run

---

**Kamal Mosadegh** — Freelance Developer · Contact by email only: kamalmosadegh6977@gmail.com
