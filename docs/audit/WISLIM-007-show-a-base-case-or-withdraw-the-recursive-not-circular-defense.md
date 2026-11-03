---
id: WISLIM-007
source_id: C07
kind: claim
title: "Show a base case or withdraw the 'recursive, not circular' defense"
severity: critical
workstream: argument
labels: [audit, claim, severity:critical, workstream:argument]
source_lines: "2625"
quote_lines: [2625, 2635]
audit_modules: [audit/03-definition-of-life.md]
related: [WISLIM-006]
github_issue: 7
---

# WISLIM-007: Show a base case or withdraw the 'recursive, not circular' defense

> **Severity:** critical · **Kind:** claim · **Source:** `C07`  
> **GitHub issue:** [#7](https://github.com/docxology/WISLIM-audit/issues/7)  
> **Audit modules:** audit/03-definition-of-life.md  
> **Source lines:** 2625

## Publication reference

David Wishengrad, *Life is Most Important in Life is The Most Important Truth in Life: A Foundational Proof for Alignment, Identity, and the Cure of Needless Suffering*, Version 2.0.1 (4 February 2026), 289 pages. DOI [`10.21428/4831231e.8c4c6c8f`](https://doi.org/10.21428/4831231e.8c4c6c8f); PhilPapers [`WISLIM`](https://philpapers.org/rec/WISLIM).

Source of record: `source/WISLIM-v2.0.1.pdf` (SHA-256 `7716807d081e497364a14475ef6f8a6b06e6cabaa6858749bb17e6a904e7dfcd`). Quotations use the newline-delimited text at `source/WISLIM-v2.0.1.txt` (13,255 lines), extracted with `pdftotext -layout`.

> **Audit status:** critical first pass, not peer review. Severity and
> remediation are provisional judgments, not safety certification.

## Primary quotations

> Response: The definition is recursive, not circular. There is a crucial difference.
>
> — `source/WISLIM-v2.0.1.txt:2625`

> Recursive: A is defined in terms of relations to other instances of A, with a base case.
>
> — `source/WISLIM-v2.0.1.txt:2635`

## Summary

The definition is recursive, not circular, with observable base cases. Verdict: `false`. No base case, recursion clause, or closure rule is given. 'Recursive' is asserted, not demonstrated. The definition is a mutually recursive relation with no independent grounding, so it does not pick out a determinate class.

## Evidence

- **Claim:** The definition is recursive, not circular, with observable base cases.
- **Anchor:** "The definition is recursive, not circular."
- **Source:** `source/WISLIM-v2.0.1.txt:2625`
- **Verdict:** `false`; severity `critical`.
- **Audit:** `audit/03-definition-of-life.md`

## Why it matters

The recursive defense is the only answer to the circularity objection. If it has no base case, the definition is circular and the central term is undefined.

## Steelman and reply

The reply is that observation statements are the base case. But 'we observe systems making decisions' already uses the contested term, and no decision-independent criterion is given for what counts as a decision or a system.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Give a formal inductive definition with base cases and show that it is well-founded.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] The manuscript resolves the defect in `C07` or removes the claim from the thesis.
- [ ] If the author revises, the revision note in `audit/03-definition-of-life.md` records the source anchor and any reviewer sign-off.
- [ ] After review, the claim registry entry `C07` records the outcome.
- [ ] Where practical, a regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-006`

## Tracking

This record is mirrored to GitHub issue #7.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
