---
id: TASK-3
title: Design the dataset loader interface
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
  - TASK-2
type: feature
ordinal: 3000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The main data is PAN-2012 now and PANC later (full-length ChatCoder2 chats), plus CONDA for benign game chat. One interface keeps the harness dataset-agnostic so PANC drops in without touching experiments. Per AGENTS.md the project authors design and write this; agents explain options and review.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Interface exposes per conversation: stable id, ordered messages with author and index, conversation label, message-level labels when the dataset has them, and the train/test split
- [ ] #2 PAN-2012 implemented behind the interface
- [ ] #3 Train/test separation enforced by the interface so an index built from train can never see test conversations
- [ ] #4 Unit tests use synthetic fixtures only
- [ ] #5 A short note lists what PANC and CONDA must provide to plug in without harness changes
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 If code changed: ruff check and pytest pass
- [ ] #2 No data, derived artifacts, or raw chat text committed or displayed (hygiene test passes)
- [ ] #3 If output was produced (table, figure, page): rendered result inspected, not just executed
- [ ] #4 Steps to reproduce recorded (commands, seeds, pinned versions and model revisions)
- [ ] #5 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->
