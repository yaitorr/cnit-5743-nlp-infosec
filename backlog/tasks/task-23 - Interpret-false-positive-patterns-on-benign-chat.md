---
id: TASK-23
title: Interpret false-positive patterns on benign chat
status: To Do
assignee: []
created_date: '2026-11-24T10:36:00Z'
updated_date: '2026-11-24T10:39:00Z'
labels:
  - track-policy
  - bias
milestone: m-2
dependencies:
  - TASK-15
type: task
ordinal: 23000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
TASK-15 produces false-positive rates; this task asks what they mean. Which harmless conversations trip each detector, who is affected, and what a wrong flag costs a person and a platform. Aggregate results only; no raw chat text.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Written interpretation of which kinds of benign chat are flagged by each detector, drawn from aggregate results only
- [ ] #2 Harm of a false flag described for the people involved and for the platform, including the consensual-adult hard case in PAN-2012
- [ ] #3 Limits of the evidence stated (dataset differences, operating threshold chosen)
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->
