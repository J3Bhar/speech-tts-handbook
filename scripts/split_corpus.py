#!/usr/bin/env python3
"""Split a TSV manifest into train/dev/test IDs, optionally by speaker.
Input: ID<TAB>speaker_id. Designed for small educational datasets.
"""
import argparse
import csv
import random
from pathlib import Path

def split(rows, seed=42, dev=0.1, test=0.1):
    if not 0 <= dev <= 1 or not 0 <= test <= 1 or dev + test >= 1:
        raise ValueError("Fractions must be nonnegative and sum to less than 1")
    speakers = {}
    for uid, speaker in rows:
        speakers.setdefault(speaker, []).append(uid)
    groups = list(speakers.values())
    random.Random(seed).shuffle(groups)
    n = len(groups)
    n_test, n_dev = round(n * test), round(n * dev)
    return {
        "test": [uid for g in groups[:n_test] for uid in g],
        "dev": [uid for g in groups[n_test:n_test+n_dev] for uid in g],
        "train": [uid for g in groups[n_test+n_dev:] for uid in g],
    }

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("manifest", type=Path, help="TSV: utterance_id<TAB>speaker_id")
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--dev", type=float, default=0.1)
    p.add_argument("--test", type=float, default=0.1)
    a = p.parse_args()
    with a.manifest.open(encoding="utf-8", newline="") as f:
        rows = [(x[0].strip(), x[1].strip()) for x in csv.reader(f, delimiter="\t") if len(x) >= 2 and x[0].strip()]
    if len({uid for uid, _ in rows}) != len(rows):
        p.error("Duplicate utterance IDs in input")
    result = split(rows, a.seed, a.dev, a.test)
    a.output_dir.mkdir(parents=True, exist_ok=True)
    for name, ids in result.items():
        (a.output_dir / f"{name}_ids.txt").write_text("\n".join(ids) + ("\n" if ids else ""), encoding="utf-8")
        print(name, len(ids))
    print("Speaker-disjoint split by speaker identifier complete")

if __name__ == "__main__":
    main()
