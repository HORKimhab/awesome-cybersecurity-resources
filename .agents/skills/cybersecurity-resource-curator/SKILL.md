---
name: cybersecurity-resource-curator
description: Curate cybersecurity resources in this repository's README.md. Use when a request asks to add, update, remove, move, or categorize a security tool, repository, article, guide, course, dataset, or URL — including shorthand like "add url1, url2" or "/add url1 url2".
---

# Cybersecurity Resource Curator

`README.md` (~8k lines) is the only catalog. **Never read it whole** — use `scripts/curate.py`. Never edit `data/automation/state.json` or create per-resource files.

## Add URLs (2 tool calls)

1. `python3 scripts/curate.py prep URL [URL ...]` → one line of sections, then one JSON line per URL:
   - `dup` set → skip it and report the location.
   - `name/desc/homepage/topics` from `gh api`. Fetch the page yourself only when `note` is set (not GitHub / lookup failed) or `desc` is empty or vague.
   - `archived: true` → still add, but mention it in the report.
   - Skip anything without a real security, privacy, or defensive-research use.
2. Pipe all accepted entries in one JSON list to `python3 scripts/curate.py add`:
   ```json
   [{"section": "Scanning", "name": "Tool", "desc": "One factual sentence.",
     "links": {"GitHub": "https://github.com/o/r", "Official site": "https://x.io/", "Documentation": "https://docs.x.io/"},
     "topics": ["a", "b"]}]
   ```
   The script formats the entry, appends it to the end of the section, re-checks duplicates, refuses `Donate`, and runs `git diff --check`.
   For a new section add `"new_section": true, "after": "<closest existing section>"`; do this only when nothing fits and the category is durable.

## Entry rules

- `name`: the official capitalization (repo name unless the project brands it differently).
- `desc`: one concrete sentence on what it does and its security use. Rewrite the GitHub blurb; no marketing, emojis, star counts, or opinions.
- `links`: only verified ones. Add `Official site` from `homepage` when it's a real project site (not the repo itself). Omit unknowns.
- `topics`: the `gh` topics, minus noise (e.g. `hacktoberfest`, `awesome`); omit if empty.

## Section mapping (by primary purpose)

password/hash/wordlist → Password Cracking · rogue AP/Wi-Fi → Evil Twin Attack · Bluetooth/BLE → Bluetooth Security and Analysis · iOS labs → iOS Security Training and Practice · recon/subdomains/assets → Attack Surface Discovery · port/vuln scanners → Scanning · OSINT → Open Source Intelligence · AI agents/LLM red team/guardrails → AI Agent Security and Tooling · web app testing → Web Security · DFIR/evidence → Forensics · binary/decompile → Reverse Engineering · exploit/vuln research → Vulnerability Research · malware/sandbox → Malware Analysis · cloud/IaC → Cloud Security · privacy/anonymity/secrets → Privacy and Anonymity · C2/red team/pentest/anything else → General Security

Use the section names from `prep` output as authoritative.

## Remove / move

- `python3 scripts/curate.py find TEXT` → line and section. Read ~15 lines there, then delete the whole `### Name` block (or move it). Remove only what was explicitly requested; drop a section that becomes empty (never `Donate`).
- Warn that automated discovery may re-add removed resources.

## Report (keep it short)

One line per URL: `✅ Name → Section` · `⏭ Name: duplicate (line N, Section)` · `⚠ URL: reason`. Then at most 2 suggestion lines (e.g. archived repo, missing docs link). Don't commit unless asked; commit style: `docs: add Name1, Name2 (url1, url2)`.

Automated bulk discovery lives in `scripts/discover_resources.py` and `.github/workflows/discover-resources.yml`.
