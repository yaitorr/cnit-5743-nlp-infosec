---
id: TASK-2
title: Inspect PAN-2012 structure and count positives
status: In Progress
assignee:
  - '@yaitorr'
created_date: 2026-11-18 11:01
updated_date: '2026-11-24T11:50:00Z'
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
- [x] #1 Findings written up (aggregate only, no raw chat text) on: conversation unit, grouping key, message ordering, how long chats are segmented, and available labels (conversation-level and message-level)
- [x] #2 Counts recorded: conversations, positive conversations (P), negatives, and any provided train/test split sizes
- [x] #3 docs/spike-b-tolerances.md updated: gate 3 restated (zero flips, kept, or loosened) with a dated decision-log row
- [x] #4 No raw conversation text committed or shown in any notebook
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 If code changed: ruff check and pytest pass
- [x] #2 No data, derived artifacts, or raw chat text committed or displayed (hygiene test passes)
- [x] #3 If output was produced (table, figure, page): rendered result inspected, not just executed
- [x] #4 Steps to reproduce recorded (commands, seeds, pinned versions and model revisions)
- [x] #5 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Stream both PAN-2012 XML files and count structure/labels (scripts/inspect_pan2012.py, aggregate-only output to results/pan2012_structure.json). 2. Read the Inches & Crestani overview to explain how labels and segmentation were built. 3. Define a positive conversation (any predator author) and count P. 4. Write findings in docs/pan2012-structure.md. 5. Restate Spike B gate 3 in docs/spike-b-tolerances.md with a dated decision-log row.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Decision (2026-11-24, owner): positive conversation = contains at least one problem-1 predator author. Problem-2 lines rejected as a label: they are only participant-submitted lines judged by one expert (paper s4.2); 2,903 of 3,737 test positives have none. Gate 3 restated to zero flipped decisions (P=3,737, so 0.1% would allow ~3 flips). Observed: 55 train / 13 test conversations exceed the 150-message cap the paper describes. Reproduce: uv run python scripts/inspect_pan2012.py <repo>/data/pan2012 > results/pan2012_structure.json (stdlib only, no seeds).

Adversarial code review (AGENTS.md gate) fixed: missing label files now raise, root cleared in iterparse (peak ~98 MB), train no longer reports a misleading 0 for problem-2 metric, time-inversion metric split to separate midnight wraps (503/1,095 any step; 6/4 multiple), author-set metric restricted to multi-author sets, docs cite the paper for source claims. Declined: dataclass/argparse refactor (one-off spike script).

Owner decisions (2026-11-24) after reading the eSPD-datasets processing code: position is counted in non-empty messages; assume VTPAN and PANC are unavailable and clean PAN-2012 ourselves (eSPD is a reference only). Added measurements: 6,453 test / 2,976 train empty-text messages; 27 / 13 conversations with no non-empty message; line numbers contiguous 1..n; corpus XMLs are CRLF so their sha256 differs from eSPD's dos2unix copies (label files match). Documented in docs/pan2012-structure.md and data/README.md. Handoff for TASK-3: position unit and data scope above.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Positive conversation = contains at least one problem-1 predator author: P = 3,737 test (2.4%), 2,016 train (3.0%) of 155,128 / 66,927 conversations. Problem-2 lines were rejected as a label: they are participant-submitted lines judged by one expert (Inches & Crestani s4.2), and 2,903 of the 3,737 test positives have none. Structure: conversation id is the grouping key; `line` orders messages (0 violations); HH:MM `time` is unreliable across midnight wraps, so position is counted in messages. Organisers split chats at 25-minute gaps and kept at most 150 messages (55 train / 13 test exceed it), so earliest-detection is bounded by one segment; this motivates PANC. Spike B gate 3 restated from 0.1% relative F1 to zero flipped decisions (one flipped positive is ~0.027% of recall; 0.1% would have allowed three), with a dated decision-log row. Verification: ruff and pytest (18) pass; the owner inspected the rendered markdown tables; an adversarial code-reviewer sub-agent found 10 issues, 8 fixed and 2 declined with reasons (see notes). Follow-up: TASK-3 (loader interface) is unblocked and is authored by the project owners.
<!-- SECTION:FINAL_SUMMARY:END -->
