# Capture and gaming

## Why capture is the central risk

The framework proposes a global verification system with authority over
life-affecting decisions. Any institution with that authority is a prize. Actors
will try to control it, shape its rules, or use its legitimacy for their own
ends. The paper acknowledges capture as a risk (`source/WISLIM-v2.0.1.txt:2212`)
but does not design against it.

Capture is not a single event. It is a process:

1. **Entry:** actors gain access to the institution.
2. **Influence:** they shape rules, standards, and appointments.
3. **Control:** they determine outcomes.
4. **Entrenchment:** they make exit costly.
5. **Legitimation:** the institution's authority justifies their power.

A framework that only looks for outright bribery will miss capture by
appointment, funding, expertise, and framing.

## Types of capture

### Industry capture

**Mechanism:** Firms that build AI systems fund research, supply models, and
rotate staff into verification bodies. Standards are written around their
products. Competitors face higher compliance costs.

**Indicators:**

- revolving doors between vendors and verifiers;
- standards that match one vendor's architecture;
- funding concentration;
- barriers to entry for smaller developers;
- proprietary verification tools.

**Mitigation:**

- independent funding;
- cooling-off periods;
- conflict-of-interest disclosure;
- open standards;
- multiple vendors;
- public comment.

**Residual risk:** High. Industry expertise is necessary, and expertise often
comes from industry.

### State capture

**Mechanism:** Powerful states pressure international bodies, block
enforcement, or use the framework against rivals. They may host the
secretariat, fund the budget, or threaten withdrawal.

**Indicators:**

- disproportionate staffing from one state;
- enforcement against rivals but not allies;
- budget dependence;
- jurisdictional carve-outs;
- security-council vetoes.

**Mitigation:**

- balanced governance;
- distributed secretariat;
- independent budget;
- judicial review;
- exit rights;
- transparency.

**Residual risk:** High. States retain sovereignty and power.

### Epistemic capture

**Mechanism:** A dominant theory, model, or research program defines what
counts as evidence. Dissent is excluded from journals, conferences, and
funding.

**Indicators:**

- narrow citation networks;
- homogeneity of experts;
- suppression of negative results;
- "consensus" claims without independent replication;
- peer review captured by a school.

**Mitigation:**

- interdisciplinary review;
- adversarial collaboration;
- funding for dissent;
- open data;
- pre-registration;
- publication of negative results.

**Residual risk:** High. Expertise is necessarily concentrated.

### Metric capture (Goodhart's law)

**Mechanism:** Decision-makers optimize the metric rather than the goal. CRS,
`ΔA`, and ULP fields become targets.

**Indicators:**

- gaming of self-reported inputs;
- improvements in metrics without improvements in outcomes;
- sudden changes in classification;
- teaching to the test;
- suppression of inconvenient data.

**Mitigation:**

- multiple metrics;
- independent data;
- random audits;
- outcome-based evaluation;
- whistleblower protection;
- rotate auditors.

**Residual risk:** High. Any metric can be gamed.

### Procedural capture

**Mechanism:** Compliance becomes a box-checking exercise. The forms are filed,
the reviews are held, and the harmful decision proceeds.

**Indicators:**

- high approval rates;
- short review times;
- repetitive records;
- lack of substantive disagreement;
- appeals denied on procedure;
- auditors reliant on the audited.

**Mitigation:**

- substantive review;
- random deep audits;
- independent appeals;
- outcome tracking;
- rotate reviewers;
- publish dissent.

**Residual risk:** High. Procedures are necessary but insufficient.

### Emergency capture

**Mechanism:** A crisis justifies expanding powers, suspending review, and
suppressing dissent. The emergency becomes permanent.

**Indicators:**

- repeated emergency declarations;
- expanded powers without sunset;
- reduced transparency;
- criticism framed as disloyalty;
- emergency budgets.

**Mitigation:**

- narrow definitions;
- automatic sunset;
- legislative approval;
- judicial review;
- post-emergency audit.

**Residual risk:** High. Crises create genuine urgency.

### Rhetorical capture

**Mechanism:** "Life-first" is used to justify any policy that claims to
protect life, including war, repression, surveillance, and discrimination.

**Indicators:**

- policies labeled life-first without evidence;
- critics accused of betrayal;
- emotional appeals replacing analysis;
- expanded scope;
- emergency rhetoric.

**Mitigation:**

- precise definitions;
- independent review;
- free expression;
- pluralism;
- falsifiability.

**Residual risk:** Critical. Moral language is inherently contestable.

