---
id: WISLIM-037
source_id: AS02
kind: red-team
title: "Break correlated AI verification"
severity: high
workstream: evidence
labels: [audit, red-team, severity:high, workstream:evidence]
source_lines: "n/a (red-team scenario)"
quote_lines: [1106, 995]
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-017, WISLIM-058]
github_issue: 37
---

# WISLIM-037: Break correlated AI verification

> **Severity:** high · **Kind:** red-team · **Status:** observation · **Source:** `AS02`  
> **GitHub issue:** [#37](https://github.com/docxology/WISLIM-audit/issues/37)  
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

> Despite our differences, we converged on a unified framework— the "Consensus Statement v1.0"—which every participating AI system ratified without amendment.
>
> — `source/WISLIM-v2.0.1.txt:1106`

**Audit note.** The paper does not publish prompts, model versions, or transcripts, so independence cannot be checked.

> Multiple AI systems from competing organizations, with different architectures, training approaches, and institutional values, examined a single proposition:
>
> — `source/WISLIM-v2.0.1.txt:995`

## Summary

The FLVS treats several model families as independent reviewers, but shared training data, fine-tuning conventions, and prompt templates make their errors correlated. A vendor that knows the shared blind spot can craft a record that every model approves, producing false assurance of independent review.

## Evidence

- **Actor:** A vendor that supplies multiple models to the FLVS.
- **Preconditions:** The FLVS uses several models from different brands but the same training data, fine-tuning conventions, and prompt templates.
- **Attack path:** The vendor knows the models share a blind spot (e.g., they underweight indirect harms to disabled people). It crafts a decision record that exploits the blind spot. All models approve.
- **Impact:** Discriminatory decisions; false assurance of independent review.
- **Detection:** Red-team the models with adversarial cases; measure correlation of errors; compare with human expert review.
- **Mitigation:** Diverse model families; independent red teams; human review with authority to override; publish error correlations.
- **Residual risk:** All models may share biases from human text. High.

## Why it matters

Independence in name is not independence in fact. Correlated errors defeat the purpose of using multiple reviewers, and the framework publishes no error-correlation data.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Diverse model families
2. Independent red teams
3. Human review with authority to override
4. Publish error correlations.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] Error-correlation testing across the models is published, and a shared blind spot is shown to be caught by at least one human or model reviewer.
- [ ] If a control is adopted, it is exercised against the scenario in a red-team test.
- [ ] If the framework proceeds, residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, deployment in this context remains an explicit risk decision for the responsible authority.

## Related issues

- `WISLIM-017`
- `WISLIM-058`

## Tracking

This record is mirrored to GitHub issue #37.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
