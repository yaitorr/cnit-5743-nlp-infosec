---
id: TASK-6
title: Smoke-test d1-omni-600M in its environment
status: To Do
assignee: []
created_date: 2026-11-18 11:01
updated_date: '2026-11-24T10:38:00Z'
labels:
  - d1
  - boilerplate
  - pickup-ready
  - track-tech
milestone: m-0
dependencies: []
references:
  - https://huggingface.co/LiquidAI/d1-omni-600M
type: task
ordinal: 6000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The d1 extra was locked but never installed or run. d1 executes code shipped with the model (trust_remote_code), is under the LFM Open License v1.0, and needs transformers>=5.15, so it has to be verified and reviewed before experiments depend on it.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 uv sync --extra d1 succeeds from a clean checkout
- [ ] #2 Model loads at the pinned revision (02b55d7076f15129e59ab3f94783f32c4b088674) and answers one yes/no question on a synthetic benign text
- [ ] #3 Device and dtype used (MPS or CPU) and approximate latency per call recorded
- [ ] #4 Remote code at the pinned revision reviewed: files that execute on load and any network calls are listed in the methods note, and Yai has spot-checked them
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
Hand-off: trust_remote_code runs with local permissions, so read the remote code before the first load (AC #4).
<!-- SECTION:NOTES:END -->
