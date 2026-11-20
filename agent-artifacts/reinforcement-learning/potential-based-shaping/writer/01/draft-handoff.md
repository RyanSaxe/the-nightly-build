# Draft handoff: reinforcement-learning/potential-based-shaping (writer 01)

## Main idea (under 30 words)

Adding γΦ(s′) − Φ(s) to every reward shifts every policy's value from s by −Φ(s), so the
optimal policy stays wherever the potential term at the end of the return vanishes.

## Original work

The lesson derives the telescoped shaped return and runs Ng, Harada and Russell's theorem on the
course's own race, with a removal test that brings the loop back, and it derives and then tests
by run what no source covers: a time-limit cut that the agent bootstraps through must keep its
potential, and the sources' rule of potential 0 at the cut stopped every Q-learning run on the
race from finishing.

## Proof

`nb stamp`, then the brief's exact `nb check` with links: BLOCK 0, WARN 4, PUBLISHABLE.
Warnings left on purpose:

- W-SENTENCE-DENSITY ×2. Both are the TeX source of the two aligned equations (the expanded
  telescoping sum and the cut-episode identity). The heuristic skips code, math and svg elements
  but reads `div.nb-math-eq` as prose. No prose sentence trips it.
- W-CITE-DENSITY on `orientation` and `zeroed-cut`. Both hold only the lesson's own arithmetic,
  derivation and run, which the series prompt says need no citation.

Prose is about 2,250 words by my count (cards, captions, legends and problems included; code,
output, equations, drawings, bands and sources excluded), a little over the ~2,200 line. To get
there I cut a third problem, most of the Wiewiora section, Grześ's two-ending example and the
bicycle case (now a Go deeper row). `nb stamp` counts 4,416 because it includes code.

## Code and how it was checked

The code is in `.nb-work/reinforcement-learning/potential-based-shaping/lesson-code/`: `race.py`
(unchanged from the specification-gaming listing), `shaping.py` and `limit.py` (both printed in
full), and `figures.py`, which draws the three inline SVGs from those two files and stays off the
page. I extracted the listings from the built page, ran them with `uv run` next to `race.py`, and
they reproduce the printed outputs exactly. Phone and desktop widths in light and dark were
checked for all three figures and the four equations. There is no page-level horizontal scroll and
no KaTeX error.

## Checks off the page (throwaway code; rerun to confirm)

1. Result 1 across settings: γ ∈ {0.5, 0.9, 0.99, 0.999}, Φ scaled ×1 and ×100, and three random
   Φ (normal, σ = 20, 0 at the finish). In every case the shaped optimal moves equal the
   finish-only moves, and the largest |q*′ − (q* − Φ)| is ≤ 1.2e−13.
2. Removal test choice for result 1: Ng's undiscounted form Φ(s′) − Φ(s) at γ = 0.99 does not
   change the race's moves (all →, values 16.21 … 11.00), so it cannot show the cause. Paying
   forward moves only breaks the pairwise cancellation and brings back a loop (cells 0–5 →,
   cell 6 ←).
3. Problem 2: value iteration with finish potential c. At c = −10.1, −5, 7 every move is →. At
   c = −10.11 and −10.2 the agent never finishes. That matches c < −10/γ.
4. Problem 1: `value_iteration(0.99, once=True)` gives unpaid cells 0–6 as → → ← ← ← ← →, the
   researcher's check reproduced.
5. Result 2 with other seeds: at L = 10, seeds 10–29: potential kept 20/20 finish with error
   0.000, potential 0 at the cut 0/20 finish with errors from 83 to 98. At L = 20, seeds 5–19:
   kept 15/15, zeroed 0/15.
6. Result 2 with another step size: N(s,a)^−0.7 over 5,000 episodes at L = 10 with 10 seeds:
   kept error 0.000 and 10/10 finish, zeroed 0/10 finish. At L = 20 with N^−0.7, zeroed finished
   4/5 with only 6% of episodes cut, so the failure needs frequent cuts. I chose L = 10 because
   a quarter of the correct agent's episodes are cut there.
7. ε = 0.2 at L = 10: zeroed 0/10 finish.
8. Worst case for the explanation, long limits: at L = 30 the two rules end within 0.13 of each
   other, and at L = 50 and 100 they end at the same estimates (error 0.000), because trained
   agents are almost never cut. On the page as one sentence without numbers.
9. Worst case for the explanation, sign: with Φ = the cell number (positive, 0 at the finish),
   zeroing at the cut is a charge. Estimates fell by up to 2.2 below q* − Φ, greedy moves
   changed in 7 of 20 constant-step runs at L = 10, and none changed with N^−0.7. Not on the page.
10. Wiewiora in the runs (L = 10, seeds 0–4): shaped Q-learning from 0 and unshaped Q-learning
    from Φ on the same seed agree to 7e−15 with the potential kept at the cut, and differ by
    about 90 with it zeroed. With the cut treated as terminal and Φ = 0 there (Grześ's and
    Müller and Kudenko's setting), the shaped and unshaped agents agree to 4e−15, so their rule is
    right for their learner. Keeping Φ in that setting makes them differ by 1.7 to 3.1.

## Decisions taken without asking (assumptions to confirm)

- Potential Φ = −(moves left). It is 0 at the finish by construction, like Ng's negative-distance
  grid potentials. Because Φ < 0, one lap at γ = 0.99 nets +0.12, not a negative amount like the
  commission's example for a positive potential. The page gives the actual value and the general
  −(1 − γⁿ)Φ(s), and it shows that the endless loop still collects only −Φ(start), the same shift
  that finishing gets. I chose this sign because the zeroed-cut failure under a positive potential
  is weak and depends on the seed (check 9).
- Two results: value iteration with `charge_back` as its removal test, and Q-learning under a
  10-move limit with `zero_at_cut` as its removal test. The terminal-potential limit is covered by
  derivation and Problem 2. Necessity gets one sentence, the forward-only reward and Problem 1.
  Wiewiora's equivalence and learning speed get a short section without a run.
- Mention-only topics: Devlin and Kudenko appear only as a Go deeper row. Shaping in
  language-model RL is not mentioned, because the researcher did not cover it. Jenner et al. are
  not used.
- The record gives only venues for Grześ, Wiewiora, Randløv and Alstrøm, and Müller and
  Kudenko, so I read their titles and author names from the recorded URLs (the arXiv abstract,
  the ML Anthology records, the JAIR page and the Grześ PDF). Wiewiora's first name came from the
  arXiv mirror's PDF. Nothing else was added from those pages.

## Open questions

None blocking.
