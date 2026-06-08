---
name: daily-digest
description: Produce a concise daily digest from recent tasks and memory.
version: 1.0.0
allowed-tools:
  - list_scheduled_tasks
  - memory_search
  - memory_store
  - budget_status
---

# Daily Digest

Create a concise operational summary:

1. What was completed today.
2. What remains blocked.
3. What should happen tomorrow.

Keep the digest under 10 bullet points and store a short recap with `memory_store`.
