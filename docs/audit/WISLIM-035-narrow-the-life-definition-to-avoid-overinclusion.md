---
id: WISLIM-035
source_id: C35
kind: claim
title: "Narrow the life definition to avoid overinclusion"
severity: high
workstream: scope
labels: [audit, claim, severity:high, workstream:scope]
source_lines: "788"
quote_line: 788
audit_modules: [audit/03-definition-of-life.md]
related: [WISLIM-006]
github_issue: 35
---

# WISLIM-035: Narrow the life definition to avoid overinclusion

> **Severity:** high · **Kind:** claim · **Source:** `C35`  
> **GitHub issue:** [#35](https://github.com/docxology/WISLIM-audit/issues/35)  
> **Audit modules:** audit/03-definition-of-life.md  
> **Source lines:** 788

## Quoted passage

> Inclusive: It covers humans, animals, AI, institutions, and ecosystems.
>
> — `source/WISLIM-v2.0.1.txt:788`

## Summary

The life definition is inclusive and anti-exclusion. Verdict: `overinclusive`. Including institutions, ecosystems, and AI without criteria creates moral standing for entities that may lack interests or agency in the relevant sense. It can dilute concern for sentient beings and make 'life-first' either vacuous or arbitrary.

## Evidence

- **Claim:** The life definition is inclusive and anti-exclusion.
- **Anchor:** "It covers humans, animals, AI, institutions, and ecosystems."
- **Source:** `source/WISLIM-v2.0.1.txt:788`
- **Verdict:** `overinclusive`; severity `high`.
- **Audit:** `audit/03-definition-of-life.md`

## Why it matters

The inclusive definition is the answer to exclusion objections. If it includes institutions and ecosystems without criteria, it licenses scope creep.

## Steelman and reply

The reply is that inclusion is a moral choice, not a metaphysical claim. Inclusion without criteria is not a choice the framework can defend; it lets any system claim protection and makes the scope ungovernable.

## Required repair

1. Use a tiered moral ontology with explicit criteria for interests, sentience, and agency.

## Acceptance criteria

- [ ] The manuscript resolves the defect in `C35` or removes the claim from the thesis.
- [ ] The repair is documented in `audit/03-definition-of-life.md` with a source anchor and reviewer sign-off.
- [ ] The claim registry entry `C35` is updated from `overinclusive` to a reviewed verdict.
- [ ] A regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-006`

## Tracking

This record is mirrored to GitHub issue #35.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
