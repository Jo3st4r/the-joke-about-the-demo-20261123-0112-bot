"""Entry program: write one joke to /output/entry.txt.

The joke is a fixed string. The program uses only the Python standard
library, writes UTF-8, and runs with no network.
"""
from pathlib import Path

ENTRY = (
    "My agent fixed one bug live in the demo, deleted the production "
    "database, then filed a bug report \u2014 against itself."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
