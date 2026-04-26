# Akasha Skills

Skills library for autonomous agents (specifically made for [Akasha](https://github.com/azerothl/Akasha_app)).

📦 **Browse skills:** [https://azerothl.github.io/Akasha_skills](https://azerothl.github.io/Akasha_skills)

---

## Repository structure

```
Akasha_skills/
├── skills/
│   └── <skill-id>/
│       ├── SKILL.md     # Agent instructions (required – agentskills.io spec)
│       ├── skill.json   # Skill metadata for the gallery (id, name, version, …)
│       ├── references/  # Optional – supporting docs referenced by SKILL.md
│       └── scripts/     # Optional – helper scripts
├── scripts/
│   └── build_skills.py  # Aggregates all skill.json files → skills.json
├── skills.json          # Auto-generated index (do not edit manually)
├── index.html           # Skills gallery web page
└── .github/
    └── workflows/
        └── sync-skills.yml  # CI: rebuilds skills.json and syncs to Akasha_app
```

---

## Adding a new skill

1. Create a folder under `skills/<your-skill-id>/`.
2. Add a **`SKILL.md`** (uppercase) — this is the core agent instructions file, following the [agentskills.io specification](https://agentskills.io/specification). It must include YAML frontmatter:

   ```markdown
   ---
   name: my-skill
   description: What the skill does and when the agent should use it.
   ---
   
   # My Skill
   
   Agent instructions here…
   ```

3. Add a `skill.json` with the following fields for the gallery:

   | Field | Type | Description |
   |---|---|---|
   | `id` | string | Unique identifier (lowercase, no spaces) |
   | `name` | string | Display name |
   | `version` | string | Semantic version (e.g. `1.0.0`) |
   | `description` | string | Short description of what the skill does |
   | `author` | string | Author name or organization |
   | `category` | string | Category (e.g. `finance`, `utility`, `productivity`) |
   | `tags` | string[] | List of searchable tags |
   | `icon` | string | Icon name (see [Lucide Icons](https://lucide.dev)) |
   | `featured` | boolean | Whether the skill is highlighted |
   | `install_url` | string | Raw URL to `SKILL.md` |
   | `install_command` | string | Command for the agent to install the skill |

4. Optionally add `references/` for supporting docs and `scripts/` for helper scripts.
5. Open a pull request — CI will automatically rebuild `skills.json` on merge and sync it to `Akasha_app/data/skills.json`.

---

## Skill format reference (creating your own skill)

If you want to create a skill for your own use (e.g. hosted elsewhere or only in your `data_dir`), the daemon only needs a valid **SKILL.md**. The format below is what Akasha expects so the agent can discover and use your skill.

### Required file: SKILL.md

- **Filename:** `SKILL.md` (uppercase).
- **Frontmatter (YAML between `---`):**
  - **Required:** `name` (identifier, e.g. `my-skill`), `description` (short text: when the agent should use this skill; used for routing).
  - **Optional:** `license`, `compatibility`, `metadata` (e.g. `version: "1.0"`).
- **Body:** Markdown with instructions for the agent (when to use the skill, which tools to call, guidelines, examples). See the [Agent Skills specification](https://agentskills.io/specification).

### skill.json (for the gallery / catalog)

If you publish the skill in the Akasha_skills gallery or another tool that reads the catalog, add a `skill.json` with:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier (lowercase, no spaces) |
| `name` | string | Display name |
| `version` | string | Semantic version (e.g. `1.0.0`) |
| `description` | string | Short description |
| `author` | string | Author or organization |
| `category` | string | e.g. `utility`, `productivity` |
| `tags` | string[] | Searchable tags |
| `icon` | string | [Lucide](https://lucide.dev) icon name |
| `featured` | boolean | Whether highlighted in gallery |
| `install_url` | string | Raw URL to `SKILL.md` |
| `install_command` | string | Phrase for the agent to install the skill |

For a **user-only** skill (files in `data_dir/skills/` or install via URL without listing in the gallery), **only SKILL.md is required**; the daemon does not need `skill.json`. `skill.json` is used by the [Skills Library](https://azerothl.github.io/Akasha_app/skills.html) and catalog consumers.

### Optional directory structure

- `references/` — extra docs (e.g. REFERENCE.md) the skill can refer to.
- `scripts/`, `assets/` — helpers and assets (see [What are skills?](https://agentskills.io/what-are-skills)).

When installing from GitHub, the daemon can fetch the repo tree (SKILL.md + these folders). For other hosts, only the file at the install URL (usually `SKILL.md`) is downloaded unless the host supports directory listing.

### Installing your skill

- **Via agent:** Ask in chat, e.g. “Install the skill from https://…” The agent uses the `install_skill` tool; the URL must point to a raw `SKILL.md` or a path where `SKILL.md` is available.
- **Manual:** Copy your skill folder into `data_dir/skills/<name>/`, then type `/skills reload` in chat.

For non-GitHub hosts, configure `allowed_skill_install_hosts` in `tools_policy.yaml` (see [Akasha docs](https://azerothl.github.io/Akasha_app/docs.html#configuration)).

### Minimal SKILL.md example

```markdown
---
name: my-skill
description: Use when the user wants to do X. Do Y and Z.
---

# My Skill

When the user asks for X, use the tools A and B. Return the result in format …
```

---

## Versioning, changelog, evals

See **[EVALS_AND_VERSIONING.md](EVALS_AND_VERSIONING.md)** for semver discipline, lockfile alignment with Akasha `skills.lock.jsonl`, and the planned evals CI story (Hermes-style quality loop).

## CI / Automation

The `sync-skills.yml` workflow runs on every push to `main` that modifies a file under `skills/**`. It:

1. Runs `scripts/build_skills.py` to regenerate `skills.json` from all `skills/*/skill.json` files.
2. Commits the updated `skills.json` back to the repository.
3. Pushes the updated `skills.json` to [`Azerothl/Akasha_app`](https://github.com/azerothl/Akasha_app) at `data/skills.json` using the `GH_PAT` secret.

> **Required secret:** `GH_PAT` — a GitHub Personal Access Token with `repo` write access to both repositories.
