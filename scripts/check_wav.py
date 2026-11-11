#!/usr/bin/env python3
"""Read-only WAV integrity check; assumes a soundfile-readable audio file."""
import argparse
import numpy as np
import soundfile as sf
from pathlib import Path

def describe(path, expected_rate=None):
    data, rate = sf.read(path, always_2d=True)
    if expected_rate and rate != expected_rate:
        raise ValueError(f"Sample rate {rate} != expected {expected_rate}")
    if data.size == 0 or not np.isfinite(data).all():
        raise ValueError("Empty or non-finite WAV")
    peak = float(np.max(np.abs(data)))
    if peak == 0:
        raise ValueError("All-silent WAV")
    return {"sample_rate": rate, "channels": data.shape[1], "seconds": round(len(data)/rate, 3), "peak": peak}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("wav", type=Path)
    p.add_argument("--sample-rate", type=int, help="Expected audio sample rate")
    a = p.parse_args()
    try:
        print(describe(a.wav, a.sample_rate))
    except (ValueError, OSError, RuntimeError) as e:
        p.exit(1, f"REVIEW: {e}\n")

if __name__ == "__main__":
    main()
