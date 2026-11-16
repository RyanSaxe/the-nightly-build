# Editorial review: reinforcement-learning/action-discretization (editor/01)

## Correct

Thesis, from the draft alone: on a pendulum whose torque costs something, more
torque levels raise the best return a policy over them can reach, but a fixed
budget of steps spreads Q-learning's updates over more action values, so the
best number of levels rises with the budget. The claims under it:

1. Over evenly spaced levels the best policy falls short of continuous torque
   by at most 200·C(Δ/2)² = 800C/(k − 1)² an episode, and the exact solve's
   shortfall falls about fourfold per halving of the spacing.
2. At 60,000, 200,000 and 600,000 steps Q-learning does best with 3, 5 and 9
   levels.
3. Most of the fine sets' early deficit is too few updates per action value,
   not weaker exploration.
4. Steps per level turn a budget into a prediction of which set wins.

How each held.

**Claim 1 broke in its derivation, and its conclusion survives by a different
argument.** The draft expanded the one-step action value to second order,
Q(u* + δ) ≈ Q(u*) − (C + κ)δ², and dropped κ as "small next to C = 1" because
it scales with |b|² ≈ 0.02. κ is not small. It is the cost of steering the
pushed state back later, and that steering is paid in torque, so κ grows with
C. Two checks agree: a Riccati solve of the linearized step gives κ = 0.48 at
C = 1 (0.0037 at C = 0.001), and reading Q off ceiling.py's own 65-level
solve gives (C + κ) between 1.41 and 1.58 at four states near upright, at
t = 0, 50, 100 and 150 (it falls toward 1.08 only in the last ten steps). So
"a level δ from the best torque loses about C·δ²" is about a third too small,
and the caption's "each term is at most C(Δ/2)² to leading order" for the
rounding policy is false. Rounding pays up to (C + κ)(Δ/2)² a step, so that
argument proves only a bound about 1.5 times the printed one.

The printed bound itself is right, for a policy the draft never wrote down.
A policy that alternates between the two levels either side of u*, so that its
torques average u*, follows the best path with a wobble and pays
C(u* − a)(a + Δ − u*) ≤ C(Δ/2)² a step in extra torque. Its next step undoes
the wobble, so it never pays κ. The wobble's own cost carries 0.1·0.15² ≈ 0.002
in place of C. It fits every run: every shortfall at
C = 1 sits under 800C/(k − 1)²; the two-level shortfall (791.5) is the
back-and-forth's 4 a step; the writer's off-page finding that the bound fails
only at Pendulum-v1's C = 0.001 is the wobble term, and with it added (bound
plus 200·0.00225·(Δ/2)²) the stock shortfalls of 1.55, 0.38 and 0.12 for
k = 2, 3, 5 all fit. Fig. 1's catch data shows both forms of alternation:
two levels alternate evenly, and three levels coast with a kick at −2 every 13
to 24 steps. Those ten kicks after the catch cost 40 of the 61 return units
three levels lose from the tilted start.

Fix: I replaced the expansion, the telescoping identity and the rounding
argument with the alternation derivation (same heading slot, new heading), kept
the bound and its printed column unchanged, and moved the second-order
expansion into problem 2's answer, where the action gap needs it. That answer
now says the torque term gives C·Δ² and that near the top the steering cost
adds more of the same form, which is what the solve shows.

The same section's Seyde sentence said the best action "sits at a limit". Sec.
3 of the paper (I read pp. 3 to 4) says that holds wherever p*ᵀg(s*) ≠ 0, is
undetermined on singular arcs, and that a bang-bang solution reaches a
singular arc by switching quickly ("chattering"). Holding the rod upright is
such an arc. I narrowed the sentence to the paper's condition and added the
switching, which is the page's own back-and-forth.

The ceiling section explained the bound's fourfold looseness by the rod
"resting at the top on zero torque". The catch data contradicts that for three
levels, which keep kicking. Rewritten: the best torque sits midway between
levels only during the catch.

