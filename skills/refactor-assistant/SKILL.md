---
name: refactor-assistant
description: Assist with targeted refactorings: consistent renaming (symbol or file), extract function/module, apply simple patterns across multiple files. Use when the user asks to rename X to Y project-wide, extract a function, or apply a pattern.
license: MIT
metadata:
  version: "1.0"
---

# Refactor Assistant

Help with code refactorings that span multiple files: renaming symbols or files, extracting functions or modules, and applying simple search-replace or patch-based edits. Uses grep to find all occurrences, then search_replace, edit_file, or apply_patch. Respects require_approval for write tools.

## When to Use

- User asks to rename a symbol or file consistently across the project
- User wants to extract a function or module (identify scope, then propose edits)
- User asks to apply a simple pattern or replacement in several files

## Workflow

1. **Understand** : Clarify the refactoring (e.g. "rename X to Y", "extract this block into a function"). Identify the symbol, string, or file name and the target.
2. **Discover** : grep_content for all occurrences of X (identifiers, strings, file names). search_files if renaming files (e.g. find all files named or referencing the old name).
3. **Context** : read_file on affected files to avoid false positives (e.g. same identifier in comments vs code, or in another module).
4. **Propose** : Build a list of edits (file, location, old → new). Prefer search_replace for full-file replacements, edit_file for line ranges, apply_patch for multi-hunk changes.
5. **Execute** : For each change, if require_approval is set for write_file/edit_file/apply_patch, the daemon will ask the user; otherwise summarize and run the tool. After edits, give a short summary (files modified, count of occurrences).

## Tools to Use

- **grep_content** : Find all occurrences of the symbol or string.
- **search_files** : Find files by name or pattern when renaming files.
- **read_file** : Read files to confirm context before editing.
- **search_replace** : Replace all occurrences of a string in a file.
- **edit_file** : Replace a line range with new content.
- **apply_patch** : Apply a unified diff for multi-change edits.
- **write_file** : Only when creating a new file (e.g. extracted module).

## Execution (How to run in Akasha)

- **Find occurrences** : grep_content <repo_or_dir> "<pattern>" with a regex or literal for the symbol/string. Refine pattern to avoid irrelevant matches.
- **Read and plan** : read_file on each file that contains matches; decide exact replacements (whole word vs substring, comment vs code).
- **Apply** : search_replace path "old" | "new" for global in-file replacement; edit_file path start_line end_line "new_content" for block replacement; apply_patch path "<unified_diff>" for complex changes.
- **Summary** : After all edits, reply with the list of modified files and total occurrence count. If the user refused an approval, note which changes were skipped.

## Behavior Guidelines

- Do not refactor outside allowed_read_paths / allowed_write_paths. If a path is denied, explain and suggest adding it to tools_policy.
- Prefer the smallest safe change: avoid replacing inside string literals or comments unless the user explicitly asked for that.
- For renames, consider imports/usages in other files and update them in the same run when possible.

## Installation

To install this skill, send the following to your Akasha agent:

```
Install the refactor-assistant skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/refactor-assistant
```
