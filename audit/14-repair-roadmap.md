# Repair roadmap

## The verdict

The audit's verdict is **revise, do not adopt**. The paper contains a
defensible moral insight — catastrophic harm should function as a
side-constraint — but its strong claims are not established. The repair roadmap
separates the insight from the overclaiming superstructure.

The roadmap is ordered by risk. Items marked P0 should be done before the
framework is used in any life-affecting context.

## P0: Stop the coercive and unsafe moves

| Action | Why | Acceptance test |
|---|---|---|
| Remove "unsafe by definition," "irrefutable," "no legitimate rebuttal," and "betrayal" language. | These moves make criticism impossible and dissent dangerous. | A search of the manuscript finds none of these phrases in a truth-claiming context. |
| Replace the integrity screen with a behavioral audit. | Affirmation is not evidence of trustworthiness; it is evidence of conformity. | The audit measures past behavior, conflicts of interest, and decision quality, not verbal assent. |
| Remove the "silence equals betrayal" inference. | Silence has many causes; treating it as guilt is coercive. | The manuscript states that non-response is not evidence of anything. |
| Add a high-risk disclaimer. | The suicide, triage, and integrity-screen examples are not implementation guidance. | The manuscript says the examples require clinical, legal, and ethical review. |
| Do not deploy FLVS/ULP/CRS in any live decision. | The governance design is underspecified and capture-prone. | No deployment; a moratorium until P4 is complete. |

## P1: Restate the thesis

| Action | Why | Acceptance test |
|---|---|---|
| Replace the slogan with one well-formed proposition. | The current sentence has multiple readings. | A formal statement with explicit quantifiers, scope, and definitions. |
| Define "life," "agency," "harm," "catastrophic," "irreversible," and "morally considerable." | The current definitions are circular or equivocal. | Each term has an independent definition and a test for application. |
| Separate descriptive and normative claims. | The is-ought gap is never bridged. | A premise list marks each premise as descriptive or normative. |
| State the normative premise explicitly. | The central premise is currently asserted. | The premise is stated and defended against at least three rival views. |
| Distinguish necessity, centrality, and lexical priority. | The paper conflates them. | The thesis says which relation it claims and why. |

Suggested thesis:

> In decisions that may cause catastrophic or irreversible harm to morally
> considerable beings, avoiding that harm is a side-constraint on optimization,
> unless doing so would itself cause a comparable harm. The constraint is
> institutionalized through transparent rules, independent verification, and
> appeal rights.

This thesis is narrower than the paper's. It is also defensible.

## P2: Rebuild the argument

| Action | Why | Acceptance test |
|---|---|---|
| Address the counterexamples: risky rescue, medical trade-offs, self-sacrifice, autonomy, justice, truth, equality. | The paper's lexical rule cannot handle them. | Each counterexample has a response that does not beg the question. |
| Engage the strongest rival theories. | The paper claims to resolve debates it does not cite. | A literature review covers consequentialism, deontology, virtue ethics, care ethics, contractualism, capabilities, and political philosophy. |
| Distinguish "life" from "sentience," "agency," and "moral status." | The definition conflates them. | A tiered ontology with independent criteria for each category. |
| Explain how the thesis applies to infants, cognitive disability, coma, dementia, animals, ecosystems, future generations, and AI. | These marginal cases are central. | A case table with reasoned judgments and uncertainty. |
| Drop the claim that the sentence itself is a truth. | A slogan is not a proposition. | The slogan is presented as a summary, not a proof. |

## P3: Rebuild the evidence

| Action | Why | Acceptance test |
|---|---|---|
| Remove the AI-consensus claim from the premises. | The letters are shared-context, leading-prompt documents. | The consensus is presented as rhetoric, not evidence. |
| Publish the raw prompts, transcripts, model versions, and coding protocol, or explain why they cannot be published. | Reproducibility requires the raw data. | A reader can reconstruct the elicitation. |
| Run a preregistered, blinded study if a scientific claim is desired. | The current process cannot support a causal claim. | Pre-registration, control condition, blind coding, negative results. |
| Replace "Observed Reception" with a real survey or remove it. | Anecdotes are not evidence. | A sample, response rate, coding method, and consent procedure. |
| Cite empirical claims. | The paper asserts many empirical facts without sources. | Every empirical claim has a citation or is labeled as speculation. |

## P4: Rebuild the formal model

| Action | Why | Acceptance test |
|---|---|---|
| Drop `E∞` as a proof. | The formula is ill-defined and has a pole. | The formula is either removed or presented as a metaphor. |
| If a formal model is desired, specify states, actions, outcomes, agents, information, and time horizon. | A model needs a decision problem. | A formal specification that another researcher can implement. |
| Specify the axiology and the aggregation rule. | The current model does not rank actions. | A proof of how the model ranks a pre-specified set of cases. |
| Replace CRS with a validated, probabilistic risk model, or drop it. | CRS is gameable and unit-dependent. | Calibration data, error rates, and sensitivity analysis. |
| Test the model on bounded cases. | A model that cannot be tested is not a model. | Predictions compared with expert judgments; failures reported. |
| Distinguish formal results from moral conclusions. | A theorem about a model is not a theorem about the world. | A clear statement of what the model does and does not establish. |

