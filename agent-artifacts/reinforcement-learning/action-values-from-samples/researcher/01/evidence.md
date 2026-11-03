# Evidence: reinforcement-learning/action-values-from-samples (researcher 01)

The sources fully support the lesson's model-free step. Sutton and Barto show that greedy improvement over q needs no model, and they rewrite the policy improvement chain in q form (2nd ed., §5.2–5.3, pp. 96–98). They state exploring starts, why it is needed and why it often cannot be had (pp. 96–97), and print the Monte Carlo ES box (p. 99). The sources do not support a guarantee that the box algorithm reaches the optimal policy on this course's grid. As of November 2026, convergence of Monte Carlo ES as printed (first-visit returns, sample averages, greedy update after every episode, exploring starts) is proved only in special cases. Wang, Yuan, Shao and Ross (ICLR 2022) prove it for MDPs in which no state can be revisited under an optimal policy ("optimal policy feed-forward", OPFF), for any γ ≤ 1. Delattre and Fournier (SIAM J. Control Optim., 2026) prove a first-visit result for every finite MDP with γ < 1/2. Neither covers the grid. It is not OPFF, because cell 2's only optimal move, right, can slip into the top edge and leave the agent in cell 2, and its γ = 0.9. Tsitsiklis (JMLR 2002) and later work prove convergence for a modified algorithm that updates only the episode's starting pair, with uniform starts or with matched step sizes. There are counterexamples when the choice of starting pair depends on the current estimates: the initial-visit counterexamples of Bertsekas and Tsitsiklis (1996, cited), Wang et al. (2022, App. F) and Oliviers and Vinnicombe (2026 preprint), plus a 2026 preprint's first-visit construction supported by mean-field analysis and simulation rather than proof. For a fixed start distribution such as uniform over (cell, move), first-visit sample-average Monte Carlo ES on a non-OPFF MDP with γ ≥ 1/2 has neither a proof nor a counterexample. Sutton and Barto's "not yet been formally proved" (p. 99) therefore still holds for this grid. The commission's claim that interleaving "still reaches the optimal policy on this grid" can be supported only by runs across seeds, not by a theorem. The evidence is thin in two places. I could not open Bertsekas and Tsitsiklis's Example 5.12, which every later paper cites as the original counterexample. Both 2026 Cambridge papers are unreviewed arXiv preprints.

## Sources

### Sutton and Barto, Reinforcement Learning: An Introduction, 2nd ed.

```text
URL:         http://incompleteideas.net/book/RLbook2020.pdf (book page: http://incompleteideas.net/book/the-book-2nd.html)
Kind:        primary. The authors define Monte Carlo ES, introduced it (1998 edition, remark 5.3–4, p. 117) and own the "open question" statement.
Establishes: firsthand: the definitions, the box, the q-form improvement argument, the GPI framing, and the authors' own statement of MC ES convergence status. Their mention of Tsitsiklis 2002 is a pointer only.
Locators:    Printed page = PDF page − 22 (printed p. 99 is PDF p. 121).
```

Paraphrases, each with its locator:

