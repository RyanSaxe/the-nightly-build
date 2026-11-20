# Editorial review: reinforcement-learning/potential-based-shaping (editor/01)

## Correct

Thesis, from the draft alone: adding γΦ(s′) − Φ(s) to every reward makes an episode's shaping
rewards sum to γᴺΦ(S_N) − Φ(S₀). Where that last term vanishes, every policy's value from s
moves by −Φ(s) and the optimal policy is unchanged. Under it:

1. On the race with Φ = −(moves left), value iteration's moves equal the finish-only race's and
   each value is the finish-only value minus Φ. Paying shaping on forward moves only brings a
   loop back (cells 5 and 6).
2. A potential of c at the finish changes the comparison by γᴺc. A time-limit cut that the
   target bootstraps through needs the cut cell's ordinary potential. Zeroing it there leaves
   −γᵀΦ(S_T) uncancelled, and under a 10-move limit no greedy Q-learning agent finishes.
3. Shaped tabular Q-learning is unshaped Q-learning started from Φ (Wiewiora), so the guarantee
   says nothing about speed.

All three held.

- Derivation, line by line. The regrouped sum, the shaped return G₀ − Φ(S₀) + γᴺΦ(S_N), the
  value identities and the lap formula −(1 − γⁿ)Φ(s) are right. The sign is right too. With
  Φ(1) = −6 a lap 1 → 2 → 1 nets 1.05 + 0.99 × (−0.94) = +0.1194 exactly. The infinite run of
  laps sums to 0.1194/(1 − 0.99²) = 6.00 = −Φ(1), the same as the route to the finish. The page
  never said why the lap amount is positive, so I added one sentence. Forward and back amounts
  (1.06 − 0.01c and −0.92 − 0.01c) and staying in cell 0 (0.07) match the printed rows.
- Truncation argument, which no source covers. G′₀:T + γᵀv′(S_T) with v′ = v − Φ cancels the
  two γᵀΦ(S_T) terms and leaves the unshaped split return of termination-and-truncation minus
  Φ(S₀). Zeroing the cut adds γ·(moves left) to the cutting step's reward, 6.93 from cell 0. The
  page said the cut "pays" 0.99 times the moves left. That is the extra amount, not the step's
  reward, so both sentences now say "an extra".
- Runs. I extracted both listings from the page and ran them with `uv run` beside the race.py
  printed in specification-gaming. Both outputs match the page byte for byte, in 0.5 s and 1.3 s.
  Every number in the prose, the three SVGs and their aria-labels matches the output. Fig. 3's
  grey arrow (cell 0 back in 3 runs, forward in 2) matches "runs whose greedy move is forward".
  I reran the handoff's checks myself. At L = 10, seeds 5–29, the kept potential finished 20/20
  and the zeroed one 0/20. At L = 30 and 50 the two rules land within 0.13 and 0.000. Value
  iteration gives Problem 1's → → ← ← ← ← → and Problem 2's threshold, −10.1 finishing and
  −10.11 never finishing.
- Sources reopened. Ng, Harada and Russell (pp. 280–282): the absorbing state and the
  never-ending discounted case, the γ = 1 cycle paragraph, Theorem 1, the scope of the converse,
  and Remark 1's "Although we have not proved it here". Grześ (pp. 567–568, 571–572): Eq. 3, the
  Φ(s_N) = 0 rule, and the time-limit stops it covers. Müller and Kudenko (p. 2, p. 6): the
  truncation rule and the runs that got stuck. Wiewiora (pp. 206–208). Sutton and Barto (p. 479
  is PDF page 501, as linked). Two fixes. Wiewiora writes "exponential in the state and action
  space", which the draft had turned into "the number of state-action pairs". The page now uses
  his wording. Neither Grześ nor Müller and Kudenko "set" the potential, since both state it as a
  requirement ("has to be", "must"), so the page now says "require". "Proved, for Q-learning
  alone" became "proved for tabular Q-learning", which matches his own scope sentence.
- The card said the shift follows from the sum without the condition that makes it true. It now
  says the shift holds if the last potential is 0 or the episode never ends.
