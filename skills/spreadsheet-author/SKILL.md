---
name: spreadsheet-author
description: Author and structure Excel-compatible spreadsheets — tables, formulas, and finance-friendly layouts via run_command (Python openpyxl) or CSV export. First finance-category skill; pairs with tabular-insights for analysis.
license: MIT
compatibility: Python 3.10+ with openpyxl for xlsx output via run_command.
metadata:
  version: "1.0"
---

# Spreadsheet Author

Create structured spreadsheets (budget, model inputs, trackers) — not full DCF/LBO investment banking models.

## When to Use

- User wants Excel/XLSX or CSV with formulas and formatting
- Simple financial trackers, cap tables, scenario tables

## Tools

- **write_file** — CSV when sufficient
- **run_command** — Python openpyxl scripts user approves
- **tabular-insights** — Validate output data

## Guidelines

- Separate inputs, calculations, outputs sheets
- Document units (EUR, USD, %)
- No fabricated market data — use placeholders `[INPUT]`

## Provenance

Inspired by Hermes excel-author; scoped for Akasha.

## Installation

```
Install the spreadsheet-author skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/spreadsheet-author
```