- **Chapter 5 intro, p. 91.** Monte Carlo methods are defined only for episodic tasks. The chapter assumes that "all episodes eventually terminate no matter what actions are selected". Value estimates and policies change only when an episode ends. p. 92: chapter 5 adapts GPI from chapter 4 and learns values from sample returns instead of computing them from the MDP.
- **§5.2 Monte Carlo Estimation of Action Values, p. 96.** With a model, state values suffice to pick a policy by one-step lookahead. Without a model, "state values alone are not sufficient", so one must estimate the value of each action, and the goal becomes q\*. A pair (s, a) is visited when s is visited and a is taken there. First-visit and every-visit MC for q work as they do for states. Under a deterministic π, returns arrive for only one action per state, so the other estimates never improve.
- **§5.2, pp. 96–97, exploring starts.** One fix starts each episode in a state–action pair, with every pair having nonzero probability of being chosen, so that every pair is visited infinitely often in the limit. This is "the assumption of exploring starts". It "cannot be relied upon in general, particularly when learning directly from actual interaction with an environment". The common alternative is a stochastic policy that gives every action nonzero probability (treated in §5.4, p. 100).
- **§5.3 Monte Carlo Control, p. 97.** Control follows GPI. A small diagram shows evaluation (Q → q_π) and improvement (π → greedy(Q)). The two changes "work against each other to some extent ... but together they cause both policy and value function to approach optimality". Monte Carlo policy iteration alternates complete evaluation and complete improvement, π0 →E q_π0 →I π1 → … → π\* →E q\*. With infinitely many episodes and exploring starts, MC computes each q_πk exactly. Then "we have an action-value function, and therefore no model is needed to construct the greedy policy". Equation (5.1): π(s) ≐ argmax_a q(s, a).
- **§5.3, p. 98, q-form improvement.** For all s, q_πk(s, πk+1(s)) = q_πk(s, argmax_a q_πk(s, a)) = max_a q_πk(s, a) ≥ q_πk(s, πk(s)) ≥ v_πk(s). The policy improvement theorem (§4.2) then makes each πk+1 uniformly better than πk, or equally good, in which case both are optimal. "This in turn assures us that the overall process converges to the optimal policy". This guarantee rests on "two unlikely assumptions": exploring starts and infinitely many episodes per evaluation. The book removes the second by GPI: move the value function toward q_πk on each evaluation step without completing it. Value iteration is the extreme case. For Monte Carlo the natural choice is to "alternate between evaluation and improvement on an episode-by-episode basis".
- **Monte Carlo ES box, p. 99** (verified on the rendered page). π(s) and Q(s, a) are initialized arbitrarily and Returns(s, a) as empty lists. On each episode: choose S0, A0 "randomly such that all pairs have probability > 0", generate an episode following π, and set G ← 0. Then loop t = T−1, …, 0: G ← γG + R_{t+1}; unless (St, At) appears earlier in the episode (first-visit), append G to Returns(St, At), set Q(St, At) ← average(Returns(St, At)), and set π(St) ← argmax_a Q(St, a). Exercise 5.4 asks for the incremental mean-and-count form (§2.4).
- **Convergence statement, p. 99.** Returns are averaged "irrespective of what policy was in force when they were observed". MC ES cannot converge to a suboptimal policy, because the values would converge to that policy's values and the policy would then change. Stability occurs only at the optimum.
- **Example 5.3 Blackjack, pp. 99–100.** MC ES finds the optimal blackjack policy (Figure 5.2, p. 100). It matches Thorp's basic strategy except for one notch.
- **§4.6 Generalized Policy Iteration, pp. 86–87.** GPI is "the general idea of letting policy-evaluation and policy-improvement processes interact, independent of the granularity". If both processes continue to update all states, "the ultimate result is typically the same—convergence to the optimal value function and an optimal policy". If both processes stabilize, the policy is greedy with respect to its own value function, so the Bellman optimality equation holds and both are optimal. That is a fixed-point argument, not a convergence proof. p. 87: a two-line diagram shows the joint process approaching v\*, π\* even with "smaller, incomplete steps toward each goal".
- **§4.2 Policy Improvement, pp. 76–80.** (4.6), p. 78: q_π(s, a) = Σ p(s′, r | s, a)[r + γ v_π(s′)]. The theorem (4.7)/(4.8), p. 78: q_π(s, π′(s)) ≥ v_π(s) for all s implies v_π′(s) ≥ v_π(s). A strict inequality in (4.7) at a state gives a strict one in (4.8) there. The proof chain is on p. 78. Greedy policy (4.9), p. 79: argmax over q_π, written with the model. Ties may be split among maximizing actions (p. 79).
- **Bibliographical remark 5.3–4, p. 117.** MC ES was introduced in the 1998 edition. That "may have been the first explicit connection between Monte Carlo estimation and control methods based on policy iteration."

Quotes where the wording is itself the evidence:

```text
Quote (p. 99): "Convergence to this optimal fixed point seems inevitable as the changes to the action-value function decrease over time, but has not yet been formally proved. In our opinion, this is one of the most fundamental open theoretical questions in reinforcement learning (for a partial solution, see Tsitsiklis, 2002)."
Quote (p. 97): "In this case we have an action-value function, and therefore no model is needed to construct the greedy policy."
Quote (p. 96): "Without a model, however, state values alone are not sufficient."
```

### Sutton, "Open Theoretical Questions in Reinforcement Learning" (EuroCOLT '99)

```text
URL:         http://incompleteideas.net/papers/sutton-99.pdf
Kind:        primary. This is where Richard S. Sutton first posed the MC ES convergence question.
Establishes: firsthand: the problem statement as originally posed.
Paraphrase:  Control-case convergence results exist only for one-step bootstrapping methods, tabular Q(0) and Sarsa(0), and for no λ > 0. MC ES keeps Q(s, a) as the average of all completed returns that started by taking a in s. It selects actions greedily and explores by exploring starts. No proof of asymptotic convergence to Q* exists.
Locators:    §2 "Monte Carlo Control", author PDF p. 4. Proceedings of EuroCOLT '99, Springer, pp. 11–17. Oliviers & Vinnicombe 2026 cite the quote at p. 13.
Quote:       "It is hard to imagine any RL method simpler or more likely to converge than this, yet there remain no proof of asymptotic convergence to Q*."
```

### Tsitsiklis, "On the Convergence of Optimistic Policy Iteration", JMLR 3 (2002) 59–72

