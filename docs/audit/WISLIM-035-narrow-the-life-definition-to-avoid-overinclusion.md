---
id: WISLIM-035
source_id: C35
kind: claim
title: "Narrow the life definition to avoid overinclusion"
severity: high
status: observation
workstream: scope
labels: [audit, claim, severity:high, workstream:scope]
source_lines: "788"
quote_lines: [788, 778]
audit_modules: [audit/03-definition-of-life.md]
related: [WISLIM-006]
github_issue: 35
---

# WISLIM-035: Narrow the life definition to avoid overinclusion

> **Severity:** high · **Kind:** claim · **Status:** observation · **Source:** `C35`  
> **GitHub issue:** [#35](https://github.com/docxology/WISLIM-audit/issues/35)  
> **Audit modules:** audit/03-definition-of-life.md  
> **Source lines:** 788

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

> Inclusive: It covers humans, animals, AI, institutions, and ecosystems.
>
> — `source/WISLIM-v2.0.1.txt:788`

> Life = Any system that makes decisions that affect other life systems.
>
> — `source/WISLIM-v2.0.1.txt:778`

## Summary

The life definition is inclusive and anti-exclusion. Verdict: `overinclusive`. Including institutions, ecosystems, and AI without criteria creates moral standing for entities that may lack interests or agency in the relevant sense. It can dilute concern for sentient beings and make 'life-first' either vacuous or arbitrary.

## Evidence

- **Claim:** The life definition is inclusive and anti-exclusion.
- **Anchor:** "It covers humans, animals, AI, institutions, and ecosystems."
- **Source:** `source/WISLIM-v2.0.1.txt:788`
- **Verdict:** `overinclusive`; severity `high`.
- **Audit:** `audit/03-definition-of-life.md`

## Why it matters

The inclusive definition is the answer to exclusion objections. If it includes institutions and ecosystems without criteria, it licenses scope creep.

## Steelman and reply

The reply is that inclusion is a moral choice, not a metaphysical claim. Inclusion without criteria is not a choice the framework can defend; it lets any system claim protection and makes the scope ungovernable.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Use a tiered moral ontology with explicit criteria for interests, sentience, and agency.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] If the author addresses the concern, the revision resolves `C35` or explains why the claim is retained.
- [ ] If the author revises, the revision note in `audit/03-definition-of-life.md` records the source anchor and any reviewer sign-off.
- [ ] After review, the claim registry entry `C35` records the outcome.
- [ ] Where practical, a regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-006`

## Tracking

This record is mirrored to GitHub issue #35.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
