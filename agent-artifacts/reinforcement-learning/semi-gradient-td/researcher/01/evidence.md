# Evidence: reinforcement-learning/semi-gradient-td (researcher 01)

The sources support every definition and update the lesson needs, each with a
page in Sutton and Barto (2nd ed., 2020 printing): VE (eq. 9.1, p. 199), the
SGD and gradient Monte Carlo updates (eqs. 9.4-9.7, pp. 201-202), the reason
semi-gradient TD(0) is "semi" (p. 202), Example 9.1's rules (p. 203), the TD
fixed point (eq. 9.12, p. 206) and the bound (eq. 9.14, p. 207). Sutton's own
Lisp for Example 9.1 exists and matches the book's rules exactly. An exact solve
reproduces the book's on-policy distribution figures (1.37%, 0.17%, 0.0147%,
"more than 3 times"), and an exact computation of both solutions shows them
differing on this walk: VE at the TD fixed point is about 4.6 times VE at the
Monte Carlo solution. Tsitsiklis and Van Roy (1997) is located (Theorem 1,
Section IV, p. 679). The evidence is thin in one place the commission leans on.
Eq. 9.14 is stated for continuing tasks with gamma < 1, and the 1000-state walk
is episodic and undiscounted, so 1/(1-gamma) has no finite value there. The book
points to Bertsekas and Tsitsiklis (1996) for the episodic bound, which I could
not open. Tsitsiklis and Van Roy also treat only the discounted, non-terminating
case. Two smaller gaps follow. The book gives no step size or episode count for
the TD panel of Figure 9.2; only a comment in Sutton's code does (alpha = 0.0002,
100,000 episodes). The strong form "not the gradient of any objective" traces to
Barnard (1993), which I did not open; the book says only "not true gradient
descent".

## Sources

### 1. Sutton and Barto, Reinforcement Learning: An Introduction, 2nd ed. (2020 printing PDF)

```text
URL:         http://incompleteideas.net/book/RLbook2020.pdf
             (book page N is PDF page N+22; e.g. p. 203 is
             http://incompleteideas.net/book/RLbook2020.pdf#page=225.
             The authors' errata page documents this #page=X form.)
Kind:        primary for its own definitions, algorithms, Example 9.1/9.2 and
             the figures' stated parameters (the authors designed the example
             and ran the figures). Secondary for the convergence theorem and
             the bound in Section 9.4, which it reports and attributes to
             Tsitsiklis and Van Roy (1997) and Bertsekas and Tsitsiklis (1996).
Establishes: firsthand everything below except the proofs behind 9.12-9.14.
```

Passages, each with page and paraphrase:

- **Setting and notation, p. 197.** The approximate value function is a
  parameterized form v̂(s,w) ≈ v_π(s) with weight vector w in R^d, typically
  d << |S|; "changing one weight changes the estimated value of many states."
- **Update notation, p. 198 (Section 9.1).** Every prediction update is written
  s ↦ u (state updated, update target). MC: S_t ↦ G_t; TD(0): S_t ↦ R_{t+1} +
  γ v̂(S_{t+1}, w_t); n-step: S_t ↦ G_{t:t+n}.
- **VE objective, eq. 9.1, p. 199 (Section 9.2).** One must choose a state
  distribution μ(s) ≥ 0, Σ_s μ(s) = 1, "representing how much we care about the
  error in each state s". VE(w) ≐ Σ_{s∈S} μ(s)[v_π(s) − v̂(s,w)]². Its square
  root, "the root VE", is the quantity usually plotted. "Often μ(s) is chosen to
  be the fraction of time spent in s. Under on-policy training this is called
  the on-policy distribution."
- **Episodic on-policy distribution, eqs. 9.2-9.3, p. 199 (boxed).** η(s) =
  h(s) + Σ_s̄ η(s̄) Σ_a π(a|s̄) p(s|s̄,a), with h the start distribution and η(s)
  the expected number of time steps spent in s per episode. μ(s) = η(s) / Σ_s'
  η(s'). With discounting, put a factor γ in the second term of 9.2.
- **VE is not obviously the right objective, p. 200.** The book adopts it
  anyway. Global optimum is "sometimes possible for simple function
  approximators such as linear ones".
- **SGD toward the true value, eqs. 9.4-9.5, p. 201 (Section 9.3).**
  w_{t+1} ≐ w_t − ½ α ∇[v_π(S_t) − v̂(S_t,w_t)]² = w_t + α[v_π(S_t) −
  v̂(S_t,w_t)] ∇v̂(S_t,w_t). States in the examples are assumed to arrive with
  the same distribution μ the VE uses. Eq. 9.6 defines ∇f(w) as the column
  vector of partials. Convergence results "assume that α decreases over time"
  under the stochastic approximation conditions (2.7).
- **General SGD with a target U_t, eq. 9.7, p. 202.** w_{t+1} ≐ w_t + α[U_t −
  v̂(S_t,w_t)] ∇v̂(S_t,w_t). If E[U_t | S_t = s] = v_π(s) (unbiased), w_t
  converges to a local optimum under decreasing α. The Monte Carlo target U_t =
  G_t is "by definition an unbiased estimate", so gradient MC "is guaranteed to
  find a locally optimal solution."
- **Gradient Monte Carlo box, p. 202.** Generate a whole episode with π, then
  for t = 0..T−1: w ← w + α[G_t − v̂(S_t,w)]∇v̂(S_t,w). Weights initialized
  arbitrarily (e.g. w = 0).
- **Why "semi", p. 202.** Bootstrapping targets "all depend on the current value
  of the weight vector w_t, which implies that they will be biased and that they
  will not produce a true gradient-descent method." "The key step from (9.4) to
  (9.5) relies on the target being independent of w_t." Quote (the wording is
  the definition the lesson teaches): "Bootstrapping methods are not in fact
  instances of true gradient descent (Barnard, 1993). They take into account the
  effect of changing the weight vector w_t on the estimate, but ignore its
  effect on the target. They include only a part of the gradient and,
  accordingly, we call them semi-gradient methods."
