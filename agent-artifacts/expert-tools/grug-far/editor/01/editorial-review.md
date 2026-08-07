# Editorial review: expert-tools/grug-far (editor/01)

## Skeptic

Thesis: grug-far.nvim's one real distinction is that a project-wide ripgrep
search opens as a single editable Neovim buffer, and a Sync command writes your
hand-edits back across every file — a move `:s`, `:cdo`/`:cfdo`, quickfix
replace, and a shell `rg | sed` pipe do not offer, and one the ast-grep engine
drops. The claims it stands on: (1) the default replacement engine is ripgrep's
own `--replace`, not sed; (2) the edit-results-and-sync move is ripgrep-engine
only; (3) capture syntax is `$1`/`${1}`, never `\1`; (4) the tool is actively
maintained (latest tag 1.6.76, 2026-07-28); (5) the honest costs are the
dependency set and the `maxSearchMatches` cap.

Technical correctness was the top risk, so I checked every mechanism descriptor
against the evidence record and the researcher's flagged corrections:

- **No sed engine / ripgrep default.** "The default engine is ripgrep itself"
  (s2) matches `opts.lua` `engine = 'ripgrep'`. "the source carries no sed
  anywhere" (s3) matches the evidence note that `ripgrep/replace.lua` contains
  no `sed`. Held.
