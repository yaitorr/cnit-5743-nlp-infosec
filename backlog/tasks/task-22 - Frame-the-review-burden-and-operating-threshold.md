---
id: TASK-22
title: Frame the review burden and operating threshold
status: To Do
assignee: []
created_date: '2026-11-24T10:36:00Z'
updated_date: '2026-11-25T00:02:00Z'
labels:
  - track-policy
  - pickup-ready
milestone: m-1
dependencies: []
type: task
ordinal: 22000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Several tasks need a threshold or a notion of early detection that technical results alone cannot set: false-positive rates are reported at an operating threshold (TASK-15), calibration needs thresholds worth testing (TASK-17), and the early-detection metric weights latency (TASK-10). The policy lead says what a platform could plausibly accept.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Plausible review capacity stated as a range (reviews per N conversations), with assumptions and sources
- [ ] #2 Relative cost of a missed positive versus an unnecessary review described, with the reasoning
- [ ] #3 Recommendation for what counts as early (how many messages in is early enough), stated as a message count m (non-empty messages) so it can set the latency penalty in TASK-10 via p = ln(3)/(m-1)
- [ ] #4 Candidate operating thresholds proposed for TASK-15 and TASK-17 to evaluate, including candidate false-positive rates (for example 1% and 5%) for the TASK-10 detection-rate curve
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->
