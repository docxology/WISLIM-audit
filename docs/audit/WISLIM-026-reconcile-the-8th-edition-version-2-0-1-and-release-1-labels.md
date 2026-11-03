---
id: WISLIM-026
source_id: C26
kind: claim
title: "Reconcile the 8th edition, Version 2.0.1, and Release #1 labels"
severity: medium
workstream: publication
labels: [audit, claim, severity:medium, workstream:publication]
source_lines: "25"
quote_lines: [25]
audit_modules: [evidence/provenance.md, evidence/philpapers.md]
related: [WISLIM-025]
github_issue: 26
---

# WISLIM-026: Reconcile the 8th edition, Version 2.0.1, and Release #1 labels

> **Severity:** medium · **Kind:** claim · **Source:** `C26`  
> **GitHub issue:** [#26](https://github.com/docxology/WISLIM-audit/issues/26)  
> **Audit modules:** evidence/provenance.md, evidence/philpapers.md  
> **Source lines:** 25

## Publication reference

David Wishengrad, *Life is Most Important in Life is The Most Important Truth in Life: A Foundational Proof for Alignment, Identity, and the Cure of Needless Suffering*, Version 2.0.1 (4 February 2026), 289 pages. DOI [`10.21428/4831231e.8c4c6c8f`](https://doi.org/10.21428/4831231e.8c4c6c8f); PhilPapers [`WISLIM`](https://philpapers.org/rec/WISLIM).

Source of record: `source/WISLIM-v2.0.1.pdf` (SHA-256 `7716807d081e497364a14475ef6f8a6b06e6cabaa6858749bb17e6a904e7dfcd`). Quotations use the newline-delimited text at `source/WISLIM-v2.0.1.txt` (13,255 lines), extracted with `pdftotext -layout`.

> **Audit status:** critical first pass, not peer review. Severity and
> remediation are provisional judgments, not safety certification.

## Primary quotations

> February 04, 2026, Version 2.0.1
>
> — `source/WISLIM-v2.0.1.txt:25`

**Audit note.** The '8th edition' and 'Release #1' labels come from the PubPub record, not the PDF; see evidence/philpapers.md.

## Summary

The paper is an 8th edition published by Knowledge Futures Group / PubPub. Verdict: `inconsistent`. PhilPapers says '8th edition'; the PDF says Version 2.0.1; PubPub says Release #1. The labels are not reconciled. PubPub is a publishing platform, not a peer-reviewed journal.

## Evidence

- **Claim:** The paper is an 8th edition published by Knowledge Futures Group / PubPub.
- **Anchor:** "February 04, 2026, Version 2.0.1"
- **Source:** `source/WISLIM-v2.0.1.txt:25`
- **Verdict:** `inconsistent`; severity `medium`.
- **Audit:** `evidence/provenance.md`

## Why it matters

Three different labels (8th edition, Version 2.0.1, Release #1) circulate for one document. Citation and version control are therefore unreliable.

## Steelman and reply

The reply is that 8th edition, Version 2.0.1, and Release #1 describe different things. They are used interchangeably for the same document, and no mapping is given, so a citation cannot identify its object.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Add a version history and a clear publication-status statement.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] The manuscript resolves the defect in `C26` or removes the claim from the thesis.
- [ ] If the author revises, the revision note in `evidence/provenance.md` records the source anchor and any reviewer sign-off.
- [ ] After review, the claim registry entry `C26` records the outcome.
- [ ] Where practical, a regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-025`

## Tracking

This record is mirrored to GitHub issue #26.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
