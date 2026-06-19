#!/usr/bin/env python3

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set


ROOT = Path(__file__).resolve().parents[1]
RESOURCE_FILE = ROOT / "awesome-cybersecurity-resources.md"
STATE_FILE = ROOT / "data" / "automation" / "state.json"
PER_RUN = 10

SEARCH_QUERIES = [
    "cybersecurity tool stars:>150 pushed:>2024-01-01 archived:false",
    "security research tool stars:>150 pushed:>2024-01-01 archived:false",
    "pentest tool stars:>150 pushed:>2024-01-01 archived:false",
    "osint tool stars:>150 pushed:>2024-01-01 archived:false",
    "network scanner security stars:>150 pushed:>2024-01-01 archived:false",
]

CATEGORY_KEYWORDS = [
    ("password", "Password Cracking", "password-cracking"),
    ("hash", "Password Cracking", "password-cracking"),
    ("recon", "Attack Surface Discovery", "reconnaissance"),
    ("subdomain", "Attack Surface Discovery", "reconnaissance"),
    ("osint", "Open Source Intelligence", "osint"),
    ("forensic", "Forensics", "forensics"),
    ("malware", "Malware Analysis", "malware-analysis"),
    ("reverse", "Reverse Engineering", "reverse-engineering"),
    ("vulnerability", "Vulnerability Research", "vulnerability-research"),
    ("scanner", "Scanning", "network-scanning"),
    ("network", "Scanning", "network-scanning"),
    ("web", "Web Security", "web-security"),
    ("cloud", "Cloud Security", "cloud-security"),
]


@dataclass
class RepoEntry:
    title: str
    description: str
    github_url: str
    homepage_url: Optional[str]
    docs_url: Optional[str]
    topics: List[str]
    stars: int
    category_heading: str
    category_slug: str


def github_request(url: str, token: Optional[str]) -> Dict:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "awesome-cybersecurity-resources-bot",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def load_state() -> Dict:
    if not STATE_FILE.exists():
        return {"seen_repos": [], "last_run": None}
    return json.loads(STATE_FILE.read_text())


def save_state(state: Dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


def load_existing_repo_urls() -> Set[str]:
    if not RESOURCE_FILE.exists():
        return set()
    content = RESOURCE_FILE.read_text()
    return set(re.findall(r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", content))


def categorize(repo: Dict) -> tuple[str, str]:
    haystack = " ".join(
        filter(
            None,
            [
                repo.get("name", ""),
                repo.get("description", ""),
                " ".join(repo.get("topics", [])),
            ],
        )
    ).lower()
    for keyword, heading, slug in CATEGORY_KEYWORDS:
        if keyword in haystack:
            return heading, slug
    return "General Security", "general-security"


def shorten_description(text: Optional[str]) -> str:
    if not text:
        return "Curated cybersecurity resource discovered by the scheduled GitHub automation."
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= 220:
        return text
    return text[:217].rstrip() + "..."


def build_entry(repo: Dict) -> RepoEntry:
    heading, slug = categorize(repo)
    homepage = repo.get("homepage") or None
    docs_url = homepage if homepage and "docs" in homepage.lower() else None
    if not docs_url:
        docs_url = f"{repo['html_url']}/blob/{repo['default_branch']}/README.md"
    return RepoEntry(
        title=repo["name"],
        description=shorten_description(repo.get("description")),
        github_url=repo["html_url"],
        homepage_url=homepage,
        docs_url=docs_url,
        topics=repo.get("topics", []),
        stars=repo.get("stargazers_count", 0),
        category_heading=heading,
        category_slug=slug,
    )


def search_github(token: Optional[str], existing_urls: Set[str], seen_repos: Set[str]) -> List[RepoEntry]:
    selected: List[RepoEntry] = []
    selected_urls: Set[str] = set()

    for query in SEARCH_QUERIES:
        params = urllib.parse.urlencode(
            {
                "q": query,
                "sort": "updated",
                "order": "desc",
                "per_page": 10,
            }
        )
        url = f"https://api.github.com/search/repositories?{params}"
        payload = github_request(url, token)
        for repo in payload.get("items", []):
            repo_url = repo["html_url"]
            if repo_url in existing_urls or repo_url in seen_repos or repo_url in selected_urls:
                continue
            if repo.get("archived") or repo.get("fork"):
                continue
            selected.append(build_entry(repo))
            selected_urls.add(repo_url)
            if len(selected) >= PER_RUN:
                return selected
    return selected


def format_entry(entry: RepoEntry) -> str:
    lines = [
        f"### {entry.title}",
        "",
        entry.description,
        "",
        f"- GitHub: {entry.github_url}",
    ]
    if entry.homepage_url:
        lines.append(f"- Official site: {entry.homepage_url}")
    if entry.docs_url and entry.docs_url != entry.homepage_url:
        lines.append(f"- Documentation: {entry.docs_url}")
    if entry.topics:
        lines.append(f"- Topics: {', '.join(entry.topics[:8])}")
    lines.append("")
    return "\n".join(lines)


def append_entries(entries: Iterable[RepoEntry]) -> None:
    if not entries:
        return

    content = RESOURCE_FILE.read_text() if RESOURCE_FILE.exists() else "# Awesome Cybersecurity Resources\n"
    content = content.rstrip() + "\n\n"

    grouped: Dict[str, List[RepoEntry]] = {}
    for entry in entries:
        grouped.setdefault(entry.category_heading, []).append(entry)

    for heading, items in grouped.items():
        if f"## {heading}\n" not in content:
            content += f"## {heading}\n\n"
        marker = f"## {heading}\n"
        start = content.index(marker) + len(marker)
        next_section = content.find("\n## ", start)
        block = content[start:] if next_section == -1 else content[start:next_section]
        block = block.rstrip() + "\n\n"
        for item in items:
            block += format_entry(item)
        if next_section == -1:
            content = content[:start] + block
        else:
            content = content[:start] + block + content[next_section:]

    RESOURCE_FILE.write_text(content.rstrip() + "\n")


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    existing_urls = load_existing_repo_urls()
    state = load_state()
    seen_repos = set(state.get("seen_repos", []))

    try:
        entries = search_github(token, existing_urls, seen_repos)
    except urllib.error.HTTPError as exc:
        print(f"GitHub API request failed: {exc.code} {exc.reason}", file=sys.stderr)
        return 1
    except urllib.error.URLError as exc:
        print(f"GitHub API request failed: {exc.reason}", file=sys.stderr)
        return 1

    if not entries:
        print("No new repositories found.")
        return 0

    append_entries(entries)
    state["seen_repos"] = sorted(seen_repos | {entry.github_url for entry in entries})
    state["last_run"] = datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")
    save_state(state)

    print(f"Added {len(entries)} resource entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
