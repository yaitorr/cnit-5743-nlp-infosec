---
id: TASK-20
title: Add a pull-request CI workflow for lint and tests
status: Done
assignee:
  - '@yaitorr'
created_date: '2026-11-18T11:47:00Z'
updated_date: '2026-11-18T11:59:00Z'
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
- [x] #1 A workflow runs ruff check, ruff format --check, and pytest on every pull request into main
- [x] #2 All actions are pinned to full commit SHAs and uv is pinned to an exact version, matching pages.yml
- [x] #3 Workflow permissions are read-only (contents: read)
- [x] #4 CI needs no dataset: the checks pass on a clean checkout, including the data hygiene test
- [x] #5 Only the shared base and dev dependencies are installed, not the Sentinel or d1 extras; what this leaves uncovered is documented
- [x] #6 A deliberately failing change on a throwaway branch is shown to fail the check, then discarded
- [x] #7 A decision is recorded on adding a Windows runner (it would exercise the doctor unit tests and hygiene test on Windows, where the onboarding path is untested)
- [x] #8 A decision is recorded on making the check required in branch protection; no settings change without the owner's explicit approval
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 If code changed: ruff check and pytest pass
- [x] #2 No data, derived artifacts, or raw chat text committed or displayed (hygiene test passes)
- [x] #3 If output was produced (table, figure, page): rendered result inspected, not just executed
- [x] #4 Steps to reproduce recorded (commands, seeds, pinned versions and model revisions)
- [x] #5 Decisions and reasoning written down, and the owner can explain them without help
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

Owner decisions (2026-11-18): (AC 7) Linux only for now. The Windows leg was dropped to keep CI simple; the Windows onboarding path stays untested and the README says so. A matrix can be added later. (AC 8) Do not require the check yet: revisit after CI has run green on a few PRs, then require the single check named "check" in branch protection, with the owner explicit approval at that time. No settings changed.

Evidence: green run https://github.com/yaitorr/cnit-5743-nlp-infosec/actions/runs/44298795648 (pull_request event on the PR branch, all steps passed on ubuntu-latest: checkout, setup-uv, uv sync --locked, lint, format check, tests including the data hygiene test). Failing run https://github.com/yaitorr/cnit-5743-nlp-infosec/actions/runs/44299400951 (throwaway draft PR #4 with one unused import): Lint failed, Format check and Tests skipped, as intended. PR #4 was closed unmerged and its branch deleted; main never contained the demo file. The repo owner confirmed in chat that the demo worked and that the work looks good and reasonable (Definition of Done item 5). DoD item 3 had no table, figure, or page to inspect; the step-level results of both runs were read instead.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Added a pull-request CI workflow (.github/workflows/ci.yml, merged in PR #3). Every PR into main runs one Linux job, check: uv sync --locked, ruff check, ruff format --check, pytest. Permissions are read-only, both actions are pinned to full commit SHAs, uv is pinned to 0.11.26, and only the shared and dev dependencies are installed. The README Checks section gives the local equivalent command and lists what CI does not cover (Windows, the Sentinel and d1 environments, anything needing data, model behavior, the doctor real tool checks, the site export).

Verification: a green run on the PR itself passed every step on a clean checkout with no data, including the hygiene test; a deliberately broken change on a throwaway draft PR failed at the Lint step with later steps skipped, then was closed and its branch deleted. The repo owner confirmed the demo worked and the work looks good and reasonable.

Decisions: Linux only for now (a Windows matrix leg can be added later); the check is not yet required in branch protection. Once it has run green on a few PRs, require the single check named check, with the owner explicit approval at that time. No repository settings were changed.

Follow-ups (not created as tasks): requiring the check in branch protection after a few green PRs; optional Windows coverage; a CI path for the detector environments if that ever becomes worthwhile.
<!-- SECTION:FINAL_SUMMARY:END -->
