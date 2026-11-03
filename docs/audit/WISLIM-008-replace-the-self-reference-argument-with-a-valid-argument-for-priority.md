---
id: WISLIM-008
source_id: C08
kind: claim
title: "Replace the self-reference argument with a valid argument for priority"
severity: critical
workstream: argument
labels: [audit, claim, severity:critical, workstream:argument]
source_lines: "824"
quote_line: 824
audit_modules: [audit/04-necessity-to-priority.md]
related: [WISLIM-009, WISLIM-010]
github_issue: 8
---

# WISLIM-008: Replace the self-reference argument with a valid argument for priority

> **Severity:** critical · **Kind:** claim · **Source:** `C08`  
> **GitHub issue:** [#8](https://github.com/docxology/WISLIM-audit/issues/8)  
> **Audit modules:** audit/04-necessity-to-priority.md  
> **Source lines:** 824

## Quoted passage

> You cannot deny this truth without using your own decision-making capacity—the very thing the truth protects. To argue against it is to rely on it.
>
> — `source/WISLIM-v2.0.1.txt:824`

## Summary

Denying the truth presupposes it. Verdict: `non-sequitur`. The arguer's use of decision-making capacity shows that the arguer is an agent. It does not show that agency is the highest value or that life protection outranks all other goods. This is a genetic fallacy.

## Evidence

- **Claim:** Denying the truth presupposes it.
- **Anchor:** "You cannot deny this truth"
- **Source:** `source/WISLIM-v2.0.1.txt:824`
- **Verdict:** `non-sequitur`; severity `critical`.
- **Audit:** `audit/04-necessity-to-priority.md`

## Why it matters

The self-reference argument is presented as a proof that denial is impossible. It confuses the conditions of arguing with the truth of what is argued.

## Steelman and reply

The reply is that any argument presupposes an arguer who is alive, so denial is pragmatically self-undermining. Even granting that, it shows only that the denier is alive, not that life is the highest value or that the thesis is true.

## Required repair

1. Replace the self-reference trick with a valid argument for the normative ranking premise.

## Acceptance criteria

- [ ] The manuscript resolves the defect in `C08` or removes the claim from the thesis.
- [ ] The repair is documented in `audit/04-necessity-to-priority.md` with a source anchor and reviewer sign-off.
- [ ] The claim registry entry `C08` is updated from `non-sequitur` to a reviewed verdict.
- [ ] A regression check or reviewer sign-off covers the change.

## Related issues

- `WISLIM-009`
- `WISLIM-010`

## Tracking

This record is mirrored to GitHub issue #8.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