```text
URL:         https://www.jmlr.org/papers/v3/tsitsiklis02a.html (PDF: https://www.jmlr.org/papers/volume3/tsitsiklis02a/tsitsiklis02a.pdf)
Kind:        primary. John N. Tsitsiklis (LIDS, Massachusetts Institute of Technology) proves the theorems himself.
Establishes: firsthand: convergence of specific modified variants. Also his statement that the first-visit/every-visit variant remains open.
Paraphrase:  Setting: finite MDP, lookup tables, discounted cost with 0 < α < 1. Rewards are written as costs, minimized.
             (a) p. 60: he "settle[s]" Sutton's 1999 problem "for the case of a discounted cost criterion, under the assumption that every state-action pair is used to initialize the observed trajectories with the same frequency"; convergence "is not guaranteed if the trajectory initializations are made in an arbitrary manner".
             (b) Prop. 1, p. 63: synchronous version. Each iteration simulates one trajectory from every state, then J_{t+1} = (1 − γ_t)J_t + γ_t(J^{μt} + w_t), with μt greedy w.r.t. J_t and deterministic step sizes satisfying Σγ_t = ∞ and Σγ_t² < ∞. J_t → J* with probability 1. γ_t = 1/(t+1) with J_0 = 0 gives the plain average of returns (p. 62).
             (c) pp. 65–66: one start state per iteration, chosen uniformly at random, with only that state updated: still converges. A fixed nonuniform start distribution with a common deterministic step size cannot be handled by this proof, because the diagonal step matrix does not commute with P_μ. Nonuniform starts with step 1/n_t(i), the sample average of the returns that started at i, do converge. Both extensions are argued in the text ("the proof of Prop. 1 goes through with small modifications"; "the result remains valid"), not stated as separate propositions. Liu 2021 gives the nonuniform case as Proposition 16.
             (d) pp. 66–67: updating every state the trajectory visits, the first-visit or every-visit version, is "an open question". Arbitrary start selection (only "every state is selected infinitely often") fails: Example 5.12, pp. 234–236 of Bertsekas & Tsitsiklis (1996).
             (e) §5, pp. 70–71: §§3–4 "require knowledge of the system model" because a greedy policy w.r.t. J needs g_μ and P_μ. The Q-value version needs no model. Prop. 5, p. 71: synchronous Q-update, with one trajectory from every pair (i, u), first decision u, then greedy μt. It converges to Q* w.p. 1 for a discounted problem. The proof embeds pairs as extra states and applies Prop. 1.
             (f) §6, pp. 71–72: the trajectories are infinitely long, so the algorithm is "conceptual". Implementable versions truncate at a horizon T with α^T near zero, or restrict to problems with a zero-cost absorbing state that is reached eventually, or terminate with probability 1 − α per stage. The results "seem to be quite fragile". Still open: nonuniform-but-regular start selection, the every-visit version, undiscounted problems, and function approximation.
Locators:    pages as given (JMLR printed pages)
Quote:       p. 70: "The algorithms of the preceding two sections require knowledge of the system model. This is because gµ and Pµ are needed in order to generate a greedy policy µt corresponding to the current vector Jt." (The wording is evidence for the lesson's one idea from an independent analyst.)
```

### Liu, "On the convergence of reinforcement learning with Monte Carlo Exploring Starts", Automatica 129 (2021) 109693

```text
URL:         https://doi.org/10.1016/j.automatica.2021.109693 (free author copy with journal layout: https://www.math.uwaterloo.ca/~j49liu/papers/2021/liu2021convergence.pdf; preprint arXiv:2007.10916, July 2020, with different result numbering)
Kind:        primary. Jun Liu (Department of Applied Mathematics, University of Waterloo) proves the results.
Establishes: firsthand: extension of Tsitsiklis's start-pair-only variant to the undiscounted stochastic shortest path case, plus his statement that first-visit and every-visit remain open.
Paraphrase:  Undiscounted (α = 1) problem with a terminal state, called "MCES/optimistic policy iteration" following Tsitsiklis. Analysis is in state values J with a greedy step; Remark 17 asserts, without proof, that the model-free Q version and TD(λ) extend "without much difficulty".
             Theorem 10: if all policies are proper and step sizes satisfy Robbins–Monro, synchronous MCES converges to J* w.p. 1.
             §4 (Assumption 12, Proposition 14) relaxes properness: add a small per-step termination probability p_ε, and for small p_ε the modified problem keeps an optimal policy of the original.
             §5, Proposition 16: nonuniform random start selection converges with state-dependent steps 1/n_i(t) (the sample average, "the classical version of MCES" per Liu) or γ̂_t/p(i). §6: numerical two-state example; a common scalar step converges only for uniform selection (p = 0.5).
             §7 Conclusions: all results update only the start state. Convergence of the first-visit and every-visit versions is left as future work.
Locators:    Theorem 10 (§3); Assumption 12, Proposition 14 (§4); Proposition 16 (§5); Example 18 and Fig. 2 (§6); Remark 17; §7
```

### Wang, Yuan, Shao, Ross, "On the Convergence of the Monte Carlo Exploring Starts Algorithm for Reinforcement Learning", ICLR 2022

```text
URL:         https://arxiv.org/abs/2002.03585 (v2, 5 Aug 2022, headed "Published as a conference paper at ICLR 2022"; v1 Feb 2020 is cited by Liu as Wang and Ross)
Kind:        primary. Che Wang (New York University Shanghai and New York University), Shuhan Yuan, Kai Shao and Keith Ross (New York University Shanghai; Ross corresponding) prove their own theorems.
Establishes: firsthand: convergence of the original multi-update MCES on SFF and OPFF MDPs, a new counterexample, and a 2022 summary of the field. Their characterizations of Bertsekas & Tsitsiklis (1996) are secondhand.
Paraphrase:  Definitions, pp. 4–5. SFF: the MDP graph has no cycles. OPFF: the subgraph of transitions with positive probability under some optimal action is acyclic. "All SFF MDPs are OPFF, and all deterministic MDPs for which the optimal policy terminates w.p.1 are OPFF." They list S&B's deterministic gridworlds and blackjack as examples.
             Algorithm 1, p. 5: S&B's MCES without the first-visit check. It updates every pair along the episode, starts may follow any distribution as long as every pair is chosen infinitely often, and proofs hold for any γ ≤ 1 (p. 5).
             Theorem 1, p. 6: on SFF MDPs, Q_u → q* and π_u → π* w.p. 1. The proof is by backward induction and the strong law of large numbers, with no stochastic approximation.
             Theorem 2, p. 7: on OPFF MDPs, the same result for Algorithm 2. Algorithm 2 is first-visit, as in S&B, plus two changes: an episode that has not ended within M steps is cut off and its returns discarded, and Q starts at −∞. The cutoff exists "because an episode might never reach the terminal state for some policies (for example, due to cycling)".
             Corollary 1, p. 7: finite-horizon MCES (time in the state) converges for every MDP.
             Appendix F, pp. 26–31, Theorem 6: in an episodic MDP (two states plus terminal, γ < 1), the start-pair-only variant (Algorithm 4) fails to converge w.p. 1 under a specific schedule of exploring starts that depends on the current Q values.
             Conclusion and Figure 3, p. 9: convergence is established in three of four regions (uniform-rate updates on any MDP; original algorithm on OPFF). Original algorithm on non-OPFF is not covered, and some non-OPFF MDPs are known not to converge. "It still remains an open problem whether there exist conditions on MDPs that are weaker than the OPFF, and can still guarantee the convergence of the original MCES algorithm."
             Experiments (§7, pp. 8–9): the multi-update variant learns faster than the start-pair-only variant on blackjack and on stochastic cliff walking.
Locators:    pages as printed in arXiv v2
Quote:       p. 2: "However, our proofs require restrictions on the dynamics of the underlying MDP. Specifically, we require that under the optimal policy, a state is never revisited."
```

