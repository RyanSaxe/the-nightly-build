# Evidence record: expert-tools/grug-far (01)

The evidence strongly supports the core commission: grug-far.nvim is a live,
in-editor project-wide find-and-replace surface where matches from ripgrep (or
ast-grep) render into one editable Neovim buffer, and edits made to the result
lines are written back across files. Every mechanism claim below is verified
against the plugin's own source, not the README prose: the ripgrep engine
replaces via `rg --replace=... --passthrough`, the ast-grep engine drives
`ast-grep run --pattern= --rewrite= --update-all`, the default keymaps and the
`maxSearchMatches` cap come straight from `opts.lua`, and the "edit the results
and sync" feature lives only in the ripgrep engine's `sync.lua`. Maintenance is
healthy and dated: latest tag 1.6.76 on 2026-07-28, weekly-to-fortnightly
commits, a single maintainer (Stephan Badragan / "MagicDuck") plus outside
contributors, ~2,000 stars, two open issues both opened 2026-08-04.

The record is thin in three honest places, all recorded under Contradictions:
(1) the commission's premise that **sed is the default replacement engine is
wrong** — there is no sed engine; the three engines are `ripgrep` (default),
`astgrep`, and `astgrep-rules`, and the writer must not describe a sed backend;
(2) the signature "edit results as text and sync to disk" feature is
**ripgrep-engine only** — ast-grep and multiline replacement both disable it;
(3) GitHub's Releases tab is empty, so "release history" must be read from
version **tags**, not Releases. On the central editorial question: grug-far is
substantial and clearly distinct from ast-grep (2026-07-24). Its center of
gravity is the interactive buffer/sync model over ripgrep regex, not ast-grep;
ast-grep is one optional engine of three, boundable to a single paragraph.

## Sources

```text
URL:         https://github.com/MagicDuck/grug-far.nvim/blob/main/README.md
Kind:        primary — the plugin's own documentation, authored by the maintainer.
Establishes: What the tool is; the requirements list; the Replace-vs-Sync
             distinction in the maintainer's own words; the ripgrep-only sync
             limit; the GrugFar / GrugFarWithin commands; the diff preview.
Paraphrase:  A Neovim find-and-replace plugin. Search uses the full power of rg
             or ast-grep; replace uses almost the full power of either. Results
             open in one buffer; supplying a replacement shows a diff before
             applying. Sync writes hand-edits in the results area back to files.
Locators:    Requirements section; "Sync vs Replace" note; Commands section.
Quote:       Requirements (verbatim): "Neovim >= 0.11.0 (please use tag 1.6.3
             for nvim 0.10) - BurntSushi/ripgrep >= 14 supported, >= 15
             recommended - a Nerd Font (optional) - ast-grep (optional) if you
             would like to use the ast-grep search engine. Version >= 0.36
             recommended. - either nvim-web-devicons or mini.icons for file
             icons support (optional)".
             Sync vs Replace (verbatim): "Essentially the difference is that
             Replace runs `rg --replace=... --passthrough` on each file and does
             not depend at all on what's in the results area. Sync All does a
             line by line sync based on what's in the results area."
             Sync limit (verbatim): "sync is only supported by ripgrep engine";
             "When you do multi-line replace with --multiline and
             --multiline-dot-all flags, sync won't work so you have to use
             replace."
```

