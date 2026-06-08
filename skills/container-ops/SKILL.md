---
name: container-ops
description: Docker and container workflows aligned with Akasha run_in_container — build hints, compose checks, logs, and safe run_command patterns. Use for DevOps container tasks; not full Kubernetes.
license: MIT
compatibility: Docker CLI on PATH; run_in_container when policy allows.
metadata:
  version: "1.0"
---

# Container Ops

Container operations for Akasha agents using **run_command** and **run_in_container**.

## When to Use

- User asks about Docker images, compose, container logs
- Run tests/builds in isolated container
- Debug Dockerfile or compose.yml

## Tools

- **run_command** — `docker ps`, `docker compose config`, `docker logs`
- **run_in_container** — Execute command in policy-approved image
- **read_file** — Dockerfile, compose.yml

## Safety

- Never mount sensitive host paths without user approval
- No `--privileged` unless explicitly requested and policy allows
- Summarize output; truncate long logs

## Provenance

Inspired by Hermes docker-management; Akasha-native naming.

## Installation

```
Install the container-ops skill from https://github.com/azerothl/Akasha_skills/tree/main/skills/container-ops
```
