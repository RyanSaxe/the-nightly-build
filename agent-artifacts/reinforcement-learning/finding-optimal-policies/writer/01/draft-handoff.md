# Draft handoff: reinforcement-learning/finding-optimal-policies (writer 01)

## Output paths

- Article: `/home/user/the-nightly-build/.nb-work/reinforcement-learning/finding-optimal-policies/library/reinforcement-learning/finding-optimal-policies.html`
- Chart script + PNG (ship together): `.../library/reinforcement-learning/finding-optimal-policies/chart-1.py` and `chart-1.png`
- Scratch run dir (code I ran): `/tmp/claude-0/-home-user-the-nightly-build/3484507d-c4e1-5c1b-989a-2bda3f8f2f43/scratchpad/rl2/` (`gridworld.py` recreated verbatim from the brief, `control.py`, plus the figure generators `gen_svg.py` and the preview renderer)

## The original work, in one sentence

On lesson 1's exact slippery grid (slip 0.2, γ = 0.9), this lesson runs policy iteration and value iteration against the hand-drawn policy and shows that two evaluate-and-improve rounds reach the optimal policy, lifting the bottom two rows near the pit (cell 13 from −2.01 to −0.71, cell 14 from −1.08 to +0.61) while leaving the top eight cells, already optimal, exactly unchanged, and that value iteration reaches the same policy in 18 sweeps by folding one greedy step into each pass.

## The run

`gridworld.py` is lesson 1's file, recreated verbatim (the `transitions`, `fixed_policy`, `draw`, `move` helpers and the constants). `control.py` imports it and adds `evaluate`, `action_values`, `greedy`, `policy_iteration`, `value_iteration`. Command: `uv run control.py`. Exact console output:

```
v_pi of the hand-drawn policy:
  2.16   4.04   6.48   0.00
  0.61   0.06   0.00   6.48
 -0.72  -1.03  -0.10   4.02
 -1.86  -2.01  -1.08   1.98
v_pi(13) = -2.0055 (lesson 1: -2.01)
cell 14 q (up,right,down,left): -1.076 0.3167 -1.7774 -2.5499
cell 13 q (up,right,down,left): -2.0055 -2.0478 -2.7085 -2.6148

Policy iteration (keep old action on tie):
  round 1: 1 changed -> cell 14, v(13) = -1.8412
  round 2: 1 changed -> cell 13, v(13) = -0.7142
  round 3: 0 changed, v(13) = -0.7142
pi_* (arrows, '.' at goal and pit):
> > > .
^ ^ . ^
^ ^ > ^
^ > > ^
v_* and the gain v_* - v_pi:
  2.16   4.04   6.48   0.00     0.00   0.00   0.00   0.00
  0.61   0.06   0.00   6.48     0.00   0.00   0.00   0.00
 -0.71  -1.01   0.06   4.04     0.00   0.01   0.16   0.02
 -1.73  -0.71   0.61   2.16     0.13   1.29   1.69   0.18
v_*(13)=-0.7142 v_*(14)=0.6129; gains 13:1.2912 14:1.6889; max gain rows 0-1: 0.0000
ties at v_*: cell 9 -1.0142=-1.0142, cell 12 -1.7347=-1.7347

Value iteration from v = 0:
  tol 1e-04: 18 sweeps, err 7.6e-05, greedy == pi_*: True
  tol 1e-08: 30 sweeps, err 4.1e-09, greedy == pi_*: True
VI v(13) per sweep: 0.0 -1.0 -1.9 -2.71 -3.439 -1.9863 -1.3345 -0.9811 -0.8355 -0.7668 -0.7377 -0.7245 -0.7188 -0.7162 -0.7151 -0.7146 -0.7144 -0.7143 -0.7143
PI v(13) per round: -2.0055 -1.8412 -0.7142 -0.7142
```

### Agreement with the commission's VERIFIED numbers

