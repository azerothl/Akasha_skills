---
name: batch-processing
description: Break a large repetitive change into tracked steps (todos), execute in order, and verify. Use for migrations, renames across many files, or multi-unit work when the user wants a clear plan and progress tracking.
license: MIT
compatibility: Uses write_todos, merge_todos, read_todos, update_todo, read_file, grep_content, search_files, edit_file/search_replace, run_command (git/tests) if allowed. No separate worktree tool — use policy-approved paths.
metadata:
  version: "1.0"
---

# Batch processing

Orchestrate a **large, splittable** change using Akasha’s todo tools and file tools. Adapted for environments without isolated git worktrees per worker.

## When to Use

- Rename or API migration touching many call sites
- Replace a pattern project-wide with review checkpoints
- User explicitly wants parallelizable work decomposed into units (you may still execute sequentially unless the orchestrator splits tasks)

## Phase 1 — Discovery

1. Use **grep_content** and **search_files** to map files, symbols, and conventions.
2. **read_file** on representative modules to avoid breaking contracts.

## Phase 2 — Plan with todos

1. Decompose into **5–30 units** (scale to scope: small repos → fewer, larger units).
2. Each unit should be:
   - Implementable with a clear file/directory scope
   - Verifiable (tests, build, or concrete manual check)
   - As independent as possible from other units (note ordering if not)
3. Call **write_todos** with the full ordered list (titles + optional detail in titles).
4. Add discovery notes with **merge_todos** if new steps appear later.

## Phase 3 — Execute per unit

For each todo item:

1. **read_todos** if context was lost.
2. Implement changes with **edit_file** / **search_replace** / **write_file**.
3. If policy allows: **run_command** for tests or `git diff` sanity check.
4. **update_todo** to mark the step done (or cancelled if obsolete).

## Phase 4 — Verification

- Prefer project test command via **run_command** when allowed.
- Summarize units completed, files touched, and follow-ups.

## Notes

- This skill does **not** assume background agents or PR-per-unit; if the deployment uses Akasha’s orchestrator, the user may split work into subtasks separately.
- For Git workflows (branch/PR), combine with **git-helper** and explicit user approval before pushes.

## Installation

```
Install the batch-processing skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/batch-processing
```