```text
URL:         https://github.com/MagicDuck/grug-far.nvim/blob/main/lua/grug-far/opts.lua
Kind:        primary — the default configuration and keymap table, source of truth.
Establishes: The exact default keymaps; the default engine; the enabled engine
             list (which contains no sed); the search limits and their reason.
Paraphrase:  Default engine is 'ripgrep'; enabled engines are
             { 'ripgrep', 'astgrep', 'astgrep-rules' }. minSearchChars = 2,
             maxSearchMatches = 2000, maxWorkers = 4. All keymaps are
             <localleader>-prefixed and buffer-local.
Locators:    defaultOptions table: keymaps, engine, engines, minSearchChars,
             maxSearchMatches, maxWorkers.
Quote:       Keymaps (verbatim): replace = { n = '<localleader>r' },
             qflist = { n = '<localleader>q' }, syncLocations = { n =
             '<localleader>s' }, syncLine = { n = '<localleader>l' },
             close = { n = '<localleader>c' }, historyOpen = { n =
             '<localleader>t' }, historyAdd = { n = '<localleader>a' },
             refresh = { n = '<localleader>f' }, openLocation = { n =
             '<localleader>o' }, openNextLocation = { n = '<down>' },
             openPrevLocation = { n = '<up>' }, gotoLocation = { n = '<enter>' },
             abort = { n = '<localleader>b' }, help = { n = 'g?' },
             toggleShowCommand = { n = '<localleader>w' }, swapEngine = { n =
             '<localleader>e' }, previewLocation = { n = '<localleader>i' },
             swapReplacementInterpreter = { n = '<localleader>x' },
             applyNext = { n = '<localleader>j' }, applyPrev = { n =
             '<localleader>k' }, syncNext = { n = '<localleader>n' },
             syncPrev = { n = '<localleader>p' }, syncFile = { n =
             '<localleader>v' }, nextInput = { n = '<tab>' }, prevInput = { n =
             '<s-tab>' }.
             maxSearchMatches comment (verbatim): "stops search after this
             number of matches as getting millions of matches is most likely
             pointless and can even freeze the search buffer sometimes".
```

```text
URL:         https://github.com/MagicDuck/grug-far.nvim/blob/main/lua/grug-far/engine/ripgrep/replace.lua
Kind:        primary — the ripgrep engine's replacement implementation.
Establishes: The default engine replaces using ripgrep itself, NOT sed. The
             module builds rg args (via getArgs) with the --replace= flag and
             writes replaced content back to each matched file. A custom
             replacement interpreter (lua/vimscript) can compute per-match
             replacement text, which is then fed through rg's replacement path.
Locators:    replace.lua and sibling getArgs.lua / replaceInMatchedFiles.lua;
             the directory also contains sync.lua (the results-edit sync path).
Quote:       No occurrence of "sed" anywhere; replacement flows through
             ripgrep's native --replace=.
```

```text
URL:         https://github.com/MagicDuck/grug-far.nvim/blob/main/lua/grug-far/engine/astgrep/getArgs.lua
Kind:        primary — the ast-grep engine's argument builder.
Establishes: How grug-far drives ast-grep. Single-pattern mode: `ast-grep run`
             with `--pattern=<search>` and, when a replacement exists,
             `--rewrite=<replacement>`; `--color=never` always; `--heading=always`
             for search; `--globs=` per file-filter line (ast-grep > 0.27.x).
             Rules mode ('astgrep-rules'): `ast-grep scan` with
             `--inline-rules=<yaml>`. Replacement metavariables (e.g. $A) are
             ast-grep's own syntax passed straight through.
Locators:    getArgs.lua flag assembly; astgrep/replace.lua for --update-all.
Quote:       Flags built: "--pattern=", "--rewrite=", "scan", "--inline-rules=",
             "--color=never", "--heading=always", "--globs=".
```

```text
URL:         https://github.com/MagicDuck/grug-far.nvim/blob/main/lua/grug-far/engine/astgrep/replace.lua
Kind:        primary — the ast-grep engine's apply step.
Establishes: On Replace, the engine runs ast-grep with '--update-all' (applies
             the rewrite to files in place), then re-reads and overwrites each
             changed file; for a buffer range it appends '--stdin' (and
             '--lang=<language>') and streams with '--json=stream'. There is NO
             sync.lua in the astgrep engine directory (files: argUtils,
             blacklistedReplaceFlags, blacklistedSearchFlags, getArgs,
             getAstgrepVersion, parseResults, replace, search), confirming the
             README claim that sync is ripgrep-only.
Locators:    astgrep/ directory listing; replace.lua extraArgs = '--update-all'.
Quote:       "--update-all", "--stdin", "--lang=", "--json=stream".
```

