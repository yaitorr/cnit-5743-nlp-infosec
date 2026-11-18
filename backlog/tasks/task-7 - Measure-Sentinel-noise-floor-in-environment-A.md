---
id: TASK-7
title: Measure Sentinel noise floor in environment A
status: To Do
assignee: []
created_date: '2026-11-18 11:01'
labels:
  - sentinel
  - boilerplate
milestone: m-0
dependencies:
  - TASK-5
documentation:
  - docs/spike-b-tolerances.md
type: task
ordinal: 7000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Spike B tolerances are defined as multiples of the numerical noise floor, so it must be measured first and recorded before any A-versus-B comparison.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A fixed set of synthetic or benign texts is committed or generated deterministically
- [ ] #2 The same index scores those texts at batch size 1 and 32; the maximum absolute score difference is recorded as noise_floor in docs/spike-b-tolerances.md
- [ ] #3 Result and date added to the decision log
<!-- AC:END -->
