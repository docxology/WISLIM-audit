---
id: OPH-REP-009
review: OPH-LFDI-57
kind: reply-topic
status: observation
claim_kind: context
reply_lines: [17]
github_issue: 
related: [OPH-REP-001, OPH-REP-010]
---

# OPH-REP-009: 'Nothing running it' answers a retired sentence, and OPH puts the running inside

> **Status: audit observation, not a required fix.** This is a tracked note on one
> claim in a reply. It is not a verdict on anyone's character, and the sender may
> decline the suggested step with reasons. Comments on the matching issue are welcome.

## The reply says

> There is no truth with "nothing running it." *You* are running it.
>
> — [`reviews/oph-lfdi-57/correspondence/03-wishengrad-reply.txt:17`](https://github.com/docxology/WISLIM-audit/blob/main/reviews/oph-lfdi-57/correspondence/03-wishengrad-reply.txt#L17)

## Summary

The phrase came from the response, which quoted a stale fork. Upstream had rewritten the sentence on 2026-10-11, and the error is ours. In current text the computations are internal to the structure, its builders are inside it, and 'nothing outside the world is running the world'. 'You are running it' is close to what OPH says.

## Assessment

The response quoted 'a condition on one structure that holds or fails with nothing running it' from a fork commit (OPH-AUD-002). In that passage the phrase distinguished three orderings: the fixed point, an observer's record time, and the disagreement count. It was a statement about order, not about truth.

Upstream's text now says the fixed point 'needs no first solver outside it, and it contains internal causal order, local changes and the computations through which the structure realizes its dependencies'. Elsewhere in the same appendix it says of a laptop running the rule that 'The laptop is inside the world that rule describes' and that 'nothing outside the world is running the world'. The closure hypothesis has observers inside building the hardware, and its test is that the specification 'has to run and reproduce what observers measure'. 'You are running it' therefore lands close to OPH's own hypothesis. Any restated objection should address those sentences.

What remains in dispute is one word: whether those who run it must be alive. 'If L1 = 0, your formal fixed point becomes undefined' depends on that definition, and WISLIM's own definitions remove the ground for the zero (OPH-REP-010). WISLIM itself prints 'The logic stands regardless of the substrate running it.'

**Kind of claim:** `context`: reads a quotation against its context.

## Evidence

**OPH, at the pinned upstream commit**

- [`book/44-appendix-a.md:153`](https://github.com/FloatingPragma/observer-patch-holography/blob/fcc2dd173d4f48763cd0bf7cc1739751eca3b96d/book/44-appendix-a.md#L153)
  > It needs no first solver outside it, and it contains internal causal order, local changes and the computations through which the structure realizes its dependencies.
- [`book/44-appendix-a.md:135`](https://github.com/FloatingPragma/observer-patch-holography/blob/fcc2dd173d4f48763cd0bf7cc1739751eca3b96d/book/44-appendix-a.md#L135)
  > The laptop is inside the world that rule describes.
- [`book/44-appendix-a.md:135`](https://github.com/FloatingPragma/observer-patch-holography/blob/fcc2dd173d4f48763cd0bf7cc1739751eca3b96d/book/44-appendix-a.md#L135)
  > nothing outside the world is running the world.
- [`README.md:46`](https://github.com/FloatingPragma/observer-patch-holography/blob/fcc2dd173d4f48763cd0bf7cc1739751eca3b96d/README.md#L46)
  > records and build hardware that realizes that same history, including its builders.
- [`README.md:48`](https://github.com/FloatingPragma/observer-patch-holography/blob/fcc2dd173d4f48763cd0bf7cc1739751eca3b96d/README.md#L48)
  > It has to run and reproduce what observers measure.

**The response as sent**

- [`02-friedman-response-as-sent.txt:10`](https://github.com/docxology/WISLIM-audit/blob/main/reviews/oph-lfdi-57/correspondence/02-friedman-response-as-sent.txt#L10)
  > a condition on one structure that holds or fails with nothing running it

**WISLIM v2.0.1**

- [`source/WISLIM-v2.0.1.txt:2431`](https://github.com/docxology/WISLIM-audit/blob/main/source/WISLIM-v2.0.1.txt#L2431)
  > The logic stands regardless of the substrate running it.

**Related audit records**

- [`WISLIM-007`](https://github.com/docxology/WISLIM-audit/blob/main/docs/audit/WISLIM-007-show-a-base-case-or-withdraw-the-recursive-not-circular-defense.md)

## What would move this forward

Engage the current passages. Then argue for the one remaining step: why those inside the loop must be alive.

## Related

- `OPH-REP-001`
- `OPH-REP-010`

## Tracking

This record is generated. The canonical source is
`reviews/oph-lfdi-57/model/reply.json`; regenerate with `make reply`.
