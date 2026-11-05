# Evidence: reinforcement-learning/sarsa-and-q-learning (researcher 01)

The primary documents cover everything the brief lists, and the commission's central claim is a published theorem. Singh, Jaakkola, Littman and Szepesvári (2000) prove that tabular SARSA(0) under a fixed ε-greedy policy converges to the action values of the best policy in the ε-greedy class, provided its step sizes decay (Theorem 2, p. 297; Theorem 3, p. 299). They also state that the Q-learning rule does not find that policy (p. 298). Watkins and Dayan (1992, p. 282) prove that Q-learning converges to q* under any behavior that keeps trying every pair. The evidence is thin or qualifies the angle in five places. (1) In Sutton and Barto's pseudocode the two methods also differ in when the next action is chosen. SARSA chooses it before the update and Q-learning after, and that changes behavior when S′ = S, which happens on the course grid whenever a move hits an edge. (2) The fixed-ε theorem needs step sizes that shrink to zero. With a constant step the estimates never settle, and van Seijen et al. saw SARSA's values diverge at large α on the cliff. (3) Singh et al. state their results for discounted, continuing, communicating MDPs, and no source I read states them for an episodic grid. (4) Sutton and Barto's own Section 6.4 gives only the GLIE result, and its box is titled "estimating Q ≈ q*", so the fixed-ε claim has to cite Singh et al. (5) The brief's premise about Expected SARSA is wrong. Van Seijen et al. (2009) did not introduce it: Sutton and Barto credit George John (1994), and their own first edition posed the algorithm, unnamed, as Exercise 6.10. Van Seijen et al. named it and proved its convergence under GLIE.

## Sources

### 1. Sutton and Barto, Reinforcement Learning: An Introduction, 2nd edition

```text
URL:         http://incompleteideas.net/book/RLbook2020.pdf
             (authors' landing page: http://incompleteideas.net/book/the-book-2nd.html, which links this PDF.
             The https address on that host failed certificate verification from here, so the http address is recorded.)
Kind:        primary for the algorithms as the authors define them (update rules, boxes, Example 6.6,
             Expected Sarsa's definition, their own convergence summaries) and for the name "Sarsa",
             which Sutton gave it. Secondary for who introduced Q-learning, Sarsa and Expected Sarsa:
             the bibliographic remarks report other authors' work.
Establishes: firsthand: equations (6.7), (6.8), (6.9), the two boxes, Example 6.6, the on-/off-policy and
             target/behavior definitions. Repeats: the convergence results it summarizes without proof
             (p. 129, p. 131) and the attributions on pp. 139-140.
Paraphrase:  see locators.
Locators:    see below.
```

Printing check. The copyright page reads "© 2018, 2020 Richard S. Sutton and Andrew G. Barto". The PDF does not print the words "second printing". Its printed page numbers match every locator the earlier lessons give for this book: the Monte Carlo ES box on p. 99, the ε-soft box on p. 101, the text on p. 103, Example 6.2 on p. 125 and Example 6.6 on p. 132. The PDF page is the printed page plus 22. The copyright page also says "This work is licensed under the Creative Commons Attribution-NonCommercial-NoDerivs 2.0 Generic License", which matters for any figure captured from it.

Locators, in book order:

- **Section 2.5, p. 33, equation (2.7).** The step-size conditions are Σ α_n(a) = ∞ and Σ α_n²(a) < ∞. The book introduces them as "A well-known result in stochastic approximation theory" and does not name Robbins and Monro. It notes that a constant step size fails the second condition, so that "the estimates never completely converge but continue to vary in response to the most recently received rewards".
- **Section 5.4, p. 100.** "On-policy methods attempt to evaluate or improve the policy that is used to make decisions, whereas off-policy methods evaluate or improve a policy different from that used to generate the data."
- **Section 5.5, p. 103.** "The policy being learned about is called the target policy, and the policy used to generate behavior is called the behavior policy." On the ε-soft method of 5.4: "The on-policy approach in the preceding section is actually a compromise—it learns action values not for the optimal policy, but for a near-optimal policy that still explores." Importance sampling begins on this page, if the page points to it.
- **Section 6.4 "Sarsa: On-policy TD Control", p. 129.**
  - "for an on-policy method we must estimate q_π(s, a) for the current behavior policy π and for all states s and actions a."
  - Equation (6.7): Q(S_t, A_t) ← Q(S_t, A_t) + α[R_{t+1} + γ Q(S_{t+1}, A_{t+1}) − Q(S_t, A_t)].
  - "This update is done after every transition from a nonterminal state S_t. If S_{t+1} is terminal, then Q(S_{t+1}, A_{t+1}) is defined as zero."
  - The name: "This rule uses every element of the quintuple of events, (S_t, A_t, R_{t+1}, S_{t+1}, A_{t+1}), that make up a transition from one state–action pair to the next. This quintuple gives rise to the name Sarsa for the algorithm." The Sarsa backup diagram is in the right margin.
  - Convergence, quoted because the conditions are the evidence: "Sarsa converges with probability 1 to an optimal policy and action-value function, under the usual conditions on the step sizes (2.7), as long as all state–action pairs are visited an infinite number of times and the policy converges in the limit to the greedy policy (which can be arranged, for example, with ε-greedy policies by setting ε = 1/t)." The text cites no source for this here. The bibliographic remarks on p. 139 credit Singh et al. (2000).
