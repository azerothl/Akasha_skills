---
name: code-simplify
description: Review recent changes for reuse, quality, and efficiency; then fix issues. Use after a substantive edit or when the user asks to simplify, clean up, or reduce duplication.
license: MIT
compatibility: Uses read_file, grep_content, search_files, run_command (git diff), edit_file/search_replace/write_file. Requires paths under tools_policy. Optional run_command for tests if allowed.
metadata:
  version: "1.0"
---

# Code Simplify

Structured cleanup pass on changed code: identify what changed, run three review angles (reuse, quality, efficiency), then apply fixes.

## When to Use

- User asks to simplify, deduplicate, or clean up after changes
- User wants a focused refactor pass on a branch or recent edits
- You finished a multi-file change and should verify reuse and hot-path impact

## Phase 1 — Identify changes

- If **run_command** is allowed and the project is a Git repo: run `git diff` or `git diff HEAD` from the repository root (see **git-helper** skill for `git -C` usage).
- If there is no diff: review files the user named or that you edited in this task; use **read_file** on those paths.

## Phase 2 — Three review passes (sequential or in separate reasoning blocks)

Work from the same change set for all three.

### Pass A: Reuse

- Use **grep_content** and **search_files** to find existing helpers, utilities, or patterns that could replace new code.
- Flag duplicated logic that could call a shared function or module.
- Prefer extending existing abstractions over parallel near-copies.

### Pass B: Quality

- Redundant or derivable state; leaked internals; parameter sprawl; copy-paste with small variations.
- Stringly-typed values where constants or enums already exist.
- Comments that only restate the code — remove; keep non-obvious **why** and invariants.

### Pass C: Efficiency

- Redundant I/O, N+1 patterns, work on hot paths that could be guarded or batched.
- Reading whole files when **grep_content** could narrow scope first.
- Unbounded structures or missing cleanup where relevant.

## Phase 3 — Fix

- Aggregate findings; apply **edit_file**, **search_replace**, or **write_file** as appropriate.
- Run tests via **run_command** only if allowed and the user expects it.
- Summarize what you fixed; note false positives you skipped.

## Tools

- **read_file**, **grep_content**, **search_files**, **edit_file**, **search_replace**, **write_file**, **apply_patch**
- **run_command** : `git diff`, test commands (if policy allows)

## Installation

```
Install the code-simplify skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/code-simplify
```
