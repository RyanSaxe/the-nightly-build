# Commission: reinforcement-learning/reward-scale

Run date: 2026-11-21. Scheduled duty, open section, no commissions supplied.
Template: lesson. Voice guide: pinned by the series (`writing-coach/01/voice-guide.md`), so no writing coach runs.

## Where the course stands

Stage 3, designing environments. Published so far in stage 3: observation scale,
frame stacking and the Markov property, action frequency, action discretization,
action masking in Q-learning, action masking in MaskablePPO, specification gaming,
potential-based shaping. The stage 3 item "Reward specification, reward scale, and
specification gaming" has had its specification-gaming part and none of its
reward-scale part. This lesson takes reward scale. Held-out levels and the stage
project come later.

Taught and usable without re-teaching: MDPs, returns and discounting, Bellman
equations, value and policy iteration, Gymnasium contract with termination and
truncation, checking a custom environment, training an off-the-shelf PPO agent
(algorithm not yet taught), Monte Carlo and TD prediction, epsilon-greedy, SARSA,
Q-learning, importance sampling, n-step returns, semi-gradient TD, the deadly
triad, observation normalization (including VecNormalize for observations),
specification gaming, potential-based shaping. Not taught: DQN, Atari, policy
gradients, PPO's internals, entropy bonuses. Do not rely on any of these.

## Topic and the one idea

Topic: changing the reward's numbers without changing which rewards it pays.

The one idea: multiplying every reward by a positive constant leaves every
policy's ranking, and so the optimal policy, unchanged, while clipping rewards
into a fixed range or adding a constant to every step's reward can change the
optimal policy. Clipping can because it changes the ratios between rewards.
Adding a constant can in an episodic task because the number of steps before
termination then changes a return by an amount that differs between policies.
Derive the scaling result and the shift result in full (they are short); the
clipping case follows from an instance.

What the lesson must leave the reader able to do: look at a reward transformation
(scale, shift, clip, normalize by a running statistic) and say whether it can
change the optimal policy, and why.

A second, practical point the lesson can make with at most one result: even when
the optimum is unchanged, scale is not free for a learner whose step size and
starting estimates are fixed numbers, since Q-learning's starting estimates of 0
are optimistic or pessimistic only relative to the reward's size. The writer
decides whether this is one of the lesson's two results or a sentence.

Mention only (a sentence and pointer each, no section): DQN's clipping of Atari
scores to [−1, 1] as the famous instance (cite Mnih et al. 2015 Methods); reward
normalization by a running return statistic as done in VecNormalize and the
PPO implementation-details literature (Engstrom et al. 2020 "Implementation
Matters" or Huang et al. ICLR blog track 2022). Neither algorithm is taught yet,
so do not explain DQN or PPO.

## The case to start from

A new environment: a small courier grid. The agent starts in a corridor or grid
with a near drop-off paying a small reward and a far one paying a larger reward,
each ending the episode, and a per-step reward. Sizes and values are the writer's
to choose so that: under the raw reward the far drop-off is optimal, under
clipping to [−1, 1] the near one becomes optimal, and under an added constant
(for example shifting the per-step charge from −1 to 0 or to a positive value)
the optimal policy changes again, in the extreme to never delivering. The
writer may choose the discount and must say it. Build it as a Gymnasium
environment so it fits the course's contract, and solve it exactly with value
iteration so each claim about the optimal policy is checked by an exact solver,
then show that Q-learning learns what value iteration says.

Link specification-gaming (its race and loop arithmetic) and potential-based-shaping
(the shift there was the potential difference, which is why it was safe; the
contrast with an arbitrary constant shift is worth one or two sentences). Link
the lessons that taught value iteration and Q-learning where used.

## Boundaries

- At most two experimental results, each checked as the series prompt requires
  (new seeds, the worst case for the explanation, removal tests on the page).
- Code as `uv run` scripts with inline metadata, run exactly as printed,
  finishing in a few minutes on a laptop CPU, under about 100 lines each.
- Draw what the agent learned: the policy on the grid under each reward, as
  inline SVG that follows the themes. The same grid diagram can return with the
  changed arrows marked.
- End with an `nb-note` of two or three problems with answers in `details`.
  One problem asks about a transformation the lesson did not work through
  (for example, a positive scale combined with a shift in a continuing task, or
  clipping a reward that is already within range).
- Do not explain DQN, PPO or VecNormalize's algorithm.

## Recent patterns to break (from the last lessons)

- The last several "Why this matters" openers begin by recalling an earlier
  lesson's environment ("In the race from specification gaming, ...") or by a
  sentence of the form "An agent paid only at ... ". Open on this lesson's own
  case instead.
- Headlines in the series have become long single-clause claims with one
  embedded number and a "so"/"once"/"only if" turn in the dek
  ("... leaves the optimal policy alone", "... learns them only if ...").
  Avoid "leaves ... alone" (used on 20 November) and the dek pattern
  "X, so Y" which several recent deks use.
- Three of the last five lessons used the eight-cell race or the Tower of Hanoi;
  this lesson uses a new environment, as decided above.
- Go-deeper lines have settled into "Name, Title: section (pages) does X";
  that form is furniture-like and acceptable, but vary what each line says
  about why to read it.

## Neighbours in tonight's edition

The daily brief and a feature run tonight; neither touches RL. No overlap risk.

## Production record

Series production policy is `required: true`: researcher, writer and editor at
the orchestrator's model ("inherit") and effort xhigh. The runtime honours this:
each runs as a subagent on the inherited model at xhigh effort.

## Decisions after drafting

- Two end problems instead of three: within the series' "two or three". Settled.
- Scale's effect on learning: tabular Q-learning from 0 is exactly invariant to
  a positive scale, so the lesson treats scale's practical effect in one
  paragraph through a nonzero starting estimate, not as a result. Settled.
- The paraphrase of Baselines issue #538 stands if the editor finds it faithful
  to the issue's words.