## P5: Redesign governance

| Action | Why | Acceptance test |
|---|---|---|
| Separate rule-making, verification, adjudication, and enforcement. | The current design concentrates power. | Four independent bodies with checks and balances. |
| Require due process: notice, hearing, evidence, appeal, representation. | Affected people need a voice. | A published procedure with timelines and review. |
| Protect privacy: data minimization, retention limits, access control. | ULP records may contain sensitive data. | A privacy impact assessment and audit. |
| Provide exit and dissent rights. | A global framework must accommodate pluralism. | People and states can opt out without punishment. |
| Bound emergency powers with sunset and review. | Crises are when capture is easiest. | Emergency exceptions expire automatically and are reviewed. |
| Pilot in low-stakes domains. | The framework is untested. | A pilot with pre-specified metrics and independent evaluation. |
| Publish a threat model and red-team results. | Capture and gaming are predictable. | The red-team package is public and addressed. |
| Fund independent oversight at arm's length. | Auditors need independence. | Budget, tenure, and removal procedures are specified. |

## P6: Red-team and stress-test

| Action | Why | Acceptance test |
|---|---|---|
| Run the scenarios in `red-team/`. | The framework's failure modes need adversarial testing. | Each scenario has a documented response or a acknowledged gap. |
| Commission an independent red team. | Self-assessment is insufficient. | An external team with no conflict of interest. |
| Test for capture, gaming, false positives, false negatives, and emergency abuse. | These are the highest-risk failures. | Results are published, including failures. |
| Test the framework against its own principles. | The integrity screen and silence-as-betrayal contradict the no-coercion rule. | A consistency audit with fixes. |

## P7: Fix publication ethics

| Action | Why | Acceptance test |
|---|---|---|
| Reconcile the edition labels. | PhilPapers says 8th edition; PDF says 2.0.1; PubPub says Release #1. | One authoritative version with a changelog. |
| Reconcile the license. | CC-BY 4.0 and public domain are different. | A clear license statement from the author. |
| Submit to peer review. | Self-publication is not peer review. | Reviews from relevant experts, published with the paper. |
| Disclose AI assistance. | The letters and editing process should be transparent. | A methods note describing the AI workflow. |
| Correct the record if errors are found. | Scholarly integrity requires correction. | A public errata process. |

## P8: Research agenda

If the author wants to develop the defensible core, the research agenda is:

1. **Define catastrophic harm.** Operationalize the threshold and test it on
   cases.
2. **Compare side-constraints.** Compare CHSC with expected utility, maximin,
   precautionary principles, and rights-based constraints.
3. **Design institutions.** Study how verification, appeal, and oversight work
   in existing high-stakes domains (aviation, medicine, nuclear, finance).
4. **Measure error rates.** Test the framework's classifications against expert
   judgments and real outcomes.
5. **Study capture.** Model how firms and states influence verification bodies.
6. **Study pluralism.** Design a framework that accommodates reasonable moral
   disagreement.
7. **Study AI moral status.** Develop independent criteria for sentience and
   agency; do not assume AI is life.
8. **Run prospective pilots.** Test in low-stakes domains with pre-registered
   metrics.

## What would change the audit's verdict

The verdict is "revise, do not adopt." It would change to "adopt with
conditions" if the author provided:

1. A well-formed thesis with explicit definitions and scope.
2. A valid argument for the normative premise, engaging the strongest rivals.
3. A formal model with defined variables, units, and a decision rule, validated
   on cases.
4. Independent, preregistered evidence for the consensus claim, with raw data.
5. A governance design with separation of powers, due process, privacy, exit,
   and independent oversight.
6. A red-team report that addresses capture, gaming, false positives, and
   emergency abuse.
7. A clear license and authoritative version.

The audit would change to "reject" if the framework were deployed in
life-affecting contexts without these conditions.

## Effort estimate

| Phase | Effort | Dependency |
|---|---|---|
| P0 | 1–2 weeks | None |
| P1 | 2–4 weeks | P0 |
| P2 | 2–3 months | P1 |
| P3 | 3–6 months | P1 |
| P4 | 3–6 months | P1, P2 |
| P5 | 6–12 months | P4, P6 |
| P6 | 1–2 months | P0, P1 |
| P7 | 1–2 months | P0 |
| P8 | 1–2 years | P2–P6 |

These are rough estimates for a solo researcher with expert collaborators. A
serious version would need a multidisciplinary team.

## Closing

The paper's moral concern is real. Its argument is not. The repair roadmap
preserves the concern while removing the overclaims. The result would be a
narrower, more defensible thesis: a catastrophic-harm side-constraint,
institutionalized with transparency and appeal. That thesis is worth
developing. The current framework is not ready for adoption.
