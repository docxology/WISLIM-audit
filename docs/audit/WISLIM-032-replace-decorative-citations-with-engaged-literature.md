---
id: WISLIM-032
source_id: C32
kind: claim
title: "Replace decorative citations with engaged literature"
severity: medium
workstream: evidence
labels: [audit, claim, severity:medium, workstream:evidence]
source_lines: "392"
quote_lines: [392, 388]
audit_modules: [audit/11-citations-and-scholarship.md, evidence/citation-audit.md]
related: [WISLIM-027, WISLIM-028]
github_issue: 32
---

# WISLIM-032: Replace decorative citations with engaged literature

> **Severity:** medium · **Kind:** claim · **Status:** observation · **Source:** `C32`  
> **GitHub issue:** [#32](https://github.com/docxology/WISLIM-audit/issues/32)  
> **Audit modules:** audit/11-citations-and-scholarship.md, evidence/citation-audit.md  
> **Source lines:** 392

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

> See Appendix C for full references to Bostrom, Christiano, Friston, Hadfield-Menell, Leike, Ord, O'Keefe, Russell, Yudkowsky, and others.
>
> — `source/WISLIM-v2.0.1.txt:392`

**Audit note.** The appendix lists names; it does not engage their arguments.

> See Appendix B for independent verification of this framework by multiple AI systems from different organizations.
>
> — `source/WISLIM-v2.0.1.txt:388`

## Summary

The paper's citations support its claims. Verdict: `decorative`. The citations are name-drops. Friston is irrelevant to the argument. The paper does not engage the is-ought gap, moral pluralism, or the technical AI-safety literature. Some bibliographic details are inconsistent.

## Evidence

- **Claim:** The paper's citations support its claims.
- **Anchor:** "Appendix C"
- **Source:** `source/WISLIM-v2.0.1.txt:392`
- **Verdict:** `decorative`; severity `medium`.
- **Audit:** `audit/11-citations-and-scholarship.md`

## Why it matters

The citations are the paper's claim to scholarship. If they are name-drops rather than engaged arguments, the paper has not tested its thesis against the literature.

## Steelman and reply

The reply is that the bibliography is a map of relevant literature. A map is not an engagement; none of the cited positions is reconstructed, criticized, or shown to be compatible with the thesis.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Add a real literature review with claim-by-claim citation and engagement.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] If the author addresses the concern, the revision resolves `C32` or explains why the claim is retained.
- [ ] If the author revises, the revision note in `audit/11-citations-and-scholarship.md` records the source anchor and any reviewer sign-off.
- [ ] After review, the claim registry entry `C32` records the outcome.
- [ ] Where practical, a regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-027`
- `WISLIM-028`

## Tracking

This record is mirrored to GitHub issue #32.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
