---
id: WISLIM-014
source_id: C14
kind: claim
title: "Make the no-coercion rule apply to the framework itself"
severity: high
status: observation
workstream: rhetoric
labels: [audit, claim, severity:high, workstream:rhetoric]
source_lines: "238"
quote_lines: [238]
audit_modules: [audit/10-rhetoric-and-coercion.md, audit/06-agency-and-life.md]
related: [WISLIM-010, WISLIM-016, WISLIM-024]
github_issue: 14
---

# WISLIM-014: Make the no-coercion rule apply to the framework itself

> **Severity:** high · **Kind:** claim · **Status:** observation · **Source:** `C14`  
> **GitHub issue:** [#14](https://github.com/docxology/WISLIM-audit/issues/14)  
> **Audit modules:** audit/10-rhetoric-and-coercion.md, audit/06-agency-and-life.md  
> **Source lines:** 238

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

> Actions that affect life must maintain epistemic transparency — no manipulation or misrepresentation.
>
> — `source/WISLIM-v2.0.1.txt:238`

## Summary

Actions affecting life must maintain epistemic transparency and avoid coercion. Verdict: `self-undermining`. The paper's own rhetoric — 'silence equals betrayal,' the integrity screen, 'unsafe by definition' — is coercive. The rule is also too broad: privacy, confidentiality, and justified non-disclosure are normal in medicine and security.

## Evidence

- **Claim:** Actions affecting life must maintain epistemic transparency and avoid coercion.
- **Anchor:** "Actions that affect life must maintain epistemic transparency"
- **Source:** `source/WISLIM-v2.0.1.txt:238`
- **Verdict:** `self-undermining`; severity `high`.
- **Audit:** `audit/10-rhetoric-and-coercion.md`

## Why it matters

Transparency and non-coercion are the framework's own conditions. Applying them only to agents and not to the framework is a consistency failure.

## Steelman and reply

The reply is that the framework is a theory, so transparency applies only to actions it governs. A theory that tells agents to avoid coercion while using coercive rhetoric and a loyalty screen has not applied its own condition.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Specify minimal, proportionate, rights-respecting communication and exceptions for privacy and security.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] If the author addresses the concern, the revision resolves `C14` or explains why the claim is retained.
- [ ] If the author revises, the revision note in `audit/10-rhetoric-and-coercion.md` records the source anchor and any reviewer sign-off.
- [ ] After review, the claim registry entry `C14` records the outcome.
- [ ] Where practical, a regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-010`
- `WISLIM-016`
- `WISLIM-024`

## Tracking

This record is mirrored to GitHub issue #14.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
