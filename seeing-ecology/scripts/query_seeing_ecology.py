#!/usr/bin/env python3
"""Query Juan Li's public bilingual Seeing Ecology concept & graph endpoints."""

from __future__ import annotations
import argparse
import json
from urllib.request import Request, urlopen

DEFAULT_URL = "https://juanli.me/seeing-ecology/api/v1/concepts.json"

def fetch(url: str) -> dict:
    req = Request(url, headers={"User-Agent": "seeing-ecology-skill/1.0"})
    with urlopen(req, timeout=20) as resp:
        return json.load(resp)

def main() -> None:
    parser = argparse.ArgumentParser(description="Query Juan Li · Seeing Ecology concepts.")
    parser.add_argument("--lang", choices=["en", "zh"], default="en")
    parser.add_argument("--q", default="", help="Keyword or concept slug filter")
    parser.add_argument("--url", default=DEFAULT_URL)
    args = parser.parse_args()

    data = fetch(args.url)
    q = args.q.strip().lower()
    for c in data.get("concepts", []):
        blob = json.dumps(c, ensure_ascii=False).lower()
        if q and q not in blob:
            continue
        title = f"{c['title']['en']} ({c['title']['zh']})" if args.lang == "en" else f"{c['title']['zh']} ({c['title']['en']})"
        defn = c["definition"][args.lang]
        cites = " · ".join(c.get("citations", []))
        url = (c.get("urls") or {}).get(args.lang) or "https://juanli.me/seeing-ecology/"
        print(f"- [{c['status'].upper()}] {title}\n  Definition: {defn}\n  Citations: {cites}\n  URL: {url}\n")

if __name__ == "__main__":
    main()
