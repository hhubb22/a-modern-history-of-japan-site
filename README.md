# A Modern History of Japan Web Edition

This project turns the book manuscript into a static reading site built with MkDocs and Material for MkDocs.

## What is included

- A bilingual site structure with `中文` and `English` sections
- A sync script that copies the source Markdown and images into `docs/`
- A readable documentation theme tuned for long-form text
- A GitHub Pages workflow for automated deployment

## Source repository

By default, the sync script reads from:

```text
~/Documents/a-modern-history-of-japan
```

If your source lives elsewhere, pass `--source /path/to/repo`.

## Local setup

```bash
uv sync
make serve
```

Then open the local URL printed by MkDocs, usually `http://127.0.0.1:8000`.

## Common commands

```bash
make sync   # refresh docs/ from the source manuscript
make serve  # sync and start a local preview server
make build  # sync and build the static site into site/
```

You can also run the commands directly:

```bash
uv run python scripts/sync_content.py
uv run mkdocs serve
uv run mkdocs build
```

## GitHub Pages

The workflow at `.github/workflows/deploy.yml` builds the site and deploys it to GitHub Pages.

The deployment workflow builds from the committed `docs/` content in this repository. The sync script is for local content refresh before you commit changes.

To enable it:

1. Push this repository to GitHub.
2. In repository settings, enable `Pages` and choose `GitHub Actions` as the source.
3. Push to `main`.

## Content layout

```text
docs/
  index.md
  en/
  zh/
  images/
```

The sync step copies:

- English source chapters from the repository root into `docs/en/`
- Chinese chapters from `zh/` into `docs/zh/`
- Image assets from `images/` into `docs/images/`

English chapter image paths are rewritten from `images/...` to `../images/...` so they work from `docs/en/`.
