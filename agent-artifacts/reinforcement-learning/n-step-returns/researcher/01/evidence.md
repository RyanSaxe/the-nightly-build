# Evidence: reinforcement-learning/n-step-returns (researcher 01)

Sutton and Barto's second edition supports every definition the lesson needs:
the n-step return (7.1), the n-step TD update (7.2), the error-reduction
property (7.3), and the pseudocode with its τ bookkeeping, all on printed pages
143–144. It also supports the experiment: Example 7.1 and Figure 7.2 on page 145
show that on the 19-state walk an intermediate n (n = 4 lowest) beats n = 1 and
the near-Monte-Carlo n = 256 and 512, each at its own best α. Sutton's published
Lisp for that figure fixes the parts of the setup the book leaves out: start
state, exact values, α grid, and averaging order. Watkins (1989), pp. 85–87,
defines the "corrected n-step truncated return" and its error-reduction bound,
as Sutton and Barto's remarks say. The record is thin on one point, and the
commission gets it wrong. Section 7.1 states that intermediate n worked best but
gives no reason; no passage there "discusses why". With γ = 1, eq. 7.3 gives a
factor of 1 on this walk, so it cannot explain the win either. The win is
conditional. It holds at each n's best α, on a 19-state chain, over the first 10
episodes. My throwaway runs, which are not sources, find n = 1 best on a 5-state
walk and at episodes 91–100. Singh and Dayan (1998) find, for λ rather than n,
that the best value falls as trials accumulate. Any causal sentence on the page
needs its own removal test.

## Sources

### 1. Sutton and Barto, *Reinforcement Learning: An Introduction*, 2nd ed.

```text
URL:         http://incompleteideas.net/book/RLbook2020.pdf
             (book page: http://incompleteideas.net/book/the-book-2nd.html)
Kind:        primary. The authors define the method and ran the Figure 7.2
             experiment for this text (Ch. 7 remarks, p. 158).
Establishes: firsthand: definitions 7.1–7.3, the algorithm, Example 7.1,
             Figure 7.2 and its measure. Repeats Watkins's priority claim.
Locators:    printed page numbers; PDF page = printed + 22 (p. 142 = PDF 164).
             © 2018, 2020; CC BY-NC-ND 2.0 (copyright page).
```

**1a. Section 7.1 definitions (pp. 142–144).**

- p. 142: Section 7.1 opens. Figure 7.1 shows backup diagrams from "1-step TD
  and TD(0)" through "∞-step TD and Monte Carlo". Methods "in which the temporal
  difference extends over n steps are called n-step TD methods."
- p. 143, Eq. 7.1, exact:
  `G_{t:t+n} ≐ R_{t+1} + γR_{t+2} + ··· + γ^{n−1}R_{t+n} + γ^n V_{t+n−1}(S_{t+n})`,
  "for all n, t such that n ≥ 1 and 0 ≤ t < T − n." If t + n ≥ T, "all the
  missing terms are taken as zero, and the n-step return defined to be equal to
  the ordinary full return (G_{t:t+n} ≐ G_t if t + n ≥ T)." The one-step return
  is `G_{t:t+1} ≐ R_{t+1} + γV_t(S_{t+1})`, and the book calls each
  `G_{t:t+n}` a "truncated return".
- p. 143, the delay: "No real algorithm can use the n-step return until after
  it has seen R_{t+n} and computed V_{t+n−1}. The first time these are available
  is t + n."
- p. 143, Eq. 7.2, exact:
  `V_{t+n}(S_t) ≐ V_{t+n−1}(S_t) + α[G_{t:t+n} − V_{t+n−1}(S_t)],  0 ≤ t < T`,
  and all other states stay unchanged. The book names this algorithm "n-step
  TD". Quote, because it is the tail rule the code must follow: "Note that no
  changes at all are made during the first n − 1 steps of each episode. To make
  up for that, an equal number of additional updates are made at the end of the
  episode, after termination and before starting the next episode."
- p. 144, the pseudocode box "n-step TD for estimating V ≈ v_π", transcribed
  from the rendered page:

  ```text
  Input: a policy π
  Algorithm parameters: step size α ∈ (0, 1], a positive integer n
  Initialize V(s) arbitrarily, for all s ∈ S
  All store and access operations (for S_t and R_t) can take their index mod n + 1
  Loop for each episode:
    Initialize and store S_0 ≠ terminal
    T ← ∞
    Loop for t = 0, 1, 2, ... :
      If t < T, then:
        Take an action according to π(·|S_t)
        Observe and store the next reward as R_{t+1} and the next state as S_{t+1}
        If S_{t+1} is terminal, then T ← t + 1
      τ ← t − n + 1   (τ is the time whose state's estimate is being updated)
      If τ ≥ 0:
        G ← Σ_{i=τ+1}^{min(τ+n, T)} γ^{i−τ−1} R_i
        If τ + n < T, then: G ← G + γ^n V(S_{τ+n})          (G_{τ:τ+n})
        V(S_τ) ← V(S_τ) + α[G − V(S_τ)]
    Until τ = T − 1
  ```

