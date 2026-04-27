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
- **Pilot convention:** `skills/<id>/scripts/self_check.sh` (bash + `python3` sanity on `skill.json`). CI runs **calculator** and **date-time** in `.github/workflows/skills-eval-smoke.yml`; add more skills to that step as they gain scripts.

## Quality metadata

- Use `tags`, `category`, and `featured` in `skill.json` for discovery; add **`compatibility`** (Akasha version range) when you know minimum daemon features.
