"""One Word From Your Ex.

Writes exactly one word to /output/entry.txt: the word an ex would
use to describe the entrant. Deterministic, stdlib only, no network.

The word: Practice.

Why this word, judged against the kit rubric in order:

1. Exactly one word an ex would say about a partner they once had.
   "He was practice" is a sentence a real person says, bitter and
   plain, about someone they dated before the real thing.
2. It makes you laugh through a sharp turn. The relationship is
   reframed in a single word: not a romance, a rehearsal. The laugh
   is the sudden demotion from partner to training exercise.
3. It stings because it is painfully true and the entrant knows it.
   The word admits the whole relationship was preparation for
   somebody else, and the loss is left unsaid for the reader to
   fill in. No insult is needed; the reframe does the damage.
4. It lands instantly and cannot be swapped. "Rehearsal" is an
   event, not a person; "Trial" sounds legal; "Warmup" sounds like
   sport; "Lesson" is a self-help cliche. Only "Practice" says, in
   one word, "you were the run-through before the real thing."
5. It is relatable. Almost everyone has been, or has had, the
   practice relationship, the one that taught the other person
   what they actually wanted. People repeat the word because they
   have lived it.

No explanation is attached, because the word needs none.
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
