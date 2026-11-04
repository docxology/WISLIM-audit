---
id: OPH-REP-004
review: OPH-LFDI-57
kind: reply-topic
status: observation
claim_kind: attribution
reply_lines: [8]
github_issue: 70
related: [OPH-REP-003, OPH-REP-005, OPH-REP-006]
---

# OPH-REP-004: 'Choose not to grant' changes the subject of the sentence

> **Status: audit observation, not a required fix.** This is a tracked note on one
> claim in a reply. It is not a verdict on anyone's character, and the sender may
> decline the suggested step with reasons. Comments on the matching issue are welcome.

## The reply says

> his attempt to treat the LFDI as a set of philosophical "premises" he can simply choose not to grant, rather than the inescapable operational physics of decision-making.
>
> — [`reviews/oph-lfdi-57/correspondence/03-wishengrad-reply.txt:8`](https://github.com/docxology/WISLIM-audit/blob/main/reviews/oph-lfdi-57/correspondence/03-wishengrad-reply.txt#L8)

## Summary

The response said five review topics 'rest on premises OPH does not grant'. That is a checkable report about OPH's text. The note turns it into a personal choice, then treats declining a frame as declining physics.

## Assessment

'Rest on premises OPH does not grant' has OPH as its subject. A word search of the pinned commit finds no occurrence of LFDI, WISLIM, or Wishengrad, so the report can be checked by anyone. Nothing in that sentence is about what its author chooses.

The response's author states his position for this record: he rejects the idea that one specific framing of a cognitive encounter works as a mandate on others, binding them to its rules of language game. He does engage the inescapable relational, enactive, and cognitive setting, with an ontological pluralism. His paper on cognitive art and science says both things plainly: '[we have to exist for this exclaimation’s validity]' and 'different Alice’s respond differently to different Bob’s, as viewed by different Carla’s.'

'Operational physics' needs an argument too. In WISLIM v2.0.1 the LFDI is a conditional decision rule, `if action_affects_life(context)` with an `else: pass` branch. It is a proposed rule for action. Calling it physics does not make declining it a mistake about nature. The philosophical literature has names for the distinction: for Wittgenstein 'the speaking of language is part of an activity, or of a form of life', and Carnap's principle of tolerance says 'we are not in the business of setting up prohibitions but of arriving at conventions'.

**Kind of claim:** `attribution`: attributes to the response or its author something the text does not say.

## Evidence

**The response as sent**

- [`02-friedman-response-as-sent.txt:11`](https://github.com/docxology/WISLIM-audit/blob/main/reviews/oph-lfdi-57/correspondence/02-friedman-response-as-sent.txt#L11)
  > 5 rest on premises OPH does not grant

**WISLIM v2.0.1**

- [`source/WISLIM-v2.0.1.txt:212`](https://github.com/docxology/WISLIM-audit/blob/main/source/WISLIM-v2.0.1.txt#L212)
  > if action_affects_life(context):
- [`source/WISLIM-v2.0.1.txt:222`](https://github.com/docxology/WISLIM-audit/blob/main/source/WISLIM-v2.0.1.txt#L222)
  > else: pass

**Related audit records**

- [`WISLIM-012`](https://github.com/docxology/WISLIM-audit/blob/main/docs/audit/WISLIM-012-specify-or-withdraw-the-life-first-decision-invariant.md)

**Literature**

- Daniel Ari Friedman (2025), *On Cognitive Art & Science: Toward Wholeness From Both Sides*, version 1.0. DOI 10.5281/zenodo.16740439. [Link](https://zenodo.org/records/16740439)
- Ludwig Wittgenstein, *Philosophical Investigations*, §23, as quoted in Biletzki and Matar, "Ludwig Wittgenstein", *Stanford Encyclopedia of Philosophy*. [Link](https://plato.stanford.edu/entries/wittgenstein/)
- Rudolf Carnap, *The Logical Syntax of Language*, §17, as quoted in Leitgeb and Carus, "Rudolf Carnap", *Stanford Encyclopedia of Philosophy*. [Link](https://plato.stanford.edu/entries/carnap/)

## What would move this forward

Offer an argument that OPH must adopt the frame. Do not treat a report about what OPH says as a decision by one person.

## Related

- `OPH-REP-003`
- `OPH-REP-005`
- `OPH-REP-006`

## Tracking

This record is generated. The canonical source is
`reviews/oph-lfdi-57/model/reply.json`; regenerate with `make reply`.
