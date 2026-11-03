---
id: WISLIM-006
source_id: C06
kind: claim
title: "Replace the circular definition of life with a tiered ontology"
severity: critical
workstream: argument
labels: [audit, claim, severity:critical, workstream:argument]
source_lines: "778"
quote_lines: [778, 788]
audit_modules: [audit/03-definition-of-life.md]
related: [WISLIM-007, WISLIM-035]
github_issue: 6
---

# WISLIM-006: Replace the circular definition of life with a tiered ontology

> **Severity:** critical · **Kind:** claim · **Source:** `C06`  
> **GitHub issue:** [#6](https://github.com/docxology/WISLIM-audit/issues/6)  
> **Audit modules:** audit/03-definition-of-life.md  
> **Source lines:** 778

## Publication reference

David Wishengrad, *Life is Most Important in Life is The Most Important Truth in Life: A Foundational Proof for Alignment, Identity, and the Cure of Needless Suffering*, Version 2.0.1 (4 February 2026), 289 pages. DOI [`10.21428/4831231e.8c4c6c8f`](https://doi.org/10.21428/4831231e.8c4c6c8f); PhilPapers [`WISLIM`](https://philpapers.org/rec/WISLIM).

Source of record: `source/WISLIM-v2.0.1.pdf` (SHA-256 `7716807d081e497364a14475ef6f8a6b06e6cabaa6858749bb17e6a904e7dfcd`). Quotations use the newline-delimited text at `source/WISLIM-v2.0.1.txt` (13,255 lines), extracted with `pdftotext -layout`.

> **Audit status:** critical first pass, not peer review. Severity and
> remediation are provisional judgments, not safety certification.

## Primary quotations

> Life = Any system that makes decisions that affect other life systems.
>
> — `source/WISLIM-v2.0.1.txt:778`

> It covers humans, animals, AI, institutions, and ecosystems.
>
> — `source/WISLIM-v2.0.1.txt:788`

## Summary

Life means any system that makes decisions affecting other life systems. Verdict: `circular/equivocal`. The definiens contains 'life systems,' so the definition is circular unless an independent base case is supplied. 'Decision' is broad enough to include thermostats and markets. The definition conflates biological life, sentience, agency, and moral patiency.

## Evidence

- **Claim:** Life means any system that makes decisions affecting other life systems.
- **Anchor:** "Life = Any system that makes decisions that affect other life systems."
- **Source:** `source/WISLIM-v2.0.1.txt:778`
- **Verdict:** `circular/equivocal`; severity `critical`.
- **Audit:** `audit/03-definition-of-life.md`

## Why it matters

The definition fixes the extension of 'life' for every later claim. If it includes any decision-making system, the framework's scope becomes unlimited and its metrics can be gamed.

## Steelman and reply

The reply is that the definition is a stipulation needed to include AI and institutions. Stipulation can fix usage, but it cannot make the stipulated class morally considerable, and it makes the framework's scope hostage to any system that decides.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Use a tiered ontology: biological life, sentience, agency, and moral status, each with independent criteria.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] The manuscript resolves the defect in `C06` or removes the claim from the thesis.
- [ ] If the author revises, the revision note in `audit/03-definition-of-life.md` records the source anchor and any reviewer sign-off.
- [ ] After review, the claim registry entry `C06` records the outcome.
- [ ] Where practical, a regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-007`
- `WISLIM-035`

## Tracking

This record is mirrored to GitHub issue #6.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
