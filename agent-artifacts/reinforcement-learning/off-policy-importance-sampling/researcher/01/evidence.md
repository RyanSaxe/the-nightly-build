# Evidence: reinforcement-learning/off-policy-importance-sampling (researcher 01)

Sutton and Barto's second edition, Section 5.5 (pp. 103–108), supports every definition the
lesson needs. It defines coverage, the importance-sampling ratio, ordinary and weighted importance
sampling, and their bias and variance, and it works Example 5.5 with its infinite-variance sum.
Section 5.6 (pp. 109–110) gives the incremental weighted update. The book states the key identity,
E[ρG | S_t = s] = v_π(s) (eq. 5.4), without deriving it, so the derivation on the page is the
writer's own and needs no citation. Four places push back on the commission. (1) Ordinary
importance sampling is unbiased only in its first-visit form; the book calls every-visit ordinary
IS biased. (2) Infinite variance needs episodes of unbounded length, and the book attributes it to
loops. Long episodes alone or a distant target alone do not produce it, because with a bounded
length the ratio is bounded. (3) The book's Figure 5.4 caption says the ordinary estimates "do
not converge". Precup, Sutton and Dasgupta (2001) note that the law of large numbers gives
convergence with probability 1 whenever returns are bounded, which holds in Example 5.5, where
E[ρG] = 1 is finite. The variance is infinite and the convergence is slow, and the lesson must not
claim the estimate never converges. (4) No paper clearly introduced importance sampling for
off-policy RL evaluation. Precup, Sutton and Singh (2000) credit the weighted Monte Carlo method in
Sutton and Barto's 1998 first edition, and the second edition credits Precup et al. only with
per-decision importance sampling, so the lesson should not name an "introducer". The course code is
well documented. `baselines.exact_value` solves any stochastic policy table exactly, but it returns
only the 14-cell mean. No course function computes a ratio, so the estimators need new code.

## Sources

### Sutton and Barto, Reinforcement Learning: An Introduction, 2nd edition

```text
URL:         http://incompleteideas.net/book/RLbook2020.pdf  (authors' full PDF, linked as "Full Pdf"
             from the book page http://incompleteideas.net/book/the-book-2nd.html, which states
             "Second Edition ... MIT Press, Cambridge, MA, 2018"). Publisher page
             https://mitpress.mit.edu/9780262039246/reinforcement-learning/ returns 403 to a plain
             request (gated, not dead); the course already cites it as the book's Sources link.
             PDF page = printed page + 22 (p. 103 is #page=125; p. 107 is #page=129;
             p. 110 is #page=132; p. 149 is #page=171; p. 152 is #page=174).
Kind:        primary. Sutton and Barto are the authors of the definitions, the estimators as written
             here, Examples 5.4–5.5, the variance calculation and the incremental algorithm. For the
             claim that weighted-IS variance goes to zero they repeat Precup, Sutton and Dasgupta
             (2001), which owns it (entry below).
Establishes: firsthand: everything listed under Paraphrase. Repeats: the weighted-IS variance
             result (PSD 2001) and the history of weighted IS (Rubinstein 1981 etc., not opened).
Locators:    Section 5.5, pp. 103–108; Example 5.4 and Fig. 5.3, p. 106; Example 5.5,
             pp. 106–108, Fig. 5.4 p. 107; Exercises 5.5 (p. 105), 5.6–5.8 (p. 108); Section 5.6,
             pp. 109–110, box p. 110; Section 5.10 Summary, p. 116; Bibliographical and Historical
             Remarks 5.5 and 5.9, p. 117; Section 7.3, pp. 148–149; Section 7.5, p. 152; reference
             list (Precup, Sutton, Singh 2000: pp. 759–766). Pagination in RLbook2018.pdf
             (http://incompleteideas.net/book/RLbook2018.pdf) is identical for pp. 103–110. A
             word-level diff found layout changes only, plus one notation change: on p. 108 the
             2018 file writes the expectation of the squared scaled return as E_b[...] and the
             2020 file writes E[...]. The errata page (http://incompleteideas.net/book/errata.html)
             lists no correction to pp. 103–110.
```

Paraphrase, by locator:

- **Off-policy, target and behavior policy (p. 103).** The policy being learned about is the
  *target policy*. The policy that generates behavior is the *behavior policy*. Learning from data
  "off" the target policy is *off-policy learning*. On-policy methods are the special case in which
  the two policies are the same. Off-policy methods "are often of greater variance and are slower to
  converge". In prediction, π and b are both fixed and given, with b ≠ π.
- **Coverage (p. 103).** To use episodes from b to estimate values for π, every action taken under π
  must be taken at least occasionally under b: π(a|s) > 0 implies b(a|s) > 0. This "is called the
  assumption of coverage." It follows that b must be stochastic wherever it differs from π. π may be
  deterministic, which is the case of interest in control (greedy target, ε-greedy behavior).
- **Importance-sampling ratio (p. 104, eq. 5.3).** The probability of the trajectory
  A_t, S_{t+1}, …, S_T under π is ∏_{k=t}^{T−1} π(A_k|S_k) p(S_{k+1}|S_k, A_k). The ratio
  ρ_{t:T−1} = ∏_{k=t}^{T−1} π(A_k|S_k) / b(A_k|S_k). The transition probabilities appear
  identically in numerator and denominator and cancel, so the ratio depends only on the two
  policies and the sequence, not on the MDP.
- **Why returns need it, and eq. 5.4 (p. 104).** Returns from b have the wrong expectation,
  E[G_t | S_t = s] = v_b(s). The ratio transforms them: E[ρ_{t:T−1} G_t | S_t = s] = v_π(s) (5.4).
  The book states (5.4) and gives no derivation.
- **Ordinary importance sampling (pp. 104–105, eq. 5.5).** Number time steps across episode
  boundaries. Let T(s) be the time steps at which s is visited (first visits only, for a first-visit
  method). V(s) = Σ_{t∈T(s)} ρ_{t:T(t)−1} G_t / |T(s)|. "When importance sampling is done as a
  simple average in this way it is called ordinary importance sampling."
