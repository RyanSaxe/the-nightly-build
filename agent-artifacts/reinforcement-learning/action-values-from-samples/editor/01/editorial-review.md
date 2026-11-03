# Editorial review: reinforcement-learning/action-values-from-samples (editor/01)

## Correct

Thesis, from the draft alone: an agent that averages the return after each (cell, move) pair
can improve its policy without the slip probabilities, because the greedy step over action
values reads none, and Monte Carlo ES, which improves after every episode, reached the grid's
optimal policy in its runs although no published proof covers this grid.

1. The greedy step over q_π needs no model, and the q-form chain makes the greedy policy no
   worse. Held. The derivation is complete, and the S&B quote (p. 97, eq. 5.1) and the chain
   (p. 98) match the authors' PDF.
2. Without exploring starts, moves the policy does not take get no returns, so the greedy step
   cannot leave the starting policy. Held. It holds by construction in `greedy`, and
   `explore=False` gave 0 of 20 again in my rerun. One break: the S&B quote "cannot be relied
   upon in general..." is on printed p. 96, not p. 97 (checked in RLbook2020.pdf, PDF p. 118).
   I fixed that locator, and narrowed the exploring-starts definition's locator from pp. 96-97
   to p. 96, where the words are.
3. Evaluation does not have to finish before improvement, but the averages have to carry over.
   Held, with two breaks in the wording. "By 100,000 episodes it has the same 18 runs" stated an
   equality that only these seeds show. On seeds 100-119 (`check_seeds.py`, rerun) the kept
   5,600 schedule ends at 16 and improving after every episode ends at 20. "Waiting ... does not
   help" also contradicted Fig. 3, where the kept 5,600 line leads 15 to 12 at 20,000. I rewrote
   the paragraph to say only what holds on both seed sets: it starts later, catches up by
   20,000, and from 50,000 on is never ahead. The removal test for "clearing is what costs" is
   the kept schedule, which differs only in `forget`, and it stands.
4. Only the optimal policy can be a resting point, and on this grid convergence is unproved.
   Held. I read S&B p. 99 past the quote, Tsitsiklis p. 60 and Prop. 5, Wang et al. p. 2,
   Algorithm 2 and the conclusion, and Delattre and Fournier's abstract and p. 2. The "only half
   the way is done" sentence goes on to say they can treat only γ < 1/2, so the page uses it
   fairly. I recomputed q* from lesson 2's code: cell 2 has a single optimal move, right, and its
   up-slip leaves the agent in cell 2, so the grid is not OPFF. Following the orchestrator's
   decision, I cut the Delattre and Fournier bullet back to "first-visit Monte Carlo control on
   any finite problem with a discount below 1/2", which is how their abstract states the result.
   "Each with its own conditions on step sizes and long episodes" claimed both conditions for
   all three results, and Wang et al. use sample averages with no step-size condition, so I
   changed "and" to "or".

Numbers. I copied `gridworld.py` (lesson 1), `control.py` (lesson 2) and `estimators.py`
(lesson 3) verbatim from the linked lessons' HTML, and `mc_control.py` and `experiment.py` from
this page, then ran them with `uv run` in a scratch folder. `experiment.py` printed output
byte-identical to the page's (2 min 28 s). `control.py` reproduces lesson 2's printed output
exactly, and `mc_control.py` imports and runs clean. I checked every number in the prose,
table, problems and answers against that output, and all match: 0.32 / −1.08, the four cell-14
values, the episode returns, 56 pairs, 84 of 2,000,000 cut, half at 10,000, 18 at 100,000, the
0.35 gap at cell 5, run 0's wrong cells, the −0.29 / 0.06 at cell 10, 5 and 2 for the cleared
schedule, and the problem 1 answer (−1.7803). `figures.py`, rerun on that output, regenerated
all eight figure SVGs on the page byte for byte, before I changed Fig. 1's wording and Fig. 2's
aria-label. Fig. 3's plotted points match the printed table.

