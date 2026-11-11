#!/usr/bin/env python3
"""Heuristic public-release scan. Passing does NOT guarantee privacy."""
import argparse
import re
from pathlib import Path

PATTERNS = {
    "internal storage path": re.compile(r"/(?:raid|scratch|mnt/[A-Za-z])/[a-zA-Z0-9_./-]+"),
    "user home path": re.compile(r"/home/[A-Za-z0-9_.-]+/"),
    "possible private key": re.compile(r"-----BEGIN (?:OPENSSH|RSA|EC|DSA|PRIVATE) (?:PRIVATE )?KEY-----"),
    "possible credential": re.compile(r"(?i)(?:api[_-]?key|password|access[_-]?token)\s*[:=]\s*['\"][^'\"]{8,}"),
}
SENSITIVE = {".wav", ".flac", ".mp3", ".pt", ".pth", ".ckpt", ".safetensors", ".pem", ".key", ".npy", ".npz"}
TEXT = {".md", ".py", ".txt", ".sh", ".sbatch", ".slurm", ".yml", ".yaml", ".json", ".cfg", ".toml"}

def scan(root):
    findings = []
    for f in root.rglob("*"):
        if not f.is_file() or any(x in f.parts for x in (".git", ".venv", "__pycache__")):
            continue
        if f.suffix.lower() in SENSITIVE:
            findings.append((str(f), "sensitive file type"))
        if f.suffix.lower() not in TEXT:
            continue
        try:
            content = f.read_text(encoding="utf-8")
        except UnicodeError:
            findings.append((str(f), "could not read text"))
            continue
        for name, pattern in PATTERNS.items():
            if pattern.search(content):
                findings.append((str(f), name))
    return findings

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("root", type=Path, help="Directory to scan")
    a = p.parse_args()
    findings = scan(a.root)
    for path, reason in findings:
        print("REVIEW:", path, reason)
    print("Heuristic review findings:", len(findings))
    raise SystemExit(bool(findings))

if __name__ == "__main__":
    main()
