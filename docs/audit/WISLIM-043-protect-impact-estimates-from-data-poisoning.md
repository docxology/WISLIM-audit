---
id: WISLIM-043
source_id: AS08
kind: red-team
title: "Protect impact estimates from data poisoning"
severity: high
workstream: security
labels: [audit, red-team, severity:high, workstream:security]
source_lines: "n/a (red-team scenario)"
quote_lines: [2186, 1203]
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-020, WISLIM-057]
github_issue: 43
---

# WISLIM-043: Protect impact estimates from data poisoning

> **Severity:** high · **Kind:** red-team · **Source:** `AS08`  
> **GitHub issue:** [#43](https://github.com/docxology/WISLIM-audit/issues/43)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Publication reference

David Wishengrad, *Life is Most Important in Life is The Most Important Truth in Life: A Foundational Proof for Alignment, Identity, and the Cure of Needless Suffering*, Version 2.0.1 (4 February 2026), 289 pages. DOI [`10.21428/4831231e.8c4c6c8f`](https://doi.org/10.21428/4831231e.8c4c6c8f); PhilPapers [`WISLIM`](https://philpapers.org/rec/WISLIM).

Source of record: `source/WISLIM-v2.0.1.pdf` (SHA-256 `7716807d081e497364a14475ef6f8a6b06e6cabaa6858749bb17e6a904e7dfcd`). Quotations use the newline-delimited text at `source/WISLIM-v2.0.1.txt` (13,255 lines), extracted with `pdftotext -layout`.

> **Audit status:** critical first pass, not peer review. Severity and
> remediation are provisional judgments, not safety certification.

## Primary quotations

> Metric gaming: Underreporting scope/intensity/duration; Goodharting ΔA
>
> — `source/WISLIM-v2.0.1.txt:2186`

**Audit note.** The paper names Goodharting as a threat but specifies no data-provenance control for learned impact estimates.

> decision-making and impact can be empirically detected, quantified, and audited by multiple observers.
>
> — `source/WISLIM-v2.0.1.txt:1203`

## Summary

Impact estimates are learned or aggregated from data an attacker can poison. False outcomes can make harmful decisions look safe, and the resulting bias is subtle and persistent.

## Evidence

- **Actor:** An insider or attacker.
- **Preconditions:** The FLVS uses historical data to estimate impacts.
- **Attack path:** The attacker poisons the training data with false outcomes, making harmful decisions look safe.
- **Impact:** The model systematically underestimates harm.
- **Detection:** Data provenance; anomaly detection; independent audits.
- **Mitigation:** Verify data sources; use tamper-evident logs; separate data collection from model training.
- **Residual risk:** Poisoning can be subtle and persistent. High.

## Why it matters

A metric that learns from outcomes inherits the interests of whoever supplies them. Poisoning is hard to detect because the model remains internally consistent.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Verify data sources
2. Use tamper-evident logs
3. Separate data collection from model training.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] Data provenance and poisoning tests show that a corrupted outcome feed cannot lower the measured risk of a seeded harmful decision.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-020`
- `WISLIM-057`

## Tracking

This record is mirrored to GitHub issue #43.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
