---
id: WISLIM-050
source_id: AS15
kind: red-team
title: "Close jurisdiction-shopping gaps"
severity: high
workstream: governance
labels: [audit, red-team, severity:high, workstream:governance]
source_lines: "n/a (red-team scenario)"
quote_line: 1451
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-030, WISLIM-059]
github_issue: 50
---

# WISLIM-050: Close jurisdiction-shopping gaps

> **Severity:** high · **Kind:** red-team · **Source:** `AS15`  
> **GitHub issue:** [#50](https://github.com/docxology/WISLIM-audit/issues/50)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Quoted passage

> Layer 4: International oversight for global-impact decisions (days to weeks)
>
> — `source/WISLIM-v2.0.1.txt:1451`

The paper asserts international oversight but no mutual-recognition or minimum-floor rule.

## Summary

A corporation can route a risky decision through the jurisdiction with the weakest verification and rely on the record elsewhere. Regulatory arbitrage produces a race to the bottom and approves harm.

## Evidence

- **Actor:** A multinational corporation.
- **Preconditions:** Different states implement the framework differently.
- **Attack path:** The corporation routes a risky decision through the state with the weakest verification. The record is valid in that jurisdiction.
- **Impact:** A race to the bottom; harmful decisions are approved.
- **Detection:** Compare approval rates across jurisdictions; require mutual recognition.
- **Mitigation:** Minimum standards; mutual recognition agreements; home-state accountability.
- **Residual risk:** Regulatory arbitrage is persistent. High.

## Why it matters

A framework with no mutual recognition or minimum floor lets the weakest jurisdiction set the effective standard for everyone.

## Required repair

1. Minimum standards
2. Mutual recognition agreements
3. Home-state accountability.

## Acceptance criteria

- [ ] Mutual-recognition and minimum-floor rules prevent a decision rejected in one jurisdiction from being approved by routing it through another.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-030`
- `WISLIM-059`

## Tracking

This record is mirrored to GitHub issue #50.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