- **Box, p. 130: "Sarsa (on-policy TD control) for estimating Q ≈ q*".** Parameters: "step size α ∈ (0, 1], small ε > 0". Q(terminal, ·) = 0. In each step the box takes A, observes R and S′, chooses A′ from S′ "using policy derived from Q (e.g., ε-greedy)", updates Q(S, A) with γQ(S′, A′), and then sets S ← S′ and A ← A′. The next action is chosen before the update.
- **Section 6.5 "Q-learning: Off-policy TD Control", p. 131.**
  - "off-policy TD control algorithm known as Q-learning (Watkins, 1989)".
  - Equation (6.8): Q(S_t, A_t) ← Q(S_t, A_t) + α[R_{t+1} + γ max_a Q(S_{t+1}, a) − Q(S_t, A_t)].
  - "the learned action-value function, Q, directly approximates q*, the optimal action-value function, independent of the policy being followed." "The policy still has an effect in that it determines which state–action pairs are visited and updated. However, all that is required for correct convergence is that all pairs continue to be updated." "Under this assumption and a variant of the usual stochastic approximation conditions on the sequence of step-size parameters, Q has been shown to converge with probability 1 to q*."
  - Box "Q-learning (off-policy TD control) for estimating π ≈ π*": same parameters. Each step chooses A from S, takes it, observes R and S′, updates with max_a Q(S′, a), and sets S ← S′. The action is chosen at the top of the step, after the previous update.
- **p. 132.** Exercise 6.11 asks why Q-learning is off-policy. Exercise 6.12: "Suppose action selection is greedy. Is Q-learning then exactly the same algorithm as Sarsa? Will they make exactly the same action selections and weight updates?" The book prints no answer.
- **Example 6.6 "Cliff Walking", p. 132.** The task is undiscounted and episodic, with reward −1 on every transition. "Stepping into this region incurs a reward of −100 and sends the agent instantly back to the start." Both methods use ε-greedy action selection with ε = 0.1. "After an initial transient, Q-learning learns values for the optimal policy, that which travels right along the edge of the cliff. Unfortunately, this results in its occasionally falling off the cliff because of the ε-greedy action selection. Sarsa, on the other hand, takes the action selection into account and learns the longer but safer path through the upper part of the grid. Although Q-learning actually learns the values of the optimal policy, its online performance is worse than that of Sarsa, which learns the roundabout policy. Of course, if ε were gradually reduced, then both methods would asymptotically converge to the optimal policy."
- **Section 6.6 "Expected Sarsa", p. 133.** The algorithm is "just like Q-learning except that instead of the maximum over next state–action pairs it uses the expected value, taking into account how likely each action is under the current policy." Equation (6.9): Q(S_t, A_t) ← Q(S_t, A_t) + α[R_{t+1} + γ Σ_a π(a | S_{t+1}) Q(S_{t+1}, a) − Q(S_t, A_t)]. "Given the next state, S_{t+1}, this algorithm moves deterministically in the same direction as Sarsa moves in expectation." Expected Sarsa "eliminates the variance due to the random selection of A_{t+1}". Figure 6.3 on p. 133 compares the three methods on the cliff as a function of α and is "Adapted from van Seijen et al. (2009)".
- **p. 134.** Figure 6.4 gives the backup diagrams for Q-learning and Expected Sarsa. "In these cliff walking results Expected Sarsa was used on-policy, but in general it might use a policy different from the target policy π to generate behavior ... suppose π is the greedy policy while behavior is more exploratory; then Expected Sarsa is exactly Q-learning."
- **Section 6.7, pp. 134-135.** This section covers maximization bias. In Example 6.7 and Figure 6.5, "Even at asymptote, Q-learning takes the left action about 5% more often than is optimal at our parameter settings (ε = 0.1, α = 0.1, and γ = 1)."
- **Section 7.5, p. 152.** "Is off-policy learning possible without importance sampling? Q-learning and Expected Sarsa from Chapter 6 do this for the one-step case". This is a citable reason that one-step Q-learning needs no importance sampling.
- **Bibliographical remarks 6.4, p. 139.** "The Sarsa algorithm was introduced by Rummery and Niranjan (1994). They explored it in conjunction with artificial neural networks and called it 'Modified Connectionist Q-learning'. The name 'Sarsa' was introduced by Sutton (1996). The convergence of one-step tabular Sarsa (the form treated in this chapter) has been proved by Singh, Jaakkola, Littman, and Szepesvári (2000)." Also on p. 139: "The modern form of the bucket brigade, when simplified in various natural ways, is nearly identical to one-step Sarsa, as detailed by Wilson (1994)."
- **Bibliographical remarks 6.5, p. 140.** "Q-learning was introduced by Watkins (1989), whose outline of a convergence proof was made rigorous by Watkins and Dayan (1992). More general convergence results were proved by Jaakkola, Jordan, and Singh (1994) and Tsitsiklis (1994)."
- **Bibliographical remarks 6.6, p. 140.** "The Expected Sarsa algorithm was introduced by George John (1994), who called it 'Q̄-learning' and stressed its advantages over Q-learning as an off-policy algorithm. John's work was not known to us when we presented Expected Sarsa in the first edition of this book as an exercise, or to van Seijen, van Hasselt, Whiteson, and Weiring (2009) when they established Expected Sarsa's convergence properties and conditions under which it will outperform regular Sarsa and Q-learning. ... Van Seijen et al. defined 'Expected Sarsa' to be an on-policy method exclusively (as we did in the first edition), whereas now we use this name for the general algorithm in which the target and behavior policies may differ. The general off-policy view of Expected Sarsa was noted by van Hasselt (2011), who called it 'General Q-learning.'" The book misspells Wiering as "Weiring" here. Its reference list, which begins on p. 481, has no entry for John (1994).

### 2. Sutton and Barto, Reinforcement Learning: An Introduction, 1st edition (1998), Section 6.5, Exercise 6.10

```text
URL:         http://incompleteideas.net/book/first/ebook/node65.html
Kind:        primary: the authors' own first edition, which van Seijen et al. and the 2nd edition both name
             as where the algorithm was posed.
Establishes: the 1998 book posed the algorithm as an exercise without naming it.
Paraphrase:  Exercise 6.10 describes a learning algorithm "just like Q-learning except that instead of the
             maximum over next state-action pairs it uses the expected value, taking into account how likely
             each action is under the current policy". It asks whether the method is on-policy or
             off-policy, what its backup diagram is, and whether it would work better or worse than Sarsa.
             The text gives the algorithm no name.
Locators:    Section 6.5 "Q-Learning: Off-Policy TD Control", Exercise 6.10 (HTML edition, no page numbers;
             the update rule is an image and did not come through as text)
```