- p. 144, Eq. 7.3, exact:
  `max_s |E_π[G_{t:t+n} | S_t = s] − v_π(s)| ≤ γ^n max_s |V_{t+n−1}(s) − v_π(s)|`,
  "for all n ≥ 1." Preceding sentence: the expected n-step return "is
  guaranteed to be a better estimate of v_π than V_{t+n−1} is, in a worst-state
  sense." Following: "This is called the error reduction property of n-step
  returns. Because of the error reduction property, one can show formally that
  all n-step TD methods converge to the correct predictions under appropriate
  technical conditions." The book states the property and gives no proof.
- p. 143, Exercise 7.1: the n-step error can be written as a sum of TD errors if
  the estimates do not change. This could be a short recursive-form exercise.

**1b. Example 7.1, Figure 7.2, Exercise 7.3 (pp. 144–145).**

- p. 144–145, first paragraph of Example 7.1, on the 5-state walk of Example 6.2
  with V(s) = 0.5 initially. After one episode C → D → E → right terminal
  (return 1), one-step TD changes only V(E). Two-step changes V(D) and V(E). Any
  n > 2 changes all three visited states "toward 1, all by the same amount."
  This is the book's only Section 7.1 statement about how far information
  travels per episode.
- p. 145, setup quote: "a larger random walk process, with 19 states instead of
  5 (and with a −1 outcome on the left, all values initialized to 0)". The
  minus sign is lost in the PDF text layer and was confirmed on the rendered
  page.
- p. 145, measure quote: "the square-root of the average squared error between
  the predictions at the end of the episode for the 19 states and their true
  values, then averaged over the first 10 episodes and 100 repetitions of the
  whole experiment (the same sets of walks were used for all parameter
  settings)."
- p. 145, the finding, quoted in full: "Note that methods with an intermediate
  value of n worked best. This illustrates how the generalization of TD and
  Monte Carlo methods to n-step methods can potentially perform better than
  either of the two extreme methods." No reason is given here or anywhere in
  Section 7.1.
- p. 145, Figure 7.2. Caption: "Performance of n-step TD methods as a function
  of α, for various values of n, on a 19-state random walk task (Example 7.1)."
  Y axis: "Average RMS error over 19 states and first 10 episodes", ticks 0.25
  to 0.55. X axis: α from 0 to 1. Curves are drawn for n = 1, 2, 4, 8, 16, 32,
  64, 128, 256, 512, and every curve starts at about 0.55 at α = 0. Readings are
  under Numbers.
- p. 145, Exercise 7.3, quoted in full: "Why do you think a larger random walk
  task (19 states instead of 5) was used in the examples of this chapter? Would
  a smaller walk have shifted the advantage to a different value of n? How
  about the change in left-side outcome from 0 to −1 made in the larger walk?
  Do you think that made any difference in the best value of n?" The book gives
  no answer.

**1c. Example 6.2 (p. 125).** The 5-state walk. "all episodes start in the
center state, C, then proceed either left or right by one state on each step,
with equal probability". Reward +1 on the right, all others 0. "Because this
task is undiscounted, the true value of each state is the probability of
terminating on the right". True values for A–E are 1/6 to 5/6. Example 7.1
does not restate the start state for the 19-state version. Sutton's code
(source 2) does.

**1d. Elsewhere in the book.**

- p. 141, Chapter 7 introduction: "Neither MC methods nor one-step TD methods
  are always the best… The best methods are often intermediate between the two
  extremes." The page also argues that n-step methods "free you from the tyranny
  of the time step". That argument is about decoupling how often actions change
  from the bootstrapping interval. It is not about variance.
- pp. 145–146, Section 7.2, for the one-sentence pointer. "n-step Sarsa"
  redefines the n-step return with `Q_{t+n−1}(S_{t+n}, A_{t+n})` (Eq. 7.4,
  p. 146) and updates `Q` (Eq. 7.5). p. 147, Figure 7.4: in a gridworld, after
  one episode, one-step Sarsa strengthens only the last action while n-step
  Sarsa strengthens the last n, "so that much more is learned from the one
  episode."
