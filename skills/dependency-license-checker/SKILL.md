---
name: dependency-license-checker
description: List project dependencies (Cargo, npm, pip) and produce a license report; flag GPL/AGPL or other policy-relevant licenses. Use when the user asks for dependency licenses, compliance check, or "what licenses do we use."
license: MIT
compatibility: Requires the project's package manager (cargo, npm, pip) for listing dependencies. Optional: cargo-license, license-checker, or pip-licenses for direct license info; otherwise read manifest files or web_search.
metadata:
  version: "1.0"
---

# Dependency / License Checker

List dependencies of a project (Rust/Cargo, Node/npm, Python/pip) and produce a license report. Optionally flag licenses that may require attention (e.g. GPL, AGPL). Uses run_command for package metadata and optionally read_file on manifests or web_search for unknown licenses.

## When to Use

- User asks for a list of dependencies and their licenses
- User wants a compliance or license audit of the project
- User asks "what licenses are we using" or "any GPL dependencies?"

## Workflow

1. **Detect ecosystem** : Check for Cargo.toml, package.json, requirements.txt, or pyproject.toml in the project root (search_files or read_file).
2. **List packages** : run_command to get the dependency list: cargo metadata (Rust), npm ls --json (Node), pip list --format=json or pip-licenses (Python). Parse output to get package name and version.
3. **Resolve licenses** : For each package, get license from manifest (read Cargo.toml lockfile, package.json, or run cargo license / license-checker / pip-licenses if available). If unknown, optionally web_search "<package> license" or web_fetch the project's license file.
4. **Report** : Build a table or list (package, version, license). Add a section "Attention" or "Restricted" for licenses that are often policy-sensitive (GPL, AGPL, etc.) and note that the user should confirm with their legal policy.
5. **Deliver** : Return the report in the response; optionally write_file to a path (e.g. LICENSE_REPORT.md) if the user asks to save it.

## Tools to Use

- **read_file** : Read Cargo.toml, Cargo.lock, package.json, package-lock.json, pyproject.toml, requirements.txt to detect dependencies and optionally license fields.
- **run_command** : cargo metadata, npm ls --json, pip list --format=json; or cargo license, npx license-checker --json, pip-licenses --format=json if installed.
- **web_search** / **web_fetch** : Optional — resolve license for a package when not in manifest or tool output.
- **write_file** : Optional — save the report to an allowed path.

## Execution (How to run in Akasha)

- **Rust** : run_command `cargo metadata --no-deps --format-version 1` from project root; parse and optionally run_command `cargo license` if in allowed_commands. Read Cargo.toml for workspace or package license.
- **Node** : run_command `npm ls --all --json` or `npx license-checker --json`; read package.json for license field.
- **Python** : run_command `pip list --format=json` and optionally `pip-licenses --format=json` or parse pyproject.toml / setup.py.
- **Unknown license** : web_search "<package_name> license" and pick the first authoritative result; or web_fetch the repo URL + /blob/main/LICENSE.
- **Report** : Format as markdown table (Package | Version | License). List GPL/AGPL (or user-specified) under "Licenses to review" with a note that legal review may be required.
- **Save** : write_file only if the user asked to save the report; use an allowed path (e.g. project root under allowed_write_paths).

## Behavior Guidelines

- Do not assert legal advice; state that license classification is for informational purposes and the user should verify with their legal/compliance team.
- If a package manager or tool is not allowed in tools_policy, explain and suggest adding it to allowed_commands or provide a manual approach (read manifest only).

## Installation

To install this skill, send the following to your Akasha agent:

```
Install the dependency-license-checker skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/dependency-license-checker
```