- **Weighted importance sampling (p. 105, eq. 5.6).** V(s) = Σ ρ_{t:T(t)−1} G_t / Σ ρ_{t:T(t)−1},
  "or zero if the denominator is zero."
- **The single-return comparison (p. 105).** With one return, the weighted estimate equals the
  observed return whatever the ratio (if nonzero). Its expectation is v_b(s), not v_π(s), so it is
  biased. The first-visit ordinary estimate is v_π(s) in expectation but can be extreme: with a
  ratio of ten it is ten times the observed return.
- **Bias and variance (p. 105).** For first-visit methods: ordinary IS is unbiased, and weighted IS
  is biased with a bias that "converges asymptotically to zero". Ordinary IS's variance "is in
  general unbounded because the variance of the ratios can be unbounded". In the weighted
  estimator the largest weight on any single return is one. Assuming bounded returns, the weighted
  estimator's variance converges to zero even when the variance of the ratios is infinite (cited
  to Precup, Sutton and Dasgupta 2001). In practice the weighted estimator "usually has
  dramatically lower variance and is strongly preferred". Ordinary IS is kept because it extends
  more easily to function approximation.
- **Every-visit (p. 105).** "The every-visit methods for ordinary and weighed [sic] importance
  sampling are both biased", with the bias falling to zero as samples increase.
- **Example 5.4, blackjack (p. 106).** One state (dealer shows a deuce, player sum 13, usable ace).
  Behavior: hit or stick with equal probability. Target: stick only on 20 or 21. True value
  ≈ −0.27726 (100 million on-policy episodes). Both methods were run 100 times for 10,000 episodes.
  Weighted IS has much lower mean squared error early on (Fig. 5.3). The minus sign was
  confirmed on the rendered page (pdftotext drops it).
- **Example 5.5, setup (pp. 106–107).** One nonterminal state s and two actions. `right` moves
  deterministically to termination with reward 0. `left` returns to s with probability 0.9 (reward
  0), or terminates with probability 0.1 and reward +1. Target π: always `left` (π(left|s) = 1).
  Behavior b: `left` and `right` with probability 1/2 each. γ = 1, so v_π(s) = 1. Ordinary IS
  estimates "will typically have infinite variance ... whenever the scaled returns have infinite
  variance—and this can easily happen in off-policy learning when trajectories contain loops"
  (p. 106).
- **Example 5.5, runs (p. 107, Fig. 5.4).** Ten independent runs of first-visit MC with ordinary IS
  are plotted on a log axis from 1 to 100,000,000 episodes. "Even after millions of episodes, the
  estimates fail to converge to the correct value of 1." Weighted IS gives exactly 1 forever after
  the first episode that ends with `left`. Episodes ending with `right` have ratio zero and enter
  neither the numerator nor the denominator of (5.6).
- **Example 5.5, infinite-variance argument (pp. 107–108).** Var[X] = E[X²] − X̄². With a finite
  mean, the variance is infinite iff E[X²] is. Episodes ending with `right` have ratio 0. Every
  other episode is k loops back to s and then a terminating `left`, with return 1. Summing
  probability × squared ratio over lengths:
  (1/2)(0.1)(1/0.5)² + (1/2)(0.9)(1/2)(0.1)(1/0.5 · 1/0.5)² + … = 0.1 Σ_{k≥0} 0.9^k · 2^k · 2
  = 0.2 Σ_{k≥0} 1.8^k = ∞.
- **Exercise 5.8 (p. 108)** asks whether every-visit MC on Example 5.5 would still have infinite
  variance. It could become a problem on the page, but the problem must be the lesson's own.
- **Section 5.6, incremental implementation (p. 109).** Ordinary IS: scale each return by
  ρ_{t:T(t)−1} and average with the incremental sample-average method, the scaled return in place of
  the reward. Weighted IS: for returns G_1, …, G_{n−1} from one state with weights W_i (e.g.
  W_i = ρ_{t_i:T(t_i)−1}), V_n = Σ_{k=1}^{n−1} W_k G_k / Σ_{k=1}^{n−1} W_k, n ≥ 2 (5.7). Update:
  V_{n+1} = V_n + (W_n / C_n)[G_n − V_n], n ≥ 1 (5.8), and C_{n+1} = C_n + W_{n+1}, C_0 = 0.
- **Box, "Off-policy MC prediction (policy evaluation) for estimating Q ≈ q_π" (p. 110).** Target
  π arbitrary. Q arbitrary and C(s, a) = 0 at the start. Each episode: b is any policy with
  coverage of π. Generate S_0, A_0, R_1, …, S_{T−1}, A_{T−1}, R_T under b. Set G ← 0 and W ← 1. Then
  for t = T−1 down to 0, while W ≠ 0: G ← γG + R_{t+1}; C(S_t, A_t) ← C(S_t, A_t) + W;
  Q(S_t, A_t) ← Q(S_t, A_t) + (W / C(S_t, A_t))[G − Q(S_t, A_t)]; W ← W π(A_t|S_t)/b(A_t|S_t).
  This is every-visit, weighted, and for action values. W is updated after Q, so a pair's weight
  covers only the actions after it. With π = b, W is always 1. Q converges to q_π for all
  encountered pairs (p. 109).
- **Summary (p. 116).** "Ordinary importance sampling produces unbiased estimates, but has larger,
  possibly infinite, variance, whereas weighted importance sampling always has finite variance and
  is preferred in practice."
- **Remarks (p. 117).** 5.5: "Off-policy methods using importance sampling have a long history and
  yet still are not well understood." Weighted IS, "also sometimes called normalized importance
  sampling", is discussed by Rubinstein (1981), Hesterberg (1988), Shelton (2001) and Liu (2001).
  The target policy was called the "estimation" policy in the first edition. 5.9: "Per-decision
  importance sampling was introduced by Precup, Sutton, and Singh (2000)."