- Every href returns 200 and lands on the work: Berkeley PDF, IFAAMAS PDFs, arXiv abstract, JAIR
  article page, ML Anthology record, and the Sutton and Barto PDF at the cited page. All five
  internal lesson links resolve, and their titles match. Titles and authors of all four sources
  and the Go deeper rows were checked against the documents. All four `data-nb-kind="primary"`
  are right, because each is the author's own claim or result.

## Reads well

- Cut "the removal test" in two places (charge_back, zero_at_cut). That is the series prompt's
  term, and no lesson has taught it. The flag sentences now say what each flag does.
- The card's second sentence, "an agent paid only at the finish has nothing to learn from before
  its first finish", restates the specification-gaming opener and that lesson's "something to
  learn from before its first finish". I rewrote it in this lesson's terms. The card's last
  sentence ("check a progress reward on paper") echoed the "before any agent trains" close the
  commission flags. It now says what the sum lets the reader decide.
- "Ng and colleagues' theorem covers two kinds of task that never leave this term" was hard to
  parse. It now says the term vanishes in both kinds of task.
- "limit.py tests this" now names the cut rule. "learn.py's settings" was a dangling file name
  and now points to specification gaming. "No run finishes" became "no greedy agent finishes",
  matching the grade in the output.
- "The ordinary return" became "the unshaped return", the page's own word for it. "Where Ng and
  colleagues first argue for a difference of potentials" replaces "the case Ng and colleagues
  argue from". I split the Wiewiora equivalence sentence in two.
- Headings, dek and takeaway do not repeat the recent forms in the commission notes. The
  headline has no number and no environment. No section opens on a cell number. The takeaway
  does not close on a by-X/by-Y pair. No em-dashes or semicolons in prose.

## The experience

The page renders cleanly at 390 px and 1280 px in both themes. It has no horizontal scroll and
no KaTeX errors. All 14 math blocks render. Labels in the three SVGs do not collide, though Fig.
1's under-cell labels are small on a phone. Each figure sits beside the paragraph that reads
it. Prose is about 2,200 words by my count (cards, captions, legends and problems; no code,
output, equations, drawings, bands or sources). The card is about 150 words and the takeaway
about 105.

What the page gives beyond its sources: it runs the telescoping argument on the course's race,
showing that the endless loop and the finish both collect −Φ(start) in shaping. It derives the
case no source covers, a time-limit cut that the agent bootstraps through, and shows by run that
the sources' rule (potential 0 at the cut) stops a bootstrapping Q-learner from finishing. That
matches the handoff's original-work sentence. The headline states the theorem, and the dek
carries its main limit.

## Edits

- Why this matters: rewrote sentences 2–3 to drop the specification-gaming opener's wording.
- Why this matters: made the value shift conditional on the last potential being 0 or the episode never ending.
- Why this matters: rewrote the last sentence ("From that sum you can tell whether a progress reward keeps the optimal policy, …").
- cancellation: "the ordinary return" → "the unshaped return".
- cancellation: added "That is positive on the race, where every potential before the finish is negative."
- cancellation: "the case Ng and colleagues argue from" → "where Ng and colleagues first argue for a difference of potentials".
- loop-returns: removed "the removal test" from the charge_back sentence.
- cut-potential: "covers two kinds of task that never leave this term" → "The term vanishes in both kinds of task that … covers".
- cut-potential: "set the potential to 0" → "require potential 0".
- cut-potential: "each cut then pays" → "each cut then pays an extra".
- zeroed-cut: "tests this" → "tests the cut rule".
- zeroed-cut: "learn.py's" → "those of learn.py in specification gaming".
- zeroed-cut: removed "the removal test" from the zero_at_cut sentence.
- zeroed-cut: "no run finishes" → "no greedy agent finishes".
- zeroed-cut: "A cut in cell 0 now pays 6.93" → "now pays an extra 6.93".
- starting-table: "proved, for Q-learning alone" → "proved for tabular Q-learning".
- starting-table: split the equivalence sentence in two.
- starting-table: the learning-speed sentence now uses Wiewiora's "exponential in the size of the state and action spaces".
- `nb stamp` rerun. Proof: BLOCK 0, WARN 4 (the two W-SENTENCE-DENSITY flags are the aligned TeX equations, and the two W-CITE-DENSITY flags are sections of the lesson's own derivation and run). PUBLISHABLE.

## Decision

approve. The argument is correct and checked by runs, and every remaining issue was fixable in
place.