- **Semi-gradient TD(0), p. 203.** Target U_t ≐ R_{t+1} + γ v̂(S_{t+1},w). Box:
  input v̂ : S+ × R^d → R "such that v̂(terminal,·) = 0"; per step w ← w + α[R +
  γ v̂(S',w) − v̂(S,w)]∇v̂(S,w). The book says these methods "do converge reliably
  in important cases such as the linear case" and "typically enable
  significantly faster learning" (pp. 202-203).
- **State aggregation, p. 203.** States are grouped, one weight per group; a
  state's value is its group's component and only that component is updated.
  "State aggregation is a special case of SGD (9.7) in which the gradient,
  ∇v̂(S_t,w_t), is 1 for S_t's group's component and 0 for the other
  components." p. 208 adds: "State aggregation is a special case of linear
  function approximation."
- **Example 9.1, p. 203 (rules, exact).** "Consider a 1000-state version of the
  random walk task (Examples 6.2 and 7.1 on pages 125 and 144). The states are
  numbered from 1 to 1000, left to right, and all episodes begin near the
  center, in state 500. State transitions are from the current state to one of
  the 100 neighboring states to its left, or to one of the 100 neighboring
  states to its right, all with equal probability. Of course, if the current
  state is near an edge, then there may be fewer than 100 neighbors on that side
  of it. In this case, all the probability that would have gone into those
  missing neighbors goes into the probability of terminating on that side (thus,
  state 1 has a 0.5 chance of terminating on the left, and state 950 has a 0.25
  chance of terminating on the right). As usual, termination on the left
  produces a reward of −1, and termination on the right produces a reward of +1.
  All other transitions have a reward of zero." Aggregation: "the 1000 states
  were partitioned into 10 groups of 100 states each (i.e., states 1–100 were
  one group, states 101–200 were another, and so on)." The example does not
  restate γ; "As usual" refers back to Example 6.2, which says "this task is
  undiscounted" (p. 125). Sutton's code (source 2) has no discount.
- **Figure 9.1 and its text, pp. 203-204.** True v_π "is nearly a straight line,
  curving very slightly toward the horizontal for the last 100 states at each
  end." The plotted approximation is "the final approximate value function
  learned by the gradient Monte-Carlo algorithm with state aggregation after
  100,000 episodes with a step size of α = 2 × 10⁻⁵." The staircase "is typical
  of state aggregation", and "These approximate values are close to the global
  minimum of the VE (9.1)." μ: "State 500, in the center, is the first state of
  every episode, but is rarely visited again. On average, about 1.37% of the
  time steps are spent in the start state. The states reachable in one step from
  the start state are the second most visited, with about 0.17% of the time
  steps being spent in each of them. From there μ falls off almost linearly,
  reaching about 0.0147% at the extreme states 1 and 1000." Leftmost groups'
  values are "clearly shifted higher than the unweighted average of the true
  values of states within the group", rightmost lower; "in the leftmost group,
  state 100 is weighted more than 3 times more strongly than state 1."
- **Linear methods, eq. 9.8, p. 205 (Section 9.4).** v̂(s,w) ≐ wᵀx(s) =
  Σ_i w_i x_i(s); x(s) is the feature vector; ∇v̂(s,w) = x(s), so 9.7 becomes
  w_{t+1} = w_t + α[U_t − v̂(S_t,w_t)]x(S_t). In the linear case there is one
  optimum, so "the gradient Monte Carlo algorithm ... converges to the global
  optimum of the VE under linear function approximation if α is reduced over
  time according to the usual conditions."
- **TD fixed point, eqs. 9.9-9.12, pp. 205-206.** "The semi-gradient TD(0)
  algorithm ... also converges under linear function approximation, but this
  does not follow from general results on SGD; a separate theorem is necessary.
  The weight vector converged to is also not the global optimum, but rather a
  point near the local optimum." The analysis is done "specifically for the
  continuing case". 9.9: w_{t+1} = w_t + α(R_{t+1}x_t − x_t(x_t − γx_{t+1})ᵀ
  w_t). 9.10: E[w_{t+1}|w_t] = w_t + α(b − Aw_t). 9.11: b ≐ E[R_{t+1}x_t] ∈ R^d,
  A ≐ E[x_t(x_t − γx_{t+1})ᵀ] ∈ R^{d×d}. 9.12: b − Aw_TD = 0 ⇒ w_TD ≐ A⁻¹b.
  Quote: "This quantity is called the TD fixed point. In fact linear
  semi-gradient TD(0) converges to this point."
- **Convergence box, eq. 9.13, pp. 206-207.** E[w_{t+1}|w_t] = (I − αA)w_t +
  αb; only A matters for convergence; A positive definite assures stability and
  existence of A⁻¹. For continuing tasks with γ < 1, A = XᵀD(I − γP)X (D =
  diag(μ), X rows x(s)ᵀ, P the state-transition matrix under π). Positive
  definiteness follows from column sums 1ᵀD(I − γP) = (1 − γ)μᵀ > 0, using μ
  stationary (Sutton 1988 p. 27; Varga 1962). "Additional conditions and a
  schedule for reducing α over time are needed to prove convergence with
  probability one."
- **The bound, eq. 9.14, p. 207.** "At the TD fixed point, it has also been
  proven (in the continuing case) that the VE is within a bounded expansion of
  the lowest possible error: VE(w_TD) ≤ 1/(1−γ) min_w VE(w)." "The asymptotic
  error of the TD method is no more than 1/(1−γ) times the smallest possible
  error, that attained in the limit by the Monte Carlo method. Because γ is
  often near one, this expansion factor can be quite large." Against that, TD
  methods "are often of vastly reduced variance".
- **Scope of the bound, p. 208.** Quote (it limits what the page may claim for
  the walk): "For episodic tasks, there is a slightly different but related
  bound (see Bertsekas and Tsitsiklis, 1996). There are also a few technical
  conditions on the rewards, features, and decrease in the step-size parameter,
  which we have omitted here. The full details can be found in the original
  paper (Tsitsiklis and Van Roy, 1997)." And: "Critical to these convergence
  results is that states are updated according to the on-policy distribution.
  For other update distributions, bootstrapping methods using function
  approximation may actually diverge to infinity." (deadly-triad pointer,
  Chapter 11).