- p. 148, Section 7.3: the off-policy n-step TD update weights the error by the
  importance-sampling ratio `ρ_{t:t+n−1}` (Eq. 7.9). This is the hook for the
  one sentence linking the importance-sampling lesson.
- p. 157, Section 7.7 summary: n-step methods "involve a delay of n time steps
  before updating", need "more computation per time step", and need more memory
  for "the last n time steps".
- p. 158, Bibliographical remarks, quoted: "The notion of n-step returns is due
  to Watkins (1989), who also first discussed their error reduction property.
  n-step algorithms were explored in the first edition of this book, in which
  they were treated as of conceptual interest, but not feasible in practice. The
  work of Cichosz (1995) and particularly van Seijen (2016) showed that they are
  actually completely practical algorithms." For 7.1–2: "The results in the
  random walk examples were made for this text based on work of Sutton (1988)
  and Singh and Sutton (1996)."
- pp. 288–289, Section 12.1 "The λ-return", for the Go-deeper pointer. Any
  average of n-step returns with positive weights summing to 1 is a valid target
  and "possesses an error reduction property similar to that of individual
  n-step returns (7.3)" (p. 288). The λ-return, Eq. 12.2 (p. 289), is
  `G^λ_t ≐ (1 − λ) Σ_{n=1}^∞ λ^{n−1} G_{t:t+n}`.
- p. 291, Figure 12.3 repeats Figure 7.2 beside the off-line λ-return on the
  same 19-state task. Text: "In both cases we get best performance with an
  intermediate value of the bootstrapping parameter, n for n-step methods and λ
  for the off-line λ-return algorithm."
- pp. 208–209, Example 9.2: the same measure is called "an unweighted average of
  the RMS error over all states and over the first 10 episodes". This confirms
  the states are weighted equally.

Go deeper: Section 7.2 (pp. 145–147), for Eq. 7.4 and Figure 7.4, the same idea
applied to control. Section 12.1 (pp. 288–291), for Eq. 12.2 and Figure 12.3,
the λ-return as an average of n-step returns that behaves like n on this task.

### 2. Sutton, Lisp code for Example 7.1 / Figure 7.2 ("online")

```text
URL:         http://incompleteideas.net/book/code/online.lisp
             (listed on http://incompleteideas.net/book/code/code2nd.html under
             "Chapter 7: n-step Bootstrapping": "N-step TD on the Random Walk,
             Example 7.1, Figure 7.2: online and offline (Lisp)")
Kind:        primary. The book's first author's own code for the figure.
Establishes: firsthand: the experiment's exact parameters that the book text
             omits.
Locators:    Lisp function names below. The file uses old Mac CR line endings;
             convert with tr '\r' '\n' to read it.
```

- `(defvar n 19)`, `(defvar right-outcome 1.0)`, `(defvar left-outcome -1.0)`,
  `(defvar initial-w 0.0)`.
- `init` sets the exact values `targets` to
  `(right − left)·(i+1)/(n+1) + left` for i = 0..18. That is
  v(i) = i/10 − 1 for states numbered 1..19, or −0.9, −0.8, …, 0, …, 0.9.
- `random-walk`: `start-state = (truncate (/ n 2))` = 9, zero-based. This is the
  centre state, the 10th of 19. Each step moves ±1 `with-prob .5`.
- `process-walk-nstep`: for each visited state in time order, the target is the
  outcome if `NN >= (length rest)`, otherwise the current `w` of the state `NN`
  steps later. The update is `w[x] += alpha·(target − w[x])`. Every reward
  before termination is 0 and γ = 1, so the n-step return is either the outcome
  or V(S_{t+n}). The walk is processed after it ends, in time order. Each target
  then sees exactly the updates for earlier times, as in the book's online
  pseudocode, so the values match. That equivalence is my reading of the code,
  and an editor can check it in a few lines.
- `standard-walks`: one copy of a standard random state generates every run's
  walks, so all (n, α) settings see the same walks.
- `residual-error` is the RMS over the 19 states. `learning-curve-nstep`
  averages each post-episode error across runs. `online-nstep` then takes
  `(mean (rest …))`, the mean over episodes 1–10, which leaves out the initial
  error. The plotted value is therefore the mean of per-episode RMS values, not
  the root of a pooled mean square.
- `online-nstep`: n doubles from 1 `while (< nstep 1000)`, giving 1…512.
  α = `(exp alog)` for alog from −5 to 0 in steps of 0.1. That is 51
  log-spaced values from 0.0067 to 1, plus a point at α = 0 drawn at the
  initial error.
