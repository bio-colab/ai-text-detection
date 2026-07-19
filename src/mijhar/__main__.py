# -*- coding: utf-8 -*-
"""CLI:  python -m mijhar file.txt [--json]   or   echo text | python -m mijhar -"""
import sys
from .report import scan_text, to_json, to_human


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    as_json = "--json" in argv
    argv = [a for a in argv if a != "--json"]
    if not argv:
        print(__doc__)
        return 2
    path = argv[0]
    if path == "-":
        text = sys.stdin.read()
    else:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    report = scan_text(text)
    try:
        print(to_json(report) if as_json else to_human(report))
    except BrokenPipeError:  # piped into head/less — not an error
        import os
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
