---
id: TASK-2
title: Inspect PAN-2012 structure and count positives
status: To Do
assignee: []
created_date: 2026-11-18 11:01
updated_date: '2026-11-24T10:38:00Z'
labels:
  - data
  - boilerplate
  - track-tech
milestone: m-0
dependencies:
  - TASK-1
type: spike
ordinal: 2000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Measuring how far into a conversation each detector first flags it requires knowing how conversations are grouped and ordered, and how long chats were split into segments. The positive count P also decides whether the provisional 0.1% end-metric tolerance in docs/spike-b-tolerances.md is achievable, since one flipped decision moves recall by about 1/P.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Findings written up (aggregate only, no raw chat text) on: conversation unit, grouping key, message ordering, how long chats are segmented, and available labels (conversation-level and message-level)
- [ ] #2 Counts recorded: conversations, positive conversations (P), negatives, and any provided train/test split sizes
- [ ] #3 docs/spike-b-tolerances.md updated: gate 3 restated (zero flips, kept, or loosened) with a dated decision-log row
- [ ] #4 No raw conversation text committed or shown in any notebook
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 If code changed: ruff check and pytest pass
- [ ] #2 No data, derived artifacts, or raw chat text committed or displayed (hygiene test passes)
- [ ] #3 If output was produced (table, figure, page): rendered result inspected, not just executed
- [ ] #4 Steps to reproduce recorded (commands, seeds, pinned versions and model revisions)
- [ ] #5 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->
