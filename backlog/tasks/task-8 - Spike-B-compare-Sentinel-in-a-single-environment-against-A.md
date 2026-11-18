---
id: TASK-8
title: 'Spike B: compare Sentinel in a single environment against A'
status: To Do
assignee: []
created_date: '2026-11-18 11:01'
labels:
  - sentinel
  - d1
  - boilerplate
milestone: m-0
dependencies:
  - TASK-7
  - TASK-6
  - TASK-2
documentation:
  - docs/spike-b-tolerances.md
type: spike
ordinal: 8000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
One environment would simplify the harness but overrides Sentinel's tested dependency pins. The decision needs evidence against thresholds that were fixed before running.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A single environment with sentence-transformers>=4 and transformers>=5.15 exists without modifying the locked sentinel and d1 extras
- [ ] #2 Sentinel's test suite run in that environment; failures listed
- [ ] #3 Gates 1a, 1b, 2 and 3 in docs/spike-b-tolerances.md evaluated and recorded
- [ ] #4 Decision recorded in the decision log: adopt the single environment or keep A and d1 separate, with reasoning
<!-- AC:END -->
