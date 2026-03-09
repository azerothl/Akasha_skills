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

## CI / Automation

The `sync-skills.yml` workflow runs on every push to `main` that modifies a file under `skills/**`. It:

1. Runs `scripts/build_skills.py` to regenerate `skills.json` from all `skills/*/skill.json` files.
2. Commits the updated `skills.json` back to the repository.
3. Pushes the updated `skills.json` to [`Azerothl/Akasha_app`](https://github.com/azerothl/Akasha_app) at `data/skills.json` using the `GH_PAT` secret.

> **Required secret:** `GH_PAT` — a GitHub Personal Access Token with `repo` write access to both repositories.
