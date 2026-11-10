# Editorial review: reinforcement-learning/n-step-returns (editor/02)

## Correct

The thesis and its claims are as in editor/01: the n-step target and its two
ends, the n-step error as the first n TD errors, the n-move delay, n = 4 lowest
at its own best step size, and the mechanism (short targets carry the outcome
back slowly, noise in long targets forces a small step). This round broke one
explanation and one description of evidence.

1. Fig. 1 walkthrough. The page said n = 6 moves V(17) and V(18) twice "because
   it updates on every visit". That reason was wrong: n = 3 also updates on
   every visit. I traced every update `nstep_td` makes on that episode
   (`editor02/checks/trace_fig1.py`). Under n = 3, the targets for times 0, 1
   and 2 read V(17), V(18) and V(19) while all three are still 0, so those
   updates change nothing, and only the +1 targets at times 3 to 5 move
   anything. Under n = 6 every target is +1, so both visits count. The sentence
   now gives that reason. The printed numbers (0.5 and 0.75) were right and
   are unchanged.
2. The `--expected` removal test. The reader is right that it is close to
   guaranteed. Monte Carlo's expected target is the true value, so once the
   noise is gone Monte Carlo has to rank first. I checked what is left of its
   error (`editor02/checks/expected_mc_unvisited.py`). At α = 1 every state
   Monte Carlo has visited is exact (largest error 4e−16), and the 0.058 is
   the error of the states no walk has reached yet. That floor is the same for
   every n. The run is still evidence for the noise half of the explanation:
   with the same states updating in the same order, removing only the noise
   cuts Monte Carlo's error from 0.49 to 0.06 and TD(0)'s only from 0.34 to
   0.28, and the best step size goes to 1 for every n. The paragraph now says
   the ranking proves nothing, says the run measures what the noise cost, and
   says what the 0.06 is. The causal claim stays. The takeaway's "the longest
   target did best" became "removing the noise cut Monte Carlo's error far more
   than TD(0)'s". It does not say "TD(0) least", because n = 2 gains less than
   TD(0) does (0.277 to 0.235).
3. Robustness. I reran `checks/seeds.py` at offsets 1000, 2000 and 3000. n = 4
   stays lowest of the swept n (0.257 to 0.259), with TD(0) at 0.343 and Monte
   Carlo at 0.479 to 0.489, the same margins as the page's run.
   `checks/integer_n.py` puts n = 3, 4 and 5 within 0.002 of each other on both
   seed sets, and n = 6 within 0.004. The page now says n = 3 and n = 5 tie
   with n = 4, so the best n is a range around 4. The headline still holds,
   since it compares n = 4 only with the two ends.
4. Fig. 3 comparison. Monte Carlo's 10th to 90th percentile band is wider than
   n = 4's at 18 of 19 states (all but state 1), at a step size of 0.022
   against 0.37. The page now says that instead of quoting one state's range.
5. The subscript definition, "V_k is the table of estimates after the update
   made at time k", agrees with the record's p. 143 text: the target needs
   "R_{t+n}" and "V_{t+n−1}", and both are first available at t + n. I placed
   it after the eq. 7.1 citation so the citation still covers only the
   equation.
6. Sutton's code (s3) sets the start state to the middle (`truncate (/ n 2)`,
   zero-based 9), `initial-w 0.0`, and one set of `standard-walks` for every
   setting. The step-size opener now attaches the s3 citation to exactly those
   three choices.

Throwaway checks for this round are in
`/tmp/claude-0/-home-user-the-nightly-build/f459be86-7567-53db-a107-d49609878cc2/scratchpad/editor02/checks/`.
Each takes as its first argument a folder holding the page's `nstep.py` and
`sweep.py`. Run `trace_fig1.py` with `python3`, and `expected_mc_unvisited.py`
with `uv run --with numpy python`.

Listings. I changed `nstep.py`: comments only in `nstep_td`, and the one-walk
demo and its `import random` are gone (see Reads well). I extracted both
listings from the built page into a fresh folder and ran all five printed
commands with `uv run`. Every output matches the page byte for byte. The four
`sweep.py` outputs are unchanged. `checks/pseudocode.py` still gives a largest
difference of 0.0 from the p. 144 box, and 0.0 from every-visit Monte Carlo at
n = ∞. Problem 1 still gives V(18) = 0.75 and V(19) = 0.85. `start_exact.py`
still has TD(0) lowest at every step size. No href changed. One inline citation
went with the cut aside (s1, p. 144 box). The proof checked links.

## Reader check 1

