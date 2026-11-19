# Editorial review: reinforcement-learning/specification-gaming (editor/01)

## Correct

Thesis, from the draft alone: value iteration and Q-learning maximize the
return of the reward as written, so a checkpoint that pays on every crossing
makes an endless loop the race's optimal policy at most discounts, and a
learner that adopts the loop is working correctly.

Claims under it, and how each held:

1. At γ = 0.99 the exact optimum loops from every cell past the checkpoint,
   and at 0.9 it finishes. Held. I pulled the three listings and their printed
   outputs out of the page HTML into a fresh folder and ran each with
   `uv run`: all three outputs match the page byte for byte (race.py under
   1 s, window.py under 1 s, learn.py about 4 s). Fig. 1's fourteen values and
   arrows match race.py's output, and `figs.py` regenerates both SVGs
   identical to the page.
2. From cell 2, finishing beats looping only while
   (F/r)γ^(D−2)(1 − γ²) > 1, which for this race is 0.514 < γ < 0.937. Held.
   I rederived v_loop = γr/(1 − γ²) (first payment on move 2, then every
   second move) and v_finish = γ⁴F, and checked that a deterministic
   stationary policy from cell 2 can only loop, finish, or cycle unpaid in
   cells 2 to 6, so the two-way comparison is complete. The peak at
   γ² = 3/5 is 1.86; with a checkpoint worth 2 it is 0.93. window.py: 99 of
   99 discounts agree, and bisection on value iteration's verdict gives
   0.5142 and 0.9373. Fig. 2's two curves sit within 0.05 SVG units of the
   formula at all 201 points, and the band edges, the 0.9 point (1.385) and
   the 0.99 point (0.193) match.
   The lower edge was stated but not explained ("counts only the next few
   rewards"). The explanation is that at a small discount most of the loop's
   value is its first crossing, which arrives three moves before the finish,
   and γ⁴ shrinks the finish far more than γ shrinks that crossing. The
   repeats still matter near the edge: at γ = 0.5 the first crossing alone
   (0.5) loses to the finish (0.625), while the whole loop (0.667) wins.
   Timing alone decides it only below 0.464. `check_runs.py`'s γ = 0.5 row
   agrees: value iteration goes back at cell 2 with a gap of 0.0417
   (0.667 − 0.625), and every run loops. I rewrote the passage around the
   γ = 0.5 comparison and kept it from claiming that timing alone decides.
3. Q-learning reaches the same loop, with the largest possible return and no
   finishes, and paying once removes it. Held. `checks/check_runs.py` and
   `checks/check_problems.py` reproduce their saved outputs exactly. Seeds 5
   to 14 give the same conclusions. γ = 0.5, 0.93 and 0.95 land where the
   window says. Limits of 10, 20 and 1000 give the same moves, and both
   problem answers check out (switch between 0.974 and 0.976; 47 crossings,
   finish on move 99).

Breaks, and the fix for each:

- "On the race they hold," after Turner's point about the convergence
  theorems. The course taught Watkins and Dayan's conditions in
  sarsa-and-q-learning, including step sizes whose squares have a finite sum.
  learn.py's constant 0.1 does not meet that. The run converges anyway
  because the race is deterministic, which the page already argues, but the
  sentence claimed more than the setting gives. I narrowed it to the
  condition Turner names: "On the race every move keeps being tried in every
  cell." The narrowing matches what the record supports, and no thin
  reporting sits behind it.
- "Ng, Harada and Russell derive a progress reward that cannot create a
  positive-reward cycle." What they prove is policy invariance (Section 1,
  p. 279, read on the rendered PDF page; Section 3). With γ < 1 a
  potential-based term can sum to a positive amount around a cycle, so the
  stated property is not their result. Now "leaves the optimal policy
  unchanged".
- "OpenAI added the boat-racing game CoastRunners to an internal benchmark in
  2016." The year is the post's date, taken from DeepMind's citation. The
  post does not say when the game went in. Now "OpenAI's 2016 post describes
  adding ...".
- "At γ = 0.9, the discount the course has used so far." The deadly-triad
  lesson used 0.99, the random-walk lessons used no discount, and action
  frequency set the discount per step, though most lessons did use 0.9. Now
  "the discount most earlier lessons used". Later, "The course's discount of
  0.9" became "A discount of 0.9", which also drops a phrase the last two
  lessons both carry.
