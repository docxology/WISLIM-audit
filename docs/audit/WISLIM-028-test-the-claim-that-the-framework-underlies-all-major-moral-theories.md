---
id: WISLIM-028
source_id: C28
kind: claim
title: "Test the claim that the framework underlies all major moral theories"
severity: high
workstream: argument
labels: [audit, claim, severity:high, workstream:argument]
source_lines: "8902"
quote_lines: [8902]
audit_modules: [audit/11-citations-and-scholarship.md, audit/12-steelman.md]
related: [WISLIM-010, WISLIM-027, WISLIM-032]
github_issue: 28
---

# WISLIM-028: Test the claim that the framework underlies all major moral theories

> **Severity:** high · **Kind:** claim · **Status:** observation · **Source:** `C28`  
> **GitHub issue:** [#28](https://github.com/docxology/WISLIM-audit/issues/28)  
> **Audit modules:** audit/11-citations-and-scholarship.md, audit/12-steelman.md  
> **Source lines:** 8902

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

> Response: No. It's a meta-framework that sits underneath those approaches:
>
> — `source/WISLIM-v2.0.1.txt:8902`

## Summary

The framework is a meta-framework underlying consequentialism, deontology, virtue ethics, and rights. Verdict: `false`. It is a substantive axiology that conflicts with each framework. The trivial fact that all frameworks presuppose agents does not yield convergence on life-first.

## Evidence

- **Claim:** The framework is a meta-framework underlying consequentialism, deontology, virtue ethics, and rights.
- **Anchor:** "It's a meta-framework that sits underneath those approaches"
- **Source:** `source/WISLIM-v2.0.1.txt:8902`
- **Verdict:** `false`; severity `high`.
- **Audit:** `audit/11-citations-and-scholarship.md`

## Why it matters

The meta-framework claim lets the paper avoid engaging rival theories. If it sits under every view, it must show how it preserves their disagreements.

## Steelman and reply

The reply is that a meta-framework can be compatible with rival theories without resolving their disputes. Compatibility is cheap; the paper must show what each theory loses or gains by adopting the framework.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Compare the framework explicitly with each rival and acknowledge conflicts.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] If the author addresses the concern, the revision resolves `C28` or explains why the claim is retained.
- [ ] If the author revises, the revision note in `audit/11-citations-and-scholarship.md` records the source anchor and any reviewer sign-off.
- [ ] After review, the claim registry entry `C28` records the outcome.
- [ ] Where practical, a regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-010`
- `WISLIM-027`
- `WISLIM-032`

## Tracking

This record is mirrored to GitHub issue #28.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