Restatement against the main-idea sentence: they match. The reader has the
target, both ends, the scope (19-state walk, first 10 episodes, each n at its
own best step size) and that a middle n wins. The reader also gives both halves
of the mechanism. Nothing about the main idea had to change.

Place by place, in the reader's order:

- n = 3 against n = 6. The reason was wrong. Corrected, see Correct 1.
- Why this matters. I cut the sentence on n-step SARSA, DQN's multi-step
  targets, the λ-return and GAE. The main idea does not need it, and the Go
  deeper rows already name each one in terms the course has taught. "Code the
  update's n-move delay" became "code an update that waits n moves for its
  target".
- Time subscripts. I added one sentence after the eq. 7.1 citation defining
  V_k. The derivation now says "Hold the estimates fixed, so V needs no time
  subscript" before the recursive form, where the subscripts first disappear.
- "A return that stops where it starts is the estimate there." Now "is defined
  as the estimate there".
- Seeds and Sutton's code. "Unused" and "do as well" are replaced by "New seeds
  for three more sets of 100 runs keep n = 4 lowest by similar margins" and
  "tie with it, so the best n is a range around 4". The Sutton's-code phrase now
  introduces the setup it fixes: start state, starting estimates, shared walks.
- `--expected`. Rewritten to say what it does and does not show. See Correct 2.
  I added one clause on why α = 1 is best for every n: a small step averages
  noisy targets, and here there is no noise to average.
- "Distance left to travel." Replaced with the literal statement: TD(0) wins
  when the outcome has to be carried back only a few states, or when the
  estimates already carry it.
- The code. Comments inside the listing answer all three questions. `T =
  infinity: the episode has not ended` is on the `update(tau, float("inf"))`
  line. A line above the guard says that if s is an end, the loop below makes
  the update. `R_{tau+1} + ... + R_h, with no discount` is on the `G` line, and
  the prose now opens that sentence with "With no discount". I cut the sentence
  on Sutton and Barto's n + 1 buffer, whose purpose the reader could not name.
- "Online updates." Now "Because n-step TD changes the estimates during an
  episode, for it the identity is only approximate."
- Monte Carlo's small step. Added the missing link: within one episode the
  same-direction moves add up like one large step, so only a small step keeps
  an estimate near the average over many episodes.

Sections the reader could skip:

- The TD-error section stays. The commission asks for a derivation, and this
  one ties the n-step target to the earlier lesson's sum of TD errors. Its
  first sentence now says what the derivation shows: where the n-step return
  sits between TD(0) and Monte Carlo.
- The delay mechanics and code stay, per the orchestrator note and the
  commission.
- Watkins stays, because the series prompt asks for a link to the work that
  introduced an idea. The Sutton's-code phrase stays in its new form, see above.

Results reported without their meaning:

- Seed robustness and margins: answered in the seeds sentence.
- `--size 5` and `--episodes 100 --first 91`: no numbers added. The commission
  limits these flags to backing the one scope sentence. Their outputs and
  margins are in the collapsed listing for anyone who wants them. The sentence
  before them now says which case each one is.
- What α = 1 and the leftover 0.06 mean: answered in the `--expected`
  paragraph.
- The Monte Carlo range at state 10: replaced by the comparison with n = 4's
  band (Correct 4).
- α = 1 against α = 0.05: the reader found this one fine. I cut the sentence
  after it, which restated why each n gets its own best step size, for length.

## Reads well

Went:

- The forward-pointer sentence in Why this matters. The reader could not tell
  what it was for. Cut, not repaired.
- "Sutton and Barto's version keeps only the last n + 1 states and rewards…".
  An aside the main idea does not use.
- The one-walk demo in `nstep.py`, its output line, and the two sentences
  explaining it. I cut this whole result for length, as the template requires
  above about 2,200 words. It repeated what Fig. 1 already shows (in one
  episode the outcome reaches n states back), and Fig. 3 shows what n = 4
  learns over a run.
- "So the comparison above gives each n its own best step size." It restated
  the paragraph's first sentence.
- "and a fifth at state 8". The half at state 6 shows the point alone.
- "Each n does best with the smallest step size" in problem 2's answer. The
  answer now opens "TD(0), at every step size", which is the part that matters.
- "If noise holds the long targets back, they should now win, and they do." It
  presented a near-certainty as a prediction.

Lifted or rewritten:

- "Nothing has to travel" in problem 2 used the same metaphor the reader
  flagged. It now reads "The estimates already carry the outcome".
- "The output matches the hand-worked estimates for Fig. 1's episode" replaces
  a line that called them "Fig. 1's estimates", since Fig. 1 shows targets.

