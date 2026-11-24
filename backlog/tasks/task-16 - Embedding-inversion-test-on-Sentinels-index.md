---
id: TASK-16
title: Embedding-inversion test on Sentinel's index
status: To Do
assignee: []
created_date: 2026-11-18 11:01
updated_date: '2026-11-24T10:38:00Z'
labels:
  - privacy
  - experiment
  - track-both
milestone: m-2
dependencies:
  - TASK-11
  - TASK-4
references:
  - https://doi.org/10.18653/v1/2023.emnlp-main.765
type: spike
ordinal: 16000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Privacy focus area: can embeddings stored by Sentinel be turned back into readable text (Morris et al., 2023)? This is where the privacy cost of index matching becomes concrete, compared with d1 which keeps nothing but needs long windows of conversation as input.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 What the index retains (corpus, embeddings or both) is verified from the code at the pinned Sentinel commit
- [ ] #2 Inversion attempted first on synthetic or benign texts; any real PAN-2012 embeddings stay in local artifacts/
- [ ] #3 Recovery metrics reported in aggregate only
- [ ] #4 A short comparison states what each design retains and what it needs as input
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 If code changed: ruff check and pytest pass
- [ ] #2 No data, derived artifacts, or raw chat text committed or displayed (hygiene test passes)
- [ ] #3 If output was produced (table, figure, page): rendered result inspected, not just executed
- [ ] #4 Steps to reproduce recorded (commands, seeds, pinned versions and model revisions)
- [ ] #5 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->
