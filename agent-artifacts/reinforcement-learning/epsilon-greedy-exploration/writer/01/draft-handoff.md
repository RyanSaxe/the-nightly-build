# Draft handoff: reinforcement-learning/epsilon-greedy-exploration (writer 01)

Main idea (29 words): Greedy policies get no returns for skipped moves. An ε-soft policy samples
every move, and ε-greedy improvement can rest only at the best ε-soft policy, which is worse than
optimal.

Original work: the lesson applies Sutton and Barto's construction (the policy's random moves moved
into the environment) to the course grid to compute the best ε-soft policy exactly for each ε,
which no source does for this grid. It then checks that against sampled on-policy Monte Carlo runs.
The price is 1.08 per start at ε = 0.1 with the optimal arrows kept up to ε = 0.32. From ε = 0.33
the best arrows leave π* at cell 9, and the ε = 0.5 runs settle there.

## Proof

`nb check ... --series reinforcement-learning --repo ...` with link checks: BLOCK 0, WARN 3,
PUBLISHABLE. Warnings left on purpose:

- W-SENTENCE-DENSITY (77 words): the "sentence" is the TeX source of equation (5.2) in its
  `nb-math-eq` div, which the parser reads as prose. No reader sees it as a sentence.
- W-CITE-DENSITY on `stall-ends` and `price`: both sections consist of the lesson's own runs, code
  and exact computation. The series prompt says no action is needed there.

Prose length: about 1,950 words counting alphabetic words, about 2,240 counting every token
(numbers, ×, = and so on), on the cards, body, captions, table and problems. To get there I cut
whole ideas: a third problem (ε = 1), the point that an agent can drop ε after learning and recover
v* when the arrows match, and a separate definition of "soft".

## Code

The printed listings are `soft_control.py` (new) and `exploration.py` (in a `details`, with its
output). Both import the earlier lessons' files unchanged. I extracted every listing exactly as
printed from lessons 1-4 and this page into an empty folder and ran `uv run exploration.py`. The
output was byte-identical to the printed output, in 3m37s. Copies are in `writer/01/code/`, with
`figures.py`, the off-page script that draws Figs. 1-3 as inline SVG from the same seeds:
`uv run figures.py <folder with the lesson files> <out dir>`.

## Checks (throwaway, in writer/01/code; each takes the lesson-file folder as its first argument)

1. New seeds 20-39 (`check_seeds.py DIR 0.1 20 40 200000`, `check_seeds.py DIR 0.5 20 40 100000`).
   With ε = 0.1, the runs at the optimal arrows were 4, 17 and 19 of 20 at 10,000, 100,000 and
   200,000 episodes (the page's seeds give 6, 14, 19). With ε = 0.5, 14 of 20 were at the best
   ε-soft arrows at 10,000 and 20 at 75,000 and 100,000 (the page gives 18, 20). The conclusions
   repeat: ε = 0.1 escapes the stall, ε = 0.5 gets there sooner and rests on the cell-9 arrows.
2. The stall across seeds (`check_seeds.py DIR 0.0 0 20 200000`): with ε = 0 no run is optimal at
   any checkpoint up to 200,000. The wrong cells are always exactly 13 and 14, so the policy never
   changes. The removal test on the page is the same flag at 10,000 episodes.
3. Worst case for "every move is sampled, so the stall ends": one run in each seed set is still
   wrong at 200,000 (cell 8 for seeds 0-19, cell 9 for seeds 20-39). These are near-ties under the
   ε-soft values (exact margins 0.88 at cell 8 and 0.38 at cell 9). By construction each move is
   tried with probability at least 0.025 on every visit to its cell (run 0's rarest pair has 430
   returns by 200,000; I did not count the two failing runs). They look slow to settle, not
   stalled.
4. Worst case for "runs settle where the exact computation says" (`check_threshold_and_averages.py`):
   at ε = 0.35, cell 9's exact margin is 0.04, and after 100,000 episodes only 12 of 20 runs aim it
   left or down. Sampled runs do not resolve near-ties. The page claims settling only at ε = 0.1
   and 0.5.
5. The flip threshold (`check_flip.py`): cell 9's up-minus-down action value under the best ε-soft
   policy is +0.0097 at ε = 0.32 and −0.0074 at ε = 0.33.
6. Averages estimate the ε-greedy policy's values beyond run 0 (`check_threshold_and_averages.py`):
   with ε = 0.1 after 200,000 episodes, the average for right at cell 14 across seeds 0-19 has a
   mean of −0.38 and a range of −0.50 to −0.31, against −0.37 for the best ε-soft policy and 0.61
   under the optimal policy. In every seed, at least 91% of the 56 pairs (96% on average) sit
   closer to the ε-soft value than to q*. The claim does not rest on run 0 alone.

## Evidence and voice notes

- Commission decisions applied: no convergence claim. The page states the fixed point and monotone
  step as proven for exact action values, says the book gives no proof for the sampled version,
  and reports only the runs. The opener uses absent averages (14 of 56 pairs), not wrong ones. The
  bandit mechanism appears only as a Go deeper pointer. GLIE gets one sentence and Singh et al.
  Origin of the term is not mentioned.
- Contradictions left off the page because they do not change what the lesson says: the "ε-greedy"
  variants that draw the random move from the other moves only (Watkins; Singh et al.'s GLIE
  wording); Silver's unproven "GLIE Monte-Carlo control converges" slide; Silver's narrower
  ε-greedy hypothesis. The page uses Sutton and Barto's definition (random over all moves) and
  their ε-soft hypothesis.
- Source 1's href is the MIT Press book page (https), with a note pointing to the authors' free copy
  the researcher read. incompleteideas.net serves https with a self-signed certificate, and the
  proof requires an https source href. Lesson 4 did the same. The reading-band rows link the free
  PDF at the cited page.
- Inline math is plain HTML (italic letters, subscripts), not `nb-math-in`. That class works in
  `nb.js` and the published lessons use it, but the furniture catalog does not document it. The
  editor may prefer the published lessons' convention.
- The step "a policy μ in the new grid moves like the ε-soft policy (1 − ε)μ + ε/|A(s)|, and every
  ε-soft policy arises this way, with μ equal to the weights of (5.2)" is my explanation of why
  Sutton and Barto's two optimization problems coincide. They assert the coincidence. The algebra
  is on the page.
- No open evidence questions.