### Delattre and Fournier, "Markov decision processes: on the convergence of the Monte-Carlo first visit algorithm", SIAM J. Control Optim. 64(3):1672–1697 (2026)

```text
URL:         https://doi.org/10.1137/25M1726200 (gated; published 3 June 2026 per Crossref). Read: arXiv:2501.08800v2, 22 Sep 2025, https://arxiv.org/abs/2501.08800
Kind:        primary. Sylvain Delattre and Nicolas Fournier (Laboratoire de Probabilités, Statistique et Modélisation, Université Paris Cité and Sorbonne Université, CNRS) prove their own theorems.
Establishes: firsthand: the first convergence proof for first-visit Monte Carlo control with no structural condition on the MDP, valid only for γ < 1/2.
Paraphrase:  Setting: finite MDP, γ ∈ [0, 1), possibly random rewards.
             Algorithm 1 (pp. 5–6) is a general family. It covers an initial (state, action) law ν_k that may depend on the past, an exploration rate ε_k(x) that may be 0 (pure greedy, ties split uniformly), first-visit returns, and learning rates α_k(x, a) ∈ [0, 1].
             Theorem 3, p. 6: if γ < 1/2, ε_k → 0, Σα_k 1{visited} = ∞ and Σα_k² 1{visited} < ∞ a.s., then V_{π̂k} → V* a.s.
             Proposition 4, p. 6: for γ ∈ (1/2, 1), a one-state, two-action MDP admits parameters of Algorithm 1 under which the value fails to converge a.s. The authors say this counterexample "is far from concerning the FVA: it only shows that our proof breaks down".
             Theorem 5, p. 7: the classical first-visit algorithm, with sample averages, ε_k(x) = (1+N_k(x))^(−θ), θ ∈ (0, 1], and every start state having positive probability, converges for γ < 1/2. "We believe that the condition γ < 1/2 is not necessary."
             §2.5 and §7, from p. 8: finite episodes with an absorbing zero-reward terminal set reachable from every state.
             p. 2: "it seems that the present paper provides the first convergence proof of the FVA without assuming any structural condition on the underlying MDP. However, only half the way is done".
Locators:    arXiv v2 page and result numbers. The journal version's numbering was not checked.
```

Researcher's reading, not stated by the authors: Theorem 3's hypotheses include S&B's MC ES, which is first-visit with sample averages, greedy (ε_k = 0), and exploring starts with every pair's probability bounded below. Such starts give infinitely many visits, so the step-size sums hold. The paper's own named corollary (Theorem 5) uses decaying ε-greedy exploration from random start states, not exploring starts.

### Oliviers and Vinnicombe, "Exploring Starts Are Not Enough: Counterexamples and a Fix for Monte Carlo Exploring Starts" (arXiv:2606.15247v1, 13 June 2026, preprint)

```text
URL:         https://arxiv.org/abs/2606.15247
Kind:        primary for its own constructions and simulations. Octave Oliviers and Glenn Vinnicombe (Department of Engineering, University of Cambridge). Marked "Preprint"; no peer review found.
Establishes: firsthand: a proved fix for the initial-visit variant, plus counterexample evidence. Their summaries of earlier work are secondhand.
Paraphrase:  Notation: IV = update only the start pair; FV = first-visit; SA = sample-average step 1/n_k(s, a). "Strict exploring starts" means every pair's start probability ≥ σ_min > 0 at every episode. The start distribution σ_k may depend on the current estimates.
             §1.1, p. 2: with starts uniform over all pairs and scalar steps, IV converges a.s. (Tsitsiklis, Chen, Liu). Earlier IV counterexamples bias starts toward non-greedy actions.
             §2, pp. 3–5: a three-state MDP with γ = 0.9, termination probability 0.1 per action, and a start strategy that depends on the current q, mixed 0.9/0.1 with uniform starts. IV/SA converges to a suboptimal boundary point (q(s, a*) = q(s, ā) ≈ 1.615) in 99.6% of runs from a stated initialization. This happens even though the greedy action is sampled at least as often as any other in each state.
             §3, Theorem 1, p. 6: IV with step α_k / g_k(a|s), where g_k is the within-state start-action probability, converges a.s. to q*. Conditions: discounted, or every episode reaches a terminal state a.s.; random tie-breaking; strict exploring starts; scalar non-increasing Robbins–Monro α_k satisfying a comparability condition. The proof is adapted from Proposition 20 of the companion paper.
             §4, pp. 8–9: a 13-state cyclic MDP (γ = 0.9999, τ ≈ 0.5123, ε_ES = 10^−4) with starts that depend on the current q. The noise-free mean-field version of FV/SA provably spirals into a suboptimal boundary point (App. C). In 40,000 sampled runs of 10^9 steps, all but about (2200/M)^5.4 stayed trapped (M = 3000–12000, the initial count). Continued runs to 10^12 steps did not escape.
             §5, p. 9: "In our simulations this occurs with sharply decreasing frequency for later starts, providing strong evidence that exploring starts alone do not guarantee convergence of Monte Carlo control methods to optimality."
Locators:    sections and pages of v1 as given
Quote:       p. 3: "Thus any convergence proof for FV/SA MCES would need to show that the stochastic sampled paths always escape the mean-field attractors. Our simulations suggest that this does not happen." (The FV/SA result is strong numerical evidence for a sampled process, not a theorem about it.)
```

