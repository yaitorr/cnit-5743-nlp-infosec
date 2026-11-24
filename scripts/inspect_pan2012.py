"""Aggregate structure and label counts for PAN-2012 (TASK-2 spike).

Streams each corpus XML once and prints counts only. No message text, author id or
conversation id is ever printed or written, so the output is safe to commit.

    uv run python scripts/inspect_pan2012.py data/pan2012 > results/pan2012_structure.json
"""

import json
import statistics
import sys
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

PAN = "pan12-sexual-predator-identification"
TRAIN_DIR = f"{PAN}-training-corpus-2012-05-01"
TEST_DIR = f"{PAN}-test-corpus-2012-05-21"
SEGMENT_CAP = 150  # the organisers kept only conversations of at most 150 messages


def read_lines(path: Path) -> list[str]:
    return path.read_text().split("\n") if path.exists() else []


def summarise(values: list[int]) -> dict[str, float]:
    q = statistics.quantiles(values, n=10)
    return {
        "min": min(values),
        "median": statistics.median(values),
        "p90": q[-1],
        "max": max(values),
    }


def inspect_split(
    xml_path: Path, predators: set[str], suspicious: dict[str, set[int]] | None
) -> dict:
    n_conv = n_msg = n_pos = over_cap = 0
    lengths: list[int] = []
    n_authors: Counter[int] = Counter()
    line_not_sequential = time_not_monotonic = 0
    pos_without_suspicious = 0
    author_sets: Counter[frozenset[str]] = Counter()
    predators_seen: set[str] = set()

    # iterparse + clear() keeps memory flat on the 394 MB test file.
    for _, conv in ET.iterparse(xml_path, events=("end",)):
        if conv.tag != "conversation":
            continue
        cid = conv.get("id")
        msgs = conv.findall("message")
        authors = [(m.findtext("author") or "").strip() for m in msgs]
        lines = [int(m.get("line")) for m in msgs]
        times = [m.findtext("time") or "" for m in msgs]

        n_conv += 1
        n_msg += len(msgs)
        lengths.append(len(msgs))
        over_cap += len(msgs) > SEGMENT_CAP
        n_authors[len(set(authors))] += 1
        author_sets[frozenset(authors)] += 1
        line_not_sequential += lines != sorted(lines) or len(set(lines)) != len(lines)
        time_not_monotonic += times != sorted(times)

        hit = predators & set(authors)
        if hit:
            n_pos += 1
            predators_seen |= hit
            pos_without_suspicious += suspicious is not None and cid not in suspicious
        conv.clear()

    repeated = sum(c for c in author_sets.values() if c > 1)
    return {
        "conversations": n_conv,
        "messages": n_msg,
        "positive_conversations": n_pos,
        "negative_conversations": n_conv - n_pos,
        "predator_ids_listed": len(predators),
        "predator_ids_present_in_xml": len(predators_seen),
        "conversations_over_150_messages": over_cap,
        "messages_per_conversation": summarise(lengths),
        "distinct_authors_per_conversation": dict(sorted(n_authors.items())),
        "conversations_with_nonsequential_line_numbers": line_not_sequential,
        "conversations_with_nonmonotonic_time": time_not_monotonic,
        "conversations_sharing_exact_author_set_with_another": repeated,
        "positives_with_no_suspicious_line_in_problem2": pos_without_suspicious,
    }


def main(root: Path) -> None:
    train_dir, test_dir = root / TRAIN_DIR, root / TEST_DIR
    train_pred = set(
        filter(None, read_lines(train_dir / f"{PAN}-training-corpus-predators-2012-05-01.txt"))
    )
    test_pred = set(filter(None, read_lines(test_dir / f"{PAN}-groundtruth-problem1.txt")))

    suspicious: dict[str, set[int]] = {}
    for row in read_lines(test_dir / f"{PAN}-groundtruth-problem2.txt"):
        if row:
            cid, line = row.split("\t")
            suspicious.setdefault(cid, set()).add(int(line))

    out = {
        "train": inspect_split(
            train_dir / f"{PAN}-training-corpus-2012-05-01.xml", train_pred, None
        ),
        "test": inspect_split(
            test_dir / f"{PAN}-test-corpus-2012-05-17.xml", test_pred, suspicious
        ),
        "problem2_test": {
            "conversations_with_suspicious_lines": len(suspicious),
            "suspicious_lines": sum(map(len, suspicious.values())),
        },
    }
    json.dump(out, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main(Path(sys.argv[1]))
