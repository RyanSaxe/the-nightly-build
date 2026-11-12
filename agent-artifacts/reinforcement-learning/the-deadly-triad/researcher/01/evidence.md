# Evidence: reinforcement-learning/the-deadly-triad (researcher 01)

The sources support the lesson's core: Sutton and Barto (2nd ed.) give the
off-policy semi-gradient TD(0) update with the per-step ratio (eq. 11.1 and
11.2, p. 258), the w-to-2w fragment with its one-line derivation (p. 260),
Baird's counterexample fully specified (pp. 261 to 262, Figures 11.1 and 11.2:
seven states, eight weights, b(dashed) = 6/7, pi(solid) = 1, gamma = 0.99,
alpha = 0.01, w0 = (1,1,1,1,1,1,10,1)), and the triad on pp. 264 to 265. I
reproduced the book's semi-gradient DP panel numerically (w8 = 335.0 and
w1..w6 = 114.4 after 1,000 sweeps), so the writer has a figure to check runs
against. The evidence is thin or contrary in four places. First, the commission
names Baird's counterexample "Example 11.1". In the book, Example 11.1 is
Tsitsiklis and Van Roy's counterexample (p. 263), and Baird's appears in Figures
11.1 and 11.2. Second, the book claims less than the commission's one idea. Its
words are that with any two of the three, "instability can be avoided" (p. 264),
not that the weights must stay bounded. The book's own guarantee covers linear
features, and Tsitsiklis and Van Roy (1997, Section X) show on-policy TD(0) with
a nonlinear approximator diverging. Third, on Baird's problem two of the three
removals are only marginally stable: the expected-update matrix has a zero
eigenvalue, and on-policy weighting puts all its mass on state 7, so the weights
stay bounded but most of them never move. Fourth, the book calls the task
"episodic" but draws no terminal state, and its Figure 11.1 caption says each
action "usually" leads to its states.

## Sources

### S1. Sutton and Barto, Reinforcement Learning: An Introduction, 2nd ed.

```text
URL:         http://incompleteideas.net/book/RLbook2020.pdf
             (linked as "Full Pdf" from http://incompleteideas.net/book/the-book-2nd.html;
             the 2018 printing is also served at http://incompleteideas.net/book/RLbook2018.pdf)
Kind:        primary. The authors' own text: they define the algorithms, built the
             book's version of Baird's example, named the triad (bib note p. 285:
             "The name 'deadly triad' is due to Sutton (2015a)") and ran Figure 11.2.
Establishes: firsthand: the off-policy semi-gradient update, the w-to-2w fragment,
             the full spec of the book's Baird variant, the reported divergence
             figure, the statement of the triad and the argument for which leg to
             give up. It only repeats Baird (1995) and Tsitsiklis and Van Roy for
             the history.
Locators:    printed page = PDF page - 22. Chapter 11 opens p. 257. 11.1 pp. 258-259.
             11.2 pp. 260-264. 11.3 pp. 264-265. Bibliographical remarks p. 285.
             I checked the 2018 and 2020 PDFs against each other: pages 257-267 have
             the same pagination and the same text in 11.2-11.3. The only text
             differences are fixes to eq. 11.6 and 11.8 and to the G_{t:t+n} line on
             p. 259, which match the official errata page
             (http://incompleteideas.net/book/errata.html). The errata list nothing
             for pp. 260-265.
```

Paraphrase, by item the brief asked for:

- **Why 11.1 is not enough (p. 258).** Off-policy learning with function
  approximation has two parts. The first is the update target, which importance
  sampling fixes. The second is the distribution of updates, which no longer
  matches the on-policy distribution. Section 11.1's semi-gradient methods handle
  only the first part, "accordingly, these methods may diverge in some cases"
  (p. 258).
- **Per-step ratio, eq. 11.1 (p. 258):** rho_t = rho_{t:t} = pi(A_t|S_t) /
  b(A_t|S_t).
- **Off-policy semi-gradient TD(0), eq. 11.2 (p. 258):** w_{t+1} = w_t +
  alpha rho_t delta_t grad v-hat(S_t, w_t). The book calls it "just like the
  corresponding on-policy algorithm (page 203) except for the addition of rho_t".
  **Eq. 11.3 (episodic/discounted TD error):** delta_t = R_{t+1} + gamma
  v-hat(S_{t+1}, w_t) - v-hat(S_t, w_t). Eq. 11.4 is the average-reward form.
