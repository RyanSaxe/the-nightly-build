# Evidence: reinforcement-learning/epsilon-greedy-exploration (researcher 01)

The sources fully support the lesson's definitions and its improvement argument. Sutton and Barto define the greedy action and ε-greedy selection in Section 2.2 (pp. 27-28). They define ε-soft policies and on-policy first-visit Monte Carlo control in Section 5.4 (pp. 100-101). They also prove, through equation (5.2) and the "moved inside the environment" construction (pp. 101-102), two results. An ε-greedy step on q_π never makes an ε-soft policy worse, and the step stops changing values only at a policy that is optimal among ε-soft policies.

The sources do not support the commission's word "converges" for the Monte Carlo algorithm itself. Sutton and Barto's argument covers policy iteration with exact action values: "it does assume that they are computed exactly" (p. 103). No primary source I found proves that the sampled, update-after-every-episode algorithm in their box reaches the best ε-soft policy, with any ε. The closest proven result is for one-step SARSA, a later lesson's method. Singh, Jaakkola, Littman and Szepesvári (2000, Theorems 2 and 3) prove that with a fixed ε-greedy learning policy it converges to the best ε-greedy policy. The same paper names GLIE and states its two conditions in Section 2.2 (pp. 291-292).

The commission's starting case also runs into the published code. In mc_control.py, a stall without exploring starts leaves the other moves with no average at all. It never produces a wrong average that goes unrevisited. The term "ε-greedy" first appears, among the documents read, in Sutton (1996): "what we call the ε-greedy policy". Watkins (1989) describes a decaying "experiment" probability but does not use the term. The earliest use is not established.

## Sources

```text
URL:         nb history --show reinforcement-learning/<slug> (the course's published lessons; library record, no public address recorded here)
Kind:        primary for what the course has taught and printed; the course owns these lessons and their code.
Establishes: firsthand, the terms, code files, environment and printed results this lesson may reuse.
Paraphrase:  Four lessons are published.
             - environments-and-the-rl-problem (2026-10-31): the slippery 4x4 grid. Cells are numbered 0-15 row by row. The goal is cell 3 (+10 on arrival), the pit is cell 6 (-20), and every other arrival pays -1. A move goes as aimed with probability 0.8 and to each perpendicular side with 0.1, and γ = 0.9. The lesson covers the MDP, the return, v_π, and the Bellman expectation equation. Code: gridworld.py (N=16, GOAL=3, PIT=6, TERMINAL, ARROWS "^>v<" for moves 0-3, R, draw(), the hand-written policy PI, STUCK, move(), transitions(slip), fixed_policy(), episode(), discounted(), radius()) and evaluate.py.
             - finding-optimal-policies (2026-11-01): action values as one backup from v_π, the greedy step, the policy improvement theorem, policy iteration, value iteration, the Bellman optimality equation, and Howard's tie rule. At the optimum, cells 9 and 12 tie between up and right. Code: control.py (GAMMA=0.9, SLIP=0.2, LIVE, evaluate(policy), action_values(v, P), greedy(v, P, old, tol), policy_iteration, value_iteration, show).
             - learning-values-from-samples (2026-11-02): first-visit and every-visit Monte Carlo prediction, TD(0), bias and variance, and the two step-size conditions (the sum of the steps is infinite and the sum of their squares is finite). It also introduces "exploration" informally, as a policy that "sometimes tries moves other than its current favorite". Code: estimators.py (GAMMA=0.9; first_visit_mc(steps, V, count, step=None), which averages with 1/count by default; every_visit_mc; td0) and compare.py.
             - action-values-from-samples (2026-11-03): estimating q_π by averaging returns per (cell, move) pair, the model-free greedy step, generalized policy iteration (GPI), exploring starts (uniform over the 56 pairs), and Monte Carlo ES. It also covers the half-proof that only the optimal policy can be a resting point, and states that no theorem covers MC ES on this grid. In its exploring-starts section it defers this lesson's topic: "The usual alternative, a policy that keeps some chance on every move, needs a lesson of its own." Code: mc_control.py (SLIP=0.2, LIVE, CAP=200; step(s, a, rng); play(policy, start, first, rng); pairs(steps), which numbers pairs as 4 × cell + move; greedy(q, count, policy); control(policy, episodes, rng, explore=True, every=1, forget=False, watch=None)) and experiment.py (PI_STAR, Q_STAR, BEST, and runs over seeds 0-19).
             mc_control.py details that bear on this lesson:
             - play() follows policy[s_next], one move per cell, after the opening move. It therefore cannot run a stochastic (ε-soft) policy unchanged.
             - greedy() treats a move with no returns as -inf, and a cell with no returns keeps its move.
             - With explore=False, every episode opens with the policy's own move. Every pair that receives a return is therefore the policy's own, and the greedy step returns the same policy. The lesson states this: "Every average then belongs to a move the policy already takes, so each greedy step returns the policy it started from."
Locators:    action-values-from-samples: section "Exploring starts give every move returns of its own"; the mc_control.py listing; the experiment.py output. The other lessons: their code listings.
Quote:       "no exploring starts, optimal runs at 10,000: 0" (experiment.py output, action-values-from-samples)
```