The new text keeps the guide's register: one step per sentence, and the reason
given before the step. Nothing new borrows from the voice guide's quoted
passages or the commission's wording. No new opener, closer, dek or heading
follows the recent-pattern notes. The headline, dek and headings are unchanged.

## The experience

Prose on the rendered page is **2,195 words** (it was 2,176). I counted with
the same Playwright script and definition as editor/01 on an `nb preview`
build. That covers both cards, headings, captions, legend text, the details
summary and note, and the problems with their answers. It leaves out the
headline and dek (49 words), equations, code, printed output, SVG text, the
bands and the sources. "n = 4" counts as three words. By section: why 138,
orientation 543, first-n-td-errors 217, delay 135, step-size 274,
outcome-and-noise 771, takeaway 117.

At 390 px and 1280 px, in light and dark, nothing overflows (scrollWidth equals
the viewport). The longest new code comment scrolls inside its listing. The
figures are unchanged.

The page gives the reader more than its sources do. It reproduces Figure 7.2
from code a reader can run, and it states the mechanism the book leaves out.
It now also measures how much of each method's error the target noise causes,
instead of claiming a ranking that the construction guaranteed. This still
matches the original-work sentence in `draft-handoff.md`, apart from its last
clause ("which makes the longest target best"). That clause now overstates
what the test shows, but the handoff is the writer's record and the page no
longer says it.

Whether a second reader check is needed: none of my changes alters the
lesson's central explanation, and none rewrites a whole section. The closest
case is the `--expected` paragraph. It still supports the same causal claim,
but it now describes its evidence differently: what the noise cost, not which
n ranks first. Most of the edits are corrections, cuts and clauses within
paragraphs. The largest cut is the one-walk demo in the delay section.

## Edits

- Why card: cut the n-step SARSA / DQN / λ-return / GAE sentence; "code the update's n-move delay" became "code an update that waits n moves for its target".
- Orientation: rewrote the n = 3 / n = 6 sentence with the correct reason (n = 3's first three targets read estimates still at 0).
- Orientation: added "V_k is the table of estimates after the update made at time k." after the eq. 7.1 citation.
- first-n-td-errors: new opening sentence on what the derivation shows; added "Hold the estimates fixed, so V needs no time subscript"; "is the estimate there" became "is defined as the estimate there"; dropped "With the estimates held fixed," from the next sentence.
- first-n-td-errors: "Online updates change the estimates…" became "Because n-step TD changes the estimates during an episode, for it the identity is only approximate."
- delay: "A running sum C…" now opens "With no discount,"; cut the sentence on Sutton and Barto's n + 1 buffer and its citation.
- nstep.py: comment on the `G` line (no discount); comment above the end-of-episode guard; comment on `update(tau, float("inf"))`.
- nstep.py: removed the one-walk demo (three lines) and `import random`; removed its output line.
- delay: replaced the two output-paragraph sentences about the demo with "The output matches the hand-worked estimates for Fig. 1's episode."
- step-size: split the opener so the s3 citation sits on the setup it fixes (start state, starting estimates, shared walks); "with the same walks for every setting" moved there.
- step-size: rewrote the seeds sentence (new seeds, similar margins; n = 3 and n = 5 tie, so the best n is a range around 4).
- step-size: cut "So the comparison above gives each n its own best step size."
- outcome-and-noise: cut "and a fifth at state 8".
- outcome-and-noise: rewrote the Monte Carlo paragraph's first sentence (wider band than n = 4's at all but one state, at a far smaller step) and replaced "A larger step would make each estimate follow the last few outcomes" with the compounding-steps sentence.
- outcome-and-noise: rewrote the `--expected` paragraph (opener; the ranking is not a test; the cost of the noise; the 0.06 floor; why α = 1 is best).
- outcome-and-noise: "a short target wins when the outcome has little distance left to travel" became "TD(0) wins when the outcome has to be carried back only a few states, or when the estimates already carry it".
- Problem 2 answer: "TD(0)." became "TD(0), at every step size."; "Nothing has to travel" became "The estimates already carry the outcome"; cut the last sentence.
- Takeaway: "With the noise removed, the longest target did best." became "Removing the noise cut Monte Carlo's error far more than TD(0)'s."
- Ran `nb stamp` (words 4497, 20 min, 3 sources).

## Decision

approve. Every place in the reader check is corrected, cut or explained. The
one wrong explanation is fixed from a trace of the printed code, and the
removal test now claims only what it shows. Every listing reruns byte for byte,
and the proof, with links checked, gives BLOCK 0.
