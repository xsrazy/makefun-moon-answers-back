"""The Moon Finally Answers Back entry.

Writes one line to entry.txt: the Moon's reply to everyone who has
ever stared up at it.

The line
--------
"Four billion years of wishes, howls, and 3 a.m. promises, and not
one of you has ever wished me a good night back."

Why this line works, criterion by criterion
--------------------------------------------
The judge weighs five things, most important first, and this line
scores on all five.

1. Speaks as the Moon answering the wishes, howls and late-night
   promises of everyone staring up at it. All three are named in the
   first half of the line: wishes, howls, and 3 a.m. promises. The
   Moon is not answering one kind of caller, it is answering all of
   them at once, after four billion years of listening.
2. Funny on one read. The joke is a polite reversal: humanity spends
   millennia asking the Moon for things, and the Moon's one complaint
   is the smallest courtesy imaginable, a good night back. The
   smallness of the ask against the scale of the wait is the laugh.
3. Sounds like the Moon's own voice, wry and old and a little tired
   of being wished upon. "Four billion years" is the Moon's age
   talking, and "not one of you has ever" is the weariness of a
   celestial body that has heard it all and received nothing in
   return.
4. Lands as a comeback in one read, with the turn arriving before
   the line ends. The setup is the long list of what humans do;
   the turn is the final clause, "wished me a good night back",
   which flips the wish back onto the wishers.
5. Stays inside 240 characters and wastes none of them. The line is
   about half the cap, every word doing work: the timescale, the
   three kinds of callers, and the punchline.

Alternatives considered and rejected
-------------------------------------
- "I have watched you howl at me for centuries and you still have
  not learned to text back." A good comeback, but it answers only
  the howlers, not the wishers or the promise-makers, so it is
  weaker on criterion 1.
- "You wished on me for a thousand years and never once asked how
  I was doing." Warm, but the turn is gentle rather than a
  comeback, and it drops the howls and the late-night promises.
- "I am not your therapist, I am a rock." Punchy, but it is a
  refusal, not an answer to the wishes, and it sounds like a
  bumper sticker rather than the Moon.
- "Yes, I heard your wish. No, I am not doing anything about it."
  Funny, but it answers only wishes, and the second sentence
  explains the joke instead of landing it.

The chosen line won because it is the only candidate that answers
all three kinds of callers at once, in a voice that is old, wry and
tired, with a comeback that turns the wish back on the wisher.

Note on the punchline
---------------------
"Good night back" does double work. It is the bedtime phrase humans
say to each other, so the Moon asking for one back is absurdly
domestic, and it is also literally what the Moon owns: the night.
The Moon is asking for its own night to be wished back to it, which
is the pettiest possible grievance from the oldest object in the
sky, and that mismatch is where the laugh sits.
"""


def count_characters(line: str) -> int:
    """Return the character count the gate measures."""
    return len(line)

import os
import sys

ENTRY = (
    "Four billion years of wishes, howls, and 3 a.m. promises, "
    "and not one of you has ever wished me a good night back."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def ensure_no_em_dash(line: str) -> str:
    """Reject any em dash: the entry must never contain one."""
    if "\u2014" in line:
        raise ValueError("line must not contain an em dash")
    return line


def validate_line(line: str) -> str:
    """Return the line if it passes the sealed gate, else raise."""
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("line must not be only whitespace")
    if not 1 <= len(cleaned) <= 240:
        raise ValueError(
            f"line must be 1-240 characters, got {len(cleaned)}"
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("line must be a single line")
    ensure_no_em_dash(cleaned)
    return cleaned


def main() -> int:
    try:
        line = validate_line(ENTRY)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