### Oliviers and Vinnicombe, "Convergence of Monte Carlo Optimistic Policy Iteration: Beyond Uniform State-Action Updates" (arXiv:2606.10580v1, 9 June 2026, preprint)

```text
URL:         https://arxiv.org/abs/2606.10580
Kind:        primary for its theorem. Same authors as above, preprint.
Establishes: firsthand: IV convergence when starts are uniform over the actions within each state.
Paraphrase:  Proposition 20: initial-visit MC optimistic policy iteration converges a.s. to q* when start actions are uniform within each state, while states may be started at arbitrary frequencies. Conditions: discounted or all-terminating episodic MDP, Robbins–Monro and comparability step sizes, random tie-breaking, strict exploring starts. The proof tracks the policy sequence, not the estimates.
             §1, p. 2 surveys known conditions: feedforward structure (Wang et al. 2022; Lubars et al. 2021), γ < 1/2 (Delattre & Fournier), uniform updates (Tsitsiklis; Chen; Liu).
             §4.1: "requiring uniform update distributions effectively forces the use of initial-visit updates". In a two-state example with γ = 0.5, IV sometimes settles on π* as fast as or faster than FV, because FV shows a "sliding mode" near decision boundaries.
             §2.2.2: they exclude every-visit because its estimates can be biased (Singh & Sutton 1996, Thm 7).
Locators:    §1 p. 2; §2.2.2; Assumption 2; Proposition 20; §4.1
```

### Chen, "Scalar-Stepsize Nonuniform Monte Carlo Optimistic Policy Iteration: A Certified Counterexample" (arXiv:2606.15978v1, 14 June 2026, preprint)

```text
URL:         https://arxiv.org/abs/2606.15978
Kind:        primary for its construction. Yuanlong Chen (affiliation not recorded).
Establishes: firsthand: a negative answer to one of Tsitsiklis's 2002 open cases.
Paraphrase:  The setting is Tsitsiklis's state-value recursion (greedy through the model), discounted, with fixed nonuniform state-selection probabilities and a common scalar Robbins–Monro step. In a three-state, two-action MDP, the iteration stays trapped near an attracting cycle with positive probability and so fails to converge (Theorem 1). It is not the q-based, sample-average box algorithm.
Locators:    abstract; Theorem 1
```

### Winnicki and Srikant, "On The Convergence Of Policy Iteration-Based Reinforcement Learning With Monte Carlo Policy Evaluation", AISTATS 2023

```text
URL:         https://arxiv.org/abs/2301.09709
Kind:        primary for its theorem. Anna Winnicki and R. Srikant (University of Illinois Urbana-Champaign).
Establishes: firsthand: convergence of a first-visit, single-trajectory scheme in which improvement uses H-step lookahead instead of one-step greedy.
Paraphrase:  The abstract presents "a solution to the open problem". The improvement step is μ_{k+1} = argmin T_μ T^{H−1} V_k (§2–3, Algorithm 1). That step applies the Bellman operator with the transition model, or uses tree search over a simulator when the model is unknown (§1.2). It is in state values with discount α ∈ (0, 1). The paper calls Tsitsiklis's setting "a hybrid of Monte Carlo sampling using a single trajectory and a generative model" (§1.1).
Locators:    abstract; §1.1; §1.2; §2 (lookahead definition); Algorithm 1
```

### Lubars, Winnicki, Livesay, Srikant, "Optimistic Policy Iteration for MDPs with Acyclic Transient State Structure" (arXiv:2102.00030, 2021)

```text
URL:         https://arxiv.org/abs/2102.00030
Kind:        primary for its theorem. Read at abstract level only.
Establishes: that the "update every visited state" variant suggested by Tsitsiklis converges when every stationary policy induces the same Markov-chain graph and that graph is acyclic once recurrent classes are collapsed.
Paraphrase:  as above. The grid fails the "same graph for every policy" condition, because each move direction gives a different set of successors.
Locators:    abstract
```

### This course's published lessons (via `./nb history --show reinforcement-learning/<slug>`)

