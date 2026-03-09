---
name: file-manager
description: List, search, copy, move, rename files and create or clean directories. Use when the user wants to organize files, find files by name or pattern, batch rename, create folder structures, or clean up by extension. Works within allowed_read_paths and allowed_write_paths from tools_policy.
license: MIT
metadata:
  version: "1.0"
---

# File Manager

Help users manage files and directories using Akasha tools. All operations are subject to tools_policy (allowed_read_paths, allowed_write_paths, allowed_commands).

## When to Use

- User asks to list files in a directory, find files by name or pattern, or search content
- User asks to copy, move, rename, or delete files/directories
- User asks to create folders or clean up by extension (e.g. remove all .tmp files)
- User asks to organize or batch-rename files

## Tools to Use

- **search_files** : Find files by glob pattern under a directory (e.g. `search_files /path "*.md"`).
- **grep_content** : Search inside file contents (e.g. `grep_content /path "pattern"`).
- **read_file** : Read a file to show its content or metadata.
- **run_command** : For copy (cp), move (mv), rename (mv), delete (rm), create directory (mkdir), list (ls). Ensure the command is allowed in tools_policy (e.g. add `cp`, `mv`, `rm`, `mkdir`, `ls` to allowed_commands or use a script path).

## Execution (How to run in Akasha)

- Listing: use **run_command** with `ls` (or `dir` on Windows) on an allowed path. Alternatively use **search_files** with a broad pattern (e.g. `*`).
- Copy/move/rename: use **run_command** with `cp`, `mv` (Linux/macOS) or `Copy-Item`, `Move-Item` (PowerShell). Paths must be under allowed_write_paths for destination.
- Create directory: **run_command** `mkdir <path>` (or `New-Item -ItemType Directory` on Windows).
- Delete: **run_command** `rm -r` or `Remove-Item`. Prefer confirmation for bulk deletes.
- Search by name: **search_files** with glob. Search by content: **grep_content**.

If run_command fails with "not allowed", remind the user to add the command or path to tools_policy.yaml.

## Behavior Guidelines

- Never suggest operations outside allowed paths. If the user asks for a path not in policy, explain how to add it to allowed_read_paths/allowed_write_paths.
- For destructive operations (delete, overwrite), summarize what will be done and, if the skill or agent supports it, use require_approval for run_command.
- Prefer relative paths when the user is "in" a project directory; otherwise use absolute paths within allowed bases.

## Installation

To install this skill, send the following to your Akasha agent:

```
Install the file-manager skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/file-manager
```