Every VERIFIED figure reproduced exactly:
- `v_π(13) = −2.0055` (matches lesson 1's −2.01).
- Cell 14 action values up −1.08, right +0.32, down −1.78, left −2.55 (right beats the hand-drawn up); cell 13 action values up −2.01, right −2.05, down −2.71, left −2.61 (hand-drawn up already best, so cell 13 does not flip first). The lesson uses **cell 14** as the move that beats the policy's choice, per the correction.
- Policy iteration with keep-the-old-action-on-a-tie converges in **3 rounds** (2 that change the policy: cell 14, then cell 13). The lesson states this tie rule explicitly and compares by action value at the tied cells 9 and 12.
- Per-cell improvement: rows 0-1 (cells 0-7) change by exactly 0.000; cell 13 gains 1.29, cell 14 gains 1.69. The lesson states the inequality as `≥` ("no worse anywhere, strictly better near the pit") and does **not** claim "better at every cell."
- Value iteration: **18 sweeps** to 1e-4, **30** to 1e-8; its greedy policy (keep-old) equals π_* at both. Cell 13 falls for four sweeps then turns at sweep 5 (shortest path to the goal is five moves).
- Ties: v_* is unique; the optimal policy is not (cells 9 and 12 tie). Stated in the lesson and in problem 2.

## Visuals (all rendered and inspected)

- Fig. 1 — greedy `max` backup at cell 14, inline SVG with theme variables, `min-width:34rem`, figure `overflow-x:auto`. Contrasts with lesson 1's expectation backup (averaged under π) in the caption.
- Fig. 2 — policy-iteration sequence π₀ → π₁ → π*, inline SVG grids with value heatmaps on one scale (lesson 1's grid-figure style), a chart-1 ring marking the flipped cell each round.
- Fig. 3 — policy-iteration vs value-iteration convergence, `nb chart` PNG (`chart-1.py` ships beside it), value of cell 13 against iteration count, with v_*(13) reference line. Caption notes a PI round is a full solve and a VI sweep is one cheap pass.
- One nb-table: per-cell v_π, v_*, gain for cells 8-15 (top rows 0-7 omitted, gain 0).
- nb-note with three problems, each answer in a `<details>`.

Rendered previews saved in the scratch dir (`fig_backup.png`, `fig_sequence.png`, `chart-1.png`); each was viewed. The two inline SVGs were previewed with theme variables mapped to the newsroom light palette (the responsive root `style` was stripped only for the standalone cairosvg preview; the published SVGs keep it).

## Proof result

`./nb check .../finding-optimal-policies.html --series reinforcement-learning --repo /home/user/the-nightly-build`

**verdict: PUBLISHABLE** (BLOCK: 0). Warnings, all non-blocking:
- `W-LENGTH-HIGH` 4071 words vs the 2000-3600 band. The lesson carries a full, runnable `control.py` listing plus its output and two multi-line derivations; the series prompt states the band is not strict and the template forbids shrinking an idea's explanation to hit a length. Flagging for the editor in case a trim is wanted; I judged the content load worth it.
- `W-SENTENCE-DENSITY` ×3: one is the telescoping-proof aligned equation (TeX punctuation, 83 "words"/score 70, inherent to the derivation); two are dense math sentences (Howard's linear-algebra proof statement; a worked-probability line). I split the prose offenders I could without fragmenting an argument.
- `W-SELF-COUNT` ×2 (sources/words still 0 in nb-meta): left for the orchestrator's `nb stamp`, per the brief ("Do not stamp counts by hand"). nb-meta `dek` and `title` match the rendered dekline and title exactly (the B-META-MATCH blocks are clear).

## Breaks from lesson 1's shapes (per the commission)

- Title: "Two improvements find the best policy" — a subject-verb-object claim with the number as the surprise, not lesson 1's "noun is a X you can Y".
- Dek: one plain sentence with this lesson's number ("lift cell 13 from −2.01 to −0.71, while the top half, already optimal, does not move"); no "and the X turns out to be" tail, no comma triad.
- Headings built differently from each other and from lesson 1 (no "X forces Y" / "Only X needs Y"): "What the hand-drawn arrows are worth", "Cell 14 would rather go right", "One greedy step is never a step down", "Evaluate, improve, repeat until the arrows stop", "A max in place of the average".
- Takeaway resolves this lesson's opener ("the hand-drawn policy was half right") and points to sampling; it does not reuse lesson 1's "I would remember the pair of them" first-person move.

## Sources (5; drawn from evidence.md, honoring its corrections)

s1 Sutton & Barto (q_π 3.13, improvement 4.7/4.8/4.9, PI §4.3, optimality 3.19, VI 4.10); s2 Howard 1960 **ch. 7** (discounted routine, keep-old tie rule ch. 4 p. 39); s3 Van Roy lec 06 (improvement Thm 3, finite-termination Thm 4); s4 Van Roy lec 05 (max-norm contraction Thm 1); s5 Bertsekas Abstract DP ch. 1 (max non-expansion, §1.2.2). AlphaGo Zero is described accurately in the Why bookend (search = improvement operator, self-play-with-search = evaluation, network trained to match both; "approximate policy iteration scheme") and linked in Go deeper — not cited as doing "evaluation by the network", and the Bellman 1957 journal paper is not cited for discounted optimality or policy iteration.
