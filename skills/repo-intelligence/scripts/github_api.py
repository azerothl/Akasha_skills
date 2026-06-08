#!/usr/bin/env python3
"""Optional GitHub API bridge when github_repo_info tool is unavailable."""
import json
import sys
import urllib.request

API = "https://api.github.com/repos/{owner}/{repo}"


def main():
    if len(sys.argv) != 3:
        print("usage: github_api.py <owner> <repo>", file=sys.stderr)
        sys.exit(1)
    owner, repo = sys.argv[1], sys.argv[2]
    url = API.format(owner=owner, repo=repo)
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "Akasha-skills"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)
    out = {
        "full_name": data.get("full_name"),
        "description": data.get("description"),
        "stars": data.get("stargazers_count"),
        "forks": data.get("forks_count"),
        "open_issues": data.get("open_issues_count"),
        "language": data.get("language"),
        "license": (data.get("license") or {}).get("spdx_id"),
        "default_branch": data.get("default_branch"),
        "updated_at": data.get("updated_at"),
        "topics": data.get("topics", []),
        "html_url": data.get("html_url"),
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