- **Example 9.2 and Figure 9.2, pp. 208-209.** Left panel: "the final value
  function learned by the semi-gradient TD(0) algorithm (page 203) using the
  same state aggregation as in Example 9.1. We see that the near-asymptotic TD
  approximation is indeed farther from the true values than the Monte Carlo
  approximation shown in Figure 9.1." No step size or episode count is given for
  the left panel. Right panel: n-step semi-gradient TD, aggregation switched to
  20 groups of 50 states, "an unweighted average of the RMS error over all
  states and over the first 10 episodes", n = 1, 2, 4, ..., 512, α from 0 to 1;
  caption: "These data are averages over 100 runs."
- **Exercise 9.1, p. 209.** "Show that tabular methods ... are a special case of
  linear function approximation. What would the feature vectors be?" (The answer,
  one-hot indicator features, is common ground; the book poses but does not
  print it.)
- **Chapter 9 summary, p. 236.** "Semi-gradient TD methods are not true
  gradient methods. In such bootstrapping methods (including DP), the weight
  vector appears in the update target, yet this is not taken into account in
  computing the gradient—thus they are semi-gradient methods. As such, they
  cannot rely on classical SGD results." Also: gradient MC and semi-gradient
  TD(0) are n-step semi-gradient TD with n = ∞ and n = 1; the asymptotic bound
  "is always tighter for higher n and approaches zero as n → ∞."
- **Bibliographical remarks, pp. 237-238.** "Semi-gradient TD(0) was first
  explored by Sutton (1984, 1988)"; "The term 'semi-gradient' to describe these
  bootstrapping methods is new to the second edition of this book." Section 9.4
  history: Sutton (1988) proved convergence in the mean to the minimal-VE
  solution for linearly independent features; several w.p.1 proofs followed for
  that case; "Convergence for the more important case of general (dependent)
  feature vectors was first shown by Dayan (1992). A significant generalization
  and strengthening of Dayan's result was proved by Tsitsiklis and Van Roy
  (1997). They proved the main result presented in this section, the bound on
  the asymptotic error of linear bootstrapping methods."
- **Section 11.4, pp. 266-269 (for Go deeper only).** p. 267: the representable
  function closest to v_π in the μ-norm is its projection Πv_π, "the solution
  asymptotically found by Monte Carlo methods, albeit often very slowly ... TD
  methods find different solutions." p. 269: with linear FA the point of zero
  projected Bellman error "is the TD fixed point, w_TD, introduced in Section
  9.4 ... this value function is generally different from those minimizing VE
  or BE." p. 270 (Section 11.5): "only the Monte Carlo methods are true SGD
  methods."

### 2. Sutton, aggreg-walknew.lisp (author's code for Example 9.1)

```text
URL:         http://incompleteideas.net/book/code/aggreg-walknew.lisp
Kind:        primary: Sutton's own code, linked from the book's code page as
             the code for "State Aggregation on the 1000-state Random Walk,
             Figures 9.1, 9.2, and 9.5". The page says the code is "made
             available as is", so it is not certified as the exact version that
             drew the printed figures.
Establishes: firsthand the conventions below. File uses classic-Mac CR line
             endings; line numbers here are after converting CR to LF.
Locators:    lines 9-24 (parameters), 38-51 (init/group/vh/learn), 53-80
             (process-walk-nstep), 82-95 (standard-walks, random-walk), 97-117
             (dp, compute-d), 119-124 (residual-error), 155-165 (commented
             invocations).
```

Conventions, exact:

- Nonterminal states are 0-based, `NN` = 1000; start state is `(truncate (/ (- n
  1) 2))` = 499, the book's state 500.
- Jump: `jump-maybe0 = (random 200) − 100`, an integer in −100..99; a 0 is
  replaced by +100. Result: 200 equally likely jumps, ±1..±100, each 1/200.
- The walk continues while 0 ≤ x < 1000. Leaving the range ends the episode with
  outcome −1.0 if x < 0, +1.0 otherwise. So any jump past an edge terminates on
  that side, which is the book's rule.
- Reward on every transition is 0 except the terminating one, which equals the
  outcome. No discount factor appears anywhere.
- `m` = 10 groups; `group-size` = 1000/10 = 100; `group(s) = floor(s/100)`, so
  0-based 0-99 (book 1-100) is group 0.
- Weights `theta` initialized to `initial-V` = 0.0. Update: `theta[g] += alpha *
  (target − theta[g])`, which is 9.7 with a one-hot gradient.
