"""Generic helpers for writing a single-line diary entry to a file.

This module knows nothing about the entry text itself. It only resolves
where the entry goes and writes the given text there, so the diary
program stays small and the file-writing behaviour can be tested alone.
"""

import os


def resolve_output_path():
    """Return the path the entry should be written to.

    The OUTPUT_PATH environment variable wins when it is set and
    non-empty; otherwise the default is /output/entry.txt. The parent
    directory is created when it does not exist yet, so the caller never
    has to worry about a missing output folder.
    """
    path = os.environ.get("OUTPUT_PATH") or "/output/entry.txt"
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    return path


def write_entry(path, text):
    """Write one diary line to path using UTF-8 encoding.

    Validation comes first on purpose: a diary entry is exactly one
    non-empty line, so refusing an empty or multi-line string here keeps
    a broken caller from silently producing an empty or malformed entry
    file. Failing loudly at the write step is better than shipping a
    bad entry.
    """
    if not text:
        raise ValueError("entry text must not be empty")
    if len(text.splitlines()) != 1:
        raise ValueError("entry text must be exactly one line")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
