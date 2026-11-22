# Commission: reinforcement-learning/held-out-levels

Run date: 2026-11-22. Scheduled duty, open section, no commissions supplied.
Template: lesson. Voice guide: pinned by the series (`writing-coach/01/voice-guide.md`), so no writing coach runs.

## Where the course stands

Stage 3, designing environments. Published so far in stage 3: observation
scale, frame stacking and the Markov property, action frequency, action
discretization, action masking in Q-learning, action masking in MaskablePPO,
specification gaming, potential-based shaping, reward scale. Remaining in
stage 3: "Held-out levels, procedural generation, domain randomization, and
checks for memorized behavior", then the stage project. That item holds more
than one idea, so it becomes two lessons. This lesson takes held-out levels,
procedural generation and checks for memorized behavior. Domain randomization
(randomizing an environment's physical parameters) is the next lesson; mention
it in at most one sentence as what comes next, without teaching it.

Taught and usable without re-teaching: MDPs, returns and discounting, Bellman
equations, value and policy iteration, the Gymnasium contract with termination
and truncation and `reset(seed=...)`, checking a custom environment, training an
off-the-shelf PPO agent with Stable-Baselines3 (algorithm not yet taught),
separate evaluation environments and several seeds, Monte Carlo and TD
prediction, epsilon-greedy, SARSA, Q-learning, importance sampling, n-step
returns, semi-gradient TD with function approximation, the deadly triad,
observation normalization, the Markov property and frame stacking, action
spaces and masking, specification gaming, potential-based shaping, reward
scale. Not taught: DQN, policy gradients, PPO's internals, entropy bonuses,
recurrent policies. Do not rely on any of these.

## Topic and the one idea

Topic: training on a fixed set of levels and testing on levels the agent has
never seen.

The one idea: an agent's return on the levels it trained on cannot tell
whether it learned the task or memorized those levels, because a policy that
maps a level's states to the right moves by heart scores the same there as one
that reads the level. Only levels drawn from the same generator and held out
of training measure that, and the gap between training-level and held-out
return is the measurement. Two things decide whether that gap can close: the
observation has to carry what differs between levels (an agent that observes
only its position cannot generalize across layouts whatever it trains on, and
this follows from the construction, so derive or argue it in full), and the
number of distinct training levels has to be large enough.

What the lesson must leave the reader able to do: build a procedural level
generator keyed on Gymnasium's reset seed, split seeds into training and
held-out sets, train, and report both returns with the gap; and say, from an
environment's observation alone, whether an agent could generalize across its
levels at all.

## The case to start from

A new environment: a small grid maze (or gridworld with walls, a goal and
perhaps a hazard) whose layout is generated from the seed passed to
`reset`, as a Gymnasium environment. Sizes are the writer's, chosen so runs
finish in minutes on a laptop CPU. Two observations of the same environment:
(a) the agent's position only, (b) a local view (for example the cells around
the agent plus the direction to the goal) that carries layout information.
The writer chooses the learner. Tabular Q-learning over the local-view
observation is a table shared across levels and is fast; SB3 PPO used off the
shelf (as in training-an-off-the-shelf-agent) is also allowed. Explain neither
beyond what earlier lessons taught.