- TD target with n = 1: `R + vh(S')` if S' is nonterminal, else `R`.
- There is no separate Monte Carlo routine. n-step with n at least the episode
  length gives the full return, which for this task is the outcome. (FAwalknew.lisp,
  source 4, uses n = 1000 for its Monte Carlo learning curves.)
- Episodes are pre-generated from a copy of a standard random state
  (`standard-walks`), so every α and n sees the same walks.
- True values `vpi`: `dp` runs 2000 in-place sweeps of v(s) = (1/200)
  Σ_{k=1..100} [v(s−k), or −1 if off the left] + [v(s+k), or +1 if off the
  right]. Iterative policy evaluation, not an exact linear solve.
- `d`: `compute-d` runs 2000 in-place sweeps of eq. 9.2 with h = 1 at state 499.
  In this file d is the unnormalized η (expected visits per episode).
- `residual-error` = sqrt(Σ_s d(s)(v̂(s) − v_π(s))²). With unnormalized d this
  is sqrt(Σ η) ≈ 9.12 times root VE (Σ η ≈ 83.15, see Numbers).
- Commented invocation (lines 156-157): `(setup 1 100000)` then
  `(learning-curve-nstep 0.0002 1 100000)`: one run, n = 1 (semi-gradient
  TD(0)), α = 0.0002, 100,000 walks, followed by plotting `vpi` and `vh`. This
  is the only record of the TD panel's step size and episode count.

### 3. Sutton and Barto, code page for the 2nd edition

```text
URL:         http://incompleteideas.net/book/code/code2nd.html
Kind:        primary: the authors' page attributing code files to figures.
Establishes: aggreg-walknew.lisp is "State Aggregation on the 1000-state Random
             Walk, Figures 9.1, 9.2, and 9.5 (Lisp)"; FAwalknew.lisp is "Why we
             use coarse coding, Figure 9.15 (Lisp)"; the page also links the
             Chapter 7 random-walk Lisp (online.lisp, offline.lisp) the
             previous lesson used. Code is "made available as is".
Locators:    "Chapter 9: On-policy Prediction with Approximation" list.
```

### 4. Sutton, FAwalknew.lisp

```text
URL:         http://incompleteideas.net/book/code/FAwalknew.lisp
Kind:        primary: Sutton's own code for the same walk with other features.
Establishes: identical random-walk, dp and compute-d routines to source 2 (so
             Example 9.1's rules are the same in both); here compute-d
             normalizes d to μ (eq. 9.3); it has state aggregation, tile coding,
             polynomial and Fourier features; its learning curves record
             residual-naive-error, an unweighted RMS over states; its nstep
             plot sets y-limits .25-.55, the range of Figure 9.2 right.
Locators:    lines 176-191 (compute-d with normalization), 193-204 (weighted
             and unweighted errors), 206-247 (learning-curve, nstep), 249-302
             (commented invocations, n = 1000 labelled "lc-mc-...").
```

### 5. Tsitsiklis and Van Roy (1997), "An Analysis of Temporal-Difference Learning with Function Approximation"

```text
URL:         https://doi.org/10.1109/9.580874 (IEEE Xplore, gated)
             Free full text from the first author's MIT page:
             https://web.mit.edu/jnt/www/Papers/J063-97-bvr-td.pdf
Kind:        primary: the authors prove the theorem.
Establishes: firsthand the w.p.1 convergence of linear TD(λ) and the error
             bound, for a discounted, non-terminating chain.
Locators:    IEEE Trans. Automatic Control 42(5):674-690, May 1997.
             Abstract and Section I, pp. 674-675; setting, Section II, p. 676;
             intuition, Section III, pp. 676-678; Theorem 1 and Assumptions
             1-4, Section IV, p. 679 (footnote 1 on p. 679); finite state
             spaces, Section VII, p. 685; importance of on-line sampling,
             Section IX, p. 686; nonlinear divergence, Section X, p. 687.
```

Paraphrase:

