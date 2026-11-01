# editor review-brief: daily-brief/2026-11-01 (01)

Inputs:
- `../../editorial-direction.md` — the standing standard and the Daily Brief series direction.
- `../../commission.md` — the six-item slate, backups, and standing instructions.
- `../../writer/01/brief.md` — the exact brief the writer worked to.
- `../../writer/01/draft-handoff.md` — the writer's handoff and word count.
- `../../researcher/01/evidence.md` — the verified anchor fact and source per item; check each cite.
- The article HTML: `/home/user/the-nightly-build/.nb-work/daily-brief/2026-11-01/library/daily-brief/2026-11-01.html`
Output: `editorial-review.md` (beside this brief).
Proof: `/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/daily-brief/2026-11-01/library/daily-brief/2026-11-01.html --series daily-brief --repo /home/user/the-nightly-build`

This brief names the inputs, the output path, and the proof line. Work from the
inputs. Where something you need is missing, ask the orchestrator.

Your job (editor, fresh eyes, final quality gate):
1. Cut slop against `spec/slop.md`, hardest at the edges (first/last sentence of
   each paragraph, each section, and the article). Compare against the recent
   record for formula and house catchphrases: the commission's recent-pattern
   notes list the shapes this piece must not reproduce. Delete, do not repair, a
   slop sentence unless something real was waiting to be said.
2. Check the three first lines against `spec/headlines.md`: headline, dek, and
   every section heading. No colon subtitle, no unanswered question, no dek
   built on negative parallelism (semicolon reversal, suspended question, comma
   triad), headings built differently from each other and from the recent
   library.
3. Check correctness and citations against `researcher/01/evidence.md`: every
   claim that could be doubted is cited, each cite matches what the source says,
   no fabricated or decorative citation, and the piece says what the reporting
   supports without hedging. Confirm the piece does the original work its
   handoff claims.
4. Check the counted bans (the proof also counts them, but catch them in prose):
   em-dash at most 4, "leverage" at most 1, "load-bearing" 0, and this press's
   "mechanism"/"mechanisms" at most 1 — rewrite the sentence (do not swap a
   synonym or repunctuate) when a count runs over.
5. You MAY make direct cuts to the draft to fix slop and tighten prose. If the
   piece needs a different argument or new prose that is not yours to write,
   that is the one thing that goes back to the writer: say so clearly as a
   REQUIRED CHANGE in your review, and the orchestrator will open a new writer
   round. If every required change is a direct cut you made, say the piece is
   SETTLED (no writer round owed for the proof alone).

Write `editorial-review.md` with: a SETTLED-or-REQUIRES-CHANGE verdict at the
top; the direct cuts you made (if any); any required changes for the writer; and
your check of correctness, citations, headlines, slop, and banned terms. Meet
`spec/slop.md` in your own prose. After any direct cuts, leave the article HTML
in a state the orchestrator can stamp and prove.

Brief-specific checks: exactly six items in order (Word, 3 news, 2 tech); one
citation per item (Word takes two); total body 300-700 words (STRICT — if over,
the fix is to cut words inside items, never drop an item); each item stands
alone and does not close on a line that hands the point back; present tense for
events; contested or single-party claims attributed; the two tech items framed
neutrally with no self-reference. Each `<h3>` headline obeys `spec/headlines.md`.
