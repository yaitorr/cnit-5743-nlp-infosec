#!/usr/bin/env python3
"""Read-only environment check for contributors (macOS and Windows).

Run it from anywhere in the repo:

    uv run --no-project scripts/doctor.py          # checks only
    uv run --no-project scripts/doctor.py --full   # also uv sync, ruff, pytest, marimo

Standard library only, so it runs before the project's own environment exists. It never
installs anything: every failure prints the command that would fix it, for the human (or
their agent) to approve. Exit code is 1 if any check FAILs, otherwise 0.

--full does create the project virtualenv (it runs ``uv sync``); the default run does not.
"""

from __future__ import annotations

import argparse
import platform
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REMOTE_SLUG = "yaitorr/cnit-5743-nlp-infosec"
PYTHON_VERSION = "3.12"
FALLBACK_BACKLOG_MIN = "1.52.0"

PASS, WARN, FAIL, INFO = "PASS", "WARN", "FAIL", "INFO"


@dataclass(frozen=True)
class Result:
    status: str
    section: str
    name: str
    detail: str = ""
    fix: str = ""


# --- pure helpers (unit-tested in tests/test_doctor.py) ------------------------------------


def parse_version(text: str) -> tuple[int, ...]:
    """First dotted number found in text, e.g. 'uv 0.11.26 (abc 2026-06-30)' -> (0, 11, 26)."""
    match = re.search(r"\d+(?:\.\d+)*", text)
    if match is None:
        raise ValueError(f"no version found in {text!r}")
    return tuple(int(part) for part in match.group().split("."))


def meets_minimum(found: str, minimum: str) -> bool:
    """Numeric (not lexicographic) comparison, so 1.9.0 is older than 1.52.0."""
    a, b = parse_version(found), parse_version(minimum)
    width = max(len(a), len(b))
    pad = lambda v: v + (0,) * (width - len(v))  # noqa: E731
    return pad(a) >= pad(b)


def read_backlog_minimum(agents_md: Path) -> str:
    """Minimum Backlog CLI version = the version recorded in AGENTS.md's instruction block."""
    try:
        text = agents_md.read_text(encoding="utf-8")
    except OSError:
        return FALLBACK_BACKLOG_MIN
    match = re.search(r"backlog\.md-instructions-version:\s*([0-9][0-9.]*)", text)
    return match.group(1) if match else FALLBACK_BACKLOG_MIN


def os_family(system: str | None = None) -> str:
    system = (system or platform.system()).lower()
    if system == "darwin":
        return "macos"
    if system == "windows":
        return "windows"
    return "linux"


# Windows hints are untested: nobody has run this on Windows yet (see ONBOARDING.md).
INSTALL_HINTS: dict[str, dict[str, str]] = {
    "git": {
        "macos": "xcode-select --install",
        "windows": "winget install --id Git.Git -e",
        "linux": "install git with your package manager",
    },
    "gh": {
        "macos": "brew install gh",
        "windows": "winget install --id GitHub.cli -e",
        "linux": "see https://cli.github.com",
    },
    "uv": {
        "macos": "brew install uv   (or see https://docs.astral.sh/uv/getting-started/installation/)",
        "windows": "winget install --id astral-sh.uv -e   (or see the uv installation docs)",
        "linux": "see https://docs.astral.sh/uv/getting-started/installation/",
    },
    "backlog": {
        "macos": "npm i -g backlog.md   (or: brew install backlog-md, or: bun add -g backlog.md)",
        "windows": "npm i -g backlog.md   (needs Node.js; or: bun add -g backlog.md)",
        "linux": "npm i -g backlog.md   (or: bun add -g backlog.md)",
    },
}


def fix_hint(tool: str, system: str | None = None) -> str:
    return INSTALL_HINTS[tool][os_family(system)]


