# -*- coding: utf-8 -*-
"""CLI:  python -m mijhar file.txt [--json]   or   echo text | python -m mijhar -"""
import sys
from .report import scan_text, to_json, to_human


def _read_file(path: str) -> str:
    if path.lower().endswith(".docx"):
        import zipfile
        import xml.etree.ElementTree as ET
        with zipfile.ZipFile(path) as docx:
            xml_content = docx.read("word/document.xml")
            tree = ET.fromstring(xml_content)
            ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            paras = []
            for p in tree.iterfind(".//w:p", ns):
                t_nodes = [n.text for n in p.iterfind(".//w:t", ns) if n.text]
                if t_nodes:
                    paras.append("".join(t_nodes))
            return "\n\n".join(paras)
    with open(path, encoding="utf-8") as f:
        return f.read()


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
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
        text = _read_file(path)
    report = scan_text(text)
    try:
        print(to_json(report) if as_json else to_human(report))
    except BrokenPipeError:  # piped into head/less — not an error
        import os
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
