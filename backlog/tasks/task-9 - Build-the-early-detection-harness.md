---
id: TASK-9
title: Build the early-detection harness
status: To Do
assignee: []
created_date: 2026-11-18 11:01
updated_date: '2026-11-24T10:38:00Z'
labels:
  - harness
  - metrics
  - track-tech
milestone: m-1
dependencies:
  - TASK-3
type: feature
ordinal: 9000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The core question is how many messages into a conversation each detector first flags it. Sentinel scores a window of messages (its default aggregator returns 0.0 below 10 messages) while d1 reads the whole prefix, so the harness needs one detector interface evaluated at each prefix length.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 For each conversation, returns the first message index where the score crosses a threshold, or none
- [ ] #2 One detector interface is used by both the Sentinel and d1 wrappers
- [ ] #3 Sentinel's aggregator is configurable; the default skewness and top_k_mean (k=3) are both runnable
- [ ] #4 Tested on synthetic conversations with known flag points
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 If code changed: ruff check and pytest pass
- [ ] #2 No data, derived artifacts, or raw chat text committed or displayed (hygiene test passes)
- [ ] #3 If output was produced (table, figure, page): rendered result inspected, not just executed
- [ ] #4 Steps to reproduce recorded (commands, seeds, pinned versions and model revisions)
- [ ] #5 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->
