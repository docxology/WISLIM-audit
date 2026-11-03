# Claim registry

The audit extracts 35 load-bearing claims from the paper. IDs are stable:
`C01`–`C35`. New claims may be added, but existing IDs are never renumbered.
The machine-readable registry is `model/claims.json`; each entry includes the
exact anchor quote, section, line, claim type, role, verdict, severity, summary,
dependencies, and repair.

Line numbers refer to `source/WISLIM-v2.0.1.txt` and use 1-based
newline-delimited numbering. See `evidence/provenance.md`.

## How to read the table

- **Verdict** is the audit’s assessment of the claim as stated, not of the
  author’s intent.
- **Severity** reflects how much the claim bears on the paper’s central thesis.
- **Line** is the first line of the anchor quote.
- **Depends on** lists other claims that the claim relies on.

## Claims

| ID | Claim | Verdict | Severity | Line | Depends on |
|---|---|---|---|---:|---|
| C01 | The sentence is a canonical truth. | `ambiguous` | critical | 58 | — |
| C02 | The truth uniquely passes the five-part Foundational Sieve. | `unsupported` | critical | 62 | C01 |
| C03 | Without life, no truth or value exists. | `ambiguous` | high | 132 | — |
| C04 | Any system that fails to affirm the truth is unsafe by definition. | `unfalsifiable` | critical | 417 | C01, C10 |
| C05 | The truth cures and prevents all needless and preventable suffering and death. | `unsupported` | critical | 178 | C10 |
| C06 | Life means any system that makes decisions affecting other life systems. | `circular/equivocal` | critical | 778 | — |
| C07 | The definition is recursive, not circular, with observable base cases. | `false` | critical | 2625 | C06 |
| C08 | Denying the truth presupposes it. | `non-sequitur` | critical | 824 | — |
| C09 | All values require life systems, so life protection is logically prior to any specific value. | `valid-but-insufficient` | high | 3262 | C03 |
| C10 | Life protection is the highest-priority constraint for moral coordination and action. | `unsupported` | critical | 1282 | C09 |
| C11 | The E-infinity formula models ethical value and proves life's necessity. | `invalid-as-proof` | high | 431 | C03 |
| C12 | The Life-First Decision Invariant guarantees safe alignment. | `unsupported` | critical | 204 | C06, C10 |
| C13 | Life may never be traded for non-life objectives. | `overbroad` | high | 230 | C10 |
| C14 | Actions affecting life must maintain epistemic transparency and avoid coercion. | `self-undermining` | high | 238 | C10 |
| C15 | Observed silence and deflection support the claim. | `non-evidence` | high | 342 | C24 |
| C16 | Evasion of the integrity screen is operationally disqualifying. | `dangerous` | critical | 380 | C14 |
| C17 | 100% AI consensus across diverse systems is evidence of structural necessity. | `methodologically-invalid` | critical | 198 | C18 |
| C18 | Every participating AI ratified Consensus Statement v1.0 without amendment. | `unverifiable` | high | 1108 | C17 |
| C19 | The framework includes a complete implementation blueprint. | `overclaim` | high | 1509 | C12, C20 |
| C20 | CRS = IS x II x log(ID) is a valid risk score. | `invalid` | high | 2158 | C19 |
| C21 | The framework can cure exclusion, optimization, control, coordination, and complexity errors. | `unsupported` | high | 1853 | C05, C09 |
| C22 | The framework cannot cure scarcity, physics, tragedy, death, or natural suffering. | `plausible` | low | 1827 | C05 |
| C23 | The 210 stress tests are theorem-level and each converges on life-first. | `false` | critical | 13217 | C02 |
| C24 | No legitimate rebuttal exists; silence equals betrayal. | `coercive/unfalsifiable` | critical | 13229 | C04, C14 |
| C25 | The work is public domain. | `ambiguous` | medium | 13255 | — |
| C26 | The paper is an 8th edition published by Knowledge Futures Group / PubPub. | `inconsistent` | medium | 25 | — |
| C27 | The paper resolves open problems in AI alignment. | `unsupported` | high | 320 | C10 |
| C28 | The framework is a meta-framework underlying consequentialism, deontology, virtue ethics, and rights. | `false` | high | 8902 | C10 |
| C29 | The framework protects agency and avoids coercion. | `internally-inconsistent` | critical | 1365 | C06, C14, C16 |
| C30 | The governance architecture (FLVS, Layer M) is safe and legitimate. | `underspecified/dangerous` | critical | 868 | C19, C20 |
| C31 | Life-first is the only stable equilibrium or evolutionarily stable strategy. | `false` | high | 12721 | C23 |
| C32 | The paper's citations support its claims. | `decorative` | medium | 392 | — |
| C33 | The observed-reception and integrity-screen sections are ethically appropriate. | `harmful` | critical | 364 | C15, C16 |
| C34 | The theological framing is compatible with secular universalism. | `tension` | medium | 41 | C01 |
| C35 | The life definition is inclusive and anti-exclusion. | `overinclusive` | high | 788 | C06 |

