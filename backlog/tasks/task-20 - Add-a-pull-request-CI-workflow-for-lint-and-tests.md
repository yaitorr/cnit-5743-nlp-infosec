---
id: TASK-20
title: Add a pull-request CI workflow for lint and tests
status: To Do
assignee: []
created_date: '2026-11-18T11:47:00Z'
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
- [ ] #2 All actions are pinned to full commit SHAs and uv is pinned to an exact version, matching pages.yml
- [ ] #3 Workflow permissions are read-only (contents: read)
- [ ] #4 CI needs no dataset: the checks pass on a clean checkout, including the data hygiene test
- [ ] #5 Only the shared base and dev dependencies are installed, not the Sentinel or d1 extras; what this leaves uncovered is documented
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
