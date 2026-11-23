#!/usr/bin/env python3
"""Dad Joke Showdown entry — one dad joke, written to /output/entry.txt."""

import os

JOKE = "I asked my dad why the car is always on empty. He said, 'I run on empty promises.'"


def main():
    # Gate-matching guards: fail loudly instead of writing an entry
    # the scorer would refuse (UTF-8, 1-200 chars, not only whitespace).
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
