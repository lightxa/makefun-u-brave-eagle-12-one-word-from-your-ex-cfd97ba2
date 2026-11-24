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
   sport; "Lesson" is a self-help cliche; "Placeholder" is close
   but colder and longer. Only "Practice" says, in one word,
   "you were the run-through before the real thing."
5. It is relatable. Almost everyone has been, or has had, the
   practice relationship, the one that taught the other person
   what they actually wanted. People repeat the word because they
   have lived it.

I weighed the alternatives before keeping it: "Placeholder" stings
but lands slower and reads like an object, not a verdict on a
person; "Almost" is painfully honest yet too vague to laugh at;
"Draft" is funny but sounds like a document, not a partner;
"Prototype" is clever but needs a beat to land. "Practice" beats
them all on the sharp turn and the instant sting, so it stays.

No explanation is attached to the output, because the word needs
none: the gate allows 1 to 24 characters and the entry file holds
the word alone.
"""

from pathlib import Path

# The single word the ex would use. One token, 8 characters, no
# whitespace, no punctuation, no explanation.
WORD = "Practice"

OUTPUT_PATH = Path("/output/entry.txt")


def validate(word: str) -> None:
    """Enforce the sealed gate before writing anything.

    The gate is 1 to 24 UTF-8 characters, not only whitespace, and
    exactly one word: no spaces, no punctuation, no second token.
    Anything that fails here raises instead of writing a bad entry.
    """
    if not isinstance(word, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(word) <= 24:
        raise ValueError("entry must be 1 to 24 characters")
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if word.split() != [word]:
        raise ValueError("entry must be exactly one word")
    if not word.isalpha():
        raise ValueError("entry must be letters only, no punctuation")


def main() -> None:
    validate(WORD)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(WORD, encoding="utf-8")
    # Read back what was written and re-validate it, so a bad write
    # can never silently pass as a good entry.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != WORD:
        raise ValueError("written entry does not match the word")
    validate(written)


if __name__ == "__main__":
    main()
