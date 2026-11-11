#!/usr/bin/env python3
"""Audit TextGrid existence and phone-tier labels; no acoustic accuracy claim."""
import argparse
from pathlib import Path

def audit(root, tier_name=None):
    files = sorted(root.glob("*.TextGrid"))
    issues = []
    if not files:
        issues.append("No TextGrid files found")
    for path in files:
        try:
            from praatio import textgrid
            tg = textgrid.openTextgrid(str(path), includeEmptyIntervals=True)
            if tier_name and tier_name not in tg.tierNames:
                issues.append(f"{path.name}: missing tier {tier_name}")
        except ImportError:
            raise RuntimeError("Install praatio: pip install praatio")
        except Exception as e:
            issues.append(f"{path.name}: cannot parse TextGrid ({e})")
    return len(files), issues

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("folder", type=Path)
    p.add_argument("--tier", default=None, help="Require this tier name (such as phones)")
    a = p.parse_args()
    try:
        count, problems = audit(a.folder, a.tier)
        print(f"Inspected {count} file(s); {len(problems)} issue(s)")
        for problem in problems:
            print("REVIEW:", problem)
        raise SystemExit(bool(problems))
    except RuntimeError as e:
        p.exit(1, str(e) + "\n")

if __name__ == "__main__":
    main()
