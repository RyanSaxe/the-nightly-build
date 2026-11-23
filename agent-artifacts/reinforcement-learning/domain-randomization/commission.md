# Commission: reinforcement-learning/domain-randomization

Authorized by `nb duty` for 2026-11-23: reinforcement-learning, open section, no
commissions. Template `lesson`; band 2,500–6,000 words (code and output count),
2–5 flexible sections, at least 1 source. The series pins its voice guide, which
`nb start-article` placed at `writing-coach/01/voice-guide.md`.

## Where the course stands

Stage 3 (Designing environments) is nearly done. Published stage-3 lessons:
observation scale, frame stacking and the Markov property, action frequency,
action discretization, action masking in Q-learning and in MaskablePPO,
specification gaming, potential-based shaping, reward scale, and held-out levels
(22 Nov). The held-out-levels lesson closed by saying the next lesson varies an
environment's physical parameters instead of its layout, which is called domain
randomization. This lesson keeps that promise. The stage-3 project lesson comes
after it, so this lesson is not a project and reports at most two results.

## Topic, one idea, starting case

- Topic: domain randomization, from the stage-3 bullet "held-out levels,
  procedural generation, domain randomization, and checks for memorized
  behavior". Sim-to-real is mention-only: one sentence and a pointer, under domain
  randomization.
- One idea: training on episodes whose physical parameter is drawn from a range
  produces a policy for that range, and when the observation does not reveal the
  parameter the agent cannot act optimally for each value. The best it can do is
  the best single policy for the mixture, which gives up return at any one value
  to avoid failing at others. Exposing the parameter (or history that reveals it)
  in the observation removes that cost. Connect this to what the course already
  taught: held-out levels (a held-out range of the parameter is the test), and the
  frame-stacking lesson's point that a table entry averages over the states
  behind it.
- Starting case: Dock, the cart pushed toward a dock, as rebuilt in the
  action-frequency lesson (link it for the rules). Extend it with one physical
  parameter drawn per episode, for example the cart's mass (how hard a push
  accelerates it) or rolling friction, and a rule that makes the parameter
  matter to the decision, for example a docking-speed limit beyond which docking
  fails. The writer may choose a different parameter or rule, or a different
  small environment, if Dock cannot show the idea plainly; record the reason in
  the handoff. Keep the learner tabular or otherwise already taught (Q-learning,
  value iteration); an exact solve per parameter value is available as a
  reference, as earlier lessons used.

The experiments, the causes to test and the page's structure are the writer's.

## Boundaries

- Do not teach POMDP machinery or belief states as a topic; partial observability
  with recurrent policies is stage 6. A sentence naming the issue and pointing
  forward is enough.
- Do not reach for adaptive methods (automatic domain randomization, system
  identification) beyond a mention.
- Sources: cite the paper that introduced domain randomization for RL transfer
  (Tobin et al. 2017 is the usual reference) and anything else the lesson takes;
  the researcher confirms what each paper says and which sections to point to.
- Check that every library API used (Gymnasium version, wrappers) still works as
  the lesson says, in November 2026.

## Recent-pattern notes (writer and editor)

- Nine of the last ten headlines name Q-learning or a method as the subject
  ("Q-learning that…", "Moving at random…, Q-learning…"). Lead this headline with
  the finding about the environment or the policy, not with the learner's name.
- Deks of the last four lessons are one sentence joining two results with
  ", while" or ", and" ("…matches its training return…, while a position-only
  agent…"; "…keeps every optimal route, and clipping…"). Build this dek another
  way.
- "Why this matters" openings recently start from a concrete agent on a grid
  ("A Q-learning agent trained on one seven-by-seven grid…", "Before a courier
  agent trains…"). The template fixes the bookend; vary how its first sentence
  enters.
- The last two takeaways open by restating a measured number from the body.
  Vary the takeaway's construction.
- Section headings are full-sentence claims across the course; that is the
  course's style and fine, but avoid three headings in a row of the form "The X's
  Y …".

## Roles (series production policy is required)

- writing-coach: not run; the series pins its voice guide.
- researcher: inherited model, xhigh effort.
- writer: inherited model, xhigh effort.
- editor: inherited model, xhigh effort.

## Decisions after researcher/01 (orchestrator)

- The one idea is sharpened. A policy trained over a hidden parameter's range
  loses return at a value only where the best action there depends on the
  parameter. Where one action is best at every value, the mixture policy matches
  each specialist, as EPOpt's hopper masses did. The lesson shows both: the
  docking-speed rule (or whatever rule the writer chooses) is what creates the
  cost, and removing that rule is the removal test for the claim. Where a cost
  exists, the lesson reports where in the range it falls, and does not claim
  it is uniform.
- Attribution: Tobin et al. 2017 named and defined domain randomization, for a
  supervised detector with rendering randomized. Peng et al. 2018 is the RL
  paper that draws physical parameters per episode and transfers the policy.
  CAD2RL and EPOpt came first in RL and can be credited in a sentence. Do not
  call Tobin an RL paper.
- Exposing the parameter: the lesson may show that an observation including
  the parameter recovers per-value optimal play inside the training range.
  It does not claim that history recovers it; that is a pointer forward to the
  stage-6 lesson on recurrent policies. If the lesson tests a held-out range,
  it does not generalize from Yu et al.'s result beyond what its own run shows.
- The quantitative claims rest on the lesson's exact solves and runs, which the
  literature does not supply for the tabular case.

## Decisions after writer/01 (orchestrator)

- Accepted: the drive holds every push at 1 m/s² whatever the load, so the
  load acts only at the dock's buffer (stops the cart iff ½mv² ≤ 0.5 J). This
  isolates the cost of hiding the parameter and keeps it exactly solvable.
- The removal test (`--no-limit`) is accepted as the check on the causal claim,
  even though it is near-trivial in this environment; the page says why.
- The unexplained gap between two learned estimates and their exact values
  may be stated in a sentence without a cause, as the series prompt allows.