- **w-to-2w (p. 260, continued p. 261).** Two states with feature 1 and feature
  2 and a single weight w, so their values are w and 2w. The first state has one
  action, which moves deterministically to the second with reward 0. The book
  writes delta_t = 0 + gamma 2w_t - w_t = (2gamma - 1) w_t and w_{t+1} = w_t +
  alpha · 1 · (2gamma - 1) w_t · 1 = (1 + alpha(2gamma - 1)) w_t. Here rho_t = 1
  because the first state has only one action. The system is unstable whenever
  gamma > 0.5. Stability "does not depend on the specific step size, as long as
  alpha > 0". The worked numbers are w = 10, gamma near 1 and alpha = 0.1, so w
  rises to nearly 11, then to about 12.1, and diverges. On p. 261 the book
  explains: on-policy, every w -> 2w transition must be followed by a transition
  out of the 2w state, which pulls w down. Off-policy, rho_t = 0 on the
  transitions the target policy would never take. The quotable line: "a promise
  can be made and then, after taking an action that the target policy never
  would, forgotten and forgiven." The book says the fragment "is not completely
  convincing because it is not complete" (p. 261), and that motivates Baird's
  example.
- **Baird's counterexample (p. 261 text and Figure 11.1; p. 262 text, eq.
  11.9 and Figure 11.2).**
  - MDP: "the episodic seven-state, two-action MDP shown in Figure 11.1".
  - Actions: dashed goes to one of the six upper states with equal probability.
    Solid goes to the seventh state. Figure 11.1 draws both actions from every
    state, including the seventh, where the solid action is a self-loop.
  - Behavior b: dashed 6/7, solid 1/7. The book notes that the next-state
    distribution under b is uniform, and that this is also the start
    distribution of each episode.
  - Target pi: always solid. The on-policy distribution for pi "is concentrated
    in the seventh state".
  - Reward: 0 on all transitions. Discount: gamma = 0.99.
  - Values: upper state i (i = 1..6) is 2w_i + w_8 and the seventh is w_7 + 2w_8.
    The book writes the first state's feature vector as x(1) = (2,0,0,0,0,0,0,1)^T
    with w in R^8.
  - True value: v_pi(s) = 0 for all s. It is exactly representable by w = 0, and
    by many other w, because 8 weights exceed 7 states. The feature vectors are
    linearly independent: "In all these ways this task seems a favorable case for
    linear function approximation" (p. 262).
  - Result (p. 262): semi-gradient TD(0) (11.2) diverges, Figure 11.2 left. "The
    instability occurs for any positive step size, no matter how small." It also
    diverges under the expected (DP) update of eq. 11.9: w_{k+1} = w_k +
    (alpha/|S|) sum_s ( E_pi[R_{t+1} + gamma v-hat(S_{t+1}, w_k) | S_t = s] -
    v-hat(s, w_k) ) grad v-hat(s, w_k), with "no randomness and no asynchrony".
  - Removal by distribution (p. 262): "If we alter just the distribution of DP
    updates ... from the uniform distribution to the on-policy distribution
    (which generally requires asynchronous updating), then convergence is
    guaranteed to a solution with error bounded by (9.14)."
  - Closing claim (p. 263): "even the simplest combination of bootstrapping and
    function approximation can be unstable if the updates are not done according
    to the on-policy distribution."
  - Figure 11.2 caption (p. 262): "The step size was alpha = 0.01, and the
    initial weights were w = (1, 1, 1, 1, 1, 1, 10, 1)^T." The left panel is
    titled "Semi-gradient Off-policy TD", x axis Steps 0-1000. The right panel is
    "Semi-gradient DP", x axis Sweeps 0-1000. The y axis is linear, with ticks at
    1, 10, 100, 200 and 300. In both panels w8 rises highest (above 300 at the
    right edge), the six curves w1-w6 rise together (about 100 or a little more
    at 1000), and w7 stays near 10. The TD panel is jagged and step-like; the DP
    panel is smooth. The caption does not say how many runs or which seed the TD
    panel shows.
- **Q-learning and averagers (pp. 263-264).** The book reports that
  counterexamples similar to Baird's exist for Q-learning (p. 263). Exercise
  11.3 (p. 264) asks for semi-gradient Q-learning on Baird's counterexample. The
  book also says, "To the best of our knowledge, Q-learning has never been found
  to diverge" with an epsilon-greedy behavior policy close to the target, "but
  there has been no theoretical analysis" (p. 263). Averagers such as nearest
  neighbor and locally weighted regression are stable; tile coding and ANNs are
  not averagers (p. 264).
