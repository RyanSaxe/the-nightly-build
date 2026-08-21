# Evidence log: expert-tools/grapple-nvim

Each entry: claim used in the draft → source → what was actually read.

1. **"A tag is a persistent pointer to a file path... saved with the
   cursor position, so a jump lands on the line you left."**
   `github.com/cbochs/grapple.nvim/blob/main/README.md`, "Tags" section:
   "A tag is a persistent tag on a file path or URL... When a file is
   tagged, Grapple will save your cursor location so that when you jump
   back, your cursor is placed right where you left off." Read in full via
   the local clone, `README.md` lines ~760-766.

2. **Six default scopes, resolver contract, fallback chains.**
   `lua/grapple/settings.lua`, `DEFAULT_SETTINGS.default_scopes` table.
   Read the full table: `global`, `static`, `cwd`, `lsp` (fallback `git`),
   `git` (fallback `cwd`), `git_branch` (fallback `cwd`).

3. **`git_branch` resolver: walks up for `.git`, shells out to
   `git symbolic-ref --short HEAD`, builds `"%s:%s"` (root, branch).**
   Same file, `git_branch.resolver` function body, quoted verbatim in the
   draft's prose description (not reproduced as a code listing, since the
   piece's one code listing is reserved for the reader-facing config).

4. **Caching: `git`/`git_branch` cache on `{"BufEnter","FocusGained"}`,
   debounce 1000ms.** Same file, `cache = { event = {...}, debounce = 1000
   }` fields on both scope definitions.

5. **Custom scope example (`$HOME`-keyed, four lines).**
   `README.md`, "Scopes" section, "Define and use a custom scope" example
   block.

6. **`Grapple.tag`/`Grapple.select` accept a `name` option; API
   signatures.** `lua/grapple/app.lua`, `grapple.options` class comment
   (`@field name? string`) and `App:tag`/`App:select` functions.
   Cross-checked against `README.md`'s "Grapple API" section, which
   documents `:Grapple tag ... name={name}`.

7. **Per-scope JSON persistence, filename = url-encoded scope id, written
   on every mutation.** `lua/grapple/state.lua`, `State:save_path`
   (`Path.join(self.save_dir, string.format("%s.json", path_encode(name)))`)
   and `State:write`.

8. **`prune` default `"30d"`, invoked explicitly, not a timer.**
   `lua/grapple/settings.lua`, `prune = "30d"` field and its doc comment;
   `lua/grapple/state.lua`, `State:prune(limit_sec)` (only runs when
   called).

9. **Only one tag per path per scope; re-tagging overwrites the name.**
   `README.md`, `Grapple.tag` section: "only one tag can be created per
   scope per file. If a tag already exists for the given file or buffer,
   it will be overridden." Confirmed against
   `lua/grapple/tag_container.lua`, `TagContainer:insert`, the "Attempt to
   clear the 'path' tag and 'name' tag" step before insertion.

10. **`TagContainer:find` precedence: index, then name (via
    `names_index`), then path.** `lua/grapple/tag_container.lua`,
    `TagContainer:find` function body, read directly; confirmed
    `names_index` is a separate table populated in `insert`/cleared in
    `remove`, independent of list position.

11. **Harpoon: `list():select(1..4)` keymaps, unlimited list length, no
    documented name lookup.** `github.com/ThePrimeagen/harpoon`,
    `harpoon2` branch `README.md`, "Basic Setup" example and feature list.

12. **Neovim marks: lowercase buffer-local, uppercase persisted via
    `'shada'`, 26 letters per case.** `neovim.io/doc/user/motion.html`,
    `mark-motions` section (mirrors `runtime/doc/motion.txt` in the
    Neovim repository).

13. **Last commit `b41ddfc`, September 29, 2024, "chore(docs): auto
    generate docs."** Confirmed two ways: `git log -1` on the local clone
    (`git -C /home/user/cbochs/grapple.nvim log -1`) and the commit's own
    GitHub permalink,
    `github.com/cbochs/grapple.nvim/commit/b41ddfc1c39f87f3d1799b99c2f0f1daa524c5f7`.

14. **Last merged PR #164, May 18, 2024, "add grapple window highlight
    groups."** `github.com/cbochs/grapple.nvim/pull/164`: "Merged commit
    dd7fd96 into cbochs:main [May 18, 2024]."

15. **Issue #197, opened April 3, 2026: `vim.validate` table-form
    deprecated under Neovim 0.12, breaks Neovim 0.10 compatibility if
    switched to positional form; names `scope_manager.lua`,
    `tag_container.lua`, `tag_manager.lua`.**
    `github.com/cbochs/grapple.nvim/issues/197`, read in full.

16. **PR #198, opened the same day, fixes #197, tested against Neovim
    0.10.4/0.11.4/0.12.0, still open.**
    `github.com/cbochs/grapple.nvim/pull/198`, read in full.

17. **715 stars, 18 open issues, 10 open pull requests.**
    `github.com/cbochs/grapple.nvim` repository home page, read directly
    for the current counts at research time.

All ten URLs cited in the article's Sources section were confirmed to
resolve at time of writing and passed `nb check`'s link and citation-order
checks with zero warnings on the final pass.
