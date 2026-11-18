---
id: TASK-19
title: 'Onboard David: doctor script, runbook, and branch protection'
status: Done
assignee:
  - '@yaitorr'
created_date: '2026-11-18T11:25:00Z'
updated_date: '2026-11-18T11:41:00Z'
labels:
  - onboarding
  - boilerplate
milestone: m-0
dependencies: []
type: task
ordinal: 19000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
David (policy and threat lead) needs to run and contribute to the project from his own machine, with his own agent, without the repo owner walking him through setup. A read-only environment check plus an agent-readable runbook gives any agent one path from a fresh machine to a claimed first task, and collaboration rules plus a protected main keep two people from breaking the public repo or the data rules.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 scripts/doctor.py reports PASS/WARN/FAIL for git, gh and its login, uv, backlog (at least the version named in the AGENTS.md instruction block), Python 3.12 availability, and repo state, with fix hints for macOS and Windows; it never installs anything
- [x] #2 doctor --full additionally runs uv sync, ruff and pytest and confirms marimo starts
- [x] #3 Version-comparison logic has unit tests
- [x] #4 ONBOARDING.md takes an agent from a fresh machine to a claimed first task, with macOS and Windows commands; Windows steps are marked untested until David runs them
- [x] #5 AGENTS.md documents the collaboration workflow: one branch per task named <name>/task-N-slug, PR into main, tasks claimed by assignee, no direct pushes to main
- [x] #6 main is protected on GitHub: pull request required with one approval from the code owner, owner can bypass, no force pushes or deletions
- [x] #7 An optional /onboard command points Claude Code at ONBOARDING.md
- [x] #8 The Backlog instruction block is refreshed to the current CLI version
- [x] #9 CODEOWNERS names the repo owner and GitHub reports no errors for it once it is on main
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
1. Refresh the Backlog instruction block via the CLI
2. Write scripts/doctor.py (stdlib only, one implementation for macOS and Windows) with unit tests for version comparison
3. Write ONBOARDING.md and the optional /onboard command
4. Add the collaboration workflow and onboarding pointer to AGENTS.md
5. Run doctor, ruff, and pytest on this machine
6. Protect main (PR required, 0 approvals, admin bypass, no force push or deletion)
7. Commit locally in cohesive commits; ask before pushing
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Doctor: single stdlib-only scripts/doctor.py (one implementation for macOS and Windows) instead of bash plus PowerShell; it runs on system Python 3.9 on a stripped PATH and prints per-tool fix commands. Verified on macOS only: default run, --full (uv sync, ruff, pytest, marimo 0.25.2), a simulated bare machine, and a simulated outdated backlog. Windows commands are untested.
Tests: 18 pass (version comparison is numeric, covering the 1.9 vs 1.52 case).
Branch protection applied to main: PR required, 0 approvals, admins not bound (owner can bypass), no force pushes or deletions. Read back via the API. Stronger option not taken: require 1 approval plus a CODEOWNERS file so only the owner can approve contributor PRs.
Open: AC 8 (refresh Backlog block via backlog agents --update-instructions, interactive; select AGENTS.md only so the block is not duplicated in CLAUDE.md). A collaborator invite needs the contributor GitHub username.

Update: switched branch protection from 0 to 1 required approval with code owner review required (read back via API), and added .github/CODEOWNERS naming the repo owner, so only the owner approval counts. The owner can still bypass for own PRs (admins not bound). CODEOWNERS is read from the base branch, so its validity can only be checked after it is merged to main (AC 9).

Close-out: PR #1 merged. GitHub reports 0 CODEOWNERS errors for main (criterion 9). The repo owner confirmed in chat that they understand the work and are comfortable with it (Definition of Done item 5).
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Onboarding for a second contributor is in place and merged (PR #1). Added scripts/doctor.py (read-only, standard-library-only environment check for macOS and Windows, with a --full mode), ONBOARDING.md and an optional /onboard command, the collaboration workflow in AGENTS.md, a refreshed Backlog instruction block (1.55.3, which sets the doctor minimum CLI version), and CODEOWNERS. main is protected: pull request required, one code-owner approval, no force pushes or deletions, owner can bypass.

Verification: ruff and pytest pass (18 tests); doctor --full is green on macOS; a simulated bare machine and a simulated outdated CLI behave correctly; GitHub reports 0 CODEOWNERS errors on main; the PR showed REVIEW_REQUIRED, confirming the protection is enforced. The repo owner confirmed in chat that they understand the work and are comfortable with it.

Risks and follow-ups: Windows commands are untested until the contributor runs the doctor. The collaborator invite still needs the contributor GitHub username. The repo has no PR checks, so the lint and test Definition of Done item is not enforced automatically; a pull-request CI workflow is a possible follow-up (not created). Contributors now need Backlog CLI 1.55.3 or newer.
<!-- SECTION:FINAL_SUMMARY:END -->
