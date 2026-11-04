#!/usr/bin/env python3
"""Check every OPH quotation in the review models against upstream.

The repository and the pinned commit come from
``reviews/oph-lfdi-57/model/review.json``. Each ``oph_evidence`` entry names a path,
a line, and a quotation. An entry may also name its own ``commit``, when the record
is about what an earlier release said. The check reads the file with ``git show``
and looks for the whitespace-normalized quotation in a window around the line:
three lines before and two after, because the sources wrap prose across lines.

Usage:

    python3 scripts/verify_oph_quotes.py --oph-repo PATH
    python3 scripts/verify_oph_quotes.py --oph-repo PATH --ref origin/main

``PATH`` is any clone that contains the commits. With ``--ref``, the script compares
the pinned evidence with that ref and reports which quotations moved and which are
gone, so a re-pin starts from a list. An entry with its own commit records a fixed
release and is not compared. The script uses only the Python standard library and
``git``.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from bisect import bisect_right
from pathlib import Path
from typing import Any, Iterator

ROOT = Path(__file__).resolve().parents[1]
MODELS = (
    ROOT / "reviews" / "oph-lfdi-57" / "model" / "review.json",
    ROOT / "reviews" / "oph-lfdi-57" / "model" / "reply.json",
)
BEFORE = 3
AFTER = 2

Blobs = dict[tuple[str, str], "list[str] | None"]


def normalize(text: str) -> str:
    return " ".join(text.split())


def pinned() -> tuple[str, str]:
    with MODELS[0].open(encoding="utf-8") as handle:
        review = json.load(handle)["review"]
    return review["oph_repository"], review["oph_commit"]


def evidence() -> Iterator[tuple[str, dict[str, Any]]]:
    for model in MODELS:
        with model.open(encoding="utf-8") as handle:
            data = json.load(handle)
        for topic in data.get("topics", []):
            for item in topic.get("oph_evidence", []):
                yield topic["id"], item


def git(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )


def read_lines(repo: Path, commit: str, path: str, blobs: Blobs) -> list[str] | None:
    key = (commit, path)
    if key not in blobs:
        shown = git(repo, "show", f"{commit}:{path}")
        blobs[key] = shown.stdout.split("\n") if shown.returncode == 0 else None
    return blobs[key]


def anchored(lines: list[str], line: int, quote: str) -> bool:
    window = normalize(" ".join(lines[max(0, line - 1 - BEFORE) : line + AFTER]))
    return normalize(quote) in window


def locate(lines: list[str], quote: str) -> int | None:
    """Return the line where a quotation starts, wherever it is in the file."""
    offsets: list[tuple[int, int]] = []
    pieces: list[str] = []
    position = 0
    for number, line in enumerate(lines, 1):
        piece = normalize(line)
        if piece:
            offsets.append((position, number))
            pieces.append(piece)
            position += len(piece) + 1
    at = " ".join(pieces).find(normalize(quote))
    if at < 0:
        return None
    return offsets[bisect_right(offsets, (at, len(lines) + 1)) - 1][1]


def verify(repo: Path, repository: str, pin: str) -> int:
    items = list(evidence())
    if not items:
        print("FAIL: the models record no OPH quotations", file=sys.stderr)
        return 1
    commits = {pin} | {item["commit"] for _, item in items if "commit" in item}
    missing = sorted(c for c in commits if git(repo, "cat-file", "-e", f"{c}^{{commit}}").returncode != 0)
    for commit in missing:
        print(f"FAIL: {repo} does not contain {commit}", file=sys.stderr)
    if missing:
        return 1

    blobs: Blobs = {}
    failures: list[str] = []
    for topic_id, item in items:
        commit = item.get("commit", pin)
        path, line, quote = item["path"], item["line"], item["quote"]
        lines = read_lines(repo, commit, path, blobs)
        if lines is None:
            failures.append(f"{topic_id}: {path} is not in {commit}")
        elif not anchored(lines, line, quote):
            failures.append(f"{topic_id}: quotation not found at {path}:{line} in {commit[:9]}: {quote!r}")

    for failure in failures:
        print(f"FAIL: {failure}", file=sys.stderr)
    if failures:
        print(f"FAIL: {len(failures)} of {len(items)} OPH quotations did not verify", file=sys.stderr)
        return 1
    print(f"OK: {len(items)}/{len(items)} OPH quotations verified at {repository} {pin}")
    return 0


def drift(repo: Path, ref: str, pin: str) -> int:
    resolved = git(repo, "rev-parse", "--verify", "-q", f"{ref}^{{commit}}")
    if resolved.returncode != 0:
        print(f"FAIL: {repo} has no commit for {ref}", file=sys.stderr)
        return 2
    commit = resolved.stdout.strip()
    behind = git(repo, "rev-list", "--count", f"{pin}..{commit}").stdout.strip() or "?"

    blobs: Blobs = {}
    held = fixed = 0
    moved: list[str] = []
    gone: list[str] = []
    for topic_id, item in evidence():
        if "commit" in item:
            fixed += 1
            continue
        path, line, quote = item["path"], item["line"], item["quote"]
        lines = read_lines(repo, commit, path, blobs)
        if lines is not None and anchored(lines, line, quote):
            held += 1
            continue
        found = locate(lines, quote) if lines is not None else None
        if found is not None:
            moved.append(f"{topic_id}: {path}:{line} is now at line {found}")
        else:
            gone.append(f"{topic_id}: {path}:{line} is gone: {quote!r}")

    print(f"{ref} is {commit}, {behind} commits past the pin {pin[:9]}")
    print(f"{held} held, {len(moved)} moved, {len(gone)} gone; {fixed} name their own release and were not compared")
    for entry in moved + gone:
        print(f"  {entry}")
    return 1 if moved or gone else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--oph-repo", required=True, help="clone containing the commits")
    parser.add_argument("--ref", help="compare the pinned evidence with this ref instead of verifying it")
    args = parser.parse_args(argv)
    repo = Path(args.oph_repo)
    repository, pin = pinned()
    if args.ref:
        return drift(repo, args.ref, pin)
    return verify(repo, repository, pin)


if __name__ == "__main__":
    raise SystemExit(main())
