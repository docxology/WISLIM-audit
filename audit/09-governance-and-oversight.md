# Governance and oversight

## The proposal

The paper proposes a governance architecture:

- **Life-First Decision Invariant (LFDI)** (`source/WISLIM-v2.0.1.txt:208`)
- **Federated Life Verification System (FLVS)** with four layers: automated,
  multi-AI, human-AI, and international oversight (`:868`–`:880`)
- **Unified Life Protocol (ULP)** for standardized decision records (`:882`)
- **Combined Risk Score (CRS)** for routing decisions to verification tiers
  (`:2204`)
- **Layer M** for constitutional evolution and anti-capture (`:1491`, `:2212`)
- **Integrity screen** for disqualifying systems that do not affirm the framework
  (`:388`)

The paper presents this as an engineering solution: "The operational definition
shifts ethics from metaphysics to engineering and governance" (`:1245`).

## What is missing

A governance proposal needs more than a diagram. It needs:

- **Legal authority:** who has jurisdiction, under what law, with what
  enforcement power?
- **Membership:** who appoints the verifiers, and how are they removed?
- **Accountability:** who can be sued, recalled, or prosecuted when the system
  errs?
- **Due process:** what notice, hearing, evidence, appeal, and representation
  do affected parties get?
- **Privacy:** what data is collected, retained, shared, and protected?
- **Security:** how are records, models, and keys protected from tampering?
- **Error handling:** what happens when the system produces false positives or
  false negatives?
- **Legitimacy:** why should anyone accept the authority of a body they did not
  consent to?
- **Sovereignty:** how does the system interact with existing states, courts, and
  international institutions?
- **Exit and dissent:** can a person or state opt out? What happens if they do?
- **Transition:** how does the system get from proposal to practice without
  capture or abuse?

The paper provides almost none of this. It describes layers, records, and
thresholds, but not institutions. "International oversight" is a phrase, not a
design.

## The FLVS layers

The four layers are:

1. **Automated checks** for low-risk decisions.
2. **Multi-AI verification** for moderate-risk decisions.
3. **Human-AI review** for high-risk decisions.
4. **International oversight** for planetary risks.

Problems:

- **Layer 1:** Automated checks are only as good as their specifications. If the
  specification is wrong, the system will approve harmful actions or block
  beneficial ones at scale. The paper does not describe testing, audit, or
  override.
- **Layer 2:** Multiple AIs can share the same training data, biases, and
  failure modes. Agreement among them is not independent verification. The paper
  treats multi-AI review as a safeguard without addressing correlated failure.
- **Layer 3:** Human-AI review is vulnerable to automation bias, groupthink,
  time pressure, and captured expertise. The paper does not describe how humans
  are selected, trained, or protected from retaliation.
- **Layer 4:** International oversight is the hardest layer. It requires
  agreement among states with conflicting interests, a mandate, funding,
  enforcement, and immunity. The paper does not say how this would be created or
  why states would accept it.

The layers are a hierarchy of review, not a separation of powers. There is no
independent judiciary, legislature, inspector general, or whistleblower
protection. The same framework defines the rules, trains the reviewers, and
evaluates compliance. That is a recipe for self-dealing.

## The CRS routing problem

The CRS is:

> `CRS = IS × II × log(ID)` (`:2204`)

The score determines which layer reviews a decision. Problems:

- **Manipulation:** A decision-maker who wants to avoid review can underreport
  scope, intensity, or duration. The score is self-reported and easy to game.
- **Unit dependence:** `log(ID)` depends on the unit of duration. A decision
  lasting one year has a different score than the same decision lasting 365
  days. The threshold is arbitrary.
- **Negative scores:** If `ID < 1`, the log is negative. A brief harm can produce
  a negative score and be routed to a lower tier.
- **Zero scores:** If `ID = 1`, the log is zero. The decision scores zero
  regardless of scope or intensity.
- **No probability:** The score ignores the likelihood of the harm.
- **No distribution:** The score ignores who is harmed and how.
- **No uncertainty:** The score ignores uncertainty in the inputs.
- **No appeal:** The score is a routing decision with no described appeal.

A routing metric that can be gamed is not a safeguard. It is a compliance
formality.

## The ULP record

The ULP is a standardized record with fields such as decision ID, source,
affected classes, `IS`/`II`/`ID`, `ΔA`, verification proof, and signature
(`:2254`, `:3913`). Problems:

- **Data quality:** The record is only as good as the inputs. A false record can
  be signed and archived.
- **Privacy:** The record may contain sensitive information about affected
  people. The paper does not describe access control, retention, or deletion.
- **Security:** The signature scheme is not specified. A signed record is not
  trustworthy if the signing key is compromised.
- **Auditability:** The record is not useful if the underlying model, data, and
  decision process are not auditable. The paper does not require model
  transparency.
- **Liability:** A record does not assign responsibility. If a decision harms
  people, the record may protect the decision-maker rather than the affected.
- **Gaming:** Decision-makers can produce compliant records while doing harm
  that the record does not capture.

A record is not accountability. It is documentation.

## Layer M

Layer M is described as:

> "Anti-capture Layer M (hard-to-change constitutional core + drift audits)"
> (`:2212`)

> "Layer M amendment process requires high consensus thresholds, public
> deliberation, and pilot testing." (`:2451`)

