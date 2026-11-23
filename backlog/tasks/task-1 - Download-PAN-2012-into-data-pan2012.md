---
id: TASK-1
title: Download PAN-2012 into data/pan2012/
status: Done
assignee:
  - '@yaitorr'
created_date: 2026-11-18 11:01
updated_date: '2026-11-23T11:54:00Z'
labels:
  - data
  - boilerplate
milestone: m-0
dependencies: []
references:
  - https://zenodo.org/records/3713280
type: task
ordinal: 1000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Everything downstream needs the main dataset on disk. PAN-2012 is public but may include real minors' conversations, so it must stay out of git, Teams and SharePoint. PANC is still being sourced, so PAN-2012 unblocks the work in the meantime.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Files extracted under data/pan2012/ and git status shows nothing from data/ except data/README.md
- [x] #2 tests/test_repo_hygiene.py still passes
- [x] #3 Source URL, retrieval date and sha256 of each archive recorded in the data/README.md dataset table
- [x] #4 Terms of use read and any redistribution limits noted in data/README.md
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
1. Read Zenodo record metadata (file, size, md5, license) before downloading
2. Download archive into the main checkout's data/pan2012/ (shared across worktrees; data/ is git-ignored) and verify size + md5
3. Compute sha256 of outer and inner archives; extract; read corpus readmes for terms of use
4. Record provenance, checksums and terms in data/README.md; symlink data/pan2012 into worktrees (untracked)
5. Run ruff + pytest (hygiene test); confirm git status shows only data/README.md
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Downloaded 2026-11-23 to main checkout data/pan2012/, symlinked into worktree. md5 matched Zenodo; sha256 recorded in data/README.md. Zenodo license: none; readmes state no redistribution terms (assumed none). PAN-2012 overview paper not consulted for terms. Repro: curl the Zenodo files URL in data/README.md, unzip outer then inner zips.

Owner reviewed the PAN-2012 overview paper: no license stated there either. Documented in data/README.md that no license exists; assume no redistribution rights.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Downloaded PAN-2012 (Zenodo 10.5281/zenodo.3713280) into the shared main-checkout data/pan2012/ and symlinked it into worktrees (untracked). Verified size and md5 against Zenodo, recorded sha256 of the outer and both inner archives, URL and retrieval date in data/README.md. Terms: no license on Zenodo, in the corpus readmes, or in the overview paper; documented as no redistribution rights assumed. Verification: ruff clean, 18 pytest passed incl. hygiene test, git status shows only data/README.md. Follow-up: TASK-2 (inspect structure).
<!-- SECTION:FINAL_SUMMARY:END -->
