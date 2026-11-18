# Commission: reinforcement-learning/action-masking-in-maskable-ppo

Authorized by: `nb duty` for 2026-11-18 (open section, no commissions; topic chosen by the orchestrator).
Template: lesson. Bands: 2,500 to 6,000 words (code and printed output count), 2 to 5 flex sections,
not strict. Minimum 1 source. Voice guide pinned by the series (writing-coach/01/voice-guide.md, written by
`nb start-article`; no writing-coach run).

## Topic

Stage 3, "Action masking in Q-learning and in an off-the-shelf agent". The 17 November lesson
(`action-masking-in-q-learning`) taught the Q-learning half on the four-disk Tower of Hanoi, with
hanoi.py exposing `action_masks()` and saying an off-the-shelf agent, MaskablePPO, "a later lesson
trains". This lesson is that later lesson: the off-the-shelf half.

## The one idea

An off-the-shelf agent takes the mask from the environment at every step and removes illegal actions
from its policy's distribution before sampling, so it never spends a step or a gradient on an illegal
move and needs no invented consequence (penalty, no-op) for one. The mask is an input like the
observation: it has to reach the agent wherever the agent chooses an action, including evaluation and
any vectorized or wrapped environment, or the trained agent picks illegal moves.

## Case to start from

The four-disk Tower of Hanoi from `hanoi.py`, printed in the 17 November lesson, imported from that
lesson by link (the course allows importing a file printed in an earlier lesson). Compare MaskablePPO
(sb3-contrib) using the mask against a plain PPO baseline that must cope without it, under a rule the
writer chooses and states for what an illegal move does. Use random and scripted baselines in the way
the 8 November lesson (`training-an-off-the-shelf-agent`) established, and a separate evaluation
environment.

The experiments, the causes to test, and the page's structure are the writer's.

## Boundaries

- Use MaskablePPO as a library. Do not explain PPO's algorithm or derive why a masked policy gradient
  stays valid: stage 5 teaches PPO and stage 6 teaches "Masking in policy gradients and why the
  gradient stays valid". A sentence and a forward pointer is the most either gets.
- Do not reteach the Q-learning masking result; link it.
- Pin versions consistent with the course (gymnasium 1.4.0, stable-baselines3 2.9.2, torch CPU wheel as
  in agent.py) unless the researcher finds that sb3-contrib's current release needs otherwise, and
  verify the current sb3-contrib release and MaskablePPO API (action_masks method, ActionMasker wrapper,
  `predict(..., action_masks=...)`, `get_action_masks`, MaskableEvalCallback) as of November 2026.
- Every experiment finishes within a few minutes on a laptop CPU. At most two experimental results.

## Neighbours in tonight's edition

Daily Brief (news) and a Feature on a separate topic; no overlap.

## Recent patterns to break (from the last five lessons)

- Headlines have each been one declarative finding with a number or a named environment, often
  "X does Y on Z" with a trailing "since"/"because" clause in the dek. Five deks in a row explain a
  mechanism with "since", "because" or "so"; vary the dek's construction.
- The 17 November lesson opened its first flex section on "estimates are never updated" and closed on a
  mechanism heading; recent lessons each open with one surprising number then a listing of the
  environment. Do not open with a full reprint of the environment listing; it is printed in the
  previous lesson.
- Bookend furniture (why / takeaway bands) is template-required and is not a habit to avoid.

## Production

Production policy is `required: true`. Researcher, writer, editor: inherited (orchestrator) model at
xhigh effort, honoured. Writing coach: not run (pinned guide).

## Decisions during production

- Researcher finding: on Hanoi's 6 actions, plain PPO with illegal moves as no-ops reaches nearly the
  same final greedy policy as MaskablePPO (one-seed check). Decided: the lesson does not claim masking
  is needed for a better final policy here. Its comparison rests on what the record shows differs:
  steps spent on illegal moves during training, and what happens when the trained agent is evaluated
  without the mask (SB3's evaluate_policy / plain predict apply none and give no warning). The
  idea's emphasis moves to the second half: the mask is an input that must reach every call that
  chooses an action. Any claim that small action spaces let a penalty or no-op suffice must be checked
  across seeds and stated narrowly; Huang and Ontañón's 4×4 result may be cited for it.
- The environment, not the agent, still defines what an illegal move does (for check_env and for the
  unmasked baseline). The lesson says so instead of claiming no consequence is needed anywhere.
