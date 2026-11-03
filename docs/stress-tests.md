# Stress-test catalog

Appendix D of the paper presents 210 entries as "theorem-level stress tests."
The audit classifies each entry by verdict and severity. The machine-readable
catalog is `model/stress-tests.json`; the argument-level critique is in
`audit/08-formal-and-scientific-claims.md`.

The catalog is a classification, not a proof. A verdict of `heuristic` means the
analogy is suggestive but not probative. A verdict of `category-error` means a
concept from one domain is applied to another without justification. A verdict
of `valid-but-insufficient` means the formal point is correct but does not
establish the thesis.

## Summary

| Verdict | Count | Meaning |
|---|---:|---|
| `category-error` | 66 | A concept from one domain is applied to another without justification. |
| `empirical-unsupported` | 9 | An empirical claim is asserted without evidence. |
| `false` | 2 | The claim is factually wrong. |
| `heuristic` | 51 | The analogy is suggestive but not probative. |
| `misapplied-formalism` | 19 | A formal result is misstated or used outside its conditions. |
| `non-sequitur` | 51 | The conclusion does not follow from the cited result. |
| `rhetorical` | 9 | A metaphor or slogan, not an argument. |
| `valid-but-insufficient` | 3 | The formal point is correct but does not establish the thesis. |

| Severity | Count |
|---|---:|
| high | 35 |
| low | 3 |
| medium | 172 |

## Full catalog

