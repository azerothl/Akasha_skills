---
name: evidence-synthesis
description: Lightweight systematic literature synthesis (~20 papers max) using arXiv search and sequential summarization. Use for research surveys; paper-critique handles single-paper review.
license: MIT
compatibility: arxiv_search tool or scripts/arxiv_search.py; Python 3.10+ stdlib for script.
metadata:
  version: "1.0"
---

# Evidence Synthesis

Small-scale **literature synthesis** — not a full academic SLR pipeline with subagents.

## When to Use

- User wants overview of research on a topic
- Survey arXiv/preprints for a technology area
- Build reading list with 1-paragraph summaries per paper

## Tools

- **arxiv_search** — Native when available
- **run_command** — `python scripts/arxiv_search.py "<query>" [max]`
- **web_fetch** — Abstract pages if needed

## Execution

1. Define research question (PICO-style if clinical)
2. Run 2–3 search queries; cap **~20 papers**
3. For each: title, authors, year, 3-bullet summary, link
4. Synthesis section: themes, gaps, conflicting findings
5. Limitations: not exhaustive, English/arXiv bias

## Provenance

Inspired by deer-flow systematic-literature-review; simplified for Akasha.

## Installation

```
Install the evidence-synthesis skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/evidence-synthesis
```
