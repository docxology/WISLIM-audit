#!/usr/bin/env python3
"""Validate the WISLIM-audit repository.

The validator is intentionally dependency-free. It checks:

- the source PDF and text hashes against ``source/metadata.json``;
- the source line and word counts;
- the stable claim IDs, required fields, line bounds, and anchor text;
- the 210-row stress-test catalog and its summary counts;
- every explicit source-line citation is within bounds;
- required audit, red-team, and evidence modules exist;
- relative Markdown links resolve.

Run from the repository root:

    python3 tools/validate.py
"""

from __future__ import annotations

import argparse
import hashlib
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
    "tools/build_stress_catalog.py",
    "tools/validate.py",
    "tests/test_repository.py",
    "docs/method.md",
    "docs/glossary.md",
    "docs/reproducibility.md",
    "docs/claims.md",
    "docs/stress-tests.md",
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


def iter_markdown() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts and "node_modules" not in path.parts
    )


def check_citations(v: Validator, line_count: int) -> None:
    for path in iter_markdown():
        text = path.read_text(encoding="utf-8")
        for match in SOURCE_CITATION_RE.finditer(text):
            line = int(match.group(1))
            rel = path.relative_to(ROOT)
            v.check(
                1 <= line <= line_count,
                f"{rel}: source citation line {line} is out of bounds (1..{line_count})",
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
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    v.check("source is immutable" in agents.lower(), "AGENTS is missing source immutability")
    provenance = (ROOT / "evidence" / "provenance.md").read_text(encoding="utf-8")
    v.check("splitlines" in provenance, "provenance is missing the line-numbering caveat")
    v.check("13,544" in provenance, "provenance is missing the splitlines count")
    v.check(
        "public domain" in provenance.lower(),
        "provenance is missing the license ambiguity",
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
        print(f"  markdown files: {len(iter_markdown())}")
        if v.warnings:
            print("Warnings:")
            for warning in v.warnings:
                print(f"  - {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
