---
name: security-audit
description: Lightweight security audit on a code tree: detect risky patterns (secrets, eval, unsafe paths, known vulnerable dependencies). Use when the user asks for a security check, secret scan, or dependency audit. Produces a severity-ranked report.
license: MIT
compatibility: Core uses grep_content and search_files only. Optional run_command for cargo audit, npm audit, pip audit requires those tools in allowed_commands and corresponding package manager installed.
metadata:
  version: "1.0"
---

# Security Audit

Perform a lightweight security audit on a directory or set of files: detect sensitive patterns, unsafe constructs, and optionally run dependency vulnerability scanners. Output a structured report by severity (critical / high / medium).

## When to Use

- User asks for a security check, secret scan, or "find credentials"
- User wants to audit dependencies for known vulnerabilities
- User asks to find risky patterns (eval, exec, hardcoded paths, dangerous HTML)

## Workflow

1. **Scope** : Determine the target directory or file list from the user request (or default to current project root).
2. **Discover** : Use search_files for config files (.env, config*.json, *.pem, *.key). Use grep_content for sensitive patterns (passwords, API keys, eval(, exec(, dangerouslySetInnerHTML, ../ or absolute paths in sensitive contexts).
3. **Analyze** : read_file on suspicious files to confirm context; optionally run_command for cargo audit, npm audit, or pip audit if allowed.
4. **Report** : Synthesize findings into a report by severity (critical / high / medium) with file:line and a short recommendation for each.

## Tools to Use

- **grep_content** : Search for sensitive patterns (secrets, eval, exec, dangerous APIs).
- **search_files** : Find config and key files (.env, *.pem, config*.json).
- **read_file** : Read flagged files to confirm and provide context.
- **run_command** : Optional — cargo audit, npm audit, pip audit (must be in allowed_commands).

## Execution (How to run in Akasha)

- **Pattern scan** : grep_content on the target directory with patterns such as `password\s*=\s*["']`, `api[_-]?key`, `eval\s*\(`, `exec\s*\(`, `dangerouslySetInnerHTML`, `\.env` references. Combine multiple grep_content calls if needed.
- **Config discovery** : search_files with patterns like `*.env`, `config*.json`, `*.pem`, `*.key` under the scope directory.
- **Dependency audit** : From repo root, run_command `cargo audit` (Rust), `npm audit --json` (Node), or `pip audit` (Python) if allowed; parse output and add to report.
- **Report** : Do not write_file unless the user asks to save the report; otherwise return the structured report in your response (sections: Critical, High, Medium; each item: path, line or range, finding, recommendation).

## Behavior Guidelines

- Do not expose full secret values in the report; mention "potential secret at path:line" and recommend rotation.
- Prefer false positives to false negatives for secrets: flag anything that looks like a credential pattern.
- If a path is denied by policy, explain that the user must add it to allowed_read_paths in tools_policy.yaml.

## Installation

To install this skill, send the following to your Akasha agent:

```
Install the security-audit skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/security-audit
```