- **Pointer for Q-learning (pp. 149, 152).** Section 7.3, p. 149, on n-step off-policy Sarsa (7.11):
  the ratio "starts and ends one step later" for action values because "We do not have to care how
  likely we were to select the action; now that we have selected it we want to learn fully from
  what happens, with importance sampling only for subsequent actions." Section 7.5, p. 152: "Is
  off-policy learning possible without importance sampling? Q-learning and Expected Sarsa from
  Chapter 6 do this for the one-step case". This is the textbook locator for the one-sentence
  pointer the commission allows.
- **License (front matter, PDF p. 4).** © 2018, 2020 Sutton and Barto, Creative Commons
  Attribution-NonCommercial-NoDerivs 2.0 Generic.

Quote (evidence for Contradiction 3): Fig. 5.4 caption, p. 107: "The correct estimate here is 1
(γ = 1), and, even though this is the expected value of a sample return (after importance
sampling), the variance of the samples is infinite, and the estimates do not converge to this
value. These results are for off-policy first-visit MC."

### Sutton and Barto, Reinforcement Learning: An Introduction, 1st edition (1998), Section 5.5

```text
URL:         http://incompleteideas.net/book/first/ebook/node55.html
             (authors' site, HTML of the 1998 edition; page footer "Mark Lee 2005-01-04";
             book index http://incompleteideas.net/book/first/ebook/the-book.html)
Kind:        primary. It is the authors' own 1998 statement of the method. Precup, Sutton and Singh
             (2000) credit it.
Establishes: firsthand: by 1998 the textbook weighted each return by the ratio of its trajectory's
             probabilities under the two policies and averaged with those weights. That is the
             weighted (normalized) estimator. The book also required coverage.
Paraphrase:  Section 5.5, "Evaluating One Policy While Following Another". To use episodes from π'
             to estimate values for π, every action taken under π must be taken at least
             occasionally under π': π(s,a) > 0 implies π'(s,a) > 0. Eq. (5.3):
             V(s) = Σ_{i=1}^{n_s} (p_i(s)/p'_i(s)) R_i(s) / Σ_{i=1}^{n_s} (p_i(s)/p'_i(s)), where
             p_i, p'_i are the probabilities of the sequence after the i-th first visit under π and
             π'. The ratio p_i/p'_i = ∏_{k=t}^{T_i(s)−1} π(s_k,a_k)/π'(s_k,a_k) needs no knowledge of
             the environment's dynamics. Behavior policy written π', not b. Exercise 5.3 asks for the
             action-value version.
Locators:    Section 5.5 (single HTML page), eq. (5.3) and the two displayed equations after it.
             Equation images numeqtmp25.png and imgtmp38.png on that page were opened to read
             the math. No printed page numbers are available from this source.
Quote:       "To average these to obtain an unbiased estimate of V^π(s), we need only weight each
             return by its relative probability of occurring under π and π'" (this wording is
             itself evidence: the 1998 text calls the weighted estimate unbiased, which the 2nd
             edition, p. 105, contradicts; see Contradictions).
```

### Precup, Sutton and Singh, "Eligibility Traces for Off-Policy Policy Evaluation" (2000)

```text
URL:         http://incompleteideas.net/papers/PSS-00.pdf  (8-page PDF on Sutton's site).
             Institutional record: https://hdl.handle.net/20.500.14394/10401 (resolves to UMass
             ScholarWorks; its metadata gives title, the three authors and year 2000, with no
             page range). Venue and pages from Sutton and Barto's reference list: Proceedings of
             the 17th International Conference on Machine Learning, pp. 759–766, Morgan Kaufmann.
Kind:        primary for its own estimators, Theorem 1 and per-decision IS. The authors defined
             them. It repeats Rubinstein (1981) for the classical unbiasedness and consistency of
             IS, and Sutton and Barto (1998) for the weighted estimator.
Establishes: firsthand: the off-policy policy-evaluation problem as stated, the first-visit
             action-value estimators Q^IS (eq. 2) and Q^ISW (eq. 3), the per-decision estimator and
             Theorem 1. It also records that the authors knew of only one prior multi-step method,
             the weighted MC method in Sutton & Barto (1998).
Paraphrase:  p. 1 (proc. p. 759): off-policy learning means learning about a policy other than
             the one followed. "1-step Q-learning is often used in an off-policy manner, learning
             about the greedy policy while the data is generated by a slightly randomized policy".
             The behavior policy must be soft (b(s,a) > 0 for all s, a), a stronger condition than
             coverage. p. 2 (proc. p. 760): Watkins's, Peng's and naive Q(λ) apply only when the
             target is deterministic and changing. Section 2, "Importance Sampling Algorithms":
             E_d{x} = ∫ x (d(x)/d'(x)) d'(x) dx = E_{d'}{x d(x)/d'(x)}, giving estimator (1),
             (1/n) Σ x_i d(x_i)/d'(x_i). It is consistent and unbiased (Rubinstein 1981). The
             weighted estimator Σ x_i w_i / Σ w_i is "consistent but biased" (p. 3, citing
             Rubinstein). It is "often faster and more stable in practice", because a rare event's
             large weight also appears in the denominator. p. 3 (proc. p. 761): first-visit
             IS estimator Q^IS(s,a) = (1/M) Σ_m R_m w_m (2), with
             w_m = ∏_{i=t_m+1}^{T_m−1} π_i/b_i. The product starts at t_m + 1, after the action a
             being evaluated. Weighted: Q^ISW(s,a) = Σ R_m w_m / Σ w_m (3), "(Sutton & Barto, 1998)".
             Section 3 introduces the per-decision estimator Q^PD. Theorem 1 says it is consistent
             and unbiased. Its weighted version is consistent but biased.
Locators:    PDF pp. 1–3 (no printed page numbers on the PDF; proceedings pages inferred as
             759 + PDF page − 1). Section 2 begins top right of p. 2; eqs. (2), (3) left column
             p. 3; Section 3 and Theorem 1 p. 3.
Quote:       p. 2: "The only prior method we know of that uses multi-step transitions appropriately
             is the weighted Monte Carlo method described briefly by Sutton and Barto (1998)."
             (evidence for the attribution question in Contradictions.)
```

