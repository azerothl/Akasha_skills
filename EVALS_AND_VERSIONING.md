# Skills: semver, changelog, evals (Hermes-style hub)

## Versioning

- Each published skill should expose **`version`** in `skill.json` (semver) and keep **`SKILL.md`** frontmatter `name` / `description` in sync.
- Breaking behaviour changes → **major** bump; additive instructions → **minor**; typo fixes → **patch**.

## Changelog

- Maintain a short **CHANGELOG** section at the bottom of `SKILL.md` or a dedicated `CHANGELOG.md` in the skill folder before tagging releases.

## Bundles & installs

- The Akasha daemon records successful installs in **`skills.lock.jsonl`** (digest + ref). Prefer **tagged** or **commit-pinned** raw URLs for `install_url`.

## Evals (CI)

- **Workflow:** `.github/workflows/skills-eval-smoke.yml` runs on `skills/**` changes: rebuilds `skills.json` and validates JSON + required keys (`id`, `name`, `version`, `install_url`) + semver-shaped `version`.
- **Goal:** extend with per-skill scripts (e.g. `python skills/foo/scripts/self_check.py`) once a convention is agreed; track in repo issues.

## Quality metadata

- Use `tags`, `category`, and `featured` in `skill.json` for discovery; add **`compatibility`** (Akasha version range) when you know minimum daemon features.