- "At both discounts, every run ... end within 0.001 of q*." The third row is
  also at 0.99 and prints 0.116. Now "In the first two rows". I added one
  sentence locating the 0.116, from a new throwaway check
  (`code/checks/check_error_state.py`, output beside it): in four of five
  once-row runs the largest error is the back move in cell 0 after the
  payment, and the 0.116 run is one of them. That state can only be reached
  by backing past the checkpoint.
- "the case that the first lesson met when it found that ...": it refers to a
  lesson by number and retells it. Now the idea with its link: only a policy
  that never ends needs a discount, which matches
  environments-and-the-rl-problem.
- Background row 05 said the chess example is "quoted below". The page
  paraphrases the chess example and quotes the what/how sentence. Corrected.

Citations. I opened every href as printed. The deepmind.google, turntrout.com,
gwern.net, ai.stanford.edu, arxiv.org and docs.google.com addresses return 200
and land on the source. I reread past each quoted passage. DeepMind's
paragraphs 1, 4 to 5, 6 and 8 say what the page attributes to them. Turner's
section paragraphs 2 to 5 hold the convergence argument. His note at the top,
dated July 2026, rolls back his confidence that reward won't become the
trained agent's target but keeps "not definitionally the optimization target".
That is all "need not pursue its reward" claims, so the sentence is fair to
his current view. Randløv and Alstrøm's p. 468 and Popov's p. 7 match the
page. The OpenAI post still answers 403, also with a browser user agent, so
its byline order and date rest on the orchestrator's decision. The page
describes the post and quotes none of it.
https://incompleteideas.net fails TLS verification from this sandbox with a
self-signed certificate, and http returns the PDF. PDF pages 75, 76 and 491
are book pp. 53, 54 and 469, as the anchors say. I moved the two reading-band
links to http, which is how published lessons link the book in their bands.
I kept source 6 on https, because the proof blocks a non-https source
(B-SOURCES-FORM, which I triggered and reverted) and published lessons'
source entries use https too. One click in a real browser would settle
whether readers see a certificate warning there.

