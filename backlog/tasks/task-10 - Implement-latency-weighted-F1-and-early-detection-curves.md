---
id: TASK-10
title: Implement latency-weighted F1 and early-detection curves
status: To Do
assignee: []
created_date: '2026-11-18 11:01'
labels:
  - metrics
milestone: m-1
dependencies:
  - TASK-3
references:
  - 'https://doi.org/10.18653/v1/2021.acl-long.386'
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