```text
URL:         https://github.com/MagicDuck/grug-far.nvim/tags
Kind:        primary — the project's own version tags (the real release record).
Establishes: Maintenance cadence and latest version. Tags are frequent patch
             bumps on the 1.6.x line.
Locators:    Tags list, newest first.
Quote:       1.6.76 (2026-07-28), 1.6.75 (2026-07-21), 1.6.74 (2026-07-12),
             1.6.73 (2026-07-10), 1.6.72 (2026-06-23), 1.6.71 (2026-06-05),
             1.6.70 (2026-05-19), 1.6.69 (2026-05-14), 1.6.68 (2026-04-27),
             1.6.67 (2026-04-11).
```

```text
URL:         https://github.com/MagicDuck/grug-far.nvim/commits/main
Kind:        primary — the commit log.
Establishes: Active, ongoing development. Most recent commit 2026-07-28
             ("make center on navigation configurable"). Commits cluster in
             sprints, roughly weekly to fortnightly, over the whole period
             sampled (Apr–Jul 2026). Outside contributors (r4ppz, null-sleep,
             akioweh) land PRs that MagicDuck commits.
Locators:    main branch commit history.
Quote:       Latest commit dated 2026-07-28.
```

```text
URL:         https://github.com/MagicDuck/grug-far.nvim/issues
Kind:        primary — the issue tracker.
Establishes: A small open backlog. Two open issues at time of research, both
             opened 2026-08-04: #599 "Function for prefills.search" and #598
             "More than one match on same line" (both by user kocv59). A low
             open count against active commits is consistent with responsive
             triage; I did not measure median response time.
Locators:    Open issues list.
Quote:       2 open issues, #598 and #599, both 2026-08-04.
```

```text
URL:         https://github.com/MagicDuck
Kind:        primary — the maintainer's GitHub profile (identity).
Establishes: The maintainer's real name for correct attribution. "MagicDuck"
             is Stephan Badragan. grug-far.nvim is his most-starred repo
             (~2,000 stars); 39 public repos.
Locators:    Profile header and pinned/popular repos.
Quote:       Name: "Stephan Badragan".
```

```text
URL:         https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md
Kind:        primary — ripgrep's own guide, owner of the --replace semantics.
Establishes: The capture-group syntax the grug-far ripgrep engine inherits.
             Replacement strings use $1, $2 (index) and $name (named groups);
             $0 is the whole match. This is the Rust regex crate syntax, so it
             differs from sed: the search pattern has no backreferences, and
             replacement uses $1 / ${1}, not \1.
Locators:    "Replacements" section of GUIDE.md.
Quote:       "Our replacement string here, fast-$1, consists of fast- followed
             by the contents of the capturing group at index 1." Named form:
             "rg 'fast\s+(?P<word>\w+)' README.md -r 'fast-$word'".
```

```text
URL:         (prior coverage, read for differentiation, not cited as fact)
             expert-tools/ast-grep, published 2026-07-24, via
             `nb history --library /home/user/library-checkout --show expert-tools/ast-grep`
Kind:        secondary — the paper's own back catalogue, used to draw the line.
Establishes: The ast-grep piece framed ast-grep as a standalone Rust/tree-sitter
             CLI matcher-and-rewriter ($PROP && $PROP() -> $PROP?.() across the
             TypeScript compiler; single-quote gotcha; YAML `sg scan` rules).
             The grug-far angle must NOT re-teach structural matching; it teaches
             the in-editor results buffer and the edit-and-sync surface, and
             names ast-grep as one selectable engine grug-far can drive.
Locators:    Full article text.
Quote:       n/a (differentiation source).
```

## Contradictions

