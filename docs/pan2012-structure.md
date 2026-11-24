# PAN-2012 structure and label counts

Findings for TASK-2. Aggregate only: no message text, author id or conversation id appears here.
Reproduce with `uv run python scripts/inspect_pan2012.py <path-to>/data/pan2012 > results/pan2012_structure.json`
(about 10 seconds and under 100 MB of memory; stdlib only). Corpus provenance and checksums are in
`data/README.md`. Background: Inches and Crestani, "Overview of the International Sexual Predator
Identification Competition at PAN-2012".

## Structure

### Conversation unit and grouping key

The unit is a `<conversation id=...>` element holding `<message line=...>` elements, each with an
`author`, a `time` and a `text`. The conversation `id` is the grouping key. Author ids are
pseudonymous and consistent across conversations, which is what makes author-level labels possible.

### Message ordering

`line` is strictly increasing within every conversation (0 violations in both splits), so it is the
ordering key. `time` is HH:MM only and "might not be the real time" per the corpus readme. It steps
backwards at least once in 503 train and 1,095 test conversations, but only 6 and 4 conversations
step backwards more than once, so almost all of these are probably a single midnight wrap rather
than real disorder (we cannot tell the two apart from HH:MM alone). Either way, HH:MM cannot give
elapsed time across a wrap, so position in a conversation is counted in messages.

### Segmentation of long chats

The organisers cut message streams into conversations wherever the gap exceeded 25 minutes and kept
only conversations of at most 150 messages (paper, section 2.1). A long grooming exchange can
therefore appear as several conversations. This is consistent with 8,730 test (3,565 train)
multi-author conversations whose exact author set also occurs in another conversation, but that is
weak evidence (a recurring pair could also be unrelated chats), and there is no session id to prove it. The cap is
not perfectly applied: 55 train and 13 test conversations exceed 150 messages (maximum 1,166).
Consequence: the earliest-detection position is bounded by one segment, not a whole relationship,
which is the motivation for PANC.

### Sources

Per the paper (section 2.1 and Table 1), positives come only from Perverted-Justice (PJ) chat logs,
and negatives are largely Omegle (about 95% two-user) and IRC logs. The sources differ in style, so a
detector could separate by source. Our own counts show 68% of conversations with exactly two authors
in both splits, and some with many authors (up to 115 in test).

## Labels

| Label | Level | Source file | Count (test) |
|---|---|---|---|
| Predator author id | Author | problem 1 ground truth | 254 ids (142 in train) |
| Suspicious line | Message | problem 2 ground truth | 6,478 lines in 834 conversations |
| Positive conversation | Conversation | derived (contains a predator author) | 3,737 |

There is no conversation-level label in the files. We define a positive conversation as one that
contains at least one predator author. Problem 2 cannot define positives: its lines are only those
submitted by participants and judged by one expert, so it is incomplete and subjective (paper,
section 4.2). 2,903 of the 3,737 positives have no problem-2 line.

## Counts

| | Train | Test |
|---|---|---|
| Conversations | 66,927 | 155,128 |
| Messages | 903,607 | 2,058,781 |
| Positives (P) | 2,016 | 3,737 |
| Negatives | 64,911 | 151,391 |
| Positive rate | 3.0% | 2.4% |
| Median / 90th percentile / max messages per conversation | 4 / 38 / 1,166 | 4 / 38 / 1,024 |

The corpus ships with a fixed train/test split (30% released as training); we keep it.

## Consequence for Spike B gate 3

One flipped positive moves recall by about 1/3,737, or 0.027%. We restated gate 3 as zero flipped
decisions; see `docs/spike-b-tolerances.md` and its decision log.