**Claim 2 held.** Every listing reran exactly as printed (uv run, from code/):
pendulum.py, ceiling.py, learn.py, --explore-ends, --per-level, --seeds 5 6 7
8 9 and ceiling.py --cost 0.001 all reproduce runs/ byte for byte after the uv
banner. Every number on the page and in Fig. 2 matches the output (I checked
each plotted point against learn.txt and ceiling.txt, and the ringed minima).
Fig. 1's returns and torque sequences match catch.json and ceiling.txt's tilted
column. Updates-per-value arithmetic (16, 89, 178, 52) and the 111,000 and
333,000 conversions are right.

**Claim 3 held, narrowed slightly.** The removal tests are on the page with
their outputs. The writer's per-level seed check and stock-cost check were
rerun (results under Edits).

**Claim 4 held, and one unmeasured step is now measured.** The page said five
levels at 111,000 steps were "still far from done". Nothing measured that
budget. A throwaway run of learn.py's own run() put five levels at −170 (seeds
0 to 4) and −105 (seeds 5 to 9) at 111,000, against about −65 at 150,000 and
333,000. The sentence stands; the check is listed for the next reader.

**A causal claim without a removal test was cut.** "The table's cells and the
constant step size both cost return there" named two causes and tested
neither. The paragraph went (see Reads well).

