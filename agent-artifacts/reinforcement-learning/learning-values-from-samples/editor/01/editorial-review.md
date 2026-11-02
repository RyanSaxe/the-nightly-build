# Editorial review: reinforcement-learning/learning-values-from-samples (editor/01)

## Correct

Thesis, from the draft alone: with the grid's slip rates and rewards hidden, a
fixed policy's value function can still be recovered from sampled episodes, and
the two ways of doing it carry their error in different places. Claims under it:
(1) Monte Carlo estimates a cell's value by averaging observed returns;
first-visit MC is unbiased and high-variance, every-visit is biased at finite
sample size. (2) TD(0) replaces the unknown return with one reward plus the
bootstrapped value of the next cell, so it learns online and is biased while the
estimates are forming, at lower variance. (3) On lesson 1's grid both converge to
v_pi, and which is faster is not settled. (4) Prediction scores a fixed policy
and cannot rank the moves not taken, which is why this is not yet control. I
could state all four from the piece.

I reconstructed lesson 1's `gridworld.py` from its published listing, wrote
`samples.py` from the inline listing, and ran `uv run samples.py` (49 s). The
output matches the pasted output block line for line: exact v_pi(13) = -2.0055,
the full RMS table, the v(13) trajectories, the seed-0 grids, and the
constant-alpha floor (every-visit MC 1.423, TD 0.825). The estimators read only
each step's reward and next cell; `first_visit_mc` and `every_visit_mc` never
touch the next cell's model, `td0` reads only reward and next cell, and none of
the three reads P, R, `transitions` or the policy. The exact linear solve lives
only in `exact_values`, which scores, exactly as the prose promises. Hand-checks:
the seed-2 episode return G from cell 13 is 0.63 (six -1 at falling weights plus
0.9^6*10), matching Fig. 1 and lesson 1; a first TD(0) update of cell 13 from
zero gives -1; the nb-note bootstrap target -1 + 0.9(-1.03) = -1.93 is right and
sits 0.08 from the exact -2.01. v_pi(13) = -2.01 is carried from lesson 1 and
cited to it, not re-derived.

One break. The runs paragraph claimed "TD's error is lower at every checkpoint but
the last" and that first-visit MC "only at 6,000 episodes" slips under TD. The run
and the chart it cites both show first-visit MC lower at 4,000 (0.307 vs 0.324)
and 6,000 (0.252 vs 0.287): the crossover is between the 2,000 and 4,000
checkpoints, which Fig. 2's own alt text ("cross near 4,000 episodes") states
correctly. I narrowed the prose to "lower at every checkpoint out to 2,000
episodes" and "somewhere past 2,000 episodes the unbiased average slips under TD,
ending at 0.25 against 0.29 by 6,000," and corrected the same wording in
`chart-1.py`'s docstring (the plotted series were already right, so the PNG did
not change).

Query decisions all hold. Bias/variance is earned from the runs, not asserted:
the piece says plainly that no one has proved either method converges faster and
that the ordering here turns on the step sizes (s1 p.124, s3 p.29). "Unbiased" is
scoped to first-visit; every-visit is labelled biased at finite n and cited to
Singh & Sutton. The curves fall because MC uses 1/N(s) and TD a decaying
N(s)^-0.7 step, and the constant-0.05 floor is shown honestly. TD-Gammon is
framed as a value function learned by TD from self-play, named a combined
prediction/control task in the body and not this lesson's tabular TD(0), with
Tesauro's own counts (200,000 games to about Neurogammon; v2.1 a one-point loss
to Robertie), not the S&B 300,000 figure.

Headline, dek and subheads check against the documents that own them: cell 13 at
-2.01 (lesson 1), the hidden-model setup, and subheads that each name a step of
this lesson's argument. All four citation hrefs open to the right document page:
the two DOIs the brief named resolve to the Springer articles (BF00114726 returns
200; BF00115009 returns 429, a rate-limit on the correct article URL), the ACM
and MIT Press pages return 403 Cloudflare/bot gates on the correct pages. These
are gating, not dead links, as the researcher recorded, and each data-nb-note
honestly points to the freely readable author PDF the researcher actually read.
Every `data-nb-kind` is `primary` and each source is the document that made the
claim it is cited for, so no secondary is dressed as an independent author.

