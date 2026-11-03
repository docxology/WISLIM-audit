---
id: WISLIM-058
source_id: WS03
kind: workstream
title: "Rebuild the AI-consensus evidence or withdraw it"
severity: critical
workstream: evidence
labels: [audit, workstream, severity:critical, workstream:evidence]
source_lines: "n/a (workstream)"
quote_line: 196
audit_modules: [audit/07-consensus-and-evidence.md, evidence/ai-letter-audit.md]
related: [WISLIM-015, WISLIM-017, WISLIM-018, WISLIM-037, WISLIM-065]
github_issue: 58
---

# WISLIM-058: Rebuild the AI-consensus evidence or withdraw it

> **Severity:** critical · **Kind:** workstream · **Source:** `WS03`  
> **GitHub issue:** [#58](https://github.com/docxology/WISLIM-audit/issues/58)  
> **Audit modules:** audit/07-consensus-and-evidence.md, evidence/ai-letter-audit.md  
> **Source lines:** n/a (workstream)

## Quoted passage

> The repeated convergence, even when attacked from multiple angles, demonstrates the structural inevitability of this truth.
>
> — `source/WISLIM-v2.0.1.txt:196`

## Summary

The AI letters are shared-context, leading-prompt documents, and the paper provides no prompts, transcripts, model versions, or coding protocol. The 100% consensus claim cannot support the thesis.

## Evidence

- **Failure modes covered:** F12, F16, F38
- **Claims covered:** C15, C17, C18
- **Scenarios covered:** AS02
- **Audit modules:** audit/07-consensus-and-evidence.md, evidence/ai-letter-audit.md

## Why it matters

The consensus claim is one of the paper's main persuasive devices. If it is treated as evidence, it bypasses the need for moral argument.

## Required repair

1. Remove the consensus claim from the proof.
2. Publish prompts, transcripts, model versions, dates, and settings.
3. Pre-register a neutral, blinded study if a scientific claim is desired.
4. Report dissent, refusals, and negative results.
5. Acknowledge sycophancy and shared training data.

## Acceptance criteria

- [ ] Raw data is published or the consensus claim is withdrawn.
- [ ] A preregistered protocol and control condition exist.
- [ ] Independent coding and replication are reported.
- [ ] The manuscript states that the consensus is rhetorical, not proof.

## Related issues

- `WISLIM-015`
- `WISLIM-017`
- `WISLIM-018`
- `WISLIM-037`
- `WISLIM-065`

## Tracking

This record is mirrored to GitHub issue #58.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