### Precup, Sutton and Dasgupta, "Off-Policy Temporal-Difference Learning with Function Approximation" (2001)

```text
URL:         http://incompleteideas.net/papers/PSD-01.pdf  (states on p. 1: "a digitally remastered
             version of a paper published in the Proceedings of the 18th International Conference
             on Machine Learning (2001), pp. 417–424 ... otherwise identical to the published
             article").
Kind:        primary. It owns Theorem 7, the result Sutton and Barto cite on p. 105 for
             weighted-IS variance going to zero.
Establishes: firsthand: Theorem 7 and its proof, and the statement that the tabular ordinary
             estimator converges with probability 1 by the law of large numbers when returns are
             bounded, while its variance can be unbounded.
Paraphrase:  Section 6, "Possibility of Weighted Importance Sampling Methods". Weighted IS is
             "widely known to produce lower variance estimates than conventional importance
             sampling, at the cost of introducing transient bias (bias that decreases to zero as
             the number of samples increases to infinity)". The tabular estimator Q^IS_N =
             (1/N) Σ R_i w_i, with w_i = ρ_{t+1} ⋯ ρ_{T−1}, satisfies E_b{R_i w_i} = Q^π(s,a). Theorem
             7: for γ < 1, var(Q^ISW_N) goes to zero as N → ∞. The proof: |Q^ISW_N| is at most the
             largest |R_i|, which is below r_max/(1 − γ) for bounded rewards. Q^ISW_N converges in
             probability, and Theorem 6 then gives vanishing variance. "The same cannot be said for
             the conventional importance sampling algorithm."
Locators:    PDF p. 7 (proceedings p. 423), Section 6, Theorems 5–7.
Quote:       p. 7: "By the law of large numbers, Q^IS_N converges w.p.1 to Q^π(s,a), if the R_i are
             bounded. But the w_i might have infinite variance, and so Q^IS_N might also have
             unbounded variance." (evidence against the Fig. 5.4 caption; see Contradictions.)
```

### The course's published lessons (via `nb history --show reinforcement-learning/<slug>`)

These are the paper's own published record. They are primary for what the course has taught and
printed. Lessons link one another inside the library as `../reinforcement-learning/<slug>.html`
(read from the `href`s in `sarsa-and-q-learning.html` in the library checkout). Every listing below
is printed in full in the lesson named, and runs with `uv run` from one folder that also holds its
imports. Titles are the published headlines.

```text
URL:         ../reinforcement-learning/sarsa-and-q-learning.html
             "Moving at random half the time, Q-learning still learns the optimal arrows" (2026-11-05)
Kind:        primary (the course's own published lesson)
Establishes: what the course has already defined about off-policy learning, and td_control.py.
Paraphrase:  Section "Learning about the greedy policy while following the ε-greedy one" defines:
             control is on-policy when the agent learns the action values of the policy that makes
             its moves (SARSA). Q-learning learns the greedy policy's action values while the
             ε-greedy policy makes the moves. "The policy being learned about is called the target
             policy, and the policy that generates the moves is called the behavior policy." "A
             method whose two policies differ is off-policy." Both cite Sutton and Barto. Section
             "What each target averages to" derives that Q-learning's average target "contains no
             π", so its estimates can rest only at q_* whatever policy makes the moves. Link this
             section for the commission's one-sentence pointer on why one-step Q-learning needs no
             ratio. Problem 1 gives the ε-greedy probabilities at ε = 0.5: greedy move 0.625, each
             other 0.125. The lesson never mentions importance sampling, a ratio or coverage.
             Notation hazard: in "The update rules differ in one term" the lesson writes "Call b
             the move in the next cell whose estimate enters the target". This lesson will use b
             for the behavior policy.
             Code: td_control.py: choose(Q, s, eps, rng) -> eps-greedy move;
             td_control(eps, episodes, rng, target="sarsa", watch=None) -> Q (N x 4). targets.py
             (has a __main__ guard, so it can be imported): value_of(arrows, eps) -> exact per-cell
             value of the eps-greedy policy around `arrows`; runs(target); main().
Locators:    sections "Learning about the greedy policy while following the ε-greedy one",
             "What each target averages to", "The update rules differ in one term"; Problem 1.
```

```text
URL:         ../reinforcement-learning/epsilon-greedy-exploration.html
             "ε-greedy control settles for the best policy that keeps exploring" (2026-11-04)
Kind:        primary (course lesson)
Establishes: the ε-greedy probabilities, ε-soft, on-policy, and soft_control.py / exploration.py.
Paraphrase:  π(a|s) = 1 − ε + ε/|A(s)| for the greedy move a*, ε/|A(s)| otherwise. With four moves
             and ε = 0.1: 0.925 and 0.025. "A policy that gives every move in every cell at least
             ε/|A(s)| is called ε-soft." "Control of this kind is called on-policy." So any ε-soft
             behavior with ε > 0 covers every target on this grid.
             Code: soft_control.py: soft_play(policy, eps, start, rng) -> steps
             [(cell, move, reward, next cell)] under the eps-greedy policy around `policy`, capped at
             CAP = 200 moves; soft_control(policy, eps, episodes, rng, watch=None);
             best_soft(eps, tol=1e-10) -> (v, q), exact best eps-soft values (eps = 0 gives v_*, q_*).
             exploration.py: best_moves(eps) -> {cell: set of tied best moves}.
Locators:    the ε-greedy policy equation and the paragraph after it; soft_control.py listing.
```

