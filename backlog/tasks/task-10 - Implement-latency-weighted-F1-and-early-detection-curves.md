---
id: TASK-10
title: Implement latency-weighted F1 and early-detection curves
status: To Do
assignee: []
created_date: 2026-11-18 11:01
updated_date: '2026-11-24T12:16:00Z'
labels:
  - metrics
  - track-tech
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

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Policy input: TASK-22 recommends what counts as early (how many messages in). Read it when designing the latency weighting. This is a recommendation, not a dependency; TASK-10 does not wait on it.

Input from TASK-2 (see docs/pan2012-structure.md). Position unit is non-empty messages. Open: how to set the latency penalty parameter p without message-level risk labels (Vogt et al. 2021 set p so the penalty is 0.5 at about 20 grooming messages using ChatCoder2 labels, which we lack; the median-length alternative is discussed there). Median conversation is 4 non-empty messages (positives: median 5, mean 33.5), so earliness here is within short segments, not whole chats; state this as a limitation. Spike B gate 3 is zero flipped decisions, which the metric's median-based speed term makes hard to bound otherwise.
<!-- SECTION:NOTES:END -->
