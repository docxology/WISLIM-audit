---
id: WISLIM-012
source_id: C12
kind: claim
title: "Specify or withdraw the Life-First Decision Invariant"
severity: critical
workstream: governance
labels: [audit, claim, severity:critical, workstream:governance]
source_lines: "204"
quote_line: 204
audit_modules: [audit/09-governance-and-oversight.md, audit/06-agency-and-life.md]
related: [WISLIM-006, WISLIM-010, WISLIM-013, WISLIM-020, WISLIM-030]
github_issue: 12
---

# WISLIM-012: Specify or withdraw the Life-First Decision Invariant

> **Severity:** critical · **Kind:** claim · **Source:** `C12`  
> **GitHub issue:** [#12](https://github.com/docxology/WISLIM-audit/issues/12)  
> **Audit modules:** audit/09-governance-and-oversight.md, audit/06-agency-and-life.md  
> **Source lines:** 204

## Quoted passage

> We define a minimal, auditable protocol that any AI system, human institution, or policy engine must follow to guarantee safe alignment under the canonical truth:
>
> — `source/WISLIM-v2.0.1.txt:204`

## Summary

The Life-First Decision Invariant guarantees safe alignment. Verdict: `unsupported`. The predicates action_affects_life, preserves_life, explored_best_life_preserving_alternatives, and no_life-risking_deception_or_coercion are undefined. There is no algorithm, data model, failure analysis, or test. A 'terminal fault' can be triggered accidentally or exploited adversarially.

## Evidence

- **Claim:** The Life-First Decision Invariant guarantees safe alignment.
- **Anchor:** "a minimal, auditable protocol that any AI system"
- **Source:** `source/WISLIM-v2.0.1.txt:204`
- **Verdict:** `unsupported`; severity `critical`.
- **Audit:** `audit/09-governance-and-oversight.md`

## Why it matters

The invariant is the operational heart of the framework. If it cannot be implemented without halting on ordinary decisions, the framework is not deployable.

## Steelman and reply

The reply is that the invariant is a design pattern, not a decision procedure. A design pattern that halts on any action affecting life still needs the conflict rule the paper never supplies.

## Required repair

1. Specify formal semantics, implement in a sandbox, and evaluate against baselines with adversarial testing.

## Acceptance criteria

- [ ] The manuscript resolves the defect in `C12` or removes the claim from the thesis.
- [ ] The repair is documented in `audit/09-governance-and-oversight.md` with a source anchor and reviewer sign-off.
- [ ] The claim registry entry `C12` is updated from `unsupported` to a reviewed verdict.
- [ ] A regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-006`
- `WISLIM-010`
- `WISLIM-013`
- `WISLIM-020`
- `WISLIM-030`

## Tracking

This record is mirrored to GitHub issue #12.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