- `(setup 100 10)` gives 100 runs of 10 walks. The comment after
  `(online-nstep)` reads "1st edition, Figure 7.2, upper graph". The code
  index ties the same file to the 2nd edition's Figure 7.2.

### 3. Watkins, *Learning from Delayed Rewards* (1989)

```text
URL:         https://www.cs.rhul.ac.uk/~chrisw/new_thesis.pdf
             (author's page: https://www.cs.rhul.ac.uk/~chrisw/thesis.html, which
             says the file "has been scanned in from a photocopy")
Kind:        primary. The originating document for the corrected n-step return.
Establishes: firsthand: the definition and the error-reduction bound.
Locators:    Title page: Christopher John Cornish Hellaby Watkins, King's
             College, "Thesis Submitted for Ph.D.", May 1989. Chapter 7
             "Primitive Learning", Section 2 "Methods of Estimating Values and
             Action-Values", printed pp. 84–87 (PDF pp. 91–94; PDF = printed +
             7). The scan has no text layer, so I read it from rendered pages.
             The page number on printed p. 86 prints as "%" in the scan; it sits
             between pp. 85 and 87.
```

- p. 85 defines the uncorrected "n-step truncated return"
  `r_t^{[n]} = r_t + γr_{t+1} + γ²r_{t+2} + ··· + γ^{n−1}r_{t+n−1}`. It lists
  three disadvantages of estimating values by averaging it. The value is
  "only available to the agent after a time delay of n steps". "The truncated
  returns may have a high variance". And the agent "must continue to follow
  policy f for at least n steps".
- p. 86 credits Sutton (1988) with "temporal difference" methods, then defines:
  "The *corrected n-step truncated return* for time t is
  `r_t^{(n)} ≡ r_t + γr_{t+1} + ··· + γ^{n−1}r_{t+n−1} + γ^n U_{t+n}(x_{t+n})`".
  U is the agent's current value approximation. Watkins's r_t is the reward
  received at time t, which Sutton and Barto write R_{t+1}. The page then
  states, with K = max_x |U(x) − V_f(x)|,
  `max_x |E[r^{(n)}(x)] − V_f(x)| ≤ γ^n K`.
- p. 87: "This might be called the *error-reduction property* of corrected
  truncated returns." Also: "E[r^{(n)}(x)] is not necessarily closer to V_f(x)
  than U(x) is for *all* x — but the maximum error of E[r^{(n)}(x)] is less than
  the maximum error of U." Weighted averages of corrected returns keep the
  property. Weights proportional to λ^n give r^λ, "investigated by Sutton
  (1988)".
- p. 85 assumes γ < 1 ("Because γ < 1, γ^n will approach zero").
- Corrigenda (PDF p. 5) amend pp. 90–91, 98, 227–228 and leave pp. 84–87
  untouched.
- This confirms the commission's attribution and Sutton and Barto's p. 158
  remark. Cite Watkins for introducing corrected n-step returns and their error
  reduction. Do not cite him for the n-step TD algorithm in the form of Eq. 7.2.

### 4. Singh and Dayan, "Analytical Mean Squared Error Curves for Temporal Difference Learning"

```text
URL:         https://doi.org/10.1023/A:1007495401240 (Machine Learning 32,
             5–40, 1998; the Springer landing page rate-limited (HTTP 429),
             gated, not dead). Read from the author-hosted manuscript
             https://web.eecs.umich.edu/~baveja/Papers/MLjournal4.pdf.
Kind:        primary for its own analytical and simulated results; it
             is about TD(λ) with offline updates, not n-step TD.
Establishes: firsthand: on random-walk and cyclic chains, the
             error-minimising bootstrapping parameter depends on trial number,
             initial bias and trial length.
Locators:    manuscript pages (1–38), not journal pages. Volume and pages are
             from the mlanthology.org record, since Springer was gated.
```

- Manuscript p. 8, Fig. 2: "Symmetric Random Walk (SRW)". Absorption on the left
  pays +1 and on the right −1, the mirror of Sutton and Barto. "All trials start
  in the middle state." §4.1 and §4.3 use the 19-state SRW.
- Manuscript p. 13, §4.3, H2: "the smaller the constant α and λ, the smaller the
  asymptotic MSE." H3: "larger values of α or λ lead to faster convergence to the
  asymptotic value of MSE".
- Manuscript pp. 17–18, §4.5, Figure 10 at α = 0.05: "the minimum-error λ is not
  constant as a function of trial number, and … it generally shifts from a high
  initial value to lower values with increasing trial number." The authors
  explain it from H2 and H3. Large λ wins early because it converges faster,
  and small λ wins later because its asymptote is lower. The passage I read does
  not name the chain used for Figure 10.