### 3. Watkins, Learning from Delayed Rewards (1989)

```text
URL:         https://www.cs.rhul.ac.uk/~chrisw/new_thesis.pdf
             (Watkins's page https://www.cs.rhul.ac.uk/~chrisw/thesis.html: "the original electronic version is
             long lost, and this version has been scanned in from a photocopy." The PDF has no text layer.
             I read it from rendered page images.)
Kind:        primary: the author's thesis, where one-step Q-learning is defined.
Establishes: firsthand: the one-step Q-learning update, the requirement to try every action in every state,
             and the first convergence argument (an outline, per S&B p. 140).
Paraphrase:  Title page: "Learning from Delayed Rewards", Christopher John Cornish Hellaby Watkins,
             King's College, "Thesis Submitted for Ph.D.", May 1989.
             Ch. 5 §3.2, p. 64: the action value of an action is Q(x,a) = ρ(x,a) + γ Σ_y P_xy(a) V(y).
             Ch. 7 §3 "Learning Action-Values", p. 95: U^Q_t(x) = max_a Q_t(x,a), and Q defines a current
             policy f^Q that chooses an action of maximal estimated action value.
             p. 96: "The simplest method is one-step Q-learning": Q_{t+1}(x_t,a_t) = (1−α)Q_t(x_t,a_t) +
             α(r_t + γU^Q_t(x_{t+1})), where α is "a 'learning factor', a small positive number". All other Q
             values are unchanged. Watkins's r_t is the reward after a_t, which S&B write R_{t+1}.
             Appendix 1 "Convergence of One-Step Q-Learning", p. 220: the observations [x a r y] need not
             come from a connected sequence of actions. The proof builds an "action replay" process.
             Appendix 1 §3, p. 227, as printed: sufficient conditions are an infinite number of observations
             of each pair, learning factors that are positive, decrease monotonically and tend to zero, and
             a sum of learning factors that is infinite. The corrigenda page (the fifth page of the PDF,
             unnumbered) replaces p. 227 lines 7-13: r and y are sampled from a distribution depending only on
             x and a; rewards have "finite mean and finite variance"; and for each pair the learning factors
             are "monotonically decreasing, tends to zero, and sums to infinity".
Locators:    title page; Ch. 5 §3.2 p. 64; Ch. 7 §3 pp. 95-96; Appendix 1 p. 220 and §3 p. 227; corrigenda
             page (PDF p. 5). Printed page = PDF page − 7 in the body.
Quote:       p. 96: "Note that the actions that the agent should take are not specified. In fact, the agent
             is free to take whatever actions it likes, but for it to be sure of finding the optimal action
             value function eventually, it must try out each action in each state many times."
             p. 96, on priority: "Although this is a very simple idea, it has not, as far as I know, been
             suggested previously. However ... it is unlikely that nobody has considered this Monte-Carlo
             method before."
```

### 4. Watkins and Dayan, "Q-learning" (1992)

```text
URL:         https://doi.org/10.1007/BF00992698 (Machine Learning 8(3-4):279-292, May 1992, per Crossref)
             Read from Dayan's copy: https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf
             (The Springer page returned 429 and a cookie redirect from here.)
Kind:        primary: the authors' own convergence theorem and proof.
Establishes: firsthand: Q-learning converges to Q* with probability 1 under the stated conditions.
Paraphrase:  The paper is labelled "Technical Note". Christopher J.C.H. Watkins is listed at 25b Framfield
             Road, Highbury, London, and Peter Dayan at the Centre for Cognitive Science, University of
             Edinburgh.
             Abstract, p. 279: the paper "presents and proves in detail a convergence theorem for Q-learning
             based on that outlined in Watkins (1989)". Q-learning "converges to the optimum action-values
             with probability 1 so long as all actions are repeatedly sampled in all states and the
             action-values are represented discretely."
             §2, p. 280: discounted rewards, factor γ with 0 < γ < 1.
             §2, p. 281, eq. (1): Q_n(x,a) = (1−α_n)Q_{n−1}(x,a) + α_n[r_n + γV_{n−1}(y_n)] if x = x_n and
             a = a_n, and Q_{n−1}(x,a) otherwise. Eq. (2): V_{n−1}(y) = max_b Q_{n−1}(y,b). The description
             "assumes a look-up table representation".
             p. 281: the sequence "must include an infinite number of episodes for each starting state and
             action ... under the stochastic conditions of the theorem, no method could be guaranteed to find
             an optimal policy under weaker conditions. Note, however, that the episodes need not form a
             continuous sequence—that is the y of one episode need not be the x of the next episode."
             Watch the word: W&D's "episode" is one (x, a, y, r) step, not an episode in the course's sense.
             This clause is what lets the theorem cover episodic resets.
             Theorem, p. 282: "Given bounded rewards |r_n| ≤ ℜ, learning rates 0 ≤ α_n < 1, and
             Σ_{i=1}^∞ α_{n^i(x,a)} = ∞, Σ_{i=1}^∞ [α_{n^i(x,a)}]² < ∞, ∀x, a, then Q_n(x, a) → Q*(x, a)
             as n → ∞, ∀x, a, with probability 1." Here n^i(x,a) is the index of the ith time action a is
             tried in state x (p. 281).
Locators:    abstract p. 279; §2 pp. 280-281, eqs. (1)-(2); Theorem p. 282, eq. (3)
```

### 5. Rummery and Niranjan, "On-line Q-learning using connectionist systems" (1994)

