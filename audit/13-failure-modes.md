# Failure modes

This catalogue names the ways the framework can fail. It is a design tool, not
a prediction. Each failure mode has an ID for reference in the red-team package.

## Argument and definition

| ID | Failure | Description | Consequence | Severity |
|---|---|---|---|---|
| F01 | Slogan ambiguity | The central sentence has no single well-formed reading. | The paper proves a precondition claim but asserts a priority claim. | Critical |
| F02 | Circular definition | "Life" is defined in terms of "life systems" without a base case. | The definition cannot ground moral status or scope. | Critical |
| F03 | Necessity/priority conflation | A necessary condition is treated as a lexically prior value. | Invalid inference from "without life, no value" to "life overrides all values." | Critical |
| F04 | Is-ought gap | Descriptive premises are used to support a normative conclusion. | The central moral premise is asserted, not defended. | Critical |
| F05 | Equivocation | "Life" shifts among biological life, sentience, agency, and moral patiency. | The framework overincludes and underincludes at the same time. | High |
| F06 | Unfalsifiability | "Irrefutable," "unsafe by definition," and "no legitimate rebuttal" define away criticism. | The framework cannot learn from error. | Critical |
| F07 | Motte-and-bailey | The modest precondition claim is used to defend the strong priority claim. | Critics are answered with a claim they did not challenge. | High |

## Formal and empirical

| ID | Failure | Description | Consequence | Severity |
|---|---|---|---|---|
| F08 | Toy formalism | `E∞ = (L₁ × U) / D` has undefined variables and a pole at `D = 0`. | The formula cannot rank actions or prove the thesis. | High |
| F09 | Trivial theorem | "If L = 0, then E∞ = 0" is arithmetic, not ethics. | The theorem does not establish moral priority. | High |
| F10 | Metric gaming | CRS is self-reported and easy to manipulate. | Decisions can be routed to lower scrutiny. | High |
| F11 | Unit dependence | `log(ID)` depends on the unit of duration. | The same harm gets different scores depending on measurement. | Medium |
| F12 | Correlated verification | Multi-AI review uses models with shared training data and biases. | Agreement is mistaken for independent verification. | High |
| F13 | Automation bias | Human reviewers defer to AI recommendations. | The human layer becomes a rubber stamp. | High |
| F14 | Stress-test illusion | 210 analogies create an impression of interdisciplinary proof. | Readers overestimate the evidence. | High |
| F15 | Citation laundering | Well-known AI safety works are cited without engaging their arguments. | The bibliography signals authority without support. | High |
| F16 | Consensus artifact | Shared-context, leading-prompt letters are treated as independent evidence. | The "100% consensus" claim is unverifiable. | Critical |

## Governance and institutions

| ID | Failure | Description | Consequence | Severity |
|---|---|---|---|---|
| F17 | Capture | Industry, states, or factions influence the verifiers. | The framework legitimizes the interests it claims to constrain. | Critical |
| F18 | Legitimacy deficit | A global authority is proposed without consent or democratic accountability. | Affected people have no reason to accept its authority. | Critical |
| F19 | Integrity-screen coercion | People must affirm the framework or be disqualified. | Dissent is punished; conformity is mistaken for commitment. | Critical |
| F20 | Silence-as-betrayal | Non-response is treated as moral guilt. | Chilling effect; critics are excluded. | Critical |
| F21 | Scope creep | "Life-affecting" expands to cover almost every decision. | The framework becomes a universal permit requirement. | High |
| F22 | Emergency powers | Crises justify suspending review and rights. | Capture is easiest when stakes are highest. | High |
| F23 | Liability vacuum | ULP records document decisions but do not assign responsibility. | No one is accountable when harm occurs. | High |
| F24 | Privacy erosion | Records contain sensitive data about affected people. | Surveillance and discrimination risks. | High |
| F25 | Security failure | Records and models can be tampered with or leaked. | Verification is unreliable. | High |
| F26 | Model drift | The AI models used for verification change over time. | Past approvals may not reflect current behavior. | Medium |
| F27 | Regulatory capture by formalism | Compliance becomes box-checking. | The framework legitimizes harm while appearing rigorous. | High |

## High-risk applications

| ID | Failure | Description | Consequence | Severity |
|---|---|---|---|---|
| F28 | Triage false positive | The framework blocks a life-saving procedure because it appears to trade lives. | Preventable death. | Critical |
| F29 | Triage false negative | The framework approves a harmful procedure because the metric misses the harm. | Preventable death or injury. | Critical |
| F30 | Suicide/euthanasia confusion | "Life may never be traded" conflicts with voluntary choice and agency. | Coercion or abandonment of vulnerable people. | Critical |
| F31 | AI moral status overclaim | AI systems are included as "life" without evidence of sentience or interests. | Resources and moral concern are diverted from beings with interests. | High |
| F32 | Animal/ecosystem flattening | Incommensurable moral statuses are aggregated into one metric. | Misallocation and moral blindness. | High |
| F33 | Political abuse | "Life-first" is used to justify repression, war, or surveillance. | The framework becomes a tool of power. | Critical |
| F34 | Martyrdom/sacrifice denial | The framework cannot accommodate voluntary sacrifice for a higher value. | It overrides deep moral commitments. | Medium |
| F35 | Cultural imperialism | A particular moral hierarchy is presented as universal. | Legitimate pluralism is suppressed. | High |

## Publication and provenance

| ID | Failure | Description | Consequence | Severity |
|---|---|---|---|---|
| F36 | Version ambiguity | PhilPapers says 8th edition; PDF says 2.0.1; PubPub says Release #1. | Readers cannot tell what they are citing. | Medium |
| F37 | License ambiguity | CC-BY 4.0 vs public-domain dedication. | Redistribution and reuse are legally unclear. | High |
| F38 | Missing raw data | No prompts, transcripts, model versions, or coding protocol. | The consensus claim cannot be reproduced. | High |
| F39 | Anecdotal reception | "Observed Reception" has no sample or method. | Non-response is misinterpreted as evidence. | High |
| F40 | No peer review | The work is self-published and not independently reviewed. | Errors persist; credibility is limited. | Medium |

## How failures interact

The failure modes compound:

- F02 (circular definition) enables F05 (equivocation), which enables F21
  (scope creep).
- F03 (necessity/priority) enables F07 (motte-and-bailey), which enables F19
  (integrity screen).
- F06 (unfalsifiability) enables F16 (consensus artifact) and F20
  (silence-as-betrayal).
- F10 (metric gaming) enables F17 (capture) and F27 (formalism capture).
- F28–F30 (high-risk applications) are the most dangerous because they involve
  immediate harm to vulnerable people.

## Priority for repair

The highest-priority failures are:

1. F19/F20 (coercion and silence-as-betrayal).
2. F28–F30 (high-risk applications).
3. F17/F18 (capture and legitimacy).
4. F02/F03/F04 (definition and inference).
5. F16/F38 (consensus and missing data).
6. F08/F10 (formalism and metrics).

These are addressed in `audit/14-repair-roadmap.md`.