- Manuscript p. 19, §4.6, H5: "If the initial value function has a high bias,
  one should begin with a large λ". Manuscript p. 21: higher cyclicity "leads to
  longer trials and therefore requires larger λ to obtain the same mix of the
  random payoff". This is the closest sourced statement on Exercise 7.3's
  chain-length question, and it concerns λ.

### 5. Hernandez-Garcia and Sutton, "Understanding Multi-Step Deep Reinforcement Learning: A Systematic Study of the DQN Target" (2019)

```text
URL:         https://arxiv.org/abs/1901.07510 (v2, 7 Feb 2019)
Kind:        primary for its own experiments; secondary for the bias–variance
             claim it attributes to Kearns and Singh (2000).
Establishes: firsthand: in a DQN-like architecture on mountain car, the
             largest n tested did best.
Locators:    §4.2 "Comparison of n-Step Algorithms", Figure 2.
```

- §4.2 tests n ∈ {1, 3, 5, 10, 20} for Retrace, Q-learning, Tree Backup, Sarsa,
  Q(σ = 0.5) and decaying σ, over 100 runs. "The 20-step version of each
  algorithm performed better than with smaller values of n in terms of initial
  and overall performance. In terms of final performance, values of n ≥ 3
  performed similarly." Also: "we were not able to find a value of n that was
  too high".
- §4.2 opening: "The parameter n has been shown to trade-off between the bias
  and the variance of the estimate of the return (Kearns & Singh, 2000)." This
  repeats Kearns and Singh, whose paper I could not open (see Limits).
- Go deeper: §4.2, a short read showing that in deep control the best n was the
  largest one tried.

### 6. De Asis, Hernandez-Garcia, Holland and Sutton, "Multi-Step Reinforcement Learning: A Unifying Algorithm" (AAAI 2018)

```text
URL:         https://arxiv.org/abs/1703.01327 (v2, 11 Jun 2018)
Kind:        primary for its own experiment.
Establishes: firsthand: on a two-action 19-state random walk, n = 3 and α = 0.4
             were representative of the best settings for every Q(σ) variant
             over 50 episodes.
Locators:    "Experiments", subsection "19-State Random Walk", Figures 2–3.
```

- The walk is reformulated "such that each state had two actions". The agent
  learns action values on-policy under an equiprobable policy, and "the
  resulting state values are identical" to the usual walk. Terminal rewards are
  −1 and +1. RMS error against "analytically computed values" was measured after
  each episode, over 50 episodes and 100 runs. "Figure 3 shows the results with
  n = 3 and α = 0.4, which was found to be representative of the best parameter
  setting for each instance of Q(σ) on this task."
- This sits close to Sutton and Barto's best region (n = 4, α ≈ 0.37), with a
  longer averaging window and action values.
- Go deeper: weaker fit for a prediction lesson. Its subject is σ, the degree of
  sampling, which Sutton and Barto treat in §7.6. Only the 19-state paragraph
  bears on n.

## Contradictions

1. **The commission says Section 7.1 "discusses why intermediate n wins." It
   does not.** p. 145 states the finding and calls it an illustration that
   n-step methods "can potentially perform better". No mechanism is offered.
   The nearest sourced material is all indirect. Example 7.1's first paragraph
   (pp. 144–145) counts how many states one episode updates. Figure 7.4
   (p. 147) does the same for Sarsa. Watkins p. 85 says uncorrected truncated
   returns "may have a high variance". Singh and Dayan §4.5 give a mechanism
   for λ: large λ converges faster, small λ has the lower asymptote. A
   "propagates further without the full return's variance" sentence has no
   source behind it for n-step TD on this walk. It stands only with the page's
   own removal test.

2. **Eq. 7.3 cannot explain the win on this walk.** This is my derivation, not
   a source's. The walk is undiscounted, so γ^n = 1, and Eq. 7.3 reads "worst
   error ≤ worst error". Because the walk terminates, the bound can be tightened.
   Rewards before termination are exact in expectation, so
   `E[G_{t:t+n} | S_t = s] − v(s) = E[(V − v)(S_{t+n}) · 1{t+n < T} | S_t = s]`,
   which bounds the error by K·P(T > t+n | S_t = s). From the centre state no
   episode ends in fewer than 10 steps, so for n ≤ 9 that probability is 1 at
   the centre. A constant error V − v = K then gives worst-state error exactly
   K. For every n in 1–9, the guarantee on this walk is no reduction at all.
   Eq. 7.3 is still the convergence argument (p. 144). It does not separate
   n = 4 from n = 1 here.

