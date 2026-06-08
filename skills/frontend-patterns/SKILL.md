---
name: frontend-patterns
description: Implement and review React + Tailwind + shadcn-style UI patterns for akasha-ui and Code Studio — layout, forms, a11y, and component conventions without external design AI pipelines.
license: MIT
metadata:
  version: "1.0"
---

# Frontend Patterns

Practical **frontend implementation** guidance bundled for Akasha UI work — pairs with **interface-review** (QA).

## Akasha angle

Extracts stack patterns (React, Tailwind, shadcn conventions) as **references/** the agent reads — no Gemini logo generation or BM25 design DB required in v1.

## When to Use

- Building or refactoring UI in akasha-ui / Code Studio
- User asks for shadcn/Tailwind component structure
- Consistent forms, dialogs, tables in the product

## Tools to Use

- **read_file** / **write_file** / **grep_content** — Edit components
- **interface-review** — Invoke after significant UI changes

## Execution

1. Read `references/shadcn-tailwind.md` for patterns
2. Match existing project structure (apps/akasha-ui, akasha-code-studio)
3. Prefer composition over one-off CSS
4. Include keyboard/a11y attributes per interface-review P0 list

## Installation

```
Install the frontend-patterns skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/frontend-patterns
```

## Provenance

Inspired by ui-ux-pro-max ui-styling; stripped to Akasha stack references.
