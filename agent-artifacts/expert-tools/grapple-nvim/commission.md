# Commission: expert-tools/grapple-nvim

## Assignment
Cover **grapple.nvim**, the Neovim plugin that tags files by name and scope and
jumps back to them instantly, as the week's Neovim entry in the rotation. The
recent run has leaned Python and command-line (beartype, jujutsu, outlines,
atuin); the last Neovim pieces were grug-far (2026-08-07) and oil.nvim
(2026-07-29), so a Neovim navigation tool is the right rotation.

The subject is the tool and the work it changes: how a developer moves between
the handful of files a task actually touches, without the mental cost of
buffer lists, marks, or a fuzzy-finder round-trip.

## Angle and required contribution
Read past the README. Inspect the implementation and show the part that changes
the work: how grapple scopes tags (per git branch, per working directory, per
custom resolver), where it persists them, and how a name-addressed jump differs
from harpoon's ordered list, native marks, or `:b` buffer switching. Show one
concrete Neovim configuration and keymap that proves the value in use — tag a
file, jump to it by name across a scope change — not an installation tutorial.
Explain where it enters a workflow, what it replaces or enables, what adoption
costs, and whether its maintenance history makes it safe to depend on. Name the
tool and the work it changes in the headline and the section headings.

## Boundaries
- Template `article`: 1200-3000 words, 2-6 flex sections, per-section citation,
  minimum 6 sources. Sources: the repository, its documentation, commit and
  release history, maintainer notes, and real user configurations.
- The code example proves the tool's value; it does not become an install guide.
- If deep inspection shows grapple is thin or unmaintained enough that the piece
  cannot stand, the closest equally strong, easy-to-miss Neovim navigation
  plugin (for example arrow.nvim) is an acceptable pivot — record the reason in
  the draft handoff and flag it to the orchestrator before writing.

## Production record
- Correspondent (coach + research + draft + self-proof): model
  `claude-sonnet` tier, high effort for research.
- Editor (fresh eyes, required): model `claude-opus-4-8`, high effort.
- nb-meta: harness `claude-code-routine`, model `claude-opus-4-8`, date
  `2026-08-21`.
- Proof: `nb check .nb-work/expert-tools/grapple-nvim/library/expert-tools/grapple-nvim.html --series expert-tools --library /home/user/library-checkout`

## Recent patterns to break
The template sets the form; the back-catalog does not. Recent expert-tools pieces
have hardened into a mold — do not inherit it.
- Do not default to the fixed arc mechanism → worked example → comparison table
  → a two-column "what holds up / what to be careful about" box → a "Verdict"
  section. Let this tool's own material choose the sections and their order.
  A closing "Verdict" heading is not required and has become a formula.
- Headings: avoid the recurring wh-clause/gerund limitation heading ("What
  checking one item cannot promise", "Whether a one-maintainer decorator is safe
  to leave on", "Where the old rebase instincts still work").
- Dek: avoid the "X, which Y" and "the guarantee holds on A … and thins to B the
  moment C" hedge-contrast mold.
- Opener: avoid opening on a generalized definitional claim that then narrows.
- Maintenance caveat: avoid the "the project's own docs say so plainly" /
  "treat that as the tool's claim about itself" tic when reporting a self-stated
  metric.
