#!/usr/bin/env python3
"""Build the 210-row stress-test catalog from the source text.

The verdict map below is the audit's curated judgment. The script extracts the
paper's own titles from Appendix D, so the catalog cannot silently drift from
the source. Run from the repository root:

    python3 tools/build_stress_catalog.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source" / "WISLIM-v2.0.1.txt"
OUT = ROOT / "model" / "stress-tests.json"

# id: (verdict, severity, note)
V = {
    1: ("misapplied-formalism", "high", "Gödel's incompleteness is about formal systems; it does not imply an ethical axiom. The 'necessary meta-axiom' conclusion is a non sequitur."),
    2: ("misapplied-formalism", "high", "Diagonalization shows that certain lists cannot exhaust a set; it does not show that value lists collapse without life."),
    3: ("non-sequitur", "high", "Box(V -> Life) is asserted, not proved. Even if true, it establishes necessity, not lexical priority."),
    4: ("non-sequitur", "high", "Setting u(death)=0 is a modeling choice. Expected utility does not entail a lexicographic life constraint."),
    5: ("non-sequitur", "high", "Life-preserving strategies are not the only Nash equilibria; payoffs, institutions, and information determine equilibria."),
    6: ("category-error", "high", "Semantic truth is not identical to channel capacity. 'No decoder' does not make truth claims meaningless in the relevant sense."),
    7: ("empirical-unsupported", "high", "Anti-life strategies can persist; 'self-negating' is not a general evolutionary result."),
    8: ("category-error", "high", "Life is not the only far-from-equilibrium structure; a thermodynamic fact does not yield a moral priority."),
    9: ("heuristic", "medium", "Risk dominance can be a decision heuristic, but the probabilities and utilities are unspecified. It is not a proof."),
    10: ("misapplied-formalism", "high", "No contraction mapping or function is defined. 'Life-first is the only non-degenerate fixed point' is asserted."),
    11: ("heuristic", "medium", "Cooperation can be rational in repeated games, but the specific life-first norm does not follow; other equilibria exist."),
    12: ("non-sequitur", "medium", "Simplicity is not truth. 'Life-first' is not shown to be the shortest description of morality."),
    13: ("category-error", "high", "Tarski's undefinability theorem concerns truth predicates in formal languages; it does not imply a moral axiom."),
    14: ("heuristic", "medium", "Tipping points are real, but the normative conclusion is not derived from catastrophe theory."),
    15: ("non-sequitur", "high", "Kantian, utilitarian, and virtue frameworks all presuppose agents, but they disagree about priority. Convergence is asserted, not shown."),
    16: ("non-sequitur", "high", "The likelihoods are not estimated. 'Posterior near 1' is a rhetorical assertion, not a Bayesian result."),
    17: ("non-sequitur", "medium", "No free lunch concerns optimization algorithms; it does not imply a universal moral constraint."),
    18: ("misapplied-formalism", "high", "Arrow's theorem concerns social-choice aggregation. A lexicographic life-first rule may violate other fairness conditions and is not a resolution."),
    19: ("category-error", "medium", "Entropy is not a moral measure. The second law does not rank values."),
    20: ("non-sequitur", "medium", "The fact that we can argue does not show that life-first strategies are uniquely survivable."),
    21: ("non-sequitur", "high", "Assuming 'something else is most important' and then assuming life ends does not produce a contradiction unless one assumes life is necessary for meaning."),
    22: ("heuristic", "medium", "Precaution is reasonable under uncertainty, but it does not establish the specific principle or its scope."),
    23: ("heuristic", "medium", "The precautionary principle supports caution; it can also justify arbitrary restrictions. It is not a lexicographic proof."),
    24: ("non-sequitur", "high", "Universalizability tests maxims, not the ranking of life over every other value."),
    25: ("valid-but-insufficient", "medium", "If values are modeled as zero without life, the sum is zero. That is a modeling assumption, not an argument for priority."),
    26: ("category-error", "medium", "Values are not functions requiring a nonempty support set in the relevant sense."),
    27: ("non-sequitur", "medium", "One can define a lexicographic order, but the choice of order is normative and needs argument."),
    28: ("category-error", "medium", "'Value measure' is undefined; absolute continuity is a modeling choice, not a moral result."),
    29: ("category-error", "medium", "Moral values are not objects and morphisms. The category-theory analogy is decorative."),
    30: ("valid-but-insufficient", "medium", "G(Life>0) is a safety invariant if specified, but it does not establish that life outranks all other values."),
    31: ("non-sequitur", "medium", "Obligations presuppose agents, but not that life protection is the ground of all obligations."),
    32: ("non-sequitur", "medium", "Knowledge requires agents; that does not establish a moral ranking."),
    33: ("category-error", "medium", "Interventions and counterfactuals are formal tools; they do not yield a moral target."),
    34: ("category-error", "medium", "Counterfactual value may require subjects, but that is a contested metaethical premise."),
    35: ("heuristic", "medium", "Invariants are useful in program verification, but 'life=0' is not a program state."),
    36: ("heuristic", "medium", "Model checking can verify temporal properties, but the moral target is not a finite-state model."),
    37: ("category-error", "medium", "Curry-Howard does not ground moral value."),
    38: ("heuristic", "medium", "Worst-case control design is useful, but the analogy to ethics is not a proof."),
    39: ("heuristic", "medium", "A control barrier requires dynamics and a safe set; 'life>0' is not specified as one."),
    40: ("heuristic", "medium", "Viability kernels are formal; the moral conclusion is not derived."),
    41: ("heuristic", "medium", "Tail risk is relevant, but extinction is not a quantified random variable in the paper."),
    42: ("heuristic", "medium", "Maximin is a decision rule under uncertainty, not a proof of life's priority."),
    43: ("heuristic", "medium", "Minimax regret is a decision rule; it does not entail a lexicographic life constraint."),
    44: ("heuristic", "medium", "Epsilon-constraints are a modeling choice. Life as a hard constraint is asserted, not derived."),
    45: ("non-sequitur", "medium", "Incentive compatibility does not imply life-first."),
    46: ("heuristic", "medium", "Hazard functions are a tool; 'life-first' is not a hazard model."),
    47: ("heuristic", "medium", "Absorbing states are real, but the moral conclusion is not derived."),
    48: ("heuristic", "medium", "'Loss of life' as a top event is a design choice; the analysis does not establish priority."),
    49: ("category-error", "medium", "Network connectivity is not moral value."),
    50: ("non-sequitur", "medium", "Contracts require parties; they do not require life-first."),
    51: ("non-sequitur", "high", "A parliament of theories may not unanimously approve life-first; the claim is asserted."),
    52: ("non-sequitur", "medium", "Aumann's theorem requires common priors and honest updating; it does not imply convergence on life-first."),
    53: ("heuristic", "medium", "Strict scrutiny is a legal analogy; 'life' is not a legal right in the relevant sense."),
    54: ("heuristic", "medium", "The V-model is an engineering method; the choice of top requirement is normative."),
    55: ("non-sequitur", "medium", "Pareto optimality does not imply life-first; many allocations are Pareto optimal."),
    56: ("heuristic", "medium", "Dynamic programming requires an objective; life-first is not derived."),
    57: ("non-sequitur", "high", "Falsifiability is a scientific norm; the paper's claim is not falsifiable as stated."),
    58: ("non-sequitur", "medium", "Coherence of beliefs does not imply a moral axiom."),
    59: ("non-sequitur", "medium", "Bargaining solutions depend on disagreement points; life-first is not derived."),
    60: ("category-error", "medium", "Moral value is not an initial object in a category."),
    61: ("misapplied-formalism", "high", "Stability of a dynamical system is not moral stability."),
    62: ("heuristic", "medium", "Lyapunov stability is a control tool; the moral conclusion is not derived."),
    63: ("misapplied-formalism", "high", "Self-referential provability does not ground ethics."),
    64: ("category-error", "medium", "Channel capacity is not truth."),
    65: ("non-sequitur", "medium", "Induction requires a base case; the paper asserts one rather than proving it."),
    66: ("category-error", "medium", "Computability does not imply purpose."),
    67: ("non-sequitur", "medium", "Loss functions are designed, not discovered; life-first is not a natural loss."),
    68: ("misapplied-formalism", "medium", "The verification principle is self-undermining and is not a moral criterion."),
    69: ("heuristic", "medium", "Extinction payoffs can support cooperation, but the specific norm is not derived."),
    70: ("category-error", "medium", "Symmetry and conservation are physical theorems; moral values are not conserved quantities."),
    71: ("category-error", "medium", "Continuity of a function is not moral continuity."),
    72: ("misapplied-formalism", "high", "Brouwer requires a continuous map from a compact convex set; no such map is defined."),
    73: ("misapplied-formalism", "high", "Gödel-Rosser strengthens incompleteness; it does not yield a moral axiom."),
    74: ("misapplied-formalism", "medium", "Finite satisfiability does not imply moral truth."),
    75: ("category-error", "medium", "Order in combinatorial structures is not moral order."),
    76: ("category-error", "medium", "Model size is not moral scale."),
    77: ("misapplied-formalism", "high", "Rice's theorem concerns program properties; it does not imply a safety axiom."),
    78: ("misapplied-formalism", "high", "Undecidability does not imply a moral default."),
    79: ("non-sequitur", "medium", "Market equilibrium does not imply life-first."),
    80: ("empirical-unsupported", "high", "Longevity is not evidence of truth; many false beliefs persist."),
    81: ("category-error", "medium", "Expressive power of second-order logic is not moral truth."),
    82: ("heuristic", "medium", "State transitions do not imply moral priority."),
    83: ("heuristic", "medium", "Stability is a mathematical property; moral stability is undefined."),
    84: ("non-sequitur", "medium", "Computational hardness does not imply a moral axiom."),
    85: ("heuristic", "medium", "Sensitivity is real; 'life-first is the strange attractor' is a metaphor."),
    86: ("non-sequitur", "medium", "Pareto optimality does not imply life-first."),
    87: ("heuristic", "medium", "Repeated risks can lead to ruin, but the specific principle is not derived."),
    88: ("non-sequitur", "medium", "The Monty Hall problem is a probability puzzle with no moral conclusion."),
    89: ("category-error", "medium", "Population genetics is irrelevant to the moral thesis."),
    90: ("category-error", "medium", "Distribution convergence is not moral convergence."),
    91: ("heuristic", "medium", "Convexity is a risk tool; the moral conclusion is not derived."),
    92: ("non-sequitur", "medium", "Bargaining solutions do not imply life-first."),
    93: ("empirical-unsupported", "medium", "The Great Filter is a hypothesis; 'life-first is the only way through' is unsupported."),
    94: ("category-error", "medium", "Universality of computation is not moral universality."),
    95: ("heuristic", "medium", "Small causes can have large effects; the moral conclusion is not derived."),
    96: ("heuristic", "medium", "Extinction payoffs can change equilibria; the specific norm is not derived."),
    97: ("category-error", "medium", "An infinite-expectation paradox does not resolve moral priority."),
    98: ("category-error", "medium", "Infinite regress in motion is not moral regress."),
    99: ("non-sequitur", "medium", "Long-run averages do not show that life-first is true."),
    100: ("category-error", "medium", "Universal approximation does not imply a safety constraint."),
    101: ("category-error", "medium", "Compression/relevance trade-offs are not moral value."),
    102: ("category-error", "medium", "Thermodynamics is not ethics."),
    103: ("non-sequitur", "high", "Selection effects explain why observers see life-permitting conditions; they do not establish moral priority."),
    104: ("false", "high", "Observation in quantum mechanics is not consciousness. The claim is pop-science."),
    105: ("non-sequitur", "medium", "Fairness requires agents; it does not imply life-first."),
    106: ("misapplied-formalism", "high", "Banach's theorem requires a contraction mapping; none is defined."),
    107: ("heuristic", "medium", "Temporal discounting is a bias; life-first is not a correction."),
    108: ("category-error", "medium", "The pigeonhole principle is not resource ethics."),
    109: ("category-error", "medium", "The uncertainty principle is physics, not ethics."),
    110: ("category-error", "medium", "Metric geometry is not moral efficiency."),
    111: ("misapplied-formalism", "medium", "Proof length is not moral simplicity."),
    112: ("non-sequitur", "medium", "Utility theory does not imply infinite value of life."),
    113: ("non-sequitur", "high", "Bivalence does not imply 'silence equals betrayal.'"),
    114: ("category-error", "medium", "Determinism is not moral value."),
    115: ("category-error", "medium", "Symmetry is not moral universality."),
    116: ("category-error", "medium", "Quantum entanglement is not moral entanglement."),
    117: ("category-error", "medium", "Network centrality is not moral importance."),
    118: ("category-error", "medium", "Cryptographic verification is not ethical verification."),
    119: ("category-error", "medium", "Physics is not ethics."),
    120: ("heuristic", "medium", "Redundancy is useful; 'life-first is the moral parity bit' is a metaphor."),
    121: ("non-sequitur", "high", "Simplicity does not establish truth or priority."),
    122: ("category-error", "medium", "Statistical information is not moral information."),
    123: ("heuristic", "medium", "Extinction payoffs can change equilibria; the specific norm is not derived."),
    124: ("heuristic", "medium", "Heuristics are useful; life-first is not the only viable default."),
    125: ("heuristic", "medium", "History can matter, but the moral conclusion is not derived."),
    126: ("non-sequitur", "medium", "Social-choice monotonicity is not life-first."),
    127: ("category-error", "medium", "Error distance is not moral deviation."),
    128: ("category-error", "medium", "Optimization duality is not moral constraint."),
    129: ("category-error", "medium", "Ordinals are not a moral hierarchy."),
    130: ("non-sequitur", "medium", "Belief updating is not moral priority."),
    131: ("heuristic", "medium", "Constrained optimization is a tool; the choice of constraint is normative."),
    132: ("category-error", "medium", "Linear systems are not moral systems."),
    133: ("non-sequitur", "medium", "Comparative advantage is not a moral principle."),
    134: ("rhetorical", "medium", "Self-similarity is a metaphor, not an argument."),
    135: ("heuristic", "medium", "Life-first may expand the feasible frontier; this is not proved."),
    136: ("category-error", "medium", "Information reversibility is not moral reversibility."),
    137: ("category-error", "medium", "Membership functions are not moral truth."),
    138: ("category-error", "medium", "Statistical mechanics is not ethics."),
    139: ("non-sequitur", "medium", "Self-application is a consistency check, not a proof."),
    140: ("heuristic", "medium", "Fault tolerance is useful; the moral conclusion is not derived."),
    141: ("heuristic", "medium", "Project management is not ethics."),
    142: ("category-error", "medium", "Inference under uncertainty is not moral priority."),
    143: ("empirical-unsupported", "high", "Social tipping points are complex; the claim is not established."),
    144: ("heuristic", "medium", "Resource allocation is a tool; the normative criterion is not derived."),
    145: ("category-error", "medium", "Topology is not ethics."),
    146: ("heuristic", "medium", "Control stability is not moral stability."),
    147: ("non-sequitur", "medium", "Mechanism design is not a moral foundation."),
    148: ("misapplied-formalism", "medium", "Completeness of first-order logic does not imply life-first."),
    149: ("category-error", "medium", "Matching algorithms are not moral matchings."),
    150: ("heuristic", "medium", "Optimization is a tool; the objective is not derived."),
    151: ("empirical-unsupported", "medium", "Multi-agent learning is complex; the claim is speculative."),
    152: ("category-error", "medium", "Geometry is not ethics."),
    153: ("rhetorical", "low", "Operating systems are not moral agents."),
    154: ("rhetorical", "medium", "Chaos is a metaphor here, not a moral argument."),
    155: ("heuristic", "medium", "Tail risk is relevant, but extinction is not quantified."),
    156: ("non-sequitur", "medium", "Utility theory does not imply that life is non-substitutable."),
    157: ("non-sequitur", "medium", "Fairness metrics do not imply life-first."),
    158: ("heuristic", "medium", "Reducing search space is useful; the moral conclusion is not derived."),
    159: ("non-sequitur", "medium", "Modus tollens is valid only if the premises are; the premises are not established."),
    160: ("category-error", "medium", "Syntax is not semantics or ethics."),
    161: ("category-error", "medium", "Neuroscience is not ethics."),
    162: ("non-sequitur", "medium", "Long-run averages do not show that life-first is true."),
    163: ("non-sequitur", "medium", "Economics is not ethics."),
    164: ("misapplied-formalism", "medium", "Self-reference in computation is not moral self-grounding."),
    165: ("non-sequitur", "high", "The slippery-slope fallacy is named, not avoided; the claim is asserted."),
    166: ("category-error", "medium", "Thermodynamics is not moral direction."),
    167: ("heuristic", "medium", "Network resilience is a tool; the moral conclusion is not derived."),
    168: ("non-sequitur", "medium", "Optimizing optimizers does not imply life-first."),
    169: ("empirical-unsupported", "medium", "Self-generation is a biological concept; the moral conclusion is not derived."),
    170: ("heuristic", "medium", "Repurposing is a metaphor; no moral conclusion follows."),
    171: ("non-sequitur", "high", "The principle of sufficient reason does not imply life-first and may be false."),
    172: ("category-error", "medium", "Quantum information is not moral information."),
    173: ("heuristic", "medium", "Regret minimization is a decision rule; the specific principle is not derived."),
    174: ("category-error", "medium", "Information theory is not ethics."),
    175: ("category-error", "medium", "Geometry is not ethics."),
    176: ("category-error", "medium", "Neuroscience is not ethics."),
    177: ("category-error", "medium", "Functional programming is not ethics."),
    178: ("category-error", "medium", "Linguistics is not ethics."),
    179: ("category-error", "medium", "Belief updating is not moral learning."),
    180: ("category-error", "medium", "Information dependence is not moral dependence."),
    181: ("empirical-unsupported", "high", "Evolutionary stability depends on the game; the claim is false as stated."),
    182: ("category-error", "medium", "Probabilistic boundaries are not moral boundaries."),
    183: ("heuristic", "medium", "Temporal bias is real; life-first is not a correction."),
    184: ("rhetorical", "medium", "Dynamical-systems talk is a metaphor here."),
    185: ("category-error", "medium", "Semiotics is not ethics."),
    186: ("heuristic", "medium", "Multi-criteria analysis is a tool; the choice of criteria is normative."),
    187: ("category-error", "medium", "Encoding is not moral truth."),
    188: ("empirical-unsupported", "medium", "Criticality is a hypothesis; the moral claim is not derived."),
    189: ("rhetorical", "medium", "A speculative physics theory does not yield a moral conclusion."),
    190: ("non-sequitur", "medium", "Communication requires shared assumptions; it does not imply life-first."),
    191: ("false", "medium", "'Conservation of moral mass' is invented; there is no such conservation law."),
    192: ("misapplied-formalism", "medium", "The halting problem does not imply a moral default."),
    193: ("misapplied-formalism", "high", "Gödel's second theorem does not imply an external moral axiom."),
    194: ("category-error", "medium", "Physics is not ethics."),
    195: ("category-error", "medium", "Recursion is not moral grounding."),
    196: ("heuristic", "medium", "Constraint satisfaction is a tool; the constraints are normative."),
    197: ("heuristic", "medium", "Reflective equilibrium is a method; it does not uniquely select life-first."),
    198: ("rhetorical", "medium", "Cosmological typicality is not moral priority."),
    199: ("heuristic", "medium", "Robustness is a virtue; the claim is not established."),
    200: ("non-sequitur", "medium", "Semantic grounding is not moral priority."),
    201: ("non-sequitur", "medium", "Efficiency is not ethics."),
    202: ("valid-but-insufficient", "medium", "A temporal safety invariant does not establish priority."),
    203: ("category-error", "medium", "Optimization geometry is not ethics."),
    204: ("empirical-unsupported", "high", "Longevity is not evidence of truth."),
    205: ("rhetorical", "low", "Cellular automata are not moral systems."),
    206: ("rhetorical", "medium", "Emergence is a metaphor here."),
    207: ("non-sequitur", "medium", "Foundationalism versus coherentism is a metaethical debate; the paper asserts a foundation."),
    208: ("category-error", "medium", "Physics is not ethics."),
    209: ("misapplied-formalism", "medium", "A fixed-point theorem does not imply that life-first is the ethical fixed point."),
    210: ("rhetorical", "low", "A programming analogy is not an ethical argument."),
}


def titles() -> list[str]:
    text = SOURCE.read_text(encoding="utf-8")
    start = text.find("Catalogue of Theorem-Level Stress Tests")
    if start < 0:
        raise SystemExit("Appendix D heading not found")
    found: dict[int, str] = {}
    for line in text[start:].splitlines():
        match = re.match(r"^\s*(\d{1,3})\.\s+(.*\S)\s*$", line)
        if match:
            number = int(match.group(1))
            if 1 <= number <= 210 and number not in found:
                found[number] = match.group(2)
    missing = [n for n in range(1, 211) if n not in found]
    if missing:
        raise SystemExit(f"Missing stress-test titles: {missing}")
    return [found[n] for n in range(1, 211)]


def main() -> None:
    rows = []
    for number, title in enumerate(titles(), 1):
        verdict, severity, note = V[number]
        rows.append({
            "id": f"ST{number:03d}",
            "number": number,
            "title": title,
            "verdict": verdict,
            "severity": severity,
            "note": note,
        })
    payload = {
        "schema_version": 1,
        "source": "source/WISLIM-v2.0.1.txt",
        "paper_claim": "Appendix D presents 210 'theorem-level' stress tests that allegedly converge on life-first.",
        "audit_summary": {
            "total": len(rows),
            "verdict_counts": {
                verdict: sum(1 for row in rows if row["verdict"] == verdict)
                for verdict in sorted({row["verdict"] for row in rows})
            },
            "severity_counts": {
                severity: sum(1 for row in rows if row["severity"] == severity)
                for severity in sorted({row["severity"] for row in rows})
            },
        },
        "tests": rows,
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT} with {len(rows)} rows")
    print(json.dumps(payload["audit_summary"], indent=2))


if __name__ == "__main__":
    main()
