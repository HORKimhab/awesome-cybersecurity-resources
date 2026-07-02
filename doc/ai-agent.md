# AI Agent Workflow

This document defines the repo-local workflow for collecting and indexing cybersecurity resources from the internet first.

## Goal

Store cybersecurity resources in a consistent Markdown plus YAML frontmatter format that is easy to review, search, and automate.

## Canonical Resource Format

Each resource entry should be a Markdown file with YAML frontmatter.

Required fields:
- `title`
- `description`
- `type`
- `category`
- `resources`

Optional fields:
- `suggestion`
- `source_file`
- `source_section`
- `source_repo`
- `source_url`
- `archive_url`
- `tags`

Rules:
- `resources` must contain URL strings only
- one logical resource entry per file
- use kebab-case file names

## Ingestion Workflow

### 1. Internet search

Search the internet for useful tools, repositories, articles, and documentation.

Example:
- search for `hashcat`
- prefer official sources such as the project website, GitHub repository, wiki, or docs
- create a curated entry in `README.md`

Curated list format for `README.md`:
- keep each entry lean
- include only the heading, one short description, and source links
- include `Topics` only when they add signal
- do not add `Why it matters`
- do not add `Suggested metadata`
- keep `type` and `category` in YAML-only structured files under `data/resources/`, not in the curated Markdown list

Preferred source order:
1. official project site
2. official GitHub repository
3. official documentation or wiki
4. reputable secondary references

What to store:
- resource name
- short description
- main repository URL
- official site URL when available
- useful supporting URLs
- optional archive URL

Automation variant:
- run a scheduled job to query GitHub for candidate repositories
- add up to five new resources per run
- skip repositories already present in the curated list
- commit the changes automatically

### 2. Repository Markdown search

Search repository Markdown files, including `doc/*.md`, for useful tools, sections, or references.

Use this to enrich an existing entry or create a new one from local notes.

### 3. External Git repositories

External repositories are temporary inputs only.

Workflow:
1. clone the repository into a temporary directory
2. inspect README files and relevant docs
3. extract useful metadata and URLs
4. create or update a structured resource entry
5. remove the temporary clone when finished

Do not commit cloned repository contents into this repo.

### 4. Internet Archive

When possible:
- archive the source URL or repository URL
- store the returned archive reference in `archive_url`

Do not store archive downloads locally or in this repository.

## Suggested Categories

- `reconnaissance`
- `network-scanning`
- `web-security`
- `forensics`
- `malware-analysis`
- `osint`
- `threat-intelligence`
- `reverse-engineering`
- `cloud-security`
- `training`

## Suggested Types

- `tool`
- `repository`
- `article`
- `documentation`
- `course`
- `cheatsheet`
- `dataset`

## Entry Creation Checklist

1. Confirm the item is relevant to cybersecurity.
2. Search the internet and prefer official sources.
3. Write a short, factual description.
4. Set one primary `type`.
5. Set one primary `category`.
6. Add all relevant source URLs to `resources`.
7. Add provenance fields when extracted from docs or repositories.
8. Add `archive_url` when available.

## Example Commands

Search local Markdown files:

```sh
rg -n "nmap" . --glob "*.md"
```

Search only docs:

```sh
rg -n "nmap" doc --glob "*.md"
```

Internet-first example:

1. Search for `hashcat`
2. Verify the official GitHub repository and project site
3. Add an entry to `README.md`
4. Optionally create `data/resources/hashcat.md` if a structured standalone record is useful

## GitHub Action Usage

Primary output file:
- `README.md`

Automation files:
- `.github/workflows/discover-resources.yml`
- `scripts/discover_resources.py`
- `data/automation/state.json`

Behavior:
1. GitHub Actions runs every hour
2. the script searches GitHub for candidate cybersecurity repositories
3. it selects up to five repositories not already stored
4. it appends them under category headings in `README.md`
5. it updates the automation state file
6. the workflow commits and pushes the result

Adjustment points:
- edit `SEARCH_QUERIES` in `scripts/discover_resources.py` to change discovery scope
- edit `CATEGORY_KEYWORDS` to improve automatic categorization
- manually clean the curated list when needed because automatic search is heuristic-based

## Recommendation

Keep this workflow in `doc/ai-agent.md` rather than a platform-specific skill file for now.

Reason:
- it stays versioned inside the repo
- it is readable by humans and agents
- it can later be converted into a dedicated skill if the workflow becomes stable enough
