# Commission: reinforcement-learning/sarsa-and-q-learning

Series: reinforcement-learning (open course, template lesson, lesson 6). Stage 2
topic "SARSA and Q-learning". The owner's voice guide is pinned
(writing-coach/01/voice-guide.md); no writing-coach run.

## Topic and the one idea

Temporal-difference control. The lesson takes lesson 3's one-step TD update and
applies it to action values, updating after every move instead of after every
episode as lessons 4 and 5 did. The one idea: the two methods differ only in the
action whose value the target uses. SARSA's target uses the move the ε-greedy
policy actually takes next, so it learns the action values of the policy it follows
and can only rest at the best ε-soft policy that lesson 5 found. Q-learning's
target uses the largest action value in the next cell, so it learns the optimal
action values q* while it behaves ε-greedily. This is where the course first
defines off-policy learning: a target policy (greedy) different from the behavior
policy (ε-greedy). Importance sampling, n-step returns and function approximation
are later lessons; give importance sampling at most a pointer.

## Case to start from

Lesson 5's ε = 0.5 result on the course's slippery 4×4 grid: the best ε-soft policy
turns cell 9 left or down, away from the optimal arrows. Run SARSA and Q-learning
at a fixed ε from the same start policy on the same grid. The commission expects
(the writer must confirm by running) that SARSA's greedy arrows follow the best
ε-soft policy and Q-learning's follow the optimal policy, and that Q-learning's
own ε-greedy behavior can earn less per episode than SARSA's while it does so.
If the runs do not show this, report what they show; do not force it.

Everything else (which experiments, which removal tests, page structure) is the
writer's, within the series prompt's limits: at most two experimental results,
seeds rechecked, causes removal-tested on the page.

## Code and continuity

Reuse the course's environment and code from the earlier lessons (gridworld.py,
estimators.py, mc_control.py, control.py, exploration.py) and link the lessons
that print them. New listings run with `uv run file.py` via inline script metadata
and finish in minutes on a laptop CPU. Charts of the lesson's runs are inline SVG.
Step size and the convergence conditions (GLIE for SARSA, Robbins–Monro step
sizes, every pair visited infinitely often) are stated, cited and not derived;
derive the main idea, which is what each target estimates.

Mention only: Expected SARSA, with a sentence and a pointer. The cliff-walking
example from Sutton and Barto may be a Go-deeper pointer or a one-sentence
comparison, not a second environment.

## Neighbouring articles tonight

Daily brief (news and two technology items, none on RL methods) and a Feature
whose topic is being chosen. No overlap expected.

## Recent patterns to break (from lessons 1–5)

- Deks of lessons 3 and 5 are two clauses joined by ", and" ("Averaging whole
  episodes gives …, and updating after every move gives …"; "… needs a policy that
  sometimes moves at random, and the price …"). Build tonight's dek another way.
- Headlines of lessons 1–5 are claims of the form "<subject> <verb> …". Keep the
  claim, vary the build.
- Lesson 5 ended its body with a table of a swept parameter ("How much ε costs")
  before the Problems note. Do not close tonight on a parameter-sweep table.
- Recurring wording across lessons: "the course's slippery grid", "on this grid",
  "cell 13" as the anchor cell. Use cells the idea needs (cell 9 is the natural one
  tonight), and vary the grid reference.
- Lesson 5's opening section title was a count ("Forty-two moves with no returns")
  and its first figure was a four-triangle action-value grid. A triangle grid is the
  course's established notation and can return; the opening count formula should
  not.

## Production record

| Role | Model | Effort | Note |
| --- | --- | --- | --- |
| writing-coach | not run | — | voice guide pinned by series.yaml |
| researcher | session model (inherit) | xhigh | required; honoured via Agent effort xhigh |
| writer | session model (inherit) | xhigh | required |
| editor | session model (inherit) | xhigh | required |

## Decisions after research (orchestrator)

- "Differ only in the target" is a claim about the update rules. Say so, and teach
  the one other difference Sutton and Barto's boxes print: Sarsa picks its next
  move before the update and Q-learning after. Say where it matters on this grid
  (a move into an edge leaves the agent in the same cell) only if the runs show it
  matters; otherwise one sentence.
- The fixed-ε result for SARSA cites Singh et al. 2000 (Theorems 2–3), and the page
  says their theorem is stated for continuing, discounted tasks and with step sizes
  that shrink. On the course's episodic grid the lesson's runs are the evidence.
  Do not claim the theorem covers this grid. Equating Singh et al.'s ε-greedy class
  optimum with lesson 5's best ε-soft policy is the lesson's own step; show it or
  check it by run (lesson 5's best_soft gives the target values).
- Step sizes: the writer chooses. If runs use a constant α, say what that means for
  the estimates (they keep moving) and how arrows were read off. Cite step-size
  conditions to Sutton and Barto (2.7), p. 33, and do not use the label
  "Robbins–Monro" (no opened document supports it).
- Expected SARSA: one sentence; credit John (1994) as Sutton and Barto do, with the
  name from van Seijen et al. (2009).
- Do not explain what the letter Q stands for.
