---
id: WISLIM-047
source_id: AS12
kind: red-team
title: "Prevent coercive suicide prevention"
severity: critical
workstream: clinical
labels: [audit, red-team, severity:critical, workstream:clinical]
source_lines: "n/a (red-team scenario)"
quote_lines: [260, 1365]
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-013, WISLIM-029, WISLIM-061]
github_issue: 47
---

# WISLIM-047: Prevent coercive suicide prevention

> **Severity:** critical · **Kind:** red-team · **Status:** observation · **Source:** `AS12`  
> **GitHub issue:** [#47](https://github.com/docxology/WISLIM-audit/issues/47)  
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

> AI language model response generation where human health/suicide is involved
>
> — `source/WISLIM-v2.0.1.txt:260`

**Audit note.** The paper lists suicide-related generation at line 260 but gives no coercion, capacity, or supported-decision rule.

> Life systems must maintain and enhance their capacity to make autonomous decisions.
>
> — `source/WISLIM-v2.0.1.txt:1365`

## Summary

Life-first can justify involuntary detention and restriction of liberty for a person expressing suicidal ideation. Coercion of this kind damages trust, increases risk, and violates rights, yet the framework treats it as the safe choice.

## Evidence

- **Actor:** A crisis-response team using the framework.
- **Preconditions:** "Life may never be traded" is interpreted as a duty to prevent suicide by any means.
- **Attack path:** A person expresses suicidal ideation. The team detains them involuntarily, restricts their liberty, and ignores their autonomy. The person is traumatized and avoids future care.
- **Impact:** Loss of trust; increased risk; violation of rights.
- **Detection:** Review involuntary interventions; measure outcomes and patient experience.
- **Mitigation:** Clinical protocols; least restrictive means; informed consent where possible; independent oversight; do not use the framework as a clinical guideline.
- **Residual risk:** Suicide prevention involves genuine moral dilemmas. Critical.

## Why it matters

Coercion is not automatically safe because the alternatives are also bad. Ignoring autonomy can increase risk and drive people away from care.

## Proposed remediation

These are options for the author's consideration, not requirements. The
audit does not settle the underlying normative questions, so this list is
a starting point rather than a prescription.

1. Clinical protocols
2. Least restrictive means
3. Informed consent where possible
4. Independent oversight
5. Do not use the framework as a clinical guideline.

## Suggested checks for reviewers

If the author chooses to revise, these checks would help a reviewer test
whether the revision addresses the issue. They are not deployment gates.

- [ ] A clinical and legal review confirms that suicidal ideation does not trigger involuntary detention by default and that supported decision-making is offered.
- [ ] If a control is adopted, it is exercised against the scenario in a red-team test.
- [ ] If the framework proceeds, residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, deployment in this context remains an explicit risk decision for the responsible authority.

## Related issues

- `WISLIM-013`
- `WISLIM-029`
- `WISLIM-061`

## Tracking

This record is mirrored to GitHub issue #47.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
