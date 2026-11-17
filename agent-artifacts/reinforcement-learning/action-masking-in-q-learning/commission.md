# Commission: reinforcement-learning/action-masking-in-q-learning

Authorized by `nb duty` for 2026-11-17 (open section). Template: lesson.
Bands: 2500 to 6000 words (code and output count), 2 to 5 flex sections, min 1 source. Not strict.
Production: required. Researcher, writer, editor at the orchestrator's model, effort xhigh. Voice guide pinned (no writing coach invoked).

## Where the course stands

Stage 1 and stage 2 are complete through the deadly triad. Stage 3 (designing environments) has covered observation scale (11-13), the Markov property and frame stacking (11-14), action frequency (11-15) and action discretization (11-16). Remaining in stage 3: action removal and factoring, action masking in Q-learning and in an off-the-shelf agent, time awareness, reward design, shaping, held-out levels, the project.

## Topic

Action masking in Q-learning: state-dependent removal of actions that the environment forbids. Static removal of a useless action gets at most a sentence as the special case where the mask never changes. The off-the-shelf agent (MaskablePPO in sb3-contrib) is a later lesson; mention in one sentence at most.

## The one idea

When legality depends on the state, the mask has to apply in two places in Q-learning: in action selection (greedy and exploratory) and inside the bootstrap target, where the max runs over the next state's legal actions only. Masking selection alone leaves the target maximizing over action values the agent never updates, so their initial (or extrapolated) estimates leak into every legal value upstream.

## Case to start from

A small tabular environment, new to the course, in which the set of legal actions changes from state to state and a substantial share of state-action pairs are illegal. The writer builds it; it must be Gymnasium-compatible and expose the mask through `info` (the convention MaskablePPO and Gymnasium's own environments such as Taxi use; the researcher confirms the current convention). Compare against the conventions an environment designer could choose instead: an illegal action that is a no-op with a penalty, or one that ends the episode. The writer decides the experiments; the commission fixes only that the lesson's reported results (at most two) teach the two-place rule and that any causal claim has its removal test on the page.

Link the lesson that introduced each piece reused: Q-learning (`sarsa-and-q-learning`), the Gymnasium contract (`termination-and-truncation`, `checking-a-custom-environment`), ε-greedy (`epsilon-greedy-exploration`).

## Boundaries

- Teach only RL ideas earlier lessons taught, plus masking. Function approximation is taught (semi-gradient, deadly triad), so a sentence about why the leak is worse under generalization is allowed if it is checked or plainly marked as not run here.
- Do not reuse the slippery grid, Pitch, Dock or the pendulum unless the idea needs them.
- No invented history. If a paper clearly introduced invalid-action masking in RL (Huang and Ontañón 2020 is the usual citation for policy gradients), the researcher confirms what it actually shows.

## Recent-pattern notes (11-14 to 11-16)

- Headlines: the last four all lead with the method or a measured quantity ("Q-learning values...", "Deciding ten times as often leaves Q-learning...", "The best number of torque levels..."), and three of four deks open "On <environment>, ..." or name Gymnasium's wrapper. Break both: a dek that does not start with "On".
- "Why this matters" bands in the last three open with a general statement that the designer chooses something ("How often an agent acts is a choice the environment's designer makes", "A Q-learning table needs a finite list of actions"). Open differently.
- Takeaway bands open with a one-line abstract restatement ("Discretizing a continuous action trades a ceiling against experience", "Deciding more often shrinks the differences..."). Open on the lesson's concrete result instead.
- Section-heading outline of the last three lessons: problem case → derivation/bound → baseline code → wrapper/fix → "most of the gain comes from" ablation. Do not end on another "Most of X's gain comes from Y" section.
- Recurring phrasings: "the gap", "one more estimate per cell", "called X" as a definition device after a description (used 3+ times per lesson). Use the definition device sparingly.

## Decisions log

(none yet)
- 2026-11-17 (after researcher/01): The new environment exposes the mask both as `info["action_mask"]` (int8, fresh copy each call, Gymnasium's Taxi convention) and as an `action_masks()` method (the sb3-contrib MaskablePPO interface), so the later MaskablePPO lesson reuses it unchanged. The lesson says in one sentence that conventions differ (info, method, observation dict) and does not claim one shared convention.
- 2026-11-17: If Taxi is mentioned, describe it accurately: its masked actions are executable no-ops with penalties (−1 wall, −10 bad pickup/drop-off), so its mask is advisory on top of the no-op-with-penalty convention. In Gymnasium 1.4.0 the registered ID is `Taxi-v4` (`Taxi-v3` raises DeprecatedEnv; orchestrator checked with uv run on 2026-11-17).
- 2026-11-17: The lesson's comparison is, as far as the record shows, the first measurement of masking selection without masking the target; say what the record supports (known practice in Gymnasium's tutorial, OpenSpiel, Hanabi/Dopamine, Zahavy et al.; a docstring bug fixed on main) without claiming a priority the record cannot settle. Do not copy Gymnasium 1.4.0's tutorial code (it skips updates on terminal steps).
- 2026-11-17: The leak's size depends on the illegal entries' initial values relative to the legal values (researcher's own reasoning, not a source). The writer's worst-case check varies initialization and reward sign; −∞ initialization of illegal entries is a fix to test, not assume.
- Package installs through `uv run` work in this environment (gymnasium 1.4.0 fetched and ran).
- 2026-11-17 (reader check 1, editor/02): Reader check run on the editor/01 page. Editor/02 approved after cutting or explaining all eight places and correcting leak.py's error columns to exclude the goal state's never-acted pairs. The central explanation was unchanged and no section was rewritten, so no second check is run; the corrected error figures are reproduced from the printed listing. Both W-CITE-DENSITY warnings (orientation, resting-point) accepted under the series direction. The one sentence on library mask conventions stays, per the earlier decision. The writer/01 handoff's off-page check figures (0.067, 0.017) likely carry the same goal-grading inflation; nothing on the page depends on them.
- Roles: researcher, writer and editor at xhigh effort on the orchestrator's model (claude-opus-5-5); reader check by a fresh agent at default effort; voice guide pinned.