```text
URL:         http://incompleteideas.net/book/the-book-2nd.html (book page). Full text: http://incompleteideas.net/book/RLbook2020.pdf (authors' PDF, © 2018, 2020, MIT Press; PDF page = printed page + 22)
Kind:        primary for its definitions, the algorithm box and the ε-soft improvement argument, which the authors make. Secondary for the history in its Bibliographical and Historical Remarks, which report other people's work.
Establishes: firsthand, the definitions of greedy, ε-greedy and ε-soft, the on-policy first-visit MC control algorithm, and the proof that ε-greedy improvement is monotone with a fixed point at the best ε-soft policy (under exact evaluation). It only repeats the claim about Watkins's priority.
Paraphrase:  Richard S. Sutton and Andrew G. Barto, Reinforcement Learning: An Introduction, second edition.
             - Greedy and exploration (2.1, p. 26). The actions with the greatest estimated value are the greedy actions. Selecting one is exploiting, and selecting a nongreedy action is exploring.
             - Sample averages and greedy selection (2.2, p. 27). Eq. (2.1) estimates Q_t(a) as a sample average. Eq. (2.2) is greedy selection, A_t = argmax_a Q_t(a), with ties broken arbitrarily.
             - ε-greedy (2.2, pp. 27-28). With small probability ε the agent picks uniformly among all the actions, the greedy one included. In the limit every action is sampled infinitely often. The book calls these "just asymptotic guarantees".
             - Greedy stalling in the bandit (2.3, pp. 29-30, Figure 2.2). On the 10-armed testbed, greedy selection with sample averages starting at 0 "often got stuck performing suboptimal actions". It found the optimal action in about one-third of tasks, and in the other two-thirds "its initial samples of the optimal action were disappointing, and it never returned to it". ε = 0.1 found the optimal action sooner but "never selected that action more than 91% of the time".
             - Why action values need exploration (5.2, p. 96). Following a deterministic policy observes returns for only one action per state, and "With no returns to average, the Monte Carlo estimates of the other actions will not improve with experience." The section then defines exploring starts and names the usual alternative: stochastic policies with nonzero probability on every action (pp. 96-97).
             - MC ES convergence (5.3, p. 99). Convergence of MC ES to the optimal policy "has not yet been formally proved", which the book calls "one of the most fundamental open theoretical questions in reinforcement learning". The previous lesson already uses this.
             - On-policy definitions (5.4, p. 100). On-policy methods evaluate or improve the policy that makes the decisions. A soft policy has π(a|s) > 0 everywhere. Under ε-greedy, each nongreedy action gets ε/|A(s)| and the greedy action gets 1 - ε + ε/|A(s)|. An ε-soft policy has π(a|s) ≥ ε/|A(s)| for all s and a, for some ε > 0. "Among ε-soft policies, ε-greedy policies are in some sense those that are closest to greedy."
             - The algorithm (5.4, p. 101). GPI requires only that the policy move toward greedy, so the policy is moved to ε-greedy. The box "On-policy first-visit MC control (for ε-soft policies), estimates π ≈ π*" lists:
               - Parameter: small ε > 0.
               - Initialization: an arbitrary ε-soft π, arbitrary Q(s, a), and an empty list Returns(s, a) for every pair.
               - Each episode: generate it following π, then loop backward with G ← γG + R_{t+1}.
               - At the first visit of each pair: append G, set Q to the average, set A* = argmax_a Q(S_t, a) (ties arbitrary), and set π(·|S_t) to ε-greedy around A*.
             - Monotone improvement (5.4, pp. 101-102). Eq. (5.2) shows that for ε-greedy π' on q_π and any ε-soft π, q_π(s, π'(s)) ≥ v_π(s). The inequality holds because (π(a|s) - ε/|A(s)|)/(1 - ε) are nonnegative weights summing to 1, and a weighted average is at most the maximum. By the policy improvement theorem ((4.7)-(4.8), Section 4.2, p. 78), π' ≥ π.
             - Fixed point (5.4, p. 102). Equality forces optimality among ε-soft policies. In a new environment, with probability 1 - ε the action is the chosen one, and with probability ε the environment repicks it uniformly at random. The best general policy there equals the best ε-soft policy in the original environment. Its optimal value ṽ* uniquely solves the Bellman optimality equation (3.19, p. 63) with these altered transitions (an unnumbered display). A policy that is no longer improved satisfies the same equation, so v_π = ṽ*.
             - Scope of the argument (5.4, pp. 102-103). It shows "policy iteration works for ε-soft policies", is "independent of how the action-value functions are determined", and "does assume that they are computed exactly". The cost: "Now we only achieve the best policy among the ε-soft policies."
             - The compromise (5.5, p. 103). The on-policy approach "learns action values not for the optimal policy, but for a near-optimal policy that still explores."
             - Sarsa (6.4, p. 129). Sarsa converges w.p.1 to an optimal policy under the step-size conditions (2.7) if all pairs are visited infinitely often and the policy converges in the limit to greedy, "for example, with ε-greedy policies by setting ε = 1/t". Remarks 6.4 (p. 139) credit the proof for one-step tabular Sarsa to Singh, Jaakkola, Littman and Szepesvári (2000).
             - Cliff Walking (Example 6.6, p. 132). With ε = 0.1, Sarsa learns "the longer but safer path", and Q-learning learns the optimal path but falls off the cliff during ε-greedy play.
             - History (Remarks 2.2, p. 44). "The first to use ε-greedy methods may also have been Watkins (1989, p. 187), but the idea is so simple that some earlier use seems likely."
Locators:    printed pp. 26, 27 (eqs. 2.1, 2.2), 27-28 (ε-greedy definition), 28 (Exercise 2.1), 29-30 (Section 2.3, Figure 2.2), 44 (Remarks 2.2), 63 (eq. 3.19), 78 (eqs. 4.7, 4.8), 96-97 (Section 5.2), 99 (Section 5.3, MC ES open question), 100 (Section 5.4 opens below Figure 5.2), 101 (box; eq. 5.2 begins), 102 (eq. 5.2 ends; the environment construction; unnumbered ṽ* displays), 103 (closing paragraph of 5.4; opening of 5.5), 129 (Section 6.4), 132 (Example 6.6), 139 (Remarks 6.4).
Quote:       "This analysis is independent of how the action-value functions are determined at each stage, but it does assume that they are computed exactly." (pp. 102-103; the exact wording sets what the textbook proves)
             "A simple alternative is to behave greedily most of the time, but every once in a while, say with small probability ε, instead select randomly from among all the actions with equal probability, independently of the action-value estimates. We call methods using this near-greedy action selection rule ε-greedy methods." (pp. 27-28; definition to cite)
```

