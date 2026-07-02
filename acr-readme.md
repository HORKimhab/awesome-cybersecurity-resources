# awesome-cybersecurity-resources
Awesome Cybersecurity Resources, [`more`](README.md).

## Purpose

This repository stores curated cybersecurity resources gathered from the internet, repository documentation, and selected local notes.

The canonical format is:
- one resource per Markdown file
- YAML frontmatter as the source of truth
- `resources` as an array of URL strings only

## Structure

- [`data/resources/`](data/resources/): structured resource entries
- [`data/templates/`](data/templates/): reusable frontmatter templates
- [`data/automation/`](data/automation/): automation state
- [`doc/`](doc/): agent and workflow documentation
- [`doc/ai-agent.md`](doc/ai-agent.md): agent workflow notes
- [`scripts/discover_resources.py`](scripts/discover_resources.py): local discovery automation
- [`.github/workflows/discover-resources.yml`](.github/workflows/discover-resources.yml): scheduled GitHub Actions job

## Workflow

1. Search the internet for a cybersecurity tool, project, article, or repository.
2. Prefer official sources such as the project website, GitHub repository, wiki, or documentation.
3. Convert the result into a structured resource entry.
4. Store the curated entry in `README.md` and, when needed, in `data/resources/`.
5. For external repositories, clone temporarily for analysis only.
6. Store only extracted metadata and URLs in this repo.
7. Archive the source URL or repository URL when possible.
8. Store archive metadata or links, not downloaded archive content.

## GitHub Automation

The repository includes an hourly GitHub Action at [`.github/workflows/discover-resources.yml`](.github/workflows/discover-resources.yml).

What it does:
- searches GitHub for five candidate cybersecurity repositories every hour
- skips repositories already recorded in `README.md`
- appends new curated entries
- stores deduplication state in `data/automation/state.json`
- commits the update automatically

Manual local run:

```sh
python3 scripts/discover_resources.py
```

Import missing entries from the ParrotSec package index in the simplified format:

```sh
python3 scripts/discover_resources.py --parrot-packages
```

Notes:
- the workflow uses the built-in `GITHUB_TOKEN`
- the workflow is scheduled hourly at minute `22` in UTC, not local time
- GitHub scheduled workflows run only from the repository default branch
- GitHub scheduled workflows may still be delayed occasionally under load
- repository search quality depends on GitHub metadata and the configured search queries

## License

This project is licensed under the MIT License. See `LICENSE`.

## Example Search

Search the internet for a keyword such as `hashcat`, gather the official URLs, then add a curated entry to `README.md`.

## TODO
- [ ] https://docs.google.com/document/d/12KLm2Pfypw1QPobGN6QUBgj8Yq7C3PY-Q6Z_WoxI-WQ/edit?usp=sharing
- [ ] Keep current logic and add trending related to cybersecurity 


## Donate

Support the maintenance of this project with PayPal or by scanning the QR code below.

<p align="center">
  <a href="https://www.paypal.com/donate/?hosted_button_id=GHBZLGLY76KNA">
    <img src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" alt="Donate with PayPal">
  </a>
</p>

<p align="center">
  <img src="data/images/qr-code-hkimhab-merchant-988.png" alt="Donation QR code" height="180">
</p>
