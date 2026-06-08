---
name: skill-discovery
description: Browse and install skills from the Akasha gallery and trusted upstream catalogs. Use when the user wants to find, compare, or install a skill by topic, category, or name — not when authoring a new skill from scratch.
license: MIT
metadata:
  version: "1.0"
---

# Skill Discovery

Help users **find** and **install** skills for Akasha. Primary catalog: [Akasha_skills gallery](https://azerothl.github.io/Akasha_skills).

## Akasha angle

Replaces generic “find skills” flows with Akasha-native **list_skills**, **search_skills_catalog** (when available), **install_skill**, and the public gallery JSON index — not third-party skill marketplaces as the main path.

## When to Use

- User asks “what skills exist?”, “find a skill for X”, “install a skill for API docs”
- User wants to browse categories (research, development, design, finance, electronics)
- User asks about hardware/KiCad skills → point to upstream kicad-happy (see references)

## Tools to Use

- **search_skills_catalog** — Search remote Akasha_skills index by keyword (preferred when enabled)
- **list_skills** — List skills already installed locally
- **read_skill** — Load full instructions before invoking an installed skill
- **install_skill** — Install from GitHub tree URL
- **web_fetch** — Fallback: fetch `https://raw.githubusercontent.com/azerothl/Akasha_skills/main/skills.json`

## Execution

1. **Clarify intent** — topic, category, or skill name
2. **Search catalog**
   - TOOL: `search_skills_catalog <query>` if available
   - Else **web_fetch** the gallery JSON and filter by `description`, `tags`, `category`
3. **Present matches** — id, name, one-line description, category, install URL
4. **Install on request** — TOOL: `install_skill <github-tree-url>`
5. **Confirm** — TOOL: `list_skills` and suggest **read_skill** before first use

## Related meta skills (already in Akasha_skills repo)

| Skill | Purpose |
|-------|---------|
| skill-authoring | Write new skills |
| debug-akasha | Daemon/CLI troubleshooting |
| batch-processing | Repetitive file changes |
| code-simplify | Simplify code |
| memory-hygiene | Memory cleanup |

## Upstream hardware (optional)

For KiCad/PCB workflows, prefer **install_skill** from upstream — see `references/upstream-hardware.md` (kicad-happy). Do not mirror all 13 skills unless user confirms hardware focus.

## Behavior Guidelines

- Prefer Akasha_skills gallery over skills.sh; mention skills.sh only as external discovery
- Never install from untrusted hosts blocked by `tools_policy.yaml`
- One recommendation batch (3–5 skills max) unless user asks for full list

## Provenance

Inspired by deer-flow find-skills; recentered on Akasha gallery and install_skill.

## Installation

```
Install the skill-discovery skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/skill-discovery
```
