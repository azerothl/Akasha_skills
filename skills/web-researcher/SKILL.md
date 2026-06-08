---
name: web-researcher
description: Multi-phase web research with source validation and synthesis. Use when the user needs thorough, up-to-date information, cross-source verification, OSINT-style public-source investigation, or structured research reports — not a single quick search.
license: MIT
metadata:
  version: "2.0"
---

# Web Researcher

Structured web research for Akasha: multi-query discovery, deep reading, validation, and synthesis using **web_search** and **web_fetch** only (no subagent delegation).

## Akasha angle

Unlike single-query search skills, this workflow runs **four phases** (Broad → Deep → Validate → Synthesize), tracks confidence per claim, and includes optional **OSINT-light** patterns for public-source investigation. Inspired by multi-phase research methodologies; adapted for Akasha tools and policy.

## When to Use

- User needs comprehensive research (market, technology, policy, competitors)
- User asks to verify facts across multiple sources
- User wants a structured report with citations and confidence labels
- User asks for OSINT-style investigation using **public** sources only
- User needs current documentation, release notes, or news synthesis

## Tools to Use

- **web_search** — Primary discovery; run multiple targeted queries per phase
- **web_fetch** — Read full pages when snippets are insufficient (official docs, articles)
- **write_file** — Optional: save report to an allowed path when user requests

## Execution — Four phases

### Phase 1 — Broad discovery

Run **3–5 web_search** queries with different angles:

- Core topic + synonyms
- `"topic" site:official-domain` when an authority site is known
- Recent angle: add year or `"latest"` / `"2025"` / `"2026"` when freshness matters
- Contrarian or limitation angle: `"topic" problems OR limitations OR criticism`

See `references/query-patterns.md` for query templates.

Collect 8–15 candidate URLs. Prefer authoritative domains (official docs, government, established publishers).

### Phase 2 — Deep read

For the top 3–5 URLs:

- Use **web_fetch** when policy allows and snippets lack detail
- Extract: key facts, dates, numbers, named entities, direct quotes (short)
- Note **source URL** and **retrieval date** for each fact

If **web_fetch** is denied, rely on snippets and state the limitation.

### Phase 3 — Validate

- Cross-check critical claims with **1–2 additional web_search** queries
- Label each major claim:
  - **High** — 2+ independent authoritative sources agree
  - **Medium** — single authoritative source or multiple weak sources
  - **Low** — single non-authoritative source or inferred
- Flag contradictions explicitly; do not hide disagreement

### Phase 4 — Synthesize

Deliver a structured report:

1. **Executive summary** (3–5 bullets)
2. **Findings** by theme (with confidence labels)
3. **Sources** — numbered list of URLs actually used
4. **Gaps** — what could not be verified or needs user input
5. **Suggested follow-ups** — optional next queries

## OSINT-light (optional)

When the user asks for investigation using public sources, read `references/osint-light.md` and:

- Chain evidence: each conclusion links to a fetched or searched source
- Do not access non-public data, bypass paywalls illegally, or doxx individuals
- Prefer primary sources (filings, official registries, project docs) over aggregators

## Behavior Guidelines

- Never invent URLs; only cite URLs from **web_search** results or user input
- State when information may be outdated
- Do not copy long passages; summarize and attribute
- If **web_search** is disabled, explain how to enable it in `tools_policy.yaml` and answer from training knowledge with a clear staleness warning

## Provenance

Methodology inspired by public multi-phase research skills (e.g. deer-flow deep-research, Hermes osint-investigation). Rewritten for Akasha; not a verbatim port.

## Installation

```
Install the web-researcher skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/web-researcher
```
