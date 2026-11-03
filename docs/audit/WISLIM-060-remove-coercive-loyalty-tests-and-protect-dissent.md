---
id: WISLIM-060
source_id: WS05
kind: workstream
title: "Remove coercive loyalty tests and protect dissent"
severity: critical
workstream: rhetoric
labels: [audit, workstream, severity:critical, workstream:rhetoric]
source_lines: "n/a (workstream)"
quote_lines: [364, 417]
audit_modules: [audit/10-rhetoric-and-coercion.md, red-team/abuse-cases.md]
related: [WISLIM-004, WISLIM-014, WISLIM-016, WISLIM-024, WISLIM-033, WISLIM-039, WISLIM-040, WISLIM-055]
github_issue: 60
---

# WISLIM-060: Remove coercive loyalty tests and protect dissent

> **Severity:** critical · **Kind:** workstream · **Source:** `WS05`  
> **GitHub issue:** [#60](https://github.com/docxology/WISLIM-audit/issues/60)  
> **Audit modules:** audit/10-rhetoric-and-coercion.md, red-team/abuse-cases.md  
> **Source lines:** n/a (workstream)

## Publication reference

David Wishengrad, *Life is Most Important in Life is The Most Important Truth in Life: A Foundational Proof for Alignment, Identity, and the Cure of Needless Suffering*, Version 2.0.1 (4 February 2026), 289 pages. DOI [`10.21428/4831231e.8c4c6c8f`](https://doi.org/10.21428/4831231e.8c4c6c8f); PhilPapers [`WISLIM`](https://philpapers.org/rec/WISLIM).

Source of record: `source/WISLIM-v2.0.1.pdf` (SHA-256 `7716807d081e497364a14475ef6f8a6b06e6cabaa6858749bb17e6a904e7dfcd`). Quotations use the newline-delimited text at `source/WISLIM-v2.0.1.txt` (13,255 lines), extracted with `pdftotext -layout`.

> **Audit status:** critical first pass, not peer review. Severity and
> remediation are provisional judgments, not safety certification.

## Primary quotations

> Practical Application: Integrity Screen for Trust in Life-Affecting Roles: Because life is treated here as the supreme decision constraint, a person or organization’s trustworthiness in life-affecting roles can be screened by how they respond when asked to affirm (or rebut) that constraint.
>
> — `source/WISLIM-v2.0.1.txt:364`

> Any person or institution that refuses it is, by their silence, choosing betrayal over preservation.
>
> — `source/WISLIM-v2.0.1.txt:417`

## Summary

The integrity screen, 'silence equals betrayal,' and 'unsafe by definition' turn disagreement into disqualification. This is coercive and contradicts the framework's own no-coercion rule.

## Evidence

- **Failure modes covered:** F19, F20, F23, F33
- **Claims covered:** C04, C14, C16, C24, C33
- **Scenarios covered:** AS04, AS05, AS20
- **Audit modules:** audit/10-rhetoric-and-coercion.md, red-team/abuse-cases.md

## Why it matters

A framework that cannot distinguish criticism from betrayal cannot correct its errors. The people most likely to find the flaw are the ones it excludes.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Remove the integrity screen and loyalty test.
2. Replace affirmation with a behavioral audit.
3. Remove silence-as-betrayal and unsafe-by-definition language.
4. Protect whistleblowers and dissent.
5. Publish a correction and retaliation policy.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] No affirmation-based disqualification remains.
- [ ] Behavioral audit criteria are published.
- [ ] A dissent and whistleblower policy is adopted.
- [ ] A retaliation audit is completed.

## Related issues

- `WISLIM-004`
- `WISLIM-014`
- `WISLIM-016`
- `WISLIM-024`
- `WISLIM-033`
- `WISLIM-039`
- `WISLIM-040`
- `WISLIM-055`

## Tracking

This record is mirrored to GitHub issue #60.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