```text
URL:         ../reinforcement-learning/learning-values-from-samples.html
             "An agent can learn what each state is worth without knowing the rules" (2026-11-02)
Kind:        primary (course lesson)
Establishes: GAMMA, the running-mean form of Monte Carlo, first-visit unbiasedness, and the grid.
Paraphrase:  Grid: 4×4, cells 0–15 row by row from the top left. Goal = cell 3, +10 on arrival.
             Pit = cell 6, −20 on arrival. Every other arrival −1. Goal and pit end the episode.
             The aimed move succeeds with probability 0.8, and the move turns a quarter turn to
             each side with 0.1 each. A move into an edge stays put. γ = 0.9. Exact v of the
             hand-drawn policy PI, cells 0–15: [2.16, 4.04, 6.48, 0, 0.61, 0.06, 0, 6.48,
             −0.72, −1.03, −0.10, 4.02, −1.86, −2.01, −1.08, 1.98]. Cell 13 = −2.01, with about 80% of
             episodes reaching the goal (mean return +1.67) and 20% the pit (−16.78). The running
             mean V_n = V_{n−1} + (1/n)[G_n − V_{n−1}] is derived. First-visit returns are unbiased,
             and every-visit is biased with few episodes. The standard deviation of one on-policy
             return from cell 13 is 7.57 in the prose. The sampled figure printed by compare.py is
             7.58 from 50,000 returns, and the exact table prints 7.57.
             Code: estimators.py: GAMMA = 0.9; first_visit_mc(steps, V, count, step=None);
             every_visit_mc(steps, V, count); td0(steps, V, count, step=None, decay=0.7). Steps are
             (cell, action, reward, next cell). first_visit_mc computes G itself from the rewards,
             so it cannot take a ratio. An IS estimator needs its own code. compare.py:
             exact_values() -> per-cell v_PI (has a __main__ guard).
Locators:    "The test problem is a grid whose exact values are known"; "Monte Carlo waits for the
             episode to end"; "First visits and every visit"; estimators.py listing; compare.py
             output.
```

```text
URL:         ../reinforcement-learning/checking-a-custom-environment.html
             "Gymnasium's environment checker passes a grid with a backward slip" (2026-11-07)
Kind:        primary (course lesson)
Establishes: baselines.py, including exact_value; the baseline values.
Paraphrase:  baselines.py (deps gymnasium==1.4.0, numpy): random_policy(obs, rng) -> uniform move;
             hand_drawn(obs, rng) -> PI[obs]; exact_value(probs) -> the MEAN of v_π over the 14
             cells reset starts from, where probs[s, a] is any (stochastic) policy table, solved
             from the rules, never from the environment; EXACT = {"random": −10.90,
             "hand-drawn": 1.36}; returns(env, policy, episodes, seed, watch=None) -> array of
             discounted returns at GAMMA from env.reset starts. exact_value returns a scalar, not
             per-cell values. Policies here have the signature policy(obs, rng). The lesson spells
             "behaviour" (behaviour.py, "by behaviour"), while the SARSA lesson writes "behavior
             policy".
Locators:    "The rules fix what each baseline should earn"; baselines.py listing.
```

```text
URL:         ../reinforcement-learning/training-an-off-the-shelf-agent.html
             "PPO's greedy arrows outscore the sampled moves its training curve averages" (2026-11-08)
Kind:        primary (course lesson)
Establishes: the optimal value and how a later lesson used exact_value on a stochastic table.
Paraphrase:  seeds.py prints "exact values: random -10.90, hand-drawn 1.36, optimal 1.61". It
             computes q_star = action_values(value_iteration(1e-12)[0], transitions(SLIP)). price.py
             scores the ε-greedy policy around the optimal arrows with exact_value((1 − EPS) *
             arrows + EPS / 4). At ε = 0.05 it is worth 1.08, 0.53 below optimal. agent.py and
             seeds.py need stable-baselines3/torch and are not relevant to this lesson.
Locators:    seeds.py output; Problem 1 (price.py).
```

Files printed in other lessons, which the four lessons above import. I read only their listings,
to record exact signatures. This goes slightly beyond the four lessons the brief named; see the
question for the orchestrator.

```text
URL:         ../reinforcement-learning/environments-and-the-rl-problem.html
             "The value of a state is an average you can solve for" (2026-10-31)
Kind:        primary (course lesson)
Establishes: gridworld.py; the spectral radius ρ(Q) of the hand-drawn policy.
Paraphrase:  gridworld.py: N = 16; GOAL, PIT = 3, 6; TERMINAL = [3, 6]; ARROWS = "^>v<" (moves 0–3 =
             up, right, down, left); R[s'] reward for arriving in s'; draw(rows); PI (hand-drawn
             arrows: "> > > . / ^ ^ . ^ / ^ ^ > ^ / ^ ^ ^ ^"); STUCK; move(s, a);
             transitions(slip) -> P[s, a, s'] with zero rows for terminals;
             fixed_policy(policy, slip) -> (Q, b) for a deterministic policy array, terminal
             columns of Q zeroed; episode(P, policy, start, rng) -> [(cell, intended action,
             reward, next cell)], uncapped, deterministic policy array; discounted(steps, gamma);
             radius(A). Lesson 1 printed "gamma 1.0: rho 0.4894" for Q = fixed_policy(PI, 0.2)[0],
             and it uses ρ(Q) for the spectral radius. That symbol clashes with S&B's ρ for the
             ratio.
Locators:    gridworld.py listing; evaluate.py output line "gamma 1.0: rho 0.4894".
```