```text
URL:         https://mi.eng.cam.ac.uk/reports/abstracts/rummery_tr166.html (Cambridge abstract page)
             PDF: https://mi.eng.cam.ac.uk/reports/svr-ftp/auto-pdf/rummery_tr166.pdf ("automatically generated
             from original PostScript"; its text layer is unreadable, so I read rendered pages)
Kind:        primary: the authors' report introducing the update S&B call Sarsa.
Establishes: firsthand: the MCQ-L update and its difference from Q-learning, what the authors expect it to
             converge to, and, in a footnote, that the name SARSA was Sutton's suggestion.
Paraphrase:  Cover: "On-line Q-learning using connectionist systems", G. A. Rummery & M. Niranjan,
             CUED/F-INFENG/TR 166, September 1994, Cambridge University Engineering Department.
             The setting is back-propagation neural networks with eligibility traces, applied to a
             simulated robot.
             §3.2 "Modified Connectionist Q-Learning", p. 6: the authors doubt that max_a Q(x,a) gives the best
             estimate of the return early in learning, and object to zeroing λ after non-greedy actions.
             They "introduce an alternative update algorithm based more strongly on TD-learning, called
             Modified Connectionist Q-Learning (MCQ-L)". Eq. (9): Δw_t = η[r_t + γQ_{t+1} − Q_t]
             Σ_{k=0}^t (γλ)^{t−k} ∇_w Q_k, where Q_t is shorthand for Q(x_t, a_t) (footnote 1, p. 5).
             "This differs from normal Q-learning in the use of the Q_{t+1} associated with the action
             selected, rather than the greedy max_{a∈A} Q_{t+1} used in Q-learning."
             p. 7: if greedy actions are taken, the equation "is exactly equivalent to standard Q-learning".
             "MCQ-L therefore samples from the distribution of possible future returns given the current
             exploration policy". Eq. (10) gives the target as E{r_t + γ Σ_a P(a|x_{t+1}) Q(x_{t+1}, a)}.
             "Consequently, at any point during training, the Q-function should give an estimation of the
             expected returns that are available for the current exploration policy." The authors also expect
             it to reach the optimal values once exploration is reduced. They assert this without proof.
Locators:    cover; §3 p. 5 (footnote 1); §3.2 p. 6, eq. (9) and footnote 3; p. 7, eq. (10)
Quote:       footnote 3, p. 6, attached to "(MCQ-L)": "Though Rich Sutton suggests SARSA, as you need to know
             State-Action-Reward-State-Action before performing an update."
```

The tabular one-step rule (6.7) is eq. (9) with λ = 0 and a lookup table in place of the network. Singh et al. (p. 291) call SARSA(0) "a special case of SARSA(λ) with λ = 0". The report itself never writes the tabular one-step form.

### 6. Sutton, "Generalization in Reinforcement Learning: Successful Examples Using Sparse Coarse Coding" (1996)

```text
URL:         https://proceedings.neurips.cc/paper/1995/hash/8f1d43620bc6bb580df6e80b0dc05c48-Abstract.html
             (listed as Advances in Neural Information Processing Systems 8 (NIPS 1995); pp. 1038-1044 per the
             S&B reference list; PDF from the "Paper" link on that page)
Kind:        primary: the printed use of the name that S&B p. 139 credit, by its author.
Establishes: firsthand: Sutton used the name "sarsa" in print, crediting Rummery and Niranjan for the
             method, and described it as learning the values of the policy being followed.
Paraphrase:  Richard S. Sutton, University of Massachusetts, Amherst.
             §1, p. 1039: "The reinforcement learning methods we use are variations of the sarsa algorithm
             (Rummery & Niranjan, 1994; Singh & Sutton, 1996). This method is the same as the TD(λ) algorithm
             (Sutton, 1988), except applied to state-action pairs instead of states, and where the predictions
             are used as the basis for selecting actions." The action values "are estimated for all states and
             actions, and for the policy currently being followed by the agent."
             Figure 1, p. 1040: the sarsa algorithm with CMAC features, ε-greedy selection and traces.
             The paper does not explain the name.
Locators:    §1 p. 1039; Figure 1 p. 1040
```

### 7. Singh, Jaakkola, Littman and Szepesvári, "Convergence Results for Single-Step On-Policy Reinforcement-Learning Algorithms" (2000)

