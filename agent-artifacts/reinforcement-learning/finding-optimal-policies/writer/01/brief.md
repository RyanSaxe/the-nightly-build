# writer brief: reinforcement-learning/finding-optimal-policies (01)

Inputs:
- `../../editorial-direction.md` — the full standing editorial standard.
- `../../commission.md` — what this lesson teaches, the finding, boundaries, visuals, and the recent-pattern notes to break.
- `../../writing-coach/01/voice-guide.md` — how the piece sounds.
- `../../researcher/01/evidence.md` — the anchored sources; cite from here.
- The article file to write into (already initialized, do not recreate its skeleton):
  `/home/user/the-nightly-build/.nb-work/reinforcement-learning/finding-optimal-policies/library/reinforcement-learning/finding-optimal-policies.html`
Output: `draft-handoff.md` (write it beside this brief) AND the finished article HTML at the path above.
Proof: `/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/finding-optimal-policies/library/reinforcement-learning/finding-optimal-policies.html --series reinforcement-learning --repo /home/user/the-nightly-build`

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me (the
orchestrator). You may read the engine/press/template furniture catalogs
referenced by the editorial direction for the exact HTML of a furniture
component, and lesson 1's published HTML for its grid-figure style, but take
your content from the inputs above.

## Run the code for real

Every number, grid, and figure in the lesson must come from a run that actually
happened. Reuse lesson 1's gridworld **unchanged** so results compare directly.
Create a scratch run directory (outside the `library/` tree, e.g. under
`/tmp/claude-0/.../scratchpad/rl2/`), write `gridworld.py` there with the exact
source below, write your new `control.py` importing from it, and run with
`uv run control.py` (uv is installed; inline script metadata pulls numpy). The
published lesson shows your new code and links lesson 1 for `gridworld.py`; it
does not reprint the whole of `gridworld.py` (quote only the few helpers you
call if useful).

`gridworld.py` (verbatim from lesson 1 — recreate exactly, including indentation):

```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""A slippery 4x4 grid as arrays. Cells are 0 to 15, row by row from top."""
import numpy as np

N = 16
GOAL, PIT = 3, 6
TERMINAL = [GOAL, PIT]
ARROWS = "^>v<"  # the actions up, right, down, left are numbered 0, 1, 2, 3
STEPS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# R[s'] is the reward for arriving in s'.
R = np.full(N, -1.0)
R[GOAL], R[PIT] = 10.0, -20.0


def draw(rows):
    """A policy drawn as rows of arrows. Terminal cells, ".", get action 0."""
    return np.array([max(ARROWS.find(arrow), 0) for arrow in rows.split()])


# The fixed policy, written by hand.
PI = draw(""">  >  >  .
^  ^  .  ^
^  ^  >  ^
^  ^  ^  ^""")

# The same policy with the bottom row pressed against the bottom wall.
STUCK = draw(""">  >  >  .
^  ^  .  ^
^  ^  >  ^
v  v  v  v""")


def move(s, a):
    """The cell reached by moving as intended. An edge leaves s in place."""
    row, col = s // 4 + STEPS[a][0], s % 4 + STEPS[a][1]
    return 4 * row + col if 0 <= row < 4 and 0 <= col < 4 else s


def transitions(slip):
    """P[s, a, s'], with all-zero rows for the terminal cells."""
    P = np.zeros((N, 4, N))
    for s in set(range(N)) - set(TERMINAL):
        for a in range(4):
            P[s, a, move(s, a)] += 1 - slip
            P[s, a, move(s, (a + 1) % 4)] += slip / 2
            P[s, a, move(s, (a + 3) % 4)] += slip / 2
    return P


def fixed_policy(policy, slip):
    """Q, the policy's moves among non-terminal cells, and b, the expected
    one-step reward from each cell. Terminal rows and columns of Q are zero."""
    P_pi = transitions(slip)[np.arange(N), policy]
    Q = P_pi.copy()
    Q[:, TERMINAL] = 0.0
    return Q, P_pi @ R
```

(That is the subset you need: `transitions`, `fixed_policy`, `draw`, the
constants. The `episode`/`discounted`/`radius` helpers from lesson 1 are not
needed here; you may omit them from your recreated file or keep them.)

Facts about the grid that make the code easy to get right:
- A length-16 value vector `v` holds 0 at the two terminal cells (GOAL=3,
  PIT=6). Then the action value is `q(s,a) = P[s,a] @ (R + gamma * v)` — exactly
  the one-step form lesson 1 used for its cell-5 backup. Arriving-reward `R[s']`
  plus discounted next value, averaged over the slip.
- Policy evaluation of a deterministic policy: `Q, b = fixed_policy(pi, slip)`
  then `v = np.linalg.solve(np.eye(16) - gamma*Q, b)` (lesson 1's direct solve).
- Greedy policy: `pi_new[s] = argmax_a q(s,a)` for non-terminal s.
- Value iteration: `v_next[s] = max_a P[s,a] @ (R + gamma*v)` for non-terminal
  s, terminal stays 0; iterate to a stated max-norm tolerance.
- Use slip 0.2 and gamma 0.9 (lesson 1's setting) as the headline run so cell 13
  and the values line up with lesson 1.

Report in `draft-handoff.md` the exact console output you got, and base every
figure and sentence on it. If a result surprises you (e.g. the number of policy
iterations, or whether the greedy policy of VI equals PI's), report what the run
actually showed.

## What to write

Follow `commission.md`'s short list of ideas, finding, boundaries, and visuals,
and the voice guide. Structure: the `why` bookend (write last), an orientation
section, 3-4 flex sections that are the argument's steps, the `takeaway` bookend
(write last), and Sources. Target the 2000-3600 word band (code counts; the
series is not strict, so clarity wins over hitting the band exactly, but do not
sprawl). Break the recent-pattern shapes listed in the commission: a title and
dek built differently from lesson 1's, headings built differently from each
other and from lesson 1's, and a takeaway that does not reuse lesson 1's
first-person "I would remember" move.

Visuals: draw the greedy `max` backup as inline SVG (theme variables, aria-label,
`style="width:100%;min-width:34rem;height:auto"`, figure `overflow-x:auto`);
show the policy-iteration sequence as grids with value heatmaps in lesson 1's
established style; and a figure comparing policy iteration and value iteration
converging. For computed heatmaps/curves you may use `nb chart` (run
`/home/user/the-nightly-build/nb chart --help` first). Define every RL term on
first use. End the body with an `nb-note` of two or three problems answerable
from the lesson alone, each with its answer and working inside a `details`
element.

Citations: every non-bookend section carries at least one cite to a Sources
entry drawn from `evidence.md` (min 4 sources). Bookends carry no citations.
Keep the `nb-meta` JSON and the fixed chrome lines intact; fill title, dek,
date (2026-11-01), and the body. Do not stamp counts by hand — the orchestrator
runs `nb stamp`.

Run the proof yourself before handing off, and report its result in
`draft-handoff.md`. In `draft-handoff.md` also state, in one sentence, the
original work this lesson does (per the editorial standard). Meet `spec/slop.md`
throughout, and test every section's first and last sentence and the article's
last sentence hardest.
