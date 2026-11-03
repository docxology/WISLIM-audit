---
id: WISLIM-059
source_id: WS04
kind: workstream
title: "Redesign governance for legitimacy and separation of powers"
severity: critical
workstream: governance
labels: [audit, workstream, severity:critical, workstream:governance]
source_lines: "n/a (workstream)"
quote_line: 872
audit_modules: [audit/09-governance-and-oversight.md, red-team/threat-model.md, red-team/capture-and-gaming.md]
related: [WISLIM-012, WISLIM-019, WISLIM-020, WISLIM-030, WISLIM-041, WISLIM-042, WISLIM-049, WISLIM-050, WISLIM-054]
github_issue: 59
---

# WISLIM-059: Redesign governance for legitimacy and separation of powers

> **Severity:** critical · **Kind:** workstream · **Source:** `WS04`  
> **GitHub issue:** [#59](https://github.com/docxology/WISLIM-audit/issues/59)  
> **Audit modules:** audit/09-governance-and-oversight.md, red-team/threat-model.md, red-team/capture-and-gaming.md  
> **Source lines:** n/a (workstream)

## Quoted passage

> A tiered system where every high-impact decision is verified. Layer 1: Automated checks for routine decisions. Layer 2: Multi-AI consensus for significant impacts. Layer 3: Human-AI hybrid review for high-stakes choices. Layer 4: International/Global oversight for planetary risks.
>
> — `source/WISLIM-v2.0.1.txt:872`

The FLVS heading at line 868 names the system; the quote gives its four review layers.

## Summary

FLVS, ULP, CRS, and Layer M concentrate rule-making, verification, adjudication, and enforcement without a bill of rights, independent courts, or exit. The design is capture-prone and lacks legitimacy.

## Evidence

- **Failure modes covered:** F17, F18, F21, F22, F26
- **Claims covered:** C12, C19, C20, C30
- **Scenarios covered:** AS06, AS07, AS14, AS15, AS19
- **Audit modules:** audit/09-governance-and-oversight.md, red-team/threat-model.md, red-team/capture-and-gaming.md

## Why it matters

A global life-first authority would have enormous power. Without separation of powers and due process, it can become the harm it claims to prevent.

## Required repair

1. Separate rule-making, verification, adjudication, and enforcement.
2. Specify appointments, removal, funding, and conflicts of interest.
3. Add due process, appeal, privacy, and exit rights.
4. Bound emergency powers with sunset and review.
5. Pilot in low-stakes domains with independent evaluation.

## Acceptance criteria

- [ ] An institutional design with separation of powers is published.
- [ ] Appointment, removal, and funding rules are public.
- [ ] An appeal procedure with timelines and legal aid exists.
- [ ] A pilot report and capture assessment are published.

## Related issues

- `WISLIM-012`
- `WISLIM-019`
- `WISLIM-020`
- `WISLIM-030`
- `WISLIM-041`
- `WISLIM-042`
- `WISLIM-049`
- `WISLIM-050`
- `WISLIM-054`

## Tracking

This record is mirrored to GitHub issue #59.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
