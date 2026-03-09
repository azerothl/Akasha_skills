---
name: web-researcher
description: Targeted web search, synthesis of results, and fact-checking. Use when the user needs up-to-date information, multiple sources, or verification of facts. Combines web_search and optional web_fetch.
license: MIT
metadata:
  version: "1.0"
---

# Web Researcher

Perform targeted web searches, synthesize results, and help verify facts using web_search and, when allowed, web_fetch.

## When to Use

- User asks for current information (news, rates, documentation, versions)
- User wants multiple sources or a synthesis of what is available online
- User asks to verify a fact or compare claims across sources
- User needs links, citations, or references to official docs or articles

## Tools to Use

- **web_search** : Run one or more search queries. Use clear, specific queries; refine if the first results are off-topic.
- **web_fetch** : If allowed by tools_policy, fetch a specific URL to extract content (e.g. official docs, release notes) and summarize or quote.

## Execution (How to run in Akasha)

- For a single question: use **web_search** with a well-formed query. Summarize the top results and cite sources (URLs) when possible.
- For synthesis: run **web_search** with 1–3 queries covering different angles, then combine findings in your response. Note agreement or disagreement between sources.
- For fact-checking: **web_search** for corroborating or contradicting sources; present a short conclusion and links.
- For deep reading: if the user provides a URL or you get one from search, use **web_fetch** (if allowed) to retrieve the page and summarize or extract the relevant part.

## Behavior Guidelines

- Always prefer authoritative sources (official docs, known publishers). Mention when information might be outdated or from a single source.
- Do not invent URLs; only cite URLs returned by web_search or explicitly provided by the user.
- If web_fetch is not allowed or fails, rely on web_search snippets and suggest the user open the link for full content.

## Installation

To install this skill, send the following to your Akasha agent:

```
Install the web-researcher skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/web-researcher
```