| ID | # | Title | Verdict | Severity |
|---|---:|---|---|---|
| ST001 | 1 | Gödel’s Incompleteness (meta-logic) | `misapplied-formalism` | high |
| ST002 | 2 | Cantor’s Diagonalization (lists can’t close the set) | `misapplied-formalism` | high |
| ST003 | 3 | Modal Logic (necessity vs. possibility) | `non-sequitur` | high |
| ST004 | 4 | Decision Theory / Expected Utility | `non-sequitur` | high |
| ST005 | 5 | Game Theory / Nash Stability | `non-sequitur` | high |
| ST006 | 6 | Information Theory (signal, entropy, meaning) | `category-error` | high |
| ST007 | 7 | Evolutionary Game Theory / Replicator Dynamics | `empirical-unsupported` | high |
| ST008 | 8 | Thermodynamics / Far-from-equilibrium Systems | `category-error` | high |
| ST009 | 9 | Pascal’s Wager / Risk Dominance | `heuristic` | medium |
| ST010 | 10 | Fixed-Point Theorems (stability under iteration) | `misapplied-formalism` | high |
| ST011 | 11 | Cooperation Theorems / Repeated Prisoner’s Dilemma | `heuristic` | medium |
| ST012 | 12 | Kolmogorov Complexity / Minimum Description Length | `non-sequitur` | medium |
| ST013 | 13 | Tarski’s Undefinability of Truth (meta-levels again) | `category-error` | high |
| ST014 | 14 | Catastrophe Theory / Tipping Points | `heuristic` | medium |
| ST015 | 15 | Moral Philosophy Triangulation (Kant, Utilitarianism, Virtue) | `non-sequitur` | high |
| ST016 | 16 | Bayes’ Theorem (evidence aggregation) | `non-sequitur` | high |
| ST017 | 17 | No Free Lunch Theorem (optimization limits) | `non-sequitur` | medium |
| ST018 | 18 | Arrow’s Impossibility Theorem (voting paradoxes) | `misapplied-formalism` | high |
| ST019 | 19 | Second Law of Thermodynamics (entropy growth) | `category-error` | medium |
| ST020 | 20 | Survivorship Bias (hidden failures) | `non-sequitur` | medium |
| ST021 | 21 | Reductio ad Absurdum (proof by contradiction) | `non-sequitur` | high |
| ST022 | 22 | Black Swan Theory (rare catastrophic events) | `heuristic` | medium |
| ST023 | 23 | Precautionary Principle (burden of proof under risk) | `heuristic` | medium |
| ST024 | 24 | Kant’s Universalizability (categorical imperative) | `non-sequitur` | high |
| ST025 | 25 | Sigma (Σ) Collapse of Values | `valid-but-insufficient` | medium |
| ST026 | 26 | Set Theory / Support Non-Emptiness | `category-error` | medium |
| ST027 | 27 | Order Theory / Lexicographic Priority | `non-sequitur` | medium |
| ST028 | 28 | Measure Theory / Absolute Continuity of Value on Life | `category-error` | medium |
| ST029 | 29 | Category Theory (Arrows Require Objects) | `category-error` | medium |
| ST030 | 30 | Temporal Logic (LTL/CTL) Safety Invariant | `valid-but-insufficient` | medium |
| ST031 | 31 | Deontic Logic (Obligation Semantics) | `non-sequitur` | medium |
| ST032 | 32 | Epistemic Logic / Common Knowledge | `non-sequitur` | medium |
| ST033 | 33 | Causal Inference (do-Calculus) | `category-error` | medium |
| ST034 | 34 | Counterfactuals (Structural Causal Models) | `category-error` | medium |
| ST035 | 35 | Program Verification / Invariant Proofs | `heuristic` | medium |
| ST036 | 36 | Model Checking (Automata over Policies) | `heuristic` | medium |
| ST037 | 37 | Type Theory / Curry–Howard (Lightweight Analogy) | `category-error` | medium |
| ST038 | 38 | Robust Control (H-∞ / Worst-Case Design) | `heuristic` | medium |
| ST039 | 39 | Control Barrier Certificates | `heuristic` | medium |
| ST040 | 40 | Viability Theory (Aubin) | `heuristic` | medium |
| ST041 | 41 | Risk Measures (CVaR / Tail Risk) | `heuristic` | medium |
| ST042 | 42 | Maximin (Rawlsian Security) | `heuristic` | medium |
| ST043 | 43 | Minimax Regret | `heuristic` | medium |
| ST044 | 44 | Multi-Objective Optimization / Pareto & ε-Constraint | `heuristic` | medium |
| ST045 | 45 | Mechanism Design / Incentive Compatibility | `non-sequitur` | medium |
| ST046 | 46 | Survival Analysis (Hazard Functions) | `heuristic` | medium |
| ST047 | 47 | Markov Chains / Absorbing States | `heuristic` | medium |
| ST048 | 48 | Reliability Engineering / Fault-Tree Top Event | `heuristic` | medium |
| ST049 | 49 | Percolation Theory / Network Robustness | `category-error` | medium |
| ST050 | 50 | Social Contract Stability (Hobbes–Rousseau Frame) | `non-sequitur` | medium |
| ST051 | 51 | Moral Uncertainty “Parliament” Models | `non-sequitur` | high |
| ST052 | 52 | Aumann Agreement Theorem (common priors, rationality) | `non-sequitur` | medium |
| ST053 | 53 | Legal Strict Scrutiny Analogy | `heuristic` | medium |
| ST054 | 54 | Systems Engineering “V-Model” (Top Requirement) | `heuristic` | medium |
| ST055 | 55 | Pareto Optimality (Economics) | `non-sequitur` | medium |
| ST056 | 56 | Bellman Optimality (Dynamic Programming) | `heuristic` | medium |
| ST057 | 57 | Falsifiability (Popperian Science) | `non-sequitur` | high |
| ST058 | 58 | Bayesian Coherence (Dutch Book Argument) | `non-sequitur` | medium |
| ST059 | 59 | Nash Bargaining Solution | `non-sequitur` | medium |
| ST060 | 60 | Category Theory (Initial Object) | `category-error` | medium |
| ST061 | 61 | Stability of Fixed Points (Dynamical Systems) | `misapplied-formalism` | high |
| ST062 | 62 | Lyapunov Stability (Control Theory) | `heuristic` | medium |
| ST063 | 63 | Gödel–Löb’s Theorem (Self-referential consistency) | `misapplied-formalism` | high |
| ST064 | 64 | Shannon Capacity (Information Theory) | `category-error` | medium |
| ST065 | 65 | Induction Principle (Mathematics) | `non-sequitur` | medium |
| ST066 | 66 | Church–Turing Thesis (Computability) | `category-error` | medium |
| ST067 | 67 | Entropy Minimization in Learning (Machine Learning) | `non-sequitur` | medium |
| ST068 | 68 | Logical Positivism (Verification Principle) | `misapplied-formalism` | medium |
| ST069 | 69 | Prisoner’s Dilemma with Extinction Payoff | `heuristic` | medium |
| ST070 | 70 | Noether’s Theorem (Symmetry & Conservation) | `category-error` | medium |
| ST071 | 71 | Mean Value Theorem (continuity & slope guarantee) | `category-error` | medium |
| ST072 | 72 | Brouwer Fixed-Point Theorem (maps to itself) | `misapplied-formalism` | high |
| ST073 | 73 | Gödel–Rosser Strengthening (consistency under weaker assumptions) | `misapplied-formalism` | high |
| ST074 | 74 | Compactness Theorem (finite subsets imply whole) | `misapplied-formalism` | medium |
| ST075 | 75 | Ramsey Theory (order in chaos) | `category-error` | medium |
| ST076 | 76 | Löwenheim–Skolem Theorem (models of all sizes) | `category-error` | medium |
| ST077 | 77 | Rice’s Theorem (nontrivial program properties undecidable) | `misapplied-formalism` | high |
| ST078 | 78 | Halting Problem (undecidable processes) | `misapplied-formalism` | high |
| ST079 | 79 | Arrow–Debreu Equilibrium (general economics) | `non-sequitur` | medium |
| ST080 | 80 | Lindy Effect (longer survival = longer expectation) | `empirical-unsupported` | high |
| ST081 | 81 | Second-Order Logic Strength (beyond first-order) | `category-error` | medium |
| ST082 | 82 | Markov Chains (future depends only on present state) | `heuristic` | medium |
| ST083 | 83 | Eigenvalue Stability (systems stability) | `heuristic` | medium |
| ST084 | 84 | P vs NP (hardness of problems) | `non-sequitur` | medium |
| ST085 | 85 | Chaos Theory (sensitive dependence on initial conditions) | `heuristic` | medium |
| ST086 | 86 | Pareto Optimality (no one worse off) | `non-sequitur` | medium |
| ST087 | 87 | Borel–Cantelli Lemma (probability of repeated events) | `heuristic` | medium |
| ST088 | 88 | Monty Hall Problem (counterintuitive probabilities) | `non-sequitur` | medium |
| ST089 | 89 | Hardy–Weinberg Equilibrium (population genetics) | `category-error` | medium |
| ST090 | 90 | Central Limit Theorem (distribution convergence) | `category-error` | medium |
| ST091 | 91 | Jensen’s Inequality (convexity principle) | `heuristic` | medium |
| ST092 | 92 | Nash Bargaining Solution (variant) | `non-sequitur` | medium |
| ST093 | 93 | Fermi Paradox (where is everyone?) | `empirical-unsupported` | medium |
| ST094 | 94 | Turing Completeness (expressive systems) | `category-error` | medium |
| ST095 | 95 | Butterfly Effect (small causes, big effects) | `heuristic` | medium |
| ST096 | 96 | Prisoner’s Dilemma with Extinction Payoff (variant) | `heuristic` | medium |
| ST097 | 97 | St. Petersburg Paradox (infinite expectations) | `category-error` | medium |
| ST098 | 98 | Zeno’s Paradoxes (infinite regress problems) | `category-error` | medium |
| ST099 | 99 | Law of Large Numbers (averages converge with trials) | `non-sequitur` | medium |
| ST100 | 100 | Universal Approximation Theorem (neural networks) | `category-error` | medium |
| ST101 | 101 | Information Bottleneck Principle (Trade-off of Compression vs. Relevance) | `category-error` | medium |
| ST102 | 102 | Minimum Energy Principle (Physics Thermodynamic Pathways) | `category-error` | medium |
| ST103 | 103 | Anthropic Conditioning in Cosmology (Selection Effects) | `non-sequitur` | high |
| ST104 | 104 | Quantum Observer Effect (Measurement Requires Observation) | `false` | high |
| ST105 | 105 | Game-Theoretic Envy-Free Allocations | `non-sequitur` | medium |
| ST106 | 106 | Banach Fixed Point Theorem (Contraction Mapping Guarantee) | `misapplied-formalism` | high |
| ST107 | 107 | Temporal Discounting in Behavioral Economics | `heuristic` | medium |
| ST108 | 108 | Dirichlet Principle (Pigeonhole Argument) | `category-error` | medium |
| ST109 | 109 | Heisenberg Uncertainty Principle | `category-error` | medium |
| ST110 | 110 | Triangle Inequality (Metric Space Constraint) | `category-error` | medium |
| ST111 | 111 | Gödel’s Speed-Up Theorem (Proof Length Explosion) | `misapplied-formalism` | medium |
| ST112 | 112 | Law of Diminishing Marginal Utility | `non-sequitur` | medium |
| ST113 | 113 | Law of the Excluded Middle (Classical Logic) | `non-sequitur` | high |
| ST114 | 114 | Laplace’s Demon (Deterministic Prediction Limit) | `category-error` | medium |
| ST115 | 115 | Invariance under Transformation (Symmetry Principles) | `category-error` | medium |
| ST116 | 116 | Bell’s Theorem (Non-Local Correlation Constraints) | `category-error` | medium |
| ST117 | 117 | Eigenvector Centrality (Network Influence Metric) | `category-error` | medium |
| ST118 | 118 | Zero-Knowledge Proofs (Verification without Disclosure) | `category-error` | medium |
| ST119 | 119 | Principle of Least Action (Lagrangian Physics) | `category-error` | medium |
| ST120 | 120 | Error-Correcting Codes (Preservation under Noise) | `heuristic` | medium |
| ST121 | 121 | Occam’s Razor (Principle of Parsimony) | `non-sequitur` | high |
| ST122 | 122 | Fisher Information (Sensitivity of Likelihood) | `category-error` | medium |
| ST123 | 123 | Nash Equilibrium with Extinction Cost | `heuristic` | medium |
| ST124 | 124 | Bounded Rationality (Limits of Decision Making) | `heuristic` | medium |
| ST125 | 125 | Hysteresis in Dynamical Systems | `heuristic` | medium |
| ST126 | 126 | Monotonicity in Social Choice | `non-sequitur` | medium |
| ST127 | 127 | Hamming Distance (Error Sensitivity Measure) | `category-error` | medium |
| ST128 | 128 | Duality in Optimization (Primal-Dual Relationship) | `category-error` | medium |
| ST129 | 129 | Transfinite Induction (Ordinal Progressions Beyond Infinity) | `category-error` | medium |
| ST130 | 130 | Temporal Coherence in Belief Updating | `non-sequitur` | medium |
| ST131 | 131 | Lagrange Multipliers (Constrained Optimization Method) | `heuristic` | medium |
| ST132 | 132 | Principle of Superposition (Linear System Solutions) | `category-error` | medium |
| ST133 | 133 | Ricardian Comparative Advantage (Trade Efficiency) | `non-sequitur` | medium |
| ST134 | 134 | Fractal Self-Similarity (Scale-Invariant Patterns) | `rhetorical` | medium |
| ST135 | 135 | Pareto Frontier Expansion via Life-Priority Constraint | `heuristic` | medium |
| ST136 | 136 | Reversible Computation (No Information Loss) | `category-error` | medium |
| ST137 | 137 | Fuzzy Logic Membership Functions | `category-error` | medium |
| ST138 | 138 | Ergodic Hypothesis (Time Averages = Ensemble Averages) | `category-error` | medium |
| ST139 | 139 | Moral Reflexivity (Meta-Ethical Feedback) | `non-sequitur` | medium |
| ST140 | 140 | Redundancy in Fault-Tolerant Design | `heuristic` | medium |
| ST141 | 141 | Critical Path Method (Project Dependency Analysis) | `heuristic` | medium |
| ST142 | 142 | Principle of Maximum Entropy (Inference Under Uncertainty) | `category-error` | medium |
| ST143 | 143 | Phase Transitions in Complex Systems | `empirical-unsupported` | high |
| ST144 | 144 | Resource-Constrained Scheduling | `heuristic` | medium |
| ST145 | 145 | Topological Invariants (Persistent Properties under Deformation) | `category-error` | medium |
| ST146 | 146 | Control Lyapunov Functions (Asymptotic Stability Design) | `heuristic` | medium |
| ST147 | 147 | Nash Implementation (Mechanism Design Realizability) | `non-sequitur` | medium |
| ST148 | 148 | Gödel’s Completeness Theorem (Syntactic and Semantic Equivalence) | `misapplied-formalism` | medium |
| ST149 | 149 | Stable Marriage Problem (Gale-Shapley Algorithm) | `category-error` | medium |
| ST150 | 150 | Gradient Descent (Local Minimization Algorithm) | `heuristic` | medium |
| ST151 | 151 | Multi-Agent Reinforcement Learning (MARL Instability) | `empirical-unsupported` | medium |
| ST152 | 152 | Non-Euclidean Geometry (Curved Space Foundations) | `category-error` | medium |
| ST153 | 153 | Non-Blocking I/O in Operating Systems | `rhetorical` | low |
| ST154 | 154 | Chaos Threshold in Dynamical Systems | `rhetorical` | medium |
| ST155 | 155 | Expected Shortfall (Tail Risk Beyond VaR) | `heuristic` | medium |
| ST156 | 156 | Indifference Curve Analysis (Consumer Preference Theory) | `non-sequitur` | medium |
| ST157 | 157 | Algorithmic Fairness Constraints (AI Decision Systems) | `non-sequitur` | medium |
| ST158 | 158 | Combinatorial Explosion (Exponential Growth of Possibilities) | `heuristic` | medium |
| ST159 | 159 | Modus Tollens (Contrapositive Logic) | `non-sequitur` | medium |
| ST160 | 160 | Generative Grammar (Structure of Possible Sentences) | `category-error` | medium |
| ST161 | 161 | Hebbian Learning Rule (Neurons That Fire Together Wire Together) | `category-error` | medium |
| ST162 | 162 | Law of Large Numbers (Stabilization of Averages) | `non-sequitur` | medium |
| ST163 | 163 | Deadweight Loss (Inefficiency from Market Distortions) | `non-sequitur` | medium |
| ST164 | 164 | Recursion Theorem (Self-Referencing Computation) | `misapplied-formalism` | medium |
| ST165 | 165 | Slippery Slope Fallacy (Incremental Harm Rationalization) | `non-sequitur` | high |
| ST166 | 166 | Arrow of Time (Irreversibility of Temporal Flow) | `category-error` | medium |
| ST167 | 167 | Spectral Gap (System Resilience in Networks and Operators) | `heuristic` | medium |
| ST168 | 168 | Meta-Optimization (Tuning the Optimizers) | `non-sequitur` | medium |
| ST169 | 169 | Autopoiesis (Self-Generating Systems) | `empirical-unsupported` | medium |
| ST170 | 170 | Exaptation in Evolution (Repurposing Traits) | `heuristic` | medium |
| ST171 | 171 | Principle of Sufficient Reason (Nothing Without Cause) | `non-sequitur` | high |
| ST172 | 172 | Law of Conservation of Information (Quantum and Black Hole Theory) | `category-error` | medium |
| ST173 | 173 | Principle of Least Regret (Decision Making Under Uncertainty) | `heuristic` | medium |
| ST174 | 174 | Surprisal in Information Theory (Measuring Unexpectedness) | `category-error` | medium |
| ST175 | 175 | Ricci Flow (Geometrical Smoothing Process) | `category-error` | medium |
| ST176 | 176 | Temporal Binding (Perceptual Compression of Cause and Effect) | `category-error` | medium |
| ST177 | 177 | Monads in Functional Programming (Sequencing Effects Safely) | `category-error` | medium |
| ST178 | 178 | Universal Grammar Hypothesis (Innate Language Structures) | `category-error` | medium |
| ST179 | 179 | Bayesian Surprise (Measuring Informational Shift) | `category-error` | medium |
| ST180 | 180 | Mutual Information (Shared Signal Between Variables) | `category-error` | medium |
| ST181 | 181 | Nash Equilibrium in Evolutionary Biology | `empirical-unsupported` | high |
| ST182 | 182 | Markov Blanket (Boundary of Predictive Sufficiency) | `category-error` | medium |
| ST183 | 183 | Hyperbolic Discounting (Time-Inconsistent Preferences) | `heuristic` | medium |
| ST184 | 184 | Dynamic Systems with Attractors (Behavioral Gravitation Points) | `rhetorical` | medium |
| ST185 | 185 | Semiotic Triad (Sign, Object, Interpretant) | `category-error` | medium |
| ST186 | 186 | Multi-Criteria Decision Analysis (MCDA) | `heuristic` | medium |
| ST187 | 187 | Gödel Encoding (Symbolic Arithmetic of Logic) | `category-error` | medium |
| ST188 | 188 | Edge of Chaos (Criticality in Complex Systems) | `empirical-unsupported` | medium |
| ST189 | 189 | Invariant Set Theory (Quantum-Gravity Hypothesis) | `rhetorical` | medium |
| ST190 | 190 | Common Ground Theory (Shared Understanding in Communication) | `non-sequitur` | medium |
| ST191 | 191 | Conservation of Moral Mass (Ethical Continuity Hypothesis) | `false` | medium |
| ST192 | 192 | Turing’s Halting Problem (Undecidability of Program Termination) | `misapplied-formalism` | medium |
| ST193 | 193 | Gödel’s Second Incompleteness Theorem (Limits of Self-Proof) | `misapplied-formalism` | high |
| ST194 | 194 | Broken Symmetry (Spontaneous Divergence in Physics) | `category-error` | medium |
| ST195 | 195 | Y-Combinator (Fixed-Point Generator in Lambda Calculus) | `category-error` | medium |
| ST196 | 196 | Constraint Satisfaction Problem (CSP) | `heuristic` | medium |
| ST197 | 197 | Reflexive Equilibrium (Ethics + Theory Adjustment Loop) | `heuristic` | medium |
| ST198 | 198 | Principle of Mediocrity (Cosmological Typicality) | `rhetorical` | medium |
| ST199 | 199 | Counterfactual Robustness (Model Stability to Hypotheticals) | `heuristic` | medium |
| ST200 | 200 | Grounding Problem in Philosophy of Mind (How Symbols Gain Meaning) | `non-sequitur` | medium |
| ST201 | 201 | Transaction Cost Economics (Friction in Coordination) | `non-sequitur` | medium |
| ST202 | 202 | Temporal Logic (Reasoning Over Time) | `valid-but-insufficient` | medium |
| ST203 | 203 | Natural Gradient Descent (Curvature-Aware Optimization) | `category-error` | medium |
| ST204 | 204 | Lindy Effect (Durability Predicts Longevity) | `empirical-unsupported` | high |
| ST205 | 205 | Game of Life (Cellular Automaton by Conway) | `rhetorical` | low |
| ST206 | 206 | Emergence (Macro Patterns from Micro Rules) | `rhetorical` | medium |
| ST207 | 207 | Infinite Regress Problem (Unending Justification Chains) | `non-sequitur` | medium |
| ST208 | 208 | Thermodynamic Feasibility (First and Second Law Compliance) | `category-error` | medium |
| ST209 | 209 | Fixed Point Theorem (Existence of Stable States) | `misapplied-formalism` | medium |
| ST210 | 210 | Memory Safety in Systems Design | `rhetorical` | low |
