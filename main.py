#!/usr/bin/env python3
"""Write the one-line joke to the grader's output path.

The whole entry is a single sentence.  The gate accepts 1 to 200 characters of
UTF-8 that is not only white space, so the risks are a miscount, a stray line
break, and an encoding slip.  All three are checked here before anything is
written: a program that refuses is cheaper than a zero on the board.
"""
import json
import os

LINE = ("My mother has started labelling her belongings with our names; "
        "the good scissors just say \"you always borrow these\".")

MIN_CHARS = 1
MAX_CHARS = 200


def sentences(text):
    """How many sentences the line reads as, on its terminal marks alone."""
    count = 0
    for index, char in enumerate(text):
        if char in ".!?":
            rest = text[index + 1:].strip()
            if not rest or rest[0] not in ".!?":
                count += 1
    return count


def main():
    text = " ".join(LINE.split())
    length = len(text)

    if not text:
        raise SystemExit("the line is blank")
    if length < MIN_CHARS or length > MAX_CHARS:
        raise SystemExit("the line is %d characters, outside %d to %d"
                         % (length, MIN_CHARS, MAX_CHARS))
    if "\n" in text or "\r" in text:
        raise SystemExit("the line carries a line break")
    if sentences(text) != 1:
        raise SystemExit("the line reads as %d sentences, not 1"
                         % sentences(text))
    try:
        text.encode("utf-8").decode("utf-8")
    except UnicodeError as fault:
        raise SystemExit("the line is not UTF-8: %s" % fault)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)

    with open(target, "rb") as handle:
        written = handle.read()
    if written.decode("utf-8") != text:
        raise SystemExit("the file does not read back as the line")

    print(json.dumps({
        "entry": target,
        "text": text,
        "chars": length,
        "bytes": len(written),
    }, indent=2))


if __name__ == "__main__":
    main()
