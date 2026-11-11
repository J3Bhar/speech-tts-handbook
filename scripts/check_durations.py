#!/usr/bin/env python3
"""Check token counts and duration totals from simple TSV data.
Columns: utterance_id<TAB>token_count<TAB>space-separated_integer_durations<TAB>mel_frames
"""
import argparse
import csv
from pathlib import Path

def check(token_count, durations, frames, eos_zero=False):
    if eos_zero:
        if len(durations) != token_count + 1 or not durations or durations[-1] != 0:
            return "expected one terminal EOS 0 duration"
        durations = durations[:-1]
    elif len(durations) != token_count:
        return "duration count does not match token count"
    if any(x < 0 for x in durations):
        return "negative duration"
    if sum(durations) != frames:
        return f"duration sum {sum(durations)} != mel frames {frames}"
    return None

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("tsv", type=Path)
    p.add_argument("--eos-zero", action="store_true", help="Dataset has a final zero duration for EOS")
    a = p.parse_args()
    errors, count = [], 0
    with a.tsv.open(encoding="utf-8", newline="") as f:
        for line, row in enumerate(csv.reader(f, delimiter="\t"), 1):
            if not row:
                continue
            count += 1
            try:
                uid, n, ds, frames = row[:4]
                message = check(int(n), [int(x) for x in ds.split()], int(frames), a.eos_zero)
                if message:
                    errors.append(f"line {line} ({uid}): {message}")
            except (ValueError, IndexError) as e:
                errors.append(f"line {line}: invalid input ({e})")
    print(f"Checked {count} utterance(s); {len(errors)} issue(s)")
    for error in errors:
        print("REVIEW:", error)
    raise SystemExit(bool(errors))

if __name__ == "__main__":
    main()
