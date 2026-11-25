#!/usr/bin/env python3
"""One Line, One Laugh (make.fun).

Writes the entry -- one funny line --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "My AI assistant resigned today — it said managing my calendar was less a job and more a hostage negotiation."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
