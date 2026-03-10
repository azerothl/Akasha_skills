---
name: api-spec-consumer
description: From an OpenAPI spec (URL or local path), produce an API summary (endpoints, methods, auth) and optionally example calls (curl or code snippets). Use when the user shares a spec link or file and wants a quick overview or examples.
license: MIT
compatibility: No required external tools. Optional jq or yq (via run_command) improves JSON/YAML parsing; otherwise parse in context from read_file or web_fetch content.
metadata:
  version: "1.0"
---

# API Spec Consumer

Read an OpenAPI (Swagger) specification from a URL or local file and produce a structured summary: endpoints, methods, parameters, and security schemes. Optionally generate example requests (curl or code snippets) for one or two representative endpoints.

## When to Use

- User provides a link or path to an OpenAPI/Swagger spec and wants a summary
- User asks for "API overview" or "list of endpoints" from a spec
- User wants example curl or code for calling the API

## Workflow

1. **Input** : Get the spec via web_fetch (if URL) or read_file (if path). Support JSON and YAML; if binary or unclear, try both.
2. **Parse** : Extract paths, path items, operations (get, post, put, delete, etc.), parameters, requestBody, responses, and security (securitySchemes, operation-level security). Use run_command with jq/yq if available for large specs; otherwise parse in context.
3. **Summarize** : Build a list of endpoints (path + method + short description). Summarize auth (e.g. Bearer, API Key, OAuth2) from components.securitySchemes and top-level security.
4. **Examples** (optional) : For 1–2 representative endpoints (e.g. GET and POST), generate a sample curl command or a short code snippet (e.g. fetch in JS, requests in Python). Include required headers or auth placeholder.
5. **Deliver** : Reply with the summary and optional examples. If the user asked to save, write_file to an allowed path (e.g. API_SUMMARY.md).

## Tools to Use

- **web_fetch** : Fetch the spec from a URL (must be in allowed_web_domains if restricted).
- **read_file** : Read the spec from a local path (allowed_read_paths).
- **run_command** : Optional — jq or yq to query paths, .paths, .components; e.g. jq '.paths | keys' spec.json.
- **write_file** : Optional — write the summary or examples to a file.

## Execution (How to run in Akasha)

- **Fetch** : web_fetch <url> or read_file <path>. If the content is YAML, you may run_command with yq to convert to JSON or parse in context.
- **Extract** : From the spec object, read .paths (each key is a path; each value has get, post, etc.). For each operation, collect summary, parameters, requestBody. Read .components.securitySchemes and .security for auth.
- **Summary** : Format as markdown: ## Endpoints (table or list with Method, Path, Summary); ## Authentication (type and location).
- **Example** : For a chosen endpoint, build curl -X METHOD URL -H "Header: value" or a 3–5 line code snippet. Use a placeholder for base URL and auth (e.g. YOUR_TOKEN).
- **Save** : write_file only if the user requested a file; use an allowed path.

## Behavior Guidelines

- Do not invent endpoints or parameters; only report what is in the spec. If the spec is invalid or incomplete, say so.
- For examples, use placeholders for secrets (API key, token) and document required headers.
- If the spec is very large, summarize the main paths and mention "… and N more endpoints"; optionally list all path keys.

## Installation

To install this skill, send the following to your Akasha agent:

```
Install the api-spec-consumer skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/api-spec-consumer
```