```text
URL:         https://doi.org/10.1023/A:1007678930559 (Springer, gated; resolves to https://link.springer.com/article/10.1023/A:1007678930559). Free copy on Szepesvári's site: https://sites.ualberta.ca/~szepesva/papers/singh98convergence.pdf (22 pages, carries the journal pagination 287-308)
Kind:        primary; the authors state and prove the GLIE and fixed-exploration results.
Establishes: firsthand, the GLIE definition and label, the convergence of SARSA(0) under GLIE, the convergence of SARSA(0) with a fixed rank-based learning policy (fixed ε-greedy included) to the best policy of that class, and an ε-greedy schedule that is provably GLIE.
Paraphrase:  Satinder Singh (AT&T Labs-Research), Tommi Jaakkola (Department of Computer Science, Massachusetts Institute of Technology), Michael L. Littman (Department of Computer Science, Duke University) and Csaba Szepesvári (Mindmaker Ltd., Budapest), "Convergence Results for Single-Step On-Policy Reinforcement-Learning Algorithms", Machine Learning, 2000, pp. 287-308. Crossref gives vol. 38, issue 3, March 2000. The free copy's header prints "39".
             - Figure 1 (p. 288). A 3-state deterministic MDP with γ = 0.9. Without exploration, r is optimal from state y. With 50% exploratory actions, l is best from y, because exploration sometimes takes the costly r at state z.
             - Greedy learning (2.1, p. 291). With a greedy learning policy, SARSA(0) and Q-learning coincide and "would not converge to optimal solutions, in general, because the need for infinite exploration would not be satisfied."
             - Learning policies (2.2, pp. 291-292). A decaying-exploration policy gives up adaptivity to approach optimal behavior. A persistent-exploration policy "will not converge to optimality in the standard sense".
             - GLIE (2.2, pp. 291-292). GLIE is defined by two conditions: (1) every action is executed infinitely often in every state that is visited infinitely often; (2) in the limit the learning policy is greedy with respect to the Q-value function with probability 1. "We label learning policies satisfying the above conditions as GLIE, which stands for 'greedy in the limit with infinite exploration.'" They attribute ε-greedy exploration to Sutton (1996). They show that ε_t(s) = c/n_t(s), with 0 < c < 1 and n_t(s) the number of visits to s, makes ε-greedy GLIE (proof in Appendix B.2, p. 304).
             - RRR policies (2.2, p. 292). Fixed ε-greedy is a "restricted rank-based randomized" (RRR) policy with T(1) = 1 - ε + ε/m and T(i) = ε/m.
             - Theorem 1 (3.1, p. 294). In a finite MDP, SARSA(0) with a GLIE learning policy, a lookup table, Robbins-Monro step sizes and finite reward variance converges to Q*, and the learning policy converges to an optimal policy.
             - Theorems 2 and 3 (3.2, pp. 296-300). Theorem 2 (p. 297): SARSA(0) with an RRR learning policy converges to Q̄, the unique fixed point of eq. (7). Theorem 3 (p. 299): the greedy restricted policy for Q̄ is an optimal restricted policy, by an alternate-MDP argument parallel to Sutton and Barto's. Corollary (p. 300): with every T(i) > 0, SARSA(0) converges to an optimal restricted policy.
             - Caveat (p. 300). Because the step sizes decay to zero, "in the limit, the learner is still exploring, but it is not able to learn anything new from its discoveries."
             - Scope (Section 2, pp. 289-290; Conclusion, p. 300). The setting is a discounted MDP (0 ≤ γ < 1) assumed "communicating" (every state reachable from every other). The authors call these "the first convergence results for any on-policy algorithm" and say they "do not seem to extend naturally to general multi-step on-policy algorithms".
Locators:    Figure 1 and text, p. 288; Section 2 (γ < 1 and the communicating assumption), pp. 289-290; Section 2.1, p. 291; Section 2.2 "Learning policies", pp. 291-292 (GLIE conditions at the foot of p. 291, the label at the top of p. 292); Theorem 1, p. 294; Section 3.2, pp. 296-300 (Theorem 2, p. 297; Theorem 3, p. 299; corollary and caveat, p. 300); Conclusion, p. 300; Appendix B.2, p. 304.
Quote:       "We label learning policies satisfying the above conditions as GLIE, which stands for 'greedy in the limit with infinite exploration.'" (p. 292; the naming sentence)
             "For a discount factor of γ = 0.9, the optimal action choice from state y is r (value 75.8 as opposed to 74.9 for action r)." (p. 288; printed as is, the second "r" evidently means l)
```