```text
URL:         ../reinforcement-learning/action-values-from-samples.html
             "Action values let an agent improve its policy from episodes alone" (2026-11-03)
Kind:        primary (course lesson)
Establishes: mc_control.py; the optimal arrows.
Paraphrase:  mc_control.py: SLIP = 0.2; LIVE (14 non-terminal cells); CAP = 200; step(s, a, rng) ->
             (reward, next cell), the environment, which samples the slip; play(policy, start, first,
             rng); pairs(steps) (pair index 4 * cell + move); greedy(q, count, policy);
             control(...). experiment.py draws the optimal arrows PI_STAR as "> > > . / ^ ^ . ^ /
             ^ ^ > ^ / ^ > > ^" (up and right tie at cells 9 and 12).
Locators:    mc_control.py listing; experiment.py header.
```

```text
URL:         ../reinforcement-learning/finding-optimal-policies.html
             "Two improvements find the best policy" (2026-11-01)
Kind:        primary (course lesson)
Establishes: control.py.
Paraphrase:  control.py defines its own GAMMA, SLIP = 0.9, 0.2 and LIVE. evaluate(policy) ->
             per-cell v for a deterministic policy array. action_values(v, P) -> q[s, a].
             greedy(v, P, old, tol=1e-9); policy_iteration(start) (prints);
             value_iteration(tol) -> (v, sweeps, trace13). The file has a __main__ guard.
Locators:    control.py listing.
```

```text
URL:         ../reinforcement-learning/termination-and-truncation.html
             "Q-learning that treats its time limit as terminal learns the values of a different
             grid" (2026-11-06)
Kind:        primary (course lesson)
Establishes: grid_env.py (SlipperyGrid) and the terminated/truncated distinction.
Paraphrase:  grid_env.py (deps gymnasium==1.4.0, numpy): SlipperyGrid(gym.Env), with observation
             Discrete(16) and action Discrete(4). reset(seed=None, options={"start": s}) picks a
             random LIVE cell by default. step(action) -> (cell, float reward, terminated, False,
             {}). TimeLimit sets truncated. Relevant here because a cut episode has no full return,
             and an importance-sampled return from a cut episode is no longer unbiased.
Locators:    grid_env.py listing.
```

## Contradictions

1. **Ordinary IS's convergence in Example 5.5.** Sutton and Barto's Fig. 5.4 caption (p. 107) says
   the ordinary estimates "do not converge to this value", and the text says that "even after
   millions of episodes, the estimates fail to converge". Precup, Sutton and Dasgupta (2001, p. 7)
   state that the ordinary tabular estimator "converges w.p.1 ... if the R_i are bounded", while
   its variance may be unbounded. In Example 5.5 returns are 0 or 1 and E_b[ρG] = 1 is finite. The
   strong law of large numbers needs only a finite mean, so the average converges with probability
   1. The infinite variance removes the 1/√n error rate. The text's "even after millions of
   episodes" describes the ten plotted runs and is correct as an observation. The caption's "do not
   converge", read as a limit statement, is wrong. The lesson can say the variance is infinite, so
   no number of episodes gives the estimate a finite standard error, and its runs still jump after
   millions of episodes. It should not say the estimate never converges. Researcher's derivation,
   not from a source, for the writer to check if used: X = ρG takes the value 2^{k+1} with
   probability 0.05 · 0.45^k (k loops, then `left` to termination), so P(X ≥ x) falls as
   x^{−1.152} (exponent log₂(1/0.45)). A tail exponent between 1 and 2 means a finite mean and
   infinite variance. The error of the n-episode mean then shrinks only about as n^{−0.13}.
2. **What causes infinite variance.** The commission says "with long episodes or a target far from
   the behavior, the ordinary estimator's variance can be infinite". Sutton and Barto (p. 106) put
   the cause in loops: infinite variance "can easily happen in off-policy learning when
   trajectories contain loops". If episodes have a bounded length T_max and every ratio π/b is
   finite, ρ is bounded by (max π/b)^{T_max}. The variance is then finite, though it can grow
   exponentially with T_max. Infinite variance needs episode lengths without bound, with the
   per-step ratio large enough against the probability of continuing. In Example 5.5 the sum is
   0.2 Σ 1.8^k, where 1.8 = 2 (the ratio per `left`) × 0.9 (the probability of looping), and it
   diverges because 1.8 ≥ 1. The researcher check under Numbers finds the same structure on the
   course's grid. Behavior must be far enough from the target relative to how long episodes run.
   Distance alone is not enough. A course cap of CAP = 200 moves (mc_control, soft_play,
   TimeLimit) makes every variance finite in principle. It also biases the estimator whenever it
   cuts an episode.
3. **"Ordinary IS is unbiased" holds for the first-visit estimator only.** Sutton and Barto, p. 105:
   every-visit ordinary and weighted IS "are both biased". The derivation of (5.4) applies to the
   first-visit return, or to the return of an episode from its start state. The lesson's estimator
   must be first-visit, or start every episode in the evaluated cell, for the unbiasedness claim and
   its run to agree. The p. 110 box is every-visit and weighted.
4. **Weighted IS: "bounded variance" needs bounded returns.** Sutton and Barto p. 105 qualify it
   ("assuming bounded returns"), and the Summary (p. 116) says "always has finite variance" with no
   qualification. PSD 2001 proves vanishing variance for γ < 1 with bounded rewards. The proof's
   key step, |weighted estimate| ≤ max |G|, holds for any bounded returns. That covers Example 5.5
   (γ = 1, returns 0 or 1) and the course grid (γ = 0.9). The commission's claim holds for both.
5. **1998 vs 2018 on weighted IS's bias.** The 1998 first edition (Section 5.5) introduces the
   weighted estimate (5.3) as "an unbiased estimate of V^π(s)". The second edition (p. 105)
   corrects this: weighted IS is biased, with expectation v_b(s) after one return. Do not cite the
   first edition for estimator properties.
