# Citation audit

## Scope

This file audits the ten references in Appendix C
(`source/WISLIM-v2.0.1.txt:9723`–`:9775`) and the citation practice in the
paper. It asks two questions:

1. Is the reference accurately described?
2. Does it support the claim the paper uses it for?

## The references

| # | Reference | What it actually argues | How the paper uses it | Support? |
|---|---|---|---|---|
| 1 | Russell & Norvig, *AI: A Modern Approach* (2021) | A textbook covering AI methods. | General background. | Background only. |
| 2 | Russell, *Human Compatible* (2019) | AI systems should be uncertain about human preferences; value alignment is hard. | "The Life-First framework addresses this by making the preservation of life the explicit, non-negotiable ground." | No. The framework asserts a preference rather than modeling uncertainty. |
| 3 | Christiano, Shlegeris, & Amodei (2018) | Amplifying weak experts to supervise strong learners. | "The Life-First framework provides the meta-principle that makes such approaches safe." | No. No argument connects amplification to life-first. |
| 4 | Leike et al. (2018) | Reward modeling for scalable alignment. | "Life-prioritization [is] a necessary constraint on reward interpretation." | No. Reward modeling does not entail life-first. |
| 5 | Yudkowsky (2008) | Existential risk from advanced AI. | "A cross-domain provable constraint that prohibits value drift into lethal regimes." | No. Yudkowsky argues for caution, not a life-first axiom. |
| 6 | Bostrom (2014) | Superintelligence and existential risk. | Same as above. | No. Bostrom does not argue for life-first. |
| 7 | Hadfield-Menell et al. (2016) | Cooperative inverse reinforcement learning. | "The meta-prior such agents must adopt: no goal may override the preservation of life." | No. CIRL does not entail a moral hierarchy. |
| 8 | Friston (2010) | The free-energy principle as a theory of brain function. | "The Life-First framework extends this logic to ethics." | No. This is a category move, not an extension. |
| 9 | Ord (2020) | Existential risk and the value of the future. | "A cross-domain provable constraint." | No. Ord argues for precaution, not lexical priority. |
| 10 | O'Keefe et al. (2020) | Cooperative AI as a research agenda. | "Without shared agreement that life is most important, no cooperation framework can be morally stable." | No. The paper asserts the shared agreement; O'Keefe et al. do not. |

## Pattern

The pattern is consistent:

1. Cite a well-known work.
2. Summarize it in one sentence.
3. Assert that the paper's framework "resolves," "grounds," or "underpins" it.
4. Do not engage the work's actual argument, conditions, or limitations.

This is decorative citation. It signals familiarity with the AI alignment
literature without using that literature as evidence or argument.

## What is missing

The paper's thesis is a normative one. A serious bibliography would include:

### Normative ethics

- Consequentialism: Mill, Sidgwick, Parfit, Smart, Williams.
- Deontology: Kant, Korsgaard, O'Neill, Scanlon.
- Virtue ethics: Aristotle, Foot, MacIntyre, Hursthouse.
- Care ethics: Gilligan, Noddings, Held, Tronto.
- Contractualism: Rawls, Scanlon, Gauthier.
- Capabilities: Sen, Nussbaum.
- Natural law: Aquinas, Finnis.

### Moral status

- Singer, *Animal Liberation*.
- Regan, *The Case for Animal Rights*.
- Nussbaum, *Frontiers of Justice*.
- McMahan, *The Ethics of Killing*.
- Jaworska, on marginal cases.
- Kittay, on dependency and disability.

### Population ethics

- Parfit, *Reasons and Persons*.
- Arrhenius, *Population Ethics*.
- Broome, *Weighing Lives*.

### Risk and precaution

- Jonas, *The Imperative of Responsibility*.
- Sunstein, *Laws of Fear*.
- Gardiner, *A Perfect Moral Storm*.
- Ord, *The Precipice* (already cited, but not engaged).

### Paternalism and autonomy

- Mill, *On Liberty*.
- Dworkin, on paternalism.
- Feinberg, *The Moral Limits of the Criminal Law*.
- Quong, *Liberalism without Perfection*.

### Governance and legitimacy

- Rawls, *Political Liberalism*.
- Waldron, *Law and Disagreement*.
- Buchanan, *The Legitimacy of International Law*.
- Habermas, on deliberative democracy.

### AI safety

- Amodei et al., "Concrete Problems in AI Safety."
- Hendrycks et al., "Unsolved Problems in ML Safety."
- Hubinger et al., "Risks from Learned Optimization."
- Soares et al., "Corrigibility."
- Hadfield-Menell et al. (already cited, but not engaged).

The paper cites none of these. It claims to resolve "centuries of debate"
without engaging the debate.

## Citation accuracy

The references are mostly accurate in their bibliographic details:

- Russell & Norvig 2021, 4th edition, Pearson. Correct.
- Russell 2019, Viking. Correct.
- Christiano, Shlegeris & Amodei 2018, arXiv:1810.08575. Correct.
- Leike et al. 2018, arXiv:1811.07871. Correct.
- Yudkowsky 2008, in Bostrom & Ćirković, Oxford University Press, pp. 308–345.
  Correct.
- Bostrom 2014, Oxford University Press. Correct.
- Hadfield-Menell et al. 2016, NeurIPS. Correct.
- Friston 2010, *Nature Reviews Neuroscience* 11(2), 127–138. Correct.
- Ord 2020, Hachette. Correct.
- O'Keefe et al. 2020, *Nature* 586(7829), 34–36. Correct.

The problem is not bibliographic accuracy. It is that the citations do not
support the claims.

## The "100% consensus" is not a citation

The AI letters are not independent sources. They are documents produced for the
paper. They are not peer-reviewed, not accompanied by prompts or transcripts,
and not cited to model documentation. They cannot bear the weight the paper
places on them. See `evidence/ai-letter-audit.md`.

## The "Observed Reception" is not a study

The paper says:

> "A recurring pattern has been observed: acknowledgment without engagement,
> deflection to side-issues (tone, wording, politics), requests to 'hold,' and
> prolonged silence without a stated rebuttal." (`:342`–`:344`)

There is no sample, response rate, coding method, or consent procedure. The
claim is anecdotal. It is also used coercively: silence is treated as betrayal
(`:417`–`:419`, `:13243`–`:13245`).

## The PhilPapers record

PhilPapers lists eight references; the PDF lists ten. The difference may be due
to extraction or deposit. The record reports no citations of the work as of
2026-11-03. Downloads (1,843) are not citations or peer review.

## Verdict

The bibliography is accurate but decorative. It supports general AI safety
points, not the life-first thesis. The paper ignores the ethics literature it
claims to resolve. The citation practice is not sufficient for a scholarly
work.

## Repair

1. Add a substantive literature review.
2. Engage the strongest objections, not just the friendly background.
3. Cite sources for empirical claims.
4. Distinguish "cites" from "supports."
5. Remove the claim that no legitimate rebuttal exists.
6. Publish the AI prompts and transcripts if the consensus claim is retained.
