# awesome-cybersecurity-resources
Awesome Cybersecurity Resources, [`more`](README.md).

## Purpose

This repository stores curated cybersecurity resources gathered from the internet, repository documentation, and selected local notes.

`README.md` is the resource catalog and source of truth. Each entry contains a heading, a concise factual description, and verified source links.

## Structure

- [`data/automation/`](data/automation/): automation state
- [`.agents/skills/cybersecurity-resource-curator/`](.agents/skills/cybersecurity-resource-curator/): automatically loaded resource-curation workflow
- [`scripts/discover_resources.py`](scripts/discover_resources.py): local discovery automation
- [`.github/workflows/discover-resources.yml`](.github/workflows/discover-resources.yml): scheduled GitHub Actions job

## Workflow

1. Search the internet for a cybersecurity tool, project, article, or repository.
2. Prefer official sources such as the project website, GitHub repository, wiki, or documentation.
3. Write a concise resource entry in the most appropriate `README.md` section.
4. For external repositories, clone temporarily for analysis only.
5. Store only the curated description and verified links in this repo.

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