- Setting (abstract; Section II, p. 676): an irreducible aperiodic Markov chain,
  "a single endless trajectory", costs g(i,j) per transition, discount factor α
  ∈ (0,1). Notation: their α is the discount (S&B's γ), their γ_t is the step
  size (S&B's α), costs replace rewards, J* is the cost-to-go (S&B's v_π), Φr is
  the linear approximation (S&B's Xw), D is diag of steady-state probabilities.
- Section I, p. 675: "Though absorbing (and typically finite state) Markov
  chains have been the dominant setting for past analyses, we find the
  infinite-horizon framework to be the most natural ... the ideas used in our
  analysis can be applied to the simpler context of absorbing Markov chains.
  Though this extension is omitted from this paper, it can be found in [16]"
  ([16] = Bertsekas and Tsitsiklis, Neuro-Dynamic Programming, 1996). "At about
  the same time ... Gurvits [17] independently established convergence with
  probability one in the context of absorbing Markov chains" ([17] = private
  communication, 1996). Contribution 1 claims "the first such result that
  handles the case of 'compact representations' ... in which there are fewer
  parameters than states."
- Section III, pp. 677-678: Π is the projection onto the span of the basis
  functions in the D-weighted norm, "the solution to the weighted linear
  least-squares problem" with "the error associated with each state ... weighed
  by the frequency with which the state is visited." TD(1)'s deterministic
  variant is steepest descent toward ΠJ*; for λ < 1 "the error function changes
  from one time step to the next, and therefore it is not a true steepest
  descent method." If states are sampled with a distribution other than the
  steady state, Π need not be a nonexpansion in the norm where T^(λ) contracts,
  and "the algorithm might not converge at all".
- Theorem 1, p. 679, under Assumptions 1-4 (irreducible aperiodic chain with
  finite-variance costs; linearly independent basis functions with finite
  second moments; a mixing condition automatically met for finite chains;
  step sizes positive, nonincreasing, predetermined, Σγ_t = ∞, Σγ_t² < ∞):
  (1) J* ∈ L2(S,D); (2) for any λ ∈ [0,1], linear TD(λ) converges with
  probability one; (3) the limit r* is the unique solution of ΠT^(λ)(Φr*) =
  Φr*; (4) ‖Φr* − J*‖_D ≤ (1 − λα)/(1 − α) ‖ΠJ* − J*‖_D.
- Footnote 1, p. 679: "It has been brought to our attention by V. Papavassiliou
  that this bound can be improved to ‖Φr* − J*‖_D ≤ (1 − λα)/√((1 − α)(1 + α −
  2λα)) ‖ΠJ* − J*‖_D." At λ = 0 this is 1/√(1 − α²).
- p. 679-680: with lookup-table features the result recovers earlier tabular
  results; Dayan [8] had "a weak form of convergence (convergence in the mean)"
  for general linear features.

### 6. Bertsekas, Dynamic Programming and Optimal Control, 3rd ed., Vol. II, Chapter 6 "Approximate Dynamic Programming" (online update)

```text
URL:         https://web.mit.edu/dimitrib/www/dpchapter.pdf
Kind:        primary: the author's own analysis (Bertsekas is a co-author of
             the 1996 book S&B cite for the episodic bound). The chapter calls
             itself "work in progress" that "more than likely contains errors";
             title page dated November 11, 2011.
Establishes: firsthand the episodic (stochastic shortest path) form of the
             projected equation and why its TD(0) bound is weaker; the
             Pythagorean bound for the discounted case.
Locators:    Section 6.3.1, Prop. 6.3.1-6.3.2 and the note after it,
             pp. 360-362; Section 6.6 "Stochastic Shortest Path Problems",
             Prop. 6.6.1 and the bounds after it, pp. 458-462.
```

Paraphrase:

- Prop. 6.3.2, p. 361 (discounted): ‖J_μ − Φr*‖_ξ ≤ 1/√(1 − α²) ‖J_μ − ΠJ_μ‖_ξ,
  proved by the Pythagorean theorem plus the contraction of ΠT in the
  steady-state-weighted norm ξ. The note after it (pp. 361-362): the
  proposition holds "if T is any (possibly nonlinear) contraction with respect
  to the Euclidean norm of the projection".
- Section 6.6, pp. 458-459 (episodic): no discounting, a cost-free termination
  state 0, a proper policy so all other states are transient, φ(0) = 0,
  trajectories restart from a fixed start distribution q0. The projection
  weight is q(i) = Σ_t P(i_t = i), the expected visits per trajectory, which is
  S&B's η in eq. 9.2. T J = g + PJ with P over the nonterminal states.
- p. 460: ‖PJ‖_q ≤ ‖J‖_q always. "Let λ = 0. We use a different argument
  because T is not necessarily a contraction with respect to ‖·‖_q." Bracketed
  note: "if q0(i) > 0 for all i ... P and hence T is a contraction with respect
  to ‖·‖_q." ΠT is still a contraction "with respect to a different norm".
- p. 461-462: for λ > 0 the bound is 1/√(1 − α_λ²) in the q-norm; for λ = 0,
  ‖J_μ − Φr0*‖ ≤ 1/(1 − α0) ‖J_μ − ΠJ_μ‖ in the unspecified norm in which ΠT
  contracts, with modulus α0.

### 7. Sutton and Barto, errata page

```text
URL:         http://incompleteideas.net/book/errata.html
Kind:        primary: the authors' corrections.
Establishes: the only Chapter 9 correction listed for the 2020 second printing
             is a typo on p. 211-212 ("the length the interval"); the p. 198,
             202, 204, 206 and 208 errata belong to the 2018 first printing and
             are already fixed in RLbook2020.pdf (checked: p. 202 reads
             "E[U_t|S_t = s] = v_π(s)", p. 206 reads "R^{d×d}"). Also documents
             the #page=X link form.
Locators:    "Errata for the second printing (2020)"; "Errata for the first
             printing (2018)"; "Notes".
```

### 8. Zhang, Python re-implementation, chapter09/random_walk.py

```text
URL:         https://github.com/ShangtongZhang/reinforcement-learning-an-introduction/blob/master/chapter09/random_walk.py
             (read through raw.githubusercontent.com; the blob page is the
             document's own address)
Kind:        secondary: a third party's re-implementation, linked from the
             authors' code page; no authorship of the example.
Establishes: only that an independent re-implementation also used α = 2e-4 and
             1e5 episodes for Figure 9.2 left (lines 293-298), and α = 2e-5,
             1e5 episodes for Figure 9.1 (lines 261-269). It repeats; it does
             not establish what Sutton ran.
Locators:    lines 16-33 (constants: states 1..1000, start 500, STEP_RANGE
             100), 261-305 (figure_9_1, figure_9_2_left).
```

## Contradictions

1. **Eq. 9.14 does not cover the commission's walk as written.** The book
   states it "in the continuing case" with γ < 1 (p. 207), and Tsitsiklis and
   Van Roy prove it for a discounted, non-terminating chain (p. 676, α ∈
   (0,1)). The walk is episodic and undiscounted (p. 125 via "As usual";
   source 2 has no discount). At γ = 1 the factor 1/(1−γ) is undefined. The
   book itself says the episodic bound is "slightly different but related"
   and sends the reader to Bertsekas and Tsitsiklis (1996) (p. 208). Bertsekas's
   2011 chapter (source 6, p. 460-462) adds that for TD(0) on an episodic task
   with a single start state, the bound holds in some norm in which ΠT
   contracts, not necessarily the visit-weighted norm in which VE is measured.
   The page can state 9.14 as the general result for discounted continuing
   tasks and must not present 1/(1−γ) as this walk's bound.

   Researcher arithmetic, not a source, for the writer to reproduce if the page
   wants a number: on this walk with 10 groups, P (nonterminal transitions) is a
   contraction in the μ-norm with modulus β = ‖D^{1/2} P D^{-1/2}‖₂ ≈ 0.9959.
   Bertsekas's Prop. 6.3.2 argument (p. 361, "holds if T is any ...
   contraction" in the projection norm) then gives VE(w_TD) ≤ 1/(1−β²) min VE ≈
   122 × min VE. The measured ratio is about 4.6 (see Numbers). Any form of the
   bound is loose here by a factor above 20.

2. **9.14 and Tsitsiklis and Van Roy's Theorem 1 use different constants.**
   9.14 bounds VE, a squared norm, by 1/(1−γ). Theorem 1(4) at λ = 0 bounds the
   unsquared norm by 1/(1−α), which squared gives 1/(1−γ)². 9.14 follows from
   the improved bound in their footnote 1 (1/√(1−γ²), squared 1/(1−γ²) ≤
   1/(1−γ)), which is also Bertsekas's Prop. 6.3.2. A page that cites 9.14 and
   links the paper should not say Theorem 1 prints 9.14 verbatim.

3. **"Introduced linear TD's convergence result" needs care.** S&B's
   bibliographic remarks (p. 237) credit Dayan (1992) with the first
   convergence (in the mean) for general dependent features and Tsitsiklis and
   Van Roy (1997) with the w.p.1 result and the error bound. The paper itself
   claims the first w.p.1 result with fewer parameters than states (p. 675),
   omits the absorbing-chain (episodic) case, and credits Gurvits with an
   independent absorbing-chain result (p. 675). Linking Tsitsiklis and Van Roy
   where the lesson states that linear TD converges, and to the error bound, is
   accurate. Saying they proved it for episodic tasks like this walk is not.

4. **Constant step sizes versus the convergence conditions.** The book's
   guarantees for gradient MC (pp. 202, 205) and the paper's Assumption 4 (p.
   679) require decreasing step sizes. The book's own runs use constant α
   (2 × 10⁻⁵ for MC, p. 203) and call the results "close to the global minimum"
   (p. 204) and "near-asymptotic" (p. 208). A constant-α run hovers near
   w_MC or w_TD rather than converging to it. My two throwaway seeds (Numbers)
   put the final weights within about 0.02 (MC) and 0.013 (TD) of the exact
   solutions.

