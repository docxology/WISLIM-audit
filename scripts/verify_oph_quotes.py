#!/usr/bin/env python3
"""Check every OPH quotation in the review models against the pinned commit.

The repository and commit come from ``reviews/oph-lfdi-57/model/review.json``.
Each ``oph_evidence`` entry names a path, a line, and a quotation. The check
reads the file at the pinned commit with ``git show`` and looks for the
whitespace-normalized quotation in a window around the line: three lines before
and two after, because the sources wrap prose across lines.

Usage:

    python3 scripts/verify_oph_quotes.py --oph-repo PATH

``PATH`` is any clone that contains the pinned commit. The script uses only the
Python standard library and ``git``.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterator

ROOT = Path(__file__).resolve().parents[1]
MODELS = (
    ROOT / "reviews" / "oph-lfdi-57" / "model" / "review.json",
    ROOT / "reviews" / "oph-lfdi-57" / "model" / "reply.json",
)
BEFORE = 3
AFTER = 2


def normalize(text: str) -> str:
    return " ".join(text.split())


def pinned() -> tuple[str, str]:
    with MODELS[0].open(encoding="utf-8") as handle:
        review = json.load(handle)["review"]
    return review["oph_repository"], review["oph_commit"]


def evidence() -> Iterator[tuple[str, dict[str, Any]]]:
    for model in MODELS:
        if not model.is_file():
            continue
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--oph-repo", required=True, help="clone containing the pinned commit")
    args = parser.parse_args(argv)
    repo = Path(args.oph_repo)
    repository, commit = pinned()

    found = git(repo, "cat-file", "-e", f"{commit}^{{commit}}")
    if found.returncode != 0:
        print(f"FAIL: {repo} does not contain {commit}", file=sys.stderr)
        return 1

    blobs: dict[str, list[str] | None] = {}
    failures: list[str] = []
    total = 0
    for topic_id, item in evidence():
        total += 1
        path, line, quote = item["path"], item["line"], item["quote"]
        if path not in blobs:
            shown = git(repo, "show", f"{commit}:{path}")
            blobs[path] = shown.stdout.split("\n") if shown.returncode == 0 else None
        lines = blobs[path]
        if lines is None:
            failures.append(f"{topic_id}: {path} is not in {commit}")
            continue
        window = normalize(" ".join(lines[max(0, line - 1 - BEFORE) : line + AFTER]))
        if normalize(quote) not in window:
            failures.append(f"{topic_id}: quotation not found at {path}:{line}: {quote!r}")

    for failure in failures:
        print(f"FAIL: {failure}", file=sys.stderr)
    if failures:
        print(f"FAIL: {len(failures)} of {total} OPH quotations did not verify", file=sys.stderr)
        return 1
    print(f"OK: {total}/{total} OPH quotations verified at {repository} {commit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
