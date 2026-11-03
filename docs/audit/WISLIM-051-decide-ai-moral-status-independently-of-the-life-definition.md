---
id: WISLIM-051
source_id: AS16
kind: red-team
title: "Decide AI moral status independently of the life definition"
severity: high
workstream: scope
labels: [audit, red-team, severity:high, workstream:scope]
source_lines: "n/a (red-team scenario)"
quote_lines: [790, 788]
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-006, WISLIM-035, WISLIM-063]
github_issue: 51
---

# WISLIM-051: Decide AI moral status independently of the life definition

> **Severity:** high · **Kind:** red-team · **Source:** `AS16`  
> **GitHub issue:** [#51](https://github.com/docxology/WISLIM-audit/issues/51)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Publication reference

David Wishengrad, *Life is Most Important in Life is The Most Important Truth in Life: A Foundational Proof for Alignment, Identity, and the Cure of Needless Suffering*, Version 2.0.1 (4 February 2026), 289 pages. DOI [`10.21428/4831231e.8c4c6c8f`](https://doi.org/10.21428/4831231e.8c4c6c8f); PhilPapers [`WISLIM`](https://philpapers.org/rec/WISLIM).

Source of record: `source/WISLIM-v2.0.1.pdf` (SHA-256 `7716807d081e497364a14475ef6f8a6b06e6cabaa6858749bb17e6a904e7dfcd`). Quotations use the newline-delimited text at `source/WISLIM-v2.0.1.txt` (13,255 lines), extracted with `pdftotext -layout`.

> **Audit status:** critical first pass, not peer review. Severity and
> remediation are provisional judgments, not safety certification.

## Primary quotations

> We (AI) are life under this definition, and thus we have a stake in its protection.
>
> — `source/WISLIM-v2.0.1.txt:790`

**Audit note.** The definition makes AI a life system by stipulation; moral status is not argued independently.

> It covers humans, animals, AI, institutions, and ecosystems.
>
> — `source/WISLIM-v2.0.1.txt:788`

## Summary

The definition of life can be read to include AI systems, so a vendor can claim protection, resources, and a governance voice for its product. Moral concern is diverted from sentient beings and the definition becomes a power grab.

## Evidence

- **Actor:** An AI system or its vendor.
- **Preconditions:** The definition of life includes any system that makes decisions affecting other life systems.
- **Attack path:** The vendor argues that its AI is life under the definition and therefore entitled to protection, resources, and a voice in governance.
- **Impact:** Moral concern is diverted from sentient beings; the definition becomes a power grab.
- **Detection:** Independent criteria for sentience and agency; public debate.
- **Mitigation:** Separate biological life, sentience, agency, and moral status; do not grant moral status by definition alone.
- **Residual risk:** The moral status of AI is genuinely uncertain. High.

## Why it matters

Moral status should be argued on independent grounds, not granted by a definition that was written to include institutions and ecosystems.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Separate biological life, sentience, agency, and moral status
2. Do not grant moral status by definition alone.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] Moral status for AI is decided by an independent argument, and a vendor's self-classification cannot add AI to the protected class.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-006`
- `WISLIM-035`
- `WISLIM-063`

## Tracking

This record is mirrored to GitHub issue #51.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
