# Draft handoff: reinforcement-learning/learning-values-from-samples (writer 01)

## Original work (the one sentence)

On lesson 1's grid with the model hidden, this lesson measures from 40-seed runs
scored against the known v_pi where each estimator's error comes from, and so
turns Sutton and Barto's "which converges faster is open" into a concrete
bias-variance picture: first-visit Monte Carlo's cell-13 estimate swings wildly
but centers, unbiased, on -2.01, while TD(0)'s climbs smoothly yet sits biased
too low (near -2.69 at 100 episodes) before settling, and a constant step size
leaves both on a floor (RMS 1.42 and 0.82) that the decaying schedules clear.

This is visible on the page in Fig. 2 (the RMS learning curves with across-seed
bands, TD lower and tighter early, unbiased MC crossing under it at 6,000
episodes), Fig. 3 (first-visit MC's value grid converging to lesson 1's exact
grid), and the prose reading of cell 13's trajectory for each method.

## Proof result

`./nb check .../learning-values-from-samples.html --series reinforcement-learning
--repo /home/user/the-nightly-build` (links included): **BLOCK: 0, PUBLISHABLE.**

One warning left on purpose:

- **W-LENGTH-HIGH** — 4054 words against the 2000-3600 band. The band counts
  code, and this lesson carries the required full `samples.py` listing (150
  lines) plus its run output, three mechanism visuals with captions (inline-SVG
  backup contrast, computed learning-curve chart, converging value heatmap), two
  annotated equations, and a three-problem `nb-note`. It is in line with lesson 2
  (3974 words, same warning). Prose was trimmed and five dense sentences split to
  clear every other warning; cutting further would drop required teaching. Flagged
  for the editor rather than cut.

All other checks pass. Chrome `render-check` is clean (no overflow at 390px, no
page errors, KaTeX and Prism load). Every rendered visual was inspected: the
backup SVG (arrows reach their targets, no label overlap), both charts, both
annotated equations, and the code listing.

## Every number is from a real run

`samples.py` (shown inline, not committed) reconstructs lesson 1's `gridworld.py`
and implements first-visit MC, every-visit MC and TD(0) using only sampled
episodes (reward and next cell); `transitions` and the exact solve appear only in
the environment that emits episodes and in `exact_values`, which scores. Run with
`uv run samples.py`, ~47 s. The two committed chart scripts embed that run's
printed series (documented in each script's docstring). v_pi(13) = -2.01 and the
-1.94 one-cell check are inherited from lesson 1, cited to it in prose and the
Background link, not re-derived.

Committed beside the article: `chart-1.py`/`chart-1.png` (learning curves) and
`chart-2.py`/`chart-2.png` (value heatmap) only, matching lessons 1-2.

## Query decisions honored

- Bias/variance is earned from the runs, not asserted; "which converges faster"
  is stated as open (S&B p. 124 / Sutton 1988 p. 29).
- "MC is unbiased" is scoped to first-visit; every-visit is labelled biased at
  finite n (Singh & Sutton), with its slightly higher final RMS shown.
- Curves converge because MC uses 1/N(s) and TD uses a decaying step
  (alpha = N(s)^-0.7); the constant-alpha floor is shown honestly.
- TD-Gammon framed honestly in the opener (a neural-net TD learner, Tesauro's own
  counts: 200,000 games to ~Neurogammon; v2.1 a one-point loss to Robertie) and
  named a combined prediction/control task in the body, not this lesson's tabular
  TD(0).

## Recent shapes broken

No AlphaGo opener (TD-Gammon instead); dek built on a new frame (no "...while
[contrast]" mold); body closes on the prediction-vs-control gap, not "the next
lesson"; takeaway closes on this lesson's own finding; headings vary in
construction.

## Open questions for the orchestrator

None blocking. The evidence supported every claim made. Sources s2 (Singh &
Sutton) and s3 (Sutton 1988) are cited by their canonical DOIs (both resolve)
with a note pointing to the author PDFs the researcher actually read, because the
form check requires https and the authors' sites serve the papers over http only.
