---
id: TASK-17
title: Calibration and review-threshold analysis
status: To Do
assignee: []
created_date: 2026-11-18 11:01
updated_date: '2026-11-24T10:38:00Z'
labels:
  - experiment
  - track-both
milestone: m-2
dependencies:
  - TASK-11
  - TASK-13
  - TASK-22
type: task
ordinal: 17000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Calibration results tell a platform what a review threshold costs: how many conversations humans must review and how many positives slip through. This is the bridge between the technical results and the policy analysis.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Calibration measured for d1 probabilities and, where meaningful, Sentinel scores
- [ ] #2 For several thresholds: reviews per N conversations and missed positives, with caveats about PAN-2012 class balance
- [ ] #3 Presented in a form the policy lead can use directly
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 If code changed: ruff check and pytest pass
- [ ] #2 No data, derived artifacts, or raw chat text committed or displayed (hygiene test passes)
- [ ] #3 If output was produced (table, figure, page): rendered result inspected, not just executed
- [ ] #4 Steps to reproduce recorded (commands, seeds, pinned versions and model revisions)
- [ ] #5 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->
