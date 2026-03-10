---
name: changelog-releaser
description: Generate a draft CHANGELOG or release notes from Git history (since last tag or a date). Use when the user wants release notes, a changelog for a new version, or a summary of commits since last release.
license: MIT
compatibility: Requires Git installed and available in PATH. Add git to allowed_commands in tools_policy.yaml. Write operations need allowed_write_paths for the repo.
metadata:
  version: "1.0"
---

# Changelog / Release Notes

Generate a draft CHANGELOG or release notes from the Git history (from the last tag or a given range). Commits can be grouped by type (feat, fix, docs, refactor, etc.) when using conventional commits.

## When to Use

- User asks for release notes, changelog draft, or "what changed since last release"
- User wants to prepare a new version announcement from recent commits
- User asks for a summary of commits since a tag or date

## Workflow

1. **Scope** : Determine the repository path (current project or user-provided). Run from repo root.
2. **Discover** : run_command to get the latest tag (e.g. git describe --tags --abbrev=0) and then git log TAG..HEAD --oneline --no-merges (or git log --since=DATE if user specified a date).
3. **Parse** : Parse commit subjects; if they follow conventional commits (feat:, fix:, docs:, refactor:), use that for grouping; otherwise keep a flat list.
4. **Group** : Group by type (Features, Fixes, Documentation, Refactoring, etc.) or leave as a single list.
5. **Write** : write_file a draft CHANGELOG.md or a release-notes block. Include a short note like "Draft — please review before publishing."

## Tools to Use

- **run_command** : git -C <repo> describe --tags --abbrev=0; git -C <repo> log TAG..HEAD --oneline --no-merges; optionally git log --format=... for full messages.
- **read_file** : Optionally read existing CHANGELOG.md to prepend or match format.
- **write_file** : Write the draft CHANGELOG or release notes to an allowed path.

## Execution (How to run in Akasha)

- **Get last tag** : run_command `git -C <repo_path> describe --tags --abbrev=0` (or handle repos with no tags: use git rev-list --max-parents=0 HEAD or a default range).
- **Get commits** : run_command `git -C <repo_path> log <TAG>..HEAD --oneline --no-merges`. If user asked "since date", use `git log --since="YYYY-MM-DD" --oneline --no-merges`.
- **Optional full messages** : run_command `git -C <repo_path> log <TAG>..HEAD --no-merges --format=%s%n%b` for grouping by conventional prefix.
- **Write draft** : write_file to e.g. CHANGELOG_DRAFT.md or a path the user specified. Use markdown sections (## Features, ## Fixes, etc.) and list commits; add a line "Draft — please review before publishing."

## Behavior Guidelines

- Do not run destructive git commands (reset, push). Only read history and write a file.
- If the repo has no tags, suggest using "since date" or use HEAD~N as range and mention it in the draft.
- Respect allowed_write_paths; if writing to the repo, ensure the path is allowed.

## Installation

To install this skill, send the following to your Akasha agent:

```
Install the changelog-releaser skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/changelog-releaser
```
