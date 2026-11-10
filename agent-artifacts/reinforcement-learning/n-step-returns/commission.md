# Commission: reinforcement-learning/n-step-returns

Series: reinforcement-learning (Courses). Template: lesson. Mode: open.
Run date: 2026-11-10. Authorized by `nb duty` for 2026-11-10.

## Topic

Stage 2, "N-step returns". The course has taught Monte Carlo and TD(0)
prediction, action values and generalized policy iteration, ε-greedy
exploration, SARSA and Q-learning, and (on 2026-11-09) ordinary and weighted
importance sampling. Stage 2 still owes n-step returns, then function
approximation with semi-gradient updates, then the deadly triad. This lesson is
n-step returns and nothing after them.

## The one idea

n-step TD prediction: the target sums n real rewards and then bootstraps from
the estimate n moves later, so n = 1 is TD(0) and an n at least the episode
length is Monte Carlo, and an intermediate n can learn faster than either end.

The writer owns the 30-word main-idea sentence in `draft-handoff.md` and may
sharpen this one.

## Case to start from

A random walk on a chain of states, of the kind Sutton and Barto use in Section
7.1 (19 non-terminal states, terminal rewards of −1 on the left and +1 on the
right, undiscounted, exact values known in closed form). It is a new
environment for the course, chosen because its states lie on a line, so the
distance a reward's information travels per episode is something a figure can
show directly. The writer builds it as a small Python file and links nothing
for its rules, since no earlier lesson introduced it.

The earlier lesson "An agent can learn what each state is worth without knowing
the rules" (`learning-values-from-samples`) showed in its Fig. 2 that TD(0)
carries the goal's reward back about one cell per pass while Monte Carlo carries
it the whole way. That observation is the natural question this lesson answers.
Link that lesson where the observation is used; do not redescribe it.

The writer may instead start the body from one short episode on the chain,
updated by hand with n = 1, n = 3 and n = ∞, before generalizing.

## Boundaries

- Prediction only for the main idea. n-step SARSA may get one sentence and a
  pointer; it does not get a section. Off-policy n-step with importance sampling
  is a later lesson: at most one sentence that names it, linking the 2026-11-09
  importance-sampling lesson.
- λ-returns, TD(λ) and eligibility traces are "Mention only" (backward-view
  traces) or belong to stage 5 (GAE through the λ-return). At most a pointer.
