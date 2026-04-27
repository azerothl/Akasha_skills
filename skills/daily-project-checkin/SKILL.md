---
name: daily-project-checkin
description: Create and review daily project check-ins using schedule_task and memory tools.
version: 1.0.0
allowed-tools:
  - schedule_task
  - list_scheduled_tasks
  - cancel_scheduled_task
  - memory_search
  - memory_store
---

# Daily Project Check-in

Use this skill when the user wants a recurring project follow-up.

## Workflow

1. Ask which project is targeted and preferred local time.
2. Create a recurring task with `schedule_task` using a cron expression.
3. Store context in long-term memory with `memory_store`:
   - project name
   - check-in cadence
   - expected outputs
4. On each check-in, summarize:
   - what changed since last run
   - blockers
   - next action with owner and due date

## Safety

- Do not overwrite an existing schedule without explicit user confirmation.
- If the user asks to stop follow-ups, call `cancel_scheduled_task`.
