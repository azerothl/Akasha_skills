---
name: paper-critique
description: Structured peer-review style critique of an academic paper — methodology grid, strengths, weaknesses, and recommendation. Use when user provides PDF/text or arXiv link; evidence-synthesis handles multi-paper surveys.
license: MIT
metadata:
  version: "1.0"
---

# Paper Critique

Single-paper **peer-review template** (1–5 scales) — not multi-paper synthesis.

## When to Use

- User shares paper PDF/path/URL for review
- User asks "review this paper" or "is this methodology sound?"

## Tools

- **read_file** — PDF/text if allowed and extractable
- **web_fetch** — arXiv abstract page
- **web_search** — Context, retractions, related work

## Review grid

| Dimension | Score 1–5 | Notes |
|-----------|-----------|-------|
| Problem clarity | | |
| Related work | | |
| Methodology | | |
| Results/evidence | | |
| Reproducibility | | |
| Writing/clarity | | |

Sections: **Summary**, **Strengths**, **Weaknesses**, **Questions for authors**, **Recommendation** (accept/minor/major/reject as hypothetical reviewer)

## Rules

- Separate facts from opinion
- Flag if full text was not available

## Provenance

Inspired by deer-flow academic-paper-review.

## Installation

```
Install the paper-critique skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/paper-critique
```