## Reads well

Three cuts. "and the contrast stops being a slogan" went: it passed the
placeholder test ("the X stops being a slogan") and only decorated the plain
instruction to run both estimators. "the strongest program of the day" went: it
is a characterization of Neurogammon that none of the inputs establishes, and the
sentence carries its weight with "a strong intermediate level" alone. The
crossover sentence above was narrowed to what the run supports, which is a
correctness fix, not polish.

What I checked and kept: the antithesis "It did not score a fixed player; it
chose each move by the very values it was learning" stays because the
misconception it corrects (that TD-Gammon was fixed-policy prediction) is real
and is the point of the honest framing. "Three properties fix where Monte Carlo
is useful" is a true enumeration the commission asks for, not a rhetorical
tricolon. The bookends address the reader as the template allows and each
sentence belongs to this lesson. The edges read clean after the cuts; the last
sentence, "closing it without the model is the work ahead," points forward on the
lesson's own finding and names its own nouns.

Recent-record enforcement against lessons 1 and 2. The opener does not touch
AlphaGo/AlphaZero (both prior openers did); it opens on the model-gone framing and
TD-Gammon. The dek is built on a new frame: it names cell 13 and -2.01, which the
commission permits, but drops the banned "X does Y to cell 13 from A to B, while
Z" mold for "both reach -2.01 by routes that trade variance against bias." The
body closes on the prediction-to-control gap, not "the next lesson." The takeaway
closes on this lesson's own finding (a value function cannot rank the moves not
taken), not a reflective "remember the pair" line. The headings are this lesson's
argument steps and do not echo L2's "A max in place of the average" or "Evaluate,
improve, repeat until the arrows stop."

## The experience

The rendered page earns its visuals. Fig. 1 contrasts the two backups on one real
episode: MC backs cell 13 up the whole 0.63 return, TD up one step to -1 + 0.9
V(9), with the rest marked unused. Arrows reach their nodes and no labels overlap.
Fig. 2 (the learning curves) shows TD starting lower and tighter and first-visit
MC crossing under near 4,000, which is what the corrected prose now says. Fig. 3
(the value heatmap at 100, 1,000 and 6,000 episodes beside the exact grid) shows
cell 13 reading -9.9 early and settling to -2.1, so the reader sees what was
learned and not only that error fell. Every number the three problems need is on
the page, and each answer is correct.

What the lesson gives beyond its sources: it puts first-visit MC and TD(0) on
lesson 1's known grid with the model hidden and reads, from 40-seed runs against
the exact v_pi, where each estimator's error comes from, turning the textbook's
"which is faster is open" into a concrete, checkable bias-variance picture on one
cell. That matches the writer's original-work sentence in draft-handoff.md.

## Edits

- Narrowed the runs paragraph: "lower at every checkpoint but the last" to "out to
  2,000 episodes," and "only at 6,000 episodes does the unbiased average slip
  under TD" to "somewhere past 2,000 episodes the unbiased average slips under TD,
  ending at 0.25 against 0.29 by 6,000." (Correctness: the run and chart show the
  crossover between 2,000 and 4,000.)
- Corrected the same characterization in `chart-1.py`'s docstring; plotted series
  unchanged, so the PNG was not re-rendered.
- Cut "and the contrast stops being a slogan" (said nothing; placeholder test).
- Cut "the strongest program of the day" (a Neurogammon claim no input supports).
- Ran `nb stamp` (words 4045) and the full proof.

## Decision

approve. The code is correct and reproduces the page's numbers, the one factual
break (the MC/TD crossover) is fixed, every query decision and recent-pattern
break holds, and the sources resolve honestly. The proof is BLOCK: 0, WARN: 1
(W-LENGTH-HIGH, 4045 words). I accept the length warning: about 1,085 of those
words are the required full `samples.py` listing and its run output, and the rest
is required teaching across three visuals, two annotated equations and three
problems, in line with lesson 2's 3,974 at the same warning. Cutting to the band
would mean dropping the code or a derivation, which the brief forbids and the
teaching needs.
