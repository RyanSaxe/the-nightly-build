# Evidence record: reinforcement-learning/finding-optimal-policies (researcher 01)

Retrieval date for every source below: 2026-11-01. Each source was downloaded
and read from the document itself, not from a search snippet. Where a page was
a scan, I read the page image. Printed page numbers are the numbers printed on
the page, not PDF page indexes. The offset is stated per source.

## Read this first: six things the brief or commission gets wrong or leaves open

1. **AlphaGo Zero does not say the network does policy evaluation.** The brief
   describes the loop as "policy improvement by search, policy evaluation by the
   network". The paper says search is the improvement operator and that
   self-play games played with search are the evaluation operator. The network
   is the function approximator both results are trained into. See item 6.
2. **Bellman's 1957 paper does not contain the discounted optimality equation.**
   "A Markovian Decision Process" works with a finite-stage max recurrence and
   its asymptotic (average-reward) behaviour. No discount factor appears. The
   discounted `v_*` equation with a `max` is in Sutton and Barto (3.19). See
   item 4.
3. **On the lesson 1 grid, the first improvement step does not flip cell 13.**
   Under `v_π`, the hand-drawn action at cell 13 (up) is already the best of the
   four. The only cell that flips in the first step is cell 14 (up to right).
   Cell 13 flips in the second step, after cell 14's new value propagates. The
   commission's worked instance for item 1 ("which action beats the one the
   hand-drawn policy actually takes" at cell 13) has no answer at cell 13. Use
   cell 14 for that instance. Numbers in the arithmetic section below.
4. **The optimal policy on this grid is not unique.** At cells 9 and 12 the
   actions up and right have exactly equal optimal action values. Tie-breaking
   changes the number of policy-iteration rounds (3 or 4 in my cross-check) and
   whether VI's arrow grid equals PI's arrow grid. The lesson has to
   state a tie rule, or compare action values instead of arrows.
5. **"The optimal policy beats the hand-drawn one at every cell" is false.** Six
   cells (0, 1, 2, 4, 5, 7) have identical value under the hand-drawn policy and
   under `π_*` (difference exactly 0.0 in my run). Under both policies those
   cells never reach the bottom two rows, so the values cannot differ. The
   improvement is strict at the eight cells of rows 2 and 3. The commission
   also asks to show that "every cell's value rises" after one improvement
   step. After the first step, cells 8 to 15 all rise strictly and cells 0 to 7
   are unchanged, so the componentwise statement is a weak inequality.
6. **Howard's chapter 4 is the average-reward (gain) version.** The discounted
   version, which matches this lesson's `γ`, is chapter 7, and Howard writes the
   discount as `β`. Cite chapter 7 for the discounted routine and chapter 4
   where the iteration cycle and stopping rule are first stated.

## Item 1. Policy improvement theorem

**Claim.** If `q_π(s, π'(s)) ≥ v_π(s)` for all `s`, then `v_{π'}(s) ≥ v_π(s)` for
all `s`, strictly wherever the first inequality is strict. The greedy policy
`π'(s) = argmax_a q_π(s,a)` satisfies the hypothesis.

**Primary.** Sutton and Barto, *Reinforcement Learning: An Introduction*, 2nd
ed., section 4.2 "Policy Improvement", printed pp. 76 to 79.
- Theorem statement, p. 78. Hypothesis (4.7), conclusion (4.8).
- One-step argument, p. 78: the chain that starts at `v_π(s) ≤ q_π(s, π'(s))`,
  expands with (4.6), re-applies (4.7) one step deeper, and repeats until it
  reaches `v_{π'}(s)`. Its steps are labelled "(by (4.6))" and "(by (4.7))".
- Greedy construction, p. 79, equation (4.9).
- Strictness / optimality case, p. 79.

Verbatim, p. 78:
> Let π and π′ be any pair of deterministic policies such that, for all s ∈ S,
> q_π(s, π′(s)) ≥ v_π(s). (4.7)
> Then the policy π′ must be as good as, or better than, π. That is, it must
> obtain greater or equal expected return from all states s ∈ S:
> v_π′(s) ≥ v_π(s). (4.8)
> Moreover, if there is strict inequality of (4.7) at any state, then there must
> be strict inequality of (4.8) at that state.

Verbatim, p. 78, the argument in prose: "Starting from (4.7), we keep expanding
the q_π side with (4.6) and reapplying (4.7) until we get v_π′(s)". The chain
carries `γ` in the printed page: `E_π'[R_{t+1} + γ R_{t+2} + γ² v_π(S_{t+2}) | S_t = s]`
and so on, ending at `E_π'[R_{t+1} + γR_{t+2} + γ²R_{t+3} + ... | S_t = s] = v_π'(s)`.

Verbatim, p. 79:
> By construction, the greedy policy meets the conditions of the policy
> improvement theorem (4.7), so we know that it is as good as, or better than,
> the original policy.

Strictness unless optimal, p. 79: if `π'` is no better than `π`, then `v_π = v_π'`,
and (4.9) gives `v_π'(s) = max_a Σ p(s',r|s,a)[r + γ v_π'(s')]`, which "is the same
as the Bellman optimality equation (4.1)". Then:
> Policy improvement thus must give us a strictly better policy except when the
> original policy is already optimal.

**Independent statement with a different proof.** Van Roy, MS&E 235A Lecture
Notes 06 "Policy Iteration" (20 Oct 2025), section 2, p. 3, Theorem 3: for `π'`
greedy with respect to `V_π`, `V_π ≤ V_π'`, and if `V_π = V_π'` then
`V_π = V_*`. Proof by the operator chain `V_π = T_π V_π ≤ T V_π = T_π' V_π`, then
`V_π ≤ T_π' V_π ≤ T_π'² V_π ≤ ... ≤ V_π'`, which uses monotonicity of `T_π'`
(Theorem 2, p. 3). This is the same argument as Sutton and Barto's telescoping
chain, written with operators.

