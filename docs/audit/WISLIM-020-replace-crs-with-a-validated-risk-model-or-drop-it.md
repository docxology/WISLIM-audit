---
id: WISLIM-020
source_id: C20
kind: claim
title: "Replace CRS with a validated risk model or drop it"
severity: high
status: observation
workstream: formal
labels: [audit, claim, severity:high, workstream:formal]
source_lines: "2158"
quote_lines: [2158]
audit_modules: [audit/09-governance-and-oversight.md, audit/08-formal-and-scientific-claims.md]
related: [WISLIM-019, WISLIM-012]
github_issue: 20
---

# WISLIM-020: Replace CRS with a validated risk model or drop it

> **Severity:** high · **Kind:** claim · **Status:** observation · **Source:** `C20`  
> **GitHub issue:** [#20](https://github.com/docxology/WISLIM-audit/issues/20)  
> **Audit modules:** audit/09-governance-and-oversight.md, audit/08-formal-and-scientific-claims.md  
> **Source lines:** 2158

> **Status: audit observation, not a required fix.** This issue records a
> point that may matter for the work's impact, clarity, or risk. It is not a
> verdict that the work is invalid, and addressing it is optional. The author
> may decline it with reasons. Severity estimates potential impact if the
> concern applies; it does not mean the overall work fails or that a change is
> mandatory.

## Publication reference

David Wishengrad, *Life is Most Important in Life is The Most Important Truth in Life: A Foundational Proof for Alignment, Identity, and the Cure of Needless Suffering*, Version 2.0.1 (4 February 2026), 289 pages. DOI [`10.21428/4831231e.8c4c6c8f`](https://doi.org/10.21428/4831231e.8c4c6c8f); PhilPapers [`WISLIM`](https://philpapers.org/rec/WISLIM).

Source of record: `source/WISLIM-v2.0.1.pdf` (SHA-256 `7716807d081e497364a14475ef6f8a6b06e6cabaa6858749bb17e6a904e7dfcd`). Quotations use the newline-delimited text at `source/WISLIM-v2.0.1.txt` (13,255 lines), extracted with `pdftotext -layout`.

> **Audit status:** critical first pass, not peer review. Severity and
> remediation are provisional judgments, not safety certification.

## Primary quotations

> Combined Risk Score (CRS): CRS = IS × II × log(ID)
>
> — `source/WISLIM-v2.0.1.txt:2158`

## Summary

CRS = IS x II x log(ID) is a valid risk score. Verdict: `invalid`. The units are unspecified. log(ID) is negative for durations below one unit and zero at one unit. The formula ignores probability, severity distribution, consent, and uncertainty. It is arbitrary, unvalidated, and easy to game.

## Evidence

- **Claim:** CRS = IS x II x log(ID) is a valid risk score.
- **Anchor:** "Combined Risk Score (CRS): CRS = IS × II × log(ID)"
- **Source:** `source/WISLIM-v2.0.1.txt:2158`
- **Verdict:** `invalid`; severity `high`.
- **Audit:** `audit/09-governance-and-oversight.md`

## Why it matters

The CRS determines which decisions get review. If the score is a product of self-reported inputs, an actor can choose its own tier.

## Steelman and reply

The reply is that the CRS is a triage heuristic, not a measurement. A triage heuristic that selects its own inputs and thresholds is a gatekeeping device, and the paper gives no calibration or validation.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Use a validated risk model with explicit assumptions, calibration, and adversarial testing.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] If the author addresses the concern, the revision resolves `C20` or explains why the claim is retained.
- [ ] If the author revises, the revision note in `audit/09-governance-and-oversight.md` records the source anchor and any reviewer sign-off.
- [ ] After review, the claim registry entry `C20` records the outcome.
- [ ] Where practical, a regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-019`
- `WISLIM-012`

## Tracking

This record is mirrored to GitHub issue #20.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
