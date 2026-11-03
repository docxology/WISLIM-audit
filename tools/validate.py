#!/usr/bin/env python3
"""Validate the WISLIM-audit repository.

The validator is intentionally dependency-free. It checks:

- the source PDF and text hashes against ``source/metadata.json``;
- the source line and word counts;
- the stable claim IDs, required fields, line bounds, and anchor text;
- the 210-row stress-test catalog and its summary counts;
- every explicit source-line citation is within bounds;
- required audit, red-team, and evidence modules exist;
- the 66-issue register, its Markdown records, and the GitHub issue map agree;
- relative Markdown links resolve.

Run from the repository root:

    python3 tools/validate.py
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SOURCE_PDF = ROOT / "source" / "WISLIM-v2.0.1.pdf"
SOURCE_TXT = ROOT / "source" / "WISLIM-v2.0.1.txt"
METADATA = ROOT / "source" / "metadata.json"
CLAIMS = ROOT / "model" / "claims.json"
STRESS = ROOT / "model" / "stress-tests.json"

CLAIM_IDS = [f"C{i:02d}" for i in range(1, 36)]
STRESS_IDS = [f"ST{i:03d}" for i in range(1, 211)]
CLAIM_VERDICTS = {
    "ambiguous",
    "circular/equivocal",
    "coercive/unfalsifiable",
    "dangerous",
    "decorative",
    "false",
    "harmful",
    "inconsistent",
    "internally-inconsistent",
    "invalid",
    "invalid-as-proof",
    "methodologically-invalid",
    "non-evidence",
    "non-sequitur",
    "overbroad",
    "overclaim",
    "overinclusive",
    "plausible",
    "self-undermining",
    "tension",
    "underspecified/dangerous",
    "unfalsifiable",
    "unsupported",
    "unverifiable",
    "valid-but-insufficient",
}
SEVERITIES = {"critical", "high", "medium", "low"}
STRESS_VERDICTS = {
    "category-error",
    "empirical-unsupported",
    "false",
    "heuristic",
    "misapplied-formalism",
    "non-sequitur",
    "rhetorical",
    "valid-but-insufficient",
}
REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "LICENSE",
    "CITATION.cff",
    "pyproject.toml",
    "source/README.md",
    "source/metadata.json",
    "source/WISLIM-v2.0.1.pdf",
    "source/WISLIM-v2.0.1.txt",
    "model/claims.json",
    "model/stress-tests.json",
    "model/issues.json",
    "model/issue-map.json",
    "tools/build_stress_catalog.py",
    "tools/validate.py",
    "scripts/build_issue_register.py",
    "scripts/build_review_register.py",
    "scripts/sync_issues.py",
    "tests/test_repository.py",
    "Makefile",
    ".github/workflows/verify.yml",
    "docs/audit/README.md",
    "docs/reviews.md",
    "docs/reviews/oph-lfdi-57/README.md",
    "docs/method.md",
    "docs/glossary.md",
    "docs/reproducibility.md",
    "docs/claims.md",
    "docs/stress-tests.md",
    "reviews/oph-lfdi-57/README.md",
    "reviews/oph-lfdi-57/intrinsic-audit.md",
    "reviews/oph-lfdi-57/extrinsic-audit.md",
    "reviews/oph-lfdi-57/response-email.md",
    "reviews/oph-lfdi-57/source/LFDI_Alignment_Audit-57.pdf",
    "reviews/oph-lfdi-57/source/LFDI_Alignment_Audit-57.txt",
    "reviews/oph-lfdi-57/source/metadata.json",
    "reviews/oph-lfdi-57/model/review.json",
    "reviews/oph-lfdi-57/verification.md",
    "evidence/README.md",
    "evidence/provenance.md",
    "evidence/philpapers.md",
    "evidence/citation-audit.md",
    "evidence/ai-letter-audit.md",
    "red-team/README.md",
    "red-team/threat-model.md",
    "red-team/adversarial-scenarios.md",
    "red-team/capture-and-gaming.md",
    "red-team/abuse-cases.md",
]
REQUIRED_FILES += [f"audit/{i:02d}-{name}.md" for i, name in enumerate([
    "verdict",
    "scope-and-method",
    "logical-form-and-ambiguity",
    "definition-of-life",
    "necessity-to-priority",
    "formula-e-infinity",
    "agency-and-life",
    "consensus-and-evidence",
    "formal-and-scientific-claims",
    "governance-and-oversight",
    "rhetoric-and-coercion",
    "citations-and-scholarship",
    "steelman",
    "failure-modes",
    "repair-roadmap",
])]

SOURCE_CITATION_RE = re.compile(r"source/WISLIM-v2\.0\.1\.txt:(\d+)")
REVIEW_CITATION_RE = re.compile(
    r"(?:reviews/oph-lfdi-57/source/)?LFDI_Alignment_Audit-57\.txt:(\d+)"
)
SHORTHAND_CITATION_RE = re.compile(r"`:(\d{1,5})`")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]*`")


class Validator:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.checks = 0
        self.warnings: list[str] = []

    def check(self, condition: bool, message: str) -> None:
        self.checks += 1
        if not condition:
            self.errors.append(message)

    def equal(self, actual: Any, expected: Any, message: str) -> None:
        self.check(actual == expected, f"{message}: expected {expected!r}, got {actual!r}")

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def check_source(v: Validator, metadata: dict[str, Any]) -> tuple[str, list[str]]:
    v.check(SOURCE_PDF.is_file(), "source PDF is missing")
    v.check(SOURCE_TXT.is_file(), "source text is missing")
    if not SOURCE_PDF.is_file() or not SOURCE_TXT.is_file():
        return "", []

    pdf_hash = sha256(SOURCE_PDF)
    text_hash = sha256(SOURCE_TXT)
    v.equal(pdf_hash, metadata["pdf_sha256"], "PDF SHA-256")
    v.equal(text_hash, metadata["text_sha256"], "text SHA-256")
    v.equal(SOURCE_PDF.stat().st_size, metadata["pdf_bytes"], "PDF byte size")

    text = SOURCE_TXT.read_text(encoding="utf-8")
    lines = text.split("\n")
    line_count = text.count("\n")
    v.equal(line_count, metadata["text_lines"], "text line count")
    v.equal(len(text.split()), metadata["text_words"], "text word count")
    v.equal(len(text.encode("utf-8")), metadata["text_bytes"], "text byte size")
    v.check(line_count > 0, "source text has no lines")
    v.check(
        text.endswith(("\n", "\f")),
        "source text should end with a newline or page break",
    )
    return text, lines


def check_claims(v: Validator, lines: list[str]) -> None:
    data = load_json(CLAIMS)
    v.check(isinstance(data, dict), "claims.json must be an object")
    claims = data.get("claims", [])
    v.equal(len(claims), 35, "claim count")
    v.equal([c.get("id") for c in claims], CLAIM_IDS, "claim IDs")
    seen: set[str] = set()
    for claim in claims:
        cid = claim.get("id", "<missing>")
        if cid in seen:
            v.errors.append(f"duplicate claim ID: {cid}")
        seen.add(cid)
        for key in (
            "id",
            "short",
            "anchor",
            "section",
            "line",
            "type",
            "role",
            "verdict",
            "severity",
            "summary",
            "dependencies",
            "repair",
        ):
            v.check(key in claim, f"{cid}: missing field {key}")
        line = claim.get("line")
        v.check(isinstance(line, int), f"{cid}: line must be an integer")
        if isinstance(line, int):
            v.check(1 <= line <= len(lines), f"{cid}: line {line} is out of bounds")
            anchor = normalize(str(claim.get("anchor", "")))
            window = normalize(
                "\n".join(lines[max(0, line - 3) : min(len(lines), line + 2)])
            )
            v.check(
                bool(anchor) and anchor in window,
                f"{cid}: anchor not found near line {line}",
            )
        v.check(
            claim.get("verdict") in CLAIM_VERDICTS,
            f"{cid}: unknown verdict {claim.get('verdict')!r}",
        )
        v.check(
            claim.get("severity") in SEVERITIES,
            f"{cid}: unknown severity {claim.get('severity')!r}",
        )
        deps = claim.get("dependencies", [])
        v.check(isinstance(deps, list), f"{cid}: dependencies must be a list")
        for dep in deps if isinstance(deps, list) else []:
            v.check(dep in CLAIM_IDS, f"{cid}: unknown dependency {dep!r}")


def check_stress(v: Validator) -> None:
    data = load_json(STRESS)
    v.check(isinstance(data, dict), "stress-tests.json must be an object")
    tests = data.get("tests", [])
    v.equal(len(tests), 210, "stress-test count")
    v.equal([t.get("id") for t in tests], STRESS_IDS, "stress-test IDs")
    v.equal([t.get("number") for t in tests], list(range(1, 211)), "stress-test numbers")
    verdicts = Counter()
    severities = Counter()
    titles: set[str] = set()
    for test in tests:
        tid = test.get("id", "<missing>")
        title = str(test.get("title", "")).strip()
        v.check(bool(title), f"{tid}: empty title")
        v.check(title not in titles, f"{tid}: duplicate title {title!r}")
        titles.add(title)
        verdict = test.get("verdict")
        severity = test.get("severity")
        v.check(verdict in STRESS_VERDICTS, f"{tid}: unknown verdict {verdict!r}")
        v.check(severity in SEVERITIES, f"{tid}: unknown severity {severity!r}")
        v.check(bool(str(test.get("note", "")).strip()), f"{tid}: empty note")
        verdicts[verdict] += 1
        severities[severity] += 1
    summary = data.get("audit_summary", {})
    v.equal(dict(verdicts), summary.get("verdict_counts"), "stress verdict counts")
    v.equal(dict(severities), summary.get("severity_counts"), "stress severity counts")


def load_register_module():
    path = ROOT / "scripts" / "build_issue_register.py"
    spec = importlib.util.spec_from_file_location("build_issue_register", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def normalize_passage(text: str) -> str:
    text = normalize(text)
    return re.sub(r"(?<=[A-Za-z0-9])-\s+(?=[A-Za-z])", "-", text)


def check_issue_register(v: Validator, lines: list[str]) -> None:
    register = load_register_module()
    issues = register.load_issues()
    for error in register.check_all(issues):
        v.check(False, f"issue register: {error}")

    v.equal(len(issues), 66, "issue count")
    v.equal(sum(1 for issue in issues if issue["kind"] == "claim"), 35, "claim issue count")
    v.equal(sum(1 for issue in issues if issue["kind"] == "red-team"), 20, "red-team issue count")
    v.equal(
        sum(1 for issue in issues if issue["kind"] == "workstream"),
        11,
        "workstream issue count",
    )
    data = load_json(ROOT / "model" / "issues.json")
    v.equal(data.get("counts", {}).get("total"), len(issues), "issue manifest total")
    v.equal(data.get("counts", {}).get("claims"), 35, "issue manifest claim count")
    v.equal(data.get("counts", {}).get("red_team"), 20, "issue manifest red-team count")
    v.equal(data.get("counts", {}).get("workstreams"), 11, "issue manifest workstream count")

    claims = {claim["id"]: claim for claim in load_json(CLAIMS)["claims"]}
    metadata = load_json(METADATA)
    for issue in issues:
        v.check(
            issue.get("status") == "observation",
            f"{issue['id']}: status is not 'observation'",
        )
        path = ROOT / issue["file"]
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for heading in (
            "## Publication reference",
            "## Primary quotations",
            "## Summary",
            "## Evidence",
            "## Proposed remediation",
            "## Suggested checks for reviewers",
            "## Tracking",
        ):
            v.check(
                heading in text,
                f"{issue['id']}: record is missing {heading}",
            )
        v.check(
            "## Required repair" not in text,
            f"{issue['id']}: record still uses the old required-repair heading",
        )
        v.check(
            "## Acceptance criteria" not in text,
            f"{issue['id']}: record still uses the old acceptance heading",
        )
        v.check(
            metadata["work"] in text,
            f"{issue['id']}: record is missing the publication title",
        )
        v.check(
            metadata["philpapers"]["doi"] in text,
            f"{issue['id']}: record is missing the publication DOI",
        )
        v.check(
            metadata["pdf_sha256"] in text,
            f"{issue['id']}: record is missing the PDF checksum",
        )
        v.check(
            "## Quoted passage" not in text,
            f"{issue['id']}: record still uses the singular quotation heading",
        )
        v.check(
            "**Status:** observation" in text,
            f"{issue['id']}: record does not mark the issue as an observation",
        )
        v.check(
            "status: observation" in text,
            f"{issue['id']}: frontmatter does not record status: observation",
        )
        v.check(
            "audit observation, not a required fix" in text,
            f"{issue['id']}: record does not say the issue is optional",
        )
        v.check(
            "does not mean the overall work fails" in text,
            f"{issue['id']}: record does not disclaim fatality",
        )
        v.check(
            "The manuscript resolves the defect" not in text,
            f"{issue['id']}: record still frames the issue as a required defect repair",
        )
        if issue["kind"] == "claim":
            v.check(
                "## Steelman and reply" in text,
                f"{issue['id']}: claim record is missing the steelman reply",
            )
            v.check(
                bool(str(issue.get("reply", "")).strip()),
                f"{issue['id']}: claim has no reply text",
            )
        v.check(
            "github_issue:" in text,
            f"{issue['id']}: record is missing the github_issue field",
        )
        quotes = issue.get("quotes")
        v.check(
            isinstance(quotes, list) and len(quotes) >= 1,
            f"{issue['id']}: record has no primary quotation",
        )
        quote_lines: list[int] = []
        for index, quote in enumerate(quotes if isinstance(quotes, list) else []):
            if not isinstance(quote, dict):
                continue
            qtext = str(quote.get("text", "")).strip()
            qline = quote.get("line")
            v.check(len(qtext) >= 25, f"{issue['id']}: quotes[{index}] is too short")
            v.check(
                isinstance(qline, int) and 1 <= qline <= len(lines),
                f"{issue['id']}: quotes[{index}].line is out of bounds",
            )
            if isinstance(qline, int) and 1 <= qline <= len(lines):
                quote_lines.append(qline)
                window = normalize_passage("\n".join(lines[qline - 1 : qline + 20]))
                v.check(
                    normalize_passage(qtext) in window,
                    f"{issue['id']}: quotations[{index}] does not appear at line {qline}",
                )
                v.check(
                    f"source/WISLIM-v2.0.1.txt:{qline}" in text,
                    f"{issue['id']}: quotations[{index}] has no line citation",
                )
        if issue["kind"] == "claim":
            claim = claims.get(issue["source_id"])
            v.check(claim is not None, f"{issue['id']}: no matching claim record")
            if claim:
                distance = (
                    min(abs(line - claim["line"]) for line in quote_lines)
                    if quote_lines
                    else 99
                )
                v.check(
                    distance <= 8,
                    f"{issue['id']}: no quotation starts within 8 lines of claim line {claim['line']}",
                )
                v.equal(issue["severity"], claim["severity"], f"{issue['id']}: severity")
                evidence_text = " ".join(issue["evidence"])
                v.check(
                    f"`{claim['verdict']}`" in evidence_text,
                    f"{issue['id']}: evidence does not carry verdict {claim['verdict']!r}",
                )

    mapping = register.load_map()
    v.equal(len(mapping), len(issues), "GitHub issue map entries")
    numbers = [entry.get("number") for entry in mapping.values()]
    v.check(
        all(isinstance(number, int) and number > 0 for number in numbers),
        "GitHub issue map numbers must be positive integers",
    )
    v.check(
        len(set(numbers)) == len(numbers),
        "GitHub issue map numbers must be unique",
    )
    for issue in issues:
        entry = mapping.get(issue["id"])
        if not isinstance(entry, dict):
            continue
        number = entry.get("number")
        v.check(
            isinstance(number, int)
            and entry.get("url", "").endswith(f"/issues/{number}"),
            f"{issue['id']}: GitHub issue URL does not match its number",
        )


def load_review_module():
    path = ROOT / "scripts" / "build_review_register.py"
    spec = importlib.util.spec_from_file_location("build_review_register", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_review_register(v: Validator) -> None:
    review_mod = load_review_module()
    data = review_mod.load_model()
    for error in review_mod.check_all(data):
        v.check(False, f"review register: {error}")

    topics = data.get("topics", [])
    v.equal(len(topics), 12, "review topic count")
    v.equal(
        [t.get("id") for t in topics],
        [f"OPH-REV-{index:03d}" for index in range(1, 13)],
        "review topic IDs",
    )
    v.equal(
        sum(1 for t in topics if t.get("oph_status") == "addressed"),
        3,
        "OPH addressed topic count",
    )
    v.equal(
        sum(1 for t in topics if t.get("oph_status") == "refuted"),
        4,
        "OPH refuted topic count",
    )
    v.equal(
        sum(1 for t in topics if t.get("oph_status") == "not-addressed"),
        5,
        "OPH not-addressed topic count",
    )
    for topic in topics:
        for path in (review_mod.topic_path(topic), review_mod.docs_topic_path(topic)):
            v.check(path.is_file(), f"{topic['id']}: missing {path.relative_to(ROOT)}")
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            for heading in (
                "## Review claim",
                "## Intrinsic assessment",
                "## Extrinsic assessment",
                "## OPH evidence",
                "## WISLIM evidence",
                "## Summary",
                "## Suggested response",
                "## Related topics",
                "## Tracking",
            ):
                v.check(
                    heading in text,
                    f"{topic['id']}: {path.relative_to(ROOT)} missing {heading}",
                )
            v.check(
                "status: observation" in text,
                f"{topic['id']}: {path.relative_to(ROOT)} missing status: observation",
            )


def iter_markdown() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts and "node_modules" not in path.parts
    )


def check_citations(v: Validator, line_count: int) -> None:
    review_line_count = 6
    for path in iter_markdown():
        text = path.read_text(encoding="utf-8")
        for match in SOURCE_CITATION_RE.finditer(text):
            line = int(match.group(1))
            rel = path.relative_to(ROOT)
            v.check(
                1 <= line <= line_count,
                f"{rel}: source citation line {line} is out of bounds (1..{line_count})",
            )
        for match in REVIEW_CITATION_RE.finditer(text):
            line = int(match.group(1))
            rel = path.relative_to(ROOT)
            v.check(
                1 <= line <= review_line_count,
                f"{rel}: review citation line {line} is out of bounds (1..{review_line_count})",
            )
        for match in SHORTHAND_CITATION_RE.finditer(text):
            line = int(match.group(1))
            rel = path.relative_to(ROOT)
            v.check(
                1 <= line <= line_count,
                f"{rel}: shorthand citation :{line} is out of bounds (1..{line_count})",
            )


def check_links(v: Validator) -> None:
    for path in iter_markdown():
        text = path.read_text(encoding="utf-8")
        text = FENCE_RE.sub("", text)
        text = INLINE_CODE_RE.sub("", text)
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1].strip()
            if not target or target.startswith(
                ("http://", "https://", "mailto:", "tel:", "#")
            ):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            if target.startswith("/"):
                resolved = (ROOT / target.lstrip("/")).resolve()
            else:
                resolved = (path.parent / target).resolve()
            rel = path.relative_to(ROOT)
            v.check(
                resolved.exists(),
                f"{rel}: broken link target {target!r}",
            )


def check_required(v: Validator) -> None:
    for rel in REQUIRED_FILES:
        v.check((ROOT / rel).is_file(), f"required file missing: {rel}")


def check_content(v: Validator) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    v.check("revise, do not adopt" in readme, "README is missing the audit verdict")
    v.check("13,255" in readme, "README is missing the source line count")
    v.check("docs/audit/" in readme, "README is missing the issue register")
    v.check("66 records" in readme, "README is missing the issue count")
    v.check("make verify" in readme, "README is missing the verification command")
    v.check(
        "audit observation, not a required fix" in readme,
        "README does not say issues are optional observations",
    )
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    v.check("source is immutable" in agents.lower(), "AGENTS is missing source immutability")
    v.check("WISLIM-001" in agents, "AGENTS is missing the stable issue ID rule")
    v.check("make register" in agents, "AGENTS is missing the register workflow")
    v.check(
        "not treat audit issues as fatal or mandatory" in agents.lower(),
        "AGENTS is missing the non-fatal framing rule",
    )
    index = (ROOT / "docs" / "audit" / "README.md").read_text(encoding="utf-8")
    v.check(
        "not a fatality rating" in index,
        "issue index does not explain that severity is not a fatality rating",
    )
    v.check(
        "read them as suggestions, not instructions" in index,
        "issue index does not frame issue titles as suggestions",
    )
    sync_source = (ROOT / "scripts" / "sync_issues.py").read_text(encoding="utf-8")
    v.check(
        "Blocks adoption" not in sync_source,
        "GitHub labels still describe issues as blocking adoption",
    )
    v.check(
        "repair before use" not in sync_source,
        "GitHub labels still require repair before use",
    )
    v.check(
        "not a required fix" in sync_source,
        "GitHub severity labels do not state that a fix is optional",
    )
    provenance = (ROOT / "evidence" / "provenance.md").read_text(encoding="utf-8")
    v.check("splitlines" in provenance, "provenance is missing the line-numbering caveat")
    v.check("13,544" in provenance, "provenance is missing the splitlines count")
    v.check(
        "public domain" in provenance.lower(),
        "provenance is missing the license ambiguity",
    )
    reproducibility = (ROOT / "docs" / "reproducibility.md").read_text(encoding="utf-8")
    v.check(
        "make issues" in reproducibility,
        "reproducibility is missing the GitHub mirror workflow",
    )
    v.check(
        "make review" in reproducibility,
        "reproducibility is missing the review register workflow",
    )
    extrinsic = (
        ROOT / "reviews" / "oph-lfdi-57" / "extrinsic-audit.md"
    ).read_text(encoding="utf-8")
    docs_reviews = (ROOT / "docs" / "reviews.md").read_text(encoding="utf-8")
    for index in range(1, 13):
        tid = f"OPH-REV-{index:03d}"
        v.check(tid in extrinsic, f"extrinsic-audit.md is missing {tid}")
        v.check(tid in docs_reviews, f"docs/reviews.md is missing {tid}")
    email = (
        ROOT / "reviews" / "oph-lfdi-57" / "response-email.md"
    ).read_text(encoding="utf-8")
    v.check(
        "https://github.com/docxology/WISLIM-audit" in email,
        "response-email.md is missing the plaintext repository URL",
    )
    verification = (
        ROOT / "reviews" / "oph-lfdi-57" / "verification.md"
    ).read_text(encoding="utf-8")
    v.check(
        "1c5a908ed3441c5d09628183af18c362dbc58bea" in verification,
        "verification receipt is missing the pinned OPH commit",
    )
    v.check(
        "23/23" in verification,
        "verification receipt is missing the OPH quote check result",
    )
    v.check(
        "2026-11-03" in verification,
        "verification receipt is missing the verification date",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="suppress the success summary",
    )
    args = parser.parse_args(argv)

    v = Validator()
    metadata = load_json(METADATA)
    text, lines = check_source(v, metadata)
    if lines:
        check_claims(v, lines)
        check_stress(v)
        check_citations(v, len(lines))
    check_issue_register(v, lines)
    check_review_register(v)
    check_required(v)
    check_links(v)
    check_content(v)

    if v.errors:
        print(f"FAIL: {len(v.errors)} error(s) after {v.checks} checks", file=sys.stderr)
        for error in v.errors:
            print(f"  - {error}", file=sys.stderr)
        if v.warnings:
            print("Warnings:", file=sys.stderr)
            for warning in v.warnings:
                print(f"  - {warning}", file=sys.stderr)
        return 1

    if not args.quiet:
        print(f"OK: {v.checks} checks passed")
        print(f"  source: {metadata['text_lines']:,} lines, {metadata['text_words']:,} words")
        print(f"  claims: {len(CLAIM_IDS)}")
        print(f"  stress tests: {len(STRESS_IDS)}")
        print("  audit issues: 66")
        print("  review topics: 12")
        print(f"  markdown files: {len(iter_markdown())}")
        if v.warnings:
            print("Warnings:")
            for warning in v.warnings:
                print(f"  - {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