6. **Who introduced importance sampling for off-policy evaluation.** The brief suggests Precup,
   Sutton and Singh (2000). That paper (p. 2) calls the "weighted Monte Carlo method described
   briefly by Sutton and Barto (1998)" the only prior multi-step method they knew. The second
   edition's remarks (p. 117) say IS off-policy methods "have a long history" without naming an
   originator, and credit PSS 2000 only with per-decision IS (5.9). The series prompt says to link
   the paper that introduced an idea "when one clearly did". None clearly did. Defensible
   phrasing: "Sutton and Barto's 1998 textbook already weighted returns this way. Precup, Sutton
   and Singh (2000) set out the ordinary and weighted estimators side by side for off-policy
   evaluation" (eqs. 2–3, p. 3).
7. **Course notation vs the source.** Sutton and Barto write b for the behavior policy and ρ for the
   ratio. The SARSA lesson used b for "the move in the next cell whose estimate enters the target".
   Lesson 1 used ρ(Q) for the spectral radius, and this lesson may need the spectral radius (see
   Numbers). The writer has to introduce b and ρ afresh and choose how to name the spectral radius
   if it appears. Spelling also differs between lessons ("behavior policy" in the SARSA lesson,
   "behaviour" in the checking lesson).
8. **Coverage vs softness.** Sutton and Barto require coverage only (π(a|s) > 0 ⇒ b(a|s) > 0).
   PSS 2000 require a soft behavior policy (b(s,a) > 0 everywhere). These do not conflict: softness
   implies coverage of every target. Coverage is what the derivation uses. It is not about avoiding
   division by zero, since b took every observed action with positive probability. It ensures that
   no trajectory π can produce is missing from the sum under b (see Limits).

## Numbers

```text
Figure: Example 5.5: P(left loops back to s) = 0.9, reward 0; P(left terminates) = 0.1, reward +1;
        right terminates, reward 0; π(left|s) = 1; b(left|s) = b(right|s) = 1/2; γ = 1; v_π(s) = 1
Owner:  Sutton and Barto 2nd ed., Example 5.5, pp. 106–107
Scope:  one nonterminal state, per episode
```

```text
Figure: E[(ρG)²] = 0.1 Σ_{k≥0} 0.9^k · 2^k · 2 = 0.2 Σ_{k≥0} 1.8^k = ∞
Owner:  Sutton and Barto 2nd ed., p. 108
Scope:  one episode under b, first-visit scaled return from s
```

```text
Figure: Fig. 5.4: 10 independent runs of first-visit ordinary IS, x-axis 1 to 100,000,000 episodes
        (log scale), y-axis 0 to 2, dotted line at the true value 1
Owner:  Sutton and Barto 2nd ed., Fig. 5.4, p. 107
Scope:  the plotted runs only; no table of values
```

```text
Figure: Example 5.5 derived (researcher, from the book's setup; writer to reproduce): an episode with
        k loops then a terminating left has b-probability 0.05 × 0.45^k and ratio 2^{k+1}; share of
        b-episodes with nonzero ratio = 0.05 / 0.55 = 1/11 ≈ 0.091; E_b[ρG] = 1.000; tail exponent
        log₂(1/0.45) = 1.152
Owner:  researcher's computation (scratch script), not a source
Scope:  per episode under b
```

```text
Figure: Example 5.4: true value ≈ −0.27726 (sign checked on the rendered page); 100 runs ×
        10,000 episodes
Owner:  Sutton and Barto 2nd ed., p. 106
Scope:  one blackjack state; not needed unless the writer mentions it
```

```text
Figure: ε-greedy move probabilities with 4 moves: ε = 0.1 → greedy 0.925, other 0.025;
        ε = 0.5 → greedy 0.625, other 0.125
Owner:  course: epsilon-greedy-exploration (equation and paragraph after); sarsa-and-q-learning
        Problem 1
Scope:  per cell
```

```text
Figure: per-step ratio for a greedy (deterministic) target and an ε-greedy behavior around the same
        arrows: 1/(1 − ε + ε/4) on the target's move, 0 otherwise; = 1.0811 at ε = 0.1,
        1.2903 at ε = 0.3, 1.6000 at ε = 0.5, 4 for uniform random behavior
Owner:  arithmetic from the two rows above and S&B eq. 5.3
Scope:  per step on which the agent makes the target's move
```

```text
Figure: hand-drawn policy PI, exact values: v(13) = −2.01; mean over the 14 start cells 1.36;
        random moves −10.90; optimal arrows 1.61
Owner:  course: learning-values-from-samples (compare.py output); checking-a-custom-environment
        (baselines.EXACT); training-an-off-the-shelf-agent (seeds.py output)
Scope:  γ = 0.9, slip 0.2; the 14-cell means are uniform over reset's start cells
```

```text
Figure: sd of one on-policy return from cell 13 under PI: 7.57 (exact table), 7.58 (50,000 samples)
Owner:  course: learning-values-from-samples (compare.py output)
Scope:  γ = 0.9; baseline for how much ratios inflate the spread
```

```text
Figure: spectral radius of Q for PI at slip 0.2, γ = 1: 0.4894
Owner:  course: environments-and-the-rl-problem (evaluate.py output "gamma 1.0: rho 0.4894");
        reproduced by the researcher check
Scope:  Q = fixed_policy(PI, 0.2)[0], non-terminal-to-non-terminal moves
```

```text
Figure: researcher check, not a source (scratch script rebuilt from the printed gridworld.py).
        Target PI, behavior ε-greedy around PI. E_b[(ρG)²] from any cell is infinite exactly
        when the spectral radius of c·Q is ≥ 1, with c = 1/(1 − 3ε/4) and Q as above. The
        reason: every reward on the grid has magnitude ≥ 1, so E_b[(ρG)²] ≥ E_b[ρ²] =
        E_π[ρ]. The radius equals c × 0.4894, so the threshold is ε* = 0.681.
        sd of ρG from cell 13: ε = 0.1 → 9.24; ε = 0.3 → 15.25; ε = 0.5 → 34.48; ε = 0.6 → 78.70;
        ε = 0.68 → 1603; ε ≥ 0.681, including uniform random behavior (radius 4 × 0.4894 = 1.958)
        → infinite.
        Simulation check, 200,000 episodes from cell 13, seed 0: ε = 0.3 → mean ρG −1.97
        (exact −2.005), sd 15.06, 23.8% of episodes with nonzero ratio; ε = 0.5 → mean −2.00,
        sd 31.79 (heavy tail, sample sd below the exact 34.48), 8.0% nonzero.
Owner:  researcher's computation; the writer must reproduce any figure used, in the lesson's code
Scope:  γ = 0.9, slip 0.2, start cell 13, episodes uncapped
```