```text
URL:         https://papers.nips.cc/paper/1995/hash/8f1d43620bc6bb580df6e80b0dc05c48-Abstract.html (proceedings page). Author's PDF: http://incompleteideas.net/papers/sutton-96.pdf
Kind:        primary; the author names the rule in his own paper.
Establishes: firsthand, an early written use of the term "ε-greedy policy" with its definition (uniform random action a fraction ε of the time). It does not establish that this is the first use.
Paraphrase:  Richard S. Sutton (University of Massachusetts, Amherst), "Generalization in Reinforcement Learning: Successful Examples Using Sparse Coarse Coding", Advances in Neural Information Processing Systems 8, pp. 1038-1044, MIT Press, 1996. The paper's Sarsa experiments select actions by "what we call the ε-greedy policy". Most of the time the action has the largest estimate, with ties broken randomly. A fraction ε of the time it is drawn uniformly from the whole action set. Figure 1's algorithm calls ε-greedy-policy(F).
Locators:    Section 1 "Reinforcement Learning and Function Approximation", second page of the paper (proceedings p. 1039), paragraph beginning "The reinforcement learning methods we use"; Figure 1 (algorithm box).
Quote:       "In our experiments, actions were selected according to what we call the ε-greedy policy." (the wording is the evidence for the term's use)
```

