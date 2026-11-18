---
id: TASK-1
title: Download PAN-2012 into data/pan2012/
status: To Do
assignee: []
created_date: 2026-11-18 11:01
updated_date: '2026-11-18T11:13:00Z'
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
- [ ] #1 Files extracted under data/pan2012/ and git status shows nothing from data/ except data/README.md
- [ ] #2 tests/test_repo_hygiene.py still passes
- [ ] #3 Source URL, retrieval date and sha256 of each archive recorded in the data/README.md dataset table
- [ ] #4 Terms of use read and any redistribution limits noted in data/README.md
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 If code changed: ruff check and pytest pass
- [ ] #2 No data, derived artifacts, or raw chat text committed or displayed (hygiene test passes)
- [ ] #3 If output was produced (table, figure, page): rendered result inspected, not just executed
- [ ] #4 Steps to reproduce recorded (commands, seeds, pinned versions and model revisions)
- [ ] #5 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->
