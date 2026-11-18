---
id: TASK-18
title: Evaluate the Sentinel-to-d1 cascade
status: To Do
assignee: []
created_date: '2026-11-18 11:01'
labels:
  - experiment
  - cascade
milestone: m-3
dependencies:
  - TASK-11
  - TASK-13
type: task
ordinal: 18000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Sentinel screens everything and d1 takes a closer look at what Sentinel flags. The two detectors live in separate environments, so the cascade runs in two stages that hand off through files in artifacts/.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Stage 1 writes flagged conversation ids and prefixes to artifacts/; stage 2 reads them in the d1 environment
- [ ] #2 Early-detection and false-positive results compared with each detector alone, using the same metrics and splits
- [ ] #3 A prediction of the cascade's effect on recall and false positives is written before running and compared with the outcome
<!-- AC:END -->
