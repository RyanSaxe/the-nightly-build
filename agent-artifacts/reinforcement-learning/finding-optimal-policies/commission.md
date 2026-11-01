# Commission: reinforcement-learning/finding-optimal-policies

Lesson 2 of the Reinforcement Learning course. Scheduled run for 2026-11-01.

## Where this sits in the course

Lesson 1 (`reinforcement-learning/environments-and-the-rl-problem`, published
2026-10-31) taught the agent-environment loop, the Markov decision process, the
return and discount, the value function `v_π`, the Bellman **expectation**
equation, and how to evaluate a **fixed, hand-drawn** policy on a slippery 4×4
grid: the direct linear solve `v = (I − γQ)^{-1} b` and iterative policy
evaluation (sweeps `v_{k+1} = b + γQ v_k`), with the max-norm contraction proof.
It computed `v_π(13) = −2.01` for a policy drawn by hand and left the obvious
question open: nobody said that hand-drawn policy was any good.

This lesson answers it: how to **find the best policy**, not evaluate a given
one. It is squarely in curriculum stage 1 ("value iteration and policy
iteration") and reuses lesson 1's exact gridworld unchanged, so the numbers are
directly comparable.

## What this lesson teaches (short list, taught completely)

Teach these and nothing else. Each gets a plain statement, a worked instance on
the grid with real numbers, and the reason it is needed here.

1. **Action value `q_π(s,a)`** — the value of taking action `a` in state `s` and
   then following `π`. Give its one-step form in terms of `v_π`. Needed because
   policy improvement compares actions, and `v_π` alone does not rank them.
   Worked instance (VERIFIED on the grid): the four action values at **cell 14**
   under lesson 1's fixed policy and its `v_π` are up −1.08, right +0.32, down
   −1.78, left −2.55 — the hand-drawn policy takes up, but right is far better.
   Contrast **cell 13**, where the four values are up −2.01, right −2.05, down
   −2.71, left −2.61: the hand-drawn action (up) is already the best there, so a
   single greedy step leaves cell 13 alone. That contrast is the reason one
   sweep is not enough and iteration is needed (cell 13 improves only once its
   neighbours do).
2. **Greedy policy and the policy improvement theorem** — acting greedily with
   respect to `q_π` gives a policy `π'` with `v_{π'}(s) ≥ v_π(s)` at every state
   (no worse anywhere), strictly better at some state unless `π` is already
   optimal. Give the one-step argument (the telescoping that turns one greedy
   step into the inequality over whole returns). Worked instance (VERIFIED):
   improving lesson 1's fixed policy to the optimal one leaves the **top half
   unchanged** — cells 0, 1, 2, 4, 5, 7 have exactly the same value under both
   policies — and strictly improves the **bottom two rows (cells 8-15)**, the
   cells that sit near the pit, by +0.001 (cell 8) up to +1.69 (cell 14) and
   +1.29 (cell 13). State the inequality as `≥` and show the per-cell gains;
   do NOT claim "better at every cell" (it is false here, and the theorem only
   promises no-worse).
3. **Policy iteration** — evaluate, improve, repeat until the policy stops
   changing. It reaches an optimal policy in finitely many steps because there
   are finitely many deterministic policies and each round strictly improves
   until the fixed point. Ties matter and must be handled explicitly: cells 9
   and 12 have two actions of equal optimal value, so the count depends on the
   tie rule. VERIFIED: with a keep-the-old-action-on-a-tie rule, policy
   iteration converges in **3 rounds**; with plain argmax it takes **4**. State
   the tie rule you use and, at a tied cell, compare by `q`-values rather than
   relying on argmax. Show the policy grids `π_0 → π_1 → … → π_*` with their
   value heatmaps.
4. **The Bellman optimality equation** (`v_*`, and `q_*`) — the optimal value is
   the fixed point of the same backup with a `max` over actions instead of an
   average under a policy. State both forms. This is the equation value
   iteration solves.
5. **Value iteration** — apply the optimality backup as an update
   `v_{k+1}(s) = max_a Σ_{s'} P(s'|s,a)[R(s') + γ v_k(s')]`; it is a max-norm
   contraction for γ < 1 (the `max` operator is a non-expansion, so lesson 1's
   contraction argument carries over), converging to `v_*`; read off the greedy
   policy at the end. Worked instance (VERIFIED): on the grid value iteration
   takes **18 sweeps** to a max-norm tolerance of 1e-4 and **30** to 1e-8, and
   its greedy policy matches policy iteration's `π_*`. Report your own run.

Tie the two together at the end as the same idea in different proportions
(evaluate then improve, versus one improvement folded into every sweep). Do NOT
open a new topic beyond this: asynchronous/in-place DP, modified policy
iteration, and anything sample-based (Monte Carlo, TD) are later lessons. A
one-sentence pointer that sampling comes next is fine; a section on it is not.

## The finding (the original work — one sentence)

On lesson 1's exact grid (slip 0.2, γ = 0.9), a handful of evaluate-and-improve
rounds reach the optimal policy: it is no worse than the hand-drawn policy
anywhere and strictly better on the bottom two rows near the pit, where it
raises cell 13 from −2.01 to −0.71 and cell 14 from −1.08 to +0.61, while
leaving the top half untouched. The hand-drawn policy was already optimal there.
Value iteration reaches the same policy by folding a single greedy step into
each sweep. Report the real numbers the code prints: rounds for policy iteration
(with the tie rule stated), sweeps for value iteration at a stated tolerance, the
optimal values grid, and the per-cell change from lesson 1's policy.

## Boundaries

- Reuse lesson 1's gridworld **unchanged** (same cells, GOAL=3, PIT=6, rewards
  +10 / −20 / −1, slip 0.2, γ = 0.9) so results compare directly. The code
  imports `gridworld.py` from lesson 1 (recreate it verbatim to run; the writer
  brief carries the exact source). Link lesson 1 in Background as the place
  `gridworld.py`, the fixed policy, and policy evaluation were established.