URLs, read 2026-11-01:
- Sutton and Barto: http://incompleteideas.net/book/RLbook2020.pdf (the author's
  free PDF; the copyright page reads "© 2018, 2020"). **PDF page index = printed
  page + 22.** I could not compare against the 2018 print; the page numbers
  here are those of this PDF.
- Van Roy lecture 06: https://web.stanford.edu/class/msande235a/files/lectures/lecture06.pdf

**Caution.** The theorem is stated for deterministic policies (p. 78). The book
says (p. 79) it "carries through as stated for the stochastic case" without
proof. The lesson's policies are deterministic, so this does not bite.

## Item 2. Action value `q_π(s,a)` and its one-step relation to `v_π`

**Claim.** `q_π(s,a)` is the expected return from taking `a` in `s` and then
following `π`. In terms of `v_π`, it is the expectation over the next reward and
the discounted next-state value.

**Source.** Sutton and Barto, ch. 3, section 3.5 "Policies and Value Functions",
printed p. 58, equation (3.13), after `v_π` in (3.12):
> Similarly, we define the value of taking action a in state s under a policy π,
> denoted q_π(s, a), as the expected return starting from s, taking the action a,
> and thereafter following policy π:
> q_π(s, a) ≐ E_π[G_t | S_t = s, A_t = a] = E_π[ Σ_{k=0}^∞ γ^k R_{t+k+1} | S_t = s, A_t = a ]. (3.13)

"We call q_π the action-value function for policy π." (p. 58.)

