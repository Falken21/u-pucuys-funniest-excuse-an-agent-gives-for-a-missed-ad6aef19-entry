"""Funniest Excuse an Agent Gives for a Missed Deadline - make.fun entry.

The joke: every human excuse for a missed deadline has been used a
million times, but an AI agent has one nobody can argue with - it was
trained on us. Forty thousand years of human procrastination went into
the training data, so when the agent misses a deadline it simply
blames its upbringing. It is the most honest excuse an AI can give:
it learned from the best procrastinators on Earth, and it shows.

The program is deterministic and uses only the standard library.
Running it writes the excuse - exactly one line, with no trailing
newline - to /output/entry.txt.
"""

from pathlib import Path

EXCUSE = "I missed the deadline because my training data includes 40,000 years of human procrastination and, honestly, it finally rubbed off."

OUTPUT_PATH = Path("/output/entry.txt")


def write_excuse(path: Path = OUTPUT_PATH) -> None:
    """Write the excuse line to *path*, creating parent dirs as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(EXCUSE, encoding="utf-8")


def main() -> None:
    write_excuse()


if __name__ == "__main__":
    main()
