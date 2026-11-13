# Draft handoff: reinforcement-learning/observation-scale (writer 01)

## Main idea (27 words)

A gradient learner's single step size must suit its largest-scale input, so an
observation's units set how slowly the rest learns; standardizing each component
removes that dependence.

## Original work

The lesson builds Dock, one cart reported in metres or millimetres, derives from
E[xxᵀ] how the units set a linear learner's stable step size and pace, checks the
c² and κ predictions with runs, and then measures the same unit change leaving
PPO's policies blind to velocity until VecNormalize, with its statistics saved
and frozen, takes the units out.

## Proof

`nb stamp`, then the brief's `nb check` with links: BLOCK 0. One warning left on
purpose:

- W-CITE-DENSITY on `orientation`. The section is Dock's rules, a worked
  update and the 19-step return that dock.py prints. The series prompt says a
  section made of a derivation or a run on the page needs no citation.

## Code and checks (all under `writer/01/code/`, run with `uv run`)

Listings on the page, rerun exactly as printed after the last edit with
identical output: `dock.py` (→ `dock.out`), `linear.py` (→ `linear.out`, about 6 s),
`agents.py` (→ `agents.out`, 3 min 17 s on 4 cores). Figures come from
`figures/make_svgs.py`, which reruns linear.py's descent and reads the two
policy maps from `agents.out`; the SVGs were checked against both outputs and
inspected with `nb preview` plus Playwright at 390 px and 1280 px in light and
dark themes (no horizontal page scroll; two equations were split onto two lines
after they clipped on a phone). `assemble.py` fills `article.template.html` with
the listings, outputs and SVGs; edit the template and rerun it, or edit the
article directly.

Checks the series prompt asks for, for the editor to rerun:

1. **New seeds, PPO** (`checks/seeds5/`, `uv run agents.py 5`, output in
   `out.txt`). Raw millimetres: velocity used at 0 to 2% of grid positions in
   all five, 6 to 53% of episodes docked. Raw metres: 7 to 83%, 0 to 65% docked.
   Normalized: velocity used at 24 to 100%. Seed 7 fails in both normalized unit
   systems (0% and 1% docked) and metres-normalized seed 6 docks 45%; the rest
   dock 77 to 100%. Fresh statistics: four of five networks dock at most 9%,
   but seed 8 docks 67% (88% through its own statistics). The page states these
   conclusions without the numbers.
2. **New seeds, linear** (`checks/linear_checks.py`, start samples 1 to 3):
   κ in metres 32.9 to 34.2, in millimetres 8.7 to 9.1 million; the position
   eigenvalue ratio is 1,000,024 to 1,003,870; 0.99 × bound converges and
   1.01 × diverges; 74 to 77 steps to 1%. Unchanged conclusions.
3. **Worst case for the c² rule** (same script, every-visit states along
   scripted episodes, where position and velocity correlate and have nonzero
   means): the position eigenvalue grows 1.97 million times, not 10⁶, and
   standardized κ is 1.158 = (1 + |r|)/(1 − |r|) with r = −0.073. The page
   states the uncorrelated condition and "roughly c²" for the correlated case.
4. **Per-sample bound** (same script): per-sample gradient Monte Carlo in metres
   at α = 0.5, 1.0, 1.5, 1.9, all below the expected update's bound of 2. 1.9
   passes |w| = 10⁶ within 57 steps and 1.5 wanders (max |w| 814); the largest
   ‖x‖² is 1.89, so 2/‖x‖² = 1.06. This backs the page's sentence that a
   per-sample run must also suit the longest feature vectors.
5. **Removal tests on the page**: the standardized row of linear.py (units
   removed, κ = 1.03, one step); the two normalized PPO rows; the fresh
   statistics row (training statistics removed).
6. **Every policy map** (`checks/maps_all.py`): all five raw millimetre runs
   split the track at its centre; four push away from it, seed 1 toward it.
   Normalized policies push right below a speed that, in most runs, falls near
   the dock.
7. **Problem 1 arithmetic** (`checks/problem1.py`): eigenvalues 2.141, 0.127
   and 0.0297, κ 72.0, 2/λmax 0.934; standardized features identical to the
   centred ones.
8. **Not on the page**: Dock variants (dock speed 0.15 or 0.2, a 100-step
   limit, a 0.1 m/s push; `checks/variants/`) still leave about one seed in
   eight of normalized PPO undocked, so the original rules stay. A fixed
   rescaling by the observation bounds (`proto/ppo1.py`, `bounds-raw`) was as
   erratic as raw metres; the page makes no claim about it.

## Evidence handling

- Contradiction 7 (LeCun's 1/λmax against Goh's 2/(λmin + λmax)): the page
  names only Goh's step, as the one that minimizes the slowest factor, which is
  the step the runs use. LeCun's eq. 39 is not needed.
- Contradiction 8: the page says the runs apply the expected update, which
  2/λmax bounds, and that a per-sample run is held to 1 − α‖x‖². The page uses
  S&B 9.6 only for the rule of thumb.
- Contradiction 1, 2, 3, 4: stated as the decisions corrected them
  (`env.save` beside the model, flags reset after `load`, fresh wrapper at mean
  0 and variance 1, `update_running_mean` after construction, `norm_reward=False`).
- Contradiction 10: the formula is cited to vec_normalize.py; Huang et al.
  appears only in Go deeper.
- The torch pin (2.14.1) follows the published PPO lesson's listing; the
  evidence names SB3 2.9.2 and Gymnasium 1.4.0 only.

## Questions for the orchestrator

- Length. On the rendered page, with cards, headings, captions, tables and
  open problem answers in and code, output, equations, drawings, bands and
  sources out, I count 2,510 whitespace-separated words, 2,250 of them
  containing a letter (the rest are table and inline numbers). That is over
  the template's 2,200. Every remaining idea is one
  the commission or its decisions ask for. If the editor wants a whole cut, the
  candidates are the second problem, the NormalizeObservation paragraph, or the
  raw-metres row (the headline's comparison would then need rewording).
- nb-meta `model` is written as "claude-opus-5-5 (effort xhigh)". Say if the
  press records effort elsewhere.