data-nb-kind. All seven are primary, and each is cited for what its authors did
or claimed. DeepMind is cited for its own definition, its causal view and its
inference about the boat, which the page attributes ("DeepMind's account
says"). Ng et al. are cited for their own term and derivation and not for the
bicycle, whose facts come from Randløv and Alstrøm. No source is presented as
independent of another it depends on.

Headline, dek and headings: the 1, 10 and eight cells match the code, and 0.94
rounds window.py's 0.9373.

## Reads well

What went:

- The Why this matters close, "On an eight-cell race you can work out from
  two geometric sums ...", is the "On a ... you will ... derive" mold the
  recent-pattern notes flag. Rewritten with the two sums as the subject.
- "Read the condition at the two ends of the discount's range." It announced
  the next sentences and said nothing itself. Deleted.
- "as a Q-learner that explored too little might keep the first route to the
  finish it found": a scenario nobody ran, attached to a cited claim. The two
  sentences after it make the point without it. Deleted.
- Problem 2's last sentence repeated the one before it. Deleted.
- "Paying only for the finish leaves the race's agent nothing to learn from
  before its first finish" restated the opening's motivation at length.
  Shortened to "brings back the problem the checkpoint was added to solve."
- "race.py holds the race and its solve" folded into the next sentence.

I found no phrasing lifted from commission.md, the briefs, or the passages the
voice guide quotes. The opener ("looks like a safe reward for a race") and the
mapping of targets to checkpoint are the article's own. The register is the
guide's: the purpose of each step comes before the step, with one step per
sentence. The lower edge was the one place running thinner than the guide, a
result stated without the number that shows it. It now carries a worked
comparison set up like the 0.99 one above it.

Headline. At 16 words it is one word longer than the series' longest recent
headlines and runs four lines at 390 px. It puts subject, verb and the
surprise, a payment of 1 beating one of 10, ahead of the condition. Its
numbers are the finding, and it has no colon, question or triad. It leaves
out the lower edge, but every word of it is true. Kept. The dek is one lean
sentence with a stance and no run numbers, unlike the last three. The four
headings take four different shapes, none is the "X never/still/only" form,
and the headings alone give the argument in order.

Also: "metres" made "meters" to match the page's American spelling, and
"Randløv and Alstrøm's simulated bicycle found a loop" now names the agent
that found it.

## The experience

I checked 390 and 1280 px in light and dark through nb preview and
Playwright. Nothing overflows the page horizontally. Both SVGs are legible,
with no label collisions and arrows that reach their cells. The blue and red
arrows follow --chart-2 and --chart-4 in both themes, as the caption says.
span.nb-math-in raises nothing in the proof. All six spans typeset with
KaTeX, with no katex-error, and nb.css lets them wrap on a phone. nb.js
typesets the class and 8 of 20 published lessons use it. It is missing only
from the furniture catalog, which is an engine documentation gap and not a
fault in this page.

Fig. 2 now pays off on both sides. A reader sees the curve under 1 left of
0.514 and right of 0.937, and the prose explains both.

Prose on the rendered page comes to 2,189 words. That counts both cards,
captions, the math legend, the problems and answers, and the details
summaries. It leaves out the title, dek, code, printed output, equations,
SVG text, reading bands and sources. The draft had 2,185. The deletions above
pay for the lower-edge explanation, the 0.116 sentence and the Turner
narrowing, so the lesson stays under the 2,200 ceiling. Stamp: 4,375 words,
19 minutes, 7 sources.

The paragraph before race.py is housekeeping, but it is short and the reader
needs it to run the code. The weight is in the derivation and the two grades,
and the piece ends on the takeaway.

What the lesson gives beyond its sources: none of the published cases computes
an optimum. The lesson derives the exact discounts at which finishing beats a
repeatable checkpoint, confirms them with value iteration, and shows that
0.99 lies outside them, so the looping policy is the optimum and not a
learning failure. That matches the original-work sentence in the handoff.

## Edits

- Why this matters, last sentence: now "Two geometric sums, the loop's and the finish's, let you find the discounts at which an eight-cell race's loop is optimal, before any agent trains."
- Background row 05: "with the chess example quoted below" to "with the chess example and the sentence quoted below"; link from https to http.
- Orientation: "the discount the course has used so far" to "the discount most earlier lessons used".
- Orientation: "race.py holds the race and its solve. Its function rule takes" to "In race.py, the function rule takes".
- Fig. 1 aria-label, in the page and in code/figs.py: "values rise from" to "values run from"; figs.html regenerated, SVGs identical to the page.
- Discount window: deleted "Read the condition at the two ends of the discount's range."
- Discount window: "An agent with a small discount counts only the next few rewards, and the loop's first crossing comes three moves before the finish." replaced by ", so the loop wins there too. The loop's first crossing comes three moves before the finish, and a small discount shrinks the later reward far more. At γ = 0.5 the loop is worth 0.5/(1 − 0.25) = 0.67, three quarters of it from the first crossing, and the finish only 10 × 0.5⁴ = 0.625."
- Discount window: "The course's discount of 0.9" to "A discount of 0.9".
- Discount window: "Neither value contains" to "Neither the loop's value nor the finish's contains".
- Discount window, last sentence: now "With γ = 1 the loop's value is infinite. The loop never ends, and only a policy that never ends needs a discount", with the link on "needs a discount".
- Q-learning: "At both discounts" to "In the first two rows".
- Q-learning: deleted "as a Q-learner that explored too little might keep the first route to the finish it found".
- Q-learning, Turner: "since the conditions of the convergence theorems fail for general agents. On the race they hold." to "since general agents fail the convergence theorems' conditions, such as trying every action. On the race every move keeps being tried in every cell."
- Q-learning, removal test: added "The third row's largest error, 0.116, is in cell 0 after the payment, reached only by backing past the checkpoint."
- Published cycles: "OpenAI added the boat-racing game CoastRunners to an internal benchmark in 2016" to "OpenAI's 2016 post describes adding the boat-racing game CoastRunners to an internal benchmark".
- Published cycles: "Randløv and Alstrøm's simulated bicycle found" to "Randløv and Alstrøm's agent, riding a simulated bicycle, found"; "metres" to "meters".
- Published cycles: "leaves the race's agent nothing to learn from before its first finish, the problem the checkpoint was added to solve" to "brings back the problem the checkpoint was added to solve".
- Published cycles: "a progress reward that cannot create a positive-reward cycle" to "a progress reward that leaves the optimal policy unchanged".
- Problem 2 answer: deleted "It finishes, but it spends almost the whole limit doing so."
- Problem 1 answer: re-indented a stray closing tag.
- Go deeper row 06: link from https to http.
- Added code/checks/check_error_state.py and check_error_state.out.txt.
- Reran nb stamp: words 4375, reading_minutes 19, sources 7.

Proof after the last edit: BLOCK 0, WARN 1, PUBLISHABLE. The warning is
W-CITE-DENSITY on discount-window, a derivation plus the lesson's own runs,
which the series direction exempts.

## Decision

approve: the argument, numbers, figures and code hold, and every fault I found
was one I could fix from the record and the reruns, so the writer has no
required change left. The reader check is next.
