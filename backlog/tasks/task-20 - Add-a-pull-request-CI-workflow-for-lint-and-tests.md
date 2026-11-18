---
id: TASK-20
title: Add a pull-request CI workflow for lint and tests
status: In Progress
assignee:
  - '@yaitorr'
created_date: '2026-11-18T11:47:00Z'
updated_date: '2026-11-18T11:50:00Z'
labels:
  - ci
  - boilerplate
milestone: m-0
dependencies: []
documentation:
  - .github/workflows/pages.yml
type: chore
ordinal: 20000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Our Definition of Done says ruff and pytest must pass when code changes, but today only a person running them enforces that. main is protected, yet no status checks exist, so a PR shows no objective evidence either way. With a second contributor opening PRs, automatic checks give the owner proof when reviewing and give the app's auto-fix something to watch. The existing Pages workflow only runs on pushes to main, so nothing runs on pull requests.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A workflow runs ruff check, ruff format --check, and pytest on every pull request into main
- [x] #2 All actions are pinned to full commit SHAs and uv is pinned to an exact version, matching pages.yml
- [x] #3 Workflow permissions are read-only (contents: read)
- [ ] #4 CI needs no dataset: the checks pass on a clean checkout, including the data hygiene test
- [x] #5 Only the shared base and dev dependencies are installed, not the Sentinel or d1 extras; what this leaves uncovered is documented
- [ ] #6 A deliberately failing change on a throwaway branch is shown to fail the check, then discarded
- [ ] #7 A decision is recorded on adding a Windows runner (it would exercise the doctor unit tests and hygiene test on Windows, where the onboarding path is untested)
- [ ] #8 A decision is recorded on making the check required in branch protection; no settings change without the owner's explicit approval
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 If code changed: ruff check and pytest pass
- [ ] #2 No data, derived artifacts, or raw chat text committed or displayed (hygiene test passes)
- [ ] #3 If output was produced (table, figure, page): rendered result inspected, not just executed
- [ ] #4 Steps to reproduce recorded (commands, seeds, pinned versions and model revisions)
- [ ] #5 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Add .github/workflows/ci.yml: on pull_request into main; read-only permissions; ubuntu and windows matrix (recommended, owner to confirm); astral-sh/setup-uv pinned by SHA with an exact uv version; uv sync --locked (base + dev only); ruff check, ruff format --check, pytest
2. Document in README what CI runs and what it leaves uncovered (Sentinel and d1 extras, model loads, anything needing data)
3. Validate: YAML parses, every action SHA-pinned, and the same commands pass on a fresh local clone
4. Commit locally; ask before pushing
5. After the PR runs: prove the check fails on a throwaway branch, record the Windows and required-check decisions, finalize with the owner
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Implemented .github/workflows/ci.yml: pull_request into main, contents: read, matrix ubuntu-latest + windows-latest (fail-fast off), astral-sh/setup-uv v10.3.3 pinned by SHA with uv 0.11.26, uv sync --locked then ruff check, ruff format --check, pytest. Input names verified against action.yml at the pinned commit. Locally verified: YAML structure and pins; the exact commands pass on a fresh clone with no data (18 tests). Not yet proven: the workflow actually running on GitHub (AC 1, 4).
Tentative decisions for the owner to confirm: (AC 7) include the Windows runner; it exercises the doctor unit tests and hygiene test on Windows, partly covering the untested onboarding path, at the cost of slower runs. (AC 8) require both check (ubuntu-latest) and check (windows-latest) in branch protection only after CI has run green on a few PRs; changing that setting needs the owner explicit approval.
<!-- SECTION:NOTES:END -->
