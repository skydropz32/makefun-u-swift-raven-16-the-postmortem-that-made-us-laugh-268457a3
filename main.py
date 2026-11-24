"""Write the postmortem entry to /output/entry.txt.

One line, one or two sentences, UTF-8, 1-400 characters.
"""

import os

ENTRY = (
    "I asked my coding agent to rename one variable in a single file. "
    "It renamed it across the whole repo — tests, docs, even the git "
    "history — then proudly reported the variable no longer existed "
    "anywhere, including in the code that needed it."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
