---
id: TASK-15
title: False-positive analysis on benign chat
status: To Do
assignee: []
created_date: 2026-11-18 11:01
updated_date: '2026-11-24T12:16:00Z'
labels:
  - bias
  - experiment
  - track-both
milestone: m-2
dependencies:
  - TASK-11
  - TASK-13
  - TASK-22
references:
  - https://doi.org/10.48550/arXiv.2106.06213
type: task
ordinal: 15000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Bias focus area: which harmless conversations trip each detector? CONDA adds Dota 2 game chat and trash talk that PAN-2012 lacks, and PAN-2012's non-grooming set includes consensual adult cybersex as a built-in hard case.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 CONDA obtained and recorded in data/README.md
- [ ] #2 False-positive rates for each detector on CONDA and on PAN-2012 non-grooming chats at the operating threshold
- [ ] #3 Slang-heavy versus standard-English comparison with a stated grouping method
- [ ] #4 Failure patterns described qualitatively without quoting raw chat; results aggregate only
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
Input from TASK-2 (see docs/pan2012-structure.md). Check whether detectors rely on shortcuts: test positives average 33.5 non-empty messages vs 12.7 for negatives, and 50.5% of positives have exactly two authors vs 68.7% of negatives. Source (Omegle, IRC, Perverted-Justice) is not labelled in the data, so author count and length are only rough proxies. Hard negatives per the literature: sexual chat between consenting adults (Omegle). Evaluate on the full split and on the >=6 messages / >=2 authors flagged slice.
<!-- SECTION:NOTES:END -->
