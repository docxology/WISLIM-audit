---
id: WISLIM-065
source_id: WS10
kind: workstream
title: "Rebuild evidence quality, citations, and human review"
severity: high
workstream: evidence
labels: [audit, workstream, severity:high, workstream:evidence]
source_lines: "n/a (workstream)"
quote_line: 392
audit_modules: [audit/11-citations-and-scholarship.md, evidence/citation-audit.md]
related: [WISLIM-021, WISLIM-027, WISLIM-028, WISLIM-032, WISLIM-037, WISLIM-044]
github_issue: 65
---

# WISLIM-065: Rebuild evidence quality, citations, and human review

> **Severity:** high · **Kind:** workstream · **Source:** `WS10`  
> **GitHub issue:** [#65](https://github.com/docxology/WISLIM-audit/issues/65)  
> **Audit modules:** audit/11-citations-and-scholarship.md, evidence/citation-audit.md  
> **Source lines:** n/a (workstream)

## Quoted passage

> See Appendix C for full references to Bostrom, Christiano, Friston, Hadfield-Menell, Leike, Ord, O'Keefe, Russell, Yudkowsky, and others.
>
> — `source/WISLIM-v2.0.1.txt:392`

## Summary

The bibliography is AI-alignment background, not ethics. The reception claim is anecdotal, and human review is vulnerable to automation bias. The paper does not engage the literature it claims to resolve.

## Evidence

- **Failure modes covered:** F13, F15, F39
- **Claims covered:** C21, C27, C28, C32
- **Scenarios covered:** AS02, AS09
- **Audit modules:** audit/11-citations-and-scholarship.md, evidence/citation-audit.md

## Why it matters

Without engaged scholarship and independent human review, the paper cannot know whether its objections have already been answered.

## Required repair

1. Add a substantive literature review.
2. Map every citation to the claim it supports.
3. Replace anecdotal reception with a survey or remove it.
4. Measure automation bias and reviewer independence.
5. Publish negative results.

## Acceptance criteria

- [ ] A citation-to-claim table exists.
- [ ] A literature review covers the major ethical traditions.
- [ ] The reception study is completed or removed.
- [ ] A human-review bias assessment is published.

## Related issues

- `WISLIM-021`
- `WISLIM-027`
- `WISLIM-028`
- `WISLIM-032`
- `WISLIM-037`
- `WISLIM-044`

## Tracking

This record is mirrored to GitHub issue #65.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
