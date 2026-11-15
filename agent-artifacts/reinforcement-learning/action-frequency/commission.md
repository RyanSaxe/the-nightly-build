# Commission: reinforcement-learning/action-frequency

Series: reinforcement-learning (open course, template `lesson`). Date: 15 November 2026.
Authorized by: `nb duty` for 2026-11-15, open section.
Voice guide: pinned by the series (`writing-coach/01/voice-guide.md`); no writing coach invoked.

## Where the course stands

Stage 2 is complete through the deadly triad (12 Nov). Stage 3 has two lessons:
observation-scale (13 Nov) and frame-stacking-and-the-markov-property (14 Nov). The next stage 3
topic is action spaces: removal, discretization, factoring, and action frequency. That topic holds
several ideas and becomes several lessons. This lesson takes action frequency only. Removal,
discretization and factoring are later lessons; do not teach them here beyond a pointer.

## The one idea

How often the agent chooses an action is an environment design choice. When a continuous-time
system is controlled at a step of length dt, the difference between the values of two actions in
the same state shrinks in proportion to dt, while the noise in a sampled Q-learning target does not
shrink with it. At a fine step, Q-learning cannot tell its actions apart and learns slowly or not at
all; the horizon in steps also grows as 1/dt, so the discount per step must change to keep the same
horizon in seconds. Repeating each chosen action for k steps (action repeat, frame skip) restores an
action gap of order k·dt and shortens the horizon in decisions, at the cost of coarser control.

Derive the main result in full: for a deterministic system with dynamics ds/dt = f(s,a) and reward
rate r(s,a), with γ = e^{-dt/τ} for a fixed time horizon τ, Q(s,a) − V(s) = O(dt). Then check it
with a run. The derivation follows Tallec, Blier and Ollivier, "Making Deep Q-learning Methods
Robust to Time Discretization" (ICML 2019), which the researcher sources; reproduce its argument,
not its deep-learning experiments.

## Case to start from

A small one-dimensional continuous-time task the writer builds, for example a point mass or cart
pushed left or right toward a goal region, integrated at step dt and discretized into a table of
cells so tabular Q-learning from the earlier lessons applies directly. The writer chooses the
environment details, but it must let dt vary over at least a factor of 10 with the same physics,
and the discount per step must be set from one horizon in seconds. Link the Q-learning lesson
(sarsa-and-q-learning) and, if the observation is position plus speed, the frame-stacking lesson.

## Experiments

Outside a project lesson, at most two results. They should show (1) the measured action gap
shrinking with dt as derived, and (2) Q-learning at a fine dt with and without action repeat, in
the same physics and the same total simulated time. The removal test for any causal claim goes on
the page as a flag. The writer designs the experiments; every result is checked against new seeds,
other cells, and the case the explanation fits worst, as the series prompt requires.

## Sources to request from the researcher

Only what the page uses: Tallec, Blier and Ollivier (2019), with the section holding the
Q − V = O(dt) argument; the DQN paper's frame-skip of 4 (Mnih et al. 2015, Methods) as the classic
practice; Gymnasium's current handling of frame skip in its Atari wrappers or environments, checked
against current documentation (November 2026); and one source on action repeat as a tuned design
choice (for example Braylan et al. 2015, or the dynamic frame-skip work of Lakshminarayanan et al.
2017) if one is clear. Sutton and Barto as needed.

## Boundaries

- 2,500 to 6,000 words including code and output; 2 to 5 flex sections.
- Code as `uv run` Python scripts with inline metadata, runnable on a laptop CPU in minutes.
- Do not explain PPO or DQN's algorithm; DQN may be named for its frame-skip setting only.
- Do not cover semi-MDPs or options beyond one sentence and a pointer.

## Recent patterns to break

- Deks recently open "On <environment>, ..." (12 Nov "On Baird's...", 9 Nov "On Sutton and Barto's
  one-state loop", 1 Nov "On lesson 1's slippery grid", 31 Oct "On a slippery 4×4 grid") and "Over
  the first 10 episodes". Do not open the dek that way.
- Headlines recently follow "<method/thing> <verb>s <object> ..." with "keeps X from" (13 Nov).
  Do not use "keeps ... from".
- Why-this-matters boxes recently end by naming a later algorithm ("DQN, later in the course,
  combines ...", "DQN ... takes its four most recent frames"). Do not end this one that way.
- Takeaways recently open by restating the lesson's equation in one sentence ("For a linear estimate
  learned with one step size α, ...", "Linear semi-gradient TD's expected update is ..."). Open this
  takeaway differently.

## Production record

Researcher, writer, editor: model inherit (orchestrator's model), effort xhigh, as required.

## Decisions recorded during production (after the evidence record)

- Correction to "the one idea": the commission's claim that sampled-target noise "does not shrink
  with dt" is withdrawn. State what the sources support: the action gap shrinks in proportion to dt
  (Tallec et al., PMLR §3.2, Theorem 2), and the error in the learned estimate does not shrink with
  it. Any claim about how the noise scales in the lesson's own environment must come from the
  lesson's own derivation or run, not be attributed to a source.
- Action repeat has more than one effect: a larger action gap, persistent exploration (Tallec
  Theorem 4; εz-greedy of Dabney et al.), and a shorter horizon in decisions (Kalyanakrishnan et
  al.). The lesson may credit run 2's improvement to a cause only after removal tests that separate
  them, for example repeating only the random actions, and changing γ per decision without
  repeating. Put the removal test that supports the claim on the page as a flag. If the tests show
  a different cause dominates in this environment, the lesson says so.
- The O(dt) result assumes a smooth value function; at a jump (next to the goal boundary) the gap
  stays finite. Use those cells as the case the explanation fits worst.
- DQN: cite its frame skip of 4 only with its stated reason (computation, Nature Methods), and do
  not attribute the action-gap argument to DQN. Keep "action repeat 4" distinct from "agent history
  length 4" (the frame stack in the previous lesson).
- Gymnasium: use `RepeatAction` (Gymnasium 1.3.0+) for the repeat, per the evidence record.

## Decisions recorded after writer round 01

- Worst-fit case: the value jump at the roll-off edge in Dock stands in for "next to the goal
  boundary"; the speed-limited dock goes to a problem. Accepted.
- Step size: no added flag or output block. The page states α = 0.3 and makes no claim that
  Q-learning at dt = 0.01 cannot learn at all; any wording of "stalls" or "fails" stays tied to the
  stated step size and simulated time.
- Length: the `--tau 0.1` removal test stays. The editor may cut prose elsewhere.
- Crash cost −2: accepted, with the reason given on the page or in the handoff as the writer chose.

- Environment name: keep "Dock" and dock.py, presented as a rebuilt variant of the 13 Nov lesson's Dock with a link, as the editor wrote it. Simulated-time wording "the same budget of 2,000 s" accepted.
