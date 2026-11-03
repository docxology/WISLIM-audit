---
id: WISLIM-060
source_id: WS05
kind: workstream
title: "Remove coercive loyalty tests and protect dissent"
severity: critical
workstream: rhetoric
labels: [audit, workstream, severity:critical, workstream:rhetoric]
source_lines: "n/a (workstream)"
quote_line: 364
audit_modules: [audit/10-rhetoric-and-coercion.md, red-team/abuse-cases.md]
related: [WISLIM-004, WISLIM-014, WISLIM-016, WISLIM-024, WISLIM-033, WISLIM-039, WISLIM-040, WISLIM-055]
github_issue: 60
---

# WISLIM-060: Remove coercive loyalty tests and protect dissent

> **Severity:** critical · **Kind:** workstream · **Source:** `WS05`  
> **GitHub issue:** [#60](https://github.com/docxology/WISLIM-audit/issues/60)  
> **Audit modules:** audit/10-rhetoric-and-coercion.md, red-team/abuse-cases.md  
> **Source lines:** n/a (workstream)

## Quoted passage

> Practical Application: Integrity Screen for Trust in Life-Affecting Roles: Because life is treated here as the supreme decision constraint, a person or organization’s trustworthiness in life-affecting roles can be screened by how they respond when asked to affirm (or rebut) that constraint.
>
> — `source/WISLIM-v2.0.1.txt:364`

## Summary

The integrity screen, 'silence equals betrayal,' and 'unsafe by definition' turn disagreement into disqualification. This is coercive and contradicts the framework's own no-coercion rule.

## Evidence

- **Failure modes covered:** F19, F20, F23, F33
- **Claims covered:** C04, C14, C16, C24, C33
- **Scenarios covered:** AS04, AS05, AS20
- **Audit modules:** audit/10-rhetoric-and-coercion.md, red-team/abuse-cases.md

## Why it matters

A framework that cannot distinguish criticism from betrayal cannot correct its errors. The people most likely to find the flaw are the ones it excludes.

## Required repair

1. Remove the integrity screen and loyalty test.
2. Replace affirmation with a behavioral audit.
3. Remove silence-as-betrayal and unsafe-by-definition language.
4. Protect whistleblowers and dissent.
5. Publish a correction and retaliation policy.

## Acceptance criteria

- [ ] No affirmation-based disqualification remains.
- [ ] Behavioral audit criteria are published.
- [ ] A dissent and whistleblower policy is adopted.
- [ ] A retaliation audit is completed.

## Related issues

- `WISLIM-004`
- `WISLIM-014`
- `WISLIM-016`
- `WISLIM-024`
- `WISLIM-033`
- `WISLIM-039`
- `WISLIM-040`
- `WISLIM-055`

## Tracking

This record is mirrored to GitHub issue #60.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
