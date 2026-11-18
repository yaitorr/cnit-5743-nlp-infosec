# Catching grooming early, and what it costs kids' privacy

Purdue CNIT 57400 group project. We run two different detectors, Roblox Sentinel and
Liquid AI d1-omni-600M (plus a cascade of the two), on the same chat data and ask how early each
one catches grooming, who it wrongly flags, and what it has to retain about children's chats.

## Setup

Sentinel and d1 need incompatible dependency versions (Sentinel pins `transformers<5` and
`numpy<2`; d1 needs `transformers>=5.15`), so each lives in its own extra and its own virtualenv.
Both are resolved together in one `uv.lock`.

```bash
# Shared code + Sentinel
UV_PROJECT_ENVIRONMENT=.venv-sentinel uv sync --extra sentinel

# Shared code + d1
UV_PROJECT_ENVIRONMENT=.venv-d1 uv sync --extra d1

# Run tests in either environment
UV_PROJECT_ENVIRONMENT=.venv-sentinel uv run pytest
```

The cascade runs in two stages and hands off through files in `artifacts/`:
Sentinel scores (sentinel env), then d1 reviews the flagged conversations (d1 env).

## Layout

| Path | Purpose |
|---|---|
| `src/grooming_eval/data/` | Dataset loaders behind one interface (PAN-2012 now, PANC later) |
| `src/grooming_eval/detectors/` | Sentinel and d1 wrappers |
| `src/grooming_eval/metrics/` | Latency-weighted F1, early-detection curves, calibration |
| `data/` | Raw datasets. **Git-ignored**; see `data/README.md` |
| `artifacts/` | Indexes, embeddings, scores. **Git-ignored** |
| `results/` | Aggregate results only (per-conversation output goes in `results/private/`) |
| `notebooks/` | Analysis notebooks |
| `dist/` | Exported deliverables, named `YYYY-MM-DD_ytorresv_CNIT-57400_<work>.pdf` |

## Data handling

This repository is public. Raw chats, Sentinel indexes, and embeddings are never committed.
`tests/test_repo_hygiene.py` fails if any are tracked.

## Results site

Aggregate results are published as a static marimo export via GitHub Pages
(`.github/workflows/pages.yml`). The datasets cannot be redistributed, so the site never includes them.
Notebooks hide their code by default; see `AGENTS.md`.

## License

Code is MIT-licensed (see `LICENSE`). The license covers this repository's code only, not the datasets
or the third-party models and libraries it uses (Sentinel is Apache-2.0; d1 is under the LFM Open License v1.0).

## Pinned third-party artifacts

| Artifact | Pin |
|---|---|
| Roblox Sentinel | `66c69854e806bd9f5c866379b6c75f3fcb4d2e6c` (Apache-2.0) |
| `LiquidAI/d1-omni-600M` | `02b55d7076f15129e59ab3f94783f32c4b088674` (LFM1.0 license; runs its own code via `trust_remote_code`) |
