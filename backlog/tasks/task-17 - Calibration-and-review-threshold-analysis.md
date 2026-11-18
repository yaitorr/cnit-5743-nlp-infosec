---
id: TASK-17
title: Calibration and review-threshold analysis
status: To Do
assignee: []
created_date: '2026-11-18 11:01'
labels:
  - experiment
milestone: m-2
dependencies:
  - TASK-11
  - TASK-13
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