```text
URL:         https://doi.org/10.1023/A:1007678930559 (Machine Learning 38(3):287-308, March 2000, per Crossref)
             Read from Szepesvári's copy: https://sites.ualberta.ca/~szepesva/papers/singh98convergence.pdf
             (the copy's running header misprints the volume as 39; journal page numbers are printed on
             every page)
Kind:        primary: the authors' own theorems for SARSA(0).
Establishes: firsthand: SARSA(0) converges to Q* under GLIE (Theorem 1). Under a fixed rank-based
             exploration policy, which includes fixed-ε ε-greedy, it converges to Q̄, whose greedy policy is
             optimal among policies of that kind (Theorems 2 and 3). Q-learning does not find that policy
             (p. 298).
Paraphrase:  The authors are listed as Satinder Singh (AT&T Labs-Research), Tommi Jaakkola (Department of
             Computer Science, MIT), Michael L. Littman (Department of Computer Science, Duke University) and
             Csaba Szepesvári (Mindmaker Ltd., Budapest).
             §1, pp. 287-288: off-policy algorithms "may update estimated value functions on the basis of
             hypothetical actions"; on-policy algorithms "update value functions strictly on the basis of the
             experience gained from executing some (possibly non-stationary) policy." Figure 1, p. 288, is the
             three-state example that lesson 5 already cites.
             §2, pp. 289-290: the setting is an infinite-horizon discounted MDP, 0 ≤ γ < 1, assumed
             "communicating" (every state reachable from every other).
             §2.1, p. 290: eq. (2) is Q-learning and eq. (3) is SARSA(0), Q_{t+1}(s_t,a_t) =
             (1−α_t)Q_t(s_t,a_t) + α_t[r_t + γQ_t(s_{t+1},a_{t+1})].
             p. 291: "Q-learning makes an update based on the greedy Q value of the successor state, s_{t+1},
             while SARSA(0) uses the Q value of the action a_{t+1} actually chosen by the learning policy. This
             makes SARSA(0) an on-policy algorithm ... because SARSA(0) learns the value of its own actions,
             the Q values can converge to optimality in the limit only if the learning policy chooses actions
             optimally in the limit." Also: "Under a greedy learning policy ... the update rules for
             Q-learning and SARSA(0) are identical."
             §2.2, pp. 291-292: GLIE means "each action is executed infinitely often in every state that is
             visited infinitely often" and "in the limit, the learning policy is greedy with respect to the
             Q-value function with probability 1". ε-greedy with ε_t(s) = c/n_t(s), 0 < c < 1, is GLIE
             (p. 292, proved in Appendix B.2, p. 304). p. 292: ε-greedy with a fixed ε is an RRR ("restricted
             rank-based randomized") learning policy with T(1) = 1 − ε + ε/m and T(i) = ε/m otherwise.
             Theorem 1, p. 294: with a GLIE learning policy, a lookup table, Σ_t α_t(s,a) = ∞,
             Σ_t α_t²(s,a) < ∞, α_t(s,a) = 0 unless (s,a) = (s_t,a_t), and Var{r(s,a)} < ∞, "Q_t converges
             to Q* and the learning policy π_t converges to an optimal policy π*".
             §3.2, p. 296, eq. (7): Q̄(s,a) = R(s,a) + γ Σ_{s'} P^a_{ss'} Σ_{a'} T(ρ(Q̄,s',a')) Q̄(s',a'), the
             fixed point in which the next action's probabilities come from the ranks under Q̄ itself.
             Theorem 2, p. 297: under an RRR learning policy, with the next action drawn from the ranks under
             the current Q_t (condition 1), a lookup table, the same step-size conditions and finite reward
             variance, SARSA(0)'s Q_t converges to Q̄.
             p. 298: "The greedy restricted policy for Q* (the optimal Q-value function of the MDP) is not an
             optimal restricted policy in general, so the Q-learning rule in Eq. (2) does not find an optimal
             restricted policy."
             Theorem 3, p. 299: "The greedy restricted policy with respect to Q̄ is an optimal restricted
             policy." The proof builds an alternate MDP whose rewards and transitions are T-weighted mixtures
             over actions, the same construction as lesson 5's modified grid.
             p. 300: "As a corollary of Theorem 2, given a communicating MDP and an RL algorithm that follows
             an RRR learning policy specified by T where T(i) > 0 for all 1 ≤ i ≤ m, SARSA(0) converges to an
             optimal restricted policy." The same page adds: "the fact that convergence depends on decaying
             the learning rate to zero means that this approach is somewhat self-contradictory; in the limit,
             the learner is still exploring, but it is not able to learn anything new from its discoveries."
             §4, p. 300: "To the best of our knowledge, these constitute the first convergence results for any
             on-policy algorithm."
             Note 1, p. 306: the name SARSA refers to "a State, Action, Reward, State, Action 5-tuple".
Locators:    pp. 287-288; Figure 1 p. 288; §2.1 pp. 290-291; §2.2 pp. 291-292; Theorem 1 p. 294; eq. (7)
             p. 296; Theorem 2 p. 297; p. 298; Theorem 3 p. 299; corollary and remark p. 300; Appendix B.2
             p. 304; Note 1 p. 306
```

My derivation, not the paper's: for the ε-greedy choice of T, a restricted policy is "aim at one arrow per cell with probability 1 − ε + ε/4, the rest ε/4 each". That class is exactly the ε-greedy policies around deterministic arrows. Lesson 5's best ε-soft policy is ε-greedy with respect to its own action values (S&B pp. 102-103), so it belongs to this class, and Q̄ for this T is lesson 5's q̃. Singh et al. never use the term ε-soft.

### 8. van Seijen, van Hasselt, Whiteson and Wiering, "A Theoretical and Empirical Analysis of Expected Sarsa" (2009)

```text
URL:         https://doi.org/10.1109/ADPRL.2009.4927542 (2009 IEEE Symposium on Adaptive Dynamic Programming
             and Reinforcement Learning, pp. 177-184, March 2009, per Crossref)
             Read from Whiteson's copy: https://www.cs.ox.ac.uk/people/shimon.whiteson/pubs/vanseijenadprl09.pdf
             (8 pages, no printed page numbers; locators are section and page of that PDF)
Kind:        primary for the name, the on-policy definition, the GLIE convergence theorem and their cliff
             runs. Secondary on where the idea came from: it reports S&B's exercise.
Establishes: firsthand: the paper names the algorithm and proves its convergence under GLIE. It does not
             claim to have invented the update.
Paraphrase:  The authors are listed as Harm van Seijen (TNO Defense, Safety and Security, The Hague),
             Hado van Hasselt (Utrecht University), Shimon Whiteson (University of Amsterdam) and Marco
             Wiering (University of Groningen).
             §I, p. 1: "Sutton and Barto proposed, in a little-noted exercise in their classic book [2, Exercise
             6.10], a variation on Sarsa designed to reduce variance in the updates. ... Though the resulting
             algorithm, which we call Expected Sarsa, may offer substantial advantages over Sarsa, it has never
             been systematically studied". Sarsa "is named for the five components employed in its update
             rule".
             §II, p. 2: "Because Sarsa is on-policy, it will not converge to optimal Q values as long as
             exploration occurs. However, by annealing exploration over time, Sarsa can converge to optimal Q
             values, just like Q-learning."
             §III, p. 2: eq. (5) is the update and Algorithm 1 the full method. "Because the update rule of
             Expected Sarsa, unlike Sarsa, does not make use of the action taken in s_{t+1}, action selection
             can occur after the update. Doing so can be advantageous in problems containing states with
             returning actions, i.e. P(s_{t+1} = s_t) > 0." "Q-learning's update rule (3) is just a special
             case of Expected Sarsa's update rule (5) for the case when the estimation policy is greedy."
             §IV, p. 3, Theorem 1: Expected Sarsa converges to the optimal value function given finite S and A,
             step sizes with Σα = ∞ and Σα² < ∞, a GLIE policy, and bounded rewards. The paper gives no
             fixed-ε result.
             §VI, p. 4: Type 1 problems are those "where the optimal ε-soft policy is better than the ε-soft
             policy based on Q*(s, a)", and Type 2 those where the two are equal. Hypothesis 1: Expected Sarsa
             will outperform Q-learning on Type 1.
             §VII.A, p. 5, cliff walking with ε = 0.1: "for large values of α the Q values of Sarsa diverge.
             Although the policy is still improved over the initial random policy during the early stages of
             learning, divergence causes the policy to get worse in the long run."
             §VII.B, p. 6, deterministic windy grid world: "the optimal policy among the ε-greedy policies (Expected Sarsa)
             is equal to the policy that is ε-greedy with respect to Q*(s, a) (Q-learning)", a Type 2 case.
Locators:    §I p. 1; §II-III p. 2; §IV p. 3; §VI p. 4; §VII.A p. 5; §VII.B p. 6 (pages of the 8-page PDF)
```