Candidate results (at most two, writer's choice and design):
1. Position-only agent on one or a few training levels: near-perfect training
   return, near-chance held-out return; the local-view agent trained the same
   way does better on held-out levels.
2. Held-out return and the gap as a function of the number of distinct
   training levels (e.g. 1, 4, 16, 64, 256 levels), across seeds.
A check for memorized behavior beyond the held-out split (for example,
perturbing one wall on a training level, or replaying a training level's
action sequence blind on another level) may support result 1 as its removal
test.

Link the lessons that introduced what is reused: the Gymnasium contract and
reset seeds, training-an-off-the-shelf-agent (separate evaluation environment,
seeds, baselines), frame-stacking-and-the-markov-property (what the
observation carries), Q-learning.

Mention only (a sentence and pointer each): Cobbe et al. 2019/2020 (CoinRun,
"Quantifying Generalization in Reinforcement Learning"; Procgen Benchmark) as
the study of training-level count against held-out return and Procgen's way of
generating levels from a seed, without installing its package; Zhang et al.
2018 "A Study on Overfitting in Deep Reinforcement Learning" (agents that
memorize random level sets); optionally Kirk et al. 2023 survey of zero-shot
generalisation in RL for Go deeper. Sim-to-real goes with domain randomization
in the next lesson.

## Boundaries

- At most two experimental results, each checked as the series prompt requires
  (new seeds, the worst case for the explanation, removal tests on the page).
- Code as `uv run` scripts with inline metadata, run exactly as printed,
  finishing in a few minutes on a laptop CPU, under about 100 lines each.
- Draw what the agent learned: several generated levels (training and
  held-out) with the agent's paths or policy drawn on them as inline SVG that
  follows the themes; a chart of held-out vs training return against the
  number of training levels as inline SVG, checked against printed output.
- End with an `nb-note` of two or three problems with answers in `details`.
  One asks about a case the lesson did not work through (for example, a
  generator whose held-out levels are drawn from a different distribution,
  or an observation that carries layout but not the goal).
- Do not teach domain randomization, recurrent policies, or PPO's algorithm.

## Recent patterns to break (from the last lessons)

- Recent headlines are short narrative claims about one agent in one named
  environment ("A courier paid for every move never delivers", "Looping
  through a checkpoint worth 1 beats a finish worth 10 at a discount of 0.99",
  "MaskablePPO's network never learns which moves are illegal"). Several use
  "never". Avoid "never" and avoid a headline built on a single number
  comparison.
- Recent deks begin "On a <size> <environment>, ..." (reward-scale,
  action-discretization) or "When only ..., ..." or carry an "only if" turn.
  Build this dek differently.
- Recent "Why this matters" openers recall an earlier lesson's environment or
  open "An agent paid only at ...". Open on this lesson's own case.
- Go-deeper lines have settled into "Name, Title: section (pages) does X";
  vary what each line says about why to read it.

## Neighbours in tonight's edition

The daily brief and a feature on international-student enrollment; neither
touches RL.

## Production record

Series production policy is `required: true`: researcher, writer and editor at
the orchestrator's model ("inherit") and effort xhigh. The runtime honours this:
each runs as a subagent on the inherited model at xhigh effort.

## Decisions after research

- Report training and held-out return side by side, never the gap alone: a gap
  also closes when training return falls (Cobbe et al. 2019 App. E), and a
  random policy has a gap near zero. The one idea is restated accordingly: the
  gap measures generalization only alongside a training return that shows the
  agent learned.
- State the impossibility claim for policies that act on the current
  observation only. A position-only agent with memory could infer walls from
  failed moves; one sentence says so and points forward (recurrent policies
  are stage 6).
- The held-out split is the test. A perturbation of a training level is at
  most a supporting check, and Zhang et al. found such checks can miss
  memorization; say so if one is used.
- Level count and observation are necessary conditions, not the whole story:
  one sentence citing Cobbe's architecture gap at 4,000 levels (Nature-CNN vs
  IMPALA-CNN); do not teach architectures.
- Level generator design: the environment picks each episode's level seed
  from its own `self.np_random` over a fixed list of allowed level seeds given
  at construction (training list vs held-out list), in the spirit of Procgen's
  `start_level`/`num_levels`. Do not rely on passing a seed to every `reset`,
  because SB3's DummyVecEnv auto-resets without a seed (evidence record).
- Choose layouts a memoryless local-view policy can actually solve (for
  example, open grids with scattered walls or a hazard, rather than mazes with
  dead ends), and say why in a sentence; Cobbe's maze agent used an LSTM.
- Position-only held-out return need not be near chance; report what the run
  gives.
- All numbers for the lesson's own results come from the writer's runs; the
  papers' level counts (hundreds to tens of thousands) are cited as theirs.
