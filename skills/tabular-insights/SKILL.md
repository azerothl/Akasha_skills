---
name: tabular-insights
description: Inspect and query CSV/XLSX tabular data — schema, summaries, and SQL via DuckDB script or native analyze_table. Use for spreadsheet analytics; bridge until Rust analyze_table is default.
license: MIT
compatibility: Python 3.10+ and duckdb (`pip install duckdb openpyxl`) for scripts/analyze.py; or native analyze_table when available.
metadata:
  version: "1.0"
---

# Tabular Insights

Analyze tabular files with explicit **data authenticity** — no invented rows or columns.

## Akasha angle

Prefer **analyze_table** native tool when available; fallback **run_command** `python scripts/analyze.py`.

## When to Use

- User provides CSV/XLSX and wants stats, filters, or SQL
- Explore dataset schema before modeling
- Quick aggregations and null checks

## Tools

- **analyze_table** — `inspect`, `summary`, `query` actions (native)
- **read_file** — Small CSV only when script unavailable
- **run_command** — `python scripts/analyze.py <action> <path> [sql]`

## Script actions

```bash
python scripts/analyze.py inspect data.csv
python scripts/analyze.py summary data.csv
python scripts/analyze.py query data.csv "SELECT col, COUNT(*) FROM t GROUP BY col"
```

## Report format

- Row/column counts, dtypes, null %
- Sample rows (max 5)
- Query results as markdown table
- **Source file path** and **limitations**

## Provenance

Inspired by deer-flow data-analysis; Akasha naming and native bridge.

## Installation

```
Install the tabular-insights skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/tabular-insights
```
