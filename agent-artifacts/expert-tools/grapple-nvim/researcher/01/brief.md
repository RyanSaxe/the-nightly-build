# Researcher brief: expert-tools/grapple-nvim

## Question this piece has to answer, past the README

The commission requires three specific technical facts, each verified
against source, not the marketing copy:

1. How does grapple.nvim's scope system actually decide "which project"
   a tag belongs to — the resolver contract, the six built-in scopes, and
   specifically what the `git_branch` resolver does that `git` doesn't.
2. Where tags persist, and what a name-addressed lookup does differently
   from an index-addressed one at the data-structure level.
3. Whether the project is maintained well enough, right now, to depend on
   for real work — measured in commit and merge dates, not adjectives.

## What was read, not just fetched

The repository was cloned in full (`/home/user/cbochs/grapple.nvim`,
`git clone https://github.com/cbochs/grapple.nvim`) rather than relying on
WebFetch summaries for anything load-bearing. Read directly from the
checkout: `README.md` in full, `lua/grapple/settings.lua` (default scope
resolvers, `prune` setting), `lua/grapple/state.lua` (JSON persistence,
`path_encode`/`save_path`), `lua/grapple/tag_container.lua` (`insert`,
`remove`, `find` — confirmed index-then-name-then-path lookup precedence
and the separate `names_index` hash table), `lua/grapple.lua` and
`lua/grapple/app.lua` (public API signatures for `tag`, `select`,
`untag`, `find`, confirmed the `grapple.options` type includes `name`).
`git log`, `git tag`, and `git shortlog` on the clone confirmed the exact
last-commit hash and date independent of any GitHub UI rendering.

WebFetch was used for GitHub-hosted pages that aren't in the git history
(issues, pull requests, the commit's own permalink for confirmation) and
for harpoon's README and Neovim's own `:h mark-motions` documentation,
which live in other repositories.

## Key findings, with where they came from

- Six default scopes (`global`, `static`, `cwd`, `lsp`, `git`,
  `git_branch`), each a resolver function returning `(id, path, err)`,
  with `lsp → git → cwd` and `git_branch → cwd` fallback chains. Source:
  `lua/grapple/settings.lua`, `default_scopes` table.
- `git_branch`'s resolver walks up for `.git`, then runs
  `git symbolic-ref --short HEAD` and builds the id as
  `string.format("%s:%s", root, branch)`. Source: same file.
- `git` and `git_branch` scopes cache on `{"BufEnter","FocusGained"}`
  with a 1000ms debounce, so the resolver isn't re-run on every keystroke.
  Source: same file.
- Tags persist as one JSON file per resolved scope id, URL-encoded into a
  filename, in `stdpath("data")/grapple` by default, written on every
  mutation via `State:write`. Source: `lua/grapple/state.lua`.
- `prune` defaults to `"30d"` and only runs when explicitly invoked; it is
  not a background timer. Source: `lua/grapple/settings.lua`.
- `TagContainer:find` checks `opts.index` first, then `opts.name` (via a
  dedicated `names_index` hash table built in `insert`/`remove`), then
  `opts.path`. A name lookup never depends on list position. Source:
  `lua/grapple/tag_container.lua`.
- Only one tag survives per path per scope; re-tagging a path overwrites
  the existing tag's name rather than adding a second entry. Source:
  README "Grapple.tag" section, confirmed against `TagContainer:insert`'s
  "Attempt to clear the 'path' tag and 'name' tag" step.
- harpoon2's setup wires keys directly to `list():select(1..4)`; its own
  README states the list can hold any number of items but documents no
  name-based lookup. Source: `ThePrimeagen/harpoon`, `harpoon2` branch
  README.
- Neovim marks: lowercase marks are buffer-local, uppercase ("file")
  marks persist via `'shada'`, 26 letters available per case. Source:
  Neovim's own `motion.txt`, `mark-motions` section.
- Maintenance timeline, all confirmed directly on GitHub, not inferred:
  - Last commit to `main`: `b41ddfc`, September 29, 2024 (doc
    regeneration).
  - Last merged pull request: #164, merged May 18, 2024 (highlight
    groups).
  - Issue #197, opened April 3, 2026: `vim.validate` table-form syntax
    deprecated under Neovim 0.12, breaking compatibility with the
    positional form needed for Neovim 0.10; names the three affected
    files.
  - Pull request #198, opened the same day (April 3, 2026): fixes #197,
    tested against Neovim 0.10.4, 0.11.4, and 0.12.0. Still open,
    unmerged, no maintainer comment, as of research date.
  - 715 stars, 18 open issues, 10 open pull requests at time of research.

## What was checked and set aside

- dotfyle.com's per-plugin config-count page was checked for an adoption
  figure comparable to harpoon's. The page did not yield a reliable
  aggregate number on inspection (individual per-user "mentions" only,
  no total), so no adoption-count claim from it made the draft.
- A fork (`danjessen/grapple.nvim`) surfaced in search results as a
  possible sign of continued community development. Not pursued or
  cited: the canonical repository's own issue/PR history already
  supplies concrete, dated, primary evidence for the maintenance
  question, and chasing a fork would widen the piece's claim ("is
  grapple.nvim maintained") into a different one ("is some fork of it
  maintained") that the commission didn't ask for.

## Pivot check

Considered and rejected. grapple.nvim's own source gives a real, specific,
citable answer to every piece of the required contribution (scope
resolution, persistence, name-vs-index addressing, adoption cost). The
maintenance stall is real and is reported plainly with hard dates, but it
does not make the tool too thin to carry the piece — if anything it gives
the piece a sharper, more specific closing argument than a clean "actively
maintained" story would have. No pivot to arrow.nvim or any other
navigation plugin was necessary. See writer/01/draft-handoff.md.