### 9. John, "When the Best Move Isn't Optimal: Q-learning with Exploration" (1994)

```text
URL:         https://cdn.aaai.org/AAAI/1994/AAAI94-258.pdf (AAAI-94 Proceedings, Student Abstracts, p. 1464)
Kind:        primary: the author's own one-page abstract, which S&B p. 140 credit with introducing Expected
             Sarsa.
Establishes: firsthand: an update that replaces the max with the expectation under the exploration
             probabilities, named "Q̄-learning", and a run where it earns more than Q-learning under
             persistent exploration.
Paraphrase:  George H. John, Computer Science Department, Stanford University.
             "The 'optimal' policy produced by Q-learning is no longer optimal if its prescriptions are only
             followed occasionally. In many situations (e.g., dynamic environments), the agent never stops
             exploring. In such domains Q-learning converges to policies which are suboptimal in the sense that
             there exists a different policy which would achieve higher reward when combined with
             exploration."
             Eq. (2) replaces V̂(x) ← max_a Q̂(x,a) with V̂(x) ← Σ_a P(a) Q̂(x,a): "update V̂(x) with the
             expected, not the maximal, future reward, taking into account the exploration policy when
             calculating the expected reward. We call this new algorithm Q̄-learning."
             Figure 1 reports average reward 3.35 for Q and 3.44 for Q̄, with 30% random actions, γ = .9,
             β = .5 and 10^6 steps. The text adds: "Q̄-learning always generates policies giving greater
             average reward, but the improvement over Q-learning depends on the domain and the amount of
             exploration."
Locators:    p. 1464, both columns and Figure 1
```

## Contradictions

1. **Do the two methods differ only in the target?** The update rules (6.7) and (6.8) differ only in the next-action term. The boxes on pp. 130-131 also order the steps differently. SARSA chooses A′ from Q before updating Q(S, A). Q-learning chooses its next action at the top of the next step, after the update. Exercise 6.12 (p. 132) asks whether greedy Q-learning and greedy Sarsa are "exactly the same", and the book prints no answer. Van Seijen et al. (§III, p. 2) say that choosing after the update matters in states with P(s_{t+1} = s_t) > 0. On the course grid a move into an edge leaves the agent in place, so S′ = S does occur. Singh et al. (p. 291) say only that the update rules are identical under greedy selection. A claim that the methods differ "only" in the target holds for the update rules. It does not hold for the boxes as printed unless the lesson's code chooses the next action at the same point in both.
2. **Box title against theorem.** The Sarsa box on p. 130 is titled "for estimating Q ≈ q*" and takes "small ε > 0" as a fixed parameter. With ε held fixed, Singh et al.'s Theorem 2 (p. 297) gives convergence to Q̄, not to Q*. Van Seijen et al. (§II, p. 2) say Sarsa "will not converge to optimal Q values as long as exploration occurs". S&B's text on p. 129 qualifies the claim with the GLIE condition. Lesson 5 found the same mismatch between the p. 101 box title and the p. 103 text.
3. **Which GLIE schedule is proved.** S&B (p. 129) give "setting ε = 1/t" as an example without proof. Singh et al. prove the GLIE property for ε_t(s) = c/n_t(s) with 0 < c < 1, where n_t(s) counts visits to state s (Appendix B.2, p. 304).
4. **Q-learning's step-size conditions differ by document.** Watkins's thesis as printed (p. 227) asks for learning factors that decrease monotonically to zero with an infinite sum, and has no square-summability condition. The corrigenda add finite reward mean and variance and keep the monotone decrease. Watkins and Dayan's Theorem (p. 282) asks for bounded rewards, 0 ≤ α_n < 1, Σα = ∞ and Σα² < ∞ for each pair, with no monotonicity. S&B (p. 131) call these "a variant of the usual stochastic approximation conditions". Cite Watkins and Dayan for the conditions a page states.
5. **Who introduced Expected SARSA.** The brief allows for van Seijen et al. (2009) having introduced it, and they did not. S&B (p. 140) credit John (1994), who called it Q̄-learning. S&B's own 1998 edition posed it unnamed as Exercise 6.10, and van Seijen et al. (§I, p. 1) cite that exercise. Van Seijen et al. contributed the name, an on-policy-only definition and a GLIE convergence proof. S&B now use the name for the general algorithm, in which the behavior policy may differ from the target policy. They credit that general view to van Hasselt (2011), which I did not open. There is also a small mismatch: S&B say John "stressed its advantages over Q-learning as an off-policy algorithm", but the abstract I read argues from the agent's continued exploration, which is the on-policy case.
6. **Qualifiers on "Rummery and Niranjan introduced SARSA".** Their 1994 rule is for neural networks with eligibility traces (eq. (9)). The tabular one-step rule is its λ = 0 special case, and the report never writes that form. S&B (p. 139) also say that a simplified modern bucket brigade "is nearly identical to one-step Sarsa", citing Wilson (1994), which I did not open. Singh et al. cite a Rummery PhD thesis dated 1994, where S&B list Rummery (1995). I opened neither.
7. **The name.** These sources agree. Rummery and Niranjan's footnote (September 1994) records the name as Sutton's suggestion. S&B (p. 139) say Sutton (1996) introduced it, and that paper uses it in print (p. 1039). The quintuple explanation appears in S&B (p. 129), in Singh et al.'s Note 1 (p. 306) and in van Seijen et al. (p. 1). The casing differs: "SARSA" (Rummery and Niranjan, Singh et al.), "sarsa" (Sutton 1996) and "Sarsa" (S&B).
8. **Fixed-ε SARSA needs a decaying step.** Theorem 2's third condition is Σα² < ∞. Singh et al. (p. 300) call the arrangement "somewhat self-contradictory". With a constant α the estimates keep moving (S&B p. 33). Van Seijen et al. (§VII.A, p. 5) saw SARSA's Q values diverge at large α on the deterministic, undiscounted cliff. A run at constant α is evidence about constant α only, and the theorem does not speak for it.
9. **Episodic grid against the theorems' setting.** Singh et al. assume a communicating, discounted, infinite-horizon MDP (pp. 289-290). The corollary on p. 300 uses that assumption to guarantee infinite visits. The course grid ends episodes at the goal and the pit and restarts them. Watkins and Dayan explicitly allow disconnected transitions (p. 281), which covers resets for Q-learning. Singh et al. say nothing about episodic tasks. Their Lemma 1 needs only finitely many pairs, the step-size conditions on each pair and a γ-contraction, which suggests the proof carries over. That reading is mine, not the paper's.
10. **Q-learning's lower online return is not universal.** The angle's prediction that Q-learning's ε-greedy behavior can earn less is supported by S&B's Example 6.6 (p. 132), John's Figure 1, Singh et al. p. 298 and van Seijen et al.'s Type 1 problems (§VI). Van Seijen et al.'s windy grid world (§VII.B, p. 6) is a Type 2 case in which the two policies coincide. On the course grid lesson 5 found that the best ε-soft arrows equal the optimal ones below ε = 0.33, so a gap requires ε ≥ 0.33. The commission's ε = 0.5 is in that range.
11. **"Q-learning learns q*" at a constant step.** S&B Example 6.7 (pp. 134-135) shows maximization bias. Even at asymptote, with ε = 0.1, α = 0.1 and γ = 1, Q-learning takes the worse action about 5% more often than optimal. On the slippery grid, Q-learning's finite-run estimates can sit above q*. The convergence theorem assumes decaying steps.