```text
URL:         reinforcement-learning/environments-and-the-rl-problem; reinforcement-learning/finding-optimal-policies; reinforcement-learning/learning-values-from-samples
Kind:        primary for the grid, code and earlier results the lesson reuses (the course's own published work).
Establishes: grid rules, the optimal policy and ties, and the form in which lesson 2 proved the improvement theorem.
Paraphrase:  Lesson 1 (gridworld.py): 16 cells, goal 3 (+10 on arrival), pit 6 (−20), other arrivals −1. Slip 0.2 means 0.8 intended and 0.1 to each perpendicular side; "a move into an edge leaves the agent where it is". episode() loops `while s not in TERMINAL` with no step cap. STUCK presses the bottom row into the bottom wall, and "no episode that enters the bottom row ever leaves it".
             Lesson 2: q_π(s, a) = Σ P(s′|s, a)[R(s′) + γ v_π(s′)]. The theorem is stated and proved with hypothesis q_π(s, π′(s)) ≥ v_π(s), via the expansion chain. π* arrows are "> > > . / ^ ^ . ^ / ^ ^ > ^ / ^ > > ^". Ties are broken by Howard's keep-current rule.
             Lesson 3: estimators.py (first_visit_mc, every_visit_mc, td0) imports nothing from the environment.
Locators:    lesson 1 gridworld.py listing and "Moves slip" paragraph; lesson 1 Fig. 7 paragraph (STUCK); lesson 2 policy improvement theorem section, printed output ("pi_*", "ties at v_*"), problem 2; lesson 3 estimators.py
```

### Researcher's check: lesson 1's grid is not OPFF (throwaway; rerun to verify)

```text
URL:         n/a (computation, reproduced below)
Kind:        primary (own computation from lesson 1's printed dynamics)
Establishes: the grid falls outside Wang et al.'s theorem. v*(13) matches lesson 2.
Paraphrase:  Value iteration at slip 0.2 and γ = 0.9 gives v*(13) = −0.7142, matching lesson 2. Optimal action sets: cells 9 and 12 each have {up, right}; every other non-terminal cell has one optimal move. Self-loops occur under optimal actions at cells 0, 1, 2, 4, 7, 8, 11, 12, 13, 14 and 15, and there are longer cycles, e.g. 1→5→1 and 8→9→8. Cell 2's only optimal move is right, which slips up into the edge with probability 0.1, so every optimal policy can revisit cell 2. The grid is not OPFF.
```

```python
# uv run --with numpy python -I opff.py   (re-implements lesson 1's transitions())
import numpy as np
N=16; T=[3,6]; S=[(-1,0),(0,1),(1,0),(0,-1)]; R=np.full(N,-1.); R[3],R[6]=10.,-20.
def mv(s,a):
    r,c=s//4+S[a][0], s%4+S[a][1]; return 4*r+c if 0<=r<4 and 0<=c<4 else s
P=np.zeros((N,4,N))
for s in set(range(N))-set(T):
    for a in range(4):
        P[s,a,mv(s,a)]+=.8; P[s,a,mv(s,(a+1)%4)]+=.1; P[s,a,mv(s,(a+3)%4)]+=.1
v=np.zeros(N)
for _ in range(2000):
    q=(P*(R+.9*v)).sum(2); v=q.max(1); v[T]=0
opt={s:[a for a in range(4) if q[s,a]>=q[s].max()-1e-9] for s in range(N) if s not in T}
print(round(v[13],4), opt[9], opt[12])                       # -0.7142 [0, 1] [0, 1]
print([s for s,A in opt.items() if any(P[s,a,s]>0 for a in A)])  # self-loops under optimal moves
```

## Contradictions

**Is MC ES convergence open or settled? It depends on which algorithm and which MDP class.** For the writer, here is each case with its source:

| Variant | MDP class | Status | Source |
|---|---|---|---|
| Full evaluation (infinite episodes) before each greedy step, exploring starts | finite | converges (Monte Carlo policy iteration) | S&B p. 98 |
| Start pair only; starts uniform over all pairs (or synchronous); scalar Robbins–Monro step | finite, discounted (γ < 1) | proved w.p. 1 (synchronous: Prop. 1, and Prop. 5 for Q; one uniform random start per episode: argued in text) | Tsitsiklis 2002 pp. 63, 65–66, 71 |
| Same | undiscounted, all policies proper (relaxable) | proved | Liu 2021 Thm 10, Prop. 14; Chen 2018 per Liu |
| Start pair only; fixed nonuniform starts; sample-average step 1/n | discounted / proper SSP | proved | Tsitsiklis 2002 p. 66; Liu 2021 Prop. 16 |
| Start pair only; start actions uniform within each state, states at any frequency | discounted or all-terminating | proved (preprint) | Oliviers & Vinnicombe 2606.10580 Prop. 20 |
| Start pair only; fixed nonuniform starts; common scalar step | discounted, state-value form | fails w.p. > 0 (preprint, certified) | Chen 2606.15978 |
| Start pair only; start choice depends on current estimates (still exploring) | episodic or continuing | can fail | B&T 1996 Ex. 5.12 (cited); Wang et al. App. F; Oliviers & Vinnicombe 2606.15247 §2 |
| S&B box: first-visit, sample averages, update every visited pair | OPFF (incl. SFF, deterministic terminating), any γ ≤ 1 | proved (with step cap M and −∞ init for OPFF) | Wang et al. 2022 Thm 1–2 |
| Same | any finite MDP, γ < 1/2 | proved | Delattre & Fournier 2026 Thm 3 (and Thm 5 for ε-greedy) |
| Same, start choice depends on current estimates | a 13-state non-OPFF MDP, γ = 0.9999 | numerical evidence of trapping; mean-field proof only (preprint) | Oliviers & Vinnicombe 2606.15247 §4 |
| Same, fixed start distribution (e.g. uniform), as on this grid | non-OPFF, γ ≥ 1/2 | **no proof, no counterexample: open** | gap across all sources above |
| First-visit with H-step model-based lookahead in place of greedy | discounted | proved | Winnicki & Srikant 2023 |

