---
id: TASK-14
title: Obtain ChatCoder2 and build PANC
status: To Do
assignee: []
created_date: 2026-11-18 11:01
updated_date: '2026-11-24T10:38:00Z'
labels:
  - data
  - track-tech
milestone: m-1
dependencies:
  - TASK-3
references:
  - https://gitlab.com/early-sexual-predator-detection/eSPD-datasets
type: task
ordinal: 14000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
PANC (Vogt et al., 2021) keeps grooming chats at full length, which measuring how far in requires. ChatCoder2 is shared only on request and a request email is pending with the data owner. Building PANC uses the published eSPD-datasets scripts. External dependency: it may arrive late, and PAN-2012 results must not wait for it.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Access to ChatCoder2 granted and recorded (date, contact) in data/README.md
- [ ] #2 PANC built with the published scripts and its checksum recorded
- [ ] #3 PANC loads through the loader interface with no harness changes
- [ ] #4 Data stays local and tests/test_repo_hygiene.py passes
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 If code changed: ruff check and pytest pass
- [ ] #2 No data, derived artifacts, or raw chat text committed or displayed (hygiene test passes)
- [ ] #3 If output was produced (table, figure, page): rendered result inspected, not just executed
- [ ] #4 Steps to reproduce recorded (commands, seeds, pinned versions and model revisions)
- [ ] #5 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->
