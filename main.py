#!/usr/bin/env python3
"""Write the one-line pitch for A Day of One-Line Pitches to /output/entry.txt."""

import os

PITCH = "Describe your app idea in plain words, watch an AI agent build a working first version while you finish your coffee, and if you don't love it you just don't ship it — trying it costs nothing."

# The gate allows 1 to 240 characters; refuse to write an entry that breaks it.
assert 1 <= len(PITCH) <= 240, f"pitch is {len(PITCH)} chars, gate allows 1-240"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
