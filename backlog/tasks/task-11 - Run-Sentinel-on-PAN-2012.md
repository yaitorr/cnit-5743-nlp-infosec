---
id: TASK-11
title: Run Sentinel on PAN-2012
status: To Do
assignee: []
created_date: 2026-11-18 11:01
updated_date: '2026-11-18T11:13:00Z'
labels:
  - sentinel
  - experiment
milestone: m-1
dependencies:
  - TASK-9
  - TASK-10
  - TASK-5
type: task
ordinal: 11000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
First early-detection results for index matching. The default aggregator has a 10-message floor, so a floor-free sensitivity run keeps a latency gap against d1 from being blamed on that artifact.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Index built from the train split only, with no test conversation or near-duplicate in it
- [ ] #2 Default skewness run and top_k_mean (k=3) sensitivity run reported separately
- [ ] #3 Operating threshold set at a fixed low false-positive rate using train or validation data only
- [ ] #4 Aggregate results committed under results/; per-conversation scores only under results/private/
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 If code changed: ruff check and pytest pass
- [ ] #2 No data, derived artifacts, or raw chat text committed or displayed (hygiene test passes)
- [ ] #3 If output was produced (table, figure, page): rendered result inspected, not just executed
- [ ] #4 Steps to reproduce recorded (commands, seeds, pinned versions and model revisions)
- [ ] #5 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->
