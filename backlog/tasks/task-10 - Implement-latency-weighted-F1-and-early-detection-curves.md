---
id: TASK-10
title: Implement latency-weighted F1 and early-detection curves
status: To Do
assignee: []
created_date: 2026-11-18 11:01
updated_date: '2026-11-18T11:13:00Z'
labels:
  - metrics
milestone: m-1
dependencies:
  - TASK-3
references:
  - https://doi.org/10.18653/v1/2021.acl-long.386
type: feature
ordinal: 10000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Latency-weighted F1 (Vogt et al., 2021) is the main metric because it discounts correct flags that arrive late; plain F1 would hide how early detection happens.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Latency-weighted F1 implemented and tested against a hand-computed example
- [ ] #2 Detection-rate-versus-messages-seen curve at a fixed low false-positive rate
- [ ] #3 Metrics take scores and labels only, with no dataset dependency
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 If code changed: ruff check and pytest pass
- [ ] #2 No data, derived artifacts, or raw chat text committed or displayed (hygiene test passes)
- [ ] #3 If output was produced (table, figure, page): rendered result inspected, not just executed
- [ ] #4 Steps to reproduce recorded (commands, seeds, pinned versions and model revisions)
- [ ] #5 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->
