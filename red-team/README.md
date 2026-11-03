# Red-team package

This directory stress-tests the WISLIM framework as a governance and safety
system. It is not a personal attack on the author. It asks: if the framework
were implemented as described, how could it fail, be captured, or be used to
harm the people it claims to protect?

## Contents

- `threat-model.md` — assets, actors, trust boundaries, assumptions, and attack
  surfaces.
- `adversarial-scenarios.md` — 20 concrete scenarios with attack paths,
  impacts, detection, and mitigations.
- `capture-and-gaming.md` — how institutions, metrics, and procedures can be
  captured or gamed.
- `abuse-cases.md` — how "life-first" rhetoric can be used to justify harm.

## Method

Each scenario follows a fixed structure:

- **ID and title**
- **Actor** — who carries out the attack
- **Preconditions** — what must be true for the attack to work
- **Attack path** — the steps
- **Impact** — who is harmed and how
- **Detection** — what signal might reveal the attack
- **Mitigation** — design changes that reduce the risk
- **Residual risk** — what remains after mitigation

The scenarios are deliberately concrete. They are not predictions. They are
tests of the framework's institutions and rhetoric.

## Scope

The red team covers:

- the Life-First Decision Invariant (LFDI);
- the Federated Life Verification System (FLVS);
- the Unified Life Protocol (ULP);
- the Combined Risk Score (CRS);
- Layer M;
- the integrity screen;
- the "life-first" public rhetoric;
- the AI-consensus claim.

It does not cover:

- the author's private intentions;
- the theology of the paper;
- the truth of the paper's metaethics (covered in `audit/`);
- clinical or legal advice.

## Severity scale

| Severity | Meaning |
|---|---|
| Critical | Credible risk of death, serious injury, or irreversible loss of rights at scale. |
| High | Credible risk of significant harm, discrimination, or institutional capture. |
| Medium | Credible risk of inefficiency, legitimacy loss, or limited harm. |
| Low | Credible risk of inconvenience or reputational damage. |

## How to use this package

1. Read the threat model first.
2. For each scenario, ask whether the framework has a control that addresses
   it.
3. If the control is "the verifier will notice," ask who verifies the verifier.
4. If the control is "the model is aligned," ask how alignment is measured.
5. If the control is "the constitution forbids it," ask who interprets the
   constitution.
6. Record residual risks. A framework with unaddressed critical risks is not
   ready for deployment.

## Bottom line

The framework's governance design is a review hierarchy, not a separation of
powers. It has no independent judiciary, no appeal rights, no privacy regime,
no exit rights, and no answer to capture. The integrity screen and
silence-as-betrayal rhetoric make dissent dangerous. These are not edge cases;
they are structural features of the design.