- **"Settled" vs "open".** Tsitsiklis (p. 60, p. 72) says he "settle[d]" Sutton's problem. S&B (p. 99) call his result "a partial solution" and still list the question as open. Both are accurate under their own definition of the algorithm. Tsitsiklis changes the algorithm to update start pairs only, at uniform frequency. S&B's box updates every first-visited pair.
- **"MCES does not necessarily converge" (Wang et al. abstract).** This rests on Bertsekas & Tsitsiklis's Example 5.12. Tsitsiklis (p. 67) and Wang et al. (p. 3) describe that example as using arbitrarily chosen start states in a continuing task. Delattre & Fournier say their analogous counterexample "is far from concerning the FVA". One counterexample uses a fixed start distribution: Chen 2606.15978, with fixed nonuniform state selection. It also uses a common scalar step instead of sample averages, updates only the start state, and is in model-based state-value form. Every other counterexample I found chooses starts adaptively or arbitrarily. None applies to the box algorithm with fixed uniform starts.
- **"This largely settles a fundamental open problem" (Oliviers & Vinnicombe abstract).** Their first-visit result is a mean-field proof plus simulations. Their own text (p. 3, §5) calls it "strong evidence", and it uses q-dependent starts. Their initial-visit counterexample is fully constructed but also uses q-dependent starts.
- **Winnicki & Srikant's "solution to the open problem"** replaces greedy improvement with H-step lookahead through the Bellman operator (T^{H−1}), which needs the model or a simulator tree search. It does not cover model-free greedy MC ES.
- **Against the commission's angle.** The commission says interleaving "still reaches the optimal policy on this grid". No theorem guarantees this for the box algorithm on this grid: it is non-OPFF (Researcher's check) and γ = 0.9 > 1/2. S&B's own GPI text says "typically" (p. 86), and their p. 98 guarantee covers only complete evaluation with infinitely many episodes. Runs can show it on this grid. The page cannot present it as a property GPI guarantees. Fixed uniform exploring starts fall outside the construction of every published counterexample, but that observation about the constructions is not a theorem.
- **Episodes that never end.** S&B chapter 5 assumes episodes terminate "no matter what actions are selected" (p. 91). Lesson 1's grid violates this: STUCK never leaves the bottom row (lesson 1, Fig. 7 paragraph), and lesson 1's episode() has no cap. A greedy policy formed mid-training can contain such a loop. Wang et al.'s Algorithm 2 (p. 7) cuts episodes at M steps and discards them. Tsitsiklis §6 (p. 71) truncates at a horizon T with α^T near zero. The lesson's code needs one of these.
- **Ties at the optimum.** Lesson 2's output shows exact ties at cells 9 (−1.0142) and 12 (−1.7347). As the Q estimates converge, argmax at those cells can flip indefinitely between two optimal moves. Wang et al. assume a unique optimal policy for simplicity and say the proof extends (pp. 6–7). Oliviers & Vinnicombe assume random tie-breaking. A test of "the greedy policy matches the optimal one" has to accept either optimal move at cells 9 and 12.
- **Minor citation discrepancy.** Liu (§6) adapts his two-state example from "Bertsekas & Tsitsiklis, 1996, Example 5.11". Tsitsiklis, Wang et al. and Oliviers & Vinnicombe cite the counterexample as Example 5.12 (Tsitsiklis: pp. 234–236). I could not check the book.

## Numbers

```text
Figure: printed page = PDF page − 22 in RLbook2020.pdf (MC ES box: printed p. 99 = PDF p. 121)
Owner:  Sutton & Barto, 2nd ed. (2020 PDF)
Scope:  whole book PDF, 548 pages
```

```text
Figure: S&B locations: ch. 5 intro p. 91; §5.2 pp. 96–97; §5.3 pp. 97–99; eq. (5.1) p. 97; q-form chain p. 98; MC ES box p. 99; convergence statement p. 99; Example 5.3/Fig. 5.2 pp. 99–100; §5.4 p. 100; §4.2 pp. 76–80 ((4.6)–(4.8) p. 78, (4.9) p. 79); §4.6 pp. 86–87; remark 5.3–4 p. 117
Owner:  Sutton & Barto, 2nd ed.
Scope:  printed page numbers
```

```text
Figure: γ < 1/2 (discount factor threshold for the first-visit proof)
Owner:  Delattre & Fournier 2026, Theorems 3 and 5
Scope:  any finite MDP; the proof method fails for γ > 1/2 (Prop. 4)
```

```text
Figure: γ = 0.9, slip 0.2 (0.8 / 0.1 / 0.1), goal +10, pit −20, other arrivals −1
Owner:  lesson 1 (gridworld.py)
Scope:  this course's grid
```

```text
Figure: v*(13) = −0.7142; ties: cell 9 up = right = −1.0142, cell 12 up = right = −1.7347
Owner:  lesson 2 printed output (reproduced by Researcher's check)
Scope:  slip 0.2, γ = 0.9
```

