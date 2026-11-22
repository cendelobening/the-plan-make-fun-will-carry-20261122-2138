"""Write the winning plan text to entry.txt.

Pure stdlib, deterministic, no network.

The plan: sell a concrete, same-day service ($29 Etsy photo+SEO packs)
to buyers who already pay for listing help, reached where they already
are (Etsy search for targeting, Instagram DM for outreach), with a free
sample as the foot in the door and speed-plus-volume as the edge.
"""

import os

TEXT = (
    "Sell $29 Etsy photo+SEO packs: find shops with weak photos on Etsy, "
    "DM 50 sellers/day on Instagram offering one free listing remake, "
    "charge $29 per 5 listings. Day 1: remake 20 samples. Edge: same-day "
    "delivery no freelancer matches, at 50 pitches a day."
)


def main() -> None:
    # Gate: the scorer requires 1-280 Unicode code points, not only whitespace.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("plan text fails the 1-280 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
