# Agent instructions

Rules for AI coding agents working in this repository. Humans: these are also the project's working
rules.

New to this repository? Follow `ONBOARDING.md` (Claude Code: `/onboard`).

## Data handling (the repo is public)

- Never commit anything under `data/` or `artifacts/`, raw chats, Sentinel indexes, or embeddings.
- Never print raw chat text in a notebook, test output, or log that could be committed or published.
- Commit aggregate results only. Per-conversation outputs go in `results/private/` (git-ignored).
- Ask before pushing to GitHub or changing repository settings.

## Notebooks and the published results site

Notebooks (marimo, in `notebooks/`) are exported to a public static site, so they are written for a
reader, not for the author.

- **Hide code by default.** The site is exported with `--no-include-code`, so no cell source
  appears. To show code, wrap the cell's output in `mo.show_code(...)`, and only when it strengthens
  a point or gives the reader information they need (e.g. how a metric is defined, or a non-obvious
  method choice). Readers can consult the source for everything else.
- Notebooks read only committed files in `results/`, never `data/` or `artifacts/`, so the site
  builds without datasets.
- Look at the rendered page, not only whether the export succeeded.

## Environments

- Sentinel and d1 need incompatible dependency versions, so they are separate uv extras (`sentinel`,
  `d1`) with separate virtualenvs. Do not merge them into one environment without the equivalence
  check described in the project notes.
- Third-party code is pinned to exact versions/commits (see the README). d1 runs its own code on
  load.

## Division of work

Agents scaffold plumbing, tooling, and checks. The core logic (dataset loaders, metrics, and the
evaluation harness) is designed and written by the project authors; agents explain options and
review rather than author it unprompted.

## Collaboration workflow

- **One branch per task**, named `<name>/task-N-slug` (for example `yai/task-3-loader-interface`).
  `main` is protected: never push to it directly.
- **Claim the task first** in Backlog:
  `backlog task edit TASK-N -s "In Progress" -a @<github-username>`. One assignee per task. Read
  `backlog instructions task-execution` before starting.
- **Open a pull request into `main`.** Link the task and say how each Definition of Done item was
  met. The repo owner reviews and merges. Backlog changes (status, notes, final summary) travel in
  the same branch.
- **Keep commits focused**, with messages that explain why, not only what.
- **Each contributor keeps their own local copy of the data.** Never share it through the repo,
  Teams, or SharePoint.
- **Ask the repo owner** before changing repository settings, other people's tasks, or this file's
  rules.

## Conventions

- Python 3.12, `uv` for everything, `ruff` for lint/format, `pytest` for tests.
- Deliverable exports go in `dist/` named `YYYY-MM-DD_ytorresv_CNIT-57400_<work>.<ext>`.

<!-- rumdl-disable MD013 -->
<!-- BACKLOG.MD GUIDELINES START -->
<!-- backlog.md-instructions-version: 1.55.3 -->
<CRITICAL_INSTRUCTION>

## Backlog.md Workflow

This project uses Backlog.md for task and project management.

**At the beginning of each conversation in this project, run `backlog instructions overview` before answering or taking action. Re-read it only if you have not read it yet in the current conversation.**

Use the overview to decide whether to search, read, create, or update Backlog tasks.

Before task lifecycle actions, read the matching detailed guide:
- `backlog instructions task-creation` before creating or splitting tasks
- `backlog instructions task-execution` before planning, changing status or assignee, adding a plan or implementation notes, or implementing task work
- `backlog instructions task-finalization` before checking acceptance criteria, writing final summaries, or moving tasks to terminal statuses

Use `backlog <command> --help` before running unfamiliar commands. Help shows options, fields, and examples.

Do not edit Backlog task, draft, document, decision, or milestone markdown files directly. Use the `backlog` CLI so metadata, relationships, and history stay consistent.

</CRITICAL_INSTRUCTION>
<!-- BACKLOG.MD GUIDELINES END -->
<!-- rumdl-enable MD013 -->