- **The deadly triad, Section 11.3 (p. 264 to p. 265).**
  - Statement, p. 264: "the danger of instability and divergence arises whenever
    we combine all of the following three elements, making up what we call the
    deadly triad".
  - The three definitions, p. 264. Function approximation (e.g. linear FA or
    ANNs). Bootstrapping, defined as "Update targets that include existing
    estimates ... rather than relying exclusively on actual rewards and complete
    returns (as in MC methods)". Off-policy training, defined as "Training on a
    distribution of transitions other than that produced by the target policy".
    The book adds that sweeping uniformly through the states, as DP does, "is an
    example of off-policy training".
  - The danger is not due to control or GPI, and not due to learning or to
    uncertainty about the environment. It arises in prediction, and "just as
    strongly in planning methods, such as dynamic programming" (p. 264).
  - The two-of-three sentence, p. 264, quoted in full in the Quote block below.
  - Which leg to give up (pp. 264-265). Function approximation "most clearly
    cannot be given up" (p. 264). Bootstrapping can be dropped "at the cost of
    computational and data efficiency" (pp. 264-265). Off-policy learning is
    "essential" for learning many predictions in parallel from one stream of
    experience (p. 265).
- **History (p. 285, bibliographical remarks 11.2 and 11.3).** The earliest
  w-to-2w example is credited to Tsitsiklis and Van Roy (1996), who also gave
  Example 11.1. Baird's counterexample "is due to Baird (1995), though the
  version we present here is slightly modified". The triad "was first identified
  by Sutton (1995b) and thoroughly analyzed by Tsitsiklis and Van Roy (1997)."

```text
Quote:       p. 264: "If any two elements of the deadly triad are present, but not all
             three, then instability can be avoided." (The commission's "state the
             claim as the book does" turns on these words.)
```

### S2. Baird (1995), Residual Algorithms: Reinforcement Learning with Function Approximation

```text
URL:         http://leemon.com/papers/1995b.pdf  (author's site; proceedings DOI
             https://doi.org/10.1016/B978-1-55860-377-6.50013-X resolves to Elsevier,
             not opened. Book bib: Proc. 12th ICML, pp. 30-37, Morgan Kaufmann.)
Kind:        primary. The author's own paper introducing the star problem.
Establishes: firsthand: the original star problem and its divergence claim, and the
             later two-action "modified star" MDP in the errata.
Locators:    PDF pp. 1-8 are the paper and p. 9 is an errata page dated 15 Jul 95.
             The PDF is the corrected version, not the proceedings as printed. The
             errata say Figure 1 "was incorrect (fixed by adding the coefficients of
             2)". Sections: 3 "Direct Algorithms" (PDF pp. 2-3), Figure 1 "The star
             problem" (PDF p. 2), 9 "Simulation Results" (PDF pp. 7-8), Errata
             (PDF p. 9). The PDF has no printed proceedings page numbers.
```

Paraphrase:

