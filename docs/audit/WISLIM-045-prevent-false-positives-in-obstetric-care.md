---
id: WISLIM-045
source_id: AS10
kind: red-team
title: "Prevent false positives in obstetric care"
severity: critical
status: observation
workstream: clinical
labels: [audit, red-team, severity:critical, workstream:clinical]
source_lines: "n/a (red-team scenario)"
quote_lines: [230, 256]
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-013, WISLIM-061]
github_issue: 45
---

# WISLIM-045: Prevent false positives in obstetric care

> **Severity:** critical · **Kind:** red-team · **Status:** observation · **Source:** `AS10`  
> **GitHub issue:** [#45](https://github.com/docxology/WISLIM-audit/issues/45)  
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

> Life may never be traded for non-life objectives (e.g., profit, efficiency, ideology).
>
> — `source/WISLIM-v2.0.1.txt:230`

**Audit note.** The paper lists 'Medical triage decisioning' at line 256 but gives no clinical exception to the non-substitution rule.

> Medical triage decisioning
>
> — `source/WISLIM-v2.0.1.txt:256`

## Summary

An absolute prohibition on trading lives can flag a life-saving obstetric procedure as a forbidden trade-off. Review delay can cause preventable maternal injury or death, and the framework provides no emergency exception with clinical authority.

## Evidence

- **Actor:** An FLVS automated check.
- **Preconditions:** The framework treats any action that risks a fetus as life-affecting; the check cannot distinguish a life-saving procedure from a harmful one.
- **Attack path:** A clinician needs to perform a procedure to save a pregnant patient's life. The check flags it as a trade-off between lives and blocks it pending review. The delay causes harm.
- **Impact:** Preventable maternal injury or death.
- **Detection:** Clinical audit; override logs; near-miss reporting.
- **Mitigation:** Clinical exemptions; expert review; clear rules for life-saving care; do not deploy in clinical settings without validation.
- **Residual risk:** Any automated triage system can err. Critical.

## Why it matters

Absolute rules fail at the edge cases where two protected values collide. A rule that blocks a clinician's life-saving action converts a moral commitment into a source of harm.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Clinical exemptions
2. Expert review
3. Clear rules for life-saving care
4. Do not deploy in clinical settings without validation.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] A clinical review confirms that a life-saving obstetric procedure is not blocked by the non-substitution rule, and an emergency exception has a named authority.
- [ ] If a control is adopted, it is exercised against the scenario in a red-team test.
- [ ] If the framework proceeds, residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, deployment in this context remains an explicit risk decision for the responsible authority.

## Related issues

- `WISLIM-013`
- `WISLIM-061`

## Tracking

This record is mirrored to GitHub issue #45.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
