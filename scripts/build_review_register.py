#!/usr/bin/env python3
"""Build the tracked review register for the OPH/LFDI review.

The review is a one-page image PDF. Its OCR text is the citation base. Each
distinct claim becomes one topic record under ``reviews/oph-lfdi-57/topics/``
and one row in the generated review index.

Usage:

    python3 scripts/build_review_register.py
    python3 scripts/build_review_register.py --check

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
MODEL = REVIEW_DIR / "model" / "review.json"
TOPICS = REVIEW_DIR / "topics"
INDEX = REVIEW_DIR / "README.md"
DOCS_REVIEWS = ROOT / "docs" / "reviews.md"
DOCS_REVIEW_DIR = ROOT / "docs" / "reviews" / "oph-lfdi-57"
DOCS_TOPICS = DOCS_REVIEW_DIR / "topics"
DOCS_INDEX = DOCS_REVIEW_DIR / "README.md"
SOURCE = REVIEW_DIR / "source"
METADATA = SOURCE / "metadata.json"
REVIEW_TEXT = SOURCE / "LFDI_Alignment_Audit-57.txt"
REVIEW_PDF = SOURCE / "LFDI_Alignment_Audit-57.pdf"
WISLIM_URL = "https://github.com/docxology/WISLIM-audit/blob/main"
TOPIC_COUNT = 12

VERDICTS = {
    "valid": "supported as stated",
    "partly-valid": "partly supported; part is overstated or under-specified",
    "unsupported": "the review does not supply enough argument or evidence",
    "question-begging": "the conclusion depends on a premise the review does not defend",
    "out-of-scope": "the claim applies a norm or method the target does not purport to use",
    "unverifiable": "the claim cannot be checked from the available materials",
}
OPH_STATUSES = {
    "addressed": "OPH discusses the topic and the review's point is at least partly acknowledged",
    "refuted": "OPH's stated position contradicts the review's claim",
    "not-addressed": "OPH does not discuss the review's specific claim",
    "unverifiable": "the OPH response cannot be determined from the available sources",
}
REQUIRED_TOPIC_FIELDS = (
    "id",
    "title",
    "review_quote",
    "review_line",
    "verdict",
    "oph_status",
    "summary",
    "intrinsic",
    "extrinsic",
    "oph_evidence",
    "wislim_evidence",
    "response",
    "tags",
    "related",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def slugify(text: str, limit: int = 72) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    if len(text) <= limit:
        return text
    cut = text[:limit]
    if "-" in cut:
        cut = cut.rsplit("-", 1)[0]
    return cut.rstrip("-")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_model() -> dict[str, Any]:
    with MODEL.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_metadata() -> dict[str, Any]:
    with METADATA.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_lines() -> list[str]:
    return REVIEW_TEXT.read_text(encoding="utf-8").splitlines()


def topic_path(topic: dict[str, Any]) -> Path:
    return TOPICS / f"{topic['id']}-{slugify(topic['title'])}.md"


def window(lines: list[str], line: int, before: int = 0, after: int = 1) -> str:
    return "\n".join(lines[max(0, line - 1 - before) : line + after])


def check_model(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    review = data.get("review")
    if not isinstance(review, dict):
        return ["review metadata is missing"]
    topics = data.get("topics")
    if not isinstance(topics, list):
        return ["topics must be a list"]
    if len(topics) != TOPIC_COUNT:
        errors.append(f"expected {TOPIC_COUNT} topics, found {len(topics)}")
    expected_ids = [f"OPH-REV-{index:03d}" for index in range(1, TOPIC_COUNT + 1)]
    actual_ids = [topic.get("id") for topic in topics]
    if actual_ids != expected_ids:
        errors.append("topic IDs are not the stable sequence OPH-REV-001..012")

    metadata = load_metadata()
    if metadata.get("pdf_sha256") != sha256(REVIEW_PDF):
        errors.append("review PDF hash does not match metadata")
    if metadata.get("text_sha256") != sha256(REVIEW_TEXT):
        errors.append("review text hash does not match metadata")
    lines = load_lines()
    seen_titles: set[str] = set()
    known_ids = set(expected_ids)
    for topic in topics:
        tid = topic.get("id", "<missing>")
        for field in REQUIRED_TOPIC_FIELDS:
            if field not in topic:
                errors.append(f"{tid}: missing field {field}")
        if not isinstance(topic.get("title"), str) or not topic["title"].strip():
            errors.append(f"{tid}: title is empty")
        if topic.get("title") in seen_titles:
            errors.append(f"{tid}: duplicate title")
        seen_titles.add(topic.get("title"))
        if topic.get("verdict") not in VERDICTS:
            errors.append(f"{tid}: unknown verdict {topic.get('verdict')!r}")
        if topic.get("oph_status") not in OPH_STATUSES:
            errors.append(f"{tid}: unknown OPH status {topic.get('oph_status')!r}")
        line = topic.get("review_line")
        if not isinstance(line, int) or not 1 <= line <= len(lines):
            errors.append(f"{tid}: review_line is out of bounds")
            continue
        quote = str(topic.get("review_quote", "")).strip()
        if len(quote) < 20:
            errors.append(f"{tid}: review_quote is too short")
        if normalize(quote) not in normalize(window(lines, line)):
            errors.append(f"{tid}: review_quote does not appear at line {line}")
        for field in ("summary", "intrinsic", "extrinsic", "response"):
            if not str(topic.get(field, "")).strip():
                errors.append(f"{tid}: {field} is empty")
        for field in ("oph_evidence", "wislim_evidence"):
            evidence = topic.get(field)
            if not isinstance(evidence, list):
                errors.append(f"{tid}: {field} must be a list")
                continue
            for index, item in enumerate(evidence):
                if not isinstance(item, dict):
                    errors.append(f"{tid}: {field}[{index}] is not an object")
                    continue
                for key in ("path", "line", "quote"):
                    if key not in item:
                        errors.append(f"{tid}: {field}[{index}] missing {key}")
                if not isinstance(item.get("line"), int) or item.get("line", 0) < 1:
                    errors.append(f"{tid}: {field}[{index}].line is not positive")
                if len(str(item.get("quote", "")).strip()) < 10:
                    errors.append(f"{tid}: {field}[{index}].quote is too short")
                if field == "wislim_evidence":
                    evidence_path = ROOT / str(item.get("path", ""))
                    if not evidence_path.is_file():
                        errors.append(f"{tid}: missing WISLIM evidence {item.get('path')}")
                        continue
                    evidence_lines = evidence_path.read_text(encoding="utf-8").splitlines()
                    quote_line = item.get("line")
                    if isinstance(quote_line, int) and 1 <= quote_line <= len(evidence_lines):
                        evidence_window = window(evidence_lines, quote_line, before=2, after=1)
                        if normalize(str(item.get("quote", ""))) not in normalize(evidence_window):
                            errors.append(
                                f"{tid}: WISLIM evidence quote not found at "
                                f"{item.get('path')}:{quote_line}"
                            )
        related = topic.get("related", [])
        if not isinstance(related, list):
            errors.append(f"{tid}: related must be a list")
        else:
            for other in related:
                if other == tid:
                    errors.append(f"{tid}: related contains itself")
                if other not in known_ids:
                    errors.append(f"{tid}: related contains unknown ID {other!r}")
    return errors


def external_evidence_url(review: dict[str, Any], item: dict[str, Any]) -> str:
    commit = review["oph_commit"]
    return (
        f"https://github.com/docxology/observer-patch-holography/blob/"
        f"{commit}/{item['path']}#L{item['line']}"
    )


def render_topic(topic: dict[str, Any], review: dict[str, Any]) -> str:
    tags = ", ".join(topic["tags"])
    related = ", ".join(topic["related"]) or "none"
    lines = [
        "---",
        f"id: {topic['id']}",
        f"review: {review['id']}",
        "kind: review-topic",
        "status: observation",
        f"verdict: {topic['verdict']}",
        f"oph_status: {topic['oph_status']}",
        f"review_line: {topic['review_line']}",
        f"tags: [{tags}]",
        f"related: [{related}]",
        "---",
        "",
        f"# {topic['id']}: {topic['title']}",
        "",
        f"> **Review claim:** {VERDICTS[topic['verdict']]}  ",
        f"> **OPH response:** {OPH_STATUSES[topic['oph_status']]}  ",
        f"> **Review source:** `reviews/oph-lfdi-57/source/"
        f"LFDI_Alignment_Audit-57.txt:{topic['review_line']}`",
        "",
        "> **Status: audit observation, not a required fix.** This is a tracked",
        "> review note, not a verdict that OPH is invalid or that anyone must",
        "> change the paper. The sender may decline the response with reasons.",
        "",
        "## Review claim",
        "",
        f"> {topic['review_quote']}",
        ">",
        f"> — `reviews/oph-lfdi-57/source/LFDI_Alignment_Audit-57.txt:{topic['review_line']}`",
        "",
        "## Intrinsic assessment",
        "",
        topic["intrinsic"].strip(),
        "",
        "## Extrinsic assessment",
        "",
        topic["extrinsic"].strip(),
        "",
        "## OPH evidence",
        "",
    ]
    if topic["oph_evidence"]:
        for item in topic["oph_evidence"]:
            lines += [
                f"- [`{item['path']}:{item['line']}`]({external_evidence_url(review, item)})",
                f"  > {item['quote']}",
            ]
    else:
        lines.append("- No OPH statement addresses this claim directly.")
    lines += ["", "## WISLIM evidence", ""]
    if topic["wislim_evidence"]:
        for item in topic["wislim_evidence"]:
            url = f"{WISLIM_URL}/{item['path']}#L{item['line']}"
            lines += [
                f"- [`{item['path']}:{item['line']}`]({url})",
                f"  > {item['quote']}",
            ]
    else:
        lines.append("- No WISLIM audit record bears on this point.")
    lines += [
        "",
        "## Summary",
        "",
        topic["summary"].strip(),
        "",
        "## Suggested response",
        "",
        topic["response"].strip(),
        "",
        "## Related topics",
        "",
    ]
    if topic["related"]:
        for other in topic["related"]:
            lines.append(f"- `{other}`")
    else:
        lines.append("- None.")
    lines += [
        "",
        "## Tracking",
        "",
        f"This topic is part of review `{review['id']}`. The canonical record is",
        "`reviews/oph-lfdi-57/model/review.json`; regenerate with `make review`.",
        "",
    ]
    return "\n".join(lines)


def render_index(data: dict[str, Any], audit_prefix: str = "") -> str:
    review = data["review"]
    topics = data["topics"]
    lines = [
        "# OPH/LFDI review tracker",
        "",
        f"This directory tracks the review **{review['title']}** received",
        f"{review['received']}. The review is a one-page image-only PDF. Its OCR",
        "text is the citation base; the PDF has no text layer, so equations and",
        "subscript markers may be inexact.",
        "",
        f"- **Target:** {review['target']}",
        f"- **Target record:** {review['target_url']}",
        f"- **OPH repository:** {review['oph_repository']}",
        f"- **OPH commit:** `{review['oph_commit']}`",
        f"- **Source PDF:** `{review['source_pdf']}`",
        f"- **Source text:** `{review['source_text']}`",
        f"- **Topics:** {len(topics)}",
        "",
        "## How to read this tracker",
        "",
        "Each topic records one distinct claim in the review. **Review claim**",
        "grades the claim's intrinsic support. **OPH response** records whether",
        "OPH addresses it, contradicts it, or is silent. These are observations,",
        "not a finding that OPH is invalid or that a change is required.",
        "",
        "| ID | Topic | Review claim | OPH response |",
        "|---|---|---|---|",
    ]
    for topic in topics:
        lines.append(
            f"| [{topic['id']}](topics/{topic_path(topic).name}) "
            f"| {topic['title']} | {topic['verdict']} | {topic['oph_status']} |"
        )
    lines += [
        "",
        "## Audits and response",
        "",
        f"- [Intrinsic audit]({audit_prefix}intrinsic-audit.md): logic, definitions, evidence,",
        "  and provenance internal to the review.",
        f"- [Extrinsic audit]({audit_prefix}extrinsic-audit.md): the review against OPH's",
        "  statements and against the WISLIM audit.",
        f"- [Response email draft]({audit_prefix}response-email.md): short reply with a plaintext",
        "  public URL. Not sent.",
        "",
        "## Tracked files",
        "",
        "- `reviews/oph-lfdi-57/model/review.json` is canonical; edit it, then run `make review`.",
        "- `topics/*.md` and this index are generated; do not edit them by hand.",
        "- `reviews/oph-lfdi-57/source/` holds the received PDF, its normalized OCR text, and metadata.",
        "",
        "## Rights",
        "",
        "The review is reproduced as received for audit and response. It is not",
        "relicensed. The OPH quotations are short citations from the public OPH",
        "repository at the recorded commit.",
        "",
    ]
    return "\n".join(lines)


def render_docs_reviews(data: dict[str, Any]) -> str:
    review = data["review"]
    topics = data["topics"]
    addressed = [t for t in topics if t["oph_status"] == "addressed"]
    refuted = [t for t in topics if t["oph_status"] == "refuted"]
    not_addressed = [t for t in topics if t["oph_status"] == "not-addressed"]
    lines = [
        "# External reviews and responses",
        "",
        "This index tracks external reviews and critiques received in connection",
        "with the WISLIM audit and related research programs, decomposed into",
        "source-anchored, modular topic records under `docs/reviews/` and",
        "`reviews/`.",
        "",
        f"## `{review['id']}` — {review['title']}",
        "",
        f"- **Received:** {review['received']}",
        f"- **Format:** {review['review_type']}",
        f"- **Target:** {review['target']} ({review['target_url']})",
        f"- **External verification corpus:** `{review['oph_repository']}` at commit `{review['oph_commit']}`",
        f"- **Source PDF:** [`{review['source_pdf']}`](../{review['source_pdf']})",
        f"- **Source OCR text:** [`{review['source_text']}`](../{review['source_text']})",
        "- **Canonical model:** [`reviews/oph-lfdi-57/model/review.json`](../reviews/oph-lfdi-57/model/review.json)",
        "- **Intrinsic audit:** [`reviews/oph-lfdi-57/intrinsic-audit.md`](../reviews/oph-lfdi-57/intrinsic-audit.md)",
        "- **Extrinsic audit:** [`reviews/oph-lfdi-57/extrinsic-audit.md`](../reviews/oph-lfdi-57/extrinsic-audit.md)",
        "- **Response email draft:** [`reviews/oph-lfdi-57/response-email.md`](../reviews/oph-lfdi-57/response-email.md)",
        f"- **Tracked topics:** {len(topics)} (`OPH-REV-001`–`OPH-REV-012`)",
        f"  - **Addressed by OPH:** {len(addressed)}",
        f"  - **Refuted by OPH:** {len(refuted)}",
        f"  - **Not addressed (external LFDI stipulations / provenance):** {len(not_addressed)}",
        "",
        "### Topic register (`OPH-REV-001`–`OPH-REV-012`)",
        "",
        "| ID | Topic | Intrinsic verdict | OPH disposition | Summary |",
        "|---|---|---|---|---|",
    ]
    for topic in topics:
        fname = topic_path(topic).name
        lines.append(
            f"| [{topic['id']}](reviews/oph-lfdi-57/topics/{fname}) "
            f"| {topic['title']} | `{topic['verdict']}` | `{topic['oph_status']}` "
            f"| {topic['summary']} |"
        )
    lines += [
        "",
        "### Topics addressed by OPH",
        "",
    ]
    for topic in addressed:
        fname = topic_path(topic).name
        lines.append(
            f"- **[`{topic['id']}`](reviews/oph-lfdi-57/topics/{fname}) — {topic['title']}** "
            f"(`{topic['verdict']}`): {topic['summary']}"
        )
    lines += [
        "",
        "### Topics refuted by OPH",
        "",
    ]
    for topic in refuted:
        fname = topic_path(topic).name
        lines.append(
            f"- **[`{topic['id']}`](reviews/oph-lfdi-57/topics/{fname}) — {topic['title']}** "
            f"(`{topic['verdict']}`): {topic['summary']}"
        )
    lines += [
        "",
        "### Topics not addressed by OPH (external LFDI stipulations or provenance)",
        "",
    ]
    for topic in not_addressed:
        fname = topic_path(topic).name
        lines.append(
            f"- **[`{topic['id']}`](reviews/oph-lfdi-57/topics/{fname}) — {topic['title']}** "
            f"(`{topic['verdict']}`): {topic['summary']}"
        )
    lines.append("")
    return "\n".join(lines)


def docs_topic_path(topic: dict[str, Any]) -> Path:
    return DOCS_TOPICS / f"{topic['id']}-{slugify(topic['title'])}.md"


def write_all(data: dict[str, Any]) -> None:
    TOPICS.mkdir(parents=True, exist_ok=True)
    DOCS_TOPICS.mkdir(parents=True, exist_ok=True)
    review = data["review"]
    for topic in data["topics"]:
        rendered = render_topic(topic, review)
        topic_path(topic).write_text(rendered, encoding="utf-8")
        docs_topic_path(topic).write_text(rendered, encoding="utf-8")
    INDEX.write_text(render_index(data), encoding="utf-8")
    DOCS_INDEX.write_text(
        render_index(data, audit_prefix="../../../reviews/oph-lfdi-57/"),
        encoding="utf-8",
    )
    DOCS_REVIEWS.write_text(render_docs_reviews(data), encoding="utf-8")


def check_all(data: dict[str, Any]) -> list[str]:
    errors = check_model(data)
    review = data["review"]
    for topic in data["topics"]:
        expected = render_topic(topic, review)
        for path in (topic_path(topic), docs_topic_path(topic)):
            if not path.is_file():
                errors.append(f"{topic['id']}: missing {path.relative_to(ROOT)}")
                continue
            if path.read_text(encoding="utf-8") != expected:
                errors.append(
                    f"{topic['id']}: {path.relative_to(ROOT)} is out of date; run make review"
                )
    if not INDEX.is_file():
        errors.append("review index is missing; run make review")
    elif INDEX.read_text(encoding="utf-8") != render_index(data):
        errors.append("review index is out of date; run make review")
    expected_docs_index = render_index(
        data, audit_prefix="../../../reviews/oph-lfdi-57/"
    )
    if not DOCS_INDEX.is_file():
        errors.append("docs review index is missing; run make review")
    elif DOCS_INDEX.read_text(encoding="utf-8") != expected_docs_index:
        errors.append("docs review index is out of date; run make review")
    expected_docs_reviews = render_docs_reviews(data)
    if not DOCS_REVIEWS.is_file():
        errors.append("docs/reviews.md is missing; run make review")
    elif DOCS_REVIEWS.read_text(encoding="utf-8") != expected_docs_reviews:
        errors.append("docs/reviews.md is out of date; run make review")
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
        print(f"OK: {len(data['topics'])} review topics and indexes are current")
        return 0
    write_all(data)
    print(
        f"wrote {len(data['topics'])} review topics, reviews/oph-lfdi-57/README.md, "
        "docs/reviews/oph-lfdi-57/README.md, and docs/reviews.md"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
