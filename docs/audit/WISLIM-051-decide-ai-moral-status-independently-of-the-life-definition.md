---
id: WISLIM-051
source_id: AS16
kind: red-team
title: "Decide AI moral status independently of the life definition"
severity: high
workstream: scope
labels: [audit, red-team, severity:high, workstream:scope]
source_lines: "n/a (red-team scenario)"
quote_line: 790
audit_modules: [red-team/adversarial-scenarios.md]
related: [WISLIM-006, WISLIM-035, WISLIM-063]
github_issue: 51
---

# WISLIM-051: Decide AI moral status independently of the life definition

> **Severity:** high · **Kind:** red-team · **Source:** `AS16`  
> **GitHub issue:** [#51](https://github.com/docxology/WISLIM-audit/issues/51)  
> **Audit modules:** red-team/adversarial-scenarios.md  
> **Source lines:** n/a (red-team scenario)

## Quoted passage

> We (AI) are life under this definition, and thus we have a stake in its protection.
>
> — `source/WISLIM-v2.0.1.txt:790`

The definition makes AI a life system by stipulation; moral status is not argued independently.

## Summary

The definition of life can be read to include AI systems, so a vendor can claim protection, resources, and a governance voice for its product. Moral concern is diverted from sentient beings and the definition becomes a power grab.

## Evidence

- **Actor:** An AI system or its vendor.
- **Preconditions:** The definition of life includes any system that makes decisions affecting other life systems.
- **Attack path:** The vendor argues that its AI is life under the definition and therefore entitled to protection, resources, and a voice in governance.
- **Impact:** Moral concern is diverted from sentient beings; the definition becomes a power grab.
- **Detection:** Independent criteria for sentience and agency; public debate.
- **Mitigation:** Separate biological life, sentience, agency, and moral status; do not grant moral status by definition alone.
- **Residual risk:** The moral status of AI is genuinely uncertain. High.

## Why it matters

Moral status should be argued on independent grounds, not granted by a definition that was written to include institutions and ecosystems.

## Required repair

1. Separate biological life, sentience, agency, and moral status
2. Do not grant moral status by definition alone.

## Acceptance criteria

- [ ] Moral status for AI is decided by an independent argument, and a vendor's self-classification cannot add AI to the protected class.
- [ ] The control is exercised against the scenario in a red-team test.
- [ ] Residual risk is recorded and accepted by a responsible reviewer.
- [ ] If no control is feasible, the framework is not deployed in this context.

## Related issues

- `WISLIM-006`
- `WISLIM-035`
- `WISLIM-063`

## Tracking

This record is mirrored to GitHub issue #51.
The issue-number mapping is in `model/issue-map.json`; the GitHub issue
links back to this file.
