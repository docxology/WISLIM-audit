---
id: OPH-REP-003
review: OPH-LFDI-57
kind: reply-topic
status: observation
claim_kind: attribution
reply_lines: [8]
github_issue: 69
related: [OPH-REP-004, OPH-REP-013]
---

# OPH-REP-003: The quoted word 'incorrect' is not in the response

> **Status: audit observation, not a required fix.** This is a tracked note on one
> claim in a reply. It is not a verdict on anyone's character, and the sender may
> decline the suggested step with reasons. Comments on the matching issue are welcome.

## The reply says

> Daniel’s claim that the audit is "incorrect" stems
>
> — [`reviews/oph-lfdi-57/correspondence/03-wishengrad-reply.txt:8`](https://github.com/docxology/WISLIM-audit/blob/main/reviews/oph-lfdi-57/correspondence/03-wishengrad-reply.txt#L8)

## Summary

The note puts 'incorrect' in quotation marks as Daniel Ari Friedman's claim. The word occurs nowhere in the sent email or in this repository at the commit the email linked.

## Assessment

The response's own verbs were 'addressed', 'contradicted', and 'rest on premises OPH does not grant'. A word search of the as-sent text and of this repository at 6f19b85 returns zero hits for 'incorrect'; the test suite keeps that check on the as-sent text.

This repository did use a stronger label than the email at that commit: 'refuted', on four topics. That is a fair thing to object to, and it has been corrected (OPH-AUD-004). The objection here is to the quotation marks, which report a word that was not used.

A one-word verdict also skips the work. The response was a list of twelve tracked topics with quoted evidence, three different dispositions, and an offer to record any reply. Disagreement is most useful at that level, in this meta-philosophical and para-logical space above all, where the semantics are the subject. LFDI's own rule asks for 'epistemic transparency — no manipulation or misrepresentation'.

**Kind of claim:** `attribution`: attributes to the response or its author something the text does not say.

## Evidence

**The response as sent**

- [`02-friedman-response-as-sent.txt:9`](https://github.com/docxology/WISLIM-audit/blob/main/reviews/oph-lfdi-57/correspondence/02-friedman-response-as-sent.txt#L9)
  > 3 are addressed by
- [`02-friedman-response-as-sent.txt:10`](https://github.com/docxology/WISLIM-audit/blob/main/reviews/oph-lfdi-57/correspondence/02-friedman-response-as-sent.txt#L10)
  > 4 are contradicted by
- [`02-friedman-response-as-sent.txt:11`](https://github.com/docxology/WISLIM-audit/blob/main/reviews/oph-lfdi-57/correspondence/02-friedman-response-as-sent.txt#L11)
  > 5 rest on premises OPH does not grant

**WISLIM v2.0.1**

- [`source/WISLIM-v2.0.1.txt:238`](https://github.com/docxology/WISLIM-audit/blob/main/source/WISLIM-v2.0.1.txt#L238)
  > Actions that affect life must maintain epistemic transparency — no manipulation or misrepresentation.

**Related audit records**

- [`WISLIM-014`](https://github.com/docxology/WISLIM-audit/blob/main/docs/audit/WISLIM-014-make-the-no-coercion-rule-apply-to-the-framework-itself.md)

## What would move this forward

Say whether 'incorrect' is the sender's characterization or the bot's, and engage a specific topic record.

## Related

- `OPH-REP-004`
- `OPH-REP-013`

## Tracking

This record is generated. The canonical source is
`reviews/oph-lfdi-57/model/reply.json`; regenerate with `make reply`.
