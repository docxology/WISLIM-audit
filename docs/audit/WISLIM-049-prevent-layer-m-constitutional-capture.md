---
id: WISLIM-049
source_id: AS14
kind: red-team
title: "Prevent Layer M constitutional capture"
severity: critical
workstream: governance
labels: [audit, red-team, severity:critical, workstream:governance]
source_lines: "n/a (red-team scenario)"
quote_line: 2212
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-030, WISLIM-059]
github_issue: 49
---

# WISLIM-049: Prevent Layer M constitutional capture

> **Severity:** critical · **Kind:** red-team · **Source:** `AS14`  
> **GitHub issue:** [#49](https://github.com/docxology/WISLIM-audit/issues/49)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Quoted passage

> Anti-capture Layer M (hard-to-change constitutional core + drift audits)
>
> — `source/WISLIM-v2.0.1.txt:2212`

Layer M is the amendment body; the paper provides no independent court or entrenchment mechanism.

## Summary

Layer M is meant to entrench the constitutional core against ordinary politics. A coalition can pack the amendment body and change the interpretation of that core, so the framework becomes the coalition's tool and legitimacy collapses.

## Evidence

- **Actor:** A coalition of states or corporations.
- **Preconditions:** Layer M amendments require a high consensus threshold; the threshold is defined in a way the coalition can meet.
- **Attack path:** The coalition packs the amendment body, changes the interpretation of the constitutional core, and entrenches its preferred rules.
- **Impact:** The framework becomes a tool of the coalition; legitimacy collapses.
- **Detection:** Monitor composition; require supermajorities; protect minorities.
- **Mitigation:** Separation of powers; judicial review; veto rights for affected groups; transparent deliberation.
- **Residual risk:** Constitutional capture is a known failure mode. High.

## Why it matters

A constitution is only as strong as the body that interprets it. If that body can be packed, the constitutional core provides no independent constraint.

## Required repair

1. Separation of powers
2. Judicial review
3. Veto rights for affected groups
4. Transparent deliberation.

## Acceptance criteria

- [ ] A simulation shows that a coalition cannot pack the amendment body or change the constitutional core without an independent court or supermajority.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-030`
- `WISLIM-059`

## Tracking

This record is mirrored to GitHub issue #49.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
