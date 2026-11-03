#!/usr/bin/env python3
"""Build the audit issue register from ``model/issues.json``.

Each issue gets one Markdown record under ``docs/audit/`` and one entry in the
generated index ``docs/audit/README.md``.

Usage:

    python3 scripts/build_issue_register.py
    python3 scripts/build_issue_register.py --check

The script uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ISSUES = ROOT / "model" / "issues.json"
METADATA = ROOT / "source" / "metadata.json"
OUT_DIR = ROOT / "docs" / "audit"
INDEX = OUT_DIR / "README.md"
MAP = ROOT / "model" / "issue-map.json"
REPO_URL = "https://github.com/docxology/WISLIM-audit"
KIND_LABELS = {
    "claim": "claim",
    "red-team": "red-team",
    "workstream": "workstream",
}
SEVERITIES = {"critical", "high", "medium", "low"}
STATUS_LINES = [
    "> **Status: audit observation, not a required fix.** This issue records a",
    "> point that may matter for the work's impact, clarity, or risk. It is not a",
    "> verdict that the work is invalid, and addressing it is optional. The author",
    "> may decline it with reasons. Severity estimates potential impact if the",
    "> concern applies; it does not mean the overall work fails or that a change is",
    "> mandatory.",
    "",
]
REQUIRED_FIELDS = (
    "id",
    "source_id",
    "kind",
    "title",
    "severity",
    "workstream",
    "labels",
    "source_lines",
    "quotes",
    "audit_modules",
    "summary",
    "why",
    "evidence",
    "repair",
    "acceptance",
    "related",
    "file",
)


def slugify(text: str, limit: int = 80) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    if len(text) <= limit:
        return text
    cut = text[:limit]
    if "-" in cut:
        cut = cut.rsplit("-", 1)[0]
    return cut.rstrip("-")


def load_issues() -> list[dict[str, Any]]:
    with ISSUES.open(encoding="utf-8") as handle:
        data = json.load(handle)
    return data["issues"]


def load_metadata() -> dict[str, Any]:
    with METADATA.open(encoding="utf-8") as handle:
        return json.load(handle)


def render_publication(metadata: dict[str, Any]) -> list[str]:
    work = metadata["work"]
    doi = metadata["philpapers"]["doi"]
    philpapers = metadata["philpapers"]["url"]
    pdf_sha = metadata["pdf_sha256"]
    pages = metadata["pages"]
    lines = metadata["text_lines"]
    published = date.fromisoformat(metadata["date"])
    date_text = f"{published.day} {published.strftime('%B')} {published.year}"
    return [
        "## Publication reference",
        "",
        f"David Wishengrad, *{work}*, Version {metadata['version']} "
        f"({date_text}), {pages} pages. DOI "
        f"[`{doi}`](https://doi.org/{doi}); PhilPapers "
        f"[`{metadata['philpapers']['id']}`]({philpapers}).",
        "",
        f"Source of record: `source/WISLIM-v2.0.1.pdf` (SHA-256 `{pdf_sha}`). "
        f"Quotations use the newline-delimited text at "
        f"`source/WISLIM-v2.0.1.txt` ({lines:,} lines), extracted with "
        "`pdftotext -layout`.",
        "",
        "> **Audit status:** critical first pass, not peer review. Severity and",
        "> remediation are provisional judgments, not safety certification.",
        "",
    ]


def issue_by_id(issues: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {issue["id"]: issue for issue in issues}


def expected_file(issue: dict[str, Any]) -> Path:
    return ROOT / issue["file"]


def check_manifest(issues: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    if len(issues) != 66:
        errors.append(f"expected 66 issues, found {len(issues)}")
    expected_ids = [f"WISLIM-{i:03d}" for i in range(1, 67)]
    actual_ids = [issue.get("id") for issue in issues]
    if actual_ids != expected_ids:
        errors.append("issue IDs are not the stable sequence WISLIM-001..WISLIM-066")
    seen_sources: dict[str, str] = {}
    seen_files: dict[str, str] = {}
    for issue in issues:
        iid = issue.get("id", "<missing>")
        for field in REQUIRED_FIELDS:
            if field not in issue:
                errors.append(f"{iid}: missing field {field}")
        if issue.get("kind") not in KIND_LABELS:
            errors.append(f"{iid}: unknown kind {issue.get('kind')!r}")
        if issue.get("severity") not in SEVERITIES:
            errors.append(f"{iid}: unknown severity {issue.get('severity')!r}")
        source = issue.get("source_id")
        if source in seen_sources:
            errors.append(f"{iid}: duplicate source_id {source!r} also used by {seen_sources[source]}")
        seen_sources[source] = iid
        file_name = issue.get("file", "")
        if file_name in seen_files:
            errors.append(f"{iid}: duplicate file {file_name!r} also used by {seen_files[file_name]}")
        seen_files[file_name] = iid
        if not file_name.startswith("docs/audit/WISLIM-"):
            errors.append(f"{iid}: file must be under docs/audit/ and start with WISLIM-")
        if not file_name.endswith(".md"):
            errors.append(f"{iid}: file must end with .md")
        canonical = f"docs/audit/{iid}-{slugify(issue.get('title', ''))}.md"
        if file_name != canonical:
            errors.append(f"{iid}: file should be {canonical!r}, found {file_name!r}")
        related = issue.get("related", [])
        if not isinstance(related, list):
            errors.append(f"{iid}: related must be a list")
        for other in related if isinstance(related, list) else []:
            if other == iid:
                errors.append(f"{iid}: related contains itself")
        if not isinstance(issue.get("labels"), list) or not issue["labels"]:
            errors.append(f"{iid}: labels must be a non-empty list")
        for key in ("summary", "why"):
            if not str(issue.get(key, "")).strip():
                errors.append(f"{iid}: {key} is empty")
        quotes = issue.get("quotes")
        if not isinstance(quotes, list) or not quotes:
            errors.append(f"{iid}: quotes must be a non-empty list")
        else:
            for index, quote in enumerate(quotes):
                if not isinstance(quote, dict):
                    errors.append(f"{iid}: quotes[{index}] must be an object")
                    continue
                if not str(quote.get("text", "")).strip():
                    errors.append(f"{iid}: quotes[{index}].text is empty")
                line = quote.get("line")
                if not isinstance(line, int) or line < 1:
                    errors.append(f"{iid}: quotes[{index}].line must be a positive integer")
                if "note" in quote and not isinstance(quote["note"], str):
                    errors.append(f"{iid}: quotes[{index}].note must be a string")
        if issue.get("kind") == "claim" and not str(issue.get("reply", "")).strip():
            errors.append(f"{iid}: claim issues need a steelman reply")
        for key in ("evidence", "repair", "acceptance"):
            value = issue.get(key)
            if not isinstance(value, list) or not value:
                errors.append(f"{iid}: {key} must be a non-empty list")
    known = set(actual_ids)
    for issue in issues:
        for other in issue.get("related", []):
            if other not in known:
                errors.append(f"{issue['id']}: related issue {other!r} is not in the register")
    for prefix, count in (("C", 35), ("AS", 20), ("WS", 11)):
        found = sorted(
            issue["source_id"]
            for issue in issues
            if str(issue.get("source_id", "")).startswith(prefix)
        )
        expected = [f"{prefix}{i:02d}" for i in range(1, count + 1)]
        if found != expected:
            errors.append(f"{prefix} coverage: expected {expected}, found {found}")
    return errors


def load_map() -> dict[str, Any]:
    if not MAP.is_file():
        return {}
    with MAP.open(encoding="utf-8") as handle:
        return json.load(handle).get("issues", {})


def sentence_case(text: str) -> str:
    text = text.strip()
    if text and text[0].islower():
        return text[0].upper() + text[1:]
    return text


def render_file(
    issue: dict[str, Any],
    number: int | None = None,
    metadata: dict[str, Any] | None = None,
) -> str:
    metadata = metadata or load_metadata()
    labels = ", ".join(issue["labels"])
    modules = ", ".join(issue["audit_modules"]) or "n/a"
    related = ", ".join(issue["related"]) or "none"
    quote_lines = ", ".join(str(quote["line"]) for quote in issue["quotes"])
    github = (
        f"[#{number}]({REPO_URL}/issues/{number})"
        if number
        else "not filed yet (run `make issues`)"
    )
    lines = [
        "---",
        f"id: {issue['id']}",
        f"source_id: {issue['source_id']}",
        f"kind: {issue['kind']}",
        f'title: "{issue["title"]}"',
        f"severity: {issue['severity']}",
        f"workstream: {issue['workstream']}",
        f"labels: [{labels}]",
        f'source_lines: "{issue["source_lines"]}"',
        f"quote_lines: [{quote_lines}]",
        f"audit_modules: [{modules}]",
        f"related: [{related}]",
        f"github_issue: {number if number else 'null'}",
        "---",
        "",
        f"# {issue['id']}: {issue['title']}",
        "",
        f"> **Severity:** {issue['severity']} · **Kind:** {issue['kind']} · "
        f"**Status:** observation · **Source:** `{issue['source_id']}`  ",
        f"> **GitHub issue:** {github}  ",
        f"> **Audit modules:** {modules}  ",
        f"> **Source lines:** {issue['source_lines']}",
        "",
    ]
    lines += STATUS_LINES
    lines += render_publication(metadata)
    lines += ["## Primary quotations", ""]
    for quote in issue["quotes"]:
        lines += [
            f"> {quote['text']}",
            ">",
            f"> — `source/WISLIM-v2.0.1.txt:{quote['line']}`",
            "",
        ]
        note = str(quote.get("note", "")).strip()
        if note:
            lines += [f"**Audit note.** {note}", ""]
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
    lines += [
        "",
        "## Proposed remediation",
        "",
        "These are options for the author's consideration, not requirements. The",
        "audit does not settle the underlying normative questions, so this list is",
        "a starting point rather than a prescription.",
        "",
    ]
    for index, item in enumerate(issue["repair"], 1):
        lines.append(f"{index}. {sentence_case(item)}")
    lines += [
        "",
        "## Suggested checks for reviewers",
        "",
        "If the author chooses to revise, these checks would help a reviewer test",
        "whether the revision addresses the issue. They are not deployment gates.",
        "",
    ]
    for item in issue["acceptance"]:
        lines.append(f"- [ ] {item.strip()}")
    lines += [
        "",
        "## Related issues",
        "",
    ]
    if issue["related"]:
        for other in issue["related"]:
            lines.append(f"- `{other}`")
    else:
        lines.append("- None.")
    if number:
        tracking = f"This record is mirrored to GitHub issue #{number}."
    else:
        tracking = "This record is not yet mirrored to a GitHub issue."
    lines += [
        "",
        "## Tracking",
        "",
        tracking,
        "The issue-number mapping is in `model/issue-map.json`; the GitHub issue",
        "links back to this file.",
        "",
    ]
    return "\n".join(lines)


def render_index(issues: list[dict[str, Any]]) -> str:
    mapping: dict[str, Any] = load_map()
    severities = Counter(issue["severity"] for issue in issues)
    workstreams = Counter(issue["workstream"] for issue in issues)
    lines = [
        "# Audit issue register",
        "",
        "This is the canonical, source-bound issue register for the WISLIM audit.",
        "Every issue has one Markdown record in this directory and one mirrored",
        "GitHub issue. Issue IDs are stable; do not renumber them.",
        "",
        "This index is generated by `scripts/build_issue_register.py`. Edit",
        "`model/issues.json`, then run `make register`; do not edit this file.",
        "",
        "## How to read these issues",
        "",
        "These are audit observations, not defect notices or deployment gates. An",
        "issue can be relevant and worth answering without being fatal, and the",
        "author may reasonably decline a proposed response. Severity estimates",
        "potential impact if the concern applies; it is not a fatality rating and",
        "does not make a change mandatory. Titles name a concern and a possible",
        "response; read them as suggestions, not instructions.",
        "",
        "| Kind | Count |",
        "|---|---:|",
        f"| Claim issues | {sum(1 for i in issues if i['kind'] == 'claim')} |",
        f"| Red-team issues | {sum(1 for i in issues if i['kind'] == 'red-team')} |",
        f"| Workstream issues | {sum(1 for i in issues if i['kind'] == 'workstream')} |",
        f"| Total | {len(issues)} |",
        "",
        "Source coverage: `C01`–`C35` (35 claims), `AS01`–`AS20` (20 red-team",
        "scenarios), and `WS01`–`WS11` (11 workstreams). Every issue carries at",
        "least one verbatim primary quotation from the publication, checked against",
        "`source/WISLIM-v2.0.1.txt`, plus a full publication reference.",
        "",
        "| Severity (impact estimate) | Count |",
        "|---|---:|",
    ]
    for severity in ("critical", "high", "medium", "low"):
        lines.append(f"| {severity} | {severities.get(severity, 0)} |")
    lines += ["", "| Workstream | Count |", "|---|---:|"]
    for name, count in sorted(workstreams.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| `{name}` | {count} |")
    lines += [
        "",
        "## How to use",
        "",
        "- Read the issue record for quotations, evidence, an optional proposed",
        "  response, and suggested reviewer checks.",
        "- Nothing here is a required change; a reasoned reply can decline an issue.",
        "- The GitHub issue is the discussion and tracking surface.",
        "- `make verify` checks the register, records, and local links.",
        "- `make issues-check` verifies the GitHub mirror (requires `gh` auth).",
        "- After editing `model/issues.json`, run `make register` and `make issues`.",
        "",
    ]
    for kind, heading in (
        ("claim", "Claim issues"),
        ("red-team", "Red-team issues"),
        ("workstream", "Workstream issues"),
    ):
        lines += [f"## {heading}", "", "| ID | Issue | Severity | GitHub | Record |", "|---|---|---|---|---|"]
        for issue in issues:
            if issue["kind"] != kind:
                continue
            number = mapping.get(issue["id"], {}).get("number")
            github = f"[#{number}](https://github.com/docxology/WISLIM-audit/issues/{number})" if number else "—"
            record = f"[{issue['id']}]({Path(issue['file']).name})"
            lines.append(
                f"| {issue['id']} | {issue['title']} | {issue['severity']} | {github} | {record} |"
            )
        lines.append("")
    return "\n".join(lines)


def number_for(issue: dict[str, Any], mapping: dict[str, Any]) -> int | None:
    entry = mapping.get(issue["id"])
    if isinstance(entry, dict):
        number = entry.get("number")
        if isinstance(number, int):
            return number
    return None


def write_all(issues: list[dict[str, Any]]) -> None:
    mapping = load_map()
    metadata = load_metadata()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for issue in issues:
        path = expected_file(issue)
        path.write_text(
            render_file(issue, number_for(issue, mapping), metadata),
            encoding="utf-8",
        )
    INDEX.write_text(render_index(issues), encoding="utf-8")


def check_all(issues: list[dict[str, Any]]) -> list[str]:
    errors = check_manifest(issues)
    mapping = load_map()
    metadata = load_metadata()
    numbers: dict[int, str] = {}
    for issue_id, entry in mapping.items():
        if not isinstance(entry, dict) or not isinstance(entry.get("number"), int):
            errors.append(f"issue map: {issue_id} has no integer number")
            continue
        number = entry["number"]
        if number in numbers:
            errors.append(
                f"issue map: number #{number} is assigned to {numbers[number]} and {issue_id}"
            )
        numbers[number] = issue_id
    known = {issue["id"] for issue in issues}
    for issue_id in mapping:
        if issue_id not in known:
            errors.append(f"issue map: unknown issue {issue_id!r}")
    for issue in issues:
        path = expected_file(issue)
        if not path.is_file():
            errors.append(f"{issue['id']}: missing file {path.relative_to(ROOT)}")
            continue
        actual = path.read_text(encoding="utf-8")
        expected = render_file(issue, number_for(issue, mapping), metadata)
        if actual != expected:
            errors.append(f"{issue['id']}: file is out of date; run make register")
    if not INDEX.is_file():
        errors.append("docs/audit/README.md is missing; run make register")
    else:
        actual_index = INDEX.read_text(encoding="utf-8")
        expected_index = render_index(issues)
        if actual_index != expected_index:
            errors.append("docs/audit/README.md is out of date; run make register")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify generated files")
    args = parser.parse_args(argv)
    issues = load_issues()
    if args.check:
        errors = check_all(issues)
        if errors:
            print(f"FAIL: {len(errors)} register error(s)", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)
            return 1
        print(f"OK: {len(issues)} issue records and index are current")
        return 0
    write_all(issues)
    print(f"wrote {len(issues)} issue records and docs/audit/README.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
