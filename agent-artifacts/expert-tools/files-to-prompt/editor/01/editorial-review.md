# Editorial review — expert-tools/files-to-prompt (editor, round 01)

## Decision
Approve. No redraft required. Proof clean after direct edits: `BLOCK: 0`,
`WARN: 0`, `PUBLISHABLE`.

## Skeptic
Skeptic: thesis "files-to-prompt is a 334-line, 17-month-dormant utility that
still folds a chosen slice of a repo into one citable prompt, worth adopting for
its core job but not trusted blind, because two undocumented matching bugs and
its documented strengths all trace to the same minimal implementation"; tested 6
claims (real captured runs vs invented; the two footguns tied to actual source;
the dormancy caveat stated not buried; every data-nb-kind label; the "still niche,
not a default" scale claim; headline/dek as claims); broke: none.

Verification detail:
- **Runs are real, not invented.** Confirmed against this repo's own tree:
  `engine/assets/` holds exactly two stylesheets (`nb.css`, `themes/newspaper.css`),
  one script (`nb.js`), and three PNGs (`apple-touch-icon.png`, `favicon-32.png`,
  `favicon-64.png`) — matching Fig 1's three UnicodeDecodeError warnings and its
  quoted stdout, whose first line (`/* The Nightly Build — site chrome + shared
  article chrome.`) matches the file character-for-character. `engine/ci_helpers.py`
  and `engine/check.py` exist for the `--cxml` run (Fig 2). Byte counts (8,217;
  7,576) match evidence items 4–5. Fig 3's `should_ignore` listing is verbatim to
  evidence item 1. The `--cxml` default-mode tagging and default-mode binary
  exclusion are both shown from captured output, as the brief required.
- **Both footguns accurate and source-tied.** The `-e` suffix bug (returns `copy`
  for `-e py` via `str.endswith(("py",))`) and the anchored-`.gitignore` leak
  (`/src/staticfiles/` leaks `bundle.txt` because `fnmatch` runs on the bare
  basename) are each demonstrated by a real scratch run AND corroborated by the
  matching independently-filed issue (#60, #46), and both correctly trace to the
  `should_ignore`/`process_path` source. The piece correctly reframes "binary
  skipping" as a decode-failure catch, per the evidence Contradictions note.
- **Maintenance caveat honest, not buried.** The ~17-month dormancy (last
  commit/release 2025-02-19), 13 open issues, and ~200 installs/day appear in the
  dek, the `nb-stat-strip`, and the Verdict — the caveat leads the maintenance
  section rather than hiding in it. The "adopt, but don't trust blind" judgment is
  earned from facts already shown.
- **data-nb-kind audit: all 20 correct.** Primaries are the tool's own source,
  README, tests, PyPI/GitHub records, the author's own posts, the two user-filed
  issues, and the first-hand runs. The two secondaries are Repomix's landing page
  (scale comparison) and s20 — correctly scoped to the independent adopter
  `layer8`'s reply, not simonw's primary top-level comment in the same HN thread.
  No wrong label hides a missing independent source.

## Cut
Cut: 2 words plus 1 heading word and 1 self-reference phrase; worst tell:
"quiet/quietly" used four times, twice in consecutive section headings ("…quietly
drops three PNGs" / "Where the matching quietly gives up"), a formula. Direct edits:
- Dropped "quietly" from the Fig-1 heading (also more accurate — the run prints
  three warnings, so the drop is not quiet), breaking the parallel-heading formula.
- Removed "quietly" from "which ones quietly don't" in the orientation, leaving two
  distinct-sense uses of "quiet" in the piece.
- "roughly seventeen months before this piece" → "…earlier" (self-reference).
- "Thirteen issues sit open as of this writing" → "Thirteen issues sit open"
  (self-reference; the date is already established).
No scaffold headings, no install-tutorial drift, no hype adjectives, no
manufactured punchline, and no writer-brief instruction leakage found. The Verdict
`nb-note-strong` and the three `nb-code` listings each carry evidence, not
decoration.

## Reader
Reader: this gives me a source-grounded trust verdict the README, release notes,
and any single source do not — that the tool's two documented strengths (clean
decode-failure exclusion, citable `--cxml` tags) and its two undocumented failures
(the `-e` suffix match, the anchored-`.gitignore` leak) all fall out of the same
seven lines of minimal implementation, demonstrated on this repo's real tree and
confirmed in the wild by independently filed issues, alongside a plain dormancy
verdict. This matches the draft-handoff's stated original-work sentence. Prose sits
with the voice-guide exemplars (command-first, flat declarative cost register), not
a median AI summary. Headline is the largest claim, declarative, names the tool and
its action, no colon tell.

## Required work by owner
None.

## Proof
`./nb check … --series expert-tools --library /home/user/library` → `BLOCK: 0`,
`WARN: 0`, `PUBLISHABLE`, re-run after the edits above.
