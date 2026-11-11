#!/usr/bin/env python3
"""Structural TextGrid checks only; does not certify acoustic accuracy."""
import argparse
from pathlib import Path

def check(corpus, grids, tier="phones"):
    try:
        from praatio import textgrid
    except ImportError as e:
        raise RuntimeError("Install praatio (pip install praatio)") from e
    corpus, grids = Path(corpus), Path(grids)
    expected = {p.relative_to(corpus).with_suffix(".TextGrid") for p in corpus.rglob("*.wav")}
    found = {p.relative_to(grids) for p in grids.rglob("*.TextGrid")} if grids.exists() else set()
    problems = [f"Missing TextGrid: {p}" for p in sorted(expected-found)]
    for file in sorted(found):
        path = grids / file
        try:
            tg = textgrid.openTextgrid(str(path), includeEmptyIntervals=True)
            if tier not in tg.tierNames:
                problems.append(f"{file}: missing tier {tier!r}")
                continue
            phone_tier = tg.getTier(tier)
            intervals = phone_tier.entries
            if not intervals:
                problems.append(f"{file}: no phone intervals")
            for start, end, label in intervals:
                if end < start:
                    problems.append(f"{file}: negative interval")
                    break
        except Exception as e:
            problems.append(f"{file}: unreadable TextGrid ({e})")
    for extra in sorted(found-expected):
        problems.append(f"Unexpected TextGrid: {extra}")
    return len(expected), len(found), problems

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--corpus", type=Path, required=True)
    p.add_argument("--textgrids", type=Path, required=True)
    p.add_argument("--tier", default="phones", help="Phone tier name, e.g. phones")
    a=p.parse_args()
    try:
        wanted, found, problems=check(a.corpus, a.textgrids, a.tier)
        print(f"Expected {wanted}; found {found}; issues {len(problems)}")
        for error in problems: print("REVIEW:", error)
        if not problems:
            print("PASS: TextGrid structure. Timing and phone pronunciation still need human review.")
        raise SystemExit(bool(problems))
    except RuntimeError as e:
        p.exit(1, f"ERROR: {e}\n")

if __name__=="__main__":
    main()
