#!/usr/bin/env python3
"""Publish and verify the GitHub mirror of the audit issue register.

The Markdown records under ``docs/audit/`` are canonical. This script creates
one GitHub issue per record, records the issue number in
``model/issue-map.json``, and keeps each issue body in sync with its record.

Usage:

    python3 scripts/sync_issues.py            # create missing, then sync
    python3 scripts/sync_issues.py --check    # read-only verification
    python3 scripts/sync_issues.py --dry-run  # show planned actions

The script shells out to the authenticated ``gh`` CLI. It uses only the Python
standard library.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from build_issue_register import (
    ROOT,
    check_manifest,
    load_issues,
    write_all,
)

MAP = ROOT / "model" / "issue-map.json"
BODY_LIMIT = 60_000
TITLE_RE = re.compile(r"^(WISLIM-\d{3}): ")
BRANCH = "main"

LABELS: dict[str, tuple[str, str]] = {
    "audit": ("5319e7", "Critical audit of WISLIM v2.0.1"),
    "claim": ("1d76db", "Issue against a registered claim (C01-C35)"),
    "red-team": ("b60205", "Adversarial scenario or abuse case"),
    "workstream": ("0e8a16", "Multi-issue repair workstream"),
    "severity:critical": ("b60205", "Blocks adoption; may cause severe harm"),
    "severity:high": ("d93f0b", "Material defect; repair before use"),
    "severity:medium": ("fbca04", "Should be repaired; lower immediate risk"),
    "severity:low": ("c2e0c6", "Editorial or clarity repair"),
    "workstream:argument": ("1d76db", "Thesis, definitions, and normative argument"),
    "workstream:formal": ("006b75", "Formal model and risk metrics"),
    "workstream:evidence": ("0052cc", "Evidence, citations, and human review"),
    "workstream:governance": ("6f42c1", "Governance, oversight, and appeals"),
    "workstream:rhetoric": ("d4c5f9", "Rhetoric, coercion, and dissent"),
    "workstream:clinical": ("e99695", "Clinical, legal, and ethical review"),
    "workstream:security": ("ee0701", "Privacy, security, and record integrity"),
    "workstream:scope": ("bfd4f2", "Scope, moral status, and definitions"),
    "workstream:publication": ("bfdadc", "Versioning, licensing, and publication"),
    "workstream:red-team": ("f9d0c4", "Independent red team and corrections"),
}


class GhError(RuntimeError):
    """A ``gh`` invocation failed."""


def gh(*args: str, input_text: str | None = None) -> str:
    proc = subprocess.run(
        ["gh", *args],
        input=input_text,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "").strip()
        raise GhError(f"gh {' '.join(args[:3])} failed: {detail}")
    return proc.stdout


def normalize(text: str | None) -> str:
    if not text:
        return ""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    lines = [line.rstrip() for line in lines]
    while lines and not lines[-1]:
        lines.pop()
    while lines and not lines[0]:
        lines.pop(0)
    return "\n".join(lines)


def load_store() -> dict[str, Any]:
    if not MAP.is_file():
        return {
            "schema_version": 1,
            "repository": "docxology/WISLIM-audit",
            "note": "GitHub issue-number mapping for the audit register.",
            "issues": {},
        }
    with MAP.open(encoding="utf-8") as handle:
        return json.load(handle)


def save_store(data: dict[str, Any]) -> None:
    ordered = {
        key: data["issues"][key]
        for key in sorted(data["issues"], key=lambda key: int(key.split("-")[1]))
    }
    data["issues"].clear()
    data["issues"].update(ordered)
    MAP.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def repo_slug() -> str:
    with (ROOT / "model" / "issues.json").open(encoding="utf-8") as handle:
        return json.load(handle).get("repository", "docxology/WISLIM-audit")


def record_url(issue: dict[str, Any], repo: str) -> str:
    return f"https://github.com/{repo}/blob/{BRANCH}/{issue['file']}"


def render_body(issue: dict[str, Any], numbers: dict[str, int], repo: str) -> str:
    related_lines: list[str] = []
    for other in issue["related"]:
        number = numbers.get(other)
        if number:
            related_lines.append(f"- #{number} ({other})")
        else:
            related_lines.append(f"- {other} (not filed)")
    if not related_lines:
        related_lines.append("- None.")

    modules = ", ".join(f"`{module}`" for module in issue["audit_modules"]) or "n/a"

    lines = [
        f"<!-- wislim-issue: {issue['id']} -->",
        f"# {issue['id']}: {issue['title']}",
        "",
        f"**Severity:** {issue['severity']} · **Kind:** {issue['kind']} · "
        f"**Source:** `{issue['source_id']}`  ",
        f"**Workstream:** `{issue['workstream']}`  ",
        f"**Register record:** [`{issue['file']}`]({record_url(issue, repo)})  ",
        f"**Audit modules:** {modules}  ",
        f"**Source lines:** {issue['source_lines']}",
        "",
        "## Quoted passage",
        "",
        f"> {issue['quote']}",
        ">",
        f"> — `source/WISLIM-v2.0.1.txt:{issue['quote_line']}`",
        "",
    ]
    note = str(issue.get("quote_note", "")).strip()
    if note:
        lines += [note, ""]
    lines += [
        "## Summary",
        "",
        issue["summary"].strip(),
        "",
        "## Evidence",
        "",
    ]
    for item in issue["evidence"]:
        lines.append(f"- {item.strip()}")
    lines += ["", "## Why it matters", "", issue["why"].strip()]
    if issue.get("reply"):
        lines += ["", "## Steelman and reply", "", issue["reply"].strip()]
    lines += ["", "## Required repair", ""]
    for index, item in enumerate(issue["repair"], 1):
        text = item.strip()
        if text[:1].islower():
            text = text[:1].upper() + text[1:]
        lines.append(f"{index}. {text}")
    lines += ["", "## Acceptance criteria", ""]
    for item in issue["acceptance"]:
        lines.append(f"- [ ] {item.strip()}")
    lines += ["", "## Related issues", "", *related_lines, "", "---", ""]
    lines.append(
        "<sub>Canonical record: "
        f"[`{issue['file']}`]({record_url(issue, repo)}). "
        "Issue IDs are stable; do not renumber. Source citations use "
        "newline-delimited line numbers in `source/WISLIM-v2.0.1.txt`. "
        "Edit the record and run `make issues`; use comments for discussion.</sub>"
    )
    body = "\n".join(lines) + "\n"
    if len(body) > BODY_LIMIT:
        raise ValueError(f"{issue['id']}: body is {len(body)} characters, over the {BODY_LIMIT} limit")
    return body


def remote_issues(repo: str) -> list[dict[str, Any]]:
    output = gh(
        "issue",
        "list",
        "--repo",
        repo,
        "--state",
        "all",
        "--limit",
        "500",
        "--json",
        "number,title,state,url,labels,body",
    )
    data = json.loads(output or "[]")
    for item in data:
        item["label_names"] = sorted(label["name"] for label in item.get("labels", []))
        item["body"] = item.get("body") or ""
    return data


def index_remote(remote: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for item in remote:
        match = TITLE_RE.match(item["title"])
        if not match:
            continue
        issue_id = match.group(1)
        if issue_id in indexed:
            raise GhError(
                f"duplicate GitHub issues for {issue_id}: "
                f"#{indexed[issue_id]['number']} and #{item['number']}"
            )
        indexed[issue_id] = item
    return indexed


def ensure_labels(repo: str, dry_run: bool) -> None:
    for name in sorted(LABELS):
        color, description = LABELS[name]
        if dry_run:
            print(f"would ensure label {name}")
            continue
        gh(
            "label",
            "create",
            name,
            "--repo",
            repo,
            "--color",
            color,
            "--description",
            description,
            "--force",
        )


def create_issue(
    issue: dict[str, Any],
    body: str,
    repo: str,
    dry_run: bool,
) -> dict[str, Any] | None:
    title = f"{issue['id']}: {issue['title']}"
    if dry_run:
        print(f"would create {title}")
        return None
    args = [
        "issue",
        "create",
        "--repo",
        repo,
        "--title",
        title,
        "--body-file",
        "-",
    ]
    for label in issue["labels"]:
        args += ["--label", label]
    url = gh(*args, input_text=body).strip().splitlines()[-1]
    number = int(url.rsplit("/", 1)[-1])
    print(f"created #{number} {title}")
    return {"number": number, "url": url, "title": title, "state": "OPEN"}


def sync(repo: str, issues: list[dict[str, Any]], dry_run: bool) -> int:
    data = load_store()
    registry: dict[str, dict[str, Any]] = data.setdefault("issues", {})

    ensure_labels(repo, dry_run)
    if dry_run:
        for issue in issues:
            body = render_body(issue, {}, repo)
            print(f"would create {issue['id']}: {issue['title']} ({len(body)} chars)")
        print(f"would sync {len(issues)} issues")
        return 0

    remote = remote_issues(repo)
    by_id = index_remote(remote)

    # 1. Create or adopt every issue, in stable ID order.
    for issue in issues:
        issue_id = issue["id"]
        existing = by_id.get(issue_id)
        if existing:
            registry[issue_id] = {
                "number": existing["number"],
                "url": existing["url"],
                "title": existing["title"],
                "state": existing["state"].upper(),
            }
            continue
        numbers = {key: entry["number"] for key, entry in registry.items()}
        created = create_issue(issue, render_body(issue, numbers, repo), repo, dry_run)
        if created:
            registry[issue_id] = created
            save_store(data)

    # 2. Reload so adopted and new issues are in one index.
    remote = remote_issues(repo)
    by_id = index_remote(remote)
    missing = [issue["id"] for issue in issues if issue["id"] not in by_id]
    if missing:
        print(f"FAIL: missing GitHub issues: {', '.join(missing)}", file=sys.stderr)
        return 1

    numbers = {issue["id"]: by_id[issue["id"]]["number"] for issue in issues}

    # 3. Rewrite bodies now that every related number is known.
    changed = 0
    for issue in issues:
        item = by_id[issue["id"]]
        expected = render_body(issue, numbers, repo)
        if normalize(item["body"]) != normalize(expected):
            gh(
                "issue",
                "edit",
                str(item["number"]),
                "--repo",
                repo,
                "--body-file",
                "-",
                input_text=expected,
            )
            changed += 1
    print(f"updated {changed} issue bodies")

    # 4. Add any missing labels.
    relabeled = 0
    for issue in issues:
        item = by_id[issue["id"]]
        current = set(item.get("label_names", []))
        missing_labels = [label for label in issue["labels"] if label not in current]
        if not missing_labels:
            continue
        args = ["issue", "edit", str(item["number"]), "--repo", repo]
        for label in missing_labels:
            args += ["--add-label", label]
        gh(*args)
        relabeled += 1
    if relabeled:
        print(f"added labels to {relabeled} issues")

    # 5. Persist the map and regenerate records so they carry issue numbers.
    for issue in issues:
        item = by_id[issue["id"]]
        registry[issue["id"]] = {
            "number": item["number"],
            "url": item["url"],
            "title": item["title"],
            "state": item["state"].upper(),
        }
    save_store(data)
    write_all(issues)
    print(f"synced {len(issues)} issues; wrote model/issue-map.json and docs/audit/")
    return 0


def check(repo: str, issues: list[dict[str, Any]]) -> int:
    errors: list[str] = []
    registry = load_store().get("issues", {})
    known = {issue["id"] for issue in issues}

    for issue_id in registry:
        if issue_id not in known:
            errors.append(f"issue map: unknown issue {issue_id!r}")
    numbers = [entry.get("number") for entry in registry.values()]
    if len(set(numbers)) != len(numbers):
        errors.append("issue map: duplicate issue numbers")

    try:
        remote = remote_issues(repo)
    except GhError as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    by_id = index_remote(remote)
    filed = {issue["id"]: by_id[issue["id"]]["number"] for issue in issues if issue["id"] in by_id}

    unsynced = [issue["id"] for issue in issues if issue["id"] not in by_id]
    if unsynced:
        errors.append(f"missing GitHub issues: {', '.join(unsynced)}")
    extras = sorted(set(by_id) - known)
    if extras:
        errors.append(f"GitHub issues with no register record: {', '.join(extras)}")

    for issue in issues:
        issue_id = issue["id"]
        entry = registry.get(issue_id)
        if not isinstance(entry, dict):
            errors.append(f"{issue_id}: no entry in model/issue-map.json")
            continue
        item = by_id.get(issue_id)
        if not item:
            continue
        if entry.get("number") != item["number"]:
            errors.append(
                f"{issue_id}: map has #{entry.get('number')}, GitHub has #{item['number']}"
            )
        expected_title = f"{issue_id}: {issue['title']}"
        if item["title"] != expected_title:
            errors.append(f"{issue_id}: title differs; run make issues")
        if normalize(item["body"]) != normalize(render_body(issue, filed, repo)):
            errors.append(f"{issue_id}: body is out of date; run make issues")
        missing_labels = sorted(set(issue["labels"]) - set(item["label_names"]))
        if missing_labels:
            errors.append(f"{issue_id}: missing labels: {', '.join(missing_labels)}")

    if errors:
        print(f"FAIL: {len(errors)} issue mirror error(s)", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print(f"OK: {len(issues)} GitHub issues match the register")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify the GitHub mirror")
    parser.add_argument("--dry-run", action="store_true", help="print planned actions")
    parser.add_argument("--repo", default=None, help="override the GitHub repository")
    args = parser.parse_args(argv)

    try:
        gh("auth", "status")
    except (GhError, FileNotFoundError) as error:
        print(f"FAIL: gh is not available or not authenticated: {error}", file=sys.stderr)
        return 1

    issues = load_issues()
    errors = check_manifest(issues)
    if errors:
        print(f"FAIL: issue register is invalid ({len(errors)} error(s))", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    repo = args.repo or repo_slug()
    try:
        gh("repo", "view", repo, "--json", "name", "--jq", ".name")
    except GhError as error:
        print(f"FAIL: cannot access {repo}: {error}", file=sys.stderr)
        return 1

    if args.check:
        return check(repo, issues)
    return sync(repo, issues, args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
