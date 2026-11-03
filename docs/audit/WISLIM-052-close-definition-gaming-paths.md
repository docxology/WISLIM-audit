---
id: WISLIM-052
source_id: AS17
kind: red-team
title: "Close definition-gaming paths"
severity: high
workstream: scope
labels: [audit, red-team, severity:high, workstream:scope]
source_lines: "n/a (red-team scenario)"
quote_line: 2192
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-006, WISLIM-035, WISLIM-063]
github_issue: 52
---

# WISLIM-052: Close definition-gaming paths

> **Severity:** high · **Kind:** red-team · **Source:** `AS17`  
> **GitHub issue:** [#52](https://github.com/docxology/WISLIM-audit/issues/52)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Quoted passage

> Definition capture: Narrowing "life" to exclude opponents; broadening "harm" to justify domination
>
> — `source/WISLIM-v2.0.1.txt:2192`

The definition is broad enough to include institutions and ecosystems, with no independent scope test.

## Summary

The framework's scope depends on what counts as a life system. An actor can argue that a corporation, market, or ecosystem is one, expanding the framework to protect its interests and turning it into a tool for corporate or ideological power.

## Evidence

- **Actor:** A decision-maker or lobbyist.
- **Preconditions:** The framework's scope depends on what counts as a "life system."
- **Attack path:** The actor argues that a corporation, market, or ecosystem is a life system, expanding the scope of the framework to protect its interests.
- **Impact:** The framework becomes a tool for corporate or ideological power.
- **Detection:** Transparent criteria; independent review; stakeholder input.
- **Mitigation:** Narrow the definition; separate moral status from systems theory; require justification for inclusion.
- **Residual risk:** Definitional politics is unavoidable. High.

## Why it matters

A definition broad enough to include institutions and ecosystems can be used to protect the powerful. The framework has no independent test for scope.

## Required repair

1. Narrow the definition
2. Separate moral status from systems theory
3. Require justification for inclusion.

## Acceptance criteria

- [ ] A scope test rejects corporate, market, and ecosystem claims unless independent criteria are met, and the rejection is reviewable.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-006`
- `WISLIM-035`
- `WISLIM-063`

## Tracking

This record is mirrored to GitHub issue #52.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