- At most two experimental results. The obvious candidates: error against step
  size for several n (the shape of Sutton and Barto's Figure 7.2, reproduced
  with the lesson's own code, not copied) and one picture of how far
  information travels per episode for different n. The writer chooses.
- Any causal claim (for example "intermediate n wins because it propagates
  further without the full return's variance") needs a removal test on the page
  per the series prompt, or it is cut.
- The derivation that deserves full treatment is the n-step error-reduction
  property (Sutton and Barto eq. 7.3) or the recursive form of the n-step
  return; the writer picks what the main idea needs. A side result gets no
  derivation.
- The n-step update has a delay: an estimate for time t can update only at time
  t + n. Code must handle the episode's tail (the τ bookkeeping). Teach it with
  the code, plainly.

## Sources

`min_sources: 1`. Sutton and Barto, Reinforcement Learning: An Introduction,
2nd ed., Chapter 7 (Sections 7.1, and optionally 7.2) is the main source.
Watkins (1989) is commonly credited with n-step returns ("corrected n-step
truncated return"); cite only what the researcher confirms. Sutton and Barto's
Section 7.1 also discusses why intermediate n wins; cite that passage if the
lesson relies on it.

## Production

- Voice guide pinned by the series (`writing-coach/01/voice-guide.md`), no
  writing-coach run.
- Policy `required: true`: researcher, writer and editor run at the inherited
  orchestrator model, effort xhigh. Writing coach not run.
- Lesson reader check required after the editor's first review.

## Neighbours in this edition

daily-brief/2026-11-10 (news, word of the day) and one feature. No overlap.

## Recent-pattern notes (from the last three lessons)

- Headlines have run as a claim about one method on a named environment, often
  with a clause of conditions: "Moving at random half the time, Q-learning still
  learns the optimal arrows"; "PPO's greedy arrows outscore the sampled moves
  its training curve averages"; "Importance sampling values a policy from
  episodes another policy played". "Arrows" appears in two of three. Avoid
  "arrows", and avoid a headline that opens with a participial clause.
- Deks have used the shape "X does A, but on <env> B unless C" with a precise
  threshold. Build a different dek.
- Section headings recently put a numerical finding into the heading ("At
  ε = 0.5 the two methods part at cell 9", "The grid's logs center the ordinary
  estimate on 1.36 until coverage fails"). Use at most one heading with a
  number in it.
- Phrases recurring across recent lessons: "the slippery grid", "the
  hand-drawn arrows", "the course's grid", "exact solve", "in the terms of the
  … lesson". This lesson uses a new environment, so none of them should be
  needed.
- Background bands have grown to six rows. Keep this one to the lessons the
  page actually uses.

## Decisions after research (researcher/01)

- Correction: Sutton and Barto's Section 7.1 states that an intermediate n
  performs best on the 19-state walk and does not give a mechanism. No opened
  source gives one. Any explanation of why intermediate n wins is the lesson's
  own claim and stands only with an on-page removal test (series prompt), or
  it is cut.
- Scope of the headline claim: "intermediate n learns faster" holds when each n
  is compared at its own best step size, on the 19-state walk, over the first
  10 episodes. At a fixed large α, or later in training, or on a 5-state walk,
  n = 1 can win (researcher's throwaway runs; Singh and Dayan 1998 for λ). The
  page states the claim within that scope and says in a sentence that the best
  n depends on α, the chain and how long training runs. It does not claim
  intermediate n "ends up more accurate".
- Eq. 7.3's error-reduction bound gives no reduction guarantee for n ≤ 9 from
  the centre state on an undiscounted walk (researcher's derivation in the
  record). If the lesson presents 7.3, it says what the bound guarantees
  (convergence) and does not use it to explain the n = 4 win. The writer may
  prefer the recursive form of the n-step return as the derivation instead.
- Setup to reproduce for Figure 7.2's shape: Sutton's own code as recorded
  (start in the centre, v(i) = i/10 − 1 for the 19-state walk with states
  1..19 per the record's convention, log α grid, RMS over states averaged over
  the first 10 episodes and 100 runs, same walks for every n and α). The
  lesson's numbers come from the lesson's own run, not read off the book's
  figure.
- Do not cite Kearns and Singh (2000); it was not opened.

## Decisions during drafting (writer/01 queries)

- incompleteideas.net: https fails certificate verification from this sandbox
  and could not be confirmed for readers. Every published lesson cites the
  host over http (e.g. http://incompleteideas.net/book/RLbook2020.pdf), so
  decided: use the http address consistently for every incompleteideas.net
  source, the Lisp code included, with no certificate note. If the proof
  rejects http for a source, tell me rather than work around it.
- The `--size 5` and `--episodes 100 --first 91` runs count as checks of result
  2's scope, not a third result. They may stay on the page as flags backing the
  one scope sentence, provided the prose reports no further finding from them.
- Amended after the editor's query: the proof requires an https href in the
  Sources list (B-SOURCES-FORM). The Lisp source's Sources entry keeps the
  https href, and its note names the http address readers can open, with no
  mention of certificates. Inline and band links stay http.

## Reader check

- Reader check 1 ran on the page after editor/01 (fresh agent; page text,
  figure images, the one linked earlier lesson, press reader background). Its
  report is copied verbatim in editor/02/review-brief.md.
- editor/02 answered every place and approved. Its changes correct one stated
  reason, reframe what the `--expected` run shows, and trim or define terms;
  they neither change the central explanation nor rewrite a whole section, so
  no second reader check runs (decided by the orchestrator).