5. **"Not a gradient of any fixed objective" is stronger than what I could
   source.** The book says bootstrapping methods "are not in fact instances of
   true gradient descent (Barnard, 1993)" (p. 202) and "only the Monte Carlo
   methods are true SGD methods" (p. 270). Barnard (1993) was not opened. The
   page can carry the stronger claim by its own derivation: the expected TD(0)
   update is α(b − Aw); if it were −α∇f(w) for some twice-differentiable f, then
   ∇²f = A would be symmetric. On this walk A = XᵀD(I − P)X is not symmetric
   (researcher check: ‖A − Aᵀ‖_F / ‖A‖_F ≈ 0.116; e.g. A[5,6] ≈ −0.0488 vs
   A[6,5] ≈ −0.0428 with 1-based group indices). That argument covers the
   expected update on this walk; it is not a quote from any source.

6. **"μ decides where each step is accurate" holds within groups for MC, not
   across groups.** The book shows μ's effect as a within-group shift: each MC
   step sits at the μ-weighted mean of v_π over its group, pulled toward the
   heavier states (p. 204). Across groups the MC errors are nearly equal
   (per-group RMS 0.048-0.057, Numbers), because each group's error is set by
   the slope of v_π over 100 states, not by the group's μ mass. For TD the
   per-group error is not ordered by μ either: lowest in groups 501-700 (0.062),
   0.103 in the start-state group 401-500, which holds the most μ mass. No
   source discusses per-group TD errors.

