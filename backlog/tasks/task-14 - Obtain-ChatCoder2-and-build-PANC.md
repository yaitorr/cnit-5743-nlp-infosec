---
id: TASK-14
title: Obtain ChatCoder2 and build PANC
status: To Do
assignee: []
created_date: '2026-11-18 11:01'
labels:
  - data
milestone: m-1
dependencies:
  - TASK-3
references:
  - 'https://gitlab.com/early-sexual-predator-detection/eSPD-datasets'
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
