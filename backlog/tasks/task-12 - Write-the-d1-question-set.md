---
id: TASK-12
title: Write the d1 question set
status: To Do
assignee: []
created_date: 2026-11-18 11:01
updated_date: '2026-11-18T11:13:00Z'
labels:
  - d1
milestone: m-1
dependencies:
  - TASK-6
references:
  - https://doi.org/10.1016/j.chiabu.2021.105392
  - https://doi.org/10.18653/v1/2025.naacl-long.241
type: task
ordinal: 12000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
d1 answers typed questions with calibrated probabilities, so the questions encode what we treat as warning signs. They target grooming and approach stages (sexualized talk, image requests, secrecy, isolation, checking whether adults are around, pushing to meet or change apps) following Ringenberg et al. (2022). Age and location questions are context only because they are common in harmless chat (An et al., 2025). The policy lead owns the explicit-versus-inferred framing.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Question set versioned in the repo with type (yes/no, choice or score) and criteria per question
- [ ] #2 Context-only questions are marked and excluded from alert logic
- [ ] #3 Each question traces to a strategy in the grooming-strategy taxonomy
- [ ] #4 Reviewed by the policy lead
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 If code changed: ruff check and pytest pass
- [ ] #2 No data, derived artifacts, or raw chat text committed or displayed (hygiene test passes)
- [ ] #3 If output was produced (table, figure, page): rendered result inspected, not just executed
- [ ] #4 Steps to reproduce recorded (commands, seeds, pinned versions and model revisions)
- [ ] #5 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->
