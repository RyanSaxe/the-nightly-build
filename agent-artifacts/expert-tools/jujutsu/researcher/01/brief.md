# researcher brief: expert-tools/jujutsu (01)

Inputs:
- ../../editorial-direction.md — citation standard, declared reader, series territory
- ../../commission.md — the tool, the workflow change to prove, the honest-cost and maintenance judgment required

Output: ./evidence.md

Establish, from sources you open (prefer primary: the project's own docs, code,
and design documents):
- The model that makes the workflow change: the working copy as a commit, the
  `@` working-copy revision, the absence of a staging area and automatic
  snapshotting, the operation log and `jj undo` / `jj op restore`, and how the
  Git backend and colocated (`jj git init --colocate`) repositories work. Cite
  the official documentation and, where the reasoning matters, the design docs.
- A concrete, verified command sequence that demonstrates the value on a real
  repository: reordering or splitting commits, amending an older commit, or
  recovering from a botched rebase with `jj undo`. Record the exact commands and
  their observable effect, verified against current `jj` behavior and version,
  not reconstructed from memory. Note the `jj` version the behavior reflects.
- First-class conflicts: how a conflict is recorded in a commit rather than
  halting the operation, and what the user does next. Enough to support a
  section if the writer needs it.
- The honest costs: Git-interop and colocated-repo caveats, workflow habits that
  do not transfer from Git, current maturity and stability, and the maintenance
  picture (who owns it, backing, release cadence, contributor activity), from
  the repository history and release record.

Search for what breaks the "adopt it" angle: documented sharp edges, data-loss
or interop footguns, and credible practitioner complaints. Record them in
Contradictions. Meeting the six-source floor means six sources that change the
picture, not padding.
