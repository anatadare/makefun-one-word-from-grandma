#!/usr/bin/env python3
"""One Word From Grandma: the single word a grandma would text about AI.

The word is "AyeEye": how a grandma hears the initials "A.I." and types
them back as one word. Warm and a little baffled, funny with no caption
needed, tied to AI itself, and fresh because nobody spells it that way.
"""

import os

WORD = "AyeEye"


def validate(word):
    """The gate wants 1-30 UTF-8 chars, one word, not only whitespace."""
    if not word or len(word) > 30 or word != word.strip():
        raise ValueError("word must be 1-30 characters, no surrounding whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word")
    return word


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(WORD))


if __name__ == "__main__":
    main()
