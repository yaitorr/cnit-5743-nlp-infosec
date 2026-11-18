---
id: TASK-13
title: Run d1 on PAN-2012
status: To Do
assignee: []
created_date: 2026-11-18 11:01
updated_date: '2026-11-18T11:13:00Z'
labels:
  - d1
  - experiment
milestone: m-1
dependencies:
  - TASK-9
  - TASK-10
  - TASK-12
type: task
ordinal: 13000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
First early-detection results for the typed-question decision model, on the same splits and thresholding protocol as Sentinel so the comparison is fair.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Per-question probabilities saved for every evaluated prefix (private results only)
- [ ] #2 Alert rule combining questions is defined and justified before looking at test results
- [ ] #3 Same split and threshold-setting protocol as Sentinel; aggregate results committed under results/
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 If code changed: ruff check and pytest pass
- [ ] #2 No data, derived artifacts, or raw chat text committed or displayed (hygiene test passes)
- [ ] #3 If output was produced (table, figure, page): rendered result inspected, not just executed
- [ ] #4 Steps to reproduce recorded (commands, seeds, pinned versions and model revisions)
- [ ] #5 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->
