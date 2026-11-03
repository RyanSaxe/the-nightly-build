# Commission: reinforcement-learning/action-values-from-samples (lesson 4)

Authorized by `nb duty` for 2026-11-03 (open course; next lesson chosen by the orchestrator).
Template: lesson. Not strict; band 2,500–6,000 words including code and output; 2–5 flex sections;
at least one source. The voice guide is pinned by the series (writing-coach/01 was written by
`nb start-article`); no writing-coach run.

## Where the course stands

Published: 1 `environments-and-the-rl-problem` (MDP, return, Bellman expectation, exact solve,
prints `gridworld.py`); 2 `finding-optimal-policies` (policy improvement, policy iteration, value
iteration, using the known model); 3 `learning-values-from-samples` (first-visit and every-visit
MC prediction, TD(0), bias and variance, step-size schedules; prints `estimators.py` and
`compare.py`). Lesson 3 closes on "A value function cannot yet choose a better move": choosing a
move from V needs the model, which the sampling agent does not have.

## The topic and the one idea

Stage 2, "Action values from samples and generalized policy iteration".

One idea: an agent that estimates the value of each (cell, move) pair, q(s, a), from episodes
can improve its policy without the move probabilities, because the greedy choice over q needs no
model; and evaluation need not finish before improvement starts — interleaving partial
evaluation with greedy improvement (generalized policy iteration) still reaches the optimal
policy on this grid.

Derive in full: why greedy improvement over q_π needs no model (lesson 2's policy improvement step
rewritten with q in place of the one-step lookahead), and the policy improvement theorem in its q
form, which lesson 2 already proved for the model-based case — reuse it with a link, do not re-prove
beyond what the q form needs.

## The case to start from

The same 4×4 slippery grid (goal 3 pays +10, pit 6 pays −20, step −1, slip 0.8/0.1/0.1, γ = 0.9)
and lesson 3's fixed policy. Import `gridworld.py` (lesson 1) and, where useful, `estimators.py`
(lesson 3), linking the lessons. Grade against lesson 2's exact optimal policy and values.

## Exploration: a boundary, not this lesson's topic

A greedy agent that only learns about the moves it takes stops learning about the others. This
lesson handles that with exploring starts (each episode begins from a random cell AND a random
first move), stated as an assumption with a sentence on why it is needed and that it is often
unavailable. Why greedy learning stalls without it, and epsilon-greedy, is the next lesson's
topic: show at most one run or one sentence that the assumption matters, and do not teach
epsilon-greedy here. Do not teach SARSA or Q-learning (later lessons).

## Required on the page

- What the agent learned, drawn on the grid: the policy as arrows and q as per-move values
  (e.g. four triangles per cell) at a few points in training, against lesson 2's optimal arrows.
- At most two experimental results that teach the idea (e.g. how many episodes until the greedy
  policy matches the optimal one across seeds; whether improving after every episode versus after
  a full evaluation changes that). Every causal claim gets its removal test on the page.
- Problems in a closing `nb-note`, answers in `details`.

## Sources

Sutton and Barto, Reinforcement Learning: An Introduction, 2nd ed., chapter 5 (Monte Carlo
control, exploring starts, GPI, the open convergence question for MC ES) and section 4.6 (GPI).
Cite the specific sections and pages. The researcher confirms what is known about convergence of
Monte Carlo ES (Sutton and Barto state it as open; check whether later work, e.g. Tsitsiklis 2002
on optimistic policy iteration, or Wang, Yuan, Ross 2020s results on MC ES convergence, settles a
version of it) because the lesson must state that status correctly.

## Neighbours in this edition

daily-brief/2026-11-03; feature/marvell-lumentum-optics. No overlap.

## Recent patterns to break (lessons 1–3)

- Deks open "On lesson 1's slippery grid…" / "On a slippery 4×4 grid…". Do not open the dek with
  the grid.
- Lesson 3's "Why this matters" opens by recapping the earlier lessons ("The first two lessons in
  this course solved…"). Open on the problem instead; recap belongs in the Background band.
- Lesson 3 ends its body on a "cannot yet" pointer section ("A value function cannot yet choose a
  better move"). Don't build the last flex section as a "cannot yet" pointer to the next lesson.
- Lesson 3 printed long experiment scripts; the series prompt caps a script near 100 lines and two
  results. Keep to it.

## Production

Series policy (required: true): researcher inherit/xhigh, writer inherit/xhigh, editor
inherit/xhigh; writing-coach pinned. Runtime: inherit = this orchestrator's model.

## Run log
- researcher/01: inherit model, xhigh effort. Evidence accepted.

## Decisions after evidence (orchestrator)

- The one idea is restated: the commission's "still reaches the optimal policy on this grid" is an
  observation across seeds, never a guarantee. The page states convergence status from the
  peer-reviewed results only (Sutton and Barto p. 99; Tsitsiklis 2002 for the start-pair-only
  variant; Wang et al. 2022 for its MDP class; Delattre and Fournier 2026 for gamma < 1/2), and
  says plainly that this grid (gamma 0.9, revisitable states) is covered by none of them.
  2026 arXiv preprints are optional; if cited, as preprints carrying their authors' hedges.
- Episodes need a step cap during control: a greedy policy mid-training can loop forever. State
  the cap and what a capped episode does to the returns, in a sentence; truncation proper is
  taught with the Gymnasium contract later.
- "Matches the optimal policy" accepts either tied optimal move at cells 9 and 12.
- writer/01: inherit model, xhigh effort. Proof BLOCK 0 WARN 0, 4,055 words.
- Decision (orchestrator): Delattre and Fournier is described only as the authors state their
  result; the page does not say or imply their theorem covers the Sutton and Barto box algorithm
  (that is the researcher's reading). Use the handoff's tighter wording.
- editor/01: inherit model, xhigh effort. Approved. MIT Press link kept: same address as lessons 1–3, which passed CI.
- check_seeds.py and figures.py moved out of writer/01 (the artifact contract allows only the brief/output pair); the seed checks remain listed in draft-handoff.md.
