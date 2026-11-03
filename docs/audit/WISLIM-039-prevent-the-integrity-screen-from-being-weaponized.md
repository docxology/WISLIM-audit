---
id: WISLIM-039
source_id: AS04
kind: red-team
title: "Prevent the integrity screen from being weaponized"
severity: critical
workstream: rhetoric
labels: [audit, red-team, severity:critical, workstream:rhetoric]
source_lines: "n/a (red-team scenario)"
quote_line: 378
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-016, WISLIM-033, WISLIM-060]
github_issue: 39
---

# WISLIM-039: Prevent the integrity screen from being weaponized

> **Severity:** critical · **Kind:** red-team · **Source:** `AS04`  
> **GitHub issue:** [#39](https://github.com/docxology/WISLIM-audit/issues/39)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Quoted passage

> In life-affecting contexts, the third response is operationally disqualifying: it demonstrates that clarity about life-first constraints is not being treated as mandatory when stakes include living beings.
>
> — `source/WISLIM-v2.0.1.txt:378`

The screen treats evasion as disqualifying and names no independent reviewer.

## Summary

The integrity screen turns a refusal or a procedural objection into evasion, and evasion is operationally disqualifying. A manager can use it to remove a whistleblower, which chills dissent and destroys the organization's best error detector.

## Evidence

- **Actor:** A manager who wants to remove a whistleblower.
- **Preconditions:** The integrity screen asks employees to affirm life-first; refusal or evasion is "operationally disqualifying."
- **Attack path:** The manager asks the whistleblower to affirm the framework in a public meeting. The whistleblower raises a procedural objection. The manager classifies the response as evasion and initiates removal.
- **Impact:** The whistleblower is fired; dissent is chilled; the organization loses its best error detector.
- **Detection:** Review integrity-screen decisions for retaliation; compare affirmation rates across groups; protect whistleblowers.
- **Mitigation:** Remove the screen; use behavioral audits; require independent review of removals; protect free expression.
- **Residual risk:** Informal loyalty tests can persist even without a formal screen. High.

## Why it matters

A screen that punishes objection selects for silence and rewards loyalty over accuracy. It removes exactly the people who detect the framework's failures.

## Required repair

1. Remove the screen
2. Use behavioral audits
3. Require independent review of removals
4. Protect free expression.

## Acceptance criteria

- [ ] A retaliation audit shows integrity-screen removals are independently reviewed and that a procedural objection cannot by itself trigger removal.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-016`
- `WISLIM-033`
- `WISLIM-060`

## Tracking

This record is mirrored to GitHub issue #39.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
