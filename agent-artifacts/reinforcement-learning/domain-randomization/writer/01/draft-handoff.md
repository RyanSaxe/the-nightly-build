# Writer handoff: reinforcement-learning/domain-randomization (01)

## Main idea (30 words)

When a physical parameter drawn each episode is hidden, the best policy is one
policy for the whole range, which loses return wherever the best move depends on
the parameter.

## Original work

The literature measures the cost of a hidden parameter only with trained deep-RL
policies, and the lesson turns it into an exact computation: LoadedDock's load
changes only the dock's reward, so the best blind policy is the optimum of one
averaged Dock, which value iteration solves and Q-learning reaches.

## Proof

`nb check ... --series reinforcement-learning --repo /home/user/the-nightly-build`
(links checked): BLOCK: 0, WARN: 3, verdict PUBLISHABLE.

Warnings left on purpose: W-CITE-DENSITY on `averaged-dock`, `who-pays` and
`q-learning`. Those sections are a derivation and the lesson's own runs, which
the series prompt says need no citation.

Prose, counted on the rendered page as the template defines it, is about 2,230
words with the section headings and about 2,185 without. That is at the 2,200
line. To get there I cut a third problem, the Yu/Xie literature paragraph, the
EPOpt hopper sentence in "who pays", a Chen sentence on memory and a
check_env sentence. Yu and Chen remain in Go deeper.

## Design decisions the commission left open

- The load's mass does not change the motion: the drive holds each push at
  1 m/s². With a push of 1/m m/s², one push from rest already puts the loads in
  different states, so a table keyed on (x, v) partly sees the mass, and the
  cost of hiding it can't be isolated or solved exactly. With the mass acting
  only at the dock, every policy's average over loads equals its return in one
  averaged Dock, even for policies with memory. Problem 2 asks what changes if
  the push did depend on the mass.
- The rule is a buffer that stops a cart only if ½mv² ≤ 0.5 J, which gives each
  load its own speed limit (1.00, 0.71, 0.58, 0.50 m/s for 1 to 4 kg).
- Decisions last 0.1 s (Dock(0.1), the same physics as RepeatAction of 10 at
  0.01 s), so the state stays on a 5 mm by 0.1 m/s grid and a table keyed on
  the exact state needs no cells. The return is undiscounted, which makes costs
  read in seconds and lets qlearn.py run unchanged.
- Start fixed at rest at x = 0.2. It gives a graded cost (0.22, 0.14, 0.08,
  0.00 s) and paths of one switch for 1 and 2 kg. The 3 kg and 4 kg best paths
  include one right push during braking, which is optimal at 0.1 s decisions.
  The page explains the 4 kg case.

## Checks (rerun from `.nb-work/reinforcement-learning/domain-randomization/scratch/`)

dock.py and qlearn.py there are rebuilt from the `nb history --show` text of
the action-frequency and frame-stacking lessons, with indentation restored. To
rerun as a reader would, copy the published files.

1. **Seeds.** `uv run train.py --runs 10 11 12 13 14 15 16 17 18 19` (output
   in `train_10_19.out`): every run's greedy returns are identical to runs 0-9
   for every load. At the parting state, the braking estimates and the
   1/2/3 kg pushing estimates match exact.py to two decimals again. The hidden
   push estimate is −1.49 (runs 0-9: −1.51; exact −1.47), and the 4 kg push
   estimate is −2.29 (runs 0-9: −2.27; exact −2.36). Every run ranks the moves
   as exact.py does.
2. **Hidden push estimate.** A throwaway run (seeds 0-4) at 20k/40k/80k
   episodes gave per-run values from −1.38 to −1.98, with means of −1.53, −1.59
   and −1.59. The estimate doesn't settle on the exact value within these
   budgets, so the page states only that the two estimates differ by up to 0.09
   and that the agents push there only when they explore. It doesn't say why.
3. **Training budgets.** Hidden mass: 10k episodes gave 6/10 runs with exact
   greedy returns, and 20k gave 10/10. Observed mass, ε = 0.1: 30k 0/10, 50k
   7/10, 70k 10/10. With ε = 0.2, 30k gave 0/10 and 50k 8/10. I chose 20k and
   80k. `uv run train.py` took 242 s with a second run in parallel ("about four
   minutes" on the page).
4. **Other starts (cells) for result 1.** `uv run exact.py --start X V` for
   (0.1, 0), (0.3, 0), (0.4, 0), (0.5, 0), (0.2, 0.5) and (0.6, 1.0): each time
   the cost is 0.00 at 4 kg and doesn't shrink toward the light end (3 kg is
   0.00 where it shares the 4 kg path). At (0.9, 0) the cost is 0.00 for every
   load, because even pushing all the way arrives at 0.45 m/s and no load's best
   move depends on its mass. The page limits the "light end" statement to the
   x = 0.2 start.
5. **Removal test (on the page).** `uv run exact.py --no-limit`: every load's
   best policy pushes right all the way, and the cost is 0.00 for 1 to 6 kg. In
   LoadedDock the mass then does nothing, and the page says so.
6. **Worst-fit case.** At `--start 0.8 1.0` no load heavier than 1 kg can be
   saved. "The policy brakes for the heaviest load" fails there: it brakes for
   the 1 kg load, and the cost (0.03 s) falls on the doomed heavy loads.
   Problem 1 covers this.
7. **Training range.** `--masses 1 2 3 4 5 6`: the policy follows the 6 kg
   path (0.40 m/s, 1.60 s), no load crashes, and the 1 kg cost rises to 0.31 s.
   `--masses 1 2`: the policy follows the 2 kg path, the 1 kg cost is 0.07 s,
   and 3-6 kg crash. These support "safe only up to the heaviest load it was
   built from".
8. **Gymnasium 1.4.0.** check_env passes LoadedDock with both observations. A
   reset that indexes `options["mass"]` raises KeyError under check_env, which
   is why reset uses `get`. A mass drawn from a separate generator passes
   check_env always with the mass hidden, and in 4 of 6 tries with it observed.
   The page therefore doesn't claim the checker catches that mistake.
9. **Float boundary.** Some best paths arrive exactly at a limit (the 5 kg load
   at √0.2 m/s, the 1 kg load at 1.00 m/s from x = 0.5). loads.py compares the
   energy with a 1e-9 tolerance, as dock.py's hit() does for time.

## Open questions

- Evidence: with the Yu, Xie, RMA and Chen material cut for length, the body
  cites only Tobin, EPOpt and CAD2RL (history), Peng (per-episode draws and
  sim-to-real) and the Gymnasium reset docs. If the editor wants a published
  case where hiding the parameter costs return, Yu et al. Fig. 2(b) is the
  candidate, but adding it would cost words over the cap.
- Voice: none.
