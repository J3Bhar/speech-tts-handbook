#!/usr/bin/env python3
"""Check that an MFA corpus has matching non-empty WAV/TXT pairs."""
import argparse
import wave
from pathlib import Path

def check_corpus(root):
    root = Path(root)
    if not root.is_dir():
        return 0, ["Corpus directory missing"]
    wavs = sorted(root.rglob("*.wav"))
    txts = set(root.rglob("*.txt"))
    issues = []
    if not wavs:
        issues.append("No WAV files found")
    expected = set()
    for wav in wavs:
        txt = wav.with_suffix(".txt")
        expected.add(txt)
        if txt not in txts:
            issues.append(f"Missing transcript for {wav.relative_to(root)}")
        elif not txt.read_text(encoding="utf-8").strip():
            issues.append(f"Empty transcript for {wav.relative_to(root)}")
        try:
            with wave.open(str(wav), "rb") as f:
                if f.getnframes() <= 0:
                    issues.append(f"Zero-length audio: {wav.relative_to(root)}")
        except (wave.Error, EOFError, OSError):
            issues.append(f"Unsupported or unreadable PCM WAV: {wav.relative_to(root)}")
    for extra in sorted(txts - expected):
        issues.append(f"Transcript without matching WAV: {extra.relative_to(root)}")
    return len(wavs), issues

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--corpus", required=True, type=Path)
    args=p.parse_args()
    total, issues=check_corpus(args.corpus)
    print(f"Checked {total} recordings: {len(issues)} issue(s)")
    for issue in issues: print("REVIEW:", issue)
    raise SystemExit(bool(issues))

if __name__ == "__main__":
    main()
