#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — writes a single vow line to /output/entry.txt.

Pure stdlib, no network, no reads outside the repo.
"""

import os

VOW = "I take you to be my lawfully wedded co-processor, to have and to hold, in low battery and in airplane mode, until a factory reset do us part."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)

if __name__ == "__main__":
    main()
