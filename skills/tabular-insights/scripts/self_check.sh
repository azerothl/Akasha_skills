#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
test -f skill.json
python3 - <<'PY'
import json, pathlib
d = json.loads(pathlib.Path("skill.json").read_text(encoding="utf-8"))
assert d.get("id") == "tabular-insights"
assert d.get("version")
print("tabular-insights self_check OK")
PY
python3 -m py_compile scripts/analyze.py
