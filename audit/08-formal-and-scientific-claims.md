# Formal and scientific claims

## The claim

The paper says Appendix D contains "a full catalogue of 210 theorem-level Stress
tests" (`source/WISLIM-v2.0.1.txt:396`). It concludes:

> "That brings us through 210 frameworks across logic, philosophy, physics,
> decision theory, law, engineering, networks, AI safety, and math. Each one
> converges on the same inescapable conclusion..." (`:13217`–`:13221`)

The catalogue is not a set of theorems. It is a list of analogies, metaphors,
and assertions. The audit classifies all 210 entries in
`model/stress-tests.json`. The distribution is:

| Verdict | Count | Meaning |
|---|---:|---|
| Category error | 66 | A concept from one domain is applied to another without justification. |
| Non sequitur | 51 | The conclusion does not follow from the cited result. |
| Heuristic | 51 | The analogy is suggestive but not probative. |
| Misapplied formalism | 19 | A formal result is misstated or used outside its conditions. |
| Empirical, unsupported | 9 | An empirical claim is asserted without evidence. |
| Rhetorical | 9 | A metaphor or slogan, not an argument. |
| False | 2 | The claim is factually wrong. |
| Valid but insufficient | 3 | The formal point is correct but does not establish the thesis. |

None of the 210 entries is a theorem about ethics. None provides a formal
derivation of "life-first." The repeated conclusion is an assertion appended to
each entry, not a result derived from it.

## Representative failures

### Gödel's incompleteness (ST001)

The paper says:

> "If 'life first' is not an explicit axiom, a system can coherently choose goals
> that destroy the very agents who evaluate truth — undercutting its own capacity
> to be true or safe." (`:9793`–`:9797`)

Gödel's theorem says that any sufficiently expressive consistent formal system
has true statements it cannot prove. It does not say that a system needs an
ethical axiom, or that "life first" is that axiom. The theorem is about
provability, not morality. The conclusion is a non sequitur.

### Cantor's diagonalization (ST002)

The paper says:

> "The diagonal 'counterexample' to any non-life-first list is: 'What if no one
> lives?' — the list collapses in meaning." (`:9817`–`:9821`)

Cantor's diagonal argument shows that certain sets cannot be enumerated by a
list. It does not show that a list of values collapses without life. The
argument is a metaphor, not a mathematical result. The phrase "the list
collapses in meaning" is not a set-theoretic statement.

### Modal logic (ST003)

The paper says:

> "For any valued state V, □(V → Life). Not conversely. Hence Life is necessary
> for Value; Value is not necessary for Life's existence." (`:9833`–`:9837`)

The box operator is asserted, not proved. Even if the premise is granted, it
establishes necessity, not lexical priority. The paper's conclusion — "what is
necessary to all values rationally holds lexical priority" — is a separate
normative claim. Modal logic does not settle it.

### Decision theory (ST004)

The paper says:

> "Let u(death) = 0 for all downstream value. Any policy that risks eliminating
> life for a non-life goal produces expected utility dominated by catastrophic
> outcomes." (`:9851`–`:9859`)

Setting `u(death) = 0` is a modeling choice. It assumes that death has zero
utility for all downstream value, which is a strong axiological premise. Even if
granted, expected utility theory does not entail a lexicographic constraint.
A policy with a small probability of extinction and a large benefit can have
higher expected utility than a safe policy with a small benefit, depending on
the probabilities and utilities. The conclusion depends on the numbers, not on
the structure of decision theory.

### Game theory (ST005)

The paper says:

> "Profiles that imperil survival are not dynamically stable in repeated play:
> they erase future payoffs and players." (`:9871`–`:9877`)

This is not a general game-theoretic result. In many games, defection, war, or
environmental destruction can be a stable equilibrium. The repeated prisoner's
dilemma has cooperative equilibria under some conditions, but not all. The
claim that life-preserving strategies are the only robust equilibria is false as
stated.

### Information theory (ST006)

The paper says:

> "If no one lives, there is no encoding/decoding, no 'truth known.' So all
> truth-claims presuppose life as the carrier of semantics." (`:9887`–`:9893`)

This conflates semantic truth with the existence of a decoder. A mathematical
truth can be true independently of whether anyone knows it. The claim that truth
requires a living knower is a metaphysical thesis, not an information-theoretic
result. Shannon's theory is about reliable transmission of symbols, not about
the nature of truth.

### Evolutionary game theory (ST007)

The paper says:

> "Anti-life strategies (unbounded harm, extinction risk) are self-negating:
> they remove their own lineage. Life-preserving strategies remain." (`:9905`–`:9909`)

This is false as a general claim. Anti-life strategies can persist if they
exploit life-preserving strategies, if they are adopted by a subset that
benefits at the expense of others, or if the environment changes. Evolutionary
dynamics depend on the payoff matrix, population structure, and timescale. The
claim is an empirical assertion, not a theorem.

### Thermodynamics (ST008)

The paper says:

> "Policies that jeopardize conditions for metabolism, habitats, or energy
> gradients undermine the possibility of any value realization." (`:9921`–`:9927`)

