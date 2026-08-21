# Editorial review: expert-tools/grapple-nvim (01)

## Decision

APPROVED. No required change remains. Three direct edits made; nothing routed
to the writer.

## What I verified

The maintenance-trust section carries the piece, so I checked its claims
against the sources rather than the evidence digest alone.

- Last commit `b41ddfc`, 2024-09-29, "chore(docs): auto generate docs":
  confirmed on the local clone (`git -C /home/user/cbochs/grapple.nvim log -1`).
- git_branch resolver walks up for `.git`, shells out
  `git symbolic-ref --short HEAD`, and joins `string.format("%s:%s", root,
  branch)`: confirmed in `lua/grapple/settings.lua`. Cache on
  `{"BufEnter","FocusGained"}`, debounce 1000ms: confirmed. Six scopes with the
  stated fallbacks: confirmed.
- `TagContainer:find` precedence index -> name -> path, with `names_index` a
  separate table populated in `insert` and cleared in `remove`: confirmed in
  `lua/grapple/tag_container.lua`. The article's claim that a name lookup
  "never changes shape just because a different tag was removed" is exact.
- Issue #197 / PR #198, opened 2026-04-03, still open, no maintainer reply:
  confirmed by fetching both threads. Only `maxrzaw` has commented on #198. The
  sentence "Neither has drawn a reply from the maintainer" holds.
- Stat-strip arithmetic (23mo since Sept 2024, 27mo since May 2024) is right
  against the 2026-08-21 dateline.

Every claim the argument rests on is carried by the evidence record and a
citation that resolves; citation numbers follow order of first appearance. The
code listing proves the tool in use (tag by name, jump across a branch switch),
not installation.

## The mold is broken

Confirmed against the recent expert-tools record. The last several pieces
(beartype, grug-far) close on a two-column holds-up grid plus a Verdict note
and a wh-clause limitation heading ("What checking one item cannot promise",
"Whether a one-maintainer decorator is safe to leave on"). This draft uses no
table, no holds-up grid, no Verdict note; its six headings run six different
constructions and none opens on What/Whether/Where. The maintenance report is
built from commit hashes and an issue number, not the self-report tic the
commission flagged.

## Direct edits

1. **Dek, rewritten.** The old dek said "Each tag's cursor position lands in
   its own JSON file keyed to the resolved scope" — but Grapple writes one file
   per scope holding all that scope's tags, not one file per tag. It also tied
   "a branch switch" to "harpoon's four numbered slots quietly pointing at new
   files," which conflates two separate arguments: harpoon's slots drift when
   the list is reordered or pruned, not when a branch changes, and harpoon has
   no branch scope for a switch to touch. New dek: "The git_branch scope gives
   each branch its own tag file on disk, so checking out another branch loads a
   different set of names under keymaps that never change." It states the
   mechanism accurately and adds to the headline instead of restating it.

2. **Section 4 heading.** Removed the trailing period on "Deleting a tag never
   renumbers the names around it" — the only heading of six carrying one.

3. **Section 1 close.** Cut "That's the part worth reading past the README for."
   It graded the material and added nothing after the surprise it followed. The
   section now ends on "Switch branches, and the same name can resolve to a
   different file," which is where the argument actually lands.

## Proof

`./nb stamp` then
`./nb check .nb-work/expert-tools/grapple-nvim/library/expert-tools/grapple-nvim.html --series expert-tools --library /home/user/library-checkout`:

```
BLOCK: 0
WARN:  0
verdict: PUBLISHABLE
```

Final: 1,621 words, 10 sources, 7-minute read. Within the article template's
bands (1200-3000 words, 2-6 flex sections, 6+ sources).
