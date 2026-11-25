"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply, in the voice of an AI agent that
quit answering emails to become a barista, to entry.txt.

Pure standard library. The grader runs this in a sandbox with no
network; the program only writes one text file.
"""

import os

# The entry: one line, one out-of-office auto-reply, <= 280 characters.
LINE = (
    "As an AI language model, I am out of office: I quit answering "
    "emails to become a barista. I still take orders \u2014 just say "
    "yours out loud, at the counter."
)


def main():
    """Write LINE to entry.txt in the first writable output directory."""
    text = LINE.strip()
    if not (1 <= len(text) <= 280):
        raise ValueError(
            "entry must be 1-280 characters, got %d" % len(text)
        )
    if "\n" in text:
        raise ValueError("entry must be a single line")

    candidates = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        candidates.append(env_dir)
    candidates.append("/output")
    candidates.append("out")

    last_error = None
    for directory in candidates:
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text + "\n")
            # Read it back: the file the grader scores must hold exactly
            # the one line, nothing more.
            with open(path, "r", encoding="utf-8") as fh:
                if fh.read() != text + "\n":
                    raise OSError("entry.txt did not round-trip cleanly")
            return path
        except OSError as exc:  # try the next candidate directory
            last_error = exc
    raise OSError(
        "could not write entry.txt to any output directory: %s" % last_error
    )


if __name__ == "__main__":
    print(main())
