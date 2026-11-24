"""Aggregate structure and label counts for PAN-2012 (TASK-2 spike).

Streams each corpus XML once and prints counts only. No message text, author id or
conversation id is ever printed or written, so the output is safe to commit.

    uv run python scripts/inspect_pan2012.py data/pan2012 > results/pan2012_structure.json
"""

import json
import statistics
import sys
from collections import Counter
from itertools import pairwise
from pathlib import Path
from xml.etree import ElementTree as ET

PAN = "pan12-sexual-predator-identification"
TRAIN_DIR = f"{PAN}-training-corpus-2012-05-01"
TEST_DIR = f"{PAN}-test-corpus-2012-05-21"
SEGMENT_CAP = 150  # the organisers kept only conversations of at most 150 messages
MIN_MESSAGES = 6  # the VTPAN and PANC filters drop segments shorter than this


def read_lines(path: Path) -> list[str]:
    """Non-empty stripped lines. A missing file raises instead of silently yielding no labels."""
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def summarise(values: list[int]) -> dict[str, float]:
    """Min, median, 90th percentile and max, all as floats."""
    q = statistics.quantiles(values, n=10)
    return {
        "min": float(min(values)),
        "median": float(statistics.median(values)),
        "p90": float(q[-1]),
        "max": float(max(values)),
    }


def class_profile(rows: list[tuple[int, int]]) -> dict[str, float]:
    """Length and author-count profile of one class; rows are (non-empty messages, authors)."""
    lengths = [length for length, _ in rows]
    return {
        "nonempty_messages": summarise(lengths) | {"mean": round(statistics.fmean(lengths), 1)},
        f"share_with_at_least_{MIN_MESSAGES}_nonempty_messages": round(
            sum(n >= MIN_MESSAGES for n in lengths) / len(rows), 3
        ),
        "share_with_exactly_two_authors": round(sum(a == 2 for _, a in rows) / len(rows), 3),
    }


def inspect_split(
    xml_path: Path, predators: set[str], suspicious: dict[str, set[int]] | None
) -> dict:
    n_conv = n_msg = n_pos = over_cap = over_cap_nonempty = 0
    n_empty_msg = n_no_nonempty = lines_not_contiguous = 0
    lengths: list[int] = []
    nonempty_lengths: list[int] = []
    by_class: dict[bool, list[tuple[int, int]]] = {True: [], False: []}
    n_authors: Counter[int] = Counter()
    lines_not_increasing = time_any_backward = time_multi_backward = 0
    pos_without_suspicious = 0
    author_sets: Counter[frozenset[str]] = Counter()
    predators_seen: set[str] = set()

    # Clearing each conversation AND the root keeps memory flat on the 394 MB test file:
    # clearing only the conversation leaves an empty element per conversation on the root.
    root = None
    for event, conv in ET.iterparse(xml_path, events=("start", "end")):
        if root is None:
            root = conv
        if event != "end" or conv.tag != "conversation":
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
        # A message counts only if its text has non-whitespace content (the position unit).
        nonempty = sum(bool((m.findtext("text") or "").strip()) for m in msgs)
        nonempty_lengths.append(nonempty)
        n_empty_msg += len(msgs) - nonempty
        n_no_nonempty += nonempty == 0
        over_cap_nonempty += nonempty > SEGMENT_CAP
        lines_not_contiguous += lines != list(range(1, len(lines) + 1))
        n_authors[len(set(authors))] += 1
        author_sets[frozenset(authors)] += 1
        lines_not_increasing += not all(a < b for a, b in pairwise(lines))
        # Times are HH:MM strings, so one drop can be a midnight wrap, not a real inversion.
        backward = sum(b < a for a, b in pairwise(times))
        time_any_backward += backward > 0
        time_multi_backward += backward > 1

        hit = predators & set(authors)
        by_class[bool(hit)].append((nonempty, len(set(authors))))
        if hit:
            n_pos += 1
            predators_seen |= hit
            pos_without_suspicious += suspicious is not None and cid not in suspicious
        conv.clear()
        root.clear()

    # Only multi-author sets: a lone author recurring says nothing about segmentation.
    repeated = sum(c for a, c in author_sets.items() if len(a) > 1 and c > 1)
    result = {
        "by_class": {
            "positive": class_profile(by_class[True]),
            "negative": class_profile(by_class[False]),
        },
        "conversations": n_conv,
        "messages": n_msg,
        "positive_conversations": n_pos,
        "negative_conversations": n_conv - n_pos,
        "predator_ids_listed": len(predators),
        "predator_ids_present_in_xml": len(predators_seen),
        "conversations_over_150_messages": over_cap,
        "messages_per_conversation": summarise(lengths),
        "messages_with_empty_text": n_empty_msg,
        "conversations_with_no_nonempty_message": n_no_nonempty,
        "conversations_over_150_nonempty_messages": over_cap_nonempty,
        "nonempty_messages_per_conversation": summarise(nonempty_lengths),
        "conversations_with_lines_not_1_to_n": lines_not_contiguous,
        "distinct_authors_per_conversation": dict(sorted(n_authors.items())),
        "conversations_with_non_increasing_line_numbers": lines_not_increasing,
        "conversations_with_any_backward_time_step": time_any_backward,
        "conversations_with_multiple_backward_time_steps": time_multi_backward,
        "multi_author_conversations_sharing_author_set_with_another": repeated,
    }
    if suspicious is not None:  # problem 2 has no train labels, so the key is omitted there
        result["positives_with_no_suspicious_line_in_problem2"] = pos_without_suspicious
    return result


def main(root: Path) -> None:
    train_dir, test_dir = root / TRAIN_DIR, root / TEST_DIR
    train_pred = set(read_lines(train_dir / f"{PAN}-training-corpus-predators-2012-05-01.txt"))
    test_pred = set(read_lines(test_dir / f"{PAN}-groundtruth-problem1.txt"))
    assert train_pred and test_pred, "predator lists are empty; check the data path"

    suspicious: dict[str, set[int]] = {}
    for row in read_lines(test_dir / f"{PAN}-groundtruth-problem2.txt"):
        cid, line = row.split("\t")
        suspicious.setdefault(cid, set()).add(int(line))

    out = {
        "train": inspect_split(
            train_dir / f"{PAN}-training-corpus-2012-05-01.xml", train_pred, None
        ),
        "test": inspect_split(
            test_dir / f"{PAN}-test-corpus-2012-05-17.xml", test_pred, suspicious
        ),
        "predator_ids_shared_between_train_and_test": len(train_pred & test_pred),
        "problem2_test": {
            "conversations_with_suspicious_lines": len(suspicious),
            "suspicious_lines": sum(map(len, suspicious.values())),
        },
    }
    json.dump(out, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main(Path(sys.argv[1]))
