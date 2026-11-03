---
id: WISLIM-063
source_id: WS08
kind: workstream
title: "Separate biological life, sentience, agency, and moral status"
severity: high
workstream: scope
labels: [audit, workstream, severity:high, workstream:scope]
source_lines: "n/a (workstream)"
quote_line: 778
audit_modules: [audit/03-definition-of-life.md, audit/06-agency-and-life.md]
related: [WISLIM-006, WISLIM-035, WISLIM-051, WISLIM-052]
github_issue: 63
---

# WISLIM-063: Separate biological life, sentience, agency, and moral status

> **Severity:** high · **Kind:** workstream · **Source:** `WS08`  
> **GitHub issue:** [#63](https://github.com/docxology/WISLIM-audit/issues/63)  
> **Audit modules:** audit/03-definition-of-life.md, audit/06-agency-and-life.md  
> **Source lines:** n/a (workstream)

## Quoted passage

> Life = Any system that makes decisions that affect other life systems.
>
> — `source/WISLIM-v2.0.1.txt:778`

## Summary

The definition includes humans, animals, AI, institutions, and ecosystems, but does not distinguish their moral status. It also excludes or marginalizes beings without decision-making capacity.

## Evidence

- **Failure modes covered:** F31, F32, F35
- **Claims covered:** C06, C35
- **Scenarios covered:** AS16, AS17
- **Audit modules:** audit/03-definition-of-life.md, audit/06-agency-and-life.md

## Why it matters

A category that includes everything cannot guide trade-offs. A category that requires agency repeats the exclusion the paper claims to oppose.

## Required repair

1. Adopt a tiered ontology: biological life, sentience, agency, and moral status.
2. Specify criteria for each tier.
3. Address infants, cognitive disability, coma, dementia, animals, ecosystems, future generations, and AI.
4. Consult disability and animal-ethics experts.

## Acceptance criteria

- [ ] A published taxonomy and criteria exist.
- [ ] A case table covers the marginal cases.
- [ ] Independent review is completed.
- [ ] The scope statement appears in the thesis.

## Related issues

- `WISLIM-006`
- `WISLIM-035`
- `WISLIM-051`
- `WISLIM-052`

## Tracking

This record is mirrored to GitHub issue #63.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
