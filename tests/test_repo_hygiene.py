"""Guardrail: the repo is public, so no data or derived artifacts may be tracked."""

import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ALLOWED = {"data/README.md", "artifacts/.gitkeep", "dist/.gitkeep"}
FORBIDDEN_PREFIXES = ("data/", "artifacts/", "results/private/", "dist/")


def tracked_files() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files"], cwd=REPO, capture_output=True, text=True, check=True
    ).stdout
    return out.splitlines()


def test_no_data_or_artifacts_tracked():
    leaked = [f for f in tracked_files() if f.startswith(FORBIDDEN_PREFIXES) and f not in ALLOWED]
    assert not leaked, f"Sensitive paths are tracked in git: {leaked}"
