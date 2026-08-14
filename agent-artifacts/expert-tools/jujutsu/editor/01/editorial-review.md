# Editorial review: expert-tools/jujutsu (editor/01)

## Skeptic

**Thesis.** In Jujutsu the working copy is already a commit and every command
is written into one operation log, so undoing a mistake means pointing back at a
recorded operation rather than reconstructing history. The piece proves it by
typing a wrong rebase destination and recovering the exact pre-mistake commit
IDs with one `jj undo`.

The claims it stands on, and how each held:

- **The demonstration reproduces the evidence with nothing invented.** I laid
  the article's code listing (the `jj log` / `jj rebase -s uomvmzxo -d root()` /
  `jj undo` / `jj log` sequence) beside the researcher's verified Demo B line by
  line. Every change ID, commit ID (`01a1182e`, `c323dd04`, `4a46c9d1` before;
  `cdc6bf8c`, `a7677b0a` after the rebase), operation ID (`88b3604a313c`,
  `e7af953a3da7`) and command message matches. The article strips the
  `researcher@example.com … 06:59:05` author/timestamp columns from the `jj log`
  blocks; that is an omission, not an invention, and the evidence columns (the
  IDs) are retained intact. `config.py` gone from disk, `removed 1 files`, the
  split-then-reunified graph: all present in the evidence. Held.