- **Commission premise vs. reality: there is no sed engine.** The commission
  and subject brief describe replacement as "sed by default, with ast-grep and
  ripgrep's own --replace selectable." The source contradicts this flatly.
  `opts.lua` sets `engine = 'ripgrep'` and `engines = { 'ripgrep', 'astgrep',
  'astgrep-rules' }`. The default ripgrep engine replaces with
  `rg --replace=... --passthrough` (README, verbatim) and its `replace.lua`
  contains no reference to sed. The writer must present the default as
  ripgrep's own replace, and the three engines as ripgrep / ast-grep /
  ast-grep-rules. Any sentence built on a sed backend is factually wrong. (This
  is likely a stale mental model: some earlier find/replace plugins shelled out
  to sed; grug-far does not.)

- **README's headline feature vs. its own fine print: sync is ripgrep-only.**
  The tool's signature move — hand-edit the result lines, then write those exact
  edits back — is available only in the ripgrep engine. The astgrep engine
  directory has no `sync.lua`; the README states "sync is only supported by
  ripgrep engine," and sync is additionally disabled under `--multiline` /
  `--multiline-dot-all`. So the "edit the results as text" story does not hold
  for the ast-grep engine, where you instead use the Replace field + Replace
  action (`ast-grep ... --update-all`). This is the true boundary of the feature
  and should be stated, not glossed.

- **Empty Releases tab vs. active tag stream.** GitHub's Releases page reads
  "There aren't any releases here," which could be misread as an unmaintained
  project. The real release record is the tag stream (1.6.76 on 2026-07-28,
  frequent 1.6.x bumps). Cite tags, and the LuaRocks package, for versioning —
  not the Releases tab.

- **Replace vs. Sync All are usually equivalent, with one exception.** README:
  if you do not edit the results list, "Sync All and Replace have equivalent
  outcomes," except that multiline replacement forces Replace. The distinction
  the article rests on (results-as-buffer) only bites when you actually edit the
  result lines; otherwise the two paths converge. State this honestly rather
  than implying sync is always the different path.

## Numbers

```text
Figure: Neovim >= 0.11.0 required (tag 1.6.3 for nvim 0.10)
Owner:  README Requirements section (primary)
Scope:  Hard runtime requirement of current main / 1.6.x.
```

```text
Figure: ripgrep >= 14 supported, >= 15 recommended; ast-grep >= 0.36 recommended (optional)
Owner:  README Requirements section (primary)
Scope:  ripgrep is mandatory (search backend); ast-grep only if that engine is used.
```

```text
Figure: maxSearchMatches = 2000 (default)
Owner:  opts.lua defaultOptions (primary)
Scope:  Search stops after 2000 matches to avoid freezing the buffer; can
        overshoot slightly. This is the concrete "huge result set" failure-mode
        guard the brief asks about.
```

```text
Figure: maxWorkers = 4; minSearchChars = 2 (defaults)
Owner:  opts.lua defaultOptions (primary)
Scope:  Concurrency cap for file replacement; minimum typed chars before a
        search fires.
```

```text
Figure: 3 search/replace engines (ripgrep default, astgrep, astgrep-rules)
Owner:  opts.lua engines list (primary)
Scope:  The full engine menu. No sed.
```

```text
Figure: Latest tag 1.6.76, dated 2026-07-28; latest commit 2026-07-28
Owner:  Tags page and commit log (primary)
Scope:  10 days before the article's working date (2026-08-07). Weekly-to-
        fortnightly cadence across Apr–Jul 2026.
```

```text
Figure: ~2,000 GitHub stars; 2 open issues (both 2026-08-04); 1 primary maintainer
Owner:  Repo / profile / issues pages (primary)
Scope:  Adoption and backlog snapshot at research time.
```

## The part that changes the work (for the writer, exact keys)

Two concrete demonstrations, both verified against source. The first is the
signature move (distinct from ast-grep); the second draws the ast-grep line.

