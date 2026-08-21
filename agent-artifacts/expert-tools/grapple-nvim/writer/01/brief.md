# Writer brief: expert-tools/grapple-nvim

## Angle taken

The piece is built around one technical fact the commission specifically
asked for: a name-addressed tag resolves through a scope, and switching
the scope (most sharply, switching git branch under the `git_branch`
scope) changes which file the name points to without changing the keymap
or the name itself. Every section either sets that fact up, proves it, or
draws a consequence from it.

## Section order and why

1. **Orientation** — the everyday problem (buffer list, marks, `:b`) with
   no persistent name, then Grapple's fourth option and its scoping catch.
2. **How a scope decides what a name means** — the resolver contract, six
   built-in scopes, `git_branch`'s exact logic, caching, and the
   "any function with this shape" generality (custom resolver).
3. **Tag by name, jump by name** — the required nb-code listing (a real
   lazy.nvim spec, not an install tutorial) plus the proof scenario: tag
   `hot` on one branch, tag a different file `hot` on another branch,
   show the jump resolving differently. This is the section that actually
   demonstrates the commission's required proof ("tag a file, jump to it
   by name across a scope change").
4. **A name outlives its position** — the analytical payoff: index vs.
   name addressing at the data-structure level, contrasted against
   harpoon's ordered list, native Neovim marks, and `:b`. This is the
   "how does a name-addressed jump differ" half of the commission.
5. **Old branches keep their tag files** — adoption cost: one JSON file
   per resolved scope, no automatic pruning, one-tag-per-path-per-scope
   as a habit to unlearn coming from harpoon.
6. **The commits stopped in 2024** — maintenance trust, dated and cited,
   closing on an earned synthesis rather than a labeled Verdict note.

## Furniture used, and what was deliberately not used

- One `nb-code` figure (section 3): the required config/keymap proof.
- One `nb-stat-strip`, two stats (section 6): months since last commit,
  months since last merge, replacing what the last several pieces did
  with a holds-up grid and a Verdict note.
- No `nb-table`. The scope comparison and the grapple/harpoon/marks
  contrast are relationships (why an index shifts and a name doesn't),
  not a spec-sheet of parallel rows, so they stayed in prose. Four of the
  five most recent expert-tools pieces used a table; this one doesn't
  need one to carry its evidence.
- No holds-up grid, no Verdict note. The closing section's own prose
  carries the weight-of-evidence judgment.

## Pivot

None. See researcher/01/brief.md, "Pivot check." grapple.nvim's source
carries the piece; the maintenance stall (last commit September 2024, last
merge May 2024, an open unmerged fix for a live Neovim 0.12 compatibility
bug reported April 2026) became the sharpest part of the argument rather
than a reason to abandon it.

## Proof result

`./nb stamp` then `./nb check ... --series expert-tools --library
/home/user/library-checkout`: BLOCK 0, WARN 0, verdict PUBLISHABLE, on the
final pass. First pass caught one blocking error (`nb-meta` mode was
`collection`, series expects `open`) and four warnings (two dense
sentences, a citation-order mismatch between the persistence and
lookup-table sources, and an all-caps stat-strip label reading as an
unfilled placeholder). All four addressed: `mode` corrected, both
sentences split, source numbering reordered to match first appearance,
stat labels rewritten to keep any single caps run under four words (the
project's own placeholder-detection threshold).

Final counts: 1,637 words, 10 sources, 7-minute read.
