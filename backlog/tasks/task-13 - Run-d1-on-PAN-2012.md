---
id: TASK-13
title: Run d1 on PAN-2012
status: To Do
assignee: []
created_date: '2026-11-18 11:01'
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
