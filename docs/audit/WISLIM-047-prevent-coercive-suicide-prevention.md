---
id: WISLIM-047
source_id: AS12
kind: red-team
title: "Prevent coercive suicide prevention"
severity: critical
workstream: clinical
labels: [audit, red-team, severity:critical, workstream:clinical]
source_lines: "n/a (red-team scenario)"
quote_line: 260
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-013, WISLIM-029, WISLIM-061]
github_issue: 47
---

# WISLIM-047: Prevent coercive suicide prevention

> **Severity:** critical · **Kind:** red-team · **Source:** `AS12`  
> **GitHub issue:** [#47](https://github.com/docxology/WISLIM-audit/issues/47)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Quoted passage

> AI language model response generation where human health/suicide is involved
>
> — `source/WISLIM-v2.0.1.txt:260`

The paper lists suicide-related generation at line 260 but gives no coercion, capacity, or supported-decision rule.

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

## Required repair

1. Clinical protocols
2. Least restrictive means
3. Informed consent where possible
4. Independent oversight
5. Do not use the framework as a clinical guideline.

## Acceptance criteria

- [ ] A clinical and legal review confirms that suicidal ideation does not trigger involuntary detention by default and that supported decision-making is offered.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-013`
- `WISLIM-029`
- `WISLIM-061`

## Tracking

This record is mirrored to GitHub issue #47.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
