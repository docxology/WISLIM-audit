---
id: WISLIM-050
source_id: AS15
kind: red-team
title: "Close jurisdiction-shopping gaps"
severity: high
status: observation
workstream: governance
labels: [audit, red-team, severity:high, workstream:governance]
source_lines: "n/a (red-team scenario)"
quote_lines: [1451, 880]
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-030, WISLIM-059]
github_issue: 50
---

# WISLIM-050: Close jurisdiction-shopping gaps

> **Severity:** high · **Kind:** red-team · **Status:** observation · **Source:** `AS15`  
> **GitHub issue:** [#50](https://github.com/docxology/WISLIM-audit/issues/50)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

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

> Layer 4: International oversight for global-impact decisions (days to weeks)
>
> — `source/WISLIM-v2.0.1.txt:1451`

**Audit note.** The paper asserts international oversight but no mutual-recognition or minimum-floor rule.

> Layer 4: International/Global oversight for planetary risks.
>
> — `source/WISLIM-v2.0.1.txt:880`

## Summary

A corporation can route a risky decision through the jurisdiction with the weakest verification and rely on the record elsewhere. Regulatory arbitrage produces a race to the bottom and approves harm.

## Evidence

- **Actor:** A multinational corporation.
- **Preconditions:** Different states implement the framework differently.
- **Attack path:** The corporation routes a risky decision through the state with the weakest verification. The record is valid in that jurisdiction.
- **Impact:** A race to the bottom; harmful decisions are approved.
- **Detection:** Compare approval rates across jurisdictions; require mutual recognition.
- **Mitigation:** Minimum standards; mutual recognition agreements; home-state accountability.
- **Residual risk:** Regulatory arbitrage is persistent. High.

## Why it matters

A framework with no mutual recognition or minimum floor lets the weakest jurisdiction set the effective standard for everyone.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Minimum standards
2. Mutual recognition agreements
3. Home-state accountability.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] Mutual-recognition and minimum-floor rules prevent a decision rejected in one jurisdiction from being approved by routing it through another.
- [ ] If a control is adopted, it is exercised against the scenario in a red-team test.
- [ ] If the framework proceeds, residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, deployment in this context remains an explicit risk decision for the responsible authority.

## Related issues

- `WISLIM-030`
- `WISLIM-059`

## Tracking

This record is mirrored to GitHub issue #50.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
