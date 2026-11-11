#!/usr/bin/env python3
"""Create an MFA corpus from a TSV manifest without modifying source audio.
Manifest columns: utterance_id<TAB>wav_path<TAB>transcript[<TAB>speaker].
Paths are relative to manifest location unless absolute.
"""
import argparse
import csv
import re
import shutil
from pathlib import Path

VALID_ID = re.compile(r"^[A-Za-z0-9_-]+$")

def prepare(manifest, output, dry_run=False):
    manifest = Path(manifest).resolve()
    output = Path(output).resolve()
    if not manifest.is_file():
        raise ValueError("Manifest does not exist")
    if output.exists():
        raise ValueError("Output already exists; choose a new empty location")
    rows, seen = [], set()
    with manifest.open(encoding="utf-8", newline="") as f:
        for line, fields in enumerate(csv.reader(f, delimiter="\t"), 1):
            if not fields or not any(fields):
                continue
            if len(fields) not in (3, 4):
                raise ValueError(f"Line {line}: use ID, WAV, transcript, [speaker]")
            uid, wav_text, transcript = [x.strip() for x in fields[:3]]
            speaker = fields[3].strip() if len(fields) == 4 else "speaker_001"
            if not VALID_ID.fullmatch(uid) or not VALID_ID.fullmatch(speaker):
                raise ValueError(f"Line {line}: ID and speaker must use letters, numbers, _ or -")
            if not transcript or uid in seen:
                raise ValueError(f"Line {line}: missing transcript or duplicate ID")
            if "\n" in transcript or "\r" in transcript:
                raise ValueError(f"Line {line}: transcript must be one line")
            seen.add(uid)
            wav = Path(wav_text)
            if not wav.is_absolute():
                wav = (manifest.parent / wav).resolve()
            if not wav.is_file() or wav.suffix.lower() != ".wav":
                raise ValueError(f"Line {line}: WAV missing or wrong extension")
            dest = output / speaker / f"{uid}.wav"
            if dest == wav or output == wav.parent or output in wav.parents:
                raise ValueError("Output must not overlap source audio")
            rows.append((wav, dest, transcript))
    if not rows:
        raise ValueError("Manifest has no valid recordings")
    if dry_run:
        return len(rows)
    output.mkdir(parents=True)
    for wav, dest, transcript in rows:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(wav, dest)
        dest.with_suffix(".txt").write_text(transcript + "\n", encoding="utf-8")
    return len(rows)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--manifest", required=True, type=Path)
    p.add_argument("--output", required=True, type=Path)
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()
    try:
        n = prepare(a.manifest, a.output, a.dry_run)
        print(f"PASS: {n} utterances " + ("can be prepared" if a.dry_run else "prepared"))
    except (ValueError, OSError) as e:
        p.exit(1, f"ERROR: {e}\n")

if __name__ == "__main__":
    main()
