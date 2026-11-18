# Data directory

Everything here except this file is git-ignored, because the repository is public.

## Datasets

| Dataset | Role | Status | Where it goes |
|---|---|---|---|
| PAN-2012 | Main dataset for now | Public ([Zenodo](https://zenodo.org/records/3713280)) | `data/pan2012/` |
| PANC | Planned main dataset (full-length grooming chats) | Source request pending | `data/panc/` |
| ChatCoder2 | Needed to build PANC; shared on request only | Not obtained | `data/chatcoder2/` |
| CONDA | Harmless Dota 2 game chat for the bias tests | Not downloaded | `data/conda/` |

## Rules

1. Never commit raw or per-conversation data, even for PAN-2012. PAN-2012 may include real minors' conversations.
2. Never commit Sentinel indexes or embeddings (they hold or reveal the chats). Those go in `artifacts/`.
3. Never redistribute ChatCoder2 or PANC.
4. Share code and aggregate results only. Keep raw data out of Teams and SharePoint.
5. Record where each dataset came from and its checksum in this table when you add it.
