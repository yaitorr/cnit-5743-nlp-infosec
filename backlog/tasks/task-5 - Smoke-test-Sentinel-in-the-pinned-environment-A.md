---
id: TASK-5
title: Smoke-test Sentinel in the pinned environment (A)
status: To Do
assignee: []
created_date: '2026-11-18 11:01'
labels:
  - sentinel
  - boilerplate
milestone: m-0
dependencies:
  - TASK-4
type: task
ordinal: 5000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The Sentinel extra was resolved and locked but never installed or run. Environment A is the reference everything else is compared against, so it has to be shown working end to end.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 uv sync --extra sentinel succeeds from a clean checkout
- [ ] #2 A small index built with SentinelLocalIndex.from_texts from synthetic texts scores held-out synthetic texts end to end
- [ ] #3 Sentinel's own test suite at the pinned commit passes in environment A (result recorded)
- [ ] #4 The command sequence is documented in the README
<!-- AC:END -->