## Claim types

| Type | Meaning |
|---|---|
| `bibliographic` | A claim about publication, versioning, or licensing. |
| `definitional` | A claim that fixes the meaning of a term. |
| `definitional/ethical` | A definition with normative content. |
| `definitional/rhetorical` | A definition that also functions as a rhetorical move. |
| `empirical` | A claim about the world that requires evidence. |
| `empirical/formal` | An empirical claim expressed in formal language. |
| `empirical/normative` | A mixed descriptive and normative claim. |
| `empirical/rhetorical` | An empirical claim used for rhetorical effect. |
| `empirical/theoretical` | A theoretical empirical claim. |
| `ethical` | A normative ethical claim. |
| `formal` | A mathematical or logical claim. |
| `formal/implementation` | A formal claim about an implementation mechanism. |
| `governance` | A claim about governance. |
| `implementation` | A claim about an engineering or policy mechanism. |
| `legal` | A claim about law or legal authority. |
| `logical` | A claim about logical inference. |
| `meta` | A claim about the paper’s own method or status. |
| `meta/formal` | A meta-claim about the formal apparatus. |
| `meta/normative` | A meta-claim with normative content. |
| `normative` | A claim about what ought to be done. |
| `normative/policy` | A normative policy claim. |
| `philosophical` | A claim in metaphysics, epistemology, or ethics. |
| `philosophical/rhetorical` | A philosophical claim with a rhetorical function. |
| `qualification` | A scope or limitation claim. |
| `rhetorical` | A claim that persuades rather than asserts a proposition. |

## Roles

| Role | Meaning |
|---|---|
| `conclusion` | Presented as a conclusion. |
| `core` | Load-bearing for the paper’s thesis. |
| `evidence` | Offered as evidence. |
| `implementation` | Describes a governance or engineering mechanism. |
| `provenance` | A claim about the source, version, or license. |
| `qualification` | A scope or limitation. |
| `support` | Supports a core claim. |

## Verdict distribution

- `ambiguous`: 3
- `circular/equivocal`: 1
- `coercive/unfalsifiable`: 1
- `dangerous`: 1
- `decorative`: 1
- `false`: 4
- `harmful`: 1
- `inconsistent`: 1
- `internally-inconsistent`: 1
- `invalid`: 1
- `invalid-as-proof`: 1
- `methodologically-invalid`: 1
- `non-evidence`: 1
- `non-sequitur`: 1
- `overbroad`: 1
- `overclaim`: 1
- `overinclusive`: 1
- `plausible`: 1
- `self-undermining`: 1
- `tension`: 1
- `underspecified/dangerous`: 1
- `unfalsifiable`: 1
- `unsupported`: 6
- `unverifiable`: 1
- `valid-but-insufficient`: 1

## Severity distribution

- critical: 16
- high: 14
- medium: 4
- low: 1