7. **The TD staircase is not symmetric about the start state.** Exact w_TD for
   groups 401-500 and 501-600 is −0.001 and +0.122; MC gives −0.087 and +0.093.
   The book's Figure 9.2 left, read off the plot, shows about −0.03 and +0.09, so
   the asymmetry is in the authors' run too. State 500 is in group 401-500,
   carries 1.37% of the time steps (7.7% of its group's μ mass), and is not the
   exact centre (v_π(500) ≈ −0.0009). No source explains the asymmetry; per the
   series prompt the page should say so briefly if it shows it.

8. **Code-page attributions are loose (affects provenance only).** The code
   page credits aggreg-walknew.lisp with Figures 9.1, 9.2 and 9.5, but that file
   has no Fourier or polynomial features (Figure 9.5 is "Fourier basis vs
   polynomials", p. 214), and its `residual-error` is weighted by unnormalized
   visit counts, not the unweighted RMS the book says Figure 9.2 right uses
   (p. 209). FAwalknew.lisp has those features, an unweighted error and the
   right panel's y-range. "Figure 9.15" on the code page is the book's Figure
   9.10 ("Why we use coarse coding", p. 218); Figure 9.15 is a deep
   convolutional network. Example 9.1's rules are identical in both files.

## Numbers

Book figures:

```text
Figure: 1000 nonterminal states, start state 500, jumps ±1..±100 each 1/200
Owner:  Sutton and Barto p. 203; aggreg-walknew.lisp lines 88-95
Scope:  Example 9.1 rules

Figure: termination probability 0.5 from state 1 (left); 0.25 from state 950 (right)
Owner:  Sutton and Barto p. 203
Scope:  per step from that state

Figure: rewards −1 (left exit), +1 (right exit), 0 otherwise; undiscounted
Owner:  Sutton and Barto p. 203 and p. 125; aggreg-walknew.lisp lines 18-19, 60-61
Scope:  every transition

Figure: 10 groups of 100 states (1-100, 101-200, ...)
Owner:  Sutton and Barto p. 203
Scope:  Example 9.1 and Figure 9.2 left

Figure: gradient MC α = 2 × 10⁻⁵, 100,000 episodes
Owner:  Sutton and Barto p. 203
Scope:  Figure 9.1, one final value function

Figure: semi-gradient TD(0) α = 0.0002, 100,000 episodes, 1 run
Owner:  aggreg-walknew.lisp commented invocation, lines 156-157 (not stated in the book)
Scope:  presumed Figure 9.2 left; Zhang's re-implementation uses the same

Figure: μ(500) ≈ 1.37%; each state reachable in one step from 500 (400-499, 501-600) ≈ 0.17%; μ(1), μ(1000) ≈ 0.0147%; μ(100) > 3 × μ(1)
Owner:  Sutton and Barto p. 204
Scope:  fraction of all time steps, on-policy, episodic (eq. 9.3)

Figure: Figure 9.1 distribution axis 0 to 0.0137, tick at 0.0017; value axis −1 to 1
Owner:  Sutton and Barto p. 204 (figure)
Scope:  right-side scale is μ

Figure: Figure 9.2 right: 20 groups of 50, first 10 episodes, unweighted RMS over 1000 states, 100 runs, n = 1..512, α in [0, 1]
Owner:  Sutton and Barto pp. 208-209
Scope:  n-step comparison, outside this lesson

Figure: VE(w_TD) ≤ 1/(1−γ) min_w VE(w)
Owner:  Sutton and Barto eq. 9.14 p. 207 (attributed to Tsitsiklis and Van Roy 1997)
Scope:  continuing tasks, γ < 1, on-policy, linear features
```

Researcher cross-check by exact linear solve and two simulations. These are not
citable; the writer's own printed output replaces them. Method: P is the
1000×1000 substochastic matrix of nonterminal transitions, r the expected
one-step reward (−1/200 per off-left jump, +1/200 per off-right jump); v_π =
(I − P)⁻¹r; η = (I − Pᵀ)⁻¹e_500; μ = η/Ση; X the 1000×10 one-hot group matrix;
D = diag(μ); w_MC = (XᵀDX)⁻¹XᵀDv_π; A = XᵀD(I − P)X, b = XᵀDr, w_TD = A⁻¹b (the
episodic form, with x(terminal) = 0, matching Bertsekas Section 6.6).

```text
Figure: Σ η = 83.15 expected steps per episode; η(500) = 1.139 visits
Owner:  researcher exact solve
Scope:  per episode from state 500

Figure: μ(500) = 1.369%; μ(499) = μ(501) = 0.1726%; μ(400) = 0.1566%; μ(1) = 0.01471%; μ(1000) = 0.01469%; μ(100)/μ(1) = 3.15
Owner:  researcher exact solve (agrees with book p. 204 at its rounding; the
        one-step neighbours run from 0.157% at 400/600 to 0.173% at 499/501,
        so the book's "about 0.17%" is the upper end)
Scope:  fraction of time steps

Figure: v_π(1) = −0.9220, v_π(100) = −0.7542, v_π(500) = −0.0009, v_π(900) = +0.7520, v_π(1000) = +0.9220
Owner:  researcher exact solve
Scope:  undiscounted, probability-weighted outcome

Figure: μ mass per group (1..10): 0.0291 0.0641 0.0996 0.1349 0.1787 0.1666 0.1346 0.0994 0.0639 0.0291
Owner:  researcher exact solve
Scope:  sums to 1

Figure: w_MC (μ-weighted group means of v_π): −0.8301 −0.6516 −0.4661 −0.2791 −0.0867 +0.0928 +0.2791 +0.4661 +0.6516 +0.8301
Owner:  researcher exact solve
Scope:  minimizer of VE over 10-group aggregation

Figure: unweighted group means of v_π: −0.8456 −0.6603 −0.4717 −0.2830 −0.0943 +0.0943 +0.2830 +0.4717 +0.6603 +0.8456
Owner:  researcher exact solve
Scope:  the "unweighted average" the book contrasts on p. 204

Figure: w_TD = A⁻¹b: −0.6932 −0.4805 −0.3033 −0.1458 −0.0009 +0.1224 +0.2497 +0.3881 +0.5437 +0.7305
Owner:  researcher exact solve
Scope:  TD fixed point, 10 groups, on-policy, γ = 1

Figure: VE(w_MC) = 0.00296 (root VE 0.0544); VE(w_TD) = 0.01363 (root VE 0.1167); ratio 4.61
Owner:  researcher exact solve
Scope:  μ-weighted, 1000 states

Figure: per-group RMS error, MC: 0.048 0.054 0.054 0.054 0.057 0.054 0.054 0.054 0.054 0.048
Owner:  researcher exact solve
Scope:  μ-weighted within each group

Figure: per-group RMS error, TD: 0.145 0.179 0.172 0.144 0.103 0.062 0.062 0.095 0.121 0.111
Owner:  researcher exact solve
Scope:  μ-weighted within each group

Figure: β = ‖D^{1/2}PD^{-1/2}‖₂ = 0.9959; 1/(1−β²) = 122.5; spectral radius of P = 0.985; min eigenvalue of A + Aᵀ = 0.0022 (A positive definite)
Owner:  researcher exact solve
Scope:  see Contradictions 1

Figure: simulated final weights, α_MC = 2e-5 and α_TD = 2e-4, 100,000 episodes each, seeds 1 and 2:
        seed 1 MC −0.828 −0.663 −0.480 −0.290 −0.095 +0.093 +0.277 +0.460 +0.645 +0.826
        seed 1 TD −0.698 −0.487 −0.306 −0.150 −0.011 +0.116 +0.243 +0.381 +0.539 +0.723
        seed 2 MC −0.825 −0.663 −0.492 −0.309 −0.107 +0.074 +0.265 +0.463 +0.651 +0.820
        seed 2 TD −0.695 −0.485 −0.310 −0.157 −0.013 +0.112 +0.243 +0.381 +0.539 +0.729
Owner:  researcher throwaway simulation (pure Python, about 15 s for both methods)
Scope:  one run each; final weights after the last episode
```

## Limits

- The episodic bound S&B cite (Bertsekas and Tsitsiklis, 1996, Neuro-Dynamic
  Programming) was not opened; the book is not freely available. Bertsekas's
  2011 chapter (source 6) stands in for it and was read.
- No source states a numeric error bound for TD(0) on the 1000-state walk. The
  factor ≈ 122 is researcher arithmetic resting on Bertsekas's p. 361 note.
- The book does not state the step size or episode count for Figure 9.2 left.
  Only Sutton's code comment (α = 0.0002, 100,000 walks) and Zhang's
  re-implementation give them.
- Barnard (1993), IEEE Trans. SMC 23(2):357-365, the source S&B cite for TD not
  being true gradient descent, was not opened. Its exact wording is unverified.
- Sutton's code is "made available as is"; nothing confirms it is the exact
  version that drew Figures 9.1 and 9.2.
- incompleteideas.net failed TLS with a self-signed certificate over HTTPS from
  this environment; all its URLs above are http://, which served every file.
- Everything else the brief asked for was established.

## Source assets

```text
Asset: Figure 9.1, Sutton and Barto p. 204 (PDF page 226)
Shows: the gradient-MC staircase over the true v_π line, with μ drawn underneath
       on a right-hand scale (0 to 0.0137); the outer steps visibly sit off the
       group midpoints toward the heavier states.
Crop:  keep both axis scales, the μ silhouette and its label, and the caption;
       credit the book. The lesson's own SVG of its own run replaces it per the
       series prompt; use the original only for comparison.

Asset: Figure 9.2 left panel, Sutton and Barto p. 208 (PDF page 230)
Shows: the semi-gradient TD(0) staircase flatter than v_π, above it on the left
       and below it on the right; the 401-500 and 501-600 steps straddle zero
       unevenly.
Crop:  left panel only; omit the n-step right panel (outside the lesson); keep
       the "Left:" sentence of the caption.

Asset: Figure 11.3, Sutton and Barto p. 267 (PDF page 289)
Shows: the representable plane, v_π above it, Πv_π (min VE) and w_TD
       (PBE = 0) as different points.
Crop:  cannot cleanly drop the BE, PBE and TDE labels, which the course has not
       taught; a drawing made for the lesson is the better choice.

Asset: Tsitsiklis and Van Roy (1997)
Shows: None found that serves this lesson (its only figure-like content concerns
       nonlinear divergence, Section X).

Asset: Bertsekas Chapter 6, Figure 6.3.1, p. 361
Shows: ΠT as a contraction because Π is nonexpansive (discounted case).
Crop:  labels are dense and the figure concerns the discounted case; None
       recommended.

Asset: aggreg-walknew.lisp, FAwalknew.lisp, code2nd.html, errata.html
Shows: None found (text only).
```

## Go-deeper candidates

1. Tsitsiklis and Van Roy (1997), Section III, pp. 676-678, then Theorem 1 on
   p. 679: why weighting by the on-policy distribution makes ΠT a contraction,
   and what goes wrong with other sampling. Read for the projection view of the
   TD fixed point.
2. Sutton and Barto, the box "Proof of Convergence of Linear TD(0)", pp.
   206-207: positive definiteness of A from its column sums, (1−γ)μᵀ. Read for
   the one-page reason on-policy linear TD(0) is stable.
3. Bertsekas, DP&OC Vol. II Chapter 6 (2011 update), Section 6.6, pp. 458-462:
   the same analysis for episodic tasks with visit-count weighting, the setting
   of the 1000-state walk. Read for why the episodic TD(0) bound differs.
4. Sutton and Barto Section 11.4 "Linear Value-function Geometry", pp. 266-269,
   with Figure 11.3: Monte Carlo's Πv_π and TD's w_TD as two points of one plane.
   Caution: it sits in the off-policy chapter beside deadly-triad material and
   introduces BE and PBE, which the next lesson may want for itself.

## Discarded

```text
https://arxiv.org/pdf/1906.07073 (Nota and Thomas, "Is the Policy Gradient a Gradient?"): proves a policy-gradient update field is not a gradient via mixed partials; it is about policy gradients, not TD, so citing it for the TD claim would misattribute.
https://web.mit.edu/dimitrib/www/dpchapter.html: a landing page for Bertsekas's books that does not describe the chapter; the PDF is recorded instead.
http://incompleteideas.net/book/code/FAwalknew.lisp as the Example 9.1 code: kept as source 4 for provenance, rejected as the primary code for the lesson because the book's code page assigns Example 9.1 to aggreg-walknew.lisp and that file's defaults (m = 10) match it.
```
