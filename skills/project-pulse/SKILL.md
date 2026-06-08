---
name: project-pulse
description: Track project pulse with recurring check-ins and risk summary.
version: 1.0.0
allowed-tools:
  - schedule_task
  - list_scheduled_tasks
  - cancel_scheduled_task
  - memory_search
  - memory_store
---

# Project Pulse

Track project health in recurring loops:

1. Ensure a weekly pulse schedule exists.
2. Summarize progress, risk, owner, next milestone.
3. Persist critical updates with `memory_store`.

If the user asks to stop, cancel the pulse schedule.
