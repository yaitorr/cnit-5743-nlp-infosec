---
id: TASK-2
title: Inspect PAN-2012 structure and count positives
status: In Progress
assignee:
  - '@yaitorr'
created_date: 2026-11-18 11:01
updated_date: '2026-11-24T11:31:00Z'
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
- [ ] #3 If output was produced (table, figure, page): rendered result inspected, not just executed
- [x] #4 Steps to reproduce recorded (commands, seeds, pinned versions and model revisions)
- [ ] #5 Decisions and reasoning written down, and the owner can explain them without help
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Stream both PAN-2012 XML files and count structure/labels (scripts/inspect_pan2012.py, aggregate-only output to results/pan2012_structure.json). 2. Read the Inches & Crestani overview to explain how labels and segmentation were built. 3. Define a positive conversation (any predator author) and count P. 4. Write findings in docs/pan2012-structure.md. 5. Restate Spike B gate 3 in docs/spike-b-tolerances.md with a dated decision-log row.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Decision (2026-11-24, owner): positive conversation = contains at least one problem-1 predator author. Problem-2 lines rejected as a label: they are only participant-submitted lines judged by one expert (paper s4.2); 2,903 of 3,737 test positives have none. Gate 3 restated to zero flipped decisions (P=3,737, so 0.1% would allow ~3 flips). Observed: 55 train / 13 test conversations exceed the 150-message cap the paper describes. Reproduce: uv run python scripts/inspect_pan2012.py <repo>/data/pan2012 > results/pan2012_structure.json (stdlib only, no seeds).

Adversarial code review (AGENTS.md gate) fixed: missing label files now raise, root cleared in iterparse (peak ~98 MB), train no longer reports a misleading 0 for problem-2 metric, time-inversion metric split to separate midnight wraps (503/1,095 any step; 6/4 multiple), author-set metric restricted to multi-author sets, docs cite the paper for source claims. Declined: dataclass/argparse refactor (one-off spike script).
<!-- SECTION:NOTES:END -->
