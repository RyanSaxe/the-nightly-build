# Commission: reinforcement-learning/factored-action-spaces

Run date: 2026-11-27 (scheduled, from `nb duty`). Template: lesson. Tags: none.

## Place in the course

Stage 1 and stage 2 are complete. Stage 3 has published observation scale, frame
stacking and the Markov property, action frequency, action discretization, action
masking in Q-learning and in MaskablePPO, specification gaming, reward scale,
potential-based shaping, held-out levels, and domain randomization. The stage-3 topic
"Action spaces, including removal, discretization, factoring" still lacks factoring and
removal. This lesson teaches factoring only. Removal is a later lesson; give it at most
one sentence if the lesson needs it.

## Topic and the one idea

Topic: factored (multi-component) action spaces and factored action values.

The one idea: when an action is a tuple of components, a value written as a sum of
per-component terms, Q(s, a) ≈ Σ_d Q_d(s, a_d), lets each component be chosen by its
own argmax, which turns a joint maximization over the product of the component sizes
into a sum of small ones and cuts the number of estimates per state from Π n_d to
Σ n_d. That greedy choice is the joint optimum exactly when, at the state, the best
level of each component does not depend on the levels of the others (it suffices that
Q* is additively separable there); where the components interact, the factored
learner can choose a pair no joint learner would.

Derive in full: the separation of the argmax of a sum; the count of estimates; the
condition under which the per-component greedy choice matches the joint argmax, and a
small counterexample where it does not. Use a run to check the derivation.

## Case to start from

Build a new small Gymnasium environment whose action space is
`gymnasium.spaces.MultiDiscrete` with at least two components, where most states have
non-interacting components and a few states have a real interaction (a reward or
transition term that depends on two components together). The writer designs the
environment; it should be a new one, not the race, courier, Dock, Tower of Hanoi,
pendulum or rolling-ball cases from recent lessons. Keep it tabular so value iteration
gives the exact Q* for the joint space as a cross-check (value iteration was taught in
`finding-optimal-policies`; Q-learning in `sarsa-and-q-learning`). Link those lessons.

Learners to compare: tabular Q-learning on the flattened joint action, against a
factored Q-learner with one table per component trained on the shared TD target (the
action-branching form). Name which target the factored learner uses and why.

Report at most two experimental results. One should show the sample-efficiency gain as
the number of components grows; the other should show where the factored learner's
policy departs from the joint optimum and that it departs exactly at the interacting
states the derivation predicts. Include a removal test for any causal claim, as the
series prompt requires.

## Sources to rest on

Ask the researcher only for what the page will use. Likely: Tavakoli, Pardo and
Kormushev (2018), "Action Branching Architectures for Deep Reinforcement Learning",
for the per-component branch form and its shared target; Kanervisto, Scheller and
Hautamäki (2020), "Action Space Shaping in Deep Reinforcement Learning", for what
practitioners do with multi-discrete spaces; the current Gymnasium documentation for
`MultiDiscrete` (check it exists and behaves as written, November 2026); and Sutton and
Barto for the Q-learning update if cited.

## Boundaries

- The audience knows linear algebra, probability, and production ML; it knows only the
  RL the earlier lessons taught. Explain any RL term not yet taught.
- No deep networks; BDQ's network is a pointer, not a method to teach.
- Experiments finish in a few minutes on a laptop CPU.

## Production record

- Voice guide: pinned series guide (writing-coach/01), no coach invoked.
- Required directives: researcher, writer and editor at model inherit, effort xhigh.
  Runtime deviation: subagents run on the orchestrator's model; effort is set per agent
  as xhigh where the runtime accepts it.
- Neighbours this run: daily-brief/2026-11-27 and one feature; no overlap.
- Recent-pattern notes: `.nb-work/notes/recent-patterns.md`.

## Orchestrator decisions after research (researcher/01)

These supersede earlier text where they conflict.

- Learner: the factored learner is the sum form (as in VDN and Tang et al. 2022):
  Q(s, a) = Σ_d Q_d(s, a_d), one shared TD error
  δ = r + γ Σ_d max_{a'_d} Q_d(s', a'_d) − Σ_d Q_d(s, a_d), each table updated by α·δ.
  Its target is the ordinary Q-learning target applied to the sum, and it splits into
  per-component maxima by the lesson's derivation. Cite Tavakoli et al.'s action
  branching only as a pointer to the deep architecture, with one sentence saying its
  per-branch regression onto a mean target differs. Do not call the sum learner
  "action branching".
- Condition: additive separability of Q* at a state is sufficient, not necessary, for
  the per-component greedy choice to match the joint argmax. State it as sufficient;
  the derivation may show a non-separable case where greedy still matches (Tang et al.
  Prop. 6) if it costs a few lines, otherwise one sentence.
- Departure claim: the supported prediction is that the factored learner can depart from
  the joint optimum only where the components interact or where bias reaches through the
  bootstrapped target, and that which pair it picks there depends on how often each
  joint action was tried. Design the environment so the interaction cannot propagate
  (for example, interactions only at states whose successors are terminal or unaffected),
  check across fresh seeds, and report what the runs show. Do not write "exactly at".
- The sample-efficiency gain as components grow and the convergence of tabular factored
  Q-learning are not established by any source; the lesson's runs carry them, and the
  page says no general convergence guarantee is claimed.
- Slugs confirmed in the library: `finding-optimal-policies`, `sarsa-and-q-learning`,
  `action-discretization`, `action-masking-in-maskable-ppo` (link the last for SB3's
  per-component categorical if the lesson mentions it).

## Orchestrator decisions on the writer's queries (writer/01)

- Step size: each table takes the full step α, not α/D. Accepted; the page and handoff
  say so.
- Length: the prose (cards, body, captions, problems) must come under the template's
  2,200-word target. Keep the "stronger joint learner" comparison, because it is the
  fair qualification of the sample-efficiency result, but compress it to one or two
  sentences with its numbers; it does not count as a third result. Make the rest of the
  cut wherever the editor finds prose that does not teach the idea.
- Headline scope: the headline claims only what the averaged-choice measurement shows.
  Prefer "settle on" / "settle wrong" wording over "err", and keep the headline short;
  the page already reports last-step departures in cells 0 and 1.
- ε = 0.05 departure: report it in a sentence or two as unexplained, with no cause
  claimed, per the series prompt. No further experiment.
- Code and outputs live outside the artifact record at
  `/home/user/the-nightly-build/.nb-work/reinforcement-learning/factored-action-spaces/code/`.
