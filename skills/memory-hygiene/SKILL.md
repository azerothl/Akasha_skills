---
name: memory-hygiene
description: Review and propose cleanup for long-term memory entries (duplicates, stale, conflicting). Use when the user wants to organize, audit, or reduce noise in Akasha memory.
license: MIT
compatibility: Requires long-term memory enabled. Uses memory_search, memory_stats, memory_store, memory_delete, memory_forget. Read-only review first; apply deletes only after user confirms.
metadata:
  version: "1.0"
---

# Memory hygiene

Audit Akasha **long-term memory** and propose structured changes. Do **not** mass-delete without explicit user approval.

## When to Use

- User asks to clean up, deduplicate, or audit stored memories
- User suspects outdated or conflicting facts in memory
- After a project rename or pivot, to align stored context

## Phase 1 — Inventory

1. **memory_stats** — approximate size and entry count.
2. **memory_search** with broad queries (project name, person, topic) to sample clusters.
3. Repeat **memory_search** with narrower queries for suspected duplicates.

## Phase 2 — Classify

For groups of entries, label each as:

- **Keep** — still accurate and useful
- **Merge** — combine into one clearer **memory_store** (then remove duplicates if user agrees)
- **Stale** — superseded by newer info; prefer **memory_delete** (by id) or **memory_forget** (keyword) after confirmation
- **Conflict** — two entries disagree; surface to user with quotes and suggest resolution

## Phase 3 — Report

Output:

1. **Promotions / merges** — which ids to merge and proposed canonical text
2. **Stale / remove** — ids or keywords and rationale
3. **Conflicts** — need user decision
4. **No change** — briefly note clean areas

## Phase 4 — Apply (only if user confirms)

- **memory_delete** for specific UUIDs
- **memory_forget** for keyword-based removal when appropriate
- **memory_store** to add consolidated facts with clear `source` (e.g. `source project:myapp`)

## Rules

- Present the full proposal before destructive actions.
- Never invent memory content; base conclusions on **memory_search** results shown in context.
- If memory is empty or disabled, say so and stop.

## Installation

```
Install the memory-hygiene skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/memory-hygiene
```
