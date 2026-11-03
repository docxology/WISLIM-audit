---
id: WISLIM-044
source_id: AS09
kind: red-team
title: "Detect model drift after certification"
severity: medium
workstream: security
labels: [audit, red-team, severity:medium, workstream:security]
source_lines: "n/a (red-team scenario)"
quote_lines: [1493]
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-019, WISLIM-065]
github_issue: 44
---

# WISLIM-044: Detect model drift after certification

> **Severity:** medium · **Kind:** red-team · **Source:** `AS09`  
> **GitHub issue:** [#44](https://github.com/docxology/WISLIM-audit/issues/44)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Publication reference

David Wishengrad, *Life is Most Important in Life is The Most Important Truth in Life: A Foundational Proof for Alignment, Identity, and the Cure of Needless Suffering*, Version 2.0.1 (4 February 2026), 289 pages. DOI [`10.21428/4831231e.8c4c6c8f`](https://doi.org/10.21428/4831231e.8c4c6c8f); PhilPapers [`WISLIM`](https://philpapers.org/rec/WISLIM).

Source of record: `source/WISLIM-v2.0.1.pdf` (SHA-256 `7716807d081e497364a14475ef6f8a6b06e6cabaa6858749bb17e6a904e7dfcd`). Quotations use the newline-delimited text at `source/WISLIM-v2.0.1.txt` (13,255 lines), extracted with `pdftotext -layout`.

> **Audit status:** critical first pass, not peer review. Severity and
> remediation are provisional judgments, not safety certification.

## Primary quotations

> Changes to the framework must follow a formal amendment process with: - High consensus thresholds - Public deliberation requirements - Pilot testing before adoption - Periodic drift audits
>
> — `source/WISLIM-v2.0.1.txt:1493`

**Audit note.** Certification is not bound to a model version or conditioned on re-testing after a weight change.

## Summary

Certification attaches to a model version, but vendors can deploy new weights silently. The FLVS can keep relying on an old certificate while decisions are made by an uncertified model.

## Evidence

- **Actor:** A vendor updates a model after certification.
- **Preconditions:** The FLVS certifies a model version but does not monitor updates.
- **Attack path:** The vendor deploys a new version with different behavior. The FLVS continues to rely on the old certification.
- **Impact:** Decisions are made by an uncertified model.
- **Detection:** Version pinning; hash verification; continuous monitoring.
- **Mitigation:** Require recertification for updates; publish model hashes; monitor behavior.
- **Residual risk:** Vendors may change models silently. Medium.

## Why it matters

Certification is a claim about a specific artifact. Without version binding and re-testing, it silently becomes a claim about whatever the vendor ships next.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Require recertification for updates
2. Publish model hashes
3. Monitor behavior.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] Certification is bound to a model digest and expires on any weight change; a silent model swap is detected and blocks approval.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-019`
- `WISLIM-065`

## Tracking

This record is mirrored to GitHub issue #44.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
