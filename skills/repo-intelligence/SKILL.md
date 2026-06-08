---
name: repo-intelligence
description: Analyze an open-source GitHub repository — health signals, structure, contributors, issues, and landscape summary with Mermaid. Use for OSS evaluation; git-helper remains for local git ops.
license: MIT
compatibility: Optional github_repo_info tool or run_command with gh/curl; web_search and web_fetch always useful.
metadata:
  version: "1.0"
---

# Repo Intelligence

Structured **OSS landscape report** for a GitHub repository — not day-to-day git operations (**git-helper**).

## Akasha angle

Multi-round synthesis: metadata API + README + issues/activity signals + **web_search** for ecosystem context. Optional `scripts/github_api.py` when native tool unavailable.

## When to Use

- User asks to evaluate, compare, or research a GitHub repo
- Due diligence before adopting a dependency
- User wants Mermaid map of repo structure and ecosystem

## Tools to Use

- **github_repo_info** — Preferred: owner/repo metadata, languages, topics
- **web_fetch** — README, CONTRIBUTING, LICENSE from raw GitHub URLs
- **web_search** — Ecosystem, alternatives, recent news
- **run_command** — Optional: `gh repo view`, `gh api` if policy allows
- **write_file** — Save report if requested

## Execution

1. Parse **owner/repo** from user input
2. Gather metadata (tool or script — see `scripts/github_api.py`)
3. Fetch README summary (purpose, install, status badges)
4. Assess signals: last commit recency, open issues trend, license, contributor count
5. **web_search** — `"owner/repo" alternatives OR comparison`
6. Deliver report:

```markdown
# Repo Intelligence: owner/repo
## Summary
## Health signals
## Structure (Mermaid flowchart)
## Risks & gaps
## Sources
```

## Data authenticity

Do not invent star counts or contributor names — only report fetched data. Mark missing data explicitly.

## Provenance

Inspired by deer-flow github-deep-research; Akasha naming and tooling.

## Installation

```
Install the repo-intelligence skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/repo-intelligence
```
