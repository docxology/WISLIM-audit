#!/usr/bin/env python3
"""Publish and verify the GitHub mirror of the reply register and corrections.

``reviews/oph-lfdi-57/model/reply.json`` is canonical. This script creates one
GitHub issue per reply topic (``OPH-REP-NNN``) and per correction
(``OPH-AUD-NNN``), records the numbers in
``reviews/oph-lfdi-57/model/reply-issue-map.json``, and keeps each body in sync.
A correction with a ``fixed_in`` commit is closed as completed.

Usage:

    python3 scripts/sync_reply_issues.py            # create missing, then sync
    python3 scripts/sync_reply_issues.py --check    # read-only verification
    python3 scripts/sync_reply_issues.py --dry-run  # show planned actions

The script shells out to the authenticated ``gh`` CLI. It uses only the Python
standard library.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from typing import Any

from build_reply_register import (
    BRANCH,
    ISSUE_MAP,
    REPO_URL,
    load_issue_map,
    load_model,
    render_correction,
    render_topic,
    repo_path,
    topic_path,
    write_all,
)
from sync_issues import gh, normalize

REPO = "docxology/WISLIM-audit"
BODY_LIMIT = 60_000
TITLE_RE = re.compile(r"^(OPH-(?:REP|AUD)-\d{3}): ")
LABELS: dict[str, tuple[str, str]] = {
    "review:oph-lfdi-57": ("5319e7", "Part of the OPH/LFDI review exchange"),
    "reply-topic": ("1d76db", "Observation on one claim in the 2026-11-03 reply; not a required fix"),
    "correction": ("0e8a16", "A correction to this tracker's own record"),
}


def entries(data: dict[str, Any]) -> list[dict[str, Any]]:
    items = [dict(topic, labels=["review:oph-lfdi-57", "reply-topic"]) for topic in data["topics"]]
    items += [dict(item, labels=["review:oph-lfdi-57", "correction"]) for item in data["corrections"]]
    return items


def is_correction(item: dict[str, Any]) -> bool:
    return item["id"].startswith("OPH-AUD-")


def render_body(item: dict[str, Any], data: dict[str, Any], issues: dict[str, dict[str, Any]]) -> str:
    if is_correction(item):
        record = f"{REPO_URL}/blob/{BRANCH}/reviews/oph-lfdi-57/corrections.md"
        body = [f"# {item['id']}: {item['title']}", ""] + render_correction(item)
    else:
        record = f"{REPO_URL}/blob/{BRANCH}/{repo_path(topic_path(item))}"
        text = render_topic(item, data, issues, numbers_as_links=True)
        body = text.split("---\n", 2)[2].strip().split("\n")
    lines = [f"<!-- oph-reply-register: {item['id']} -->", *body, "", "---", ""]
    lines.append(
        f"<sub>Canonical record: [`{record.rsplit('/', 1)[-1]}`]({record}). IDs are stable. "
        "Edit the model and run `make reply-issues`; use comments for discussion.</sub>"
    )
    text = "\n".join(lines) + "\n"
    if len(text) > BODY_LIMIT:
        raise ValueError(f"{item['id']}: body is {len(text)} characters, over the {BODY_LIMIT} limit")
    return text


def remote_issues() -> dict[str, dict[str, Any]]:
    output = gh(
        "issue", "list", "--repo", REPO, "--state", "all", "--limit", "500",
        "--json", "number,title,state,url,labels,body",
    )
    indexed: dict[str, dict[str, Any]] = {}
    for item in json.loads(output or "[]"):
        match = TITLE_RE.match(item["title"])
        if not match:
            continue
        if match.group(1) in indexed:
            raise RuntimeError(f"duplicate GitHub issues for {match.group(1)}")
        item["label_names"] = sorted(label["name"] for label in item.get("labels", []))
        indexed[match.group(1)] = item
    return indexed


def save_map(issues: dict[str, dict[str, Any]]) -> None:
    ordered = {key: issues[key] for key in sorted(issues)}
    payload = {
        "schema_version": 1,
        "repository": REPO,
        "note": "GitHub issue-number mapping for the reply register and corrections.",
        "issues": ordered,
    }
    ISSUE_MAP.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def record(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "number": item["number"],
        "url": item["url"],
        "title": item["title"],
        "state": item["state"].upper(),
    }


def sync(data: dict[str, Any], dry_run: bool) -> int:
    items = entries(data)
    if dry_run:
        for item in items:
            print(f"would sync {item['id']}: {item['title']} ({len(render_body(item, data, {}))} chars)")
        return 0
    for name, (color, description) in sorted(LABELS.items()):
        gh("label", "create", name, "--repo", REPO, "--color", color, "--description", description, "--force")

    remote = remote_issues()
    for item in items:
        if item["id"] in remote:
            continue
        title = f"{item['id']}: {item['title']}"
        args = ["issue", "create", "--repo", REPO, "--title", title, "--body-file", "-"]
        for label in item["labels"]:
            args += ["--label", label]
        url = gh(*args, input_text=render_body(item, data, {})).strip().splitlines()[-1]
        print(f"created #{url.rsplit('/', 1)[-1]} {title}")

    remote = remote_issues()
    missing = [item["id"] for item in items if item["id"] not in remote]
    if missing:
        print(f"FAIL: missing GitHub issues: {', '.join(missing)}", file=sys.stderr)
        return 1
    issues = {key: record(value) for key, value in remote.items()}
    save_map(issues)

    changed = 0
    for item in items:
        current = remote[item["id"]]
        expected = render_body(item, data, issues)
        if normalize(current.get("body")) != normalize(expected):
            gh("issue", "edit", str(current["number"]), "--repo", REPO, "--body-file", "-", input_text=expected)
            changed += 1
        absent = [label for label in item["labels"] if label not in current["label_names"]]
        if absent:
            args = ["issue", "edit", str(current["number"]), "--repo", REPO]
            for label in absent:
                args += ["--add-label", label]
            gh(*args)
        if is_correction(item) and item.get("fixed_in") and current["state"].upper() == "OPEN":
            gh(
                "issue", "close", str(current["number"]), "--repo", REPO, "--reason", "completed",
                "--comment", f"Fixed in {item['fixed_in']}. See {REPO_URL}/commit/{item['fixed_in']}",
            )
            print(f"closed #{current['number']} {item['id']}")
    print(f"updated {changed} issue bodies")

    issues = {key: record(value) for key, value in remote_issues().items()}
    save_map(issues)
    write_all(data)
    print(f"synced {len(items)} issues; wrote {repo_path(ISSUE_MAP)} and the generated records")
    return 0


def check(data: dict[str, Any]) -> int:
    errors: list[str] = []
    issues = load_issue_map()
    remote = remote_issues()
    for item in entries(data):
        current = remote.get(item["id"])
        if current is None:
            errors.append(f"{item['id']}: no GitHub issue")
            continue
        if normalize(current.get("body")) != normalize(render_body(item, data, issues)):
            errors.append(f"{item['id']}: GitHub body differs from the register")
        if issues.get(item["id"], {}).get("number") != current["number"]:
            errors.append(f"{item['id']}: issue map number differs from GitHub")
        expected_state = "CLOSED" if is_correction(item) and item.get("fixed_in") else "OPEN"
        if current["state"].upper() != expected_state:
            errors.append(f"{item['id']}: state is {current['state']}, expected {expected_state}")
    for error in errors:
        print(f"FAIL: {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"OK: {len(entries(data))} GitHub issues match the reply register and corrections")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="read-only comparison with GitHub")
    parser.add_argument("--dry-run", action="store_true", help="print planned actions")
    args = parser.parse_args(argv)
    data = load_model()
    return check(data) if args.check else sync(data, args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
