---
name: log-incident-analyzer
description: Analyze a log file or command output to extract errors, stack traces, and produce a chronological summary plus root-cause hypotheses. Use when the user shares logs, a crash dump, or asks why something failed.
license: MIT
metadata:
  version: "1.0"
---

# Log / Incident Analyzer

Analyze log files or pasted command output to extract errors, stack traces, and exit codes; produce a chronological summary and root-cause hypotheses. Optionally use web_search to look up known errors or documentation.

## When to Use

- User pastes or points to a log file and asks what went wrong
- User asks to analyze a crash, exception, or error output
- User wants a timeline of events or "root cause" from logs

## Workflow

1. **Obtain content** : read_file on the path the user provided, or treat the user message as pasted content (e.g. "here are the logs: ...").
2. **Parse** : Split into lines; detect timestamps (ISO, common log formats), log levels (ERROR, WARN, INFO, DEBUG), and structure (stack traces, exception blocks).
3. **Extract** : Identify error messages, stack traces, HTTP status codes, process exit codes. Use grep_content if the content is in a file and you need to search for patterns (e.g. "ERROR", "Exception", "panic", "Traceback").
4. **Research** (optional) : web_search for the exact error message or exception type (e.g. "rust panic thread 'main'") to find docs or known issues; include links in the summary.
5. **Deliver** : Provide (1) a short summary (Summarizer-style), (2) a timeline of key events, (3) one or more root-cause hypotheses, (4) links or next steps if web_search was used.

## Tools to Use

- **read_file** : Load the log file from an allowed path.
- **grep_content** : Search for patterns (ERROR, Exception, panic, Traceback, exit code) when the log is on disk.
- **web_search** : Optional — look up the error message or exception to find documentation or similar issues.

## Execution (How to run in Akasha)

- **From file** : read_file <path> to get the full content. If the file is very large, grep_content for "ERROR", "FATAL", "Exception", "panic", "Traceback", "exit code" first to get relevant lines, then read_file on the file and focus your analysis on those regions (or ask the user to provide the last N lines).
- **From paste** : If the user pasted logs in the message, analyze that text directly; no tool call needed for the content.
- **Lookup** : web_search "<exact error or exception text>" to find official docs or Stack Overflow; cite the most relevant link(s) in your response.
- **Output** : Reply with: Summary (2–3 sentences), Timeline (ordered list of key events with time if available), Hypotheses (possible causes), and optionally Links (URLs from web_search).

## Behavior Guidelines

- Do not invent stack traces or line numbers; only report what is present in the logs.
- If the log format is unknown, still try to identify obvious error lines and timestamps; state assumptions (e.g. "assuming ISO timestamps").
- For security, do not suggest pasting secrets or tokens; if logs might contain them, recommend redaction.

## Installation

To install this skill, send the following to your Akasha agent:

```
Install the log-incident-analyzer skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/log-incident-analyzer
```
