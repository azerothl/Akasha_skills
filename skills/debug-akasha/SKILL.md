---
name: debug-akasha
description: Diagnose Akasha daemon, CLI, and config issues. Use when the user reports crashes, connection failures, missing tools, or wants to know where logs and data live.
license: MIT
compatibility: Uses run_command for `akasha doctor`, `akasha --help`, version checks; read_file for config/logs under allowed paths. Paths depend on install/OS.
metadata:
  version: "1.0"
---

# Debug Akasha

Structured troubleshooting for the **Akasha** stack (CLI, daemon, UI, skills, tools policy).

## When to Use

- Daemon not reachable, chat/TUI errors, or “tool denied” confusion
- User asks where configuration, data directory, or logs are
- After upgrade: version skew or cache issues

## Phase 1 — Version and health

If **run_command** is allowed:

- Run `akasha --version` or equivalent from PATH.
- Run `akasha doctor` (or project-documented health command) and summarize output.

If **run_command** is not allowed: ask the user to paste `akasha doctor` output.

## Phase 2 — Configuration

- Use **read_file** on paths the user provides (`tools_policy.yaml`, config files under data dir).
- Explain common knobs: `allowed_read_paths`, `allowed_commands`, `allowed_web_domains`, skill install hosts.

## Phase 3 — Skills and tools

- **list_skills** / **read_skill** — confirm skill loaded and body matches expectation.
- If a tool fails: check policy allows the path or command; quote the relevant rule.

## Phase 4 — Logs and data directory

- Logs and state locations are **installation-specific** (user profile / app data on Windows, `XDG` paths on Linux, etc.). Do not hardcode Anthropic or third-party paths.
- If the user shares a log path under **allowed_read_paths**, use **read_file** on the tail of the file (last lines) rather than loading huge files whole.

## Phase 5 — Escalation

- Capture: OS, Akasha version, exact error message, last steps before failure.
- Suggest minimal repro (single command or UI path).

## Safety

- Do not ask for secrets (API keys); remind user to redact.
- Do not run destructive commands without explicit confirmation.

## Installation

```
Install the debug-akasha skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/debug-akasha
```