## Numbers

```text
Figure: ε = 0.1; reward −1 per transition, −100 for stepping into the cliff (agent sent back to start); undiscounted
Owner:  Sutton and Barto, Example 6.6, p. 132
Scope:  cliff-walking gridworld; plot x-axis 0-500 episodes

Figure: Sarsa's curve sits just above −25 and Q-learning's near −50 "sum of rewards during episode"
Owner:  Sutton and Barto, Example 6.6 plot, p. 132 (read off the plot; the text states no numbers)
Scope:  ε = 0.1, episodes 0-500; averaging not stated on the page

Figure: asymptotic = average over 100,000 episodes (10 runs); interim = average over first 100 episodes (50,000 runs); α from 0.1 to 1; ε = 0.1
Owner:  Sutton and Barto, Figure 6.3 caption, p. 133 (adapted from van Seijen et al. 2009)
Scope:  cliff walking, Sarsa, Q-learning, Expected Sarsa

Figure: Q-learning takes left "about 5% more often than is optimal" at asymptote
Owner:  Sutton and Barto, Example 6.7 / Figure 6.5, p. 135
Scope:  ε = 0.1, α = 0.1, γ = 1; 10,000 runs; two-state maximization-bias MDP

Figure: ε = 1/t (example GLIE schedule, unproved in the book)
Owner:  Sutton and Barto, p. 129
Scope:  Sarsa convergence statement

Figure: ε_t(s) = c / n_t(s), 0 < c < 1, is GLIE
Owner:  Singh et al. 2000, §2.2 p. 292; Appendix B.2 p. 304
Scope:  n_t(s) = visits to state s up to time t

Figure: fixed-ε ε-greedy as RRR: T(1) = 1 − ε + ε/m, T(i) = ε/m for i > 1
Owner:  Singh et al. 2000, p. 292
Scope:  m = number of actions (4 on the course grid)

Figure: no exploration: from y, action r worth 75.8 against 74.9 for l; with 50% exploration: l worth 58.8 against 58.6 for r
Owner:  Singh et al. 2000, §1 p. 288 and Figure 1 (the text misprints the first pair's second action as "r")
Scope:  three-state deterministic MDP, γ = 0.9

Figure: average reward 3.35 (Q-learning) against 3.44 (Q̄-learning)
Owner:  John 1994, Figure 1, p. 1464
Scope:  30% random actions, γ = 0.9, β = 0.5, 10^6 steps, one gridworld

Figure: 0 ≤ α_n < 1, Σ_i α_{n^i(x,a)} = ∞, Σ_i α_{n^i(x,a)}² < ∞ for every (x, a); |r_n| ≤ ℜ
Owner:  Watkins and Dayan 1992, Theorem, p. 282
Scope:  per-pair step sizes, lookup table, 0 < γ < 1

Figure: Σ_n α_n(a) = ∞ and Σ_n α_n²(a) < ∞
Owner:  Sutton and Barto, eq. (2.7), p. 33
Scope:  step sizes for the nth update of a given estimate

Figure: step size α ∈ (0, 1], "small ε > 0"
Owner:  Sutton and Barto, Sarsa box p. 130 and Q-learning box p. 131
Scope:  algorithm parameters as printed
```

