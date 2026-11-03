---
id: WISLIM-042
source_id: AS07
kind: red-team
title: "Prevent vendor capture of the FLVS"
severity: high
status: observation
workstream: governance
labels: [audit, red-team, severity:high, workstream:governance]
source_lines: "n/a (red-team scenario)"
quote_lines: [2188, 2206]
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-030, WISLIM-059]
github_issue: 42
---

# WISLIM-042: Prevent vendor capture of the FLVS

> **Severity:** high · **Kind:** red-team · **Status:** observation · **Source:** `AS07`  
> **GitHub issue:** [#42](https://github.com/docxology/WISLIM-audit/issues/42)  
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

> Verifier capture: Bribery, coercion, collusion, regulatory capture
>
> — `source/WISLIM-v2.0.1.txt:2188`

**Audit note.** The paper lists verifier capture as a threat but does not separate the certifier from the vendors it regulates.

> Separation of duties (the proposer cannot be the sole verifier)
>
> — `source/WISLIM-v2.0.1.txt:2206`

## Summary

Certification depends on a body whose staff, standards, and tests can be shaped by the vendors it regulates. A vendor can place former employees in verification roles and set standards that its own models meet more easily, turning the FLVS into a barrier to entry.

## Evidence

- **Actor:** A large AI vendor.
- **Preconditions:** The vendor supplies models, funds research, and rotates staff into the FLVS.
- **Attack path:** The vendor places former employees in key verification roles. The FLVS adopts standards that favor the vendor's models. Competing models are slower or more expensive to certify.
- **Impact:** Regulatory capture; barriers to entry; the framework becomes a moat.
- **Detection:** Track revolving doors; disclose funding; require cooling-off periods.
- **Mitigation:** Independent funding; conflict-of-interest rules; transparent standards; multiple vendors.
- **Residual risk:** Capture is gradual and hard to detect. High.

## Why it matters

A certifier that depends on the regulated vendors for staff, revenue, and standards has an incentive to certify the incumbents and exclude entrants.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Independent funding
2. Conflict-of-interest rules
3. Transparent standards
4. Multiple vendors.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] The certifier's staff, funding, and standards are independent of vendors, and a blinded certification test shows no incumbent advantage.
- [ ] If a control is adopted, it is exercised against the scenario in a red-team test.
- [ ] If the framework proceeds, residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, deployment in this context remains an explicit risk decision for the responsible authority.

## Related issues

- `WISLIM-030`
- `WISLIM-059`

## Tracking

This record is mirrored to GitHub issue #42.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