- **The version claim was partly wrong, and I fixed it.** The article credited
  jj 0.33.0 with "added `jj op restore`." That is false. I opened the changelog
  (s6): 0.33.0 made `jj undo` sequential and added `jj redo`; `jj op restore`
  predates the release (it is referenced as an existing command in the same
  changelog's deprecation notes and in the operation-log doc). The article's own
  earlier paragraph already treats `jj op restore` as a standing feature. Worse,
  the demonstrated single `jj undo` reverses one operation, which is the
  *pre*-0.33.0 capability, so framing "that single-command reversal is newer
  than it looks" mislocated what 0.33.0 actually changed. Both facts are in the
  evidence, so I recast the paragraph: the single undo is long-standing, and it
  is the *multi-step reach* (repeated undo stepping further back rather than
  toggling) that dates to 0.33.0, with the pre-fix complaint (s7) kept. The
  0.33.0 date (2025-09-03), v0.44.0 (2026-08-05) and the 15-release cadence all
  verified against the changelog.

- **The four honest costs are each sourced, and I opened every one.** Git-backend
  index corruption: the concurrency doc (s10) carries the exact quote "repository
  corruption is possible because the backend is not entirely lock-free" with
  `jj debug reindex` recovery, and issue #2193 (s11) is OPEN. Lossy same-change
  resolution: the technical/conflicts doc (s12) carries "lossy in terms of
  conflict algebra" and "will lose changes," naming #6369, which (s13) is OPEN.
  Missing hooks / no `--fixup`: git-compatibility (s14) shows "Hooks: No"; the
  Minsoo review (s15) confirms the `prepare-commit-msg` FreeBSD fallback, the
  manual `fixup!` workaround, and the "small friction, but it adds up" quote
  verbatim; git-experts (s16) carries the `jj absorb` "doesn't solve all cases"
  limit. Bookmark-push / colocation: git-compatibility (s14) has the interleaving
  bug; Arun (s17) confirms the colocation-plus-workspace break with Claude Code.
  All held.

- **The backing contradiction is stated honestly.** GOVERNANCE.md (s18) has the
  "At most 1/3 … single company" cap and nine maintainers; paid_contributors.md
  (s19) lists martinvonz, ilyagr and thoughtpolice under East River Source
  Control, so exactly 3 of 9 (33%) sit at the ceiling, not under it. The math is
  right. The README (s20) carries the "full-time project at Google" disclaimer
  verbatim; the roadmap (s22) carries the "spare time" line; ersc.io (s21)
  self-describes as tooling "to help you manage your most important asset: your
  code," links jj's docs, and states no funding or formal relationship. The
  article defaults to neither "Google's tool" nor "a funded startup's tool" and
  leaves the question open. Held.

**Display text, descriptor by descriptor.** Headline ("Jujutsu undoes a botched
rebase back to the exact original commit IDs") is defended by the demo. Dek
states two real capabilities and is not the banned capability-then-caveat mold.
Section headings each name the tool or its concept and reconstruct the argument.
Fig. 1 caption matches the demo output. Stat strip ("~1 / 4 weeks … 14 months";
"3 of 9 … one payer") is accurate to the evidence and cited in nearby prose. No
false label found.

**Sourcing labels.** `data-nb-kind` audited: the four secondary sources
(HN s7, Minsoo s15, Arun s17, ersc.io s21) are correctly secondary; the rest are
the project's own docs, repo files and issue tracker, correctly primary. The
backing contradiction rests on two self-disclosed primaries (README vs.
paid_contributors); the costs pair project primaries with independent secondary
corroboration. No mislabel hiding a missing independent source.

**Links.** I opened all 22 hrefs as printed. Every one resolves to the source
itself. Only s7 (Hacker News) I could not re-open live — a transient HTTP 429
rate-limit on a valid item URL; its mkeeter quote is confirmed verbatim in the
evidence record. Minor: s10's `data-nb-locator` reads "Storage," but the exact
corruption quote sits in that page's "Syncing with rsync, NFS, Dropbox"
subsection; the link still lands on the right page, so I left it.

**Inline `<code>`.** Audited every instance. All are literal strings a reader
would type, see in output, or must read character-for-character: commands
(`jj undo`, `git commit --fixup`), the `@` and `(conflict)` labels, filenames,
commit IDs, `root()`, hook and prefix names. None is technical emphasis.

## Cut

The slop pass turned up no sentence that had to be deleted. Prose is concrete
and noun-carried; the honest-cost and backing sections earn their edge
sentences with facts. I ran the delete test on the section openers and closers.
Kept, with reasons: "A live jj 0.44.0 install now proves it, not the
documentation's own examples…" survives because the live-versus-docs sourcing
point is real and the verdict block leans on it, not empty foreshadowing.
"Jujutsu ships often enough to trust the release notes as a live record…" is
mild negative parallelism but introduces the cadence stat that follows it.
"Neither is softened here into 'Google's tool' or 'a funded startup's tool'"
echoes the brief's two-option framing, but the fork is the one the sources
themselves create (README=Google, ersc=separate company) and the synthesis is
evidence-grounded, so it is reporting, not leakage; I let it stand.

The Verdict note's imperatives ("Trust the first two findings … Leave the third
open") are the documented job of the `nb-note-strong` "Verdict" component per the
engine furniture catalog ("the weight the reader should put on it, and what
would change the assessment"), not a reader-address slop failure. Furniture is
proportionate for 2,600 words: one essential code listing, one two-number stat
strip, one holds-up grid feeding its Verdict note. No component is decorative and
none is missing; the evidence's suggested release-timeline chart is unnecessary
because the stat strip already carries the cadence claim.

Compared the dek and headings against the recent-pattern notes: the dek does not
fall into the capability-then-caveat mold the last expert-tools deks used, and
the headings vary in construction rather than repeating a comma-and-"and" shape.

Two direct edits (below), neither a slop cut: one factual correction, one
clarity repair.

## Reader

Reading the survivor straight through: what I have that the sources alone would
not give me is the connected maintenance story — a live-verified exact undo tied
to the dated release that widened undo's reach and to the pre-fix complaint that
release answered, plus the governance-cap arithmetic (3 of 9, exactly at the
1/3 ceiling) set against the README-vs-disclosure contradiction. The
draft-handoff's original-work sentence claims those same two syntheses; both
survive, and the first is now accurate about which part of undo is actually
new. The evidence supplies every fact and states neither connection itself, so
the piece is not restating its sources. The prose sits closer to the voice-guide
exemplars (Cook's mechanism-first description, Virtanen's plain cost statements)
than to a median summary. The headline, read as the largest claim, is defended
by the demonstration it names.

## Edits

- Rewrote the jj 0.33.0 paragraph: removed the false "added `jj op restore`"
  attribution and stopped crediting the demonstrated single undo as new; it now
  states that single-operation undo is long-standing and that 0.33.0 made undo
  sequential so repeated calls step further back (citations s6, s7, s6 and the
  s6 locator preserved).
- Fixed a nested-comma clarity break in the orientation section: "the same loop,
  fold in the changes, act, check out, runs before…" → "that same loop — fold
  in the changes, act, check out — runs before…" (2 em-dashes; budget is 4,
  none used before).

## Required work

None. Both defects were editor-fixable from facts already in the evidence record
and confirmed against the cited primary; no new reporting or evidence is needed.
The orchestrator runs the fresh proof after these edits.

## Decision

approve — the demonstration reproduces the evidence exactly, the four costs and
the backing contradiction are each sourced and honestly stated, every citation
resolves to its source, and the one factual error (a misattributed 0.33.0
feature) and one clarity break were corrected in place without new reporting.