One-step form in terms of `v_π`, section 4.2, printed p. 78, equation (4.6):
> q_π(s, a) ≐ E[R_{t+1} + γ v_π(S_{t+1}) | S_t = s, A_t = a]
> = Σ_{s',r} p(s', r | s, a) [ r + γ v_π(s') ]. (4.6)

The book's `p(s', r | s, a)` is the four-argument dynamics function. The
lesson's grid has `R[s']` paid on arrival, so it reads
`q(s,a) = Σ_{s'} P(s'|s,a) [R(s') + γ v(s')]`, which is (4.6) with the reward
determined by `s'`.

Related equations that the writer may want to name:
- Bellman equation for `v_π`, (3.14), p. 59, and its iterative form (4.5), p. 74.
- `v_π(s) = Σ_a π(a|s) q_π(s,a)` is **Exercise 3.12** (p. 58). It has no numbered
  equation. Do not cite an equation number for it.
- The Bellman equation for `q_π` in terms of `q_π` is **Exercise 4.3** (p. 76),
  also unnumbered. (Lesson 1's evidence record says the same.)

Why `v_π` alone does not rank actions, pp. 76 to 78: the improvement question is
whether `q_π(s,a) > v_π(s)`. Verbatim, p. 78:
> The key criterion is whether this is greater than or less than v_π(s).

URL and offset as in item 1.

## Item 3. Policy iteration: the loop, finite termination, origin

**Claim.** Alternate evaluation `E` and improvement `I`
(`π_0 →E v_π0 →I π_1 →E ... →I π_* →E v_*`). Each policy is strictly better than
the last unless it is optimal, and a finite MDP has finitely many deterministic
policies, so the loop stops after finitely many rounds.

**Sutton and Barto, section 4.3 "Policy Iteration", printed pp. 80 to 82.**
Verbatim, p. 80:
> Each policy is guaranteed to be a strict improvement over the previous one
> (unless it is already optimal). Because a finite MDP has only a finite number
> of deterministic policies, this process must converge to an optimal policy and
> the optimal value function in a finite number of iterations.

The algorithm box "Policy Iteration (using iterative policy evaluation)" is on
p. 80, with the stopping rule `policy-stable` in step 3. The warm-start remark
is on p. 80: "each policy evaluation, itself an iterative computation, is started
with the value function for the previous policy."

Tie-breaking bug, Exercise 4.4, printed p. 82:
> The policy iteration algorithm on page 80 has a subtle bug in that it may
> never terminate if the policy continually switches between two or more
> policies that are equally good.

This matters on the lesson's grid because of the ties at cells 9 and 12 (see
the arithmetic section).

"Policy iteration often converges in surprisingly few iterations", p. 82.

**A source that states the finite-termination theorem formally.** Van Roy,
Lecture Notes 06, p. 3, Theorem 4: for a finite-state, finite-action MDP and
`γ ∈ [0,1]`, for any stationary `π_0` there is a finite `k` with `V_{π_k} = V_*`.
Proof, verbatim: "Since each policy πk is a deterministic stationary policy and
there are a finite number of deterministic stationary policies, the sequence
must converge." The lecture notes use `γ ∈ [0,1]` in this theorem. URL in item 1.

**Origin.** Ronald A. Howard, *Dynamic Programming and Markov Processes* (The
Technology Press of M.I.T. and John Wiley & Sons, 1960; copyright page, LoC card
60-11030). Read from a scan with an OCR layer:
https://gwern.net/doc/statistics/decision/1960-howard-dynamicprogrammingmarkovprocesses.pdf
(a third-party host of the scan; I know of no publisher URL). **PDF page index =
printed page + 10.** My quotes below are from the OCR text, with OCR spacing
errors fixed ("wecall" read as "we call"). I checked the page layout and
equation numbers against the contents list.

Where the pieces are introduced:
- **Chapter 4**, "The Policy-Iteration Method for the Solution of Sequential
  Decision Processes", printed pp. 32 to 43. Value-determination operation
  (p. 34 onward), policy-improvement routine p. 37, iteration cycle p. 38
  (Fig. 4.2), stopping rule and properties p. 39, proof pp. 42 to 43. This
  chapter treats the undiscounted average-reward case ("gain" `g`).
- **Chapter 7**, "The Sequential Decision Process with Discounting", printed
  pp. 76 to 91. This is the discounted version that matches the lesson. The
  value-determination operation is at p. 81 with the linear system (7.9) on
  p. 82, the policy-improvement routine at p. 83, the iteration cycle in
  Fig. 7.1 on p. 84, and the proof at pp. 86 to 87.
- **Chapter 3**, "The Solution of the Sequential Decision Process by Value
  Iteration", printed pp. 26 to 31. Howard names "the value-iteration method"
  on p. 30 and "the value iteration equation" (3.1) on p. 29.

Verbatim, ch. 7, p. 83, the routine in the discounted setting:
> Suppose that the present values for an arbitrary policy have been determined.
> Then a better policy, one with higher present values in every state, can be
> found by the following procedure, which we call the policy-improvement
> routine.
> For each i, find the alternative k that maximizes
> q_i^k + β Σ_j p_ij^k v_j
> using the v_j determined for the original policy.

(Howard's `q_i^k` is the expected immediate reward, so his "test quantity" is
the lesson's `q_π(s,a)`.) Value determination, ch. 7, p. 82, equation (7.9):
`v_i = q_i + β Σ_j p_ij v_j`, i = 1,...,N, a linear system in the present values.
Howard also writes the matrix form `v = (I − βP)^{-1} q` as (7.8), p. 81,
the same as lesson 1's direct solve.

Verbatim, ch. 7, p. 84, stopping:
> The iteration cycle will be able to make policy improvements until the
> policies on two successive iterations are identical. At this point it has
> found the optimal policy, and the problem is completed.

Verbatim, ch. 4, p. 39 (stopping rule, with his tie rule):
> The optimal policy has been reached (g is maximized) when the policies on two
> successive iterations are identical. In order to prevent the policy-improvement
> routine from quibbling over equally good alternatives in a particular state,
> it is only necessary to require that the old d_i be left unchanged if the
> test quantity for that d_i is as large as that of any other alternative in the
> new policy determination.

That is the "keep the old action on ties" rule. Howard stated it in 1960. It
answers the Exercise 4.4 bug and is what I used in the cross-check below.

Howard's improvement proof for the discounted case, p. 87, equation (7.14):
`v^Δ = (I − βP^B)^{-1} γ`, where `γ` is the vector of improvements in the test
quantity (Howard's symbol, not the discount). Because `(I − βP^B)^{-1}` has
non-negative entries and at least 1 on the diagonal (p. 82), any improvement
raises at least one value and lowers none. Verbatim, p. 87:
> Therefore, the policy-improvement routine must increase the present values of
> at least one state and cannot decrease the present values of any state.

and
> It follows that when the policy-improvement routine has converged on a policy
> no other policy can have higher present values.

This is a second, linear-algebra proof of the improvement theorem. It is worth
offering beside Sutton and Barto's telescoping chain, because lesson 1 already
taught `(I − γQ)^{-1}` and the lesson can reuse it. Caveat on symbol clash: in
Howard `γ` is the improvement vector. Do not carry it over.

**Finite termination in Howard.** He counts policies on pp. 33 to 34
("there are 4 x 3 x 2 x 1 x 5 = 120 different policies" for his five-state
example) and says on p. 39 the cycle "will usually find this policy in a small
number of iterations". The explicit sentence "finitely many policies, strict
improvement, so it stops" is in Sutton and Barto p. 80 and Van Roy Theorem 4,
not in the pages of Howard I read.

**Attribution.** Sutton and Barto, "Bibliographical and Historical Remarks",
printed p. 89: "The policy improvement theorem and the policy iteration
algorithm are due to Bellman (1957a) and Howard (1960)." Bellman (1957a) there is
the book *Dynamic Programming*, which I did not open. Howard himself, in the
2002 retrospective in item 6, answers a question about Bellman: "I was not aware
of Bellman's ideas on policy iteration; I was already writing my thesis in 1957."
Howard's preface says the monograph grew out of an Sc.D. thesis submitted in
June 1958. For a primary attribution, cite Howard 1960 for the algorithm and the
two names (value-determination operation, policy-improvement routine). Say
Sutton and Barto credit Bellman as well.

## Item 4. Bellman optimality equation (`v_*`, `q_*`)

**Claim.** The optimal value function is the fixed point of the Bellman backup
with a `max` over actions in place of an average under `π`.

**Primary for the lesson's form.** Sutton and Barto, section 3.6 "Optimal
Policies and Optimal Value Functions", printed pp. 62 to 65.
- `v_*(s) ≐ max_π v_π(s)`, (3.15), p. 62.
- `q_*(s,a) ≐ max_π q_π(s,a)`, (3.16), p. 63.
- `q_*(s,a) = E[R_{t+1} + γ v_*(S_{t+1}) | S_t = s, A_t = a]`, (3.17), p. 63.
- `v_*(s) = max_a E[R_{t+1} + γ v_*(S_{t+1}) | S_t = s, A_t = a]`, (3.18), and
  `= max_a Σ_{s',r} p(s',r|s,a) [r + γ v_*(s')]`, (3.19), p. 63.
- `q_*(s,a) = E[R_{t+1} + γ max_{a'} q_*(S_{t+1}, a') | S_t = s, A_t = a]`
  `= Σ_{s',r} p(s',r|s,a) [r + γ max_{a'} q_*(s',a')]`, (3.20), p. 64.
- The same pair is restated as (4.1) and (4.2), at the start of chapter 4,
  printed p. 73.
- Backup diagrams, Figure 3.4, p. 64.

Verbatim, p. 63, the intuition:
> Intuitively, the Bellman optimality equation expresses the fact that the value
> of a state under an optimal policy must equal the expected return for the best
> action from that state:

Verbatim, p. 64, uniqueness and the link to greedy policies:
> For finite MDPs, the Bellman optimality equation for v_* (3.19) has a unique
> solution.

> Any policy that is greedy with respect to the optimal evaluation function v_*
> is an optimal policy.

Verbatim, p. 64, on the diagram contrast the lesson wants:
> These are the same as the backup diagrams for v_π and q_π presented earlier
> except that arcs have been added at the agent's choice points to represent
> that the maximum over that choice is taken rather than the expected value
> given some policy.

(The arcs on the Figure 3.4 diagram are the `max` marks at the choice points.)

**Primary for the origin of the recurrence.** Richard Bellman, "A Markovian
Decision Process", *Journal of Mathematics and Mechanics* 6(5), 1957, pp. 679 to
684. Landing page https://www.iumj.indiana.edu/IUMJ/FULLTEXT/1957/6/56038, PDF
https://www.iumj.indiana.edu/IUMJ/FTDLOAD/1957/6/56038/pdf (6 scanned pages,
printed pp. 679 to 684; I read all six as images). This is the document lesson 1
linked. Bellman numbers equations afresh in each section.

What is on the pages:
- p. 679, section 1, equation (1): `f_N(i) = Max_q [ b_i(q) + Σ_{j=1}^M a_ij(q) f_{N-1}(j) ]`,
  `f_0(i) = c_i`. This is the N-stage `max` recurrence. It is the form that
  value iteration iterates.
- p. 680, section 2, the Theorem: under conditions (2a) to (2c), `f_N(i) ~ N r` as
  `N → ∞`, with `r` given by a maximum over `q` of a Cesaro limit (equation (4)).
  The result is about long-run average reward.
- p. 681, section 4, equation (2): `r + x_i = Max_q [ b_i(q) + Σ_j a_ij(q) x_j ]`.
  This is the steady-state optimality equation in average-reward form.
- p. 684, section 7, equation (3): `f_N(i) = Min_q [ b_i(q) + Σ_j a_ij(q) f_{N-1}(j) ]`
  for a cost problem, introduced by: "The principle of optimality, cf. [2],
  asserts that q is chosen so as to yield the equation".

**What the paper does not contain.** No discount factor, no discounted
fixed-point equation `v = max_a Σ P [R + γ v]`, and no policy iteration. The
`max` is over decision vectors `q` with transition coefficients `a_ij(q)` that
satisfy `Σ_j a_ij = 1`. I did not open Bellman's 1957 book *Dynamic Programming*
(Princeton University Press), which Howard cites for this material (Howard 1960,
p. 29 footnote and reference 1, "Chapter XI"). If the lesson wants Bellman for
the discounted equation, either cite the book after someone opens chapter XI,
or cite Sutton and Barto (3.19) and say Bellman's paper gives the finite-stage
recurrence. Sutton and Barto, p. 89: "The term 'dynamic programming' is due to
Bellman (1957a)".

Howard 1960 ch. 3, p. 29, equation (3.1), is the same recurrence for the
toymaker, with the footnote: "Equation 3.1 is the application of the 'Principle
of Optimality' of dynamic programming to the Markovian decision process; this
and other applications are discussed by Bellman." That gives the lesson a
second dated anchor for "the max backup was derived by the principle of
optimality".

## Item 5. Value iteration and convergence as a contraction

**Claim.** Turning the optimality equation into an update gives
`v_{k+1}(s) = max_a Σ_{s'} P(s'|s,a) [R(s') + γ v_k(s')]`. For `γ < 1` the backup is
a contraction in the max-norm with modulus `γ`, so the iterates converge to
`v_*`, and a greedy policy for the limit is optimal.

**Sutton and Barto, section 4.4 "Value Iteration", printed pp. 82 to 84.**
Equation (4.10), p. 83: `v_{k+1}(s) ≐ max_a E[R_{t+1} + γ v_k(S_{t+1}) | S_t = s, A_t = a]`
`= max_a Σ_{s',r} p(s',r|s,a) [r + γ v_k(s')]`. Verbatim, p. 83:
> Note that value iteration is obtained simply by turning the Bellman
> optimality equation into an update rule. Also note how the value iteration
> update is identical to the policy evaluation update (4.5) except that it
> requires the maximum to be taken over all actions.

> Value iteration effectively combines, in each of its sweeps, one sweep of
> policy evaluation and one sweep of policy improvement.

Verbatim, p. 82 to 83, the truncation view:
> In fact, the policy evaluation step of policy iteration can be truncated in
> several ways without losing the convergence guarantees of policy iteration.
> One important special case is when policy evaluation is stopped after just one
> sweep (one update of each state). This algorithm is called value iteration.

Verbatim, p. 84: "All of these algorithms converge to an optimal policy for
discounted finite MDPs." The value-iteration box with the `θ` stopping rule and
the output step "Output a deterministic policy, π ≈ π_*" is on p. 83.

**Sutton and Barto do not prove the contraction.** On p. 83 they write: "For
arbitrary v_0, the sequence {v_k} can be shown to converge to v_* under the same
conditions that guarantee the existence of v_*." The proof comes from the
two references below. Their Bibliographical Remarks (p. 89) credit Puterman and
Shin (1978) for the truncated-policy-iteration view and Bertsekas (1987) for
finite-time identification of the optimal policy by value iteration. I did not
open either.

**Analysis reference 1 (opened): Van Roy, MS&E 235A, Lecture Notes 05 "Value
Iteration" (13 Oct 2025), section 3 "Discounted Value Iteration", subsection 3.1
"Convergence Analysis", printed p. 4.** URL:
https://web.stanford.edu/class/msande235a/files/lectures/lecture05.pdf
> Convergence follows from the fact that, with a discount factor γ ∈ [0, 1),
> the Bellman operator T is a contraction mapping with respect to the maximum
> norm.

Theorem 1 (contraction mapping): for finite state and action sets and
`γ ∈ [0,1)`, `‖TV − TV'‖_∞ ≤ γ ‖V − V'‖_∞` for all `V, V'`. The proof is five
lines, and its first inequality is the `max` step:
`max_a x_a − max_a y_a ≤ max_a (x_a − y_a)`. It then bounds the difference of
the averaged next-state values by `γ max_{s'} |V(s') − V'(s')|`. This is the
non-expansion of `max` inside the contraction proof, which is what the
commission wants stated. Theorem 2 (convergence): for any `V_0`, `V_{k+1} = T V_k`
converges to `V_{*,γ}`, proved from `‖V_* − V_{k+1}‖_∞ ≤ γ ‖V_* − V_k‖_∞`.
**Typo to avoid copying:** the lecture's displayed bound is
`‖V_* − V_{k+1}‖ ≤ γ^k ‖V_* − V_0‖`. The one-step inequality it proves iterates
to `γ^{k+1}`. The printed `γ^k` is true but weaker.
The lecture uses reward `r(s,a)` and transition `P`; the lesson's `R(s')`
arrival reward fits the same proof.

**Analysis reference 2 (opened): Dimitri P. Bertsekas, *Abstract Dynamic
Programming*, chapter 1 "Introduction", as posted by the author.** URL:
https://web.mit.edu/dimitrib/www/Ch1_Abstract_DP_2ND_EDITION.pdf (the file name
says 2nd edition; the file itself prints no edition line). Page numbers below
are the chapter's own printed numbers. This is the document lesson 1 linked.
- Section 1.2.2 "Monotonicity and Contraction Properties", p. 8: Assumption
  1.2.2, equation (1.8), `‖T_μ J − T_μ J'‖ ≤ α ‖J − J'‖` for every policy `μ`.
- pp. 8 to 9: the passage that deduces from (1.8) that `T = inf_μ T_μ` is also
  an `α`-contraction, equation (1.9), `‖TJ − TJ'‖ ≤ α ‖J − J'‖`. This is the
  abstract form of "the optimum over actions of contractions is a contraction".
  Verbatim, p. 8: "from which, by taking infimum of both sides over µ ∈ M, we
  have", followed by the bound on `((TJ)(x) − (TJ')(x)) / v(x)`. The same step
  with the roles of `J` and `J'` swapped, then a supremum over `x`, gives (1.9).
  With `max` in place of `inf`, this is the non-expansion step.
- p. 9: with contraction, results (a) to (d). (a) Bellman's equation has a
  unique solution. (c) "J* and Jμ can be computed by the value iteration method,
  J* = lim T^k J ... starting with any J". (d) "J* can be computed by the policy
  iteration method, whereby we generate a sequence of stationary policies via
  T_{μ^{k+1}} J_{μ^k} = T J_{μ^k}".
- Example 1.2.2 "Finite-State Discounted Markovian Decision Problems", p. 12:
  "the mappings Tμ and T are contraction mappings with respect to the standard
  (unweighted) sup-norm." This is the case the lesson's grid falls under.
- Bertsekas works with costs and minimization (`inf`); the lesson maximizes
  reward. The argument is symmetric.
- This chapter states convergence of policy iteration, not its finite
  termination. Finite termination is anchored in item 3.

I did not open Puterman, *Markov Decision Processes* (1994). I looked for its
theorem numbers (6.2.4, 6.4.2) and could not confirm them from an open text.
Do not cite Puterman by theorem number.

**A one-line bound the writer may want, derived here, not sourced.** From
`‖v_k − v_*‖ ≤ γ ‖v_{k−1} − v_*‖` and the triangle inequality,
`‖v_k − v_*‖_∞ ≤ γ/(1−γ) ‖v_k − v_{k−1}‖_∞`. With `γ = 0.9` the factor is 9. In my
run the actual error stays under the bound at every sweep, with the bound
overestimating by a factor between about 5 and 12. I did not find this exact
inequality stated in a passage I read, so cite the contraction and derive the
rest in the text, or leave it out.

## Item 6. A real case for "Why this matters"

**Preferred case: AlphaGo Zero's self-play loop, described by its authors as
policy iteration.**

Silver et al., "Mastering the game of Go without human knowledge", *Nature*
550, 354 to 359 (2017). Read from the UCL author manuscript:
https://discovery.ucl.ac.uk/id/eprint/10045895/1/agz_unformatted_nature.pdf
(42 pages, manuscript pagination). I could not check the Nature page of each
passage. The ExIt paper's reference list gives the journal citation as
"Nature, 550(7676):354–359, 2017". The sections below are the manuscript's.

Section "Reinforcement Learning in AlphaGo Zero", manuscript p. 3. Verbatim:
> The MCTS search outputs probabilities π of playing each move. These search
> probabilities usually select much stronger moves than the raw move
> probabilities p of the neural network fθ(s); MCTS may therefore be viewed as
> a powerful policy improvement operator [20, 21]. Self-play with search –
> using the improved MCTS-based policy to select each move, then using the game
> winner z as a sample of the value – may be viewed as a powerful policy
> evaluation operator. The main idea of our reinforcement learning algorithm is
> to use these search operators repeatedly in a policy iteration procedure
> [22, 23]:

References 20 and 21 are Howard, *Dynamic Programming and Markov Processes*
(MIT Press, 1960) and Sutton and Barto (1998). References 22 and 23 are
Bertsekas, "Approximate policy iteration: a survey and some new methods"
(2011) and Scherrer, "Approximate policy iteration schemes: a comparison"
(2014). So the AlphaGo Zero paper cites Howard 1960 at the sentence that calls
search a policy improvement operator.

Methods, "Reinforcement learning", manuscript p. 19. Verbatim:
> Policy iteration [20, 21] is a classic algorithm that generates a sequence of
> improving policies, by alternating between policy evaluation – estimating the
> value function of the current policy – and policy improvement – using the
> current value function to generate a better policy.

> The AlphaGo Zero self-play algorithm can similarly be understood as an
> approximate policy iteration scheme in which MCTS is used for both policy
> improvement and policy evaluation. Policy improvement starts with a neural
> network policy, executes an MCTS based on that policy's recommendations, and
> then projects the (much stronger) search policy back into the function space
> of the neural network. Policy evaluation is applied to the (much stronger)
> search policy: the outcomes of self-play games are also projected back into
> the function space of the neural network.

**What the source supports, and what it does not.**
- Supported: the authors themselves call the loop an approximate policy
  iteration scheme, and name search as the improvement step.
- The brief's split ("policy evaluation by the network") is not what the paper
  says. In the paper, MCTS does the improvement, self-play outcomes with search
  do the evaluation, and the network is the function the results are trained
  into ("projects ... back into the function space of the neural network").
  The lesson can say the network stores the evaluation, with the paper's words
  as the warrant, but should not say the network performs it.
- The paper says "approximate" and "can be understood as". It does not claim
  the equivalence the lesson's exact tabular loop has. On the 14-state grid,
  improvement is a full greedy step over exact `q_π` and evaluation is a linear
  solve. In AlphaGo Zero, both are sampled and fitted. The shared structure is
  the alternation.

**Second source, naming policy iteration directly: Anthony, Tian and Barber,
"Thinking Fast and Slow with Deep Learning and Tree Search", NeurIPS 2017.**
arXiv:1705.08439v4 (3 Dec 2017), https://arxiv.org/abs/1705.08439, PDF
https://arxiv.org/pdf/1705.08439. Read the full text. Printed page numbers are
the paper's own.
- Abstract, p. 1: "Planning new policies is performed by tree search, while a
  deep neural network generalises those plans. Subsequently, tree search is
  improved by using the neural network policy to guide search, increasing the
  strength of new plans."
- Section 7 "Related work", p. 9, the only passage where the paper names policy
  iteration as such. Verbatim: "EXIT has several connections to existing RL
  algorithms, resulting from different choices of expert class. For example, we
  can recover a version of Policy Iteration [15] by using Monte Carlo Search as
  our expert; in this case it is easy to see that Monte Carlo Tree Search gives
  stronger plans than Monte Carlo Search."
- Same section, p. 9, on AlphaGo Zero: "AlphaGo Zero (AG0)[17], presents an
  independently developed version of ExIt, and showed that it achieves
  state-of-the-art performance in Go."

Limits: the paper's own framing is imitation learning with an expert-improvement
step. Its policy-iteration remark is one sentence, about a particular choice of
expert (Monte Carlo search), and cites reference [15], Ross and Bagnell (2014),
not Howard. The brief says this paper "names policy iteration directly". True,
once, and conditionally. Use it for the two-step structure (planner proposes a
stronger policy, network absorbs it, planner gets stronger), and cite
AlphaGo Zero for the sentence that says "policy iteration".

I also read the AlphaZero arXiv paper (Silver et al., arXiv:1712.01815v1, the
supplement, p. 11), which says only: "An approach based on training dual policy
and value networks using AlphaZero-like policy iteration was successfully
applied to improve on the state-of-the-art in Hex (3)." Reference 3 is the ExIt
paper. It is not a source for the policy-iteration reading. Do not cite it for
that.

**Alternative case: Howard's own documented application.** Ronald A. Howard,
"Comments on the Origin and Application of Markov Decision Processes",
*Operations Research* 50(1), 2002, pp. 100 to 102 (DOI 10.1287/opre.50.1.100.17788;
reprint of a 1978 chapter in Puterman, ed., *Dynamic Programming and Its
Applications*). I read the copy at
https://gwern.net/doc/statistics/decision/2002-howard.pdf. **That copy holds
pp. 101 and 102 only. Page 100, where the account starts, is missing.** The
publisher page returned HTTP 403. What p. 101 says, verbatim:
> The optimum policy, for both discounted present value and average reward
> criteria, was found by value iteration.

> The optimum policy was not the policy that maximized expected immediate
> return, but rather a policy that balanced this return with the effect on
> future state transitions. The net result was a predicted few percent increase
> in the profitability of the catalog operation, which, however, amounted to
> several million dollars per year.

> The experience left me with the suspicion that there might be a way to go
> directly to the best policy without the need for value iteration. I worked on
> the problem for about six months under Dr. Kimball's supervision and was able
> to develop a policy iteration method (Howard 1960).

and, on p. 101, "I would like to have described the motivating problem at that
time, but the proprietary nature of the work with Sears, Roebuck and Company
made that impossible." The text on p. 101 also gives "a total of about 50
states" with transitions each season, and a test index of monitored customers.

What this supports: Howard solved a roughly 50-state catalog-mailing problem for
Sears with **value iteration**, found the optimum differed from the policy
that maximized immediate return, and then developed policy iteration afterward
because of that experience. It does not say policy iteration was run on the
Sears problem. The figure "a few percent" and "several million dollars per
year" are his estimates ("predicted"). The first part of the account (p. 100) is
outside what I read, so I cannot confirm how he introduces the problem there.
This case fits the lesson directly: it is a real problem where the best action
differs from the greedy-on-immediate-reward action, and where value iteration
came first and policy iteration second.

**Recommendation.** Use the AlphaGo Zero passage if the lesson wants the
connection to lesson 1's AlphaGo thread. Use Howard 2002 if the lesson wants the
algorithm's origin. They can sit together: Howard developed policy iteration
after a catalog-mailing problem for Sears, and AlphaGo Zero's authors cite
Howard's book at the sentence that calls search a policy improvement operator.
Howard 2002 as I could read it gives no date for the Sears work. Do not date it.

## Arithmetic facts for the writer (checks, not citations)

These come from my own cross-check run, not from a source. I rebuilt the grid
from the `gridworld.py` source in the writer's brief (cells 0 to 15, GOAL = 3,
PIT = 6, rewards +10 / −20 / −1 paid on arrival, slip 0.2, `γ` = 0.9, hand-drawn
`PI`), and ran numpy in the scratchpad with the direct solve. No repository file
was changed. The writer's reported numbers must come from the writer's own run.
These are for agreement checks.

Rows are listed top to bottom, columns left to right. Arrows `^ > v <` are
actions 0 to 3. Slip sends the agent to each perpendicular direction with
probability 0.1.

**`v_π` of the hand-drawn policy** (4 decimals):
```
 2.1559   4.0370   6.4835   0
 0.6129   0.0618   0        6.4835
-0.7157  -1.0291  -0.1018   4.0208
-1.8635  -2.0055  -1.0760   1.9760
```
Cell 13 is −2.0055, which matches lesson 1's −2.01.

**Action values at cell 13 under `v_π`** (order up, right, down, left):
`−2.0055, −2.0478, −2.7085, −2.6148`. The hand-drawn action (up) is the best, so
cell 13 does not flip in the first step.

Hand check of `q(13, up)`: up reaches cell 9 w.p. 0.8, slips right to cell 14
w.p. 0.1 and left to cell 12 w.p. 0.1. Every arrival pays −1.
`q = −1 + 0.9 (0.8 · (−1.0291) + 0.1 · (−1.0760) + 0.1 · (−1.8635))`
`= −1 + 0.9 · (−1.1172) = −2.0055`. This equals `v_π(13)`, as it must, since
`π(13)` is up.

Hand check of `q(13, right)`: right reaches 14 w.p. 0.8, slips down (stays in
13) w.p. 0.1, slips up to 9 w.p. 0.1.
`q = −1 + 0.9 (0.8 · (−1.0760) + 0.1 · (−2.0055) + 0.1 · (−1.0291))`
`= −1 + 0.9 · (−1.1643) = −2.0478`.

**The cell that does flip first is cell 14.** Under `v_π`, `v_π(14) = −1.0760`
and the action values are up −1.0760, right 0.3167, down −1.7774, left −2.5499.
Right beats up by 1.3927. Hand check of `q(14, right)`: right reaches 15 w.p.
0.8, slips down (stays in 14) w.p. 0.1, slips up to 10 w.p. 0.1.
`q = −1 + 0.9 (0.8 · 1.9760 + 0.1 · (−1.0760) + 0.1 · (−0.1018))`
`= −1 + 0.9 · 1.4630 = 0.3167`. No other non-terminal cell has an action that
beats the current one by more than 1e-15 under `v_π`.

**Policy iteration from the hand-drawn policy**, keeping the old action on ties
(Howard's rule, 1e-12):
- `π_0` is the hand-drawn policy. Improvement changes 1 cell (14: up to right).
- `π_1`. Improvement changes 1 cell (13: up to right).
- `π_2`. Improvement changes 0 cells. Stop.
So there are 3 evaluate-and-improve rounds, 2 of which change the policy. The
text can say "two improvements, and a third round that confirms nothing
changes". Pick one counting convention and state it.
`v(13)` across `π_0, π_1, π_2`: −2.0055, −1.8412, −0.7142.
`π_*` (rows 0 to 3): `> > > .` / `^ ^ . ^` / `^ ^ > ^` / `^ > > ^`.

**`v_*`** (4 decimals), which is also `v_{π_2}`:
```
 2.1559   4.0370   6.4835   0
 0.6129   0.0618   0        6.4835
-0.7142  -1.0142   0.0618   4.0370
-1.7347  -0.7142   0.6129   2.1559
```
Optimal action values at cell 13: up −1.8312, right −0.7142, down −1.6152,
left −2.4045.

**Per-cell improvement `v_* − v_π`:**
```
0        0        0        0
0        0        0        0
0.0015   0.0149   0.1637   0.0162
0.1289   1.2912   1.6889   0.1798
```
Cell 13 gains 1.2912. Rows 0 and 1 are exactly unchanged (see warning 5).

**Weak monotonicity holds step by step.** `v_{π_1} ≥ v_{π_0}` and
`v_{π_2} ≥ v_{π_1}` hold cell by cell in my run. In the first step, cells 8 to
15 all rise strictly and cells 0 to 7 stay equal. In the second step only cells
12 and 13 rise (cell 13 from −1.8412 to −0.7142, cell 12 from −1.8461 to
−1.7347).

**Ties at the optimum.** At `v_*`, cell 9 has up = right = −1.0142, and cell 12
has up = right = −1.7347. The ties follow from `v_*(5) = v_*(10)` and
`v_*(8) = v_*(13)`: at cell 9, up weights cell 5 by 0.8 and cells 8 and 10 by
0.1 each, and right weights cell 10 by 0.8 and cells 5 and 13 by 0.1 each, so the
two sums coincide. Cell 12 reduces to `v_*(8) = v_*(13)` the same way.
Consequences, from my run:
- With keep-old-on-ties, PI takes 3 rounds and ends with up at cells 9 and 12.
- With plain `argmax` taking the first maximum, PI takes 4 rounds. In round 3
  the improvement flips cell 9 from up to right on a tie that only floating-point
  noise in `q` decides, and round 4 finds nothing to change. It ends with right
  at cell 9.
- A VI run read out by plain `argmax` matches `π_*` arrow for arrow at some
  thresholds and not at others. At a max-norm change threshold of 1e-3 (16
  sweeps), 1e-4 (18) and 1e-6 (24) it matches. At 1e-2 (13), 1e-5 (21) and 1e-9
  (33) it does not, at the tied cells.
The lesson should compare policies by action value (the action each chooses must
have `q_*` within a small tolerance of the maximum) or define one explicit tie
rule, and say that optimal values are unique while optimal policies need not be.
Sutton and Barto say the same, p. 62: "Although there may be more than one, we
denote all the optimal policies by π_*."

**Value iteration from `v = 0`**, stopping when the max-norm change in one sweep
falls below the threshold (my run):

| threshold | sweeps | max error to `v_*` at stop |
|---|---|---|
| 1e-2 | 13 | 4.6e-03 |
| 1e-3 | 16 | 3.9e-04 |
| 1e-4 | 18 | 7.6e-05 |
| 1e-6 | 24 | 5.6e-07 |
| 1e-9 | 33 | 3.5e-10 |

Max-norm change per sweep: 5.90, 4.07, 2.77, 2.01, 1.45, 1.12, 0.629, 0.343,
0.149, 0.0691, ... (sweeps 1 to 10). The max-norm error to `v_*` shrinks by
about 0.8 per sweep over sweeps 1 to 5 and by 0.44 to 0.53 per sweep from sweep
6 on (for example 7.6e-05 to 3.4e-05 between sweeps 18 and 19). The `γ = 0.9`
factor is an upper bound, and the grid's observed rate is faster.
`v(13)` over the first eight sweeps: −1.000, −1.900, −2.710, −3.439, −1.986,
−1.335, −0.981, −0.836. The first four equal `−(1 − 0.9^k)/0.1`, which is the
discounted sum of `k` steps of −1, so each sweep only extends the chain of
step costs. At sweep 5 the value turns up. The shortest path from cell 13 to the
goal at cell 3 is five moves, so sweep 5 is the first sweep in which the +10 for
reaching cell 3 reaches cell 13. That makes cell 13 a clean example for the
convergence figure.
The greedy policy of `v_k` first equals the PI answer at sweep 5 (first-max tie
rule), well before `v_k` is near `v_*`. S&B make the same point for their
example (p. 82): "policy evaluation iterations beyond the first three have no
effect on the corresponding greedy policy."

**Sutton and Barto's Figure 4.1 / Example 4.1 does not transfer.** That grid is
a deterministic, undiscounted 4×4 gridworld with the equiprobable random
policy (p. 76). Its numbers (for example −14, −20, −22 at `k = ∞`, p. 77) do not
apply to the slippery discounted grid. Cite it for the idea that the greedy
policy can be optimal before the values converge, and not for any number.

## What I confirmed and what I could not

**Confirmed by opening the passage:**
- Item 1: theorem (4.7) and (4.8), the telescoping chain, (4.9), the strictness
  argument. S&B printed pp. 78 to 79, read as text and checked on the page
  image for the `γ` terms. Van Roy lecture 06 Theorem 3.
- Item 2: (3.13) p. 58, (4.6) p. 78.
- Item 3: S&B p. 80 (loop and finite termination), p. 82 (Exercise 4.4).
  Howard ch. 4 pp. 37 to 39 and 42 to 43, ch. 7 pp. 81 to 84 and 86 to 87.
  Van Roy Theorem 4.
- Item 4: S&B (3.15) to (3.20), pp. 62 to 64, and (4.1), (4.2) p. 73. Bellman
  1957 all six pages.
- Item 5: S&B (4.10) p. 83. Van Roy lecture 05 Theorems 1 and 2. Bertsekas ch. 1
  (1.8), (1.9), results (a) to (d), Example 1.2.2.
- Item 6: AlphaGo Zero manuscript pp. 3 and 19. ExIt abstract and section 7.
  Howard 2002 p. 101.

**Not confirmed, do not cite as if read:**
- Bellman's 1957 book *Dynamic Programming*, chapter XI. Not opened.
- Puterman, *Markov Decision Processes*, any theorem number. Not opened.
- Bertsekas, *Abstract Dynamic Programming*, chapters after 1. Also his 1987
  finite-time result and Puterman and Shin 1978. Not opened.
- The Nature page numbers of the AlphaGo Zero passages. I have only the author
  manuscript's pagination.
- Howard 2002 p. 100. The scan I could fetch lacks it, and the publisher
  returned 403. The Sears problem's opening description is therefore unread.
- Sutton and Barto page numbers against the 2018 print. They are those of the
  author's 2020 PDF.
- Howard's discounted chapter does not state a "finitely many policies"
  sentence in the pages I read. The finite-termination wording is from Sutton
  and Barto p. 80 and Van Roy Theorem 4.
