# Agent instructions

Rules for AI coding agents working in this repository. Humans: these are also the project's working rules.

## Data handling (the repo is public)

- Never commit anything under `data/` or `artifacts/`, raw chats, Sentinel indexes, or embeddings.
- Never print raw chat text in a notebook, test output, or log that could be committed or published.
- Commit aggregate results only. Per-conversation outputs go in `results/private/` (git-ignored).
- Ask before pushing to GitHub or changing repository settings.

## Notebooks and the published results site

Notebooks (marimo, in `notebooks/`) are exported to a public static site, so they are written for a reader,
not for the author.

- **Hide code by default.** The site is exported with `--no-include-code`, so no cell source appears.
  To show code, wrap the cell's output in `mo.show_code(...)`, and only when it strengthens a point or
  gives the reader information they need (e.g. how a metric is defined, or a non-obvious method choice).
  Readers can consult the source for everything else.
- Notebooks read only committed files in `results/`, never `data/` or `artifacts/`, so the site builds without datasets.
- Look at the rendered page, not only whether the export succeeded.

## Environments

- Sentinel and d1 need incompatible dependency versions, so they are separate uv extras (`sentinel`, `d1`)
  with separate virtualenvs. Do not merge them into one environment without the equivalence check described
  in the project notes.
- Third-party code is pinned to exact versions/commits (see the README). d1 runs its own code on load.

## Division of work

Agents scaffold plumbing, tooling, and checks. The core logic (dataset loaders, metrics, and the evaluation
harness) is designed and written by the project authors; agents explain options and review rather than
author it unprompted.

## Conventions

- Python 3.12, `uv` for everything, `ruff` for lint/format, `pytest` for tests.
- Deliverable exports go in `dist/` named `YYYY-MM-DD_ytorresv_CNIT-57400_<work>.<ext>`.
