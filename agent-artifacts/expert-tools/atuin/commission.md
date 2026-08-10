# Commission: expert-tools/atuin (2026-08-10)

## The tool and the work it changes

Atuin replaces the shell's default history. Instead of appending lines to a flat
`.bash_history`, it records each command as a row in a local SQLite database with
context the flat file throws away: the working directory, exit status, duration,
session, and hostname. That turns Ctrl-R from a substring scroll into a query,
and it adds an optional end-to-end-encrypted sync that carries one searchable
history across machines. The work it changes is command recall for anyone who
lives in a terminal and has ever lost a command they know they ran last month.

Show the part that actually changes the workflow with a concrete shell example:
the interactive search that replaces Ctrl-R, and a filtered `atuin search` query
that uses the context the flat file cannot (for example, "commands that failed
in this directory"). The example proves the tool's value; it is not an
installation walkthrough. Name Atuin and the work it changes in the headline and
in the section titles.

## Boundaries

- The reader is a terminal-native engineer. Assume shell fluency; do not explain
  what Ctrl-R is beyond the one line that frames the comparison.
- Explain where Atuin enters the workflow, what it replaces or enables, what
  adopting it costs (the shell hook it installs, the behavior changes to up-arrow
  and Ctrl-R, the daemon/database, the trust question of a sync server even with
  end-to-end encryption), and whether it is maintained well enough to trust.
- Read past the README: inspect how it stores and searches history, the shell
  integration, the sync/encryption design, and the real maintenance record.

## Required contribution

The article does something the docs do not: it shows, on a concrete example, what
the recorded context (directory, exit code, duration) lets a user ask that a
flat history cannot answer at all, and it weighs honestly whether that capability
is worth the shell hook and the daemon for this reader. A feature tour is not the
contribution.

## Template and furniture

Template: `article`. Use `nb-code` / `nb-code-head` for the shell example, as the
beat's pieces do. Reach for furniture only where a command or a comparison is
clearer shown than told.

## Recent expert-tools habits not to inherit

Recent pieces (files-to-prompt, grug-far, oil-nvim) each headline with the
tool name and a present-tense verb describing its mechanism, which is the right
shape for this beat — but vary the construction rather than copying their rhythm.
Two of the three close on a maintenance-and-trust section with a heading built
from a stat or the maintainer count ("Seventeen months quiet, two hundred
installs a day", "One maintainer ships every release for a plugin with 6,800
stars", "What it costs, and whether to trust it"). Cover maintenance and trust,
because the prompt requires it, but do not reuse that closing heading mold or the
install-count-in-the-headline device.

## Sources

Minimum 6 sources. Prefer the primary record: the project repository, its
documentation site, the source itself for the storage and sync design, release
history and issue tracker for the maintenance judgment. Verify the encryption and
sync claims against the project's own description, not third-party summaries.

## Runtime

Harness `claude-code-routine`; model Opus 4.8 for every role. Production policy
asks researcher/high, writer/medium, writing-coach/low, editor/high (required).
Per-invocation reasoning effort is not separately settable through this runtime's
child launches, so each role runs at the session's effort; the editor gate is
preserved in full. Writer records `harness: claude-code-routine` and
`model: Opus 4.8` in nb-meta.
