---
name: plan-orchestrator
description: Break a multi-step goal into a plan, delegate subtasks via delegate_to_agent with success_check criteria, log progress as JSONL, and run two-pass review (spec then quality). Use for complex features; batch-processing stays for repetitive edits.
license: MIT
metadata:
  version: "1.0"
---

# Plan Orchestrator

Long-horizon task execution using Akasha **delegate_to_agent** with explicit **success_check** and persistent logs — not robot MCP subtasks.

## Akasha angle

Combines Hermes-style subagent planning with RoboClaw **success_check**, **JSONL progress logs**, and defaulting rules — all via **delegate_to_agent**, not external runtimes.

## When to Use

- User goal spans multiple independent steps (research → implement → test → document)
- User asks for a plan with tracked subtasks and review gates
- Feature work too large for a single agent turn

## Tools to Use

- **write_todos** — High-level plan visible to user
- **delegate_to_agent** — One subtask per delegation with clear prompt
- **read_file** / **grep_content** / **run_command** — Direct work when simpler than delegate
- **write_file** — Append `logs/subtasks.jsonl` under project or data dir

## Execution

### 1. Plan (minimal viable)

If user omits details, infer a **3–7 step** plan rather than blocking. Document assumptions.

### 2. Per subtask

Before each **delegate_to_agent**, define:

```json
{
  "prompt": "Concrete deliverable for this subtask only",
  "success_check": "Observable condition (file exists, test passes, section written)",
  "max_retries": 1,
  "timeout_s": 120
}
```

Append to `logs/subtasks.jsonl`:

```json
{"ts":"ISO8601","step":1,"status":"started","success_check":"..."}
{"ts":"ISO8601","step":1,"status":"completed","evidence":"..."}
```

### 3. Two-pass review

After implementation subtasks:

1. **Spec review** — Matches user intent?
2. **Quality review** — Tests, edge cases, policy compliance

Use **delegate_to_agent** for review with narrow prompts, or self-review if delegation disabled.

### 4. Hard reset on retry

Before retrying a failed subtask: revert partial bad state (git checkout, delete draft file) when safe — document what was reset.

### 5. Completion

Return summary: plan, completed steps, skipped steps, open risks.

## Defaulting rules

- Missing priority → sequential order
- Missing success_check → derive from subtask title ("README updated" → file non-empty)
- Delegation unavailable → execute sequentially in current agent

## Scope boundaries

Do not delegate unrelated skills (install, browser) unless subtask requires it. One subtask = one outcome.

## Provenance

Inspired by Hermes subagent-driven-development and RoboClaw long-horizon patterns; no CoRobot MCP.

## Installation

```
Install the plan-orchestrator skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/plan-orchestrator
```
