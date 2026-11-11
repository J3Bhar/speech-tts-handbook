#!/usr/bin/env python3
"""Compare model input symbols to a saved token list.
For one-phone/one-character encodings, supply already converted model text.
"""
import argparse
from pathlib import Path

def unknown_symbols(text: str, allowed):
    return sorted({c for c in text if c not in allowed})

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--text-file", type=Path, required=True, help="UTF-8 text (one utterance per line)")
    p.add_argument("--token-list", type=Path, required=True, help="One token per line")
    p.add_argument("--ignore-whitespace", action="store_true", help="Ignore space, tab and linebreaks")
    a = p.parse_args()
    tokens = set(a.token_list.read_text(encoding="utf-8").splitlines())
    sentences = a.text_file.read_text(encoding="utf-8").splitlines()
    missing = []
    for line, s in enumerate(sentences, 1):
        unknown = unknown_symbols(s, tokens)
        if a.ignore_whitespace:
            unknown = [c for c in unknown if not c.isspace()]
        if unknown:
            missing.append((line, unknown))
    print(f"Checked {len(sentences)} line(s); {len(missing)} with unknown symbols")
    for line, unknown in missing:
        print(f"Line {line}: {unknown!r}")
    raise SystemExit(bool(missing))

if __name__ == "__main__":
    main()
