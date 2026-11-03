---
id: WISLIM-025
source_id: C25
kind: claim
title: "Reconcile the public-domain dedication with CC-BY 4.0"
severity: medium
status: observation
workstream: publication
labels: [audit, claim, severity:medium, workstream:publication]
source_lines: "13255"
quote_lines: [13255]
audit_modules: [evidence/provenance.md, LICENSE]
related: [WISLIM-026]
github_issue: 25
---

# WISLIM-025: Reconcile the public-domain dedication with CC-BY 4.0

> **Severity:** medium · **Kind:** claim · **Status:** observation · **Source:** `C25`  
> **GitHub issue:** [#25](https://github.com/docxology/WISLIM-audit/issues/25)  
> **Audit modules:** evidence/provenance.md, LICENSE  
> **Source lines:** 13255

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

> “I dedicate this work to the public domain.”
>
> — `source/WISLIM-v2.0.1.txt:13255`

**Audit note.** PubPub displays CC-BY 4.0; the dedication is the only license statement in the PDF.

## Summary

The work is public domain. Verdict: `ambiguous`. The PubPub page uses CC-BY 4.0. The PDF says public domain. These are different legal instruments. The PDF has no license page. Reuse terms are unclear.

## Evidence

- **Claim:** The work is public domain.
- **Anchor:** "I dedicate this work to the public domain."
- **Source:** `source/WISLIM-v2.0.1.txt:13255`
- **Verdict:** `ambiguous`; severity `medium`.
- **Audit:** `evidence/provenance.md`

## Why it matters

The public-domain dedication conflicts with the CC-BY notice on PubPub. Users cannot tell what they may reuse.

## Steelman and reply

The reply is that the dedication and CC-BY are compatible because CC-BY is a license and public domain is a waiver. They are not compatible as stated: CC-BY requires attribution, and a public-domain dedication purports to waive it.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Clarify the license with the author and preserve attribution.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] If the author addresses the concern, the revision resolves `C25` or explains why the claim is retained.
- [ ] If the author revises, the revision note in `evidence/provenance.md` records the source anchor and any reviewer sign-off.
- [ ] After review, the claim registry entry `C25` records the outcome.
- [ ] Where practical, a regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-026`

## Tracking

This record is mirrored to GitHub issue #25.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
