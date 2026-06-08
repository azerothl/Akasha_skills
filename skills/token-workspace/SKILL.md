---
name: token-workspace
description: Design token workspace — three-layer tokens (primitive, semantic, component) with JSON templates for CSS variables. Use when starting or auditing a design system; slides out of scope v1.
license: MIT
metadata:
  version: "1.0"
---

# Token Workspace

Document and generate **design token** structure for Akasha UI projects.

## When to Use

- User wants design tokens, theme variables, or CSS custom properties
- Audit inconsistent colors/spacing in a codebase

## Deliverables

- `references/token-template.json` as starter
- Mapping table: token → CSS var → Tailwind config key
- Optional **write_file** updated `tokens.json`

## Three layers

1. **Primitive** — raw palette, spacing scale
2. **Semantic** — `--color-primary`, `--surface-muted`
3. **Component** — `--button-primary-bg`

## Provenance

Inspired by ui-ux-pro-max design-system; doc-only v1.

## Installation

```
Install the token-workspace skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/token-workspace
```
