# Spike B: equivalence tolerances

Written **before** any A-vs-B comparison is run, so the thresholds cannot be tuned to the outcome.

## Question

Does running Sentinel in a single environment alongside d1 (overriding Sentinel's tested pins:
`sentence-transformers>=4`, `transformers>=5.15`) change its behavior compared with the pinned
reference environment (A: `sentence-transformers<4`, `transformers<5`, `numpy<2`)?

## Method

Score the same fixed texts with the same index in both environments and compare. Comparison texts are
synthetic or benign, or kept local under `artifacts/`; only aggregate differences are committed.

## Step 0: noise floor

Run environment A twice on the same texts with different batch sizes (1 vs 32). Any difference is
numerical noise. Record the maximum absolute score difference as `noise_floor`.

## Gates

B is accepted only if **all** gates pass.

| Gate | Quantity | Threshold | Status |
|---|---|---|---|
| 1a | Max absolute score difference, A vs B | at most 10 x `noise_floor` | Confirmed (2026-11-18) |
| 1b | Spearman rank correlation of scores | at least 0.999 | Confirmed (2026-11-18) |
| 2 | Agreement of flag decisions at the operating threshold (chosen on A) | at least 99.5% | Confirmed (2026-11-18) |
| 3 | Flipped decisions, A vs B, on PAN-2012 test | exactly 0 (per-conversation flag, and index of the first flagging message) | Confirmed (2026-11-24) |

## Open items

- **Gate 3 was restated on 2026-11-24** after counting positives (TASK-2; see
  `docs/pan2012-structure.md`). P = 3,737 positive test conversations (any predator author), so one
  flipped positive moves recall by about 0.027% and 0.1% would have tolerated about three flips. We
  chose zero flips instead: it is stricter, needs no assumption about how the latency-weighted F1 of
  TASK-10 responds to a flip, and is easy to verify. Gate 3 must still be smaller than the smallest
  detector-vs-detector gap we intend to claim.
- Gates 1 and 2 use judgment values (10x, 0.999, 99.5%), confirmed as-is on 2026-11-18. Rationale to
  state if asked: 10x leaves headroom above numerical noise while staying far below what a tokenization
  change would cause (expectation, not yet measured).

## Decision log

| Date | Change | Reason |
|---|---|---|
| 2026-11-18 | Gate 3 set to 0.1% (provisional) | Lowered from 1%; pending the positive count |
| 2026-11-18 | Gates 1a, 1b, 2 confirmed as proposed | Accepted by project owner before any comparison was run |
| 2026-11-24 | Gate 3 restated from 0.1% relative F1 to zero flipped decisions | P = 3,737 (test), so 0.1% would allow about 3 flips; zero flips is stricter and independent of the not-yet-written metric |
