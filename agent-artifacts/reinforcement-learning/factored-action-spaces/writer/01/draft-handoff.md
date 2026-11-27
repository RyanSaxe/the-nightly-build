# Draft handoff: reinforcement-learning/factored-action-spaces (writer 01)

Main idea (29 words): If action values add across components, each component takes its own
argmax, so Q-learning stores Σn_d estimates, not Πn_d; where components interact, per-component
choices can miss the joint optimum.

Original work: the lesson builds a new MultiDiscrete rover environment, derives where
per-component Q-tables trained on one shared TD error come to rest, and tests that derivation and
the Π-to-Σ count against its own joint and factored runs, which no source does for tabular
Q-learning.

## Proof

`nb check ... --series reinforcement-learning --repo /home/user/the-nightly-build` (links
included): BLOCK 0, WARN 4, verdict PUBLISHABLE. The four warnings are W-CITE-DENSITY on
sum-of-maxima and averaged-levels (derivations printed on the page) and on six-components and
steep-ledge (runs printed on the page). The series prompt exempts both kinds, so they stand.

Prose words, counted with code/wordcount.py by the identity's definition: about 2,260 for cards,
body, captions and problems, 2,314 with title and dek. That is past the 2,200 mark. I cut the
free-parameter count, the BDQ humanoid example, the SB3 PPO sentence, the QTRAN/IGM and Matignon
attributions and a third problem to get here. The next cut I would make is the "stronger joint
learner" paragraph in six-components, but it qualifies the headline result (see below), so I left
it for the editor to weigh.

Every listing was rerun exactly as printed after the last code edit; all four outputs on the page
are byte-identical to the rerun. Figures checked with Playwright at 390 px and 1280 px in light and
dark themes; no horizontal scroll, no clipped labels after fixes.

## Code and checks

Code and outputs: /home/user/the-nightly-build/.nb-work/reinforcement-learning/factored-action-spaces/code/
(rover.py, learn.py, scale.py, ledges.py and their .out files; figures.py draws the four inline
SVGs from the printed numbers; page_head/body/tail.html plus assemble.py rebuild the article with
escaped listings if code changes, but the article HTML is the source of truth).

Throwaway checks, each run as `uv run <file>` from code/checks/:

1. `fresh.py` (scale.py on seeds 100-109): same ordering at every D; D = 6 joint 57,000
   (54,000-63,500) vs factored 4,500 (3,000-9,000). Slowest factored run beats fastest joint run
   from D = 2 here, from D = 3 on seeds 0-9, so the page says "from three up". The page's
   "over ten times" covers both seed sets (14.4 and 12.7).
2. `uv run ../ledges.py --first-seed 100`: identical counts (joint 0 everywhere, factored 20 in
   cell 2 only).
3. `epscheck.py 0.05` and `epscheck.py 0.2`: factored departs in cell 2 in 20/20 runs at both,
   nowhere else; joint never. At 0.05 this contradicts the fixed-rate prediction (+0.25 for
   extended); the page reports it without a mechanism.
4. `lsfix.py`: exact weighted least-squares resting point of the arm in cells 2 and 5 under
   product rates: -0.5 / +0.8 at eps 0.1, +0.25 / +0.9 at 0.05, -2.0 / +0.6 at 0.2, whichever arm
   level is greedy. Confirms the page's algebra.
5. `settledpair.py`: settled (drive, arm, mast) is (2, 1, 0) in cell 2 and (2, 2, 0) in cell 5 in
   20/20 runs, so Fig. 4's "drive and mast matched the optimum everywhere" holds.
6. `snapshot.py`: reading the tables at the last step instead of averaging, the factored learner
   departs in cells 0/1/2/4 in 4/9/19/1 of 20 runs; it departs at 20%/32%/95% of second-half
   checkpoints in cells 0-2, mostly in the drive in cells 0-1. Joint: 0-3 runs, at most 2% of
   checkpoints. Page states the conclusion without numbers.
7. `jointalpha.py 0.3`: joint learner with alpha 0.3 is about twice as fast as at 0.1 (D = 6:
   31,000, 28,500-34,000) and still about 7x the factored learner.
8. `jointcount.py 0`: joint learner with N(s,a)^-0.7 steps: 1,000 / 1,250 / 1,500 / 2,500 /
   4,250 / 10,000 for D = 1-6, against factored 1,500 / 1,000 / 1,500 / 2,500 / 3,000 / 4,250.
   Page: "kept pace up to four components and still needed more than twice ... at six".
9. `dividedstep.py`: factored learner with alpha/D per table (the sum moves alpha*delta, as the
   researcher's eq. 9.19 note suggests): 1,500 / 1,500 / 4,000 / 6,750 / 11,000 / 15,500, slowest
   seed 76,000 at D = 6. This heavy tail is why learn.py gives every table alpha, which is also
   what the commission's decision text specifies. Not on the page.
10. `fixedrates.py 0.05 fixed` (and 0.1, 0.2): exploring around the optimal action instead of the
    greedy one, the cell-2 arm gap matches the derivation (+0.30, -0.70, -2.05 against +0.25,
    -0.5, -2.0), but the factored estimates elsewhere rose far above every true value (positive
    drive entries where all true values are negative) and many other cells' choices went wrong.
    Off-policy instability of the sum; not on the page.
11. Removal test on the page: `ledges.py --flat` removes the tipping penalty and every departure.
12. Worst case for the explanation: the shallow ledge, where Q* is not a sum and the arm's best
    level depends on the mast, yet the derivation predicts no departure. 0/20 runs depart.

## Open questions for the orchestrator

- Word count, above. Tell me which paragraph to drop if 2,200 is firm.
- The headline's "err only on the steep ledge" is true of the settled (averaged) choice in every
  run and on fresh seeds. Single-step readings also depart in cells 0-1 in some runs; the page
  says so. If the editor wants the headline to cover snapshots, "settle wrong only on the steep
  ledge" is the narrower version.
- The eps = 0.05 departure has a likely cause (one tip drops extended below half, after which the
  agent re-tries extended only on rare exploratory steps), but I could not isolate it: the
  fixed-rate removal destabilised the learner elsewhere (check 10). The page states the
  observation and the fixed-rate assumption without claiming the cause. A cleaner removal test
  would need a different design.
- Result 1 depends on the joint learner's step rule (checks 7-8). The page compares both at the
  same alpha = 0.1 and gives the shrinking-step check in one paragraph.
