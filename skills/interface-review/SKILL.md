---
name: interface-review
description: UI/UX and accessibility QA for web and desktop interfaces — checklist review, guideline fetch, adversarial scenarios, and file:line findings. Use when reviewing React/Vue/HTML/CSS, akasha-ui, or Code Studio UI before ship.
license: MIT
metadata:
  version: "1.0"
---

# Interface Review

Unified **design QA** skill: accessibility, UX priorities, responsive layout, and adversarial user scenarios — without external Gemini/chrome pipelines.

## Akasha angle

Merges web-design guideline audits, UX priority checklists, and adversarial UX testing into one Akasha-native workflow using **read_file**, **grep_content**, **web_fetch**, and optional **browser snapshot**.

## When to Use

- User asks for UI review, UX audit, or accessibility check
- Before merging frontend PRs (akasha-ui, Code Studio)
- User reports confusing flows or wants “break this UI” scenarios
- Compare implementation against bundled checklists in `references/`

## Tools to Use

- **read_file** / **grep_content** — Inspect components, CSS, ARIA attributes
- **web_fetch** — Fetch public guideline summaries (e.g. Vercel web design guidelines) when useful
- **browser navigate** + **browser snapshot** — Optional live UI review when enabled
- **write_file** — Optional audit report

## Execution

### 1. Scope

Identify: framework (React/Tailwind/shadcn), target files or URL, breakpoints, critical user journeys.

### 2. Priority checklist (P0 → P3)

From `references/ux-priorities.md`:

- **P0** — Accessibility blockers (keyboard trap, missing labels, contrast fail)
- **P1** — Core UX (focus order, error messages, loading states)
- **P2** — Responsive/layout polish
- **P3** — Visual consistency, micro-copy

### 3. Static analysis

- Grep for: `onClick` without keyboard equivalent, missing `alt`, `aria-*`, color-only status
- Read key components: forms, modals, navigation

### 4. Adversarial scenarios

From `references/adversarial-scenarios.md`: fast clicking, empty states, long text overflow, screen reader order.

### 5. Report format

```markdown
## Interface Review — {target}
### P0 (must fix)
- [file:line] issue — recommendation
### P1 …
### Passed checks
### Skipped (tool/policy limits)
```

Always list **skipped analyses** when browser or fetch unavailable.

## Behavior Guidelines

- Cite **file:line** for code findings
- Do not claim WCAG compliance certification — report checklist coverage
- No auto-fix unless user asks

## Provenance

Inspired by ui-ux-pro-max, deer-flow web-design-guidelines, Hermes adversarial-ux-test — fused and rewritten for Akasha.

## Installation

```
Install the interface-review skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/interface-review
```
