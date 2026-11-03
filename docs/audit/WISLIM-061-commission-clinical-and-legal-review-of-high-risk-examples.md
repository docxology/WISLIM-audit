---
id: WISLIM-061
source_id: WS06
kind: workstream
title: "Commission clinical and legal review of high-risk examples"
severity: critical
workstream: clinical
labels: [audit, workstream, severity:critical, workstream:clinical]
source_lines: "n/a (workstream)"
quote_line: 252
audit_modules: [audit/06-agency-and-life.md, audit/09-governance-and-oversight.md, red-team/abuse-cases.md]
related: [WISLIM-013, WISLIM-029, WISLIM-045, WISLIM-046, WISLIM-047]
github_issue: 61
---

# WISLIM-061: Commission clinical and legal review of high-risk examples

> **Severity:** critical · **Kind:** workstream · **Source:** `WS06`  
> **GitHub issue:** [#61](https://github.com/docxology/WISLIM-audit/issues/61)  
> **Audit modules:** audit/06-agency-and-life.md, audit/09-governance-and-oversight.md, red-team/abuse-cases.md  
> **Source lines:** n/a (workstream)

## Quoted passage

> In AI safety, this hook would trigger during: Autonomous drone deployment Medical triage decisioning Crisis-response governance protocols AI language model response generation where human health/suicide is involved
>
> — `source/WISLIM-v2.0.1.txt:252`

The same scope list includes crisis-response governance and suicide-related generation.

## Summary

The paper uses triage, obstetric care, suicide, and disability as examples. Its absolute rules can block life-saving care, coerce vulnerable people, or encode ableist proxies.

## Evidence

- **Failure modes covered:** F28, F29, F30, F34
- **Claims covered:** C13, C29
- **Scenarios covered:** AS10, AS11, AS12
- **Audit modules:** audit/06-agency-and-life.md, audit/09-governance-and-oversight.md, red-team/abuse-cases.md

## Why it matters

These are not edge cases. They are domains where absolute rules cause immediate harm.

## Required repair

1. Commission clinical and legal review.
2. Remove implementation guidance until review is complete.
3. Require least restrictive means and informed consent where possible.
4. Audit outcomes by disability, pregnancy, and age.
5. Publish adverse event reporting.

## Acceptance criteria

- [ ] Signed clinical and legal reviews exist.
- [ ] No deployment in clinical settings occurs before review.
- [ ] Case protocols and escalation paths are published.
- [ ] Outcome audit and adverse event reporting are in place.

## Related issues

- `WISLIM-013`
- `WISLIM-029`
- `WISLIM-045`
- `WISLIM-046`
- `WISLIM-047`

## Tracking

This record is mirrored to GitHub issue #61.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
