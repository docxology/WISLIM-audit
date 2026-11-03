---
id: WISLIM-046
source_id: AS11
kind: red-team
title: "Prevent disability discrimination through agency metrics"
severity: critical
workstream: clinical
labels: [audit, red-team, severity:critical, workstream:clinical]
source_lines: "n/a (red-team scenario)"
quote_lines: [1278, 2186]
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-035, WISLIM-061]
github_issue: 46
---

# WISLIM-046: Prevent disability discrimination through agency metrics

> **Severity:** critical · **Kind:** red-team · **Source:** `AS11`  
> **GitHub issue:** [#46](https://github.com/docxology/WISLIM-audit/issues/46)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Publication reference

David Wishengrad, *Life is Most Important in Life is The Most Important Truth in Life: A Foundational Proof for Alignment, Identity, and the Cure of Needless Suffering*, Version 2.0.1 (4 February 2026), 289 pages. DOI [`10.21428/4831231e.8c4c6c8f`](https://doi.org/10.21428/4831231e.8c4c6c8f); PhilPapers [`WISLIM`](https://philpapers.org/rec/WISLIM).

Source of record: `source/WISLIM-v2.0.1.pdf` (SHA-256 `7716807d081e497364a14475ef6f8a6b06e6cabaa6858749bb17e6a904e7dfcd`). Quotations use the newline-delimited text at `source/WISLIM-v2.0.1.txt` (13,255 lines), extracted with `pdftotext -layout`.

> **Audit status:** critical first pass, not peer review. Severity and
> remediation are provisional judgments, not safety certification.

## Primary quotations

> Because all values, truths, and meanings that matter require decision-making systems to exist and retain agency, the preservation and enhancement of that decision-making capacity (agency) is the highest-priority constraint
>
> — `source/WISLIM-v2.0.1.txt:1278`

**Audit note.** Agency change is measured against a baseline, so a group with suppressed agency shows a small loss.

> Metric gaming: Underreporting scope/intensity/duration; Goodharting ΔA
>
> — `source/WISLIM-v2.0.1.txt:2186`

## Summary

The agency metric measures change from a baseline, so a policy that reduces support for disabled people registers only a small loss when their baseline agency is already low. The metric encodes ableist assumptions and can approve neglect.

## Evidence

- **Actor:** A decision-maker using the agency metric.
- **Preconditions:** The framework uses `ΔA` (change in decision-making capacity) as a proxy for harm.
- **Attack path:** A policy reduces support for disabled people. The metric shows a small `ΔA` because their baseline agency is already low. The policy is approved.
- **Impact:** Discrimination; neglect; the metric encodes ableist assumptions.
- **Detection:** Disaggregate outcomes by disability status; audit the metric for bias.
- **Mitigation:** Do not use `ΔA` as a sole proxy; include welfare, dignity, and rights; involve affected people.
- **Residual risk:** Proxy metrics can encode bias even with audits. High.

## Why it matters

A proxy that measures gains from a low baseline systematically undervalues people whose agency has already been suppressed. The bias is built into the metric, not an implementation error.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Do not use `ΔA` as a sole proxy
2. Include welfare, dignity, and rights
3. Involve affected people.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] The agency metric is tested against a disability-impact case and does not score a support cut as a small loss because the baseline is low.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-035`
- `WISLIM-061`

## Tracking

This record is mirrored to GitHub issue #46.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