```text
URL:         https://www.cs.rhul.ac.uk/~chrisw/new_thesis.pdf
Kind:        primary; the thesis author describes his own agent's action selection.
Establishes: firsthand, a 1989 rule that mixes greedy choice with a state-dependent, decaying probability of "experimenting". It does not use the term "ε-greedy", and its rule differs from ε-greedy.
Paraphrase:  Christopher John Cornish Hellaby Watkins, "Learning from Delayed Rewards", thesis submitted for Ph.D., King's College (Cambridge), May 1989. The copy is a scan with no text layer, and I read the pages as images. In the second demonstration of Chapter 11 (a Skinner-box task with two actions, peck or not peck), the agent takes the higher-valued action with probability 1 - π_t. With probability π_t it "experiments" and takes the lower-valued action. π_t = T/(T + Y_t(x_t)) π_0 shrinks as the occupancy Y of the current region of state space grows (p. 179). This copy's own corrigenda use the same pagination. Its p. 187, the page Sutton and Barto cite, is a plot page ("Plot 3").
Locators:    Chapter 11 "Two Demonstrations", §6 "Behavioural Policy and Occupancy", printed p. 178 (PDF p. 185), continued p. 179 (PDF p. 186). Printed p. 187 is PDF p. 194.
Quote:       "then with probability 1−π_t it chooses the action with higher estimated value, and with probability π_t it 'experiments', and chooses the action with lower estimated value." (p. 178; the wording shows how it differs from ε-greedy)
```

```text
URL:         https://www.davidsilver.uk/teaching/ (course page). Slides: https://davidstarsilver.wordpress.com/wp-content/uploads/2025/04/lecture-5-model-free-control-.pdf
Kind:        secondary for any convergence claim. These are lecture slides that state results without proof or citation. Primary only for what the slides say.
Establishes: that a widely used course states "GLIE Monte-Carlo control converges" as a theorem. It does not establish that a proof exists.
Paraphrase:  David Silver, "Lecture 5: Model-Free Control" (43 slides; the PDF metadata dates it 2015).
             - Slide 11: ε-greedy, with probability ε/m + 1 - ε on the greedy action and ε/m on each other action.
             - Slide 12: the improvement theorem, stated "For any ε-greedy policy π" (Sutton and Barto state it for any ε-soft π).
             - Slide 15: GLIE defined as lim N_k(s, a) = ∞ and the policy converging to greedy. "ε-greedy is GLIE if ε reduces to zero at ε_k = 1/k."
             - Slide 16: "GLIE Monte-Carlo Control". Each episode, every visit gets an incremental 1/N update, then ε ← 1/k and π ← ε-greedy(Q). "Theorem: GLIE Monte-Carlo control converges to the optimal action-value function, Q(s,a) → q*(s,a)". No proof or reference is given.
             - Slide 23: Sarsa converges under GLIE plus Robbins-Monro step sizes.
Locators:    slides 11, 12, 15, 16, 23.
```

