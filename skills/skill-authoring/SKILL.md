---
name: skill-authoring
description: Guide for writing reusable Akasha skills (SKILL.md with YAML front matter). Use when the user wants to create, split, or document a workflow as an installable skill.
license: MIT
compatibility: Doc-only skill; uses read_file/write_file if creating files. Aligns with Agent Skills layout under agentskills.io and Akasha loader in akasha-daemon.
metadata:
  version: "1.0"
---

# Skill authoring (Akasha)

Turn a repeatable workflow into a **directory** `{skill-id}/SKILL.md` loadable by Akasha’s daemon.

## Directory layout

- One folder per skill: `skills/<skill-id>/SKILL.md`
- **Front matter** (YAML between `---` delimiters) must include at least:
  - `name`: machine id; **should match** the parent folder name (Akasha warns if not).
  - `description`: one line; when to use this skill (helps `list_skills` / routing).

Optional front matter used by Akasha:

- `tool_ref`: bind to an internal tool name when the skill is shorthand for a single tool (extension).
- `agents`: restrict to agent types (empty = all).

## Body content (markdown)

After the closing `---` of the front matter, write:

1. **Title** and short purpose.
2. **When to use** — triggers and examples.
3. **Tools to use** — map steps to Akasha tools (`read_file`, `grep_content`, `run_command`, `memory_store`, `write_todos`, etc.).
4. **Execution** — numbered procedure the model should follow.
5. **Guidelines** — safety, policy (`tools_policy.yaml`), path constraints.
6. **Installation** — block with `install_skill` URL pointing at this folder (GitHub tree URL pattern).

## Quality checklist

- [ ] `name` matches directory name (`skill-authoring` ↔ `skills/skill-authoring/`).
- [ ] `description` states *when* to invoke, not only *what* the skill does.
- [ ] No references to products or paths that do not exist in Akasha (use generic “data dir”, “tools policy”).
- [ ] Steps cite concrete tool names Akasha exposes (see system tool list).
- [ ] Optional: `license`, `compatibility`, `metadata.version` for sharing in **Akasha_skills**.

## Minimal template

```markdown
---
name: my-skill
description: One line. Use when the user ...
---

# My Skill

## When to Use
...

## Tools
- **read_file** ...
- **grep_content** ...

## Execution
1. ...

## Installation
Install the my-skill skill from https://github.com/ORG/REPO/tree/main/skills/my-skill
```

## Publishing

- Add the folder under the **Akasha_skills** repo (or host `SKILL.md` on HTTPS per `install_skill` rules).
- User runs **install_skill** with the GitHub tree URL or uses **/skills reload** after copying into `data_dir/skills/`.

## Installation

```
Install the skill-authoring skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/skill-authoring
```
