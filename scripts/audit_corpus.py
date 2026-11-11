#!/usr/bin/env python3
"""Check a TSV manifest: utterance_id<TAB>wav_path<TAB>transcript.
Uses standard-library wave and does not change input files.
"""
import argparse
import csv
import wave
from pathlib import Path

def audit(manifest: Path, sample_rate=None):
    problems, ids, count = [], set(), 0
    with manifest.open(encoding="utf-8", newline="") as f:
        for line, cells in enumerate(csv.reader(f, delimiter="\t"), 1):
            if not cells or not any(x.strip() for x in cells):
                continue
            count += 1
            if len(cells) < 3:
                problems.append(f"line {line}: expected ID, WAV path, transcript")
                continue
            uid, audio, transcript = cells[0].strip(), cells[1].strip(), "\t".join(cells[2:]).strip()
            if not uid or uid in ids:
                problems.append(f"line {line}: empty or duplicated utterance ID")
            ids.add(uid)
            if not transcript:
                problems.append(f"line {line}: empty transcript")
            wav = Path(audio)
            if not wav.is_absolute():
                wav = (manifest.parent / wav).resolve()
            if not wav.is_file():
                problems.append(f"line {line}: missing WAV: {audio}")
                continue
            try:
                with wave.open(str(wav), "rb") as w:
                    if w.getnframes() <= 0:
                        problems.append(f"line {line}: zero-frame WAV")
                    if sample_rate and w.getframerate() != sample_rate:
                        problems.append(f"line {line}: sample rate {w.getframerate()} != {sample_rate}")
            except (wave.Error, OSError, EOFError) as e:
                problems.append(f"line {line}: unreadable PCM WAV ({e})")
    return count, problems

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("manifest", type=Path, help="TSV: utterance_id, wav_path, transcript")
    p.add_argument("--sample-rate", type=int, default=None, help="Expected Hz (optional)")
    a = p.parse_args()
    total, errors = audit(a.manifest, a.sample_rate)
    print(f"Checked {total} records; {len(errors)} issue(s)")
    for error in errors:
        print("REVIEW:", error)
    raise SystemExit(bool(errors))

if __name__ == "__main__":
    main()
