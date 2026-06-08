---
name: chart-picker
description: Choose appropriate chart types for data stories and optionally generate AntV-style configs. Use when user needs visualization guidance; requires Node 18+ for optional generate script.
license: MIT
compatibility: Optional Node 18+ for scripts/generate.js
metadata:
  version: "1.0"
---

# Chart Picker

Select chart types and produce config snippets — optional JS generator.

## When to Use

- User has data and asks "what chart should I use?"
- Need bar/line/scatter/pie recommendation with rationale

## Tools

- **read_file** — Sample data file
- **run_command** — Optional `node scripts/generate.js <type> <data.json>`

See `references/chart-types.md` for decision tree.

## Installation

```
Install the chart-picker skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/chart-picker
```
