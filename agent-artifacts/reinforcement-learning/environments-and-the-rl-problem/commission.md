# Commission: reinforcement-learning/environments-and-the-rl-problem

## Place in the course
This is lesson 1. The library holds no published lessons, so this lesson starts
the course and sets the patterns later lessons inherit. Set `order` to 1 in
`nb-meta`. The course assumes fluency in probability, linear algebra,
optimization, PyTorch, production deep learning, and past study of bandits and
regret minimization. It teaches none of that; it builds on the bandit the reader
already knows.

## What this lesson teaches (a short list, taught completely)
The reader finishes able to write down the reinforcement-learning problem as a
Markov decision process and compute how good a fixed policy is. Four ideas, in
this order, each with a plain statement, a worked example on one running
gridworld, and why it matters here:

1. **From a bandit to an environment.** The agent-environment loop: at each step
   the agent sees a state, takes an action, and the environment returns a reward
   and a next state. A bandit is the one-state special case the reader already
   knows; adding states that the action changes is what makes the problem
   reinforcement learning. Define state, action, reward, transition.
2. **The Markov decision process.** The formal object (S, A, P, R, gamma) and the
   Markov property stated in plain words: the next state and reward depend only
   on the current state and action, not the history. Show it on the gridworld.
3. **Return and discounting.** What the agent maximizes: the discounted return
   G_t = sum_k gamma^k R_{t+k+1}. Why gamma is there (convergence of the sum and
   preference for sooner reward), what gamma = 0 and gamma -> 1 mean.
4. **Policies, value functions, and the Bellman expectation equation.** A policy
   pi; the state-value v_pi(s) and action-value q_pi(s,a) as expected return; the
   Bellman expectation equation derived in full as the recursion that relates a
   state's value to its successors'. Then compute v_pi on the gridworld two ways:
   the direct linear solve (I - gamma P_pi)^{-1} r_pi, and iterative policy
   evaluation, and show they agree.

Teach these four and stop. Value iteration, policy iteration, the Gymnasium API,
and training an off-the-shelf agent are later lessons; name them only in the
takeaway as what comes next. If the material does not fit 3600 words, cut idea 4's
iterative-evaluation half before cutting a derivation.

## The running environment (kept and grown through the course)
A small deterministic-or-near-deterministic gridworld: a 4x4 or 5x5 grid with a
goal cell (and optionally one trap), four actions (up/down/left/right), a step
reward that makes the agent prefer short paths, and a terminal goal. This is the
one custom environment the control lessons reuse, so keep it minimal and clean.
Lesson 1 only defines it as an MDP (a transition and reward model) and evaluates
a fixed policy on it; it does not yet wrap it in the Gymnasium API.

## Code (must actually run; report only what the run produced)
Python files with PEP 723 inline script metadata so `uv run file.py` works with
no other setup. Scale every run to finish in seconds on a laptop CPU.
- One file that defines the gridworld MDP (states, the transition and reward
  arrays) and one that evaluates a fixed policy by both methods above and prints
  the value function. The writer runs them and reports the actual printed
  numbers; the prose and the heatmap use those exact numbers.
- Keep `numpy` the only dependency.

## Required visuals (draw the idea before explaining it)
1. The agent-environment loop as an inline SVG (theme variables): state and
   reward going in, action coming out, the clock advancing one step. Draw the
   actual quantities, not a generic cycle.
2. The gridworld drawn as a grid with the goal, the step reward, and one policy's
   arrows on the cells (inline SVG). This shows the MDP concretely.
3. The computed state-value function as a heatmap over the grid, via `nb chart`
   (plotly), from the numbers the code actually produced. Label cells with
   values; cite the lesson's own computation in the caption.
4. The Bellman expectation equation as an annotated `nb-math` figure with every
   symbol defined in the legend.

## Geometry and policy
- Template `lesson`: Why-this-matters bookend, orientation, 2-5 flex sections,
  The-takeaway bookend, Sources. Words 2000-3600 (code counts), not strict.
  flex_sections 2-5. Body sections cited per-section; the two bookends are
  citation-exempt and are the only place the lesson addresses the reader or
  refers to itself. Write the body first, the bookends last. min_sources 4.
- Background band (in Why): optional reading, may point inside or outside the
  paper; there is no earlier lesson to link, so point to outside foundations.
  Go-deeper band (in Takeaway): always outside this paper; name which part of
  each paper to read next and why.

## Boundaries and edition fit
- The feature tonight is about evaluation cost of AI agents; the brief is news
  and model releases. This lesson owns RL foundations. Do not reach into RLVR,
  language models, or deep networks; those are far later stages.
- No hype about RL's importance in general terms. The Why bookend names the
  particular thing at stake in this lesson.

## Production
- writing-coach: model sonnet, effort low.
- researcher: model sonnet, effort high.
- writer: model opus (inherit, per series), effort high.
- editor: model opus (inherit), effort high, required.
Recorded deviations: none; "inherit" served by the orchestrator's Claude Opus,
"capable" by Claude Sonnet. No required model/effort traded down.