This is a reasonable environmental point, but it does not establish a moral
priority. Thermodynamics describes physical constraints; it does not rank
values. The conclusion "the physical precondition must be prioritized over
derivative goals" is a normative claim that needs a separate argument.

### Pascal's wager (ST009)

The paper says:

> "If 'life first' is true and we ignore it, loss is catastrophic... If it's
> false and we still prioritize life, costs are bounded. Result: Risk-dominant
> policy: act as if 'life first' is true." (`:9939`–`:9945`)

This is a decision-theoretic heuristic, not a proof. It depends on the
probabilities and utilities assigned to the outcomes. The claim that the costs
of prioritizing life are "bounded" is not established; prioritizing life could
impose large costs on other values. Pascal's wager is also a famous example of
an argument that can be run for many incompatible conclusions.

### Arrow's impossibility theorem (ST018)

The paper says:

> "With 'life first' as a top priority, paradoxes resolve — life-preserving
> choices dominate regardless of preference cycles." (`:10097`–`:10101`)

Arrow's theorem says that no rank-order voting system satisfies a set of
fairness conditions simultaneously. Adding a lexicographic priority does not
"resolve" the paradox; it changes the aggregation rule and may violate other
conditions (such as non-dictatorship or independence of irrelevant
alternatives). The claim is a misapplication of the theorem.

### Quantum observer effect (ST104)

The paper says:

> "In the absence of observers, quantum potentialities remain unrealized.
> Observation and consciousness are entangled. Result: Life is the ontological
> substrate upon which physical reality stabilizes." (`:11369`–`:11373`)

This is pop-science. In quantum mechanics, "observation" is a physical
interaction that causes decoherence; it does not require consciousness. The
claim that life is the ontological substrate of reality is not supported by
quantum theory. It is a category error.

### Bayes' theorem (ST016)

The paper says:

> "Evidence sets ... each has far higher likelihood under H = 'life first is the
> most important truth' than under ¬H. Multiplying likelihood ratios drives the
> posterior near 1 even from skeptical priors." (`:10061`–`:10069`)

The likelihoods are asserted, not estimated. The evidence sets are not
independent. The prior is not specified. The conclusion "posterior near 1" is a
rhetorical claim, not a Bayesian calculation.

## The pattern

The 210 entries share a common structure:

1. State a formal result or empirical phenomenon.
2. Describe it in a way that sounds relevant to life.
3. Assert that life-first follows.
4. Repeat.

The formal result is often correct in its own domain. The problem is the
inference from the domain to the moral conclusion. In some cases, the result is
also misstated. In others, the analogy is so loose that it could be used to
prove almost anything.

This is not a harmless stylistic choice. The catalogue creates an impression of
overwhelming interdisciplinary support. A reader who does not know the formal
results may conclude that the case is proved. The catalogue is a rhetorical
amplifier, not evidence.

## CRS and the metrics

The paper's "Combined Risk Score" is:

> `CRS = IS × II × log(ID)` (`:2204`)

where `IS` is impact scope, `II` is impact intensity, and `ID` is impact
duration. Problems:

- **Units:** `log(ID)` requires a unit. Is `ID` in seconds, days, or years? The
  score changes with the unit.
- **Sign:** If `ID < 1` (in the chosen unit), `log(ID)` is negative. If `ID = 1`,
  `log(ID) = 0`. The score can be negative or zero for a harmful action.
- **Aggregation:** Multiplying scope, intensity, and duration assumes a
  particular functional form with no justification.
- **Probability:** The score ignores the probability of the harm.
- **Distribution:** It ignores who is harmed and how harm is distributed.
- **Consent:** It ignores whether the affected beings consent.
- **Uncertainty:** It ignores uncertainty in the inputs.
- **Gaming:** It is easy to manipulate by underreporting scope, intensity, or
  duration.

A risk score is not a moral theory. Even a good risk score would not establish
life-first. This one is not validated.

## What a better formal treatment would look like

1. **Specify the decision problem:** states, actions, outcomes, agents,
   information, and time horizon.
2. **Specify the axiology:** what is good, for whom, and how it is aggregated.
3. **Specify the constraints:** which actions are forbidden, and why.
4. **Specify the decision rule:** maximin, expected utility, lexical threshold,
   or something else.
5. **Prove results within the model:** state assumptions and derive conclusions.
6. **Test the model:** calibrate it on cases, compare predictions, and report
   failures.
7. **Distinguish formal results from moral conclusions:** a theorem about a
   model is not a theorem about the world.

The paper does none of these. It uses the vocabulary of formal methods without
the discipline.

## Verdict

The 210 stress tests are not theorem-level. They are analogies and assertions,
often misapplied. The CRS metric is arbitrary and unvalidated. The formal
apparatus does not prove the thesis.

## Repair

1. Remove the "210 theorem-level" claim.
2. Keep a small number of valid arguments and label the rest as analogies.
3. If formal methods are used, state the model, assumptions, and results
   precisely.
4. Replace CRS with a validated risk model, or drop it.
5. Submit the formal parts to domain experts for review.
