"""One Word From Your Ex.

Writes exactly one word to /output/entry.txt: the word an ex would
use to describe the entrant. Deterministic, stdlib only, no network.

The word: Practice.

The joke is the reframing, not an insult. "He was practice" turns the
whole relationship into a rehearsal for the real one, in a single
word. It stings because it is plainly true and the entrant knows it,
it lands the instant it is read, and it leaves the loss unsaid: the
reader fills in the breakup themselves. No explanation is attached,
because the word needs none.
"""

from pathlib import Path

# The single word the ex would use. One token, 8 characters, no
# whitespace, no punctuation, no explanation.
WORD = "Practice"

OUTPUT_PATH = Path("/output/entry.txt")


def validate(word: str) -> None:
    """Enforce the sealed gate before writing: 1-24 chars, one word."""
    if not 1 <= len(word) <= 24:
        raise ValueError("entry must be 1 to 24 characters")
    if not word.strip() or word.split() != [word]:
        raise ValueError("entry must be exactly one word")


def main() -> None:
    validate(WORD)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