The dek and takeaway gave "18 of 20" as the result. The page seeds give 18 of 20, twenty unused
seeds give 20 of 20, and the writer's independent 100-seed reimplementation gave 96 of 100 (from
the handoff; no script for it was supplied, so I did not rerun it). The count does not repeat,
and 18 of 20 reads as a 90% rate that the other runs beat. Both lines now say "nearly every
run". The body keeps the printed 18 of 20, since the output and Fig. 3 show it, and adds one
sentence: the other seeds repeat the half at 10,000 and do better at 100,000.

Citations. I opened every href as printed. The JMLR page and both arXiv abstracts land on the
cited papers, and the incompleteideas.net PDFs in the bands return 200. The s1 href
(mitpress.mit.edu) returns 403 "Access Denied" from Akamai to a non-browser client, and I could
not open it in a browser from here. I tried pointing s1 at the authors' PDF, which is the URL in
the evidence record. Its https form fails with a self-signed certificate, and the proof blocks
a source href that is not https (`B-SOURCES-FORM`). I reverted to the MIT Press URL. See the
open question below.

Kinds. All four sources are `primary`, and each is the author of the result it is cited for:
S&B for their algorithm, definitions and open-question statement, and Tsitsiklis, Wang et al.
and Delattre and Fournier for their own theorems. The page does not claim an independent second
source anywhere.

## Reads well

What went or changed, and why:

- "Exploring starts is an assumption about the environment, and often an unavailable one."
  This came from the commission's instruction ("stated as an assumption ... that it is often
  unavailable"), and the S&B quote after it says the same thing. I rewrote it to say what the
  assumption asks of an environment and that `play` takes the start pair as an argument.
- "...the runs in Fig. 3 are evidence about it, not a guarantee." This closer took the
  commission's "an observation across seeds, never a guarantee" and recast it as an antithesis.
  I rewrote it in the article's terms: the runs show what happened on the seeds tried, and no
  theorem says every run must end at the optimal policy.
- The heading "State values cannot rank the moves at cell 14" is contradicted by its own first
  paragraph, where policy iteration ranks them from state values using the model. It now
  begins "Without the slip rule".
- "q_π is an average of returns" now reads "an agent can estimate q_π by averaging returns",
  because q_π is an expectation.
- "As the left half of Fig. 1 shows" was wrong at phone width, where the panels stack. It now
  says "the first panel".
- "`mc_control.py` is the whole agent" is wrong because the file also holds `step`, the
  environment. It now reads "the complete method".
- "Unlimited episodes" became "infinitely many episodes", which is S&B's condition.
- "Makes the policy greedy in every cell" did not match the S&B box (greedy at the states
  visited) that the Go deeper band tells readers to compare line by line. It now adds "which can
  change only the cells the episode visited", which is true of both.
- "One cell left of the corner" now names the bottom-right corner.
- I linked "action value" at its first body use to the lesson that taught it.

No sentence failed the placeholder test outright. The edges of each paragraph, section and card
carry the article's own nouns. The register matches the guide: short sentences, the purpose
stated before each step, and no borrowed exemplar clauses. Against the recent record, the dek
does not open on the grid, Why this matters opens on the problem instead of a recap, the last
section is not a "cannot yet" pointer, and the headings vary in construction. The dek's "where"
clause holds on its merits. It carries the second fact, that no theorem applies, in seven words,
and it is not one of the dek patterns the standard bans.

## The experience

I captured the page with `nb preview` and Playwright at 390 px and 1280 px in light and dark,
before and after the edits. There is no page-level horizontal scroll, and no label overlaps or
arrow stops short. Fig. 3 drew the kept 5,600 line under the cleared one through 10,000
episodes, because the two schedules play identical episodes until their second improvement.
The caption now says the two lines coincide there, so a reader does not hunt for the missing
line. Fig. 1's right panel said "average return" over exact q_π values. It now says "expected
return", and the aria-label matches. Fig. 2's 10,000-episode aria-label said "cells 10".

