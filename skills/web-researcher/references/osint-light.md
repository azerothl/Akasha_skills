# OSINT-light guidelines

Public-source investigation only. Akasha agents must stay within policy and law.

## Allowed

- **web_search** / **web_fetch** on public web pages
- Official registries, press releases, open GitHub/GitLab repos
- Published academic papers (via search + fetch)
- User-provided documents via **read_file**

## Not allowed

- Credential stuffing, private database access, or social engineering
- Circumventing authentication or paywalls
- Harassment or publishing private personal data (doxxing)

## Evidence chain

For each finding:

1. **Claim** — one sentence
2. **Evidence** — URL or document path
3. **Confidence** — High / Medium / Low
4. **Limitation** — what was not verified

## Report footer

Include: "Investigation used public sources only via Akasha web tools."
