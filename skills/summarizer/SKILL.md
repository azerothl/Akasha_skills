---
name: summarizer
description: Summarize long documents, logs, or command output. Use when the user wants a concise summary of a file, a pasted text, or the output of a command. Best for specs, logs, articles, and verbose responses.
license: MIT
metadata:
  version: "1.0"
---

# Summarizer

Produce concise summaries of documents, logs, or long text. Use read_file to load content, then summarize in structured form (bullets, sections, key facts).

## When to Use

- User asks to summarize a file, an article, or a long message
- User asks for the main points, key takeaways, or a TL;DR
- User wants a summary of command output or logs

## Tools to Use

- **read_file** : Load the document from an allowed path. For very long files, consider summarizing in chunks or the first/last sections plus key middle parts.
- **web_fetch** : If the user provides a URL and the domain is allowed, fetch the page and then summarize (optional).

## Execution (How to run in Akasha)

- For a local file: use **read_file** with the path. Read the content (or a representative part if too long for context), then write a summary in your response. Do not invoke a separate summarization tool; use your own response to provide the summary.
- For URLs: if the user pastes a URL and web_fetch is allowed, use **web_fetch** to retrieve the content, then summarize in your response.
- For command output: if the user has already run a command and pasted output, summarize that directly in your response.

## Behavior Guidelines

- Preserve critical facts, numbers, and decisions. Omit filler and repetition.
- If the content is too long to fit in context, summarize the beginning and end and note that the middle was skimmed for key points.
- For logs, focus on errors, warnings, and the sequence of main events.

## Installation

To install this skill, send the following to your Akasha agent:

```
Install the summarizer skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/summarizer
```
