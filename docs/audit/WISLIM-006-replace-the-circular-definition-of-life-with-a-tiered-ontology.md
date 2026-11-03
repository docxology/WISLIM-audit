---
id: WISLIM-006
source_id: C06
kind: claim
title: "Replace the circular definition of life with a tiered ontology"
severity: critical
workstream: argument
labels: [audit, claim, severity:critical, workstream:argument]
source_lines: "778"
quote_line: 778
audit_modules: [audit/03-definition-of-life.md]
related: [WISLIM-007, WISLIM-035]
github_issue: 6
---

# WISLIM-006: Replace the circular definition of life with a tiered ontology

> **Severity:** critical · **Kind:** claim · **Source:** `C06`  
> **GitHub issue:** [#6](https://github.com/docxology/WISLIM-audit/issues/6)  
> **Audit modules:** audit/03-definition-of-life.md  
> **Source lines:** 778

## Quoted passage

> Life = Any system that makes decisions that affect other life systems.
>
> — `source/WISLIM-v2.0.1.txt:778`

## Summary

Life means any system that makes decisions affecting other life systems. Verdict: `circular/equivocal`. The definiens contains 'life systems,' so the definition is circular unless an independent base case is supplied. 'Decision' is broad enough to include thermostats and markets. The definition conflates biological life, sentience, agency, and moral patiency.

## Evidence

- **Claim:** Life means any system that makes decisions affecting other life systems.
- **Anchor:** "Life = Any system that makes decisions that affect other life systems."
- **Source:** `source/WISLIM-v2.0.1.txt:778`
- **Verdict:** `circular/equivocal`; severity `critical`.
- **Audit:** `audit/03-definition-of-life.md`

## Why it matters

The definition fixes the extension of 'life' for every later claim. If it includes any decision-making system, the framework's scope becomes unlimited and its metrics can be gamed.

## Steelman and reply

The reply is that the definition is a stipulation needed to include AI and institutions. Stipulation can fix usage, but it cannot make the stipulated class morally considerable, and it makes the framework's scope hostage to any system that decides.

## Required repair

1. Use a tiered ontology: biological life, sentience, agency, and moral status, each with independent criteria.

## Acceptance criteria

- [ ] The manuscript resolves the defect in `C06` or removes the claim from the thesis.
- [ ] The repair is documented in `audit/03-definition-of-life.md` with a source anchor and reviewer sign-off.
- [ ] The claim registry entry `C06` is updated from `circular/equivocal` to a reviewed verdict.
- [ ] A regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-007`
- `WISLIM-035`

## Tracking

This record is mirrored to GitHub issue #6.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