```text
A. Capture-group replace across files, ripgrep engine (default), no sed:
   :GrugFar                      -> opens the split; cursor in Search field
   Search:      (\w+)Service     (ripgrep regex; a capturing group)
   Replace:     ${1}Client       (ripgrep/Rust syntax: $1 or ${1}, NOT \1)
   -> results render in the buffer, each match shown with a live diff of the
      replacement.
   <localleader>r  (replace)     -> runs rg --replace='${1}Client' --passthrough
                                    per file, writing every site.
   Expected: userService -> userClient, authService -> authClient, etc., across
   all matched files at once. Contrast with :s + :cdo/:cfdo (per-buffer, no
   project-wide preview) and with a shell rg | sed pipe (fire-and-forget, no
   review surface).
```

```text
B. The signature: edit the RESULTS as text, then sync to disk (ripgrep only):
   :GrugFar
   Search:      TODO
   -> every TODO line in the project appears as an editable line in one buffer.
   Now hand-edit individual result lines (fix wording on some, delete the line
   for matches you want to skip).
   <localleader>s  (syncLocations / "Sync All")
   -> writes exactly your edited lines back to their source files, line by line
      (Sync All depends on the results area; Replace does not). Deleting a
      result line simply excludes that match from the write. This is the thing
      prose cannot show and ast-grep has no equivalent for.
```

```text
C. Draw the line to ast-grep (one paragraph), same buffer, different engine:
   <localleader>e  (swapEngine)  -> switch to the astgrep engine
   Search (pattern): $A && $A()
   Replace (rewrite): $A?.()
   <localleader>r
   -> runs ast-grep run --pattern='$A && $A()' --rewrite='$A?.()' --update-all,
      the same structural rewrite the 2026-07-24 piece did on the CLI, but now
      previewed as a diff inside the editor. Note the boundary: with the astgrep
      engine, sync (edit-the-results) is OFF; you use the Replace field.
   The line to draw: ast-grep (2026-07-24) is the standalone matcher/rewriter;
   grug-far is the interactive surface that can DRIVE it, and whose real
   distinction is the ripgrep-backed edit-and-sync buffer, not structural
   matching.
```

## Source assets

```text
Asset: The grug-far results buffer itself — the split showing Search / Replace /
       Files / Flags input fields at top and the per-file, per-line match list
       with an inline replacement diff. Screenshots/GIFs live in the README of
       github.com/MagicDuck/grug-far.nvim.
Shows: The whole thesis in one image — search results are an editable text
       buffer with a live diff, not a transient quickfix list.
Crop:  A crop must retain the input fields AND at least two files' worth of
       match lines with the diff coloring; it may omit surrounding editor chrome
       (tabline, statusline) that identifies a personal setup.
```

```text
Asset: A before/after code listing (the natural furniture per the commission):
       the four-line input block (Search / Replace / one flag) beside the git
       diff it produces across files. Built from example A or C above, not
       lifted from a screenshot.
Shows: The exact transform and that it lands across multiple files at once.
Crop:  Keep the input fields and 2-3 representative diff hunks from different
       files; omit unchanged context lines.
```

```text
Asset: None found for maintenance claims — cite tags/commits/issues as text,
       not images.
```

## Discarded

```text
URL: https://github.com/MagicDuck/grug-far.nvim/releases — empty ("There aren't
     any releases here"). Not evidence of abandonment; the project versions via
     tags. Used only to explain the empty-Releases contradiction, not as a fact
     source.
```

```text
URL: https://raw.githubusercontent.com/MagicDuck/grug-far.nvim/main/doc/grug-far.txt
     — the help doc fetched is largely a generated mirror of the README intro
     and did not add engine/limit detail beyond the README and source; verified
     specifics against opts.lua and the engine modules instead.
```

```text
URL: dotfyle.com / neovimcraft.com / luarocks.org listings — secondary
     directory/aggregator pages. Useful only to confirm packaging (LuaRocks:
     magicduck/grug-far.nvim) and star count; all substantive claims taken from
     the repo itself.
```
