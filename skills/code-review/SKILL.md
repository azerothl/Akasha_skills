---
name: code-review
description: Review code for style, obvious risks, and good practices. Use when the user asks for a code review, wants to check code quality, find potential bugs, or improve style. Reads files and uses grep/search; does not run linters unless via run_command.
license: MIT
compatibility: Core review uses only read_file and grep_content (no external deps). Optional: run linters via run_command (e.g. cargo clippy, ruff check) if allowed in tools_policy; requires corresponding toolchain (Rust, Python, etc.) installed.
metadata:
  version: "1.0"
---

# Code Review

Perform lightweight code review using read_file, grep_content, and run_command (for linters if allowed). Focus on structure, naming, obvious bugs, and best practices.

## When to Use

- User asks to review code, check code quality, or suggest improvements
- User asks to find potential bugs or style issues in a file or directory
- User wants a second pair of eyes before committing or opening a PR

## Tools to Use

- **read_file** : Load the file(s) to review. Prefer reading the full file when it is under a few hundred lines.
- **grep_content** : Search for patterns (e.g. TODO, FIXME, unsafe, deprecated, hardcoded secrets).
- **search_files** : Discover relevant files (e.g. all .rs or .py in a directory).
- **run_command** : If allowed, run a linter or formatter (e.g. `cargo clippy`, `ruff check`) and summarize results.

## Execution (How to run in Akasha)

- For a single file: use **read_file** on the path (must be under allowed_read_paths). Analyze and respond with structured feedback (style, risks, suggestions).
- For patterns: use **grep_content** with a directory and pattern (e.g. `grep_content /project "TODO|FIXME"`).
- For project-wide review: use **search_files** to list files by extension, then **read_file** on key files (main, lib, config).
- If tools_policy allows: **run_command** to run static analysis (e.g. `cargo clippy --no-deps 2>&1` or `ruff check .`) and summarize output.

## Behavior Guidelines

- Structure feedback into sections: Strengths, Issues/Risks, Suggestions. Be concise.
- Do not execute or build the code unless the user explicitly asks and run_command is allowed.
- If a path is denied by policy, explain that the user must add it to allowed_read_paths in tools_policy.yaml.

## Installation

To install this skill, send the following to your Akasha agent:

```
Install the code-review skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/code-review
```
