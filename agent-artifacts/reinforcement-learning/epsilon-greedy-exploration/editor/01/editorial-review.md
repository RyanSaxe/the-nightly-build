# Editorial review: reinforcement-learning/epsilon-greedy-exploration (editor/01)

## Correct

Thesis, from the draft alone: with ordinary starts a greedy policy collects no returns for the
moves it skips, so Monte Carlo control can never switch to them. An ε-greedy policy samples every
move. With exact action values its improvement step never makes an ε-soft policy worse and can rest
only at the best ε-soft policy. On the course grid that policy loses value at every ε, and from
ε = 0.33 its arrow at cell 9 is not optimal.

The claims under it, and how each held:

1. The stall comes from absent returns, not wrong ones. Run 0 has 14 of 56 pairs with returns, and
   cell 14 shows [976 0 0 0]. `greedy()` in `mc_control.py` treats a move with no returns as -inf,
   so the policy cannot change. Held: the printed output, the printed `mc_control.py`, and Sutton and
   Barto p. 96, where I reread the passage in the PDF. The quote "will not improve with experience"
   is exact.
2. ε = 0.1 ends the stall. The page gives 6 of 20 runs optimal at 10,000 episodes and 19 at 200,000,
   and 0 with ε set to 0. Held. I reran the writer's seed check on seeds 20-39 and got 4, 17 and 19
   at 10,000, 100,000 and 200,000. With ε = 0.5 I got 14 at 10,000 and 20 at 75,000 and 100,000. The
   page's conclusions repeat on both seed sets.
