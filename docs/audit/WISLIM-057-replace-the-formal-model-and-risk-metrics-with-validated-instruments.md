---
id: WISLIM-057
source_id: WS02
kind: workstream
title: "Replace the formal model and risk metrics with validated instruments"
severity: high
workstream: formal
labels: [audit, workstream, severity:high, workstream:formal]
source_lines: "n/a (workstream)"
quote_lines: [427, 2158]
audit_modules: [audit/05-formula-e-infinity.md, audit/08-formal-and-scientific-claims.md, audit/09-governance-and-oversight.md]
related: [WISLIM-011, WISLIM-020, WISLIM-023, WISLIM-031, WISLIM-036, WISLIM-043]
github_issue: 57
---

# WISLIM-057: Replace the formal model and risk metrics with validated instruments

> **Severity:** high · **Kind:** workstream · **Source:** `WS02`  
> **GitHub issue:** [#57](https://github.com/docxology/WISLIM-audit/issues/57)  
> **Audit modules:** audit/05-formula-e-infinity.md, audit/08-formal-and-scientific-claims.md, audit/09-governance-and-oversight.md  
> **Source lines:** n/a (workstream)

## Publication reference

David Wishengrad, *Life is Most Important in Life is The Most Important Truth in Life: A Foundational Proof for Alignment, Identity, and the Cure of Needless Suffering*, Version 2.0.1 (4 February 2026), 289 pages. DOI [`10.21428/4831231e.8c4c6c8f`](https://doi.org/10.21428/4831231e.8c4c6c8f); PhilPapers [`WISLIM`](https://philpapers.org/rec/WISLIM).

Source of record: `source/WISLIM-v2.0.1.pdf` (SHA-256 `7716807d081e497364a14475ef6f8a6b06e6cabaa6858749bb17e6a904e7dfcd`). Quotations use the newline-delimited text at `source/WISLIM-v2.0.1.txt` (13,255 lines), extracted with `pdftotext -layout`.

> **Audit status:** critical first pass, not peer review. Severity and
> remediation are provisional judgments, not safety certification.

## Primary quotations

> At the heart of this paper’s moral and logical architecture is a single, unbranded, and universally applicable ethical formula
>
> — `source/WISLIM-v2.0.1.txt:427`

> Combined Risk Score (CRS): CRS = IS × II × log(ID)
>
> — `source/WISLIM-v2.0.1.txt:2158`

## Summary

The E-infinity formula, the Combined Risk Score, and the 210 test catalogue are presented as formal proof or operational metrics, but they are undefined, gameable, or analogical. This workstream separates the metaphor from the model and requires validation before use.

## Evidence

- **Failure modes covered:** F08, F09, F10, F11, F14
- **Claims covered:** C11, C20, C23, C31
- **Scenarios covered:** AS01, AS08
- **Audit modules:** audit/05-formula-e-infinity.md, audit/08-formal-and-scientific-claims.md, audit/09-governance-and-oversight.md

## Why it matters

Formal vocabulary creates false assurance. If the metrics are used in governance, errors will be systematic and hard to detect.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Demote E-infinity to a metaphor or specify variables, units, and a decision rule.
2. Replace CRS with a validated probabilistic model or drop it.
3. Reclassify the 210 entries as analogies, heuristics, or formal results, not theorems.
4. Publish calibration, error rates, and negative results.
5. Commission an independent formal review.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] A formal model specification exists with assumptions and unit tests.
- [ ] CRS has calibration and sensitivity analysis, or is removed.
- [ ] Every stress-test entry is labeled as analogy, heuristic, or formal result.
- [ ] An external reviewer signs off on the formal claims.

## Related issues

- `WISLIM-011`
- `WISLIM-020`
- `WISLIM-023`
- `WISLIM-031`
- `WISLIM-036`
- `WISLIM-043`

## Tracking

This record is mirrored to GitHub issue #57.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
