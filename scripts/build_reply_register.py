#!/usr/bin/env python3
"""Build the correspondence ledger, reply register, and corrections record.

``reviews/oph-lfdi-57/model/reply.json`` is canonical. Each distinct claim in the
sender's reply becomes one record under ``reviews/oph-lfdi-57/reply/``. Each
correction to this tracker becomes one section of
``reviews/oph-lfdi-57/corrections.md``. Quotations are checked against the
recorded correspondence, the verified review transcription, and the WISLIM text.

Usage:

    python3 scripts/build_reply_register.py
    python3 scripts/build_reply_register.py --check

The script uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REVIEW_DIR = ROOT / "reviews" / "oph-lfdi-57"
MODEL = REVIEW_DIR / "model" / "reply.json"
REVIEW_MODEL = REVIEW_DIR / "model" / "review.json"
ISSUE_MAP = REVIEW_DIR / "model" / "reply-issue-map.json"
CORRESPONDENCE = REVIEW_DIR / "correspondence"
LEDGER = CORRESPONDENCE / "README.md"
LEDGER_DATA = CORRESPONDENCE / "metadata.json"
RECORDS = REVIEW_DIR / "reply"
INDEX = RECORDS / "README.md"
CORRECTIONS = REVIEW_DIR / "corrections.md"
REPLY_TEXT = CORRESPONDENCE / "03-wishengrad-reply.txt"
SENT_TEXT = CORRESPONDENCE / "02-friedman-response-as-sent.txt"
REVIEW_TEXT = REVIEW_DIR / "source" / "LFDI_Alignment_Audit-57.verified.txt"
WISLIM_TEXT = ROOT / "source" / "WISLIM-v2.0.1.txt"
AUDIT_DIR = ROOT / "docs" / "audit"
REPO_URL = "https://github.com/docxology/WISLIM-audit"
BRANCH = "main"
TOPIC_COUNT = 16
CORRECTION_COUNT = 11

KINDS = {
    "attribution": "attributes to the response or its author something the text does not say",
    "context": "reads a quotation against its context",
    "logic": "the inference does not follow as stated",
    "framing": "defines in advance what counts as an answer",
    "provenance": "turns on a source, version, or verification that has not been supplied",
    "demand": "moves from argument to motive, burden, or office",
}
REQUIRED_TOPIC_FIELDS = (
    "id",
    "title",
    "kind",
    "quotes",
    "summary",
    "assessment",
    "oph_evidence",
    "sent_evidence",
    "wislim_source",
    "review_evidence",
    "audit_records",
    "literature",
    "response",
    "related",
)
REQUIRED_CORRECTION_FIELDS = (
    "id",
    "title",
    "sent_email",
    "what_was_wrong",
    "what_changed",
    "files",
)
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9.-]+")
PHONE_RE = re.compile(r"(?<![\d.])(?:\+?\d{1,2}[ .-])?\(?\d{3}\)?[ .-]\d{3}[ .-]\d{4}(?!\d)")


def normalize(text: str) -> str:
    return " ".join(text.split())


def normalize_passage(text: str) -> str:
    return re.sub(r"(?<=[A-Za-z0-9])-\s+(?=[A-Za-z])", "-", normalize(text))


def slugify(text: str, limit: int = 72) -> str:
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if len(text) <= limit:
        return text
    cut = text[:limit]
    if "-" in cut:
        cut = cut.rsplit("-", 1)[0]
    return cut.rstrip("-")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_model() -> dict[str, Any]:
    return load_json(MODEL)


def load_issue_map() -> dict[str, dict[str, Any]]:
    if not ISSUE_MAP.is_file():
        return {}
    return load_json(ISSUE_MAP).get("issues", {})


def oph_pin() -> tuple[str, str]:
    review = load_json(REVIEW_MODEL)["review"]
    return review["oph_repository"], review["oph_commit"]


def topic_path(topic: dict[str, Any]) -> Path:
    return RECORDS / f"{topic['id']}-{slugify(topic['title'])}.md"


def repo_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def blob_url(rel: str, line: int | None = None) -> str:
    suffix = f"#L{line}" if line else ""
    return f"{REPO_URL}/blob/{BRANCH}/{rel}{suffix}"


def oph_url(item: dict[str, Any]) -> str:
    repository, commit = oph_pin()
    return f"{repository}/blob/{commit}/{item['path']}#L{item['line']}"


def audit_record(issue_id: str) -> Path | None:
    matches = sorted(AUDIT_DIR.glob(f"{issue_id}-*.md"))
    return matches[0] if matches else None


def literature_index(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["key"]: item for item in data["literature"]}


def check_quote_lines(
    errors: list[str],
    label: str,
    items: list[dict[str, Any]],
    lines: list[str],
    span: int = 0,
    passage: bool = False,
) -> None:
    fold = normalize_passage if passage else normalize
    for item in items:
        line, quote = item.get("line"), str(item.get("quote", ""))
        if not isinstance(line, int) or not 1 <= line <= len(lines):
            errors.append(f"{label}: line {line!r} is out of bounds")
            continue
        if len(quote.strip()) < 8:
            errors.append(f"{label}: quotation {quote!r} is too short")
        window = fold(" ".join(lines[line - 1 : line + span]))
        if fold(quote) not in window:
            errors.append(f"{label}: quotation not found at line {line}: {quote!r}")


def check_model(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    topics = data.get("topics", [])
    corrections = data.get("corrections", [])
    expected = [f"OPH-REP-{index:03d}" for index in range(1, TOPIC_COUNT + 1)]
    if [topic.get("id") for topic in topics] != expected:
        errors.append("reply topic IDs are not the stable sequence OPH-REP-001..016")
    expected_fixes = [f"OPH-AUD-{index:03d}" for index in range(1, CORRECTION_COUNT + 1)]
    if [item.get("id") for item in corrections] != expected_fixes:
        errors.append("correction IDs are not the stable sequence OPH-AUD-001..011")

    ledger = load_json(LEDGER_DATA)
    for name, info in ledger["files"].items():
        path = CORRESPONDENCE / name
        if not path.is_file():
            errors.append(f"correspondence file is missing: {name}")
        elif sha256(path) != info["sha256"]:
            errors.append(f"{name}: hash does not match correspondence metadata")

    reply_lines = REPLY_TEXT.read_text(encoding="utf-8").splitlines()
    sent_lines = SENT_TEXT.read_text(encoding="utf-8").splitlines()
    review_lines = REVIEW_TEXT.read_text(encoding="utf-8").splitlines()
    wislim_lines = WISLIM_TEXT.read_text(encoding="utf-8").split("\n")
    known_literature = set(literature_index(data))
    known_ids = set(expected) | set(expected_fixes)
    seen_titles: set[str] = set()

    for topic in topics:
        tid = topic.get("id", "<missing>")
        for field in REQUIRED_TOPIC_FIELDS:
            if field not in topic:
                errors.append(f"{tid}: missing field {field}")
        if topic.get("title") in seen_titles:
            errors.append(f"{tid}: duplicate title")
        seen_titles.add(topic.get("title"))
        if topic.get("kind") not in KINDS:
            errors.append(f"{tid}: unknown kind {topic.get('kind')!r}")
        if not topic.get("quotes"):
            errors.append(f"{tid}: has no quotation from the reply")
        check_quote_lines(errors, f"{tid} reply", topic.get("quotes", []), reply_lines)
        check_quote_lines(errors, f"{tid} reply", topic.get("reply_evidence", []), reply_lines)
        check_quote_lines(errors, f"{tid} sent", topic.get("sent_evidence", []), sent_lines)
        check_quote_lines(errors, f"{tid} review", topic.get("review_evidence", []), review_lines)
        check_quote_lines(
            errors, f"{tid} WISLIM", topic.get("wislim_source", []), wislim_lines, span=20, passage=True
        )
        for issue_id in topic.get("audit_records", []):
            if audit_record(issue_id) is None:
                errors.append(f"{tid}: unknown audit record {issue_id}")
        for key in topic.get("literature", []):
            if key not in known_literature:
                errors.append(f"{tid}: unknown literature key {key}")
        for other in topic.get("related", []):
            if other == tid or other not in known_ids:
                errors.append(f"{tid}: bad related ID {other!r}")
    for item in corrections:
        cid = item.get("id", "<missing>")
        for field in REQUIRED_CORRECTION_FIELDS:
            if field not in item:
                errors.append(f"{cid}: missing field {field}")
        for rel in item.get("files", []):
            if not (ROOT / rel).exists():
                errors.append(f"{cid}: listed file does not exist: {rel}")
    for item in data.get("forward", []):
        check_quote_lines(errors, "forward", [item], reply_lines)
    return errors


def check_privacy(paths: list[Path]) -> list[str]:
    """Reject any email address or telephone number in the correspondence records."""
    errors: list[str] = []
    for path in paths:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if EMAIL_RE.search(text):
            errors.append(f"{repo_path(path)}: contains an email address")
        if PHONE_RE.search(text):
            errors.append(f"{repo_path(path)}: contains a telephone number")
    return errors


def privacy_paths(data: dict[str, Any]) -> list[Path]:
    paths = sorted(CORRESPONDENCE.glob("*")) + [
        MODEL,
        CORRECTIONS,
        INDEX,
        REVIEW_DIR / "response-email.md",
    ]
    paths += [topic_path(topic) for topic in data["topics"]]
    return paths


def status_note() -> list[str]:
    return [
        "> **Status: audit observation, not a required fix.** This is a tracked note on one",
        "> claim in a reply. It is not a verdict on anyone's character, and the sender may",
        "> decline the suggested step with reasons. Comments on the matching issue are welcome.",
    ]


def render_quotes(label: str, rel: str, items: list[dict[str, Any]]) -> list[str]:
    lines: list[str] = []
    for item in items:
        lines += [
            f"- [`{label}:{item['line']}`]({blob_url(rel, item['line'])})",
            f"  > {item['quote']}",
        ]
    return lines


def render_topic(
    topic: dict[str, Any],
    data: dict[str, Any],
    issues: dict[str, dict[str, Any]],
    numbers_as_links: bool = False,
) -> str:
    reply_rel = data["reply"]["source_text"]
    review_rel = "reviews/oph-lfdi-57/source/LFDI_Alignment_Audit-57.verified.txt"
    number = issues.get(topic["id"], {}).get("number", "")
    lines = [
        "---",
        f"id: {topic['id']}",
        "review: OPH-LFDI-57",
        "kind: reply-topic",
        "status: observation",
        f"claim_kind: {topic['kind']}",
        f"reply_lines: [{', '.join(str(item['line']) for item in topic['quotes'])}]",
        f"github_issue: {number}",
        f"related: [{', '.join(topic['related'])}]",
        "---",
        "",
        f"# {topic['id']}: {topic['title']}",
        "",
    ]
    lines += status_note()
    lines += ["", "## The reply says", ""]
    for item in topic["quotes"]:
        lines += [
            f"> {item['quote']}",
            ">",
            f"> — [`{reply_rel}:{item['line']}`]({blob_url(reply_rel, item['line'])})",
            "",
        ]
    lines += ["## Summary", "", topic["summary"].strip(), "", "## Assessment", ""]
    for paragraph in topic["assessment"]:
        lines += [paragraph.strip(), ""]
    lines += [f"**Kind of claim:** `{topic['kind']}`: {KINDS[topic['kind']]}.", "", "## Evidence", ""]
    evidence: list[str] = []
    if topic["oph_evidence"]:
        evidence += ["**OPH, at the pinned upstream commit**", ""]
        for item in topic["oph_evidence"]:
            evidence += [f"- [`{item['path']}:{item['line']}`]({oph_url(item)})", f"  > {item['quote']}"]
        evidence.append("")
    if topic["sent_evidence"]:
        evidence += ["**The response as sent**", ""]
        evidence += render_quotes(
            "02-friedman-response-as-sent.txt", data["reply"]["response_text"], topic["sent_evidence"]
        )
        evidence.append("")
    if topic.get("reply_evidence"):
        evidence += ["**Elsewhere in the reply**", ""]
        evidence += render_quotes("03-wishengrad-reply.txt", reply_rel, topic["reply_evidence"])
        evidence.append("")
    if topic["review_evidence"]:
        evidence += ["**The one-page review**", ""]
        evidence += render_quotes("LFDI_Alignment_Audit-57.verified.txt", review_rel, topic["review_evidence"])
        evidence.append("")
    if topic["wislim_source"]:
        evidence += ["**WISLIM v2.0.1**", ""]
        evidence += render_quotes("source/WISLIM-v2.0.1.txt", "source/WISLIM-v2.0.1.txt", topic["wislim_source"])
        evidence.append("")
    if topic["audit_records"]:
        evidence += ["**Related audit records**", ""]
        for issue_id in topic["audit_records"]:
            record = audit_record(issue_id)
            assert record is not None
            evidence.append(f"- [`{issue_id}`]({blob_url(repo_path(record))})")
        evidence.append("")
    if topic["literature"]:
        evidence += ["**Literature**", ""]
        index = literature_index(data)
        for key in topic["literature"]:
            item = index[key]
            evidence.append(f"- {item['citation']} [Link]({item['url']})")
        evidence.append("")
    if not evidence:
        evidence = ["- The claim is checked against the sources named above.", ""]
    lines += evidence
    lines += ["## What would move this forward", "", topic["response"].strip(), "", "## Related", ""]
    for other in topic["related"]:
        link = issues.get(other, {}).get("number") if numbers_as_links else None
        lines.append(f"- #{link} (`{other}`)" if link else f"- `{other}`")
    lines += [
        "",
        "## Tracking",
        "",
        "This record is generated. The canonical source is",
        "`reviews/oph-lfdi-57/model/reply.json`; regenerate with `make reply`.",
        "",
    ]
    return "\n".join(lines)


def render_index(data: dict[str, Any], issues: dict[str, dict[str, Any]]) -> str:
    reply = data["reply"]
    repository, commit = oph_pin()
    lines = [
        f"# {reply['title']}",
        "",
        f"Received {reply['received']}. The verbatim text is in",
        "[`../correspondence/03-wishengrad-reply.txt`](../correspondence/03-wishengrad-reply.txt),",
        "one paragraph per line. Each record below takes one claim and quotes it exactly.",
        "These are observations, and the sender may answer or decline any of them.",
        "",
        f"OPH evidence is pinned to `{repository}` at `{commit}`.",
        "",
        "## Voices in the reply",
        "",
        "| Lines | Voice | Detail |",
        "|---|---|---|",
    ]
    for voice in reply["voices"]:
        lines.append(f"| {voice['lines']} | {voice['name']} | {voice['detail']} |")
    lines += [
        "",
        "## Records",
        "",
        "| ID | Issue | Claim | Kind | Line |",
        "|---|---|---|---|---|",
    ]
    for topic in data["topics"]:
        entry = issues.get(topic["id"], {})
        issue = f"[#{entry['number']}]({entry['url']})" if entry else "—"
        lines.append(
            f"| [{topic['id']}]({topic_path(topic).name}) | {issue} | {topic['title']} "
            f"| `{topic['kind']}` | {topic['quotes'][0]['line']} |"
        )
    lines += ["", "## Where the reply moves the exchange forward", ""]
    for item in data["forward"]:
        lines.append(f"- \"{item['quote']}\" (line {item['line']}). {item['note']}")
    lines += ["", "## Open requests", ""]
    for index, item in enumerate(data["open_requests"], 1):
        lines.append(f"{index}. {item}")
    lines += ["", "## Literature", ""]
    for item in data["literature"]:
        lines.append(f"- {item['citation']} [Link]({item['url']}) *{item['checked']}*")
    lines += [
        "",
        "## Corrections to this tracker",
        "",
        "Reading the reply against the sources found errors on this side too. They are",
        "listed in [`../corrections.md`](../corrections.md).",
        "",
        "## Tracked files",
        "",
        "`reviews/oph-lfdi-57/model/reply.json` is canonical. This index and the records are",
        "generated by `make reply`; do not edit them by hand. `make reply-issues` mirrors them to",
        "GitHub, and issue bodies should not be edited there; comments are for discussion.",
        "",
    ]
    return "\n".join(lines)


def render_correction(item: dict[str, Any]) -> list[str]:
    affected = "Yes." if item["sent_email"] else "No."
    lines = [
        f"**Affects the email sent 2026-11-03:** {affected}",
        "",
        "**What was wrong.** " + item["what_was_wrong"].strip(),
        "",
        "**What changed.** " + item["what_changed"].strip(),
        "",
        "**Files.** " + ", ".join(f"`{rel}`" for rel in item["files"]),
    ]
    if item.get("fixed_in"):
        lines += ["", f"**Fixed in.** `{item['fixed_in']}`"]
    return lines


def render_corrections(data: dict[str, Any], issues: dict[str, dict[str, Any]]) -> str:
    lines = [
        "# Corrections to the OPH/LFDI tracker",
        "",
        "Errors found in this tracker, what changed, and whether the email of 2026-11-03",
        "carried them. The IDs are stable. The email stays as sent; see",
        "[`response-email.md`](response-email.md).",
        "",
        "| ID | Issue | Correction | In the sent email |",
        "|---|---|---|---|",
    ]
    for item in data["corrections"]:
        entry = issues.get(item["id"], {})
        issue = f"[#{entry['number']}]({entry['url']})" if entry else "—"
        anchor = slugify(f"{item['id']} {item['title']}", limit=200)
        lines.append(
            f"| [{item['id']}](#{anchor}) | {issue} | {item['title']} "
            f"| {'yes' if item['sent_email'] else 'no'} |"
        )
    lines.append("")
    for item in data["corrections"]:
        lines += [f"## {item['id']}: {item['title']}", ""]
        lines += render_correction(item)
        lines.append("")
    lines += [
        "`reviews/oph-lfdi-57/model/reply.json` is canonical; regenerate this file with `make reply`.",
        "",
    ]
    return "\n".join(lines)


def render_ledger(ledger: dict[str, Any]) -> str:
    lines = [
        "# Correspondence ledger",
        "",
        ledger["summary"],
        "",
        "| # | Sent (UTC) | From | Content | Record |",
        "|---|---|---|---|---|",
    ]
    for message in ledger["messages"]:
        record = message["record"]
        link = f"[`{record['label']}`]({record['href']})" if record else "—"
        lines.append(
            f"| {message['n']} | {message['sent']} | {message['from']} | {message['content']} | {link} |"
        )
    lines += ["", "## Privacy", "", ledger["privacy"], "", "## Recorded texts", ""]
    lines += ["| File | SHA-256 | Lines | Normalization |", "|---|---|---|---|"]
    for name, info in ledger["files"].items():
        lines.append(f"| [`{name}`]({name}) | `{info['sha256']}` | {info['lines']} | {info['normalization']} |")
    lines += ["", "`metadata.json` is canonical; regenerate this file with `make reply`.", ""]
    return "\n".join(lines)


def outputs(data: dict[str, Any]) -> dict[Path, str]:
    issues = load_issue_map()
    files = {INDEX: render_index(data, issues), CORRECTIONS: render_corrections(data, issues)}
    for topic in data["topics"]:
        files[topic_path(topic)] = render_topic(topic, data, issues)
    files[LEDGER] = render_ledger(load_json(LEDGER_DATA))
    return files


def write_all(data: dict[str, Any]) -> None:
    RECORDS.mkdir(parents=True, exist_ok=True)
    for path, text in outputs(data).items():
        path.write_text(text, encoding="utf-8")


def check_all(data: dict[str, Any]) -> list[str]:
    errors = check_model(data)
    for path, text in outputs(data).items():
        if not path.is_file():
            errors.append(f"missing {repo_path(path)}; run make reply")
        elif path.read_text(encoding="utf-8") != text:
            errors.append(f"{repo_path(path)} is out of date; run make reply")
    errors += check_privacy(privacy_paths(data))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify generated files without writing")
    args = parser.parse_args(argv)
    data = load_model()
    if args.check:
        errors = check_all(data)
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        if errors:
            return 1
        print(f"OK: {len(data['topics'])} reply topics and {len(data['corrections'])} corrections are current")
        return 0
    write_all(data)
    print(f"wrote {len(data['topics'])} reply topics, the reply index, corrections.md, and the ledger")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
