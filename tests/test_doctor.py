"""Unit tests for the pure logic in scripts/doctor.py (version comparison, hints, summary)."""

import importlib.util
import sys
from pathlib import Path

import pytest

DOCTOR_PATH = Path(__file__).resolve().parents[1] / "scripts" / "doctor.py"
spec = importlib.util.spec_from_file_location("doctor", DOCTOR_PATH)
doctor = importlib.util.module_from_spec(spec)
# Register before executing: @dataclass looks the module up in sys.modules by name.
sys.modules["doctor"] = doctor
spec.loader.exec_module(doctor)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("uv 0.11.26 (396ef7ce4 2026-06-30 aarch64-apple-darwin)", (0, 11, 26)),
        ("git version 2.54.0 (Apple Git-157)", (2, 54, 0)),
        ("1.55.3", (1, 55, 3)),
        ("v2", (2,)),
    ],
)
def test_parse_version(text, expected):
    assert doctor.parse_version(text) == expected


def test_parse_version_rejects_text_without_a_number():
    with pytest.raises(ValueError):
        doctor.parse_version("not a version")


@pytest.mark.parametrize(
    ("found", "minimum", "expected"),
    [
        ("1.55.3", "1.52.0", True),
        ("1.52.0", "1.52.0", True),  # equal counts as meeting the minimum
        ("1.9.0", "1.52.0", False),  # numeric, not lexicographic ("9" > "52" as text)
        ("2", "1.52.0", True),  # shorter versions are padded with zeros
        ("1.52", "1.52.1", False),
    ],
)
def test_meets_minimum(found, minimum, expected):
    assert doctor.meets_minimum(found, minimum) is expected


def test_read_backlog_minimum_reads_the_instruction_block(tmp_path):
    agents = tmp_path / "AGENTS.md"
    agents.write_text("<!-- backlog.md-instructions-version: 1.60.2 -->\n", encoding="utf-8")
    assert doctor.read_backlog_minimum(agents) == "1.60.2"


def test_read_backlog_minimum_falls_back_when_missing(tmp_path):
    assert doctor.read_backlog_minimum(tmp_path / "nope.md") == doctor.FALLBACK_BACKLOG_MIN
    plain = tmp_path / "AGENTS.md"
    plain.write_text("no block here", encoding="utf-8")
    assert doctor.read_backlog_minimum(plain) == doctor.FALLBACK_BACKLOG_MIN


@pytest.mark.parametrize(
    ("system", "expected"),
    [("Darwin", "macos"), ("Windows", "windows"), ("Linux", "linux")],
)
def test_os_family(system, expected):
    assert doctor.os_family(system) == expected


def test_every_tool_has_a_hint_for_each_supported_os():
    for tool, by_os in doctor.INSTALL_HINTS.items():
        assert {"macos", "windows", "linux"} <= set(by_os), tool
    assert "npm i -g backlog.md" in doctor.fix_hint("backlog", "Windows")


def test_summarize_exit_code_only_fails_on_fail():
    ok = [doctor.Result(doctor.PASS, "s", "a"), doctor.Result(doctor.WARN, "s", "b")]
    bad = ok + [doctor.Result(doctor.FAIL, "s", "c")]
    assert doctor.summarize(ok)[1] == 0
    counts, code = doctor.summarize(bad)
    assert code == 1
    assert counts[doctor.FAIL] == 1 and counts[doctor.WARN] == 1
