# Threat model

## Purpose

This threat model describes the assets, actors, trust boundaries, assumptions,
and attack surfaces of the WISLIM framework. It is the basis for the scenarios
in `adversarial-scenarios.md`.

## Assets

| Asset | Why it matters | Owner (proposed) |
|---|---|---|
| Human life and wellbeing | The framework's stated purpose. | Everyone |
| Decision records (ULP) | Evidence of what was decided and why. | FLVS |
| Verification keys | Authenticate records and approvals. | FLVS |
| Model weights and prompts | Determine verification behavior. | Vendors |
| Impact estimates (IS/II/ID) | Drive CRS and routing. | Decision-makers |
| Reputation of the framework | Legitimacy and adoption. | Author/FLVS |
| Layer M constitutional core | Constrains amendments. | International body |
| Personal data about affected people | Privacy and non-discrimination. | FLVS |
| Appeals and due process | Protect individuals from error. | Independent body |
| Public trust | Compliance and cooperation. | All |

## Actors

| Actor | Motivation | Capability |
|---|---|---|
| Author | Promote the framework; protect life. | Ideological influence; agenda-setting. |
| AI vendors | Sell models; avoid liability; shape standards. | Technical control; lobbying; model access. |
| States | Advance national interests; maintain sovereignty. | Law; force; funding; jurisdiction. |
| Institutions | Pursue their missions; manage risk. | Operational control; data; expertise. |
| Individuals | Protect themselves; pursue values. | Exit; voice; litigation; non-compliance. |
| Insiders | Money; ideology; coercion; negligence. | Access to records, models, keys. |
| Attackers | Disruption; espionage; profit. | Technical exploits; social engineering. |
| Corporations | Minimize regulation; maximize profit. | Capture; lobbying; metric manipulation. |
| NGOs | Advocate; monitor; fund. | Expertise; publicity; legitimacy. |
| Future generations | No voice; no power. | None (represented by others). |

## Trust boundaries

1. **Affected person → decision-maker.** The person may not know a decision is
   being made, may not understand the metrics, and may not have access to the
   record.
2. **Decision-maker → verifier.** The decision-maker self-reports impact
   estimates. The verifier may not have independent data.
3. **Verifier → human reviewer.** The human may defer to the AI or lack time
   and expertise.
4. **Human reviewer → international body.** The body may be distant,
   politicized, or captured.
5. **Record → public.** The record may contain sensitive data; publication may
   harm privacy.
6. **Model → deployment.** The model may change after approval; the deployment
   context may differ from the test context.
7. **Constitution → interpreter.** The text may be ambiguous; the interpreter
   may be captured.
8. **Framework → state.** The state may refuse, ignore, or weaponize the
   framework.

## Assumptions

The framework assumes:

- decision-makers will report impacts honestly;
- AI verifiers are independent and accurate;
- human reviewers are competent and unbiased;
- international bodies are legitimate and impartial;
- records are secure and trustworthy;
- the constitutional core is clear and correctly interpreted;
- affected people can appeal;
- states will comply with a global authority;
- "life" is a coherent category;
- the framework's metrics capture the relevant harms.

Each assumption is questionable. The red-team scenarios test them.

## Attack surfaces

| Surface | Attack | Scenario |
|---|---|---|
| CRS inputs | Underreport scope, intensity, or duration. | AS01 |
| Multi-AI review | Exploit correlated training data or shared prompts. | AS02 |
| ULP documents | Prompt injection or false data. | AS03 |
| Integrity screen | Weaponize against whistleblowers or rivals. | AS04 |
| Public rhetoric | Justify repression or war. | AS05 |
| Emergency powers | Suspend review and rights. | AS06 |
| Vendor relationship | Capture the verifier. | AS07 |
| Impact data | Poison the estimates. | AS08 |
| Model updates | Change behavior after approval. | AS09 |
| Triage | False positive blocks care. | AS10 |
| Disability | Discriminatory proxy metrics. | AS11 |
| Suicide prevention | Coercive detention. | AS12 |
| Records | Forge signatures or tamper. | AS13 |
| Layer M | Capture the amendment process. | AS14 |
| Jurisdiction | Forum shopping. | AS15 |
| AI status | Self-classify as life for protection. | AS16 |
| Definitions | Game "life system" scope. | AS17 |
| Privacy | Leak sensitive records. | AS18 |
| Appeals | Deny or delay appeals. | AS19 |
| Reputation | Use the framework for laundering. | AS20 |

## STRIDE analysis

| Threat | Example | Control gap |
|---|---|---|
| **Spoofing** | A decision-maker impersonates a low-risk actor. | Identity verification is unspecified. |
| **Tampering** | ULP records are altered. | Signature scheme and key management are unspecified. |
| **Repudiation** | A decision-maker denies approving a harmful action. | Records may not be non-repudiable. |
| **Information disclosure** | Sensitive data in ULP records leaks. | Privacy regime is unspecified. |
| **Denial of service** | A verifier is flooded with requests. | Capacity and prioritization are unspecified. |
| **Elevation of privilege** | A vendor gains control of Layer 4. | Capture controls are unspecified. |

## Risk matrix

| Likelihood \ Impact | Low | Medium | High | Critical |
|---|---|---|---|---|
| **High** | Medium | High | Critical | Critical |
| **Medium** | Low | Medium | High | Critical |
| **Low** | Low | Low | Medium | High |

The scenarios in `adversarial-scenarios.md` are rated on this matrix.

## What the framework does not model

- **Adversarial institutions.** It assumes good faith.
- **Power asymmetries.** It assumes equal access to appeals.
- **Cultural pluralism.** It assumes a single moral hierarchy.
- **State interests.** It assumes states will cede authority.
- **Technical uncertainty.** It assumes models are stable and accurate.
- **Long-tail risks.** It assumes the metrics capture the relevant harms.
- **Political economy.** It assumes the framework cannot be captured.

These omissions are not minor. They are the core of the governance problem.

## Conclusion

The framework's threat model is thin. It identifies capture as a risk but does
not design against it. It assumes the verifier is independent, the record is
secure, the reviewer is competent, the state complies, and the affected person
can appeal. Each assumption is an attack surface. A serious framework would
start from the assumption that every actor may be self-interested, every record
may be forged, every model may drift, and every institution may be captured.
