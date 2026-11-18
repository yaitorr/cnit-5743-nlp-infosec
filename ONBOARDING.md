# Onboarding a new contributor

A runbook for an AI agent helping a new contributor get from a fresh machine to a claimed first task.
Humans can follow it too. Read `AGENTS.md` first; it holds the standing rules this runbook assumes.

## Ground rules for the agent

- **Propose, don't install.** Show each install or configuration command, say in one sentence what it does,
  and wait for the contributor's approval before running it. The doctor script never installs anything.
- **Ask how they like to work.** Contributors differ: some write code, some mainly analyze and write. Ask what
  they want from the collaboration and adapt. Do not assume a coding background.
- **Explain as you go.** The contributor should understand each tool and step well enough to repeat it alone.
- **Public repository.** Never commit or display data, derived artifacts, or raw chat text (see `AGENTS.md`).
- **Windows is untested.** The Windows commands below have not been run by anyone yet. If one fails, say so
  plainly and report it to the repo owner instead of improvising around it.

## Step 1: check the environment

Run the doctor from the repo root:

```bash
uv run --no-project scripts/doctor.py
```

If `uv` is not installed yet, install it first (see the table below) or run it with any Python 3.9+:
`python3 scripts/doctor.py` on macOS, `py scripts/doctor.py` on Windows.

Read the result:

- **FAIL** must be fixed before going on. Each one prints the fix command.
- **WARN** deserves a look (for example, working on `main` instead of a branch).
- **INFO** is a note, not a problem.

Fix, re-run until nothing FAILs, then run `uv run --no-project scripts/doctor.py --full`. The full check also
creates the project virtualenv (`uv sync`) and runs ruff, pytest, and a marimo launch check.

| Tool | Why it is needed | macOS | Windows (untested) |
|---|---|---|---|
| git | version control | `xcode-select --install` | `winget install --id Git.Git -e` |
| gh | GitHub login, clone, PRs | `brew install gh` | `winget install --id GitHub.cli -e` |
| uv | Python, environments, running the project | `brew install uv` | `winget install --id astral-sh.uv -e` |
| backlog | task tracking (needs at least the version in `AGENTS.md`) | `npm i -g backlog.md` or `brew install backlog-md` | `npm i -g backlog.md` (needs Node.js) |

Python 3.12 and marimo need no separate install: `uv` provides Python 3.12 and the `notebooks` dependency group
provides marimo. The detectors live in separate environments because their dependencies conflict. To set one up
on macOS: `UV_PROJECT_ENVIRONMENT=.venv-sentinel uv sync --extra sentinel` (use `d1` for the other). In Windows
PowerShell: `$env:UV_PROJECT_ENVIRONMENT = ".venv-sentinel"; uv sync --extra sentinel`.

## Step 2: get access and a checkout

1. The repo owner invites the contributor as a collaborator on GitHub. Only the owner can do this.
2. Log in: `gh auth login`.
3. Clone: `gh repo clone yaitorr/cnit-5743-nlp-infosec`, then work from that folder.
4. `main` is protected. Everything goes through a branch and a pull request.
5. Data stays local. Each contributor downloads their own copy of PAN-2012 into `data/pan2012/` following
   `data/README.md`, and never shares raw data through the repo, Teams, or SharePoint.

## Step 3: learn the project

Read, in this order:

1. `README.md`: the question, setup, and layout.
2. `AGENTS.md`: standing rules, including the collaboration workflow.
3. `docs/spike-b-tolerances.md`: an example of a decision recorded before the experiment.
4. `backlog instructions overview`, then `backlog task list --plain`: the work, grouped by milestone.

Then ask the contributor to say back, in their own words, what the project measures and why it has two detectors.

## Step 4: agree how you will work

Follow the collaboration workflow in `AGENTS.md`: claim a task in Backlog, work on a branch named
`<name>/task-N-slug`, open a pull request, and let the repo owner review and merge. Read
`backlog instructions task-execution` before starting a task and `backlog instructions task-finalization`
before finishing one. Every task carries the project Definition of Done.

## Step 5: pick a first task

Ask what the contributor wants to take on, then look at open tasks that fit their role and skills. For analysis
and policy roles, good candidates are tasks that need review, framing, or written analysis rather than code
(for example the d1 question set and the review-threshold analysis). If the work they have in mind has no task
yet, propose one using `backlog instructions task-creation`, and get the repo owner's approval before creating it.

## When something is wrong

- **The doctor reports a FAIL you cannot fix:** stop and tell the contributor exactly what failed and why.
- **A command behaves differently on this machine:** say so and report it to the owner. Fixes to this runbook
  and to `scripts/doctor.py` are welcome through a normal pull request.
