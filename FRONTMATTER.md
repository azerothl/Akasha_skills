# SKILL.md frontmatter profile (Akasha ↔ akasha-os)

**Status:** Locked **2026-09-25** (Loïc) — **LOCK A**: two products, **content convention only**.

This document freezes the **common skill frontmatter profile** shared between [Akasha](https://github.com/azerothl/Akasha_app) and **akasha-os**. It does not define a unified runtime, loader, or publish pipeline.

## Principles

| Rule | Meaning |
|------|---------|
| **Intersection, not a ceiling** | The common profile is the **portable intersection** of fields both ecosystems can rely on. Products may define **additional** keys in the same file. |
| **One file** | Product-specific keys live in the **same** YAML frontmatter block at the top of `SKILL.md`. |
| **Ignore unknown keys** | Each loader reads the keys it understands and **silently ignores** the rest. |
| **No unified loader** | Akasha and akasha-os keep their own loaders. This repo does not ship a single parser for both. |
| **Dual-publish out of scope** | Automating “publish one skill to two products” is **not** part of this convention (for now). |
| **WASM plugins unrelated** | Plugin ABI or WASM packaging is **out of scope**; do not infer plugin unification from this doc. |

Skills in this repository remain **recipes for agents**: `SKILL.md` is the source of truth for instructions; `skill.json` is gallery/catalog metadata for [Akasha_skills](https://azerothl.github.io/Akasha_skills) (see [README](README.md)).

## Common fields (portable)

These fields are safe to use in any skill intended to be readable by either product (or third-party Agent Skills tooling).

| Field | Required | Type | Notes |
|-------|----------|------|-------|
| `name` | **yes** | string | Kebab-case id; **must equal** the skill folder name (e.g. `skills/<name>/` here, `var/skills/<name>/` on akasha-os, or equivalent layout). Pattern: `[a-z][a-z0-9-]{1,32}` (2–33 characters, starts with a letter). |
| `description` | **yes** | string | What the skill does **and when** to use it ([agentskills.io](https://agentskills.io/specification) style). |
| `license` | recommended | string | e.g. `MIT`. |
| `when_to_use` | optional | string | Extra routing hint; if absent, loaders may fall back to `description`. |
| `runtime` | optional | list of strings | **Always a YAML list** (never a scalar). Catalogue filter badge only — not an execution switch. See [runtime](#runtime-catalogue-filter) below. |

Minimal portable block:

```yaml
---
name: my-skill
description: What it does and when the agent should load it.
license: MIT
---
```

### `name` (identifier)

- **Same value** as the parent directory id: `skills/<name>/SKILL.md` in this repo; akasha-os uses `var/skills/<name>/` (or the host’s equivalent skills root).
- **Pattern:** `[a-z][a-z0-9-]{1,32}` — lowercase letters, digits, and hyphens only; **2–33 characters**; must **start with a letter** (not a digit or hyphen).

### `runtime` (catalogue filter)

- **Type:** YAML **sequence** only. Do **not** use a bare string, the token `both`, or any value outside the allowed set.
- **Allowed list items (only):** `akasha` | `akasha-os`
- **Examples:**
  - `runtime: [akasha-os]`
  - `runtime: [akasha]`
  - `runtime: [akasha, akasha-os]` — both products; **not** `both` or `"akasha, akasha-os"`.
- **If absent:** catalogues do **not** filter the skill by runtime (skill appears regardless of product filter).

## Product extensions (same frontmatter)

Extensions are **not** part of the portable contract. They may appear in the same `---` block; the other product’s loader ignores them.

### akasha-os only

Akasha loaders **ignore** these keys (akasha-os may require or interpret them):

| Field | Purpose |
|-------|---------|
| `tools` | Declared **tool** surface for the skill (YAML list of tool ids). |
| `required_caps` | Declared **host capabilities** the skill needs (YAML list, separate from `tools`). Do **not** fold caps into `tools` or use one key for both. |
| *(other aos-only keys)* | Future akasha-os keys follow the same rule: Akasha ignores unknown keys. |

### Akasha only

akasha-os loaders **ignore** these keys (Akasha may use them):

| Field | Purpose |
|-------|---------|
| `compatibility` | Akasha / daemon version or feature notes. |
| `metadata` | e.g. `version: "1.0"` in frontmatter (gallery may still use `skill.json` `version`). |
| Tool naming in body | Akasha often documents tools in the markdown body and `tools_policy.yaml`; there is **no** shared portable `tools:` list in the common profile. |

Existing Akasha-only keys in the wild (e.g. `tool_ref`, `agents`) remain valid; they are **not** in the portable intersection until both products adopt them.

## Loader behaviour (normative for authors)

1. Parse YAML between the first pair of `---` delimiters.
2. Require `name` and `description` for discovery/routing.
3. Do **not** fail on unknown top-level keys.
4. Do **not** require product extension keys for skills that target only one runtime.

## Example: common + both product extensions

Illustrative only — not a real skill in this repo:

```yaml
---
# --- Common (portable) ---
name: incident-triage
description: Triage production incidents from logs and tickets; use when the user reports an outage or error spike.
license: MIT
when_to_use: User mentions SEV, downtime, or “something is broken” in prod.
runtime: [akasha, akasha-os]

# --- akasha-os only (Akasha ignores) ---
tools:
  - read_logs
  - create_ticket
required_caps:
  - network.outbound

# --- Akasha only (akasha-os ignores) ---
compatibility: Akasha daemon >= 0.4; needs grep_content and run_command.
metadata:
  version: "1.2.0"
---

# Incident triage

…agent instructions; Akasha tool names and policy live in the body…
```

## Relationship to `skill.json`

| Artifact | Role |
|----------|------|
| `SKILL.md` frontmatter | Agent discovery, routing, cross-product portable metadata. |
| `skill.json` | Akasha_skills **gallery** index (`id`, `version`, `tags`, `install_url`, …). |

Keep `name` / `description` aligned with `skill.json` where both exist. Versioning discipline: [EVALS_AND_VERSIONING.md](EVALS_AND_VERSIONING.md).

## What this repo does *not* do

- Mass-migrate every skill to add `runtime` or product extension keys.
- Provide dual-publish or sync tooling between Akasha and akasha-os.
- Change WASM plugin contracts or document plugin ABI unification.

When adding or editing skills here, prefer the **common fields** for all new frontmatter; add product keys only when you intentionally target that runtime.
