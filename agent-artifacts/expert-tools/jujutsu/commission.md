# Commission: expert-tools/jujutsu

## The tool and the work it changes

The tool is **Jujutsu (`jj`)**, the Git-compatible version-control system built
by Martin von Zweigbergk and others. It qualifies: it is easy to miss (most
engineers have never left Git), and it changes a workflow every one of them runs
many times a day. It backs onto a Git repository, so the claim is not "replace
Git" but "drive the same repository through a different model of what a change
is."

The article picks the one part of that model that most changes the daily work
and proves it on a small, real example. The strongest candidate is the pairing
that makes rewriting history safe: the working copy is itself a commit that `jj`
snapshots automatically (there is no staging area and no separate "dirty tree"),
and every command is recorded in an operation log that `jj undo` / `jj op
restore` can roll back. Together they turn the operations engineers avoid in Git
out of fear (interactive rebase, reordering or splitting commits, amending an
older commit, recovering after a botched rebase) into cheap, reversible moves.
First-class conflicts, where a conflict is recorded in a commit instead of
halting the operation, are the second candidate and may earn a section if the
example needs it. Let the writer choose the single sharpest demonstration; do
not tour the whole feature list.

## Boundaries and required contribution

- Read past the README, per the series prompt. The evidence must reflect the
  actual model (working-copy commit, the `@` revision, the op log, the Git
  backend and colocated-repo behavior), drawn from the official docs, the design
  documents, and real practitioner writeups, not a features blurb.
- Show the change in a small shell example that proves the value: a sequence a
  reader could run where `jj` does in a couple of commands what Git makes slow or
  frightening, and where `jj undo` recovers from a mistake. The example proves
  the tool; it is not an installation tutorial.
- Be honest about the cost of adopting it: the Git-interop and colocated-repo
  caveats, the parts of the muscle memory that stop transferring, the maturity
  and stability state, and whether the project is maintained well enough to
  trust (ownership, release cadence, backing). The series requires this
  judgment, not a recommendation.
- Name the tool and the work it changes in the headline and the section titles.
- Word band 1200–3000; min 6 sources.

## Recent expert-tools habits not to inherit

- The dek has become a fixed shape: the tool's headline capability, then a
  caveat that undercuts it. "thins to the provider's own feature the moment you
  point it at a hosted API", "the encryption that syncs it covers less than the
  word suggests", "it still can't run a match statement or import itertools",
  "the free backend ... is narrower than the 40-language banner suggests." The
  caveat belongs in the body's honest-cost section. Write a dek that states this
  tool's actual surprise, and do not reach for the capability-then-caveat mold.
- Recent picks rotated Python (outlines), CLI (atuin), Neovim (grug-far); a VCS
  is a clean change of family, so nothing structural should echo those pieces.

## Production record

- Template: article (engine). Series: expert-tools (open). No `--tag`.
- Source floor: min 6 (article template).
- Production policy (balanced): coach capable/low, researcher capable/high,
  writer capable/medium, editor inherit/high (required). Actual: coach,
  researcher, writer on a capable model (Sonnet class); editor on the inherited
  model (Opus class). No required directive traded down.

## This edition (neighboring articles, for coherence)

Runs alongside two daily news briefs (current-events, tech-news), an investing
lesson (enterprise value to equity value per share), a Chinchilla-paper
reconstruction, an unbiased AI-copyright piece, and a word-of-the-day. This is
the edition's hands-on engineering piece; keep it concrete and tool-first, and
leave AI-industry framing to the other desks.
