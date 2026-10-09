#!/usr/bin/env python3
"""Token-cheap helper for manually curating README.md.

  curate.py prep URL [URL ...]   sections + duplicate check + GitHub metadata (JSON)
  curate.py add < entries.json   insert entries at the end of their sections
  curate.py find TEXT            locate entries by name or URL (for moves/removals)

Entry JSON for `add` (list):
  {"section": "Scanning", "name": "Tool", "desc": "One sentence.",
   "links": {"GitHub": "...", "Official site": "...", "Documentation": "..."},
   "topics": ["a", "b"]}
"""
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

README = Path(os.environ.get("CURATE_README") or Path(__file__).resolve().parent.parent / "README.md")
PROTECTED = {"Donate"}
LINK_ORDER = ["GitHub", "Official site", "Documentation"]
MAX_TOPICS = 8


def norm(url):
    u = url.strip().strip("<>").lower()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    u = re.sub(r"[?#].*$", "", u)
    u = re.sub(r"(\.git)?/*$", "", u)
    m = re.match(r"(github\.com/[^/]+/[^/]+)", u)
    return m.group(1) if m else u


def load():
    return README.read_text(encoding="utf-8").split("\n")


def sections(lines):
    return [(i, l[3:].strip()) for i, l in enumerate(lines) if l.startswith("## ")]


def index(lines):
    """Map normalized URL / lowercased title -> 'line N: ### Title (## Section)'."""
    idx, sec, title, tline = {}, None, None, 0
    for i, l in enumerate(lines):
        if l.startswith("## "):
            sec = l[3:].strip()
        elif l.startswith("### "):
            title, tline = l[4:].strip(), i + 1
            idx.setdefault("title:" + title.lower(), f"line {tline}: {title} ({sec})")
        for url in re.findall(r"https?://[^\s)>\]]+", l):
            if title:
                idx.setdefault(norm(url), f"line {tline}: {title} ({sec})")
    return idx


def gh_meta(url):
    m = re.match(r"github\.com/([^/]+)/([^/]+)$", norm(url))
    if not m:
        return {"note": "not a GitHub repo; fetch the page for a description"}
    try:
        out = subprocess.run(
            ["gh", "api", f"repos/{m.group(1)}/{m.group(2)}"],
            capture_output=True, text=True, timeout=30,
        )
        d = json.loads(out.stdout)
    except Exception as e:  # noqa: BLE001
        return {"note": f"gh failed: {e}"}
    if "full_name" not in d:
        return {"note": d.get("message", "gh lookup failed")}
    meta = {
        "name": d["name"],
        "github": d["html_url"],
        "desc": d.get("description") or "",
        "homepage": d.get("homepage") or "",
        "topics": d.get("topics", [])[:MAX_TOPICS],
    }
    if d.get("archived"):
        meta["archived"] = True
    if d["html_url"].lower() != ("https://" + norm(url)):
        meta["redirected"] = True
    return meta


def cmd_prep(urls):
    urls = [u for raw in urls for u in re.split(r"[,\s]+", raw) if u]
    lines = load()
    idx = index(lines)
    with ThreadPoolExecutor(8) as ex:
        metas = list(ex.map(gh_meta, urls))
    res = []
    for url, meta in zip(urls, metas):
        dup = idx.get(norm(url))
        if not dup and meta.get("github"):
            dup = idx.get(norm(meta["github"]))
        if not dup and meta.get("name"):
            dup = idx.get("title:" + meta["name"].lower())
        res.append({"url": url, "dup": dup or False, **({} if dup else meta)})
    print("sections:", " | ".join(s for _, s in sections(lines) if s not in PROTECTED))
    for r in res:
        print(json.dumps(r, ensure_ascii=False))


def render(e):
    out = [f"### {e['name'].strip()}", "", e["desc"].strip(), ""]
    links = {k: v for k, v in (e.get("links") or {}).items() if v}
    seen = set()
    for k in LINK_ORDER + [k for k in links if k not in LINK_ORDER]:
        if k in links and norm(links[k]) not in seen:
            seen.add(norm(links[k]))
            out.append(f"- {k}: {links[k]}")
    if e.get("topics"):
        out.append("- Topics: " + ", ".join(e["topics"][:MAX_TOPICS]))
    return out + [""]


def cmd_add():
    entries = json.load(sys.stdin)
    if isinstance(entries, dict):
        entries = [entries]
    lines = load()
    idx = index(lines)
    report = []
    for e in entries:
        sec = e["section"].strip()
        urls = [norm(v) for v in (e.get("links") or {}).values() if v]
        dup = next((idx[u] for u in urls if u in idx), None) or idx.get("title:" + e["name"].lower())
        if dup:
            report.append(f"⏭ {e['name']}: duplicate, {dup}")
            continue
        if sec in PROTECTED:
            report.append(f"⚠ {e['name']}: refusing to add under ## {sec}")
            continue
        secs = sections(lines)
        pos = next((k for k, (_, s) in enumerate(secs) if s == sec), None)
        if pos is None:
            if not e.get("new_section"):
                report.append(f"⚠ {e['name']}: no section '{sec}' (set new_section: true to create)")
                continue
            # new section goes after the section named in "after", else at end of file
            after = e.get("after")
            apos = next((k for k, (_, s) in enumerate(secs) if s == after), None)
            end = secs[apos + 1][0] if apos is not None and apos + 1 < len(secs) else len(lines)
            while end > 0 and lines[end - 1].strip() == "":
                end -= 1
            block = ["", "", f"## {sec}", ""] + render(e)
            lines[end:end] = block
            at = end + 5
        else:
            end = secs[pos + 1][0] if pos + 1 < len(secs) else len(lines)
            while end > 0 and lines[end - 1].strip() == "":
                end -= 1
            block = [""] + render(e)[:-1]
            lines[end:end] = block
            at = end + 2
        idx = index(lines)
        report.append(f"✅ {e['name']} → {sec} (line {at})")
    README.write_text("\n".join(lines), encoding="utf-8")
    chk = subprocess.run(["git", "diff", "--check", "--", str(README)],
                         capture_output=True, text=True, cwd=README.parent)
    print("\n".join(report))
    print("diff --check:", chk.stdout.strip() or "ok")


def cmd_find(text):
    lines = load()
    key = norm(text)
    hits = {v for k, v in index(lines).items() if key in k or text.lower() in k}
    print("\n".join(sorted(hits, key=lambda h: int(h.split()[1][:-1]))) or "not found")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in {"prep", "add", "find"}:
        sys.exit(__doc__)
    cmd = sys.argv[1]
    if cmd == "prep":
        cmd_prep(sys.argv[2:])
    elif cmd == "add":
        cmd_add()
    else:
        cmd_find(" ".join(sys.argv[2:]))
