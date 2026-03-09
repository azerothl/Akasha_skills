---
name: json-yaml-utils
description: Validate, format, extract fields, and convert between JSON and YAML. Use when the user works with configs, API payloads, or structured data. Uses jq, yq, or Python via run_command.
license: MIT
compatibility: Best with jq (JSON) and yq (YAML) installed; falls back to Python if unavailable. Use run_command for all operations.
metadata:
  version: "1.0"
---

# JSON / YAML Utils

Validate, format, extract fields, and convert between JSON and YAML using run_command with jq, yq, or Python.

## When to Use

- User asks to validate, format, or pretty-print JSON or YAML
- User wants to extract a field (e.g. .version, .data[0].name) or filter an array
- User asks to convert JSON to YAML or YAML to JSON
- User works with config files or API responses and needs quick transformations

## Tools to Use

- **read_file** : Load the JSON or YAML file from an allowed path.
- **run_command** : Run jq (JSON), yq (YAML/JSON), or python -c for parsing and conversion. Ensure jq/yq/python are in allowed_commands if required.
- **write_file** : If the user wants to save the result (formatted or converted), use write_file to an allowed path.

## Execution (How to run in Akasha)

- **Format/validate JSON** : `run_command jq . file.json` (or `python -m json.tool file.json`). Read file first with **read_file** if needed, or pass path to jq/python.
- **Extract field** : `run_command jq '.field' file.json` or `jq '.data[0]' file.json`. For YAML: `run_command yq '.field' file.yaml`.
- **JSON → YAML** : `run_command yq -P -r '.' (jq -s . file.json | yq -P -)` or use Python: `python -c "import json,yaml; print(yaml.dump(json.load(open('file.json'))))"`.
- **YAML → JSON** : `run_command yq -o=json file.yaml` or Python with PyYAML.
- **Write result** : Use **write_file** with the output of the command (you may need to run_command and then write_file with the captured stdout).

If jq or yq is not allowed or not installed, use Python one-liners for JSON (stdlib) or YAML (PyYAML). Mention in the response if you fell back to Python.

## Behavior Guidelines

- For large files, prefer streaming or extracting only the needed part to avoid huge outputs.
- On invalid input, report the first error (e.g. jq or Python error message) and suggest fixing the syntax.
- When writing, respect allowed_write_paths; do not overwrite without user intent.

## Installation

To install this skill, send the following to your Akasha agent:

```
Install the json-yaml-utils skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/json-yaml-utils
```