```text
URL:         https://arxiv.org/abs/2606.10580
Kind:        primary for its own theorem. Secondary as a survey of what others proved.
Establishes: firsthand, a June 2026 convergence result for Monte Carlo control with deterministic greedy policies. It also gives its authors' summary of the field, which repeats others' results.
Paraphrase:  Octave Oliviers and Glenn Vinnicombe (Department of Engineering, University of Cambridge), "Convergence of Monte Carlo Optimistic Policy Iteration: Beyond Uniform State-Action Updates", arXiv v1, 9 June 2026. They prove that initial-visit MC optimistic policy iteration (greedy deterministic policies, episodes started by an exploring-start distribution) converges when updates are uniform over the actions in each state (Proposition 20). Their introduction (pp. 1-2) lists the conditions known to give convergence: feedforward MDPs (Wang et al. 2022; Lubars et al. 2021), a discount below 1/2 (Delattre and Fournier), or equal update frequency for all pairs (Tsitsiklis 2002; Chen 2018; Liu 2021). It calls the general question "a long-standing open question". The text has no result or discussion about ε-soft or ε-greedy policies; I searched for "soft", "greedy", "epsilon" and "on-policy".
Locators:    Abstract; Section 1, pp. 1-2; Section 4.4, p. 28.
Quote:       "The asymptotic behaviour of Monte Carlo optimistic policy iteration (MC-O-PI) is a long-standing open question." (abstract)
```

## Contradictions

- **"Converges" versus what is proven.** The commission says on-policy MC control "converges to the best epsilon-soft policy". Sutton and Barto prove two things: monotone improvement and a fixed point, for policy iteration with exactly computed action values (pp. 102-103). They make no convergence claim for the sampled per-episode algorithm in their box. The box's own title ("estimates π ≈ π*") is looser than its text, which concludes "best policy among the ε-soft policies" (p. 103). The nearest proven convergence is Singh et al.'s Theorems 2 and 3, for SARSA(0) with decaying step sizes in a communicating discounted MDP. That is a TD method and out of scope. A defensible page states the fixed-point result as proven and the run as evidence. It does not say the algorithm is proven to converge.
- **The starting case versus the published code.** The commission asks for "a (cell, move) pair whose average is wrong and never revisited by the greedy policy" in the run that printed "no exploring starts, optimal runs at 10,000: 0". In that run (control(..., explore=False)), every episode opens with the policy's own move. play() then follows the policy, and greedy() skips moves with no returns. So no non-policy move ever receives a return, and the stall comes from absent averages, not wrong ones. The previous lesson already says so ("Every average then belongs to a move the policy already takes"). A wrong average that is never revisited needs a pair that got at least one return and then lost the argmax. Sutton and Barto's bandit passage (p. 30) describes exactly that mechanism, with estimates starting at 0: "its initial samples of the optimal action were disappointing, and it never returned to it". Sutton and Barto's MC boxes initialize Q "arbitrarily". mc_control.py does not: it leaves untried moves without an estimate.
- **"Not the optimal one."** An ε-soft policy with ε > 0 is stochastic, so it differs from the deterministic π* by definition. The substantive questions are the value gap v* - ṽ* and whether the greedy arrows of the best ε-soft policy differ from π*'s arrows. The sources show that the arrows can differ: in Singh et al. Figure 1 (p. 288), 50% exploration flips the best action at y, and in Sutton and Barto's Cliff Walking (p. 132), ε = 0.1 makes Sarsa take the safer path. On this grid it is a computation for the writer. No source settles it.
- **What "ε-greedy" means.** Sutton and Barto (pp. 27-28, 100), Sutton (1996) and Silver (slide 11) draw the random action from all actions, the greedy one included, so the greedy action gets 1 - ε + ε/|A|. Watkins (1989, p. 178) "experiments" by taking the other, lower-valued action. Singh et al.'s GLIE paragraph (p. 292) and Appendix B.2 phrase it as "a random exploration action with probability ε_t(s) and the greedy action with probability 1 − ε_t(s)". Their RRR form (p. 292) matches Sutton and Barto's.
- **GLIE schedules.** Singh et al. prove only ε_t(s) = c/n_t(s), with 0 < c < 1 and a per-state visit count, to be GLIE (p. 304). Sutton and Barto give "ε = 1/t" as an example (p. 129), and Silver gives ε_k = 1/k per episode (slides 15-16). I found no proof that those two schedules are GLIE in general.
- **GLIE Monte Carlo control.** Silver's slide 16 states "GLIE Monte-Carlo control converges to the optimal action-value function" with no proof or citation. Singh et al., the source that defines GLIE, prove convergence for SARSA(0) (Theorem 1), not for Monte Carlo control. I found no primary proof for the Monte Carlo case. The deterministic-greedy version, MC ES, is itself unproven in general (Sutton and Barto, p. 99; Oliviers and Vinnicombe 2026).
- **The improvement theorem's hypothesis.** Silver (slide 12) states it "For any ε-greedy policy π". Sutton and Barto (p. 101) state it for any ε-soft π, which is the more general statement the lesson needs.
- **Watkins page.** Sutton and Barto cite Watkins 1989 p. 187 (p. 44). In the RHUL copy, p. 187 is a plot. The matching passage is on p. 178.
- **Singh et al. citation details.** The free copy prints "Machine Learning, 39". Crossref and Springer give vol. 38, issue 3. The text on p. 288 says "74.9 for action r" where the context requires l.

