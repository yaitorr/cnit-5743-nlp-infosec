---
id: TASK-4
title: Select and pin the sentence-embedding model for Sentinel
status: To Do
assignee: []
created_date: 2026-11-18 11:01
updated_date: '2026-11-18T11:13:00Z'
labels:
  - sentinel
  - boilerplate
milestone: m-0
dependencies: []
references:
  - https://github.com/Roblox/Sentinel
type: task
ordinal: 4000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Sentinel needs a named sentence-transformers encoder, and every score, the noise floor and the privacy test depend on that choice. The embedding-inversion test in M3 can only run if an inversion model exists for the chosen encoder, so check availability before choosing.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Encoder name and exact model revision recorded in the README pinned-artifacts table
- [ ] #2 Rationale recorded, including compatibility with the planned embedding-inversion test
- [ ] #3 Model loads offline after the first download
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 If code changed: ruff check and pytest pass
- [ ] #2 No data, derived artifacts, or raw chat text committed or displayed (hygiene test passes)
- [ ] #3 If output was produced (table, figure, page): rendered result inspected, not just executed
- [ ] #4 Steps to reproduce recorded (commands, seeds, pinned versions and model revisions)
- [ ] #5 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->
