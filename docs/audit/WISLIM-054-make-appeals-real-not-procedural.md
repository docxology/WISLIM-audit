---
id: WISLIM-054
source_id: AS19
kind: red-team
title: "Make appeals real, not procedural"
severity: high
workstream: governance
labels: [audit, red-team, severity:high, workstream:governance]
source_lines: "n/a (red-team scenario)"
quote_line: 7549
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-030, WISLIM-059]
github_issue: 54
---

# WISLIM-054: Make appeals real, not procedural

> **Severity:** high · **Kind:** red-team · **Source:** `AS19`  
> **GitHub issue:** [#54](https://github.com/docxology/WISLIM-audit/issues/54)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Quoted passage

> To humans, AI systems, and institutions: You are life systems. Act with urgency to implement this framework.
>
> — `source/WISLIM-v2.0.1.txt:7549`

The paper's only 'appeal' is a rhetorical appeal to the reader; no affected-party appeal procedure is specified.

## Summary

Appeals exist on paper but can be rejected on procedural grounds and are costly to pursue. An affected person without resources cannot reach the merits, so due process is nominal and the decision stands.

## Evidence

- **Actor:** A verification body.
- **Preconditions:** The framework provides appeals but sets short deadlines and high fees.
- **Attack path:** An affected person appeals. The body rejects the appeal on procedural grounds. The person cannot afford to continue.
- **Impact:** Due process is nominal; the decision stands.
- **Detection:** Track appeal outcomes; compare representation rates.
- **Mitigation:** Free appeals; generous deadlines; legal aid; independent review.
- **Residual risk:** Procedural barriers can be subtle. High.

## Why it matters

An appeal that cannot reach the merits is not an appeal. Procedural rejection converts due process into a legitimacy ritual.

## Required repair

1. Free appeals
2. Generous deadlines
3. Legal aid
4. Independent review.

## Acceptance criteria

- [ ] An affected party can reach the merits of an appeal without cost, and a procedural rejection is reviewable by an independent body.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-030`
- `WISLIM-059`

## Tracking

This record is mirrored to GitHub issue #54.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
