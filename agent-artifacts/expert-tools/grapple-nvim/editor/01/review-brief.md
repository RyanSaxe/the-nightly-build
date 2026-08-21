# Editor review brief: expert-tools/grapple-nvim (01)

Inputs:
- `../../editorial-direction.md` — the governing standard (editorial, slop, headlines, press voice, template identity, series prompt).
- `../../commission.md` — the assignment, boundaries, required contribution, and the recent patterns to break.
- `../../writer/01/brief.md` and `../../writer/01/draft-handoff.md` — what the writer was asked for and what it decided (read the handoff for any pivot or open question).
- `../../researcher/01/evidence.md` — the sourced evidence the prose must not outrun.
- The article: `.nb-work/expert-tools/grapple-nvim/library/expert-tools/grapple-nvim.html`.

Proof: `./nb check .nb-work/expert-tools/grapple-nvim/library/expert-tools/grapple-nvim.html --series expert-tools --library /home/user/library-checkout`

## Recent patterns to catch (a formula shows only across issues)
- The last five expert-tools pieces settled into: mechanism → worked example →
  comparison table → a two-column "what holds up / be careful" box → a "Verdict"
  section. Confirm this draft does not reinstate that mold, and that its
  headings are not the recurring wh-clause/gerund limitation headings ("What
  checking one item cannot promise", "Whether … is safe to leave on").
- Dek: reject the "X, which Y" / "the guarantee holds on A … thins to B the
  moment C" hedge-contrast mold.
- Reject the "the project's own docs say so plainly" / "treat that as the tool's
  claim about itself" tic around a self-stated metric.

## Round focus
Fresh-eyes read at high effort. Cut slop against `spec/slop.md`, hold the
headline/dek/headings to `spec/headlines.md`, and verify every claim is carried
by the evidence record and a resolving citation (this is a tool piece — check
that the code example proves the tool's value and is not an install tutorial,
and that the maintenance-health claims match what the sources actually show).
Fix prose, structure, and documented furniture in place. Route back to the
writer only for something needing new prose or new evidence.