### Layer M capture

**Mechanism:** A coalition captures the amendment process, changes the
interpretation of the constitutional core, and entrenches its preferred rules.

**Indicators:**

- packed amendment body;
- changed voting rules;
- narrowed participation;
- opaque deliberation;
- judicial capture;
- minority exclusion.

**Mitigation:**

- separation of powers;
- supermajority requirements;
- minority vetoes;
- judicial review;
- transparent deliberation;
- sunset clauses.

**Residual risk:** High. Constitutional capture is a known failure mode.

## Gaming the CRS

The CRS is:

> `CRS = IS × II × log(ID)` (`source/WISLIM-v2.0.1.txt:2158`)

Ways to game it:

1. **Underreport scope.** Classify a population-wide harm as local.
2. **Underreport intensity.** Classify severe harm as moderate.
3. **Underreport duration.** Classify a long-term harm as short-term.
4. **Exploit the unit.** Report duration in a unit that makes `log(ID)` small or
   negative.
5. **Exploit the threshold.** Keep the score just below the review threshold.
6. **Split the decision.** Break a large decision into small ones, each below
   the threshold.
7. **Delay.** Report the harm as future and uncertain.
8. **Redefine the affected class.** Exclude groups that would raise the score.

**Mitigations:**

- independent data;
- unit standardization;
- aggregation rules;
- random audits;
- whistleblower protection;
- criminal liability for false reporting;
- publish distributions.

## Gaming the ULP

Ways to game the record:

1. **False fields.** Report favorable values.
2. **Omission.** Leave out affected groups or harms.
3. **Free-text injection.** Embed instructions in narrative fields.
4. **Signature laundering.** Use a valid signature on a false record.
5. **Version confusion.** Cite an old approval for a new decision.
6. **Scope splitting.** Use multiple records for one decision.
7. **Post-hoc rationalization.** Write the record after the decision.

**Mitigations:**

- structured fields;
- independent verification;
- data provenance;
- version control;
- audit trails;
- random deep audits;
- non-repudiation.

## Gaming the FLVS

Ways to game the layers:

1. **Layer 1:** automated checks with narrow rules.
2. **Layer 2:** multiple models from the same vendor.
3. **Layer 3:** human reviewers with no time or expertise.
4. **Layer 4:** international body with no enforcement.
5. **Forum shopping:** choose the weakest jurisdiction.
6. **Capture:** appoint friendly reviewers.
7. **Emergency:** suspend review.

## The "who guards the guardians" problem

The framework needs an institution to verify the verifiers. It does not say who
appoints them, who can remove them, or how they are funded. Without an answer,
the framework is vulnerable to the oldest problem in governance: the guardians
can become the tyrants.

Possible answers:

- **Separation of powers:** different bodies for rule-making, verification,
  adjudication, and enforcement.
- **Independent judiciary:** courts with tenure and constitutional protection.
- **Democratic oversight:** elected representatives with budget and appointment
  power.
- **Civil society:** NGOs, press, and academic monitoring.
- **Exit:** people and states can leave.
- **Transparency:** publish decisions, data, and dissent.

Each answer has costs. There is no perfect solution. The point is that the
framework does not even ask the question.

## Indicators of capture

A healthy institution should monitor:

- diversity of staff and funding;
- revolving doors;
- approval rates;
- appeal rates and outcomes;
- dissent rates;
- public trust;
- media coverage;
- whistleblower reports;
- audit findings;
- changes in rules;
- emergency declarations.

A sudden increase in approvals, a decrease in appeals, or a decline in dissent
may signal capture.

## What would a capture-resistant design look like?

1. **Separate powers.** No body both makes and enforces the rules.
2. **Independent funding.** No single donor or state.
3. **Transparency.** Decisions, data, and dissent are public.
4. **Appeals.** Affected people can challenge decisions.
5. **Exit.** People and states can opt out.
6. **Rotation.** Staff rotate; no permanent incumbents.
7. **Red teams.** Independent adversarial testing.
8. **Whistleblower protection.** Dissent is safe.
9. **Sunset clauses.** Powers expire.
10. **Pluralism.** No single moral doctrine is imposed.

The paper's design has almost none of these. It has layers, records, and a
constitution, but not a separation of powers or a bill of rights.

## Conclusion

Capture is not an edge case. It is the default outcome of concentrated power
without accountability. The framework's own anti-capture layer is a name, not a
mechanism. Until the design specifies who appoints, funds, monitors, and
removes the verifiers, the framework is capture-prone by construction.
