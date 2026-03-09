#!/usr/bin/env python3
"""
Aggregates all skills/*/skill.json files into a single skills.json index at the repo root.
Run: python3 scripts/build_skills.py
"""

import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def build():
    paths = sorted(glob.glob(os.path.join(ROOT, "skills", "*", "skill.json")))
    if not paths:
        print("No skill.json files found under skills/", file=sys.stderr)
        sys.exit(1)

    skills = []
    for path in paths:
        with open(path, encoding="utf-8") as f:
            try:
                skill = json.load(f)
            except json.JSONDecodeError as exc:
                print(f"Invalid JSON in {path}: {exc}", file=sys.stderr)
                sys.exit(1)
        skills.append(skill)

    out_path = os.path.join(ROOT, "skills.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(skills, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Built {out_path} with {len(skills)} skill(s).")

if __name__ == "__main__":
    build()