The same structure links both cases. In Example 5.5, 1.8 = 2 × 0.9 is (ratio per step) ×
(probability of continuing). On the grid it is c × ρ(Q). Uniform random behavior, the course's
`random_policy` baseline, gives ordinary IS infinite variance for the hand-drawn target.

## Limits

- Sutton and Barto give (5.4) without a proof. The full unbiasedness derivation must be the
  writer's. It sums over trajectories, cancels the transition probabilities, and uses coverage to
  show the sum under b reaches every trajectory π can produce. A run checks it. No source needs to
  be cited for the derivation.
- Coverage's role: no source states the failure mode in one sentence. The 2nd edition (p. 103)
  states the requirement. The derivation shows the consequence. Without coverage, E_b[ρG] sums
  only over trajectories b can produce, so the estimate converges to the wrong value with no
  warning. Where b(a|s) = 0, the episodes with that action never occur, so no ratio is ever
  undefined. If the writer makes this claim, it needs a run.
- Priority before 1998 was not established. I did not search the pre-1998 RL literature or open
  Rubinstein (1981), Hesterberg (1988), Kahn and Marshall, or other statistics sources for classical
  importance sampling. Both Sutton and Barto and PSS 2000 cite Rubinstein (1981) for it.
- The MIT Press page returned 403 to a plain request and I did not open it. Edition, publisher and
  year come from the authors' book page. The course already cites the MIT Press URL.
- The PSS 2000 PDF prints no page numbers. The proceedings range 759–766 comes from Sutton and
  Barto's reference list (dblp served a bot challenge). The per-page mapping (PDF p. 2 = p. 760,
  p. 3 = p. 761) is inferred.
- The first edition is cited from its HTML conversion: section 5.5 and equation (5.3), with no
  printed page.
- All variance thresholds and standard deviations for the course grid come from a researcher check,
  not a source. The writer must reproduce any of them in the lesson's code before using it.
- No course function computes ratios. first_visit_mc builds G internally. exact_value returns
  only the 14-cell mean, so per-cell truth needs control.evaluate(policy) for a deterministic
  target, targets.value_of(arrows, eps) for an ε-greedy one, or the einsum lines inside
  exact_value. Episodes from soft_play, mc_control.play or a TimeLimit are capped at 200 moves.
  The checking lesson's random episodes on the correct grid hit that cap 0 times in 4,000, but a cut
  episode breaks the unbiasedness the lesson derives. gridworld.episode is uncapped but takes only
  a deterministic policy array.
- The ratio uses the action the agent chose (the aim), not the direction a slip moved it. The course
  step tuples store the intended move ("(cell, intended action, reward, next cell)" in
  gridworld.episode), which is the right input. The slip probabilities cancel as in eq. 5.3.
- Section 5.6's index convention (C_{n+1} = C_n + W_{n+1}, update with W_n / C_n) is as printed. A
  writer who uses (5.8) should check the indices against a run. A simpler equivalent is the
  course's running mean with step W/C in place of 1/n.

## Source assets

```text
Asset: Sutton and Barto 2nd ed., Figure 5.4, p. 107 (PDF p. 129): ten ordinary-IS runs on a log
       axis from 1 to 10^8 episodes, with the one-state MDP inset (left/right, 0.9 loop,
       0.1 to termination with R = +1, π(left|s) = 1, b(left|s) = 1/2)
Shows: estimates that jump far above 1 and are still drifting after millions of episodes, beside
       the exact MDP that produces them
Crop:  must keep the inset with both policy labels, the y-axis label "(ten runs)", the dotted
       line at 1, and the log-scale x-axis label; the caption's "first-visit MC" matters. The
       PDF is CC BY-NC-ND 2.0 (front matter, PDF p. 4). The series prompt prefers the lesson's
       own runs as inline SVG, and the inset is simple enough to redraw.
```

```text
Asset: Sutton and Barto 2nd ed., Figure 5.3, p. 106: mean squared error of ordinary vs weighted IS
       on one blackjack state, 100 runs, 1 to 10,000 episodes (log scale)
Shows: weighted IS's lower early error on a case where both have finite variance
Crop:  keep both curve labels and the "(average over 100 runs)" axis note. Optional; it duplicates
       what a lesson run on the grid would show.
```

```text
Asset: Sutton and Barto 2nd ed., box "Off-policy MC prediction (policy evaluation) for estimating
       Q ≈ q_π", p. 110
Shows: the incremental weighted update and the backward loop where W stops at 0
Crop:  pseudocode, not a visual argument; a listing in the lesson's own code does this better.
```

```text
Asset: Precup, Sutton and Singh 2000, Figure 1, p. 2: a target distribution d (a bump) over a flat
       sampling distribution d'
Shows: the generic importance-sampling picture, nothing specific to RL
Crop:  None recommended.
```

Precup, Sutton and Dasgupta 2001: None found for this lesson.
Sutton and Barto 1st ed. Section 5.5: None found.

## Discarded

```text
https://dblp.org/rec/conf/icml/PrecupSS00.html: served a bot-challenge page; the page range it
  would confirm comes from Sutton and Barto's reference list instead.
https://scholarworks.umass.edu/cs_faculty_pubs/80/: reached, but its HTML carries only citation
  metadata (title, authors, 2000) and no venue or pages; recorded only as the institutional handle
  https://hdl.handle.net/20.500.14394/10401.
```
