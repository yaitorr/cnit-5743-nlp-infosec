# Data directory

Everything here except this file is git-ignored, because the repository is public.

## Datasets

| Dataset | Role | Status | Where it goes |
|---|---|---|---|
| PAN-2012 | Main dataset for now | Downloaded 2026-11-23 ([Zenodo](https://zenodo.org/records/3713280)); see [Provenance](#provenance) | `data/pan2012/` |
| PANC | Planned main dataset (full-length grooming chats) | Source request pending | `data/panc/` |
| ChatCoder2 | Needed to build PANC; shared on request only | Not obtained | `data/chatcoder2/` |
| CONDA | Harmless Dota 2 game chat for the bias tests | Not downloaded | `data/conda/` |

## Rules

1. Never commit raw or per-conversation data, even for PAN-2012. PAN-2012 may include real minors'
   conversations.
2. Never commit Sentinel indexes or embeddings (they hold or reveal the chats). Those go in
   `artifacts/`.
3. Never redistribute ChatCoder2 or PANC.
4. Share code and aggregate results only. Keep raw data out of Teams and SharePoint.
5. Record where each dataset came from and its checksum in this table when you add it.

## Provenance

PAN-2012 ("PAN12 Deception Detection: Sexual Predator Identification", Inches & Crestani), Zenodo
DOI [10.5281/zenodo.3713280](https://doi.org/10.5281/zenodo.3713280), retrieved 2026-11-23 from
`https://zenodo.org/api/records/3713280/files/pan12-sexual-predator-identification-test-and-training.zip/content`.
Zenodo publishes only an md5; sha256 was computed locally. The md5 matched Zenodo's.

| Archive | Size (bytes) | sha256 |
|---|---|---|
| `pan12-sexual-predator-identification-test-and-training.zip` (outer, md5 `a00e89c744bec0581292bfaebb171489`) | 91163031 | `1c0efbfc23e38ed52b38ae77600a758f9c1a0c53da825641ad82490b6541b81d` |
| `pan12-sexual-predator-identification-training-corpus-2012-05-01.zip` (inner) | 27619798 | `839c5abcd3e20e2123cceb85bc722dec6406655589e159aa9440c8198d599885` |
| `pan12-sexual-predator-identification-test-corpus-2012-05-21.zip` (inner) | 63584232 | `2dc28233f49d083f0c71a7007a4290f154b37d667195535088b554b93ad2a56d` |

Layout: the three zips sit in `data/pan2012/archive/`; both inner zips are extracted next to it
under `data/pan2012/`. To verify a copy: `shasum -a 256 data/pan2012/archive/*.zip`.

## Terms of use

Zenodo lists the record as open access but states **no license**. The corpus `readme.txt` files add:

- The organizers are "not responsible for the content of the documents (e.g. eventual personal
  informations that might be contained in the text)". Treat the chats as possibly containing real
  minors' conversations.
- Participants are asked not to use external or online resources (e.g. search engines) to solve the
  task, only the provided data.
- No redistribution terms are stated. Absent a license we assume **no right to redistribute**, so
  the data stays out of the repo, Teams and SharePoint (consistent with the rules above).

Source for the terms: the `readme.txt` in each corpus archive and the Zenodo record, read
2026-11-23, plus the PAN-2012 overview paper (Inches & Crestani, CLEF 2012 Working Notes), reviewed
by the repo owner, which also states no license.
**Conclusion: no license is published anywhere we looked.**

## Sharing data across worktrees

`data/` is git-ignored, so each git worktree has its own empty `data/`. Keep one copy in the main
checkout and symlink it from each worktree. The link is local and untracked; do not commit it (the
hygiene test rejects tracked paths under `data/`).

```bash
ln -s <main-checkout>/data/pan2012 data/pan2012
```
