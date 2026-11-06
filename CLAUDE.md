# Awesome Cybersecurity Resources

Curated list; `README.md` (~8k lines, ~440 KB) is the only catalog.

- **Never read README.md whole.** Use `python3 scripts/curate.py prep|add|find` (see `--help`).
- Add/remove/move resources: `/add url1 url2` or delegate to the `resource-curator` agent. Rules live in `.claude/skills/cybersecurity-resource-curator/SKILL.md` (mirror any change to `.agents/skills/...`).
- Never edit `data/automation/state.json` (owned by `scripts/discover_resources.py` + `.github/workflows/discover-resources.yml`).
- Commit only when asked. Style: `docs: add Name1, Name2 (url1, url2)`, `chore(skill|agent): ...`.
