# Editorial review: reinforcement-learning/reward-scale (editor/01)

## Correct

Thesis, from the draft alone: multiplying every reward by k > 0 multiplies
every value by k and keeps the optimal policy, while clipping and adding a
constant can change it. Clipping can because it changes the ratios between
rewards. A constant can in an episodic task because it adds
c(1 − γ^N)/(1 − γ), which depends on how long each policy's episodes last.

The claims under it, and how each held:

1. Scale. The derivation is complete and correct, including k < 0 and k = 0.
   courier.py prints the cents row at 100 times the dollar row, the same greedy
   move in every cell, and a largest |q*(cents) − 100 q*(dollars)| of 1e-13.
   Ng, Harada and Russell's footnote 3, as the record quotes it, supports the
   paraphrase. Held.
2. Clipping. The far route is −5.30 + 0.735 = −4.56 against −0.05 for the near
   route. I recounted the clipped map: 16 of 26 cells deliver near. I checked
   the rule "every cell fewer moves from the near drop-off than from the far
   one" cell by cell. A tie is impossible because the two distances always sum
   to an odd number. Held.
3. Added constant. The geometric sum, the continuing case and the episodic case
   are correct. I recomputed the fuel-free gains (1.95 and 6.03) and cell 14's
   choice (2 against 0.95⁷ × 11 = 7.68). I also recomputed the hourly values,
   20 against 14.12 from the depot. Every non-delivering move ties at 20, so the
   hourly panel is right to have no arrows. The constant-potential paragraph
   matches the shaping lesson's G′ = G − Φ(S₀) + γᴺΦ(S_N). Held.
4. Q-learning learns each version's q*. I copied both listings out of the built
   page into an empty scratch folder and ran `uv run courier.py` (0.4 s) and
   `uv run learn.py` (39 s). Both outputs are byte-identical to the printed
   output. With unused seeds 100–109, every row gives 10 of 10 on delivery and
   on optimal moves, with largest error 0.000. I reran gaps.py: the closest
   calls are cells 14, 21 and 22 under dollars, a gap of about 0.05, and every
   run gets them right. I reran problems.py: Problem 1 gives 0.6086 and 0.18
   with near under the sign. Problem 2 gives q = q_dollars + 40 to 1.4e-14.
   Held.
5. A normalizer is a positive scale while its divisor holds still. I opened the
   Stable-Baselines3 2.9.2 rendered source. It shows clip_reward=10.0,
   returns = returns·gamma + reward, and normalize_reward clipping
   reward/sqrt(var + eps) to ±10 with no mean subtracted. Held.

Figures 1 to 3 match the printed maps arrow for arrow. The outlines are right:
13 changed cells in Fig. 2 and 3 in Fig. 3.

Headline, dek and subheads: the 7 by 4 grid, the depot, both fees, both route
lengths, "five more moves", "multiplies every value by 100" and "clipped at 1"
all check against courier.py.

Baselines issue #538. This session has no GitHub API access to the repository,
so I read the page twice through a fetch tool. In unixpickle's comment of 29
August 2018 he writes that subtracting the mean "would change the dynamics of
the environment". He follows with the all-1 against all-0 example, in which the
agent wants to live or doesn't care if it lives or dies. He is one of the
issue's two assignees. The draft gave his example faithfully, with three
faults. It called his comment "the reply" in a thread that has nine comments. It
did not name him. It left out the reason he gave. Fixed: the page now names
him and his role, gives the reason, and marks the live-or-die line as his
example.

Every href, opened as printed:

- Break. Source 5 pointed at the Vectorized Environments guide, which never
  mentions ClipRewardEnv, so that citation landed on a page without the claim.
  I split it into two entries. The new source 5 is the v2.9.2 Atari wrappers
  page, which documents ClipRewardEnv as "Clip the reward to {+1, 0, -1} by
  its sign". The new source 6 is the v2.9.2 rendered vec_normalize source,
  which is the record's own reading route. The old sources 6 and 7 are now 7
  and 8.
- Unverified. The MIT Press page for Sutton and Barto returns 403 to curl and
  to the fetch tool. I could not open it in a browser. I tried the authors'
  PDF in its place, but the proof blocks an http href (B-SOURCES-FORM), and
  the https copy fails certificate verification, as the deadly-triad lesson's
  source note also records. I kept MIT Press, which nine published lessons use
  for this book. The Background row still links PDF p. 83.
- Every other href loads. The Nature page loads, with Methods behind the
  paywall as its note says. `nb check --check-links` passes.

data-nb-kind: Engstrom and colleagues is secondary, because it describes
OpenAI Baselines' PPO from outside OpenAI. Every other source is primary for
what it is cited for. The two Stable-Baselines3 entries are one owner's
documentation, and the page claims no independence between them.

## Reads well

What went or changed, and why:

- "The rows are each other's removal tests." The phrase comes from the series
  prompt's checklist, and the course never taught it. I replaced it with the
  fact behind it: which pairs of rows differ in which single number.
- "The reply ... gives the reason the mean stays". This was vague attribution,
  and "stays" could mean two things. Rewritten as above.