def summarize(results: list[Result]) -> tuple[dict[str, int], int]:
    counts = {PASS: 0, WARN: 0, FAIL: 0, INFO: 0}
    for r in results:
        counts[r.status] += 1
    return counts, (1 if counts[FAIL] else 0)


# --- process helper -----------------------------------------------------------------------


def run_split(cmd: list[str], *, timeout: int = 60) -> tuple[int, str, str]:
    """Run a command in the repo root. Returns (returncode, stdout, stderr); never raises."""
    exe = shutil.which(cmd[0])
    if exe is None:
        return 127, "", f"{cmd[0]}: not found on PATH"
    try:
        proc = subprocess.run(  # noqa: S603
            [exe, *cmd[1:]],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            errors="replace",
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return 124, "", f"timed out after {timeout}s"
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def run(cmd: list[str], *, timeout: int = 60) -> tuple[int, str]:
    """Like run_split, but returns the two streams combined."""
    rc, out, err = run_split(cmd, timeout=timeout)
    return rc, "\n".join(part for part in (out, err) if part)


# --- checks -------------------------------------------------------------------------------


def check_tool(tool: str, section: str, minimum: str | None = None) -> Result:
    rc, out = run([tool, "--version"])
    if rc != 0:
        return Result(FAIL, section, tool, "not installed", fix_hint(tool))
    first_line = out.splitlines()[0] if out else ""
    try:
        found = ".".join(str(n) for n in parse_version(first_line))
    except ValueError:
        return Result(WARN, section, tool, f"installed, version not recognised: {first_line!r}")
    if minimum and not meets_minimum(found, minimum):
        return Result(
            FAIL, section, tool, f"{found} is older than the required {minimum}", fix_hint(tool)
        )
    need = f" (needs >= {minimum})" if minimum else ""
    return Result(PASS, section, tool, f"{found}{need}")


def check_gh_auth() -> Result:
    if shutil.which("gh") is None:
        return Result(FAIL, "Tools", "gh login", "gh is not installed", fix_hint("gh"))
    rc, _ = run(["gh", "auth", "status"])
    if rc == 0:
        return Result(PASS, "Tools", "gh login", "authenticated")
    return Result(FAIL, "Tools", "gh login", "not logged in", "gh auth login")


def check_python() -> Result:
    rc, out = run(["uv", "python", "find", PYTHON_VERSION])
    if rc == 0:
        return Result(PASS, "Project", f"Python {PYTHON_VERSION}", out.splitlines()[-1])
    return Result(
        WARN,
        "Project",
        f"Python {PYTHON_VERSION}",
        "not found locally; uv will download it on first sync",
        f"uv python install {PYTHON_VERSION}",
    )


def check_repo() -> list[Result]:
    section = "Repo"
    rc, out = run(["git", "rev-parse", "--is-inside-work-tree"])
    if rc != 0 or out != "true":
        return [Result(FAIL, section, "git repository", "not a git checkout", "git clone ...")]
    results = [Result(PASS, section, "git repository", str(REPO_ROOT))]

    rc, url = run(["git", "remote", "get-url", "origin"])
    if rc == 0 and REMOTE_SLUG in url:
        results.append(Result(PASS, section, "origin remote", REMOTE_SLUG))
    else:
        results.append(
            Result(WARN, section, "origin remote", f"expected {REMOTE_SLUG}, got {url or 'none'}")
        )

    rc, branch = run(["git", "branch", "--show-current"])
    if branch == "main":
        results.append(
            Result(
                WARN,
                section,
                "branch",
                "on main; work happens on a branch and goes through a PR",
                "git switch -c <name>/task-N-slug",
            )
        )
    else:
        results.append(Result(PASS, section, "branch", branch or "(detached HEAD)"))

    rc, status = run(["git", "status", "--porcelain"])
    changed = len(status.splitlines()) if rc == 0 and status else 0
    results.append(
        Result(INFO, section, "working tree", f"{changed} uncommitted change(s)")
        if changed
        else Result(PASS, section, "working tree", "clean")
    )
    return results


def check_push_access() -> Result:
    section, name = "Repo", "push access"
    if shutil.which("gh") is None:
        return Result(INFO, section, name, "skipped (gh not installed)")
    rc, out = run(["gh", "api", f"repos/{REMOTE_SLUG}", "--jq", ".permissions.push"])
    if rc != 0:
        return Result(INFO, section, name, "could not be checked (not logged in, or offline)")
    if out.strip() == "true":
        return Result(PASS, section, name, "you can push branches")
    return Result(
        WARN,
        section,
        name,
        "read-only access",
        "ask the repo owner to add you as a collaborator",
    )


def check_data() -> Result:
    data_dir = REPO_ROOT / "data" / "pan2012"
    if data_dir.is_dir() and any(data_dir.iterdir()):
        return Result(PASS, "Data", "PAN-2012", "present locally (git-ignored)")
    return Result(INFO, "Data", "PAN-2012", "not downloaded yet; see data/README.md and TASK-1")


def full_checks() -> list[Result]:
    section = "Project (--full)"
    steps = [
        ("uv sync", ["uv", "sync"], "check the error above; see README.md Setup", 900),
        ("ruff check", ["uv", "run", "ruff", "check", "."], "fix lint errors", 300),
        ("pytest", ["uv", "run", "pytest", "-q"], "fix failing tests", 600),
        (
            "marimo",
            ["uv", "run", "--group", "notebooks", "marimo", "--version"],
            "uv sync --group notebooks",
            600,
        ),
    ]
    results: list[Result] = []
    for name, cmd, fix, timeout in steps:
        rc, out, err = run_split(cmd, timeout=timeout)
        if rc == 0:
            # Success detail comes from stdout only: uv writes its install chatter to stderr.
            detail = out.splitlines()[-1] if out else "ok"
            results.append(Result(PASS, section, name, detail))
        else:
            combined = "\n".join(part for part in (out, err) if part)
            tail = combined.splitlines()[-1] if combined else ""
            results.append(Result(FAIL, section, name, tail, fix))
    return results


# --- output -------------------------------------------------------------------------------


def render(results: list[Result]) -> str:
    lines: list[str] = []
    current = None
    for r in results:
        if r.section != current:
            current = r.section
            lines += ["", f"{current}"]
        lines.append(f"  [{r.status}] {r.name}" + (f" - {r.detail}" if r.detail else ""))
        if r.fix and r.status in (FAIL, WARN):
            lines.append(f"         fix: {r.fix}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Read-only environment check.")
    parser.add_argument("--full", action="store_true", help="also uv sync, ruff, pytest, marimo")
    parser.add_argument("--offline", action="store_true", help="skip checks that need the network")
    args = parser.parse_args(argv)

    backlog_min = read_backlog_minimum(REPO_ROOT / "AGENTS.md")
    uv = check_tool("uv", "Tools")
    results = [
        check_tool("git", "Tools"),
        check_tool("gh", "Tools"),
        check_gh_auth(),
        uv,
        check_tool("backlog", "Tools", minimum=backlog_min),
    ]
    if uv.status != FAIL:
        results.append(check_python())
    results += check_repo()
    if not args.offline:
        results.append(check_push_access())
    results.append(check_data())

    if args.full:
        if uv.status == FAIL:
            results.append(Result(FAIL, "Project (--full)", "skipped", "uv is required", ""))
        else:
            results += full_checks()

    print(f"Environment check: {os_family()}, python {platform.python_version()}")
    print(render(results))
    counts, code = summarize(results)
    print(
        f"\n{counts[PASS]} passed, {counts[WARN]} warning(s), {counts[FAIL]} failed, "
        f"{counts[INFO]} note(s)."
    )
    if code:
        print("Fix the FAIL items above, then run this again.")
    return code


if __name__ == "__main__":
    sys.exit(main())