## Numbers

```text
Figure: greedy action 1 - ε + ε/|A(s)|, each other action ε/|A(s)| (ε-greedy); ε-soft means π(a|s) ≥ ε/|A(s)|
Owner:  Sutton and Barto, Section 5.4, p. 100
Scope:  per state. With the grid's 4 moves: greedy 1 - 3ε/4, others ε/4 (arithmetic from the formula)
```

```text
Figure: Exercise 2.1, two actions and ε = 0.5: the greedy action is selected with probability 0.75 (1 - 0.5 + 0.5/2)
Owner:  Sutton and Barto, p. 28 (exercise; answer computed from the p. 100 formula)
Scope:  one selection
```

```text
Figure: greedy reward per step about 1, against a best possible of about 1.54
Owner:  Sutton and Barto, Section 2.3, p. 29, Figure 2.2
Scope:  10-armed testbed, 2000 runs of 1000 steps, sample averages starting at 0
```

```text
Figure: greedy found the optimal action in about one-third of tasks; ε = 0.1 never selected it more than 91% of the time
Owner:  Sutton and Barto, Section 2.3, p. 30
Scope:  same testbed; 91% = 1 - 0.1 + 0.1/10, the ε-greedy cap for 10 actions
```

```text
Figure: state y values 75.8 (r) vs 74.9 (l) with no exploration; 58.8 (l) vs 58.6 (r) with 50% exploration
Owner:  Singh et al. 2000, p. 288, Figure 1
Scope:  3-state deterministic MDP, γ = 0.9
```

```text
Figure: ε_t(s) = c/n_t(s), 0 < c < 1, is GLIE
Owner:  Singh et al. 2000, p. 292 and Appendix B.2, p. 304
Scope:  n_t(s) = visits to state s before time t; communicating discounted MDP
```

```text
Figure: ε-greedy cliff example uses ε = 0.1
Owner:  Sutton and Barto, Example 6.6, p. 132
Scope:  undiscounted episodic gridworld, Sarsa vs Q-learning (out of scope, pointer only)
```

