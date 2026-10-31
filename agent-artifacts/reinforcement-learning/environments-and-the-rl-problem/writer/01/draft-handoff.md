# Draft handoff: reinforcement-learning / environments-and-the-rl-problem (writer 01)

## Original-work sentence
No source in the record writes the matrix solve, its invertibility, and iterative
policy evaluation together on one worked gridworld: this lesson derives the
invertibility of `(I - gamma P_pi)` in a single line from the contraction (no
source states it), then computes `v_pi` on one 4x4 grid by both the direct solve
and iterative evaluation and shows they agree to `6.7e-10`, closing with a
by-hand one-step backup on cell 14 whose own value sits on the right-hand side of
its equation, which is why the sixteen equations must be solved as a coupled
system rather than evaluated one at a time.

## Proof result
`nb check ... --series reinforcement-learning --repo ...` with links:
**BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** Final stamp: words 3588, reading 16
min, sources 5. No warning left standing; the earlier run's 14 sentence-density
warnings and the length-high warning were all cleared by splitting long
sentences (including tightening the dek, which was 42 words) rather than by
synonym-swapping, and the two bookends are within band.

## Code outputs actually reported (all numbers in the prose and heatmap)
Run with `uv run gridworld.py` and `uv run evaluate.py` (PEP 723, numpy only;
both finish in well under a second on CPU). Files committed beside the article at
`library/reinforcement-learning/environments-and-the-rl-problem/`.

Sanity checks against the known-answer tables the evidence record supplied:
- S&B Figure 3.2 (5x5, gamma=0.9, equiprobable policy): reproduced to one decimal
  (`matches book table to 1 decimal: True`).
- S&B Figure 4.1, k=infinity (4x4, gamma=1): reproduced exactly as integers
  (`matches book table (integers): True`); after k=2 sweeps cell 1 = `-1.75`,
  which the book rounds to `-1.7` (no mismatch, per the record's note).

The running gridworld (4x4, goal terminal at cell 15, gamma=0.9), `v_pi` of the
equiprobable policy by the direct solve, rounded to one decimal (the heatmap and
prose use these):

    -9.4  -9.2  -9.0  -8.8
    -9.2  -9.0  -8.5  -8.0
    -9.0  -8.5  -7.4  -5.8
    -8.8  -8.0  -5.8   0.0

- Direct solve vs iterative policy evaluation: `max |direct - iterative| =
  6.7e-10`, iteration reached it in **187 sweeps** (theta=1e-10); `agree: True`.
- Bellman hand-check at cell 14: `sum_a pi*(r + gamma v(s')) = -5.7572`, equal to
  the stored `v_pi(14) = -5.7572` (cell 14's down-action bumps the wall back to
  14, so its value appears on both sides).
- gamma=0 check used in the nb-note: `v_pi(s) = -1` for every non-terminal cell.

## Decisions honoring the brief
- gamma = 0.9 throughout; prose states the discount is what makes the cited
  convergence/contraction (Silver L3, Szepesvari) apply and that gamma=1 would
  break it.
- Bellman expectation equation for `v_pi` derived in full, supplying the
  Markov-property step S&B's p.59 skips; `(I - gamma P_pi)` invertibility derived
  in one line from the affine operator's unique fixed point, uncited.
- `q_pi` Bellman equation given and cited to Silver slide 34 and Spinning Up
  (S&B leaves it as an unnumbered exercise).
- One notation throughout: S&B's `R_{t+1}`, four-argument `p(s',r|s,a)`, with
  `P_pi`/`r_pi` defined from `p` (noted as the lesson's own definitions).
- Four visuals built and inspected in `nb preview`: agent-environment loop
  (inline SVG), gridworld with the equiprobable policy's arrows and the terminal
  goal (inline SVG), the computed state-value heatmap (`nb chart`), and the
  annotated Bellman equation (`nb-math` with a color-coded legend). I fixed one
  rendering fault the preview revealed: the gridworld SVG's in-figure note
  overflowed the right edge, so I shortened it (the figcaption already carried
  the detail). No arrows stop short and no labels overlap.
- Banned terms: em-dash 0, leverage 0, load-bearing 0, mechanism/mechanisms 0.

## Open question for the orchestrator (sourcing URL, not a claim)
The authors' free authorized S&B PDF (`http://incompleteideas.net/book/RLbook2020.pdf`,
the copy the researcher opened) is **http-only**; the host serves no TLS, and the
proof requires an https source href (`B-SOURCES-FORM`). I therefore cited source 1
to the MIT Press publisher page for the 2nd edition
(`https://mitpress.mit.edu/9780262039246/reinforcement-learning/`), which is
https and authoritative; its 403 to our crawler is a "restricted" response that
the link check does not block, and the page-number locators land a reader on each
passage. The free full-text PDF is kept on the Background and Go-deeper reading
links (those are not `data-nb-source`, so http is allowed and resolves). If the
editor prefers the free PDF as the formal source 1, we need either an https mirror
the paper is willing to cite or a relaxation of the https rule for this host;
flagging rather than inventing an https URL for incompleteideas.net.
