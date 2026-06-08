#!/usr/bin/env bash
# Pilot eval for CI — see EVALS_AND_VERSIONING.md
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
test -f skill.json
python3 - <<'PY'
import json, pathlib, sys
p = pathlib.Path("skill.json")
d = json.loads(p.read_text(encoding="utf-8"))
assert d.get("id") == "calculator"
assert d.get("version")
print("calculator self_check OK")
PY
