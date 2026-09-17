---
name: cybersecurity-resource-curator
description: Curate cybersecurity resources in this repository's README.md. Use automatically when a request asks to add, update, remove, import, discover, categorize, move, or reorganize a security tool, project, repository, article, guide, course, dataset, or URL.
---

# Cybersecurity Resource Curator

Keep the public resource index accurate, concise, and easy to browse.

## Repository source of truth

- `README.md` is the only resource catalog and source of truth.
- Add, update, move, and remove resource entries only in `README.md`.
- Do not create per-resource Markdown files or YAML metadata records elsewhere in the repository.
- `data/automation/state.json` belongs to automated discovery. Do not modify it during a manual resource addition.

## Add or update resources

When the user asks to add one or more URLs, including shorthand such as `add url github1, github2, ...`:

- research, deduplicate, categorize, and add every accepted resource to `README.md`
- place each resource independently in its best section; URLs from one prompt do not need to share a section
- do not update `data/automation/state.json`
- provide a short suggestions summary after the edit covering the selected sections, skipped duplicates, and any useful missing official site or documentation links

## Remove resources

- Remove a resource only when the user explicitly asks to remove it.
- Match by canonical URL or resource name, then remove the complete `### Resource Name` block from `README.md`.
- If the same resource appears more than once, remove only the clearly matched entry unless the user asks to remove every occurrence.
- Remove an empty resource category after its last entry is deleted, but never remove `## Donate`.
- Do not update `data/automation/state.json` during a manual removal.
- Warn that automated discovery may add a removed resource again. If the user requests permanent exclusion, explain that a denylist needs to be implemented; do not silently create one.
- Report the resource, section, and URL removed.

## Research and acceptance

1. Confirm that the resource has a meaningful cybersecurity, security-engineering, privacy, or defensive-research use.
2. Search the current repository for duplicate titles and canonical URLs before editing. Treat URL variants such as a trailing slash or `.git` suffix as the same resource.
3. Verify current facts with authoritative sources. Prefer, in order:
   1. official project or organization site
   2. official source repository
   3. official documentation or wiki
   4. primary research publication
   5. reputable secondary source
4. If the prompt supplies only a URL, inspect it and derive a factual description. Do not create a link-only entry when an authoritative description is available.
5. Do not invent missing metadata. Omit optional README links and leave optional structured fields empty when they cannot be verified.

## Choose the README location

Place entries by their primary purpose, not by incidental keywords in a name or description.

1. Read all existing `##` headings in `README.md` before choosing a section.
2. Reuse the narrowest existing section that accurately represents the resource.
3. For a resource with several capabilities, choose the category for its main security use. Mention secondary capabilities in the description or tags instead of duplicating the entry.
4. Add a new `##` section only when no existing section fits and the subject is a durable category, an explicitly requested collection, or a group with multiple entries. Place a new section beside the most closely related sections rather than automatically at the end of the file.
5. Within a section, insert the entry after the most closely related resource when that relationship is clear. Otherwise insert it at the end of that section, immediately before the next `##` heading.
6. Never place a new resource under `## Donate`.

Use these established mappings when they fit:

- password auditing, wordlists, or hash recovery -> `Password Cracking`
- rogue access points or Wi-Fi impersonation -> `Evil Twin Attack`
- Bluetooth and BLE tooling -> `Bluetooth Security and Analysis`
- vulnerable iOS apps or iOS learning labs -> `iOS Security Training and Practice`
- reconnaissance, asset discovery, or subdomain discovery -> `Attack Surface Discovery`
- network, port, or vulnerability scanners -> `Scanning`
- investigation and public-data gathering -> `Open Source Intelligence`
- secure agents, AI red teaming, guardrails, or agent observability -> `AI Agent Security and Tooling`
- web application testing -> `Web Security`
- digital evidence and incident investigation -> `Forensics`
- binary analysis and decompilation -> `Reverse Engineering`
- vulnerability research and exploit-development research -> `Vulnerability Research`
- malicious-code analysis and sandboxes -> `Malware Analysis`
- cloud posture and cloud platform security -> `Cloud Security`
- privacy-preserving or anonymity tooling -> `Privacy and Anonymity`
- cross-domain resources with no more precise home -> `General Security`

These mappings are defaults, not a reason to ignore a better existing section.

## Write the README entry

Use this shape and preserve the surrounding section's conventions:

```markdown
### Resource Name

One short, factual description of what the resource is and its primary security use.

- GitHub: https://github.com/owner/repository
- Official site: https://example.org/
- Documentation: https://docs.example.org/
- Topics: topic-one, topic-two
```

Rules:

- Keep the description concrete and normally to one sentence.
- Prefer what the project does over marketing claims or personal opinions.
- Include only verified, useful links; do not repeat the same destination under different labels.
- Include `Topics` only when they materially improve discovery.
- Do not add `Why it matters`, `Suggested metadata`, placeholder text, popularity claims, or star counts.
- Match the capitalization used by the official project.

## External repository inputs

When an external repository must be inspected in depth, clone it only into a temporary directory, extract the needed metadata, and do not copy or commit the clone into this repository.

## Validate the change

Before finishing:

1. For additions and updates, confirm the title and canonical URLs are not duplicated elsewhere in `README.md`.
2. Confirm each added or moved entry sits inside the intended `##` section and before the next section boundary.
3. For removals, confirm the targeted entry is gone and unrelated entries remain intact.
4. Review `git diff --check` and the focused diff.
5. Report the chosen README section for each addition or move and every resource removed.
6. For URL additions, include concise suggestions in the final response without turning those suggestions into unrequested repository changes.

For automated bulk discovery behavior, inspect `scripts/discover_resources.py` and `.github/workflows/discover-resources.yml`; do not assume the manual workflow updates automation state.