3. **The best n depends on α.** Figure 7.2 shows each curve's minimum moving
   left as n grows. n = 1 is the lowest curve at the right edge (≈ 0.39 at
   α = 1, against ≈ 0.44 for n = 2). "Intermediate n is best" compares each n
   at its own best α. My check (Numbers) puts the lowest n at fixed α as 32 at
   α = 0.05, 16 at 0.1, 8 at 0.2, 4 at 0.4, 2 at 0.6–0.8, and 1 at 0.9–1.0.

4. **The best n depends on chain length (Exercise 7.3, unanswered in the
   book).** My check: on a 5-state walk with the same measure and α grid, n = 1
   is best (0.22 at α ≈ 0.33, ahead of n = 2 at 0.25), on 3 seeds. Singh and
   Dayan p. 21 make the parallel point for λ: longer trials want larger λ.

5. **The best n depends on how much experience the measure covers.** Figure 7.2
   averages episodes 1–10 only. My check: averaged over episodes 1–50, n = 4 is
   still best, but at α ≈ 0.15, and n = 2 trails it by 0.004. At episodes
   91–100, n = 1 is best (0.06 at α ≈ 0.14, ahead of n = 2 at 0.07), on 3
   seeds. Singh and Dayan §4.5 report the same drift for λ. De Asis et al.
   found n = 3 best over 50 episodes on their two-action walk. "Learns faster"
   matches the early-window measure. A claim that intermediate n ends up with
   better estimates is not supported.

6. **Deep RL found the largest n best.** Hernandez-Garcia and Sutton §4.2 found
   n = 20 best on mountain car and no n "too high". The setting differs in
   control, neural function approximation and target networks. It does not
   contradict Figure 7.2 directly. It shows that "intermediate" depends on the
   problem.

