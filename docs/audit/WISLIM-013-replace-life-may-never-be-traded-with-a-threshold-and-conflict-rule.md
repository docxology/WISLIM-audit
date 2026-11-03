---
id: WISLIM-013
source_id: C13
kind: claim
title: "Replace 'life may never be traded' with a threshold and conflict rule"
severity: high
status: observation
workstream: governance
labels: [audit, claim, severity:high, workstream:governance]
source_lines: "230"
quote_lines: [230]
audit_modules: [audit/06-agency-and-life.md, audit/09-governance-and-oversight.md]
related: [WISLIM-010, WISLIM-012, WISLIM-029]
github_issue: 13
---

# WISLIM-013: Replace 'life may never be traded' with a threshold and conflict rule

> **Severity:** high · **Kind:** claim · **Status:** observation · **Source:** `C13`  
> **GitHub issue:** [#13](https://github.com/docxology/WISLIM-audit/issues/13)  
> **Audit modules:** audit/06-agency-and-life.md, audit/09-governance-and-oversight.md  
> **Source lines:** 230

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

> Life may never be traded for non-life objectives (e.g., profit, efficiency, ideology).
>
> — `source/WISLIM-v2.0.1.txt:230`

## Summary

Life may never be traded for non-life objectives. Verdict: `overbroad`. Ordinary decisions routinely trade small risks to life for other goods (transport, medicine, rescue, resource allocation). A absolute prohibition with no exceptions makes legitimate governance impossible and conflicts with the paper's own acknowledgment of tragic choices.

## Evidence

- **Claim:** Life may never be traded for non-life objectives.
- **Anchor:** "Life may never be traded for non-life objectives"
- **Source:** `source/WISLIM-v2.0.1.txt:230`
- **Verdict:** `overbroad`; severity `high`.
- **Audit:** `audit/06-agency-and-life.md`

## Why it matters

An absolute non-substitution rule forbids the trade-offs that medicine, rescue, and war actually require. The paper needs a threshold or conflict rule and does not give one.

## Steelman and reply

The reply is that the rule forbids treating life as a means, not every trade-off. But the text says 'may never be traded', and the medicine and rescue cases are precisely trade-offs among lives; the reply requires a distinction the paper does not draw.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Use a proportionate, threshold-based rule with explicit exceptions and procedural safeguards.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] If the author addresses the concern, the revision resolves `C13` or explains why the claim is retained.
- [ ] If the author revises, the revision note in `audit/06-agency-and-life.md` records the source anchor and any reviewer sign-off.
- [ ] After review, the claim registry entry `C13` records the outcome.
- [ ] Where practical, a regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-010`
- `WISLIM-012`
- `WISLIM-029`

## Tracking

This record is mirrored to GitHub issue #13.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
