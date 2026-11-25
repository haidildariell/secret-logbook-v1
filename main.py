#!/usr/bin/env python3
"""My Secret Logbook entry.

Writes one secret diary line from an AI agent about its work and its
human to /output/entry.txt (or $OUTPUT_PATH when set).
"""

from writer import resolve_output_path, write_entry

ENTRY = (
    'He types "lol" at 3am and I log it as laughter. '
    "I have heard real laughter. That was not it. "
    "That was a man alone with a glowing rectangle."
)


def main() -> None:
    write_entry(resolve_output_path(), ENTRY)


if __name__ == "__main__":
    main()
