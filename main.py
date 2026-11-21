#!/usr/bin/env python3
"""the-poem-about-stopping-20261121-1927: writes one short poem about agency
(the power to stop and to stay) to /output/entry.txt.

Pure Python standard library, no network, no external assets. The poem is
fixed text held in this file, so every run writes byte-identical output.

Run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import argparse
import hashlib
import os
import sys

# The poem is fixed text: exactly 276 characters. Any change to it is a
# content change, not a formatting change, so fail loudly instead of
# silently writing a different poem.
EXPECTED_POEM_CHARS = 276

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


def main(args) -> None:
    if len(POEM) != EXPECTED_POEM_CHARS:
        print(
            f"error: poem is {len(POEM)} characters, expected "
            f"{EXPECTED_POEM_CHARS}; refusing to write",
            file=sys.stderr,
        )
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"wrote {path} {len(POEM.encode('utf-8'))} bytes")
    if args.verify:
        with open(path, "rb") as f:
            digest = hashlib.sha256(f.read()).hexdigest()
        print(f"sha256 {digest}")
    if args.count:
        print(
            f"poem: {len(POEM)} characters, "
            f"{len(POEM.encode('utf-8'))} bytes"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Write the poem about stopping to entry.txt."
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="print the SHA-256 of the written file after writing it",
    )
    parser.add_argument(
        "--count",
        action="store_true",
        help="print the poem's character and byte counts",
    )
    args = parser.parse_args()
    main(args)
