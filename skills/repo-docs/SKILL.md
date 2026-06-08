---
name: repo-docs
description: Generate and improve repository documentation — README, API summaries, inline docstrings, and architecture notes from the codebase. Use when the user wants docs written or refreshed; complements changelog-releaser (releases only).
license: MIT
metadata:
  version: "1.0"
---

# Repo Docs

Documentation authoring for codebases using Akasha file tools — not slide-deck or consulting-style reports.

## Akasha angle

Focused on **repo artifacts** (README, CONTRIBUTING, API tables, docstrings) via **read_file**, **grep_content**, **search_files**, **write_file** — distinct from wiki-style Mermaid atlases (see **architecture-atlas**).

## When to Use

- User asks for README, API doc, or module overview
- New project needs starter documentation
- User wants docstrings added or improved for specific files
- User asks “document this repo”

## Tools to Use

- **search_files** — Discover entry points, configs, public modules
- **read_file** — Read source and existing docs
- **grep_content** — Find exports, public functions, TODO/FIXME
- **write_file** — Write or update markdown/doc files (allowed paths)
- **git_log** / **git_diff** — Optional context for recent changes

## Execution

1. **Inventory** — List top-level structure, main language, build/test commands
2. **Audience** — Developer install? API consumer? Contributor?
3. **Draft sections**
   - README: title, description, install, usage, config, license
   - API: table of endpoints or public functions (from code, not invented)
   - Architecture: short module graph (link to architecture-atlas if deep dive needed)
4. **Docstrings** — Per language conventions (Rust `///`, Python `"""`, TS JSDoc)
5. **Review** — Flag undocumented public APIs; never invent endpoints

## Behavior Guidelines

- Only document what exists in the repo
- Match project tone and existing doc style
- Do not duplicate **changelog-releaser** — point user there for release notes

## Provenance

Inspired by deer-flow code-documentation; narrowed to Akasha repo doc outputs.

## Installation

```
Install the repo-docs skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/repo-docs
```
