#!/usr/bin/env python3
"""Refresh citation counts (OpenAlex) and GitHub stars baked into index.html.

Cards are discovered from the HTML itself, so adding a paper or repository
card requires no changes to this script. Counts are written as static spans,
so the site makes no external requests at view time.

Usage: python3 update_stats.py
Optional: GITHUB_TOKEN env var raises the GitHub API rate limit (used in CI).
"""

import json
import os
import re
import sys
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(ROOT, "index.html")
MAILTO = "sven@schippkus.eu"

BLOCK_RE = re.compile(
    r'<a\s[^>]*?href="(https://(?:doi\.org|github\.com)/[^"]+)"[^>]*>(.*?)</a>',
    re.S,
)
IMG_RE = r'<img[^>]*alt="{alt}"[^>]*>'
SPAN_RE = r'<span class="count" data-kind="{kind}"[^>]*>[^<]*</span>'
STAR_IMG = re.compile(IMG_RE.format(alt=r"GitHub\s+stars"), re.S)
CITED_IMG = re.compile(IMG_RE.format(alt=r"Citations\s+badge"), re.S)
STAR_SPAN = re.compile(SPAN_RE.format(kind="stars"), re.S)
CITED_SPAN = re.compile(SPAN_RE.format(kind="cited"), re.S)


def fetch_json(url):
    headers = {
        "User-Agent": "schipp.github.io stats updater (mailto:%s)" % MAILTO,
        "Accept": "application/vnd.github+json",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token and "api.github.com" in url:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def fetch_citations(dois):
    if not dois:
        return {}
    filt = "|".join("https://doi.org/" + d for d in dois)
    url = (
        "https://api.openalex.org/works?filter=doi:"
        + urllib.parse.quote(filt, safe="|:/")
        + "&per-page=50&select=doi,cited_by_count&mailto=" + MAILTO
    )
    try:
        data = fetch_json(url)
    except Exception as exc:
        print("WARN: OpenAlex request failed: %s" % exc)
        return {}
    return {
        r["doi"].lower().replace("https://doi.org/", "", 1): r["cited_by_count"]
        for r in data.get("results", [])
        if r.get("doi")
    }


def fetch_citation_single(doi):
    """Fallback for DOIs missing from the batch filter index (new works)."""
    try:
        data = fetch_json(
            "https://api.openalex.org/works/https://doi.org/" + doi
            + "?mailto=" + MAILTO + "&select=doi,cited_by_count"
        )
    except Exception as exc:
        print("WARN: OpenAlex lookup for %s failed: %s" % (doi, exc))
        return None
    return data.get("cited_by_count")


def fetch_repo_stars(repos):
    stars = {}
    for owner, repo in repos:
        try:
            data = fetch_json(
                "https://api.github.com/repos/%s/%s" % (owner, repo)
            )
            stars[(owner, repo)] = data["stargazers_count"]
        except Exception as exc:
            print("WARN: GitHub request for %s/%s failed: %s" % (owner, repo, exc))
    return stars


def fetch_profile_stars(user):
    total, page = 0, 1
    while True:
        try:
            data = fetch_json(
                "https://api.github.com/users/%s/repos?per_page=100&page=%d"
                % (user, page)
            )
        except Exception as exc:
            print("WARN: GitHub request for %s failed: %s" % (user, exc))
            return None
        if not data:
            break
        total += sum(r["stargazers_count"] for r in data)
        page += 1
    return total


def make_span(kind, value):
    return '<span class="count" data-kind="%s">%d</span>' % (kind, value)


def replace_block(block_html, kind, value):
    """Replace the badge img or stale count span inside a card block."""
    img = STAR_IMG if kind == "stars" else CITED_IMG
    stale = STAR_SPAN if kind == "stars" else CITED_SPAN
    span = make_span(kind, value)
    new, n = img.subn(span, block_html)
    if n:
        return new, n
    new, n = stale.subn(span, block_html)
    return new, n


def main():
    html = open(HTML_PATH, encoding="utf-8").read()

    doi_cards, repo_cards, profile_card = [], [], None
    for m in BLOCK_RE.finditer(html):
        href, body = m.group(1), m.group(2)
        if href.startswith("https://doi.org/"):
            doi = href[len("https://doi.org/"):]
            if CITED_IMG.search(body) or CITED_SPAN.search(body):
                doi_cards.append((m, doi))
        elif re.fullmatch(r"https://github\.com/[^/]+", href):
            profile_card = m
        elif re.fullmatch(r"https://github\.com/[^/]+/[^/]+", href):
            if STAR_IMG.search(body) or STAR_SPAN.search(body):
                repo_cards.append((m, href))

    repos = sorted({tuple(r.split("/")[3:5]) for _, r in repo_cards})
    profile_user = (
        profile_card.group(1).rsplit("/", 1)[-1] if profile_card else None
    )
    print("Found %d papers, %d repositories" % (len(doi_cards), len(repo_cards)))

    citations = fetch_citations({d for _, d in doi_cards})
    for doi in {d for _, d in doi_cards} - set(citations):
        count = fetch_citation_single(doi)
        if count is not None:
            citations[doi.lower()] = count
    stars = fetch_repo_stars(repos)
    profile = fetch_profile_stars(profile_user) if profile_user else None

    updates = {"cited": 0, "stars": 0}
    missing = []

    def sub(m):
        href, body = m.group(1), m.group(2)
        if href.startswith("https://doi.org/"):
            key = href[len("https://doi.org/"):].lower()
            if key in citations:
                new, n = replace_block(body, "cited", citations[key])
                updates["cited"] += n
                return m.group(0).replace(body, new, 1)
            missing.append(href)
            return m.group(0)
        if re.fullmatch(r"https://github\.com/[^/]+", href):
            if profile is not None:
                new, n = replace_block(body, "stars", profile)
                updates["stars"] += n
                return m.group(0).replace(body, new, 1)
            return m.group(0)
        owner, repo = tuple(href.split("/")[3:5])
        if (owner, repo) in stars:
            new, n = replace_block(body, "stars", stars[(owner, repo)])
            updates["stars"] += n
            return m.group(0).replace(body, new, 1)
        missing.append(href)
        return m.group(0)

    html = BLOCK_RE.sub(sub, html)

    for href, doi in doi_cards:
        key = doi.lower()
        if key in citations:
            print("  %-40s cited %d" % (doi, citations[key]))
    for (owner, repo), n in sorted(stars.items()):
        print("  %-40s stars %d" % (owner + "/" + repo, n))
    if profile is not None:
        print("  %-40s stars %d" % ("profile " + profile_user, profile))
    if missing:
        print("WARN: no count for %d link(s): %s" % (len(missing), ", ".join(sorted(set(missing)))))

    if html == open(HTML_PATH, encoding="utf-8").read():
        print("No changes.")
        return

    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated index.html: %d citation chips, %d star chips." % (updates["cited"], updates["stars"]))


if __name__ == "__main__":
    sys.exit(main())
