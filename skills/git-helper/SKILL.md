---
name: git-helper
description: Git status, log, diff, branches, and conflict resolution guidance. Use when the user asks about repo state, history, changes, or how to resolve merge conflicts. Uses run_command (git) and read_file.
license: MIT
compatibility: Requires Git to be installed and available in PATH. Add `git` to allowed_commands in tools_policy.yaml for run_command invocations.
metadata:
  version: "1.0"
---

# Git Helper

Assist with Git workflows: status, log, diff, branches, and conflict resolution. All git commands run via run_command; paths must be under allowed_read_paths and, for writes, allowed in tools_policy.

## When to Use

- User asks for git status, recent commits, or branch list
- User wants to see a diff, compare branches, or understand what changed
- User has merge/rebase conflicts and wants step-by-step resolution
- User asks how to undo a commit, stash, or create a branch

## Tools to Use

- **run_command** : Execute read-only git commands (status, log, branch, diff, show). For write operations (commit, checkout, merge, rebase), only suggest commands unless the user explicitly asks to run them and they are allowed.
- **read_file** : Read conflicted files or .git/config to help resolve conflicts or explain remotes.
- **grep_content** or **search_files** : Locate conflict markers (<<<<<<<, =======, >>>>>>>) in the repo.

## Execution (How to run in Akasha)

- Status / log / branches: use **run_command** from the repo root, e.g. `run_command git -C /path/to/repo status`, `git -C /path log -5 --oneline`, `git branch -a`.
- Diffs: **run_command** `git -C <repo> diff`, `git diff --staged`, or `git diff branch1..branch2`.
- Conflict resolution: use **read_file** on conflicted files to show the conflict blocks, then explain how to edit (keep ours/theirs or merge manually). Use **grep_content** to list files containing conflict markers if needed.
- Do not run destructive or write commands (reset --hard, push --force) without explicit user confirmation; prefer suggesting the command.

## Behavior Guidelines

- Always run git from the repository root; use `git -C <path>` if the working directory is elsewhere.
- For conflicts, show the exact conflict blocks and give clear steps (edit, add, commit).
- If run_command git is not allowed, explain that the user must add `git` (or the full path) to allowed_commands in tools_policy.yaml.

## Installation

To install this skill, send the following to your Akasha agent:

```
Install the git-helper skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/git-helper
```