- **Engine menu.** "one of the three engines the default configuration enables
  alongside a rules variant" (s2) matches `engines = { 'ripgrep', 'astgrep',
  'astgrep-rules' }`. Held — no sed backend described anywhere.
- **Sync is ripgrep-only, disabled under multiline.** "Sync is a ripgrep-engine
  feature; the ast-grep engine ships no sync path at all" (s6, s1) and "ripgrep
  engine only, and disabled even there under `--multiline` and
  `--multiline-dot-all`" (s1) both match the README verbatim quotes and the
  astgrep directory listing (no `sync.lua`). Held.
- **Capture syntax.** `(\w+)Service` → `${1}Client`; "`$1` or `${1}`... a named
  `$word`... `$0` for the whole match... never sed's `\1`" (s4) matches the
  ripgrep GUIDE.md record exactly. The underlying command
  `rg --replace='${1}Client' --passthrough` (s1) matches the README quote. Held.
- **ast-grep command.** `ast-grep run --pattern='$A && $A()' --rewrite='$A?.()'
  --update-all` (s5, s6) matches the evidence's getArgs/replace assembly and the
  worked example C. Held.
- **Version / maintenance.** Tag 1.6.76 dated 2026-07-28, "ten days before this
  was written" (article date 2026-08-07 — arithmetic checks) (s7); latest commit
  same day (s8); empty Releases tab noted as not-abandonment; two open issues
  filed 2026-08-04, ~2,000 stars, single maintainer (s9, s10). All match the
  record.
- **Dependencies / guard.** Neovim >= 0.11.0 (tag 1.6.3 for 0.10); ripgrep
  required (14+, 15 rec); ast-grep optional (0.36+); `maxSearchMatches` = 2000
  with the freeze-avoidance reasoning (s1, s2). All match.

Worked buffer listing (Fig. 1), checked line by line: the `:GrugFar` open, the
bare `TODO` search, the `file:line` result lines, the delete-to-skip annotation,
and `<localleader>s` as Sync All all match the evidence keymap table
(`syncLocations = <localleader>s`) and example B. It is a hand-built listing, not
a lifted screenshot, and carries no install boilerplate — it opens on the pivot
and shows the state change. Legitimate per the voice guide's example license.

Display text, descriptor by descriptor: headline claim (search → editable buffer
→ sync back) is true; dek claims (delete drops from write; edit rewrites the
line) are true and finer-grained than the headline; the attribution "Stephan
Badragan" matches the maintainer profile (s10); every section subhead states a
true step. `data-nb-kind` audit: all ten sources are first-party or claim-owning
(plugin source, ripgrep's own GUIDE, GitHub tags/commits/issues/profile), so
`primary` is correct throughout; no independent secondary is needed or hidden.
Citation hrefs match the evidence source URLs one-for-one.

No break survived. Every load-bearing claim traces to a primary source, and the
premise the commission got wrong (a sed default) is correctly retired in the
prose. Nothing routes to the researcher.

## Cut

The piece is lean and mostly earns its place. Four surgical fixes made (see
Edits). Two are craft breaks (a comma splice, a self-referential/prompt-echo
clause), two reduce a repeated tell.

Worst tell: the article leans on the "not X" contrast far past the standard's
one-or-two-per-piece ceiling. Counting the earned contrasts — "not after," "not
a transient quickfix list but," heading "not a replace field," heading "not
sed," "never sed's `\1`" — the correction is real in each case (the commission
itself believed the sed story), so none is an invented strawman, but the
frequency reads as a drumbeat. I cut the weakest instance ("text, not after,"
redundant with "before you see"); the load-bearing ones (ripgrep-not-sed is a
section's whole argument) stay. The writer should recast one or two of the
remaining contrasts to declaratives when the headings are reworked.

Prompt-echo / self-reference: "is the thing prose cannot show" was lifted from
the evidence record's editorial aside and narrates the article's own medium. Cut
to "is what the quickfix path does not offer," keeping the substantive quickfix
contrast.

ast-grep boundary: the paragraph draws the line cleanly (ast-grep is the
matcher, grug-far the surface that drives it, sync does not come with it), but a
mid-sentence clause — "so it binds to the parse tree and skips look-alikes
inside strings and comments" — re-treads the 2026-07-24 ast-grep piece, whose
own dek was "binds to the parse tree, not the text, so it skips every
look-alike... inside a comment, a string." Cut, which also relieves an
overlong sentence. The boundary survives intact.

Repeated pattern named: heading cadence. Three of the five section headings hang
two clauses on a comma — "What Replace runs, **and** why it is ripgrep, not
sed," "Swapping in ast-grep, **and** where the buffer stops," "What it costs,
**and** whether to trust it" — the exact "clause, and clause" drumbeat the
headline standard flags. Varying this well is a coherent rewrite past a clause,
so it routes to the writer rather than a piecemeal cut.

Furniture: the code listing, the holds-up grid, and the one `nb-note-strong`
verdict each carry cargo (the pivot demonstration, the central tradeoff, the
weighed recommendation). Three components across 1,306 words reads as a
continuous article, not a stack. No furniture cut; none missing — the source
asset the writer declined (a README screenshot) is rightly declined, because a
hand-built listing shows the move more honestly than a third-party capture with
personal editor chrome, and the standard only requests an asset when an exact
visual lets the reader test a central argument better than prose.

## Reader

Read straight through, the piece gives what the sources scattered: the single
boundary that the edit-and-sync buffer is a ripgrep-engine feature the ast-grep
engine simply drops, staged at the pivot so the reader watches the state change.
That is the original-work sentence from the handoff, and the article delivers it
— the synthesis (grug-far's one real distinction, and where it degrades to a
diff-previewing front end) is not in any single source. The prose sits closer to
the voice-guide exemplars than a median summary: it concedes limits flat
(ripgrep-only sync, the 2000 cap, a maintainer count of one) in Gallant's
anti-pitch register, then presses the case. The headline as largest claim is
true and defended; its only fault is form, not fact.

## Edits

- Cut ", not after" from the `:cdo`/`:cfdo` sentence (redundant contrast; trims the "not X" drumbeat).
- Cut "the thing prose cannot show and" → "is what the quickfix path does not offer" (self-reference / prompt-echo from the evidence aside).
- Fixed comma splice: "userService becomes userClient, authService becomes authClient" → inserted "and".
- Cut "so it binds to the parse tree and skips look-alikes inside strings and comments" from the ast-grep sentence (re-tread of the 2026-07-24 ast-grep piece; also relieves an overlong sentence).
- Ran `./nb stamp` after the cuts: words 1306, reading 6 min, sources 10.

## Required work

- **writer** — Recast the headline. "grug-far **turns** a project-wide search
  **into** an editable buffer" inherits the exact "[Tool] turns [X] into [Y]"
  frame of the immediately preceding piece, visidata (2026-08-05: "VisiData
  **turns** each new question about a table **into** a keystroke"); against the
  recent shelf it reads stamped. Find grug-far's own surprise verb. The headline
  and dek also live in the `nb-meta` block and the `<title>`, so update all
  three and re-run the proof.
- **writer** — Vary the section-heading cadence. Three of five headings use
  "clause, and clause"; break the shape without inheriting a prior piece's
  structure. Recast one or two of the surviving "not X" contrasts to declaratives
  in the same pass to bring the piece under the contrast ceiling.

## Decision

revise — the article is technically flawless and analytically strong, but the
headline inherits the prior piece's construction and the section headings repeat
one cadence, both display/structure formulas that belong to the writer.
