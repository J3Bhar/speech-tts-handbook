#!/usr/bin/env python3
"""Inspect a NumPy mel feature array (.npy); no neural inference is performed."""
import argparse
from pathlib import Path
import numpy as np

def describe(path, bins=None):
    mel = np.load(path, allow_pickle=False)
    if mel.ndim != 2:
        raise ValueError(f"Expected 2-D mel array, got {mel.shape}")
    if bins and bins not in mel.shape:
        raise ValueError(f"Neither array dimension equals requested mel bins ({bins})")
    if mel.size == 0 or not np.isfinite(mel).all():
        raise ValueError("Empty or non-finite mel features")
    return {"shape": tuple(mel.shape), "min": float(mel.min()), "max": float(mel.max())}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("mel", type=Path, help="Path to .npy array")
    p.add_argument("--bins", type=int, help="Expected number of mel bands")
    a = p.parse_args()
    try:
        print(describe(a.mel, a.bins))
    except (ValueError, OSError) as e:
        p.exit(1, f"REVIEW: {e}\n")

if __name__ == "__main__":
    main()
