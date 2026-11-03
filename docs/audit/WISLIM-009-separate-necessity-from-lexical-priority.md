---
id: WISLIM-009
source_id: C09
kind: claim
title: "Separate necessity from lexical priority"
severity: high
workstream: argument
labels: [audit, claim, severity:high, workstream:argument]
source_lines: "3262"
quote_lines: [3262]
audit_modules: [audit/04-necessity-to-priority.md]
related: [WISLIM-003, WISLIM-008, WISLIM-010]
github_issue: 9
---

# WISLIM-009: Separate necessity from lexical priority

> **Severity:** high · **Kind:** claim · **Source:** `C09`  
> **GitHub issue:** [#9](https://github.com/docxology/WISLIM-audit/issues/9)  
> **Audit modules:** audit/04-necessity-to-priority.md  
> **Source lines:** 3262

## Publication reference

David Wishengrad, *Life is Most Important in Life is The Most Important Truth in Life: A Foundational Proof for Alignment, Identity, and the Cure of Needless Suffering*, Version 2.0.1 (4 February 2026), 289 pages. DOI [`10.21428/4831231e.8c4c6c8f`](https://doi.org/10.21428/4831231e.8c4c6c8f); PhilPapers [`WISLIM`](https://philpapers.org/rec/WISLIM).

Source of record: `source/WISLIM-v2.0.1.pdf` (SHA-256 `7716807d081e497364a14475ef6f8a6b06e6cabaa6858749bb17e6a904e7dfcd`). Quotations use the newline-delimited text at `source/WISLIM-v2.0.1.txt` (13,255 lines), extracted with `pdftotext -layout`.

> **Audit status:** critical first pass, not peer review. Severity and
> remediation are provisional judgments, not safety certification.

## Primary quotations

> T1 (Foundational Priority): Life protection is a necessary condition for the instantiation of any value.
>
> — `source/WISLIM-v2.0.1.txt:3262`

## Summary

All values require life systems, so life protection is logically prior to any specific value. Verdict: `valid-but-insufficient`. The conclusion is a necessity claim, not a lexical priority claim. Necessary conditions are not automatically overriding. The key premise (all values require life systems) is asserted, not proved, and is metaethically controversial.

## Evidence

- **Claim:** All values require life systems, so life protection is logically prior to any specific value.
- **Anchor:** "T1 (Foundational Priority): Life protection is a necessary condition for the instantiation"
- **Source:** `source/WISLIM-v2.0.1.txt:3262`
- **Verdict:** `valid-but-insufficient`; severity `high`.
- **Audit:** `audit/04-necessity-to-priority.md`

## Why it matters

This is the bridge from 'life is necessary for value' to 'life protection is prior to every value'. The paper asserts the bridge without defending it.

## Steelman and reply

The reply is that 'value' entails a valuer, and valuers are alive. This establishes a causal precondition for valuing, not a lexical priority over every other value; the inference from 'necessary for' to 'outranks' is the gap.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Distinguish necessity, centrality, and lexical priority; argue for the normative ranking separately.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] The manuscript resolves the defect in `C09` or removes the claim from the thesis.
- [ ] If the author revises, the revision note in `audit/04-necessity-to-priority.md` records the source anchor and any reviewer sign-off.
- [ ] After review, the claim registry entry `C09` records the outcome.
- [ ] Where practical, a regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-003`
- `WISLIM-008`
- `WISLIM-010`

## Tracking

This record is mirrored to GitHub issue #9.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
