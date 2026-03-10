---
name: sentiment-analysis
description: Analyze sentiment (positive/negative) of text using a Python script and Hugging Face Transformers. Use when the user asks for the sentiment of a message, review, or any text.
license: MIT
compatibility: Python 3.8+, pip, and dependencies in requirements.txt (transformers, torch). First run may download the model (e.g. distilbert-base-uncased-finetuned-sst-2-english). Install with pip install -r requirements.txt in the skill directory once.
requires:
  bins: [python]
metadata:
  version: "1.0"
---

# Sentiment Analysis

Analyze the sentiment of text (positive / negative, with score) using a Python script that runs a Hugging Face Transformers pipeline. This skill uses the **scripts/** folder; the agent runs it via **run_command** with the path to the script.

## When to Use

- User asks for the sentiment of a sentence, message, or review
- User wants to know if a text is positive, negative, or neutral
- User asks to analyze opinions or tone in a piece of text

## Workflow

1. **Input** : Get the text from the user (inline in the message) or from a file (use read_file on an allowed path, then pass content to the script).
2. **Script path** : Use the skill directory path provided when the skill was installed (« Répertoire du skill ... : &lt;path&gt; »). If not in context, use AKASHA_DATA_DIR/skills/sentiment-analysis or data_dir/skills/sentiment-analysis.
3. **Run** : run_command python &lt;SKILL_DIR&gt;/scripts/sentiment.py "&lt;text&gt;" (escape quotes if needed). For long or file-based text, read_file first then pass the content as the argument.
4. **Output** : Parse the script output (JSON: label, score) and reply in natural language (e.g. « Sentiment : positif (score 0.98) »).

## Tools to Use

- **read_file** : Optional — load text from a file path (within allowed_read_paths) when the user points to a file.
- **run_command** : Required — run `python <SKILL_DIR>/scripts/sentiment.py "<text>"`. The skill directory is from the install_skill success message.

## Execution (How to run in Akasha)

**Do not** use `TOOL: sentiment-analysis "..."` (that would run a binary named sentiment-analysis). Use **run_command** explicitly:

- **Inline text** : `run_command python <SKILL_DIR>/scripts/sentiment.py "<user text>"`. Replace &lt;SKILL_DIR&gt; with the path shown after install (e.g. /path/to/data_dir/skills/sentiment-analysis). If the agent no longer has the path, use the value of AKASHA_DATA_DIR/skills/sentiment-analysis or ask the user for the data directory.
- **Text from file** : First `read_file <path>` to get content, then `run_command python <SKILL_DIR>/scripts/sentiment.py "<content>"` (truncate very long content if needed to avoid timeout).
- **Policy** : Ensure `python` is in allowed_commands (it is added automatically when the skill is installed via install_skill, because this skill declares `requires.bins: [python]`).

## Behavior Guidelines

- If the script fails (e.g. module not found), suggest installing dependencies: `pip install -r <SKILL_DIR>/requirements.txt`.
- For very long text, truncate to the first N characters (e.g. 512) before passing to the script to avoid timeouts; mention truncation in the response.
- Do not expose raw tokenizer output or internal errors; return a user-friendly summary (label + score).

## Installation

To install this skill, send the following to your Akasha agent:

```
Install the sentiment-analysis skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/sentiment-analysis
```

After installation, install Python dependencies once (from the skill directory): `pip install -r requirements.txt` (or `pip install -r scripts/requirements.txt` if requirements are in scripts/).