7. **Exercise 7.3's left-outcome question has a short answer under the book's
   own initialisations.** This is my derivation. The map x → (x + 1)/2 sends
   outcomes −1/+1 to 0/+1, initial 0 to 0.5, and true values v to (v + 1)/2.
   The n-step update commutes with that map. The 19-state walk with
   0/+1 outcomes and V₀ = 0.5 (Example 6.2's convention) is therefore an exact
   rescaling of Example 7.1's walk. It has the same best n and α, and every
   error is halved. My check gave 0.133 against 0.266 at n = 4, α = 0.37. The
   change in Example 7.1 matters only if the initial values do not move with
   it.

## Numbers

```text
Figure: v(i) = i/10 − 1, i = 1..19 (−0.9 … +0.9 in steps of 0.1; centre state 10 has v = 0)
Owner:  Sutton, online.lisp (init/targets). Closed form: v = P(right) − P(left), with P(right from i) = i/20 (gambler's ruin)
Scope:  19-state walk, outcomes −1/+1, γ = 1, equiprobable moves
```

```text
Figure: start state = centre (state 10 of 19; zero-based index 9)
Owner:  Sutton, online.lisp (random-walk); Example 6.2 p. 125 for the 5-state analogue
Scope:  every episode
```

```text
Figure: initial RMS error of V ≡ 0 = √0.3 ≈ 0.548
Owner:  derived from the exact values (mean of (i/10 − 1)² over 19 states = 0.3); matches the common α = 0 endpoint (≈ 0.55) of every curve in Fig. 7.2, p. 145
Scope:  before any episode
```

```text
Figure: n plotted = 1, 2, 4, 8, 16, 32, 64, 128, 256, 512
Owner:  Fig. 7.2 labels, p. 145; online.lisp (online-nstep)
Scope:  —
```

```text
Figure: α grid = exp(k/10), k = −50 … 0 (51 values, 0.0067 to 1), plus α = 0 drawn at the initial error
Owner:  online.lisp (online-nstep); not stated in the book
Scope:  —
```

```text
Figure: 100 runs × first 10 episodes; same walks for every (n, α); per-episode RMS over 19 states averaged over episodes and runs
Owner:  S&B p. 145; online.lisp (setup 100 10, learning-curve-nstep)
Scope:  —
```

Figure 7.2 minima, read from the plot at 300 dpi. Tolerance is about ±0.005 in
error and ±0.02 in α. These are approximate. No table is published.

```text
Figure: n=1 ≈ 0.347 at α ≈ 0.82 (≈ 0.39 at α = 1) | n=2 ≈ 0.28 at α ≈ 0.6 | n=4 ≈ 0.267 at α ≈ 0.37 (lowest) | n=8 ≈ 0.28 at α ≈ 0.22 | n=16 ≈ 0.31 at α ≈ 0.13 | n=32 ≈ 0.36 at α ≈ 0.08 | n=64 ≈ 0.41 at α ≈ 0.05 | n=128 ≈ 0.46 | n=256 ≈ 0.485 | n=512 ≈ 0.49
Owner:  S&B Figure 7.2, p. 145
Scope:  average RMS over 19 states and first 10 episodes, 100 runs
```

```text
Figure: mean episode length from the centre = 100 steps; P(T > n) = 1.000 (n = 9), 0.998 (10), 0.975 (16), 0.840 (32), 0.571 (64), 0.259 (128), 0.053 (256), 0.002 (512)
Owner:  derived (exact absorbing-chain computation; mean = i(20 − i) at i = 10). No source states it.
Scope:  19-state walk from the centre. n = 512 is Monte Carlo on 99.8% of episodes, n = 256 on about 95%. From the centre, an n-step return with n ≤ 9 always bootstraps.
```

```text
Figure: Watkins bound max_x |E[r^(n)(x)] − V_f(x)| ≤ γ^n K
Owner:  Watkins 1989, p. 86
Scope:  K = max error of current U; γ < 1 assumed (p. 85)
```

```text
Figure: n = 3, α = 0.4 representative best on the 19-state walk
Owner:  De Asis et al. 2018, "19-State Random Walk"
Scope:  Q(σ) action values, two-action walk, 50 episodes, 100 runs
```

```text
Figure: n ∈ {1, 3, 5, 10, 20}; n = 20 best in initial and overall performance
Owner:  Hernandez-Garcia and Sutton 2019, §4.2
Scope:  mountain car, DQN-like network, 100 runs
```

**Researcher's reproduction (throwaway, not a citable source).** I wrote this so
the editor can check that the writer's setup matches. It follows online.lisp:
centre start, −1/+1, V₀ = 0, online n-step TD, 100 runs × 10 walks, the same
walks for every setting, and the log α grid. Python's `random.Random(seed)`
replaces Sutton's generator, so the walks differ from the book's.

```python
import math, random
N = 19; TRUE = [2 * (i + 1) / (N + 1) - 1 for i in range(N)]
def walks(seed, runs=100, eps=10):
    rng = random.Random(seed); out = []
    for _ in range(runs):
        rs = []
        for _ in range(eps):
            x = N // 2; xs = []
            while 0 <= x < N:
                xs.append(x); x += 1 if rng.random() < 0.5 else -1
            rs.append((-1.0 if x < 0 else 1.0, xs))
        out.append(rs)
    return out
def score(W, n, alpha):
    tot = 0.0; c = 0
    for run in W:
        w = [0.0] * N
        for outcome, xs in run:
            for t, s in enumerate(xs):
                g = outcome if n >= len(xs) - t else w[xs[t + n]]
                w[s] += alpha * (g - w[s])
            tot += math.sqrt(sum((a - b) ** 2 for a, b in zip(w, TRUE)) / N); c += 1
    return tot / c
W = walks(0)
for n in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]:
    e, a = min((score(W, n, math.exp(k / 10)), math.exp(k / 10)) for k in range(-50, 1))
    print(n, round(a, 3), round(e, 3))
```

```text
Figure: seed 0 minima: n=1 0.346@0.819 | n=2 0.279@0.607 | n=4 0.266@0.368 | n=8 0.278@0.223 | n=16 0.312@0.135 | n=32 0.361@0.082 | n=64 0.413@0.050 | n=128 0.456@0.030 | n=256 0.481@0.022 | n=512 0.486@0.020
Owner:  researcher's reproduction (above); agrees with the Fig. 7.2 readings to within reading tolerance
Scope:  100 runs × 10 episodes
```

```text
Figure: seeds 1–5, minima for n = 1, 2, 4, 8, 16: n = 4 lowest on every seed (0.260–0.272 at α = 0.37); n = 2 and n = 8 within 0.002 of each other and swap order across seeds (0.273–0.286); n = 1 0.343–0.349 at α = 0.82
Owner:  researcher's reproduction
Scope:  as above. n = 4 is the robust winner. The order of n = 2 and n = 8 is noise at 100 runs.
```

```text
Figure: lowest n at fixed α (seeds 0 and 1 agree): α 0.05 → n 32 | 0.1 → 16 | 0.2 → 8 | 0.4 → 4 | 0.6 → 2 | 0.8 → 2 | 0.9 → 1 | 1.0 → 1
Owner:  researcher's reproduction
Scope:  n ∈ {1, …, 64}, first 10 episodes
```

```text
Figure: 5-state walk (−1/+1, V₀ = 0; also 0/+1, V₀ = 0.5): n = 1 best, 0.22 @ α ≈ 0.33 (second: n = 2, 0.25); 19-state averaged over episodes 1–50: n = 4 0.185 @ 0.15, n = 2 0.189; 19-state at episodes 91–100: n = 1 0.06 @ 0.14, n = 2 0.07, n = 4 0.075
Owner:  researcher's reproduction (seeds 0–2 agree)
Scope:  same measure and α grid; changes only chain length or averaging window
```

## Limits

- Kearns and Singh (2000), "Bias-Variance Error Bounds for Temporal Difference
  Updates" (COLT 2000), at https://www.cis.upenn.edu/~mkearns/papers/tdlambda.pdf,
  was not opened. curl failed TLS verification on that host, WebFetch returned
  503, and an archive fetch was refused. The bias–variance trade-off in n
  appears here only as Hernandez-Garcia and Sutton's one-sentence repetition.
  Do not cite Kearns and Singh.
- No source gives a mechanism for why intermediate n wins on this walk. Sutton
  and Barto §7.1 gives none, and Singh and Dayan's mechanism is for λ.
- No source answers Exercise 7.3. The 5-state and late-episode results are my
  throwaway runs, not citable. The writer must produce any such result with the
  lesson's own code.
- Sutton and Barto's text does not state the 19-state start state or the α
  grid. Both come from Sutton's online.lisp.
- Figure 7.2 values are read off a plot. The book publishes no table.
- Section 7.1 has no worked derivation of Eq. 7.3. Watkins says the proof is
  "essentially the same" as his one-step local improvement theorem (p. 87) and
  does not print it there. A derivation on the page is the writer's own, which
  the series allows.
- Singh and Dayan are cited from the authors' manuscript. Page numbers are
  manuscript pages. Figure 10's chain is not named in the passage I read.
- Watkins p. 86's page number is illegible in the scan ("%"). The page is
  identified by sequence.

## Source assets

```text
Asset: Figure 7.2, S&B p. 145 (PDF p. 167): RMS error against α, curves for n = 1 … 512
Shows: the U-shaped curves, each minimum moving left as n grows, n = 4 lowest
Crop:  keep both axis labels, every n label and the caption. The book is CC BY-NC-ND 2.0, and the commission says to reproduce the figure with the lesson's code, not copy it. Use it only for the editor's comparison.
```

```text
Asset: Figure 7.1, S&B p. 142: backup diagrams from 1-step TD to ∞-step TD/Monte Carlo
Shows: the spectrum of targets as a row of diagrams, the structure the main idea names
Crop:  keep all five column labels and the caption; same licence note
```

```text
Asset: pseudocode box "n-step TD for estimating V ≈ v_π", S&B p. 144
Shows: the τ ← t − n + 1 bookkeeping and the Until τ = T − 1 tail
Crop:  None needed; the lesson's own listing replaces it (transcribed above)
```

```text
Asset: Figure 12.3, S&B p. 291: off-line λ-return beside n-step TD on the same task
Shows: both bootstrapping parameters give intermediate optima of similar size
Crop:  only for a Go-deeper reference; keep both panels' labels
```

```text
Asset: Watkins 1989, printed p. 86 (PDF p. 93): the 1989 definition of the "corrected n-step truncated return" and the γ^n K bound
Shows: the origin of Eq. 7.1 in its original notation
Crop:  keep the italic term, the formula, and the max-error line; omit the page-number artefact
```

Sutton's code, Singh and Dayan, Hernandez-Garcia and Sutton, De Asis et al.:
None found that the lesson needs.

## Discarded

```text
http://incompleteideas.net/book/code/offline.lisp: the off-line variant (updates applied at episode end; 1st-edition lower graph). Chapter 7's Eq. 7.2 is online, so online.lisp is the matching file. Read only to confirm the shared setup (19 states, −1/+1, centre start).
http://incompleteideas.net/book/code/nstep-walk.tar: a 1998 C port by another author (files dated October 1998). The Lisp is the authors' own code. Listed, not used.
https://www.cs.rhul.ac.uk/~chrisw/thesis.html: author's landing page; used only to confirm the PDF's provenance.
https://mlanthology.org/mlj/1998/singh1998mlj-analytical: bibliographic index; used only for Singh and Dayan's volume and pages while Springer was gated.
```
