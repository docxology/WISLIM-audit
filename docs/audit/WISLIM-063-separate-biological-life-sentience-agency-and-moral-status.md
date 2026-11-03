---
id: WISLIM-063
source_id: WS08
kind: workstream
title: "Separate biological life, sentience, agency, and moral status"
severity: high
workstream: scope
labels: [audit, workstream, severity:high, workstream:scope]
source_lines: "n/a (workstream)"
quote_lines: [778, 788]
audit_modules: [audit/03-definition-of-life.md, audit/06-agency-and-life.md]
related: [WISLIM-006, WISLIM-035, WISLIM-051, WISLIM-052]
github_issue: 63
---

# WISLIM-063: Separate biological life, sentience, agency, and moral status

> **Severity:** high · **Kind:** workstream · **Status:** observation · **Source:** `WS08`  
> **GitHub issue:** [#63](https://github.com/docxology/WISLIM-audit/issues/63)  
> **Audit modules:** audit/03-definition-of-life.md, audit/06-agency-and-life.md  
> **Source lines:** n/a (workstream)

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

> Life = Any system that makes decisions that affect other life systems.
>
> — `source/WISLIM-v2.0.1.txt:778`

> It covers humans, animals, AI, institutions, and ecosystems.
>
> — `source/WISLIM-v2.0.1.txt:788`

## Summary

The definition includes humans, animals, AI, institutions, and ecosystems, but does not distinguish their moral status. It also excludes or marginalizes beings without decision-making capacity.

## Evidence

- **Failure modes covered:** F31, F32, F35
- **Claims covered:** C06, C35
- **Scenarios covered:** AS16, AS17
- **Audit modules:** audit/03-definition-of-life.md, audit/06-agency-and-life.md

## Why it matters

A category that includes everything cannot guide trade-offs. A category that requires agency repeats the exclusion the paper claims to oppose.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Adopt a tiered ontology: biological life, sentience, agency, and moral status.
2. Specify criteria for each tier.
3. Address infants, cognitive disability, coma, dementia, animals, ecosystems, future generations, and AI.
4. Consult disability and animal-ethics experts.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] A published taxonomy and criteria exist.
- [ ] A case table covers the marginal cases.
- [ ] Independent review is completed.
- [ ] The scope statement appears in the thesis.

## Related issues

- `WISLIM-006`
- `WISLIM-035`
- `WISLIM-051`
- `WISLIM-052`

## Tracking

This record is mirrored to GitHub issue #63.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