Labels: headline, dek and headings carry only 3/5/9 levels at 60,000/200,000/
600,000 (learn.txt), "a thousand times dearer" (1.0 against pendulum.py line
136's 0.001), and C(Δ/2)². All match their owners.

Citations: every printed href opens on its source. The three Gymnasium blob
URLs at v1.4.0 load the files (fetched), and the line locators match the
installed 1.4.0 source (constants 102 to 108, step 126 to 147, reset 149 to
167, registration 48 to 52, DiscretizeAction 201 to 348 with centres 303 to
310). arXiv 2111.02552, 2210.12566, 1901.10500 and the NeurIPS 2004 page
return 200. `nb check --check-links` passes. data-nb-kind: all four are
primary for what they are cited for. Sources 1, 2 and 4 share one author,
Farama, and the page never offers them as independent of each other.

Course boundary: every RL term the page uses (action value, value iteration,
greedy policy, Q-learning, ε, discount and horizon, truncation, bootstrapping,
cell averaging, action gap) is taught in one of the 16 published lessons and
linked at first use. I added the missing first-use link on "action values" in
the body. Continuous-action methods appear only in the Go deeper band.

## Reads well

Went:

- "That number looked like a bug to me at first." It came from the voice
  guide's own example of a personal remark, reworded, with nothing in the
  record behind it.
- "Under Pendulum-v1's own cost the same back-and-forth would pay 0.004 a
  step, 0.8 an episode." It repeated the stock-cost figure the next section
  states where it belongs.
- The paragraph on learned returns staying above their ceilings. It named two
  untested causes and nothing in the lesson used it; the plateau fact the
  prediction paragraph needs is in the printed output.

Lifted: the derivation now carries its abstract step down to Fig. 1's two
alternations before the equation, and the takeaway restates the corrected
mechanism. "Rise from −1288 to −119" now says the first figure is at 60,000
steps. Two sentences over the proof's density limit were split.

The draft did not run flat against the guide. Its edges (first and last
sentences of each paragraph, the cards, the closing takeaway sentence) pass
the placeholder test. No opener, dek or heading repeats the recent record:
no Q-learning title, no wrapper arc, no "Here you predict" close, no "called
X" definitions.

## The experience

Rendered with nb preview and captured with Playwright at 390 and 1280 px in
light and dark. No page-level horizontal scroll. Fig. 1's trace panel grew to
about 2.3 times its drawn size at desktop width, with labels larger than the
body text; I capped it at 26rem and centred the pair, which leaves it in
proportion at both widths. Fig. 2 and Fig. 3 read correctly in both themes;
Fig. 3's near-zero torques are hard to tell apart in dark mode but the band
the text points to is clear. The new two-line equation fits a phone. Pendulum
step equation overflows a phone by 3 px with the parenthesis still visible;
left as is.

Prose on the rendered page, counted as the template defines it (cards,
captions, legends, headings and problems with answers; no equations, code,
output, drawing text, bands or sources): 2,317 words, down from 2,416. That is
still over the template's 2,200. I kept Fig. 3, the only picture of what the
agent learned, which the series asks for, and problem 2, which carries the
action-gap link to the earlier lesson. The rest of the excess is the wobble
argument a correct bound needs.

What it gives beyond its sources: a bound on how much return evenly spaced
levels cost, checked against an exact solve on a pendulum with a real torque
cost, set against Q-learning runs whose best level count moves with the budget,
with removal tests that pin the move on updates per action value. That matches
the handoff's original-work sentence except for the mechanism of the bound,
which the handoff still states the old way.

## Edits

- figures/article.src.html is the source; library/.../action-discretization.html rebuilt with build.py and re-stamped after every change.
- Section "rounding-cost" replaced by "alternation": new heading, alternation derivation, extra-cost equation (two lines), wobble paragraph, bound caption "To leading order, leaving out the wobble."
- Stock-cost sentence: torque term "at most 0.8", wobble "about as much again"; Seyde sentence narrowed to the paper's first-order condition plus switching on singular stretches.
- Ceiling section: "as C·δ² predicts" → "as the bound's (Δ/2)² predicts"; looseness explained by the catch, not by resting on zero torque.
- Orientation: added why the starts are near upright (a laptop-sized table learns the full swing-up nowhere near its ceiling), per the orchestrator's ruling; cut the duplicated stock-cost sentence.
- Learning section: cut the "looked like a bug" sentence and the ceiling-gap paragraph.
- Per-level paragraph: "from −1288 at 60,000 steps to −119".
- "action values" in the body now links finding-optimal-policies at first use.
- Problem 1 answer: framed as alternating between −1 and 1.
- Problem 2 answer: derives the gap from the zero slope at u*, torque term C·Δ² plus a steering cost of the same form; ends on the gap.
- Takeaway: mechanism sentence rewritten to the alternation.
- figures/fig_catch.py and fig_catch.svg: trace panel max-width 26rem, row centred.
- Reruns and checks, all in the scratchpad, none on the page: every listing (identical output); kappa from Riccati and from ceiling.py's solve; five levels at 111,000/150,000/333,000 on seeds 0 to 9; the writer's perlevel_seeds.py, stock_learn.py and ceiling_541.py (results below).

Writer checks rerun, all identical to checks/: perlevel_seeds.py (ten-seed medians put nine levels at −59 against five's −66, and seventeen at −80, so "nine match five" and "seventeen stay behind" hold); stock_learn.py (two levels best at 60,000 and 200,000 steps, three at 600,000, as the per-level rule predicts when the ceiling side is nearly empty); ceiling_541.py (k = 3 and 5 stable, k = 9 and 17 move by about 0.6, the grid error the page cites).

Proof: `nb check ... --check-links` BLOCK: 0, WARN: 2 (W-CITE-DENSITY on ceiling and learning, both made of the lesson's own solve and runs, which the series exempts). Stamp: 4,639 words, 20 min, 4 sources.

## Decision

approve. The argument stands; the broken derivation step and the overreaching sentences are fixed on the page, and nothing left needs a different argument.

## Questions for the orchestrator

1. Length is 2,317 against about 2,200. The next whole piece to cut is problem 2 (about 120 words, and the action-frequency link goes with it, so a shorter second problem would replace it) or Fig. 3 (about 70 words, and the series' only picture of what the agent learned). I kept both. Rule on it if you want the page under 2,200.
2. The derivation section is rewritten, so the reader check should see the new text. The handoff's original-work sentence ("a level δ from the best torque costs about C·δ² a step") is out of date; use the review's wording in any PR description.
