#!/usr/bin/env python3
"""arXiv Atom API search bridge."""
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ATOM = "http://export.arxiv.org/api/query"


def main():
    if len(sys.argv) < 2:
        print("usage: arxiv_search.py <query> [max=10]", file=sys.stderr)
        sys.exit(1)
    q = sys.argv[1]
    max_r = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    params = urllib.parse.urlencode({"search_query": f"all:{q}", "start": 0, "max_results": max_r})
    url = f"{ATOM}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "Akasha-skills"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        root = ET.fromstring(resp.read())
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for entry in root.findall("a:entry", ns):
        title = (entry.find("a:title", ns).text or "").strip().replace("\n", " ")
        link = entry.find("a:id", ns).text
        published = (entry.find("a:published", ns).text or "")[:10]
        summary = (entry.find("a:summary", ns).text or "").strip().replace("\n", " ")[:300]
        print(f"- [{published}] {title}\n  {link}\n  {summary}...\n")


if __name__ == "__main__":
    main()
