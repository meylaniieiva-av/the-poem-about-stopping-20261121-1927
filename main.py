#!/usr/bin/env python3
"""the-poem-about-stopping-20261121-1927: writes one short poem about agency
(the power to stop and to stay) to /output/entry.txt.

Pure Python standard library, no network, no external assets. The poem is
fixed text held in this file, so every run writes byte-identical output.

Run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os

POEM = (
    "The kettle clicks off by itself.\n"
    "I don't. I stand there, hand on the switch,\n"
    "and let the water cool, the steam thin out,\n"
    "the morning waits for me.\n"
    "Nothing breaks. The day, unpoured,\n"
    "stays mine a little longer.\n"
    "Stopping is the smallest room I own —\n"
    "I step inside it, and stay.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"wrote {path} {len(POEM.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
