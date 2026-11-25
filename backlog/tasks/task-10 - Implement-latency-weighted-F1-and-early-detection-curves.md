---
id: TASK-10
title: Implement latency-weighted F1 and early-detection curves
status: To Do
assignee: []
created_date: 2026-11-18 11:01
updated_date: '2026-11-25T00:08:00Z'
labels:
  - metrics
  - track-tech
milestone: m-1
dependencies:
  - TASK-3
references:
  - https://doi.org/10.18653/v1/2021.acl-long.386
type: feature
ordinal: 10000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Latency-weighted F1 (Vogt et al., 2021) is the main metric because it discounts correct flags that arrive late; plain F1 would hide how early detection happens.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Latency-weighted F1 implemented with the penalty constant p (or anchor m) as an argument, defaulting to p = ln(3)/89, and tested against a hand-computed example (true positives warned at messages 1, 45, 90 with F1 = 0.8 give speed 0.7349 and F_latency 0.5879) plus edge cases: a single true positive at message 1 gives speed 1, and no true positives returns 0
- [ ] #2 Detection-rate-versus-messages-seen curve at a fixed low false-positive rate (threshold fixed on train; absolute message counts; false-positive rate reached at each k also reported)
- [ ] #3 Metrics take scores, labels and message positions only, with no dataset dependency
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
Decision (from the TASK-10 latency penalty options doc, 2026-11-24):
- Headline: latency-weighted F1 (Vogt et al., 2021), with p passed in as an argument. Default p = ln(3)/89 (penalty 0.5 at message 90) for comparability with Vogt; switch to the value derived from TASK-22's "how many messages in is early" (p = ln(3)/(m-1)) once it exists, and log the change. Report F1, speed and F_latency on the full split and on the flagged slice (at least 6 non-empty messages, two authors).
- Vogt anchor (checked against the paper, Sec. 5.1): they set p so the penalty is 0.5 when about 20 grooming messages have been exchanged, using ChatCoder2 message labels. In the median labelled CC2 chat that is message 90 (standard deviation about 200 messages), hence p = ln(3)/(90-1) = 0.0123. They rejected the conventional anchor at the median chat length (1,055 messages for their full-length chats) as far too late. Latency l counts all messages before the warning, from 1.
- Second deliverable: detection-rate curve at a false-positive rate fixed on train (acceptance criterion 2). Expect it to carry most of the earliness story on PAN-2012: p puts the penalty at 0.5 only at message 90, but half of positives have fewer than 6 non-empty messages, so every warning falls in the flat start of the penalty and F_latency cannot separate a message-1 warning from a message-5 one.
- Avoid anchoring p at the median positive length (m = 5): speed would measure segment length, not earliness. Skip ERDE: extra constants and no comparison with the eSPD papers.
- Limitation to state: PAN-2012 latency is within-segment (segments cut at 25-minute gaps, capped at 150 messages) and is not comparable to PANC speed. Vogt computes speed on full-length positive chats and F1 on segments; here both are within segments.

Policy input: TASK-22 recommends what counts as early (how many messages in) and candidate false-positive rates for the curve. Read it when setting p and the curve's operating point. This is a recommendation, not a dependency; TASK-10 does not wait on it.

Input from TASK-2 (see docs/pan2012-structure.md). Position unit is non-empty messages. Median conversation is 4 non-empty messages (positives: median 5, mean 33.5). Spike B gate 3 is zero flipped decisions, which the metric's median-based speed term makes hard to bound otherwise. Open: whether single-author conversations stay in the evaluation (changes both metrics).
<!-- SECTION:NOTES:END -->