- **Original star problem (Figure 1, PDF p. 2; Section 3, PDF pp. 2-3).** Six
  states and seven weights w0..w6. V(i) = w0 + 2w_i for i = 1..5 and V(6) = 2w0
  + w6. It is a Markov chain with one action per state. All transitions go to
  state 6, including a 6 -> 6 self-loop. Every reinforcement is zero. "During
  training, each possible transition is observed equally often." The update is
  the direct algorithm, eq. 3: Δw = α(R + γV(x') - V(x)) ∂V(x)/∂w, which Baird
  says "is exactly the TD(0) algorithm, by definition".
- **Baird's characterization (PDF p. 3).** The approximator is linear and
  general, its state vectors are linearly independent and have equal norms, and
  "using backpropagation to change the value in one state will cause neighboring
  states to change by at most two-thirds as much". If all weights start
  positive and V(6) starts much larger than the other values, all values grow
  without bound. While the first five values sit below V(6), and V(6) sits above
  its own successor V(6), "w0 is increased five times for every time that it is
  decreased". All weights go to +infinity except w6, which goes to -infinity.
- **What the paper does not give.** It gives no discount value, step size or
  initial weight vector for the star problem. A search of the text for discount
  values and initial weights found none. Section 9 reports only that the direct
  method "was unable to solve the star problem"; Figure 5 plots learning time
  against the residual mixing parameter phi, and the direct method's learning
  time "appears to approach infinity as phi approaches approximately 0.1034"
  (PDF p. 7).
- **Modified star (errata, PDF p. 9).** An MDP rather than a Markov chain, added
  for the conference presentation. Q-values use 12 weights w0..w12, with w7..w12
  labeling the dotted actions. Each state has a solid action, which goes to
  state 6, and a dotted action, which goes uniformly to states 1-5. Training
  uses a fixed behavior policy with solid 1/6 and dotted 5/6, so every solid
  Q-value is updated equally often. If the solid Q-values start larger than the
  dotted ones, and the 6 -> 6 solid Q-value is the largest, then "all weights,
  Q-values, and values will diverge to infinity", for epoch-wise and incremental
  learning and "even for small learning rates or slowly decreasing learning
  rates".

How the book's version differs from Baird's original (Baird PDF pp. 2-3 and 9
against book pp. 261-262):

| | Baird 1995 star (Fig. 1) | Sutton and Barto Fig. 11.1 |
|---|---|---|
| States | 6 (5 outer + hub) | 7 (6 upper + 1) |
| Weights | 7 (w0..w6) | 8 (w1..w8) |
| Outer value | w0 + 2w_i | 2w_i + w8 |
| Hub value | 2w0 + w6 | w7 + 2w8 |
| Actions | one (Markov chain); errata version has two | two: dashed, solid |
| Policies | none; "each possible transition observed equally often" | b: dashed 6/7, solid 1/7; pi: solid always |
| Off-policy via | update distribution that ignores the chain's dynamics | importance ratio rho = pi/b on sampled transitions; DP version uses uniform weighting |
| gamma | not stated | 0.99 |
| alpha, w0 | not stated; qualitative "all positive, V(6) much larger" | 0.01; (1,1,1,1,1,1,10,1) |
| Claimed outcome | all weights to +inf except w6 to -inf | weights diverge to infinity (Fig. 11.2) |

The mapping is: Baird's shared weight w0 corresponds to the book's w8, and
Baird's hub weight w6 to the book's w7. In both versions the shared weight has
coefficient 1 in outer states and 2 in the hub. The book adds a sixth outer
state, the second action, the policies and the numbers. The book calls its
version "slightly modified" (p. 285). The two-action, uniform-redistribution
structure first appears in Baird's own errata example, with 5/6 against 1/6
instead of 6/7 against 1/7.

### S3. Tsitsiklis and Van Roy (1997), An Analysis of Temporal-Difference Learning with Function Approximation

```text
URL:         https://web.mit.edu/jnt/www/Papers/J063-97-bvr-td.pdf  (Tsitsiklis's MIT
             page; journal record https://doi.org/10.1109/9.580874 -> IEEE Xplore 580874,
             not opened)
Kind:        primary. The authors' own theorem and counterexample. IEEE Transactions on
             Automatic Control 42(5):674-690, May 1997.
Establishes: firsthand: linear TD(lambda) converges when states are sampled from the
             chain's steady-state distribution (on-line), divergence is possible when
             they are sampled from an independent distribution (Theorem 3), and
             divergence occurs with a nonlinear approximator even on-line (Section X).
Locators:    journal page = PDF page + 673. Abstract and Section I pp. 674-675;
             Section III p. 678; Section IX "The Importance of On-Line Sampling" and
             Theorem 3, pp. 686-687; Section X "Divergence with a Nonlinear
             Approximator", pp. 687-688; Section XI Conclusions p. 688.
```

Paraphrase:

- **Section I (pp. 674-675).** Following Sutton, the paper says earlier
  counterexamples share one feature: their TD variants "do not employ on-line
  state sampling". For linear approximators, convergence is guaranteed "if
  states are sampled according to the steady-state probabilities, while
  divergence is possible when states are sampled from distributions independent
  of the dynamics of the Markov chain of interest" (p. 675).
- **Section III (p. 678).** Convergence works because the TD operator contracts
  in the steady-state-weighted norm, and the projection is a nonexpansion in
  that same norm. Under a different sampling distribution q, "there is no reason
  to believe that the projection will be a nonexpansion", so the composed
  operator "may not be a contraction and might even be an expansion". When
  states are sampled on-line, q equals the steady-state distribution pi. "There
  is no such promise when states are sampled by an independent mechanism."
- **Section IX, Theorem 3 (pp. 686-687).** This section defines "q-sampled
  TD(0)": states i_t are drawn i.i.d. from q, and successors j_t are drawn from
  the chain. The theorem says that for any q on at least two states, and any
  discount in the open interval (5/6, 1), there exist a chain, a zero cost
  function and a one-column feature matrix that make the expected weight
  diverge, ||E[r_t | r_0]|| -> infinity for every r_0 != r* = 0. The
  construction uses phi(1) = 1, phi(2) = 2 and 0 elsewhere (the w-to-2w
  features), with every row of P equal to a distribution p having p(2) > 5/(6
  alpha). It assumes q(1) >= q(2).
- **Section X (pp. 687-688).** A three-state chain with zero costs and a
  one-parameter nonlinear approximator whose values trace a spiral. TD(0) runs
  along the trajectory with a uniform steady state, which is on-line and so
  on-policy, and it diverges. The paper calls this example "a warning rather
  than a ban on all nonlinear function approximators" (p. 675).
- **Notation warning for the writer.** This paper uses alpha for the discount
  factor, gamma_t for the step size, r for the weight vector, and costs g in
  place of rewards. A quotation lifted from it will clash with the book's
  symbols.

### S4. Sutton et al. (2009), Fast Gradient-Descent Methods for Temporal-Difference Learning with Linear Function Approximation (Gradient-TD)

```text
URL:         http://incompleteideas.net/papers/SMPBSSW-09.pdf  (author's site; ICML 2009,
             Montreal; https://doi.org/10.1145/1553374.1553501 -> ACM DL returned 403
             to a scripted request, treated as gated)
Kind:        primary. The authors introduce GTD2 and TDC.
Establishes: firsthand: GTD2 and TDC minimize the projected Bellman error, are proved
             convergent with linear FA under off-policy training at O(n) cost, and
             converge on the 7-state Baird problem where TD diverges.
Locators:    Section 3 "Objective functions" (p. 2); Section 4 "Derivation of the new
             algorithms" (p. 3 on); TDC on p. 6; Section 7, Figure 5 (p. 8).
Pointer:     read Section 4 for how GTD2 and TDC turn the projected Bellman error into
             an O(n) update with a second weight vector; Figure 5 shows them
             converging on Baird's counterexample.
```

The Figure 5 caption says it shows "the 7-state version of the 'star'
counterexample (Baird 1995)", updated synchronously in DP-like sweeps. It uses
TD alpha = 0.1, gradient methods alpha = 0.05 and eta = 10, theta0 =
(1,1,1,1,1,1,10,1)^T and gamma = 0.99. TD's alpha here differs from the book's
0.01. The book's own treatment is Section 11.7, Gradient-TD Methods, pp.
278-281, with TDC on Baird's counterexample in Figure 11.5 on p. 280.

### S5. Sutton, Mahmood and White (2016), An Emphatic Approach to the Problem of Off-policy Temporal-Difference Learning

```text
URL:         https://jmlr.org/papers/v17/14-488.html  (PDF
             https://jmlr.org/papers/volume17/14-488/14-488.pdf). JMLR 17(73):1-29.
Kind:        primary. The authors introduce emphatic TD.
Establishes: firsthand: off-policy TD(0)'s expected-update ("key") matrix
             Phi^T D_mu (I - gamma P_pi) Phi need not be positive definite; emphatic TD
             reweights updates by a followon trace F_t so it is.
Locators:    Section 3 "Instability of Off-policy TD(0)" pp. 7-9 (theta->2theta,
             eq. 8, A matrix p. 8, Figure 1 and eq. 9 p. 9); Section 4 "Off-policy
             Stability of Emphatic TD(0)" pp. 10-12 (followon trace eq. 10, update
             eq. 11, p. 11).
Pointer:     read Section 3 for the cleanest matrix explanation of why off-policy
             TD(0) diverges (a two-state example where the key matrix works out to
             -0.2), then Section 4 for the followon-trace fix.
```

The page 9 example may help a writer who wants the eigenvalue view on two
states. Each of the two states (features 1 and 2) has actions left and right,
and all rewards are 0. The behavior policy is mu(right) = 0.5, so d_mu = (0.5,
0.5). The target policy is pi(right) = 1, with gamma = 0.9 and lambda = 0, and
P_pi = [[0,1],[0,1]]. The paper gives D_mu(I - gamma P_pi) = [[0.5, -0.45],
[0, 0.05]] and Phi^T D_mu (I - gamma P_pi) Phi = -0.2. It says that
"Clearly, this expected update and algorithm are not stable." Its worked step
from theta = 10 with alpha = 0.1 and rho = 2 gives theta = 10 + 1.6. Sign
convention: here A must be positive definite for stability. The update is theta
<- theta + alpha(b - A theta), the opposite sign from writing the update as w <-
w + alpha M w. The book's own treatment is Section 11.8, Emphatic-TD Methods,
pp. 281-283, with Baird's counterexample in Figure 11.6 on p. 283.

### S6. van Hasselt, Doron, Strub, Hessel, Sonnerat, Modayil (2018), Deep Reinforcement Learning and the Deadly Triad

```text
URL:         https://arxiv.org/abs/1812.02648  (v1, 6 Dec 2018; arXiv shows only v1)
Kind:        primary for its own experiments (DeepMind and Univ. of Lille authors ran
             them); secondary for its retelling of the triad and the w-to-2w example.
Establishes: firsthand: in DQN variants on 57 Atari games (336 settings per game,
             3 replications), values often exceeded the realisable bound of 100
             ("soft divergence") but never became unbounded (no NaNs).
Locators:    Section 4.1 "Unbounded divergence in deep RL (Hypothesis 1)", p. 5;
             soft divergence defined just above it (|q| > 100, from clipped rewards
             and gamma = 0.99). Section 2 and Figure 1 (p. 2) retell the w-to-2w
             example.
Pointer:     Section 4.1: with deep Q-networks the triad produced inflated but never
             unbounded values. Stage 4 can open from here.
```

Other figures on the same pages: Q-learning soft-diverged in 61% of runs, the
most of the four bootstrap targets (Section 4.2). Q-learning with n = 1
soft-diverged on 94% of runs and with n = 10 on 21% (Section 4, multi-step results, p. 7). Two caveats for any pointer.
Section 3 says target networks "do not suffice as a solution to the deadly
triad", because in the linear w-to-2w example "the weights still diverge, though
the divergence is slowed down by the copying period". The paper also attributes
the w-to-2w example to Tsitsiklis and Van Roy (1997), while the book credits
their 1996 paper (p. 285).

## Contradictions

- **Commission label against the book.** The commission writes "Baird's
  counterexample (Sutton and Barto, Example 11.1, Section 11.2)". In the book,
  Example 11.1 is "Tsitsiklis and Van Roy's Counterexample" (p. 263), the
  least-squares DP divergence with a terminal state, whose map is w_{k+1} =
  ((6 - 4ε)/5) γ w_k (eq. 11.10). Baird's counterexample has no example number.
  Cite it as "Baird's counterexample, Section 11.2, Figures 11.1 and 11.2, pp.
  261-262".
- **Commission's one idea against the book's claim.** The commission says
  "Take any one away on the same problem and the weights stay bounded". The
  book's claims are weaker. Combining all three creates a "danger of instability
  and divergence" (p. 264). With any two, "instability can be avoided" (p. 264).
  The commission's own boundary ("Do not overstate it as 'all three always
  diverge'") is consistent with the book. The "stay bounded" half is a claim
  about this problem's runs, which the lesson must show with its own runs and
  not attribute to the book.
- **"Any two are safe" against nonlinear approximation.** Tsitsiklis and Van
  Roy, Section X (pp. 687-688), show on-line (on-policy) TD(0) with a nonlinear
  approximator diverging, which is function approximation plus bootstrapping
  without off-policy training. The book's own stability results for on-policy
  semi-gradient TD are for linear features. Stating the safe-with-two claim for
  linear function approximation avoids the conflict.
- **"Episodic" against the figure.** The book says "Consider the episodic
  seven-state, two-action MDP" and says the uniform next-state distribution "is
  also the starting distribution for each episode" (p. 261). Figure 11.1 draws no
  terminal state, and its caption says the solid action "usually" results in the
  seventh state and the dashed action "usually" in one of the other six (p. 261).
  The errata page does not address either. Its own Figure 11.2 runs 1,000 steps
  with no termination described. The GTD paper's Figure 5 runs the same problem
  as DP-like sweeps. A writer can treat it as continuing with gamma = 0.99, and
  should say so.
- **Behavior proportions differ across Baird versions.** Baird's errata MDP
  uses solid 1/6 and dotted 5/6 over 6 states. The book uses solid 1/7 and
  dashed 6/7 over 7 states. Both are chosen so that the next-state distribution
  is uniform.
- **Outcome of the hub weight.** Baird's text says the hub weight w6 goes to
  -infinity (PDF p. 3). The book's Figure 11.2 shows w7 staying near 10 over
  1,000 steps or sweeps. My numerical check (see Numbers) shows the book's w7
  falling slowly, to 6.85 after 1,000 sweeps, and reaching about -2.3e20 by
  20,000 sweeps. The dominant eigenvector has a small negative w7 component. The
  two accounts agree in the long run, but in a 1,000-step plot w7 looks bounded.
  A reader could misread that.
- **Two removals on Baird are degenerate.** These are my calculations, not from
  any source. The commission's removal tests do keep the weights bounded on
  Baird. Under on-policy weighting the expected update matrix is -(1 - gamma)
  x7 x7^T. It is rank one, and only the component along x7 = (0,...,0,1,2)
  moves, because pi visits only state 7. The upper-state weights are never
  updated. With a Monte Carlo target (return 0) the matrix is -(1/7) X^T X,
  which has one zero eigenvalue (8 weights, 7 states). Both cases have maximum
  real eigenvalue 0, so they are bounded but not contracting to w = 0. Tabular
  features give a maximum real eigenvalue of -0.001429 = (gamma - 1)/7, which is
  strictly stable. The lesson should claim "bounded", not "converges to zero",
  for the first two.

## Numbers

```text
Figure: per-step ratio rho_t = pi(A_t|S_t)/b(A_t|S_t)
Owner:  Sutton and Barto eq. 11.1, p. 258
Scope:  definition
```
```text
Figure: Baird ratios: rho = 7 on a solid step (1 / (1/7)), rho = 0 on a dashed step
Owner:  derived from Sutton and Barto p. 261 (b and pi); the book does not print these values
Scope:  every state
```
```text
Figure: w-to-2w multiplier 1 + alpha(2gamma - 1); unstable iff gamma > 0.5, for any alpha > 0
Owner:  Sutton and Barto p. 260
Scope:  single transition repeated, rho = 1
```
```text
Figure: w-to-2w worked numbers: w = 10, alpha = 0.1, gamma near 1 -> w approx 11, then approx 12.1
Owner:  Sutton and Barto p. 260 (same numbers in Sutton, Mahmood and White 2016 p. 7)
Scope:  illustrative steps
```
```text
Figure: Baird feature matrix X (rows = states 1..7, columns = w1..w8):
        s1 (2,0,0,0,0,0,0,1); s2 (0,2,0,0,0,0,0,1); s3 (0,0,2,0,0,0,0,1);
        s4 (0,0,0,2,0,0,0,1); s5 (0,0,0,0,2,0,0,1); s6 (0,0,0,0,0,2,0,1);
        s7 (0,0,0,0,0,0,1,2)
Owner:  Sutton and Barto Figure 11.1 (p. 261) and x(1) on p. 262; rows 2-7 read from the
        figure's linear expressions
Scope:  7 states, 8 weights
```
```text
Figure: b(dashed|.) = 6/7, b(solid|.) = 1/7, pi(solid|.) = 1, gamma = 0.99, reward 0
Owner:  Sutton and Barto Figure 11.1 and text, p. 261
Scope:  all states
```
```text
Figure: alpha = 0.01; initial w = (1, 1, 1, 1, 1, 1, 10, 1)^T
Owner:  Sutton and Barto Figure 11.2 caption, p. 262
Scope:  both panels (TD: 1,000 steps; DP: 1,000 sweeps)
```
```text
Figure: Figure 11.2 axis: y linear with ticks 1, 10, 100, 200, 300; w8 ends above 300, w1-w6 near
        100 or a little more, w7 near 10 (read from the plot)
Owner:  Sutton and Barto Figure 11.2, p. 262
Scope:  1,000 steps/sweeps
```
```text
Figure: researcher reproduction of eq. 11.9 (alpha = 0.01, alpha/|S| weighting, w0 as above):
        after 1,000 sweeps w1..w6 = 114.43, w7 = 6.85, w8 = 335.00
Owner:  my computation (numpy), matching Figure 11.2 right; not a source. Script in my
        scratchpad: /tmp/claude-0/-home-user-the-nightly-build/73adddb6-4cd9-59e1-a2aa-3a8d60989e9b/scratchpad/scripts/baird.py
Scope:  deterministic; the writer's own run should print the same to 2 decimals
```
```text
Figure: researcher check, one TD(0) run of 1,000 steps (seed 0, numpy default_rng):
        w1..w6 between 83 and 137, w7 = 6.28, w8 = 344.66
Owner:  my computation; not a source; seed-dependent
Scope:  single run; same order of magnitude as Figure 11.2 left
```
```text
Figure: expected-update matrix M (w <- w + alpha M w) on Baird, uniform weighting,
        M = (1/7) sum_s x(s)(gamma x(7) - x(s))^T; eigenvalues: -0.57143 (x5), 0,
        0.02218, 0.23925
Owner:  my computation from the book's spec; not a source
Scope:  identical for semi-gradient DP (eq. 11.9) and the expectation of off-policy TD(0)
        under b, because E_b[rho (gamma x(S') - x(s))] = gamma x(7) - x(s) for every s
```
```text
Figure: removal variants, max real eigenvalue of M: on-policy weighting 0.0; MC target
        (return 0) 0.0; tabular 7x7 identity features -0.001429
Owner:  my computation; not a source
Scope:  same problem otherwise; zero eigenvalues are neutral directions (bounded, not decaying)
```
```text
Figure: Tsitsiklis and Van Roy Theorem 3: discount in (5/6, 1), features 1 and 2
Owner:  Tsitsiklis and Van Roy 1997, Section IX, p. 686
Scope:  q-sampled TD(0); any sampling distribution q over at least two states (the proof
        assumes q(1) > 0 and q(1) >= q(2) without loss of generality)
```
```text
Figure: emphatic paper two-state key value Phi^T D_mu (I - gamma P_pi) Phi = -0.2 (gamma = 0.9,
        d_mu = (0.5, 0.5))
Owner:  Sutton, Mahmood and White 2016, Section 3, eq. 9, p. 9
Scope:  linear, one weight, features 1 and 2
```
```text
Figure: soft divergence (|q| > 100) occurred; unbounded divergence (NaN) in 0 runs
Owner:  van Hasselt et al. 2018, Section 4.1, p. 5
Scope:  57 Atari games x 336 settings x 3 replications, DQN variants
```

## Limits

- The book does not say whether the Figure 11.2 TD panel is a single run, or
  give a seed. Only the DP panel can be checked exactly against a run.
- The book's "episodic" wording has no terminal state behind it. I found no
  author note resolving this, and the errata are silent. The writer must state
  the continuing interpretation as a choice.
- I could not open Baird (1995) as printed in the proceedings. The leemon.com
  PDF is the author's corrected July 1995 version, and its errata say the
  original Figure 1 lacked the coefficients of 2. Locators are PDF pages and
  section numbers, not proceedings pages 30-37.
- Baird (1995) gives no discount, step size or initial weights for the star
  problem, so it cannot be rerun "as Baird specified". Only the book's variant
  has numbers.
- The book gives no source for the commission's claim that removing any one
  element keeps the weights bounded on this problem. The book speaks only of
  "can be avoided". The removal results are the lesson's own evidence (my
  eigenvalue checks above agree).
- Sutton (1995b), the workshop paper the book credits with first identifying the
  triad, and Sutton (2015a), the NeurIPS tutorial credited with the name, were
  not sought. The brief did not ask for them, and the book's p. 285 note is the
  citable record of that history.
- I did not open the IEEE (TvR) or ACM (GTD) publisher pages. The author-hosted
  copies carry the journal header (TvR) and the "Appearing in Proceedings of the
  26th ICML" note (GTD).

## Source assets

Sutton and Barto (RLbook2020.pdf):

```text
Asset: Figure 11.1, Baird's counterexample diagram, p. 261 (PDF p. 283)
Shows: the seven states with their linear value expressions, solid and dashed arrows,
       and the policy and gamma labels: the whole spec in one picture
Crop:  keep all seven circles, both arrow styles, the dashed loop, the labels
       pi(solid|.) = 1, b(dashed|.) = 6/7, b(solid|.) = 1/7, gamma = 0.99 and the
       caption; omit the body text above
```
```text
Asset: Figure 11.2, two panels "Semi-gradient Off-policy TD" and "Semi-gradient DP", p. 262
       (PDF p. 284)
Shows: the book's own divergence result, against which the lesson's runs can be compared
Crop:  keep both panels, axes, the w8 / w1-w6 / w7 labels and the caption with
       alpha = 0.01 and w0; the lesson's own runs may be better drawn as inline SVG,
       per the series direction
```
```text
Asset: the w -> 2w diagram, p. 260 (PDF p. 282)
Shows: the two-circle fragment; small and easily redrawn
Crop:  redraw rather than capture
```
```text
Asset: Section 11.3 box of three definitions, p. 264
Shows: the statement in the book's own words
Crop:  text; quote rather than capture
```

Baird (1995):

```text
Asset: Figure 1, "The star problem", PDF p. 2
Shows: the original six-state chain with V(i) = w0 + 2w_i and V(6) = 2w0 + w6, for a
       then-and-now comparison with Figure 11.1
Crop:  the figure and its caption only; the labels are small at screen resolution
```

Tsitsiklis and Van Roy (1997): None found that a lesson at this level can use.
The Section X spiral (Fig. 1, p. 687) is a nonlinear case outside the lesson.

Sutton, Mahmood and White (2016):

```text
Asset: Figure 1 and eq. 9, p. 9 (theta -> 2theta without a terminal state, key matrix
       [[0.5, -0.45],[0, 0.05]], product -0.2)
Shows: the expected-update matrix argument on two states, an option for the lesson's
       eigenvalue drawing
Crop:  only if used; better redrawn in the lesson's notation
```

Sutton et al. (2009): Figure 5, p. 8 (TD diverging while GTD2 and TDC converge on
Baird). This is optional for a Go-deeper pointer and not needed on the page.

van Hasselt et al. (2018): None needed for a one-line pointer.

## Discarded

- https://www.cs.utexas.edu/~shivaram/readings/b2hd-Baird1995.html: a reading-list
  entry, used only to find the author's PDF URL.
- https://mlanthology.org/icml/1995/iii1995icml-residual: a catalogue page; it
  added nothing beyond the bibliographic data.
- https://typeset.io/pdf/residual-algorithms-reinforcement-learning-with-function-150011hve2.pdf:
  a third-party copy of Baird. The author's copy was available.
- https://sites.ualberta.ca/~szepesva/papers/GTD-ICML09.pdf: the same GTD paper
  as the incompleteideas copy, with identical section and figure placement. Kept
  the first author's copy.