- "Scale reaches a learner through a number ..." An abstraction was acting, so
  I recast the sentence with the learner as its subject.
- The opening card's last sentence promised only that the reader could say
  whether a wrapper "can move the courier's route". That is narrower than what
  the lesson teaches. It now says "can change the optimal policy of the
  environment it wraps". "Given a constant" became "shifted by a constant".
- "In a continuing task ... every episode runs forever". A continuing task has
  no episodes, so it now reads "N is infinite under every policy".
- The constant-potential sentence carried a dangling "with the drop-offs
  included where". I split it into two sentences.
- The induction for Q-learning from 0 needs both runs to draw the same random
  numbers. "And use the same seed" now says so.
- Problem 1's "0.01 per move" left open whether the delivery move is charged,
  and the answer assumes it is not. It now reads "every other move", which
  matches the setup.
- The Fig. 1 caption repeated the figure's own legend, so I cut that sentence.
- Go deeper 01's "Section 4 watches" became "reports". Background 03 now ends
  "before the courier delivers", since the limit cuts every undelivered
  episode, not only the hourly courier's.
- The takeaway's tenses mixed past and present for the same kind of claim. I
  made them consistent.

Against the recent record: the headline is short, has no number and avoids
"leaves ... alone". The dek joins two clauses with "and", not "so". The opening
card starts on this lesson's courier. The headings are built differently from
each other and from the last two lessons. The Go deeper lines vary in what they
say each source is for.

I found no clause borrowed from the voice guide's exemplars and none taken from
commission.md. The register is plain and a little drier than the guide
describes. The steps are announced before they are taken, so I left the
register alone.

## The experience

One structural change. The Q-learning section held the run, the paragraph on
scale for a learner, the normalizer paragraph and the problems, all under a
heading about Q-learning matching value iteration. A reader skimming the
headings could not find the normalizer conclusion, which the opening card
promises. I split the section. "Q-learning finds each version's routes from
rewards alone" keeps the run and its reading. "Only a nonzero start lets
Q-learning tell cents from dollars" takes the starting-estimate paragraph, the
normalizers and the problems. The normalizer paragraph now ties its missing mean
to the lesson's own shift result. The split left the run section with no
citation, which is the proof's one warning (W-CITE-DENSITY). The series prompt
says a section made of a run needs no action.

I looked at every figure at 1200 px and 390 px, in light and dark. No page
scrolls sideways, labels and arrows sit inside their cells, and the legends
fit.

Prose words on the rendered page, counted without equations, code, output,
drawing text, reading bands and sources: 2,158 words containing letters, or
2,328 tokens if each number counts as a word. The headings add 60. My edits
added about 65 words net. The page sits at the template's line of about 2,200.

What the page gives beyond its sources: Sutton and Barto pose the shift as two
unanswered exercises, and Ng, Harada and Russell state the scaling result in a
footnote. The page derives both and builds a courier on which an exact solver
shows clipping and a shift moving the optimal route while a factor of 100
cannot. Q-learning then learns each version. The page also reads library code
to say when a normalizer is only a positive scale. The writer's original-work
sentence says the same apart from the normalizer, so it stands.

Headline, reread last: "A courier paid for every move never delivers" is true
of the page's courier, paid +1 a move with fees of 3 and 12 at γ = 0.95, which
earns 20 by staying out against 14.12 for delivering. The body and the dek give
those bounds. Kept.

## Edits

- Opening card: "given a constant" became "shifted by a constant".
- Opening card, last sentence: "move the courier's route" became "change the
  optimal policy of the environment it wraps".
- Background 03: "an episode in which the courier never delivers" became
  "before the courier delivers".
- Fig. 1 caption: cut "Blue cells deliver far and amber cells near."
- Added constant: "every episode runs forever" became "N is infinite under
  every policy".
- Added constant: split the constant-potential sentence in two.
- Q-learning: the removal-tests sentence became two sentences naming which rows
  differ and in what.
- New section `nonzero-start`, "Only a nonzero start lets Q-learning tell cents
  from dollars", split out of the Q-learning section.
- Starting-estimate paragraph: new opening sentence, the same-seed condition,
  and the learner as the subject.
- Normalizer paragraph: added that subtracting a mean is an added constant; the
  issue #538 sentences rewritten with attribution, the reason, and his example.
- Problem 1: "per move" became "for every other move".
- Takeaway: "made ... sent" became "makes ... sends".
- Go deeper 01: "watches" became "reports".
- Sources: split Stable-Baselines3 into s5 (Atari wrappers page, ClipRewardEnv)
  and s6 (rendered vec_normalize.py source). Renumbered Engstrom to s7 and the
  issue to s8, and updated the inline citations and locators.
- Made the edits in work/article.src.html, rebuilt the article with
  assemble.py, and ran `nb stamp`. The listings and their output are unchanged.

## Decision

approve: every claim checks against the record, the reruns and the opened
sources, and the fixes above are made on the page with no required change left.
Final proof: BLOCK 0, WARN 1 (W-CITE-DENSITY on the run section, which needs no
action).
