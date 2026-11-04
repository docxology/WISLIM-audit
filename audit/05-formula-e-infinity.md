# The `E∞` formula

## The formula

The paper introduces:

> `E∞ = (L₁ × U) / D` (`source/WISLIM-v2.0.1.txt:431`)

with:

- `L₁` = "the inherent, non-negotiable value of a single life";
- `U` = "the unlockable potential within life";
- `D` = "the delay, distortion, or destruction that obstructs truth, action, or
  recognition of life's value";
- `E∞` = "the ethical energy released when life is valued and barriers are
  removed." (`:445`–`:447`)

The paper calls this "the operational definition of alignment, and the blueprint
for the cure of preventable suffering" (`:529`).

## The theorem

The paper's "Life-First Necessity Theorem" says:

> "If L = 0, then E∞ = 0." (`:644`)

> "Proof: If L = 0, then L × U = 0. Thus E∞ = 0 / D = 0 since D > 0." (`:650`–`:652`)

This is valid arithmetic. It is also trivial. If you multiply by zero, you get
zero. The theorem does not prove that life is morally important, that life
should be the highest priority, or that the formula models ethics. It proves
that a product with a zero factor is zero.

The theorem's conclusion — "the existence of life is a necessary condition for
any nonzero long-run outcome" (`:660`) — is true by construction. It is not an
empirical discovery or a moral result.

## The pole at D = 0

The paper says:

> "As resistance is minimized (D → 0), the output approaches infinity
> (E∞ → ∞), representing an ideal state of ethical flourishing." (`:465`–`:467`)

This is not an ideal; it is a pole. A rational function with a denominator that
goes to zero diverges. In physics and engineering, a divergence usually signals
that the model breaks down, not that the quantity becomes infinitely good. The
paper's response to the division-by-zero objection is:

> "This formula is not a conventional physical or mathematical equation. It is
> an ethical identity — a value model." (`:475`–`:479`)

But if it is not a mathematical equation, it cannot be used as a mathematical
proof. The paper wants the authority of mathematics without its constraints.
That is not a defense; it is a category shift.

If `D = 0` exactly, the expression is undefined. If `L = 0` and `D = 0`, it is
also undefined. The theorem assumes `D > 0` but does not justify that
assumption. The paper cannot have a well-defined limit and an undefined point at
the same time.

## The variables have glosses, not measurements

The paper defines the symbols in words, and the words change across its versions.
At `:435`, `L₁` is "The inherent, non-negotiable value of a single life." The formal
Version 2 makes `L` the "existence of at least one choice-capable life-bearing
system", with "L = 0 ⇔ no such system exists" (`:624`–`:626`). None of these has
units or an estimator.

The engineering Version 3 says so itself: "The formula E∞ = (L × U) / D is not meant
to compute a number. It is meant to enforce a hard rule." (`:687`–`:689`). That is a
fair account of how the formula could be used. It also means the formula cannot
carry a proof about quantities, and that a "calculation" from it reports nothing
beyond the rule.

`L₁`, `U`, and `D` are not measured, defined operationally, or assigned units.
The paper calls `L₁` "inherent, non-negotiable value," which is a normative
claim, not a quantity. `U` is a bundle of "creativity, healing, love, knowledge,
and energy" — incommensurable goods. `D` is "delay, distortion, or destruction"
— again, incommensurable categories.

A formula with no common scale cannot compare two actions. Suppose action A
saves one life and unlocks modest potential; action B saves ten lives but
suppresses some potential. The formula gives no way to compare them because
`L₁`, `U`, and `D` are not on a common scale. The formula is a metaphor dressed
as a model.

## The formula cannot adjudicate trade-offs

The paper's central normative claim is that life may never be traded for
non-life objectives. The formula does not support that claim. It multiplies
life by potential and divides by distortion. A large enough `U` or a small
enough `D` could make a small `L` produce a large `E∞`. The formula is
multiplicative, not lexicographic. It does not encode a priority rule at all.

If `L` is binary (life exists or not), then the formula says nothing about
trade-offs among lives. If `L` is a count, it says nothing about the
distribution of lives or the quality of life. If `L` is a value, it is
circular.

## The "ethical energy" metaphor

The paper compares `E∞` to energy and `D` to entropy. These are metaphors, not
models. Energy has units, conservation laws, and transformations. Ethical value
does not. Entropy has a precise statistical meaning; "ethical entropy" does not.
The metaphor may help readers visualize the author's intuition, but it cannot
bear the weight of a proof.

## The "mathematical critique" response

The paper anticipates the objection that dividing by zero is undefined. It
responds that the formula is not a conventional equation, that the limit is the
ideal, and that the formula is "illuminated" by edge cases (`:471`–`:497`). This
is hand-waving. A model that diverges at the ideal is ill-posed. A model that
changes its logical type when criticized is not a model. The paper cannot claim
mathematical proof and then exempt the mathematics from mathematical standards.

## What the formula could be

If the author wants a formal model, it should have:

- defined variables with units or ordinal scales;
- explicit assumptions and scope conditions;
- a decision rule that can rank actions;
- a treatment of uncertainty and incommensurability;
- empirical calibration and validation;
- a clear distinction between descriptive and normative components.

A simple decision-theoretic model might be:

> `EU(a) = Σ p(o|a) · u(o)`, with a side-constraint that forbids actions whose
> worst-case outcome exceeds a catastrophic-harm threshold.

That model has its own problems, but it is at least a model. It can be tested,
criticized, and revised. `E∞` cannot.

## Verdict

The `E∞` formula is not a proof. The theorem is trivial arithmetic. The
variables are unmeasured and incommensurable. The pole at `D = 0` is a
mathematical defect, not an ideal. The formula cannot adjudicate trade-offs and
does not support the paper's normative conclusion.

## Repair

1. Drop the formula as a proof.
2. If a formal model is desired, specify variables, units, assumptions, and a
   decision rule.
3. Separate the descriptive model from the normative premise.
4. Calibrate and test the model on bounded cases.
5. Do not use "infinity" as a stand-in for "ideal."
