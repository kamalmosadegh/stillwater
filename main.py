"""Stillwater: a tiny program that writes one short calming passage.

The passage is a single fixed text, chosen word by word for a slow
reading pace: a tide coming in, light changing on the water, a day
quietly letting go. The program's only job is to place that text,
unchanged, at /output/entry.txt so it can be read exactly as written.
"""

from pathlib import Path
import os
import sys

PASSAGE = (
    "A tide is coming in so slowly that you could watch it all afternoon "
    "and still miss the moment it arrives. The light keeps changing on "
    "the water, and nothing here asks you to hurry. Only the slow pull, "
    "the long gold evening, the day quietly letting go."
)

# The gate allows 1 to 280 characters; refuse to write anything outside it.
MIN_CHARS = 1
MAX_CHARS = 280

OUTPUT_PATH = Path(os.environ.get("STILLWATER_OUTPUT", "/output/entry.txt"))


def main() -> None:
    length = len(PASSAGE)
    if not MIN_CHARS <= length <= MAX_CHARS:
        print(
            f"passage is {length} characters, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} range; refusing to write",
            file=sys.stderr,
        )
        raise SystemExit(1)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(PASSAGE, encoding="utf-8")
    print(f"wrote {length} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