```text
Figure: optimal runs of 20: 0 at 10,000 episodes without exploring starts; 10 at 10,000 and 18 at 100,000 with them
Owner:  course lesson action-values-from-samples, experiment.py output
Scope:  slippery grid, seeds 0-19, policy made greedy after every episode
```

## Limits

- No primary source I found proves that first-visit on-policy MC control with a fixed ε (Sutton and Barto's box, p. 101) converges to the best ε-soft policy, under any stated conditions. What is proven: (a) monotone improvement and a fixed point only at the best ε-soft policy, with exact evaluation (Sutton and Barto, pp. 101-103); (b) convergence to the best ε-greedy policy for one-step SARSA (Singh et al. 2000, Theorems 2-3). The lesson can show convergence only empirically, in its own runs.
- I found no primary proof that GLIE Monte Carlo control converges to q*. The claim appears in Silver's slides without proof. I could not open the Stanford CS234 notes said to state it as "Theorem 5.2" (the server returned 503 and failed TLS through the proxy).
- The earliest use of the term "ε-greedy" is not established. The earliest use I read is Sutton (1996, NIPS 8), which writes "what we call". Watkins (1989) describes a different rule without the term. Sutton and Barto (p. 44) say only that Watkins "may also have been" the first to use the method. The Watkins thesis is a scan with no text layer, and I read only Chapter 11's §6 and the surrounding pages, so another passage there could describe a closer rule.
- Singh et al.'s theorems assume a communicating, discounted, continuing MDP. The course grid is episodic with terminal cells. I found no source that applies those theorems to episodic tasks in this form.
- No source gives the gap between the best ε-soft policy and the optimal policy on the course grid, or how that gap depends on ε. That gap is the writer's computation. A route it might take: by Sutton and Barto's construction (p. 102), the best ε-soft value on the grid is the optimal value of a grid whose aim is re-drawn uniformly with probability ε before the slip. That framing is my reading of their construction, not their statement about this grid.

## Source assets

```text
Asset: Box "On-policy first-visit MC control (for ε-soft policies), estimates π ≈ π*", Sutton and Barto p. 101
Shows: the full algorithm in the field's standard notation, line by line, beside which a code listing can be read
Crop:  keep the whole box, title included (its "π ≈ π*" is discussed above); omit the surrounding prose and eq. (5.2)
```

```text
Asset: Eq. (5.2) and its continuation, Sutton and Barto pp. 101-102
Shows: the ε-soft improvement inequality step by step
Crop:  better retyped as an annotated equation than cropped, because it splits across a page break
```

```text
Asset: Figure 2.2, Sutton and Barto p. 29 (two panels: average reward and % optimal action over 1000 steps, for greedy, ε = 0.01 and ε = 0.1)
Shows: greedy selection leveling off below ε-greedy because it stops sampling an action whose early samples were bad, and ε = 0.1 capped near 91% optimal action
Crop:  keep both panels and their legends; it is a bandit figure (stage 6 topic), so it is usable only as a pointer or Go deeper item, not as the lesson's main figure
```

```text
Asset: Figure 1, Singh et al. 2000 p. 288 (3-state MDP x, y, z with actions l and r and rewards +15, +0, -1, +16, -5)
Shows: an MDP small enough to check by hand where exploration changes which action is best
Crop:  keep the diagram and caption; the values (75.8/74.9, 58.8/58.6) are in the body text, not the figure
```

None found in Sutton (1996), Watkins (1989), Silver's slides or Oliviers and Vinnicombe (2026) that would carry this lesson's argument better than prose.

## Discarded

```text
https://arxiv.org/abs/2301.09709: Winnicki and Srikant (2023) prove convergence of first-visit Monte Carlo policy iteration only when the improvement step uses lookahead; no ε-soft or ε-greedy result.
https://groups.google.com/g/rl-list/c/HXhy8NAOIQo: 2009 mailing-list thread (Tanner, Cubek, Littman, Zumwalt, Powell, Geist); informal opinions with no proof, partly truncated.
http://incompleteideas.net/book/ebook/node54.html: first-edition Section 5.4, superseded by the second edition the course cites; same definitions.
```