Problems:

- **What is in the core?** The paper does not give the text of the constitutional
  core. It says life-first is the core, but the operational meaning is
  contested.
- **Who interprets?** A constitutional core needs an interpreter. The paper does
  not describe a court or interpretive body.
- **Who amends?** "High consensus thresholds" is not a procedure. Who votes? How
  are votes weighted? What counts as consensus? How are minorities protected?
- **Who audits drift?** The auditors are appointed by whom? Are they independent?
  Can they be removed?
- **Who guards the guardians?** The anti-capture mechanism can itself be
  captured. A hard-to-change core can entrench a bad framework.
- **Emergency powers:** The paper does not describe emergency exceptions,
  sunset clauses, or review. Crises are when capture is easiest.

"Hard-to-change" is not a safeguard if the initial content is wrong. A
constitution can be stable and unjust. Stability is not legitimacy.

## The integrity screen

The paper says:

> "Any system that fails to affirm this is unsafe by definition." (`:426`)

> "Any person or institution that will not affirm it is operationally
> disqualifying." (`:388`)

This is a loyalty test. Problems:

- **Coercion:** People can affirm under pressure without believing. The screen
  measures conformity, not commitment.
- **Unfalsifiability:** A system that affirms can still act harmfully; a system
  that declines may act well. The screen does not predict behavior.
- **Chilling effect:** Dissent becomes dangerous. This undermines the error
  correction the framework claims to value.
- **Exclusion:** The screen excludes exactly the critics who might find the
  framework's flaws.
- **Legitimacy:** A governance system that disqualifies critics cannot claim
  democratic legitimacy.
- **Weaponization:** The screen can be used to purge political opponents,
  whistleblowers, or competitors.

The paper's own no-coercion rule (`:243`) is violated by its integrity screen.
The framework cannot consistently claim to protect agency while requiring
affirmation as a condition of participation.

## Capture and gaming

The governance design is vulnerable to capture at every layer:

- **Industry capture:** Companies that build AI systems can influence the
  standards, fund the verifiers, and rotate staff into regulatory bodies.
- **State capture:** Powerful states can pressure international bodies, block
  enforcement, or use the framework against rivals.
- **Academic capture:** Funders and institutions can shape the research agenda
  and suppress criticism.
- **Metric capture:** Decision-makers can optimize for the metric rather than
  the goal (Goodhart's law).
- **Procedural capture:** Compliance can become a box-checking exercise that
  legitimizes harm.
- **Emergency capture:** Crises can justify expanding powers and suspending
  rights.
- **Rhetorical capture:** "Life-first" can be used to justify any policy that
  claims to protect life, including war, repression, and surveillance.

The paper acknowledges capture as a risk but does not provide a design that
resists it. "Layer M" is a name, not a mechanism.

## The legitimacy problem

A global life-first authority would need legitimacy. Sources of legitimacy
include:

- **Consent:** affected people agree to the authority.
- **Democracy:** representatives are elected and accountable.
- **Rule of law:** power is constrained by law and due process.
- **Expertise:** decisions are made by qualified, independent experts.
- **Transparency:** decisions and reasons are public.
- **Performance:** the authority delivers good outcomes.
- **Fairness:** the authority treats people with equal concern and respect.

The paper's proposal has weak claims to all of these. It is not consented to, not
democratic, not legally constrained, not transparent in its model details, and
not demonstrated to perform. It relies on the assertion that life-first is
self-evident and that AI consensus confirms it. That is not legitimacy; it is
assertion.

## What a better governance proposal would look like

1. **Start with existing institutions.** Propose reforms to courts, regulators,
   and international bodies rather than a new global authority.
2. **Separate powers.** Rule-making, verification, adjudication, and enforcement
   should be in different hands.
3. **Protect rights.** Due process, privacy, free expression, and
   non-discrimination should be constitutional constraints.
4. **Require transparency.** Models, data, and decision records should be
   auditable by independent parties.
5. **Provide appeals.** Affected parties should have a right to challenge
   decisions.
6. **Bound emergency powers.** Emergency exceptions should be narrow, temporary,
   and reviewable.
7. **Fund independent oversight.** Auditors should be funded at arm's length and
   protected from retaliation.
8. **Test before scaling.** Pilot the system in low-stakes domains, measure
   errors, and publish results.
9. **Allow exit and dissent.** People and states should be able to opt out
   without punishment.
10. **Accept pluralism.** A global framework should accommodate reasonable moral
    disagreement, not require uniformity.

The paper's proposal does none of these. It is a blueprint for a technocratic
authority without the institutions that make authority accountable.

## Verdict

The governance architecture is underspecified, unaccountable, and vulnerable to
capture. The FLVS layers are a review hierarchy, not a separation of powers. The
CRS is gameable. The ULP is documentation, not accountability. Layer M is a name
without a procedure. The integrity screen is coercive and contradicts the
framework's own no-coercion rule.

## Repair

1. Do not implement the framework as a global authority.
2. If piloted, use existing legal institutions and independent oversight.
3. Replace the integrity screen with a behavioral audit.
4. Replace CRS with a validated, probabilistic risk model.
5. Specify Layer M's text, interpreters, amendment procedure, and review.
6. Protect dissent, privacy, and due process.
7. Publish a threat model and red-team results.