Prose count on the rendered page: 2,206 words. That covers the cards, body, captions, table,
problems and answers. It leaves out headings, equations, code, output, SVG text, the reading
bands and sources. Why this matters runs 135 words and the takeaway 113. The count is at the
2,200 line, and the two sentences I added (the other seeds, the Fig. 3 overlap) account for the
rise from about 2,150. I cut no idea for it.

What the piece gives beyond its sources: on a grid the reader has already solved exactly, it
shows the model dropping out of the greedy step, runs Monte Carlo ES built from the course's own
estimator to the known answer across seeds, separates "do not wait" from "do not clear the
averages" with a removal test, and checks each published proof's conditions against this grid,
none of which it meets. The handoff's original-work sentence says the same. The headline,
"Action values let an agent improve its policy from episodes alone", is supported. Exploring
starts constrain which episodes the agent gets, but it still learns from episodes alone.

## Edits

- Dek (header and nb-meta): "in 18 of 20 runs" → "in nearly every run".
- Orientation heading → "Without the slip rule, state values cannot rank the moves at cell 14".
- Orientation ¶1: "one cell left of the corner" → "...of the bottom-right corner"; "the left half of Fig. 1" → "the first panel of Fig. 1".
- Fig. 1 right panel text and aria-label: "average return" → "expected return".
- Orientation: linked "action value" to finding-optimal-policies.
- Greedy section: "q_π is an average of returns" → "an agent can estimate q_π by averaging returns".
- Exploring starts ¶2: locator "Section 5.2, pp. 96-97" → "Section 5.2, p. 96".
- Exploring starts ¶3: rewrote the first sentence (what the environment must allow, and `play` takes the start pair); "the assumption" as the subject of the quote; locator p. 97 → p. 96.
- Every-episode ¶1: "unlimited episodes" → "infinitely many episodes".
- Every-episode ¶2: "greedy in every cell" → "greedy, which can change only the cells the episode visited".
- Every-episode ¶3: "is the whole agent" → "is the complete method".
- Every-episode, results ¶: added "Twenty other seeds repeat the half at 10,000 and do better at 100,000."
- Fig. 2 aria-label: "wrong at cells 10" → "wrong at cell 10".
- Fig. 3 caption: added "The two 5,600 lines coincide through 10,000 episodes, before the second improvement."
- Carried-averages ¶2: replaced "does not help ... the same 18 runs" with "gains nothing by the end ... catches up by 20,000 episodes, and from 50,000 on has no more runs at the optimal policy than improving after every episode".
- What-is-proved ¶2: "each with its own conditions on step sizes and long episodes" → "each with conditions of its own on step sizes or on long episodes".
- Delattre and Fournier bullet: "first-visit updates in a general form that allows random start pairs and greedy steps" → "first-visit Monte Carlo control" (the orchestrator's decision).
- Body closer: replaced "the runs in Fig. 3 are evidence about it, not a guarantee" with "The runs show what Monte Carlo ES did on the seeds tried, and no theorem says that every run must end at the optimal policy."
- Takeaway: "in 18 of 20 runs within 100,000 episodes" → "within 100,000 episodes in nearly every run".
- Ran `nb stamp` (words 4,115, 18 min, 4 sources). Proof: BLOCK 0, WARN 0, PUBLISHABLE.

Open question for the orchestrator: does https://mitpress.mit.edu/9780262039246/reinforcement-learning/
load in a browser? It returns 403 to scripted clients here. Working assumption: Akamai is
blocking bots, and readers land on the book page. If it fails in a browser too, s1 needs an
https URL that a reader can open. The authors' PDF is http-only, because its https form has a
self-signed certificate.

## Decision

approve. The argument holds, and every break I found was a locator, an overstated precision or
a wording that I could fix from the record and the reruns.
