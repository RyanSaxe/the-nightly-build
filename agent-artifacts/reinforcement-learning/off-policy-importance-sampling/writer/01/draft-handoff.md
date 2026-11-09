# Draft handoff: reinforcement-learning/off-policy-importance-sampling (writer 01)

## Main idea (27 words)

To value π from b's episodes, scale each return by ∏π(a|s)/b(a|s): the plain average is unbiased,
possibly with infinite variance; the weighted average is biased but bounded.

## Original work

The lesson derives equation 5.4, which Sutton and Barto state without proof, checks it against exact
values with repeated logs on the course's grid, and turns Example 5.5's single divergent sum into a
threshold (infinite variance for every β ≤ 0.9), confirmed by runs on both sides of it.

## Proof

`nb check ... --series reinforcement-learning --repo ...` (links included): BLOCK 0, WARN 4.

- W-SENTENCE-DENSITY ×3, left on purpose. All three "sentences" are the TeX source of the aligned
  equations (the ratio, the unbiasedness derivation, the loop's mean square), which the heuristic
  reads as prose. No prose sentence is flagged.
- W-CITE-DENSITY on `grid-logs`, left on purpose. The section is the lesson's own code, printed
  output and Table 1, which the series prompt exempts.

Prose by my count (cards, headings, captions, table cells, problems; no equations, code, output,
drawing text, bands or sources): about 2,170 words, close to the 2,200 cut line. I cut a third
problem (the grid's own infinite-variance threshold under random behavior) to get there.

## Checks (run from `code/`; scripts in `code/checks/`)

1. Seeds, grid. `uv run --with numpy python checks/grid_seed{2,3,4}.py` (grid_runs.py with seeds
   2-4). Ordinary means stay within about two standard errors of 1.36 at every log size (worst 1.52
   ± 0.07 at 100 episodes, seed 2). Weighted minus ordinary, on the same logs, is 0.74-0.78 at 10
   episodes, 0.19-0.23 at 100 and 0.01-0.04 at 1,000 in every seed. Rms errors stay within 6% of
   each other. The page rounds to "about 0.7" and "within about 5%".
2. Seeds, coverage removed. `checks/grid_unc_seed2.py --uncovered`: ordinary 0.25, 0.21, 0.23.
   `checks/uncover_limit.py` gives the exact limits for cell 7: ordinary 0.168, average ratio 0.650
   (the arrows' probability of never visiting cell 7, which the page's last grid sentence states),
   weighted 0.168/0.650 = 0.258.
3. Seeds, loop. `checks/loop_seed10.py` and `... 0.95` (seeds 10-19). At β = 0.5, nine of ten runs
   end below 1 after a million episodes (0.739-1.037; the tenth caught a scaled return of 262,144).
   At β = 0.95 all end in 0.998-1.002. The page reports only its own runs' range and does not claim
   every run ends below 1.
4. Other settings and cells. `checks/eps_sweep.py EPS SEED START` (ε = 0.3, 0.6, 1.0 from random
   starts; ε = 0.5 from cell 13). Ordinary is centered and weighted starts high in every case. The
   rms comparison is setting-specific: at ε = 0.3 weighted is up to 16% worse, and from cell 13
   weighted is better (6.8 vs 9.8 at 10 episodes), so the page limits it to "on these logs". With
   uniform random behavior the ordinary rms is 30, 22 and 4.3 (infinite variance; not on the page).
   `checks/explore1.py` reproduces the researcher's exact grid numbers (sd of ρG from cell 13 at
   ε = 0.1/0.3/0.5/0.6: 9.24/15.25/34.48/78.70; radius 0.4894).
5. Removal tests, on the page. `grid_runs.py --uncovered` removes coverage. `loop.py 0.95` puts the
   per-pass factor 0.9/β below 1.
6. Worst cases for the loop explanation. `checks/loop_worst.py`. At β = 0.9 (factor exactly 1) the
   sample mean square keeps growing (7.8 to 22.5 between 10² and 10⁶ episodes) and sd·√n grows (2.9
   to 4.9), as a borderline infinite variance should. With β = 0.5 and episodes capped at 20 moves
   the exact sd per episode is 178.5: finite but enormous, as the page says. At 10⁶ episodes the cap
   changes nothing, because no episode in those runs reached 20 moves.
7. Problem 2. `checks/shift.py`: adding 10 and 20 to every return raises the ordinary rms from 2.09
   to 3.62 and 6.64 and leaves the weighted rms at 2.16.
8. Figures. `code/figures/fig_loop.py` prints each run's estimate at 10²-10⁶ episodes, identical to
   loop.py's output. Fig. 1 is drawn from off_policy.py's printed episodes. All three SVGs and the
   equations were checked in `nb preview` with Playwright at 390 and 1280 px, light and dark. No page
   overflow; Table 1 was transposed so it fits a phone without scrolling. `code/build/` holds the
   template and builder I used; edit the article HTML directly from here on.

## Open evidence questions

- Precup, Sutton and Dasgupta (2001) is not a numbered source. Its only recorded URL is
  `http://incompleteideas.net/papers/PSD-01.pdf`. That host's https serves a self-signed
  certificate, B-SOURCES-FORM requires an https href, and dblp and the ACM DL returned bot
  challenges. The page therefore states the β = 0.5 convergence from the strong law of large numbers
  (finite mean of 1, derived on the page) and weighs Sutton and Barto's "do not converge" caption
  against it. PSD 2001 stays as a Go deeper row (http link). If you have an https URL for it, it can
  return as source 2 on the convergence sentence.
- The researcher's grid check says "every reward has magnitude ≥ 1, so E[(ρG)²] ≥ E[ρ²]". Returns can
  be as small as 0.43 in magnitude (goal after seven step costs), so the step is wrong as written,
  though the conclusion survives because |G| ≥ 0.43. The page does not use it.
