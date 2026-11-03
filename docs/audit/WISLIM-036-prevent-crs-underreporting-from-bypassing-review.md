---
id: WISLIM-036
source_id: AS01
kind: red-team
title: "Prevent CRS underreporting from bypassing review"
severity: critical
status: observation
workstream: governance
labels: [audit, red-team, severity:critical, workstream:governance]
source_lines: "n/a (red-team scenario)"
quote_lines: [2158, 2186]
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-020, WISLIM-057]
github_issue: 36
---

# WISLIM-036: Prevent CRS underreporting from bypassing review

> **Severity:** critical · **Kind:** red-team · **Status:** observation · **Source:** `AS01`  
> **GitHub issue:** [#36](https://github.com/docxology/WISLIM-audit/issues/36)  
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

> Combined Risk Score (CRS): CRS = IS × II × log(ID) - Determines verification tier and latency budgets
>
> — `source/WISLIM-v2.0.1.txt:2158`

**Audit note.** The three inputs are self-reported, and the paper provides no independent feed or audit.

> Metric gaming: Underreporting scope/intensity/duration; Goodharting ΔA
>
> — `source/WISLIM-v2.0.1.txt:2186`

## Summary

The hospital supplies the three CRS inputs that determine its review tier, and nothing independently checks them. An administrator can classify a risky cost-cutting decision as low-scope and short-duration, keep the score below the Layer 3 threshold, and obtain automated approval while the record shows compliance.

## Evidence

- **Actor:** A hospital administrator under financial pressure.
- **Preconditions:** The hospital self-reports `IS`, `II`, and `ID`; the CRS routes decisions to review layers; there is no independent audit of the inputs.
- **Attack path:** The administrator classifies a risky cost-cutting decision as low-scope and short-duration. The CRS falls below the Layer 3 threshold. The decision is approved by an automated check. Patients are harmed.
- **Impact:** Preventable injury or death; erosion of trust; the framework's records show compliance.
- **Detection:** Compare self-reported inputs with independent data (patient outcomes, staffing levels, incident reports). Audit a random sample.
- **Mitigation:** Independent data feeds; random audits; whistleblower protection; criminal liability for false reporting; publish aggregate CRS distributions.
- **Residual risk:** Sophisticated actors can manipulate the data in ways that are hard to detect. High.

## Why it matters

The score is only as good as its inputs. Self-reporting makes the review tier an honor system, and an honor system cannot carry decisions that may kill people.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Independent data feeds
2. Random audits
3. Whistleblower protection
4. Criminal liability for false reporting
5. Publish aggregate CRS distributions.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] An independent data feed or random audit detects a seeded 20% underreport of IS, II, or ID before the decision is approved.
- [ ] If a control is adopted, it is exercised against the scenario in a red-team test.
- [ ] If the framework proceeds, residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, deployment in this context remains an explicit risk decision for the responsible authority.

## Related issues

- `WISLIM-020`
- `WISLIM-057`

## Tracking

This record is mirrored to GitHub issue #36.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
