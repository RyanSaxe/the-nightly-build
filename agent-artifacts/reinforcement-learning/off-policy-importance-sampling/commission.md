# Commission: reinforcement-learning/off-policy-importance-sampling

Series: reinforcement-learning (open course, template `lesson`, not strict, 2,500–6,000 words
including code and output, 2–5 flex sections, at least 1 source). Voice guide pinned by the owner
(`writing-coach/01/voice-guide.md`); no writing-coach run.

## Where the course stands

Published, in order: environments-and-the-rl-problem, finding-optimal-policies,
learning-values-from-samples, action-values-from-samples, epsilon-greedy-exploration,
sarsa-and-q-learning, termination-and-truncation, checking-a-custom-environment,
training-an-off-the-shelf-agent. Stage 1 is complete. Stage 2 has taught MC and TD prediction,
action values and GPI, ε-greedy, SARSA and Q-learning. The SARSA lesson defined target policy,
behavior policy, on-policy and off-policy, and showed Q-learning is off-policy.

## Topic and the one idea

Topic: stage 2, "On-policy and off-policy learning, with importance sampling".

The one idea: to estimate a target policy's value from episodes another policy played, weight each
return by the product of per-step probability ratios π(a|s)/b(a|s) along the episode. The plain
average of weighted returns (ordinary importance sampling) is unbiased, and the ratio-weighted
average (weighted importance sampling) is biased but has bounded variance; with long episodes or a
target far from the behavior, the ordinary estimator's variance can be infinite.

Derive the unbiasedness of ordinary IS in full (the expectation of the ratio-weighted return under b
equals v_π), state coverage (b(a|s) > 0 wherever π(a|s) > 0) and why it is needed, and use a run to
check the derivation. One sentence and a pointer may say why one-step Q-learning needs no ratio
(its target conditions on the action taken, and the max is the target policy's own expectation).

## Case to start from

Start on a small environment where the target policy's value is known exactly, so each estimator can
be graded against the truth. The writer may use the course's SlipperyGrid with exact_value from
baselines.py (link the lesson that introduced it), or a new small environment. For the failure case,
use a classic case built to show where ordinary IS fails, such as Sutton and Barto's one-state
Example 5.5 (infinite variance). The prompt allows choosing either environment for its idea; do not
keep SlipperyGrid only because the last lessons used it.

At most two experimental results. Experiments, causes to test and page structure are the writer's.
Off-policy MC control, per-decision IS, discounting-aware IS, and n-step methods are out of scope for
this lesson (n-step is a later lesson); mention only as needed.

## Boundaries

- Rely only on RL ideas the nine published lessons taught; teach everything else here.
- Every listing runs with `uv run file.py`; print every file a listing needs; experiments finish in
  minutes on a laptop CPU.
- The page's charts of its own runs are inline SVG, checked against printed output.
- End with an nb-note of two or three problems, answers in `details`.

## Neighbours in this edition

Daily brief and a feature on 2026 redistricting ballot measures. No overlap.

## Production record (series production.required = true)

Researcher: model inherit, effort xhigh. Writer: model inherit, effort xhigh.
Editor: model inherit, effort xhigh. Writing coach: not run (voice guide pinned by owner).

## Decisions after research (orchestrator, researcher/01)

- The one idea, corrected: first-visit ordinary importance sampling is unbiased (every-visit is not);
  weighted importance sampling is biased, with bias falling to zero as returns accumulate, and its
  variance is bounded when returns are. Ordinary IS's variance is finite whenever episode length is
  bounded, however large; it is infinite only when episodes can run without limit and the expected
  squared ratio per step, times the chance of continuing, is at least 1 (Example 5.5: 2 × 0.9 = 1.8).
- Do not say the ordinary estimate never converges: it converges with probability 1 when returns
  are bounded (Precup, Sutton and Dasgupta 2001), only very slowly and with infinite variance.
- Do not name an introducer of importance sampling for off-policy RL; cite Sutton and Barto for the
  estimators and Precup, Sutton and Singh (2000) as a Go-deeper reading.
- The researcher's grid thresholds (infinite variance from ε ≈ 0.681) are its own computation: use
  them only if the lesson's code reproduces them.
- Notation: do not reuse b for anything but the behavior policy, and do not use ρ for spectral
  radius in this lesson; ρ is the importance-sampling ratio, as in Sutton and Barto.
- The researcher's reading of the listings of earlier course files is within scope.
- (writer/01 query) No https URL is available for Precup, Sutton and Dasgupta (2001). Decided: it stays a
  Go-deeper row; the convergence claim rests on the page's own strong-law argument.

## Recent-pattern notes supplied to writer and editor


- Every lesson since lesson 1 has used the same 4×4 SlipperyGrid with a pit and goal, discussed by
  cell number ("cell 9", "cell 13", "cell 14"). Fine to reuse where the idea needs it; do not lean
  on cell-number narration as the lesson's spine by habit.
- Recurring phrases to avoid as headline/dek/closer material: "the optimal arrows" (headlines of
  lessons 6, 9 and many takeaways), "the hand-drawn policy", "the course's grid / the course grid",
  "settles for", "one term".
- Headlines: a full-sentence claim, often "<method> <verb> ... the optimal arrows" or a
  counterintuitive contrast. Deks often open with a prepositional result clause ("Of five ...",
  "On lesson 1's slippery grid, ...", "With a target that stops only at ..."). Do not open the dek
  with a prepositional phrase today.
- Takeaways: restate the mechanism, then end on a specific number from the run (e.g. "loses 1.08 per
  start at ε = 0.1"). Vary the close: end on the conclusion, not by habit on a figure.
- Background bands list every prior lesson with a colon gloss; keep to the lessons this one uses.
- Openers ("Why this matters") open by recalling the previous lesson's method, then "You will ...".
  Vary the second half.
