---
name: architecture-atlas
description: Build a markdown wiki with Mermaid diagrams describing codebase architecture — modules, data flow, and key types. Use when the user wants a navigable architecture map with anti-hallucination rules; complements repo-docs.
license: MIT
metadata:
  version: "1.0"
---

# Architecture Atlas

Wiki-style architecture documentation with **Mermaid** diagrams grounded in actual code structure.

## Akasha angle

Emphasizes **evidence from code** (imports, module tree, API routes) before drawing diagrams. Output under project or `data_dir/wikis/{name}/`. Complements **repo-docs** (README/API) without duplicating it.

## When to Use

- User asks for architecture overview, system diagram, or “how does this repo fit together?”
- Onboarding doc for a large monorepo
- User wants sequence/class/flowchart diagrams from real code paths

## Tools to Use

- **search_files**, **read_file**, **grep_content** — Map modules and dependencies
- **github_repo_info** — Optional metadata for OSS repos (stars, topics, default branch)
- **write_file** — Write wiki pages (index + per-module pages)

## Execution

1. **Scope** — Repo root or subdirectory; max depth reasonable (~20 key modules)
2. **Ground truth pass** — List crates/packages, main binaries, API routers, data stores
3. **Diagram set** (Mermaid only what code supports):
   - `flowchart` — request/data flow
   - `classDiagram` — key types (if OOP/Rust structs with clear relations)
   - `sequenceDiagram` — one critical user journey
4. **Wiki layout**
   ```
   wikis/{project}/index.md
   wikis/{project}/modules/{name}.md
   ```
5. **Anti-hallucination** — Mark `[UNVERIFIED]` any node not found in code; list **Skipped analyses**

## Minimum review contract

Every atlas delivery includes:

- **Analyzed** — paths read
- **Skipped** — paths not read and why
- **Confidence** — High/Medium/Low per diagram section

## Provenance

Inspired by Hermes code-wiki; rewritten for Akasha file tools and review contract.

## Installation

```
Install the architecture-atlas skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/architecture-atlas
```
