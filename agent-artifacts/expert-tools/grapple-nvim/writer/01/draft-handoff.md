# Draft handoff: expert-tools/grapple-nvim

## Status

One draft, self-proofed clean. `nb check` verdict: PUBLISHABLE, 0 blocking
errors, 0 warnings, on the version currently at
`.nb-work/expert-tools/grapple-nvim/library/expert-tools/grapple-nvim.html`.

## Pivot

**Not taken.** grapple.nvim was inspected past the README (settings.lua,
state.lua, tag_container.lua, app.lua, the full commit and PR history) and
found strong enough, on its own code and its own timeline, to carry every
piece of the required contribution: scope resolution including a custom
resolver, persistence, name-vs-index addressing against harpoon and native
marks, adoption cost, and a maintenance-trust judgment. The maintenance
story turned out to be a stall rather than abandonment or thinness — last
commit September 29, 2024; last merged PR May 18, 2024; a still-open,
tested fix (PR #198) for a Neovim 0.12 compatibility bug reported April 3,
2026 (issue #197). That's read as material for the piece's sharpest
section, not as a reason to reach for arrow.nvim.

## Proof of the required contribution

The commission asked for one concrete config and keymap that tags a file,
then jumps to it by name across a scope change. Section 3
(`tag-by-name-jump-by-name`) does this directly: the `nb-code` listing sets
`scope = "git_branch"` and wires `<leader>mm`/`<leader>mj` to
`Grapple.tag({name=...})`/`Grapple.select({name=...})`; the prose
immediately after walks through tagging `internal/limiter.go` as `hot` on
one branch, tagging a different file `hot` on `main`, and the same keymap
resolving to a different file depending on which branch was checked out
when it ran. That's the scope-change proof, not an install tutorial — the
listing is eleven lines of config the reader would actually keep, not a
step-by-step of `:Lazy sync`.

## What changed under self-proofing

- `nb-meta.mode` was `collection` in the initial draft; the series
  registry expects `open` (matched against every other expert-tools
  article's `nb-meta`). Fixed.
- Two sentences flagged for density (40+ words, 2+ clause joins) were
  split: one in the scope-resolution section (the `git_branch`/caching
  paragraph), one in the marks paragraph of the addressing-comparison
  section, which was genuinely overloaded (three clauses joined across a
  semicolon and two `and`s) and reads better broken up regardless of the
  proof tool.
  the `state.lua` citation (persistence, first used in section 3) was
  numbered after the `tag_container.lua` citation (lookup precedence,
  first used in section 4). Swapped `s3`/`s4` throughout, including the
  Sources list, to match order of first appearance.
- The stat-strip labels ("SINCE THE LAST COMMIT", "SINCE THE LAST MERGE")
  read as unfilled all-caps placeholders under the proof's four-word
  threshold. Rewritten to embed the actual date inline
  ("SEPT 2024, LAST COMMIT" / "MAY 2024, LAST MERGE"), which also makes
  each label carry a fact instead of a category, matching how the
  jujutsu piece's stat strip is built.

## Recent patterns broken, specifically

No `nb-table`. No holds-up grid. No `nb-note-strong` "Verdict." Six
headings, six different constructions (comma-and, single declarative,
colon-lead, plain statement, plain statement, semicolon contrast) with none
opening on What/Whether/Where. No self-report hedge about the maintainer's
own claims, because none of the maintenance material comes from the
project's self-description; it's commit hashes, merge dates, and an issue
number.