- The reader has lesson 1's content available by link but the lesson still
  stands on its own: restate `v_π`, the one-step backup, and `Q`, `b` in a
  sentence each where first used, without re-deriving them.
- Audience per `press/editorial.md`: fluent in probability, linear algebra,
  optimization; new to RL. Define every RL-specific term on first use.
- Every run reported must be a run that actually happened. Scale to a second or
  two on a laptop CPU (14-state grid; trivial).

## Visuals (draw the mechanism, per press/editorial.md)

At least: (a) a backup/decision diagram for the greedy `max` at one cell — the
optimality backup drawn as choosing the best action branch, contrasted with
lesson 1's expectation backup that averaged under π; (b) the policy-iteration
sequence as policy grids with value heatmaps (arrows flipping toward `π_*`),
in the lesson's established grid-figure style; (c) a figure comparing policy
iteration and value iteration converging (e.g. value at a cell, or max error,
against round/sweep). Prefer inline SVG with theme variables for drawn
diagrams, and `nb chart` (Plotly) for computed heatmaps/curves. Look at every
visual rendered before handing on; the proof does not catch overlapping labels
or short arrows.

## Sources (min 4)

The researcher (`researcher/01/evidence.md`) has anchored the sources; use it.
Key anchors and CORRECTIONS the researcher established (honor them):
- Sutton & Barto 2nd ed.: `q_π` (3.13); policy improvement theorem (4.7)/(4.8)
  with the telescoping chain and greedy (4.9); policy iteration §4.3 and finite
  termination; value iteration §4.4 and (4.10); the discounted Bellman
  **optimality** equation (3.19). Anchor the optimality equation to S&B (3.19),
  **not** to Bellman's 1957 journal paper — the researcher read all six pages of
  that paper and it carries only the finite-stage max recurrence and
  average-reward asymptotics, with no discount and no policy iteration. Do not
  cite Bellman 1957 for discounted optimality or policy iteration.
- Howard 1960 *Dynamic Programming and Markov Processes* for the origin of
  policy iteration: the discounted treatment is **chapter 7** (value-determination
  operation, policy-improvement routine, the iteration cycle), not chapter 4
  (which is the average-reward version). Primary attribution for the algorithm.
- The max-norm contraction of the optimality operator (the `max` non-expansion
  step) is anchored to Bertsekas *Abstract Dynamic Programming* ch. 1 (used in
  lesson 1) and a lecture proof; S&B state but do not prove it.
- Real case for "Why this matters": AlphaGo Zero (Silver et al., 2017). State it
  ACCURATELY per the researcher's correction: the paper calls its Monte Carlo
  tree search a **policy improvement operator** and the self-play-plus-search
  outcomes the **policy evaluation**, and trains the network to match both,
  describing the whole loop as an "approximate policy iteration scheme." Do NOT
  say the network performs the evaluation. Keep the claim to what the paper says.
Never cite a homepage; use the anchors in `evidence.md`.

## Recent-pattern notes (break these; do not reproduce lesson 1's shapes)

From lesson 1, to avoid repeating:
- **Title mould.** Lesson 1's title was a plain declarative finding of the form
  "The value of a state is an average you can solve for" (noun + "is a … you
  can …"). Write lesson 2's title as a different construction. State this
  lesson's finding (finding the best policy, cheaply, by iterating), not that
  pattern.
- **Dek mould.** Lesson 1's dek was one long sentence of specific numbers joined
  by "and" ("…20,000 episodes and one linear solve put cell 13 at about −2, and
  the discount turns out to be needed only by a policy that never ends"). Do not
  copy the "and the X turns out to be …" tail or the comma-and compound. A plain
  one-sentence dek with this lesson's own number.
- **Section headings.** Lesson 1 used argument-step headings, several built as a
  clause with a verb acting on cells ("Cycles between cells force a joint solve",
  "Only a policy that never ends needs the discount"). Build lesson 2's headings
  differently from each other and from those; no "X forces Y" / "Only X needs Y"
  repetition.
- **Takeaway.** Lesson 1's takeaway closed in the first person ("I would remember
  the pair of them"). A first-person close is allowed in the bookend but do not
  reuse the "I would remember …" move; resolve this lesson's own opener instead.
- Required apparatus is not a habit to avoid: the bookends, the Background/Go
  deeper bands, grid figures, `nb-code`, `nb-math`, and the `nb-note` problems
  are all expected. Reusing the grid-figure visual language from lesson 1 is
  continuity, not formula.

## Production (model and effort; tier→model deviations recorded)

The runtime exposes model tiers through named subagents, so "inherit" is run on
the orchestrator's model (Opus) and "capable" on the closest available capable
model (Sonnet). Recorded actuals for this article:
- writing-coach: Sonnet, effort low (policy: capable / low).
- researcher: Sonnet, effort high (policy: capable / high).
- writer: Opus, effort high (policy: inherit / high — honored).
- editor: Opus, effort high, required (policy: inherit / high — honored).

## Edition neighbours (so the paper reads as one)

Published alongside this lesson on 2026-11-01: a Daily Brief (six short items)
and a Feature. This lesson shares no ground with them; it is the Courses piece.
Keep it self-contained and do not reference the day's news.