## Limits

- No source I read states SARSA's fixed-ε convergence for an episodic task. Singh et al. state it for discounted, continuing, communicating MDPs (see Contradiction 9).
- That Singh et al.'s optimal restricted policy, for ε-greedy T, is lesson 5's best ε-soft policy is my derivation (see the note under Source 7). No source says it in those words.
- Robbins and Monro (1951, Annals of Mathematical Statistics 22(3):400-407, DOI 10.1214/aoms/1177729586 per Crossref) was not opened: the Project Euclid PDF returned a bot-check page. S&B do not name Robbins and Monro at (2.7). If the page calls the conditions "Robbins–Monro", that label rests on no document I read. Stating the conditions with S&B (2.7), Watkins and Dayan eq. (3) or Singh et al. Theorem 2 is sourced, and lesson 3 already taught the two conditions.
- I did not open: Rummery's PhD thesis (1994 per Singh et al., 1995 per S&B); Singh and Sutton (1996), so I cannot say whether it printed "sarsa" before Sutton's NIPS paper; Wilson (1994) on the bucket brigade; van Hasselt (2011) on "General Q-learning"; Jaakkola, Jordan and Singh (1994); Tsitsiklis (1994). The brief asks for none of them.
- What the letter Q stands for is not stated in the pages of Watkins's thesis I read (Ch. 5 §3.2, p. 64; Ch. 7 §3, pp. 95-96). Watkins and Dayan's abstract (p. 279) speaks of "evaluations of the quality of particular actions at particular states" but does not say the letter stands for quality.
- The PDF of Sutton and Barto does not print the words "second printing". It carries © 2018, 2020, and its page numbers match the locators in the earlier lessons.
- Expected SARSA's convergence is proved only under GLIE (van Seijen et al., Theorem 1). No source I read gives a fixed-ε result for it. The commission makes it mention-only.
- Publisher landing pages for Watkins and Dayan and for Singh et al. did not load (Springer returned 429 and a cookie redirect). Bibliographic data comes from Crossref, and the text from the author-hosted copies named above.

## Source assets

Sutton and Barto, 2nd edition (the CC BY-NC-ND 2.0 notice on the copyright page applies to any capture):

```text
Asset: the Sarsa box, p. 130, and the Q-learning box, p. 131
Shows: the one changed term in the update (γQ(S′, A′) against γ max_a Q(S′, a)), and that Sarsa chooses A′ before
       the update while Q-learning chooses its action at the top of the next step
Crop:  each whole box with its title bar, including the "Choose A′ from S′" line in the Sarsa box; omit the
       surrounding Example 6.5 and exercise text

Asset: Example 6.6 figure, p. 132: the cliff gridworld with "Safer path" and "Optimal path", and the plot of sum of
       rewards per episode for Sarsa and Q-learning
Shows: the two learned routes and the gap in online return at ε = 0.1
Crop:  keep both path labels, the R = −1 and R = −100 labels, both curves with their labels, and the axis labels and
       ticks; omit the wrapped body text

Asset: Figure 6.4, p. 134, backup diagrams for Q-learning and Expected Sarsa (the Sarsa diagram is in the right
       margin of p. 129)
Shows: max arc against expectation over next actions
Crop:  both diagrams with the caption; useful only if the page does not draw its own

Asset: Figure 6.3, p. 133
Shows: interim and asymptotic return of the three methods against α on the cliff
Crop:  plot, legend and full caption including "Adapted from van Seijen et al. (2009)"; Expected SARSA is mention-only,
       so this is probably more than the page needs
```

Rummery and Niranjan (1994):

```text
Asset: §3.2 on p. 6: the "(MCQ-L)³" sentence, eq. (9), and footnote 3
Shows: the method's authors recording, in September 1994, that the name SARSA was Rich Sutton's suggestion
Crop:  footnote 3 in full with the footnote rule above it, plus the line carrying the superscript 3 so the reader
       sees what it is attached to; the equation is optional
```

Watkins (1989):

```text
Asset: thesis p. 96: the typewritten one-step Q-learning equation through "must try out each action in each state
       many times"
Shows: the original definition and its only requirement on behavior
Crop:  from "The simplest method is one-step Q-learning" through "many times"; the page is a scan of a photocopy,
       so check legibility at phone width
```

Watkins and Dayan (1992):

```text
Asset: the Theorem, p. 282
Shows: the exact convergence conditions, eq. (3)
Crop:  the heading "Theorem" through "with probability 1"
```

John (1994):

```text
Asset: Figure 1, p. 1464: two small gridworld policies, "Q: reward = 3.35" and "Q̄: reward = 3.44"
Shows: an exploration-aware update choosing a different policy that earns more under 30% random actions
Crop:  both grids, both reward labels, and the caption with the parameters
```

Singh et al. (2000): None found beyond Figure 1 (p. 288), which lesson 5 already points to.
Sutton (1996): None found.
van Seijen et al. (2009): None found. Sutton and Barto's Figure 6.3 is adapted from their Fig. 2 and is the clearer version.
Sutton and Barto, 1st edition HTML: None found.

## Discarded

```text
https://link.springer.com/article/10.1007/BF00992698: returned 429 and a cookie redirect; the DOI is recorded and the text read from Dayan's copy
https://link.springer.com/article/10.1023/A:1007678930559: cookie redirect and an HTML stub in place of the PDF; the DOI is recorded and the text read from Szepesvári's copy
https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-22/issue-3/A-Stochastic-Approximation-Method/10.1214/aoms/1177729586.pdf: returned a bot-check page, not the paper; not read and outside the brief
https://mlanthology.org/aaai/1994/john1994aaai-best/: index entry only; used to find the AAAI PDF, which is the document cited
```