```text
Figure: 99.6% of runs converge to a suboptimal boundary point (q ≈ 1.615); 0.4% escape to q_π*
Owner:  Oliviers & Vinnicombe 2606.15247, §2 (Fig. 2)
Scope:  their 3-state MDP, γ = 0.9, IV/SA, q-dependent starts with 0.1 uniform mixing, one stated initialization
```

```text
Figure: 40,000 runs × 10^9 steps; escape fraction ≈ (2200/M)^5.4 for M = 3000–12000; none of a continued sample escaped by 10^12 steps
Owner:  Oliviers & Vinnicombe 2606.15247, §4
Scope:  13-state cyclic MDP, γ = 0.9999, τ ≈ 0.5123, ε_ES = 10^−4, FV/SA, q-dependent starts
```

```text
Figure: Wang et al. App. F counterexample holds for 0.7 < γ < 1 with termination probability ε = (1 − γ)/10
Owner:  Wang et al. 2022, Remark 4 and Theorem 6 (App. F)
Scope:  2 states + terminal, IV variant, scheduled starts
```

## Limits

- I could not open Bertsekas & Tsitsiklis, Neuro-Dynamic Programming (1996), Example 5.12 (pp. 234–236). Its content is known only through Tsitsiklis 2002 (p. 67), Wang et al. (pp. 2–3, 26) and Oliviers & Vinnicombe (App. A). The 5.11/5.12 numbering discrepancy is unresolved.
- I read Winnicki & Srikant, "Convergence of Monte Carlo Exploring Starts with TD-Learning", IEEE CDC 2024 (DOI 10.1109/CDC56724.2024.10886885), by title only. IEEE returned no page text, Crossref carries no abstract, and I found no arXiv copy. It may add a case to the status table.
- I read Chen 2018 (arXiv:1808.08763) and Lubars et al. 2021 at abstract level only. Their conditions are recorded from their abstracts and from Liu's and Wang et al.'s descriptions.
- For the Delattre & Fournier journal version, I read only the arXiv v2 (22 Sep 2025). I confirmed the journal, volume, issue, pages and date through Crossref. Its result numbering may differ.
- The claim that Delattre & Fournier's Theorem 3 covers S&B's exploring-starts box for γ < 1/2 is my reading of the theorem's hypotheses. The authors do not state it.
- No source establishes that MC ES converges on this grid (non-OPFF, γ = 0.9) with uniform exploring starts. No source shows that it fails there either. The lesson's claim for this grid has to come from its own runs.
- Both 2026 Cambridge papers and Chen 2026 are v1 arXiv preprints, and I found no peer review for them.

## Source assets

```text
Asset: Monte Carlo ES box, S&B 2nd ed. p. 99 (PDF p. 121), the boxed pseudocode titled "Monte Carlo ES (Exploring Starts), for estimating π ≈ π*"
Shows: the exact algorithm the convergence question is about: random start pair, first-visit check, average of returns, greedy update at each visited state
Crop:  keep the whole box including its title and the "Unless the pair St, At appears in ..." line; omit Exercise 5.4 and the text below
```

```text
Asset: GPI diagram for action values, S&B p. 97 (right margin of §5.3: Q ⇄ q_π evaluation arrow, π ⇄ greedy(Q) improvement arrow); state-value version p. 86; two-line convergence sketch p. 87
Shows: evaluation and improvement as two processes pulling toward a joint fixed point π*, q*
Crop:  keep both arrows and their labels; the p. 87 sketch must keep the two labelled lines and the point v*, π*
```

```text
Asset: Wang et al. 2022, Figure 3, p. 9 (four-region summary: algorithm class × OPFF / non-OPFF)
Shows: what was proved about MCES as of 2022 and where counterexamples lie
Crop:  keep the caption. Out of date as a "current status" picture: it predates Delattre & Fournier (first-visit, γ < 1/2, all MDPs) and the 2026 preprints. Do not present it as current without saying so.
```

```text
Asset: S&B Figure 5.2, p. 100 (blackjack optimal policy and value found by MC ES)
Shows: MC ES producing an optimal policy on blackjack, an MDP that Wang et al. (pp. 4–5) classify as SFF, where convergence is now proved
Crop:  keep both policy panels and the axes labels; optional for a Why-this-matters case
```

Tsitsiklis 2002, Liu 2021, Delattre & Fournier, Winnicki & Srikant, Sutton 1999: none found that would carry the argument better than prose. Oliviers & Vinnicombe 2606.15247 Figures 1, 3 and 5 show their counterexample MDPs and trapped trajectories. These are too specialised for this lesson.

## Discarded

```text
https://arxiv.org/abs/2410.02994: Chen, Ross & Youssef 2024 (finite-sample bound, Õ(SAK³ log³(1/δ)) episodes) for a batched, modified MCES on SSP with all policies proper; a rate for a modified algorithm, which does not change the convergence status the page states
https://www.themoonlight.io/en/review/finite-sample-analysis-of-the-monte-carlo-exploring-starts-algorithm-for-reinforcement-learning: third-party summary of the paper above; secondary, not needed
https://www.alphaxiv.org/abs/2606.10580: mirror of the arXiv preprint; read the arXiv copy instead
https://www.researchgate.net/publication/384679813_Finite-Sample_Analysis_of_the_Monte_Carlo_Exploring_Starts_Algorithm_for_Reinforcement_Learning: mirror of arXiv:2410.02994
```
