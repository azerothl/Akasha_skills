---
name: synthetic-dataset
description: Generate synthetic datasets (CSV/JSON/JSONL) from a schema (Faker, choice) or by exporting/sampling Hugging Face datasets. Use when the user wants test data, a synthetic dataset, or a sample from a HF dataset (e.g. IMDB, dolly).
license: MIT
compatibility: Python 3.8+, Faker and datasets (Hugging Face) in requirements.txt. HF mode requires network access on first run (download), then local cache.
requires:
  bins: [python]
metadata:
  version: "1.0"
---

# Synthetic Dataset

Generate synthetic or derived datasets (CSV, JSON, JSONL) in two modes:

1. **Schema mode (Faker)** : from a JSON schema of columns (Faker types or choice), generate N rows. No network after install.
2. **Hugging Face mode** : load a dataset from the Hub (e.g. imdb, databricks/databricks-dolly-15k), sample N rows, export to CSV/JSON/JSONL. First run downloads; later runs use cache.

The agent runs the script via **run_command** with the skill directory path (from install_skill success message).

## When to Use

- User asks for test data, a synthetic dataset, or random rows with given columns (schema mode).
- User asks for a sample or export of a Hugging Face dataset (e.g. "500 rows from IMDB", "export databricks-dolly as JSONL") (HF mode).

## Workflow

1. **Understand** : Extract from the user request: columns/types, number of rows, format (CSV/JSON/JSONL), output path. Decide whether the source is a **Faker schema** or a **Hugging Face dataset** (e.g. "like IMDB", "500 rows of databricks-dolly"). If unclear, propose a default schema or ask for clarification.
2. **Source** :
   - **HF mode** : Identify the dataset id (and optionally split, config, columns). No schema file.
   - **Schema mode** : If the user provides a schema file, use read_file then pass content to the script (--schema path or stdin). Otherwise build a schema (e.g. from references/schema_example.json) and write_file it or pass JSON to the script.
3. **Execute** : run_command python &lt;SKILL_DIR&gt;/scripts/generate_dataset.py with either --schema &lt;path&gt; or --from-hf &lt;id&gt; (+ optional --hf-split, --hf-columns), then --rows N --format csv|json|jsonl [--output &lt;path&gt;]. If --output is in allowed_write_paths, the script writes directly; otherwise recommend a path or capture stdout and write_file.
4. **Summary** : Reply with number of rows generated, list of columns, format, and path of the created file.

## Tools to Use

- **read_file** : Read an existing schema or reference file (schema mode).
- **write_file** : Write the schema if created by the agent; or write the dataset content if the script outputs to stdout.
- **run_command** : Run the script with --schema (schema mode) or --from-hf (HF mode). Skill directory = path after install_skill or AKASHA_DATA_DIR/skills/synthetic-dataset.

## Execution (How to run in Akasha)

Do **not** use `TOOL: synthetic-dataset ...`; use **run_command** with the full path to the script.

- **Schema mode** : `run_command python <SKILL_DIR>/scripts/generate_dataset.py --schema <path> --rows 1000 --format csv --output <path>`. For stdin schema: `--schema -` and feed JSON on stdin if the daemon supports it; otherwise write_file the schema first and use --schema &lt;path&gt;.
- **Hugging Face mode** : `run_command python <SKILL_DIR>/scripts/generate_dataset.py --from-hf imdb --rows 500 --format jsonl --output out.jsonl` (optional: --hf-split train, --hf-columns text,label). First run downloads (network).
- **Policy** : requires.bins: [python] in frontmatter adds python to allowed_commands on install. Output paths must be in allowed_write_paths; document in Behavior Guidelines.

## Behavior Guidelines

- Never write outside allowed_write_paths. If the user requests a path that is not allowed, suggest a path under an allowed directory or explain how to add it in tools_policy.
- Limit the number of rows (max 50 000); beyond that, refuse or truncate and say so clearly.
- For schemas, use references/schema_example.json and the list of supported types (uuid, name, email, date, choice, etc.) documented in the skill or in a Reference section.
- If the script fails (missing module, invalid schema), explain and suggest `pip install -r requirements.txt` or fixing the schema.
- In HF mode: if download fails (network, private or unknown dataset), explain and suggest checking the dataset id or connection.

## Installation

To install this skill, send the following to your Akasha agent:

```
Install the synthetic-dataset skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/synthetic-dataset
```

After installation, install Python dependencies once (from the skill directory): `pip install -r requirements.txt`.