3. Under exact action values the ε-greedy step never makes an ε-soft policy worse, and it can rest
   only at the best ε-soft policy. Held against Sutton and Barto pp. 101-103: eq. (5.2), the
   construction that moves the policy's randomness into the environment, uniqueness of ṽ*, and "does
   assume that they are computed exactly" (exact). The writer flagged the step "every ε-soft policy is
   (1 − ε)μ + ε/|A| for some μ" as their own explanation. I checked it: μ = w(a) is a probability
   distribution exactly when π gives every move at least ε/|A|. The draft stated the last step of the
   argument in words only ("move the random part outside the max... the result is the equation
   above"). That step is the lesson's main idea, so I put it on the page as two displays.
4. The price. Losses of 0.10, 1.08, 2.23, 3.46 and 6.09; cell 9 changes from ε = 0.33; the runs at
   ε = 0.5 settle on the cell-9 arrows. Held against the output. I also swept ε from 0.01 to 1.00. Only
   cell 9 differs from the optimal moves between 0.33 and 0.79. Cell 12 joins at 0.80, and cells 8
   and 13 at 0.87. So "from ε = 0.33 its arrows are no longer optimal" holds at every ε above 0.33 on
   that grid. The values in Fig. 3 and the prose (0.06, −0.71, −7.08, −6.64) match the printed rows.

Figures recomputed by hand. q*(14, right) = −1 + 0.9(0.8 × 2.16 + 0.1 × 0.06 + 0.1 × 0.61) = 0.62,
which prints as 0.61 from unrounded values. Problem 1's 0.115 comes out the same both ways. 0.925
and 0.025 are correct, and 42 = 56 − 14. Loss divided by ε runs from 10.4 to 12.2, which supports
"almost in proportion".

Breaks, and the fix for each:

- The opening card said the fix "keeps a small probability ε on every move". The floor is
  ε/|A(s)|, as the page's own equation and Sutton and Barto p. 100 give it. Rewrote it as "at least
  ε divided by the number of moves".
- Problem 2's answer said "Every return still follows a move by the ε-greedy policy." That is false
  for the opening pair, whose move the exploring start chose. Rewrote it: after the first move the
  agent follows the ε-greedy policy, so each return samples that policy's action value for its pair.
- "a little more than the −1 that one move costs" compared a loss of 1.08 with −1. Now "about the
  size of one move's reward of −1".
- "Each greedy step therefore improves the ε-greedy policy" assumed the result the next section
  proves. Rewrote it to say what the step does, and that the policy improvement theorem was so far
  stated for a policy that makes one move per cell.
- "−0.37 in the exact panel" pointed at a "best ε-soft policy" the body had not defined yet. Now it
  says what −0.37 is: the exact action value under the ε-greedy policy around the optimal arrows. The
  resting-point section then identifies Fig. 2's second panel as q̃.
- "A run's averages estimate the same quantity" said more than the runs show, since it holds only for
  a run at those arrows. Narrowed it to run 0's averages. This edit matches the claim to the record.
  It does not cover for thin reporting.
- "soft_control.py changes only how an episode is played" was wrong because the file also holds
  `best_soft`. Replaced it.

Citations. I opened every href. The Sutton and Barto PDF links #page=51, 123 and 154 land on printed
pp. 29, 101 and 132, checked by text extraction (PDF page = printed + 22). The Singh et al. PDF
returns 200, with Figure 1 on p. 288, GLIE on pp. 291-292 and Theorem 1 on p. 294. The DOI resolves
to the Springer article. Source 1's href, the MIT Press book page, returned 403 "Access Denied" to
curl, WebFetch and headless Chromium from this sandbox. I could not confirm that a reader's browser
lands there. A web search confirms ISBN 9780262039246 is the second edition. The proof does not
block on a 403, and lesson 4 uses the same href. The orchestrator may want to open it from an
ordinary browser.

`data-nb-kind`: both sources are marked primary, and both are right. Sutton and Barto make the
definitions and the proof the page cites. Singh et al. define GLIE and prove Theorem 1.

Code. I extracted every listing exactly as printed on lessons 1-4 and this page into an empty folder.
`uv run exploration.py` printed output byte-identical to the page's in 3m39s. The writer's
`figures.py`, run on the same folder, regenerates Figs. 1-3 byte-identical to the SVG on the page. I
changed no code.

## Reads well

What went, and why:

- "each greedy step returns the policy it was given" came from the recent record. Lesson 4 says
  "each greedy step returns the policy it started from" about the same stall. I replaced it with this
  run's result: after 10,000 greedy steps the policy is still the hand-drawn one.
- "The runs here show only what it did on the seeds tried" came from the recent record too. Lesson 4
  closes its convergence section with "what Monte Carlo ES did on the seeds tried". I merged the point
  into the sentence before it.
- "The policy can arrange it instead" ended the opening section on less than the paragraph knew. Now
  it names what arranges it: a policy that sometimes moves at random.
- "Control with this policy is on-policy" named the term before saying what it means. I reordered it
  so the term ends the sentence that defines it.
- "On this grid ε = 0.1 takes ordinary starts to the optimal arrows" made a parameter the actor. The
  runs are now the subject.
- "The last lesson's `play`" referred to an earlier lesson by position. It now names the function and
  its file.
- In "…tried infinitely often, which Singh and colleagues call GLIE" the "which" had no clear
  antecedent. I split the sentence and spelled out the acronym.
- Go deeper row 4 said "a learner". It now names SARSA, the method, as the page does elsewhere.
- The takeaway gave five results one per sentence, the shape the brief records for lesson 4's
  takeaway. I recast it as four sentences, each following from the one before. Its last sentence no
  longer opens with "On this grid", which also opens the body's last paragraph.

Headline, dek and headings pass the tests. The headline has no "an agent". The dek uses no named cell
or figure and does not say "slippery grid". The headings are built differently from each other.

Opening at cell 14. The section opens on a run over the whole grid and a count of pairs with returns,
and cell 14 enters in the second paragraph as the instance. Lesson 4 opened on cell 14's values under
the fixed policy. I do not read this as a repeat. Cell 14 is the course's running example, and the
template asks for the same example.

Register. The draft already says what each step is for and keeps the derivation in short sentences.
It ran thin in one place, the resting-point paragraph, where the reader had to do the key algebra
unaided. The new displays do it on the page.

Inline math. I moved it to `nb-math-in`. All four published lessons use that class, `nb.js` renders
it, and the engine's tests cover it. In the draft, π in the prose was set upright in the body font
while the display equations beside it set π in italics. Method names and settings stay plain text
(ε-greedy, ε-soft, ε = 0.1), as lesson 1 writes γ = 0.9. The class is missing from the furniture
catalog, and someone should add it there. The catalog gap is not a reason to leave the course's
convention.

## The experience

I rendered the page with `nb preview` and Playwright at 1280 px and 390 px, in light and dark. Figs.
1-3 are legible in both themes, the legends fit, and the tied arrows at cells 9 and 12 read clearly.
There is no horizontal page scroll at 390 px. One intermediate version used an `nb-math-legend` for
q̃ that overflowed by 4 px on a phone, so I set q̃ as its own display. Code listings scroll inside
their blocks. Table 1's first column is now headed ε, not "Setting".

The page gained the derivation of the resting point, as equations, and a direct link from
`best_soft`'s `q` to q̃. Fig. 2's second panel and the −0.37 now connect to the math. It lost one
duplicate reading row (see Edits).

Prose count, taken from the published page: 2,176 tokens. That covers the cards, body, captions,
table cells, legend descriptions, and problems and answers. It leaves out equations, code, printed
output, SVG text, the reading bands and the sources. Each inline formula counts as one token. Of
those tokens, 2,059 contain a letter, and the headings add 39 more. The draft was 2,119 by the same
count. The page is under the template's 2,200.

What the page gives beyond its sources: it applies Sutton and Barto's construction to the course grid
and computes the best ε-soft policy exactly for each ε. It finds the price (1.08 per start at
ε = 0.1, close to linear in ε) and the ε at which cell 9's arrow leaves the optimal set (0.33). Then
it checks both against sampled runs, which none of the sources ran. This matches the original-work
sentence in `draft-handoff.md`.

The headline is the piece's largest claim, and the page supports "settles for". The resting point is
proven for exact values, runs at both ε settle there, and the page says no proof covers the sampled
algorithm.

## Edits

- Opening card: the floor is "at least ε divided by the number of moves", not "ε". Ordinary starts are
  defined where the card first uses them. Added that an environment cannot always offer exploring
  starts. The last clause now names the smallest ε at which the arrows stop being optimal.
- Background band: removed row 05 (Sutton and Barto 5.4, #page=122), which duplicated Go deeper
  row 01.
- Orientation, paragraph 2: "Right is the move that policy iteration switched…".
- Orientation, paragraph 3: split the conditional into two sentences. Replaced the sentence that
  echoed lesson 4 with "after 10,000 greedy steps the policy is still the hand-drawn one".
- Orientation, last sentence: "A policy that sometimes moves at random can arrange it instead."
- Floor: the on-policy sentence now defines first and names second.
- Floor: rewrote the `soft_play` paragraph's opening (no "the last lesson's", no claim that the file
  changes only episodes).
- Stall-ends, last paragraph: −0.37 named as the exact action value under the ε-greedy policy around
  the optimal arrows. The step and the theorem's reach restated without "improves".
- Safe-step: converted inline math to `nb-math-in`. "π′ is also ε-soft" became "The new policy is also
  ε-soft". The legend wording now reads "the probabilities π puts above the floor".
- Resting-point: inline math to `nb-math-in`; "the weights w(a) from equation (5.2)".
- Resting-point: added the new grid's Bellman optimality equation as a display, with the random part
  taken out of the max, plus a display and a sentence defining q̃.
- Resting-point: rewrote the uniqueness step around q̃.
- Resting-point: tied `best_soft`'s `q[s, a]` to q̃ and Fig. 2's second panel to run 0's averages.
- Resting-point: merged the exact-values sentences, and split the GLIE sentence with the acronym
  spelled out.
- Price: inline math to `nb-math-in` in the lead and the Table 1 caption. Table 1's first column is
  headed ε, with bare values.
- Price: "about the size of one move's reward of −1".
- Price: rewrote the closing two sentences with runs as the subject.
- Figure captions: Figs. 1 and 3 now end "From `exploration.py`.", like Fig. 2 and Table 1.
- Problem 1 answer: arithmetic set as `nb-math-in`.
- Problem 2 answer: corrected what the returns sample after an exploring start.
- Takeaway: recast as four linked sentences ending on the cost and the ε = 0.33 threshold.
- Go deeper row 01: π* set as `nb-math-in`.
- Go deeper row 04: "SARSA with ε = 0.1 learns a longer, safer path… the same effect as ε = 0.5 at
  cell 9".
- Ran `nb stamp` (words=3911, reading_minutes=17, sources=2).

## Decision

approve. The breaks were all fixable from the record and this checkout, and they are fixed. The page
teaches its one idea in the course's register, and the proof with link checks returns PUBLISHABLE:
BLOCK 0, WARN 4. Two W-SENTENCE-DENSITY warnings fire on the TeX of display equations. Two
W-CITE-DENSITY warnings fire on sections built from the lesson's own runs and computation, which the
series prompt exempts.
