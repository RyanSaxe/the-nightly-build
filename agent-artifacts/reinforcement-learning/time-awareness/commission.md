# Commission: reinforcement-learning/time-awareness

Run: scheduled, 2026-11-28 (nb duty, open section, no commissions supplied).
Template: lesson. Series voice guide pinned (writing-coach/01 holds it); no coach invoked.
Production policy (required): researcher, writer, editor at the orchestrator's model, effort xhigh. Recorded actual: all roles run as subagents inheriting the orchestrator model, effort xhigh.

## Where the course stands

Stages 1 and 2 are complete. Stage 3 has published observation scale, frame stacking and the Markov property, action frequency, discretization, factored actions, masking in Q-learning and in MaskablePPO, specification gaming, potential-based shaping, reward scale, held-out levels and domain randomization. Stage 3's Markov-property topic lists "time awareness", and no lesson has taught it. The lesson "Q-learning that treats its time limit as terminal learns the values of a different grid" (termination-and-truncation, 2026-11-06) states in one paragraph that if the task were to earn as much as possible within a move limit, the remaining time would belong in the observation and reaching the limit would be a termination. It did not develop that case. This lesson does.

## Topic and the one idea

Topic: time awareness, the Markov property under a time limit that is part of the task.

The one idea: when a time limit belongs to the task, the remaining time is part of the state, so it goes in the observation and reaching the limit is a termination, not a truncation.

The writer states the final main-idea sentence (at most 30 words) in draft-handoff.md and may correct this wording.

## Case to start from

Start from the course's 16-cell grid as termination-and-truncation used it (goal, pit, slip rule, four-move limit), and change one thing: the four-move limit is now a rule of the task. Choose a start cell, or extend the grid with a second, nearer, smaller reward if the original grid cannot show it, so that the best move from one cell depends on how many moves remain. The reader should see one cell where the optimal action with one move left differs from the optimal action with several left. Link termination-and-truncation for the grid and the two flags; link the lesson that introduced the grid's rules.

The writer chooses the experiments, the causes to test and the page's structure. A natural comparison is a cell-only Q-learner against one whose observation adds the remaining moves, graded against exact time-indexed values from backward induction over the remaining moves. Whether to also show Pardo et al.'s second failure (a time-unaware agent bootstrapping through the limit) or Gymnasium's TimeAwareObservation wrapper is the writer's call against the one-idea test.

## Boundaries

- Do not reteach partial-episode bootstrapping; termination-and-truncation owns it. Use it by name with a link.
- Do not reteach frame stacking or the general "an entry averages over the hidden states behind it" argument; link frame-stacking-and-the-markov-property and domain-randomization by name where the comparison helps. This lesson's new material is that time is a hidden variable the environment's own rule creates, and how the target and the flags change once it is observed.
- At most two experimental results, plus their removal tests.
- Check every Gymnasium API name against the current release (1.4.0 per termination-and-truncation; the researcher confirms).

## Neighbouring articles in this edition

The Daily Brief (2026-11-28) and one Feature run today. Neither touches RL; no overlap to manage.

## Recent patterns to break (from the last ten lessons)

- Headlines lead with an agent or method plus a surprising number ("Per-component Q-tables settle wrong only on...", "A courier paid for every move never delivers", "Q-learning values a rolling ball's cell by how often each speed reaches it"). The verb "settle" has appeared in three recent headlines/deks. Avoid it in display text.
- Deks have tended to run as one long sentence with a comma-and clause joining a second finding. Build this dek differently.
- Section headings in recent lessons often open "The ..." or with the method name, and two recent lessons have a heading of the form "Each entry/table ... averages over ...". Do not reuse that form.
- The phrase "the course's grid" recurs; name the grid concretely instead.

## Decisions after researcher/01

- Correction: the commission's "Pardo et al.'s second failure (a time-unaware agent bootstrapping through the limit)" misdescribed the paper. The time-unaware failure in Pardo et al. Section 2.2 / Fig. 1a is an agent that treats the limit as terminal without seeing time, so values from cells it cannot reach in time leak into its estimates. Bootstrapping at the limit (Section 3.1) is correct only for a task with no limit, and termination-and-truncation already taught it. If the lesson shows a failure, it is the 2.2 failure.
- Gymnasium's TimeAwareObservation appends elapsed steps, not remaining steps. Under a fixed limit the two carry the same information; the page says "elapsed" when it describes the wrapper.
- No Gymnasium 1.4.0 wrapper reports a task's own limit as terminated. The lesson's environment counts its moves and returns terminated=True itself at the limit. Whether to show the wrapper at all is the writer's call.
- Pardo's own gridworld does not need time-dependent moves, so the lesson's grid must produce its own case: the writer confirms by backward induction a cell whose optimal move differs between one move left and several left, extending the grid with a nearer, smaller reward if needed.
- Run environment: `uv run` is blocked in this sandbox by the permission layer. The orchestrator prepared an equivalent interpreter with the same pinned packages (gymnasium 1.4.0, numpy 2.4.6). Listings keep their inline script metadata and are run with that interpreter; the deviation is recorded in draft-handoff.md.
