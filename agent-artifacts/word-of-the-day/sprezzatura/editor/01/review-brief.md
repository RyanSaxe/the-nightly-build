# Editor review-brief: word-of-the-day/sprezzatura (01)

## Your job
Give this drafted Word of the Day piece the three ordered reads (skeptic, cut,
reader) and either approve it (`DONE editor` with no required change) or route
numbered repairs. Make cuts and small prose fixes directly; new prose past a
word or clause returns to the writer; evidence gaps return to the researcher.

## Begin with these exact inputs
- This brief.
- `../../editorial-direction.md` (house floor, headline standard, press voice,
  article identity, series prompt).
- The exact writer brief: `../../writer/01/brief.md` (for prompt-leakage
  detection — cut copied instructions/labels/selection rules).
- Voice guide: `../../writing-coach/01/voice-guide.md` (read first).
- Evidence record: `../../researcher/01/evidence.md` (open as a map in the
  skeptic read; reopen cited sources as an opponent).
- Draft handoff: `../../writer/01/draft-handoff.md` (open the original-work
  sentence only in the third read).
- Article: `/home/user/the-nightly-build/.nb-work/word-of-the-day/sprezzatura/library/word-of-the-day/sprezzatura.html`
- Template context: `../../../../.nb-context/`.

## What to check hardest (this piece's risk surface)
- **Display text descriptor by descriptor**: the headline, dek, and every subhead
  as claims AND as labels. Verify against the owning primaries: Castiglione's
  identity and dates (Italian courtier/diplomat/writer, 1478-1529); the dialogue's
  setting (court of Urbino, 1507; published Venice 1528); Count Lodovico da
  Canossa as the speaker who coins the term; the quotation attributed to Opdycke's
  1903 translation; the Latin tag attributed to **Ovid, *Metamorphoses*
  10.251-252** (NOT *Ars Amatoria* — the commission's original attribution was
  corrected). A wrong title/date/attribution in display text is the costliest
  error the paper prints.
- **Sourcing honesty / `data-nb-kind`**: Castiglione (translation + Italian
  original), Ovid, Cicero = primary; Merriam-Webster, Britannica, De Cruz,
  Treccani = secondary. Confirm no OED claim slipped in (it was gated/unread) and
  no Hoby wording is quoted (unverified). Etymology (Treccani) must stay separate
  from present meaning (MW/De Cruz), framed as history.
- **The modern-usage claim** must be grounded in the De Cruz (2024) instance, not
  asserted. The Roberto/affettazione paradox must be Castiglione's own text, not a
  later gloss.
- **Slop/tells**: the piece closes on the Treccani "to devalue" etymological
  irony — check it lands as argument, not a manufactured punchline; check the
  "cure carries its own failure test" throughline is not self-grading.

## Standards to apply in the cut
Full house prose and punctuation floor (period as default; em-dash only for a
real aside, at most once in a stretch; no semicolon chains; no hedged-contrast
reflex beyond one or two earned; no self-reference or reader-address; banned-terms
merged list — the proof counts these, but you judge the ones that pass count).
Compare opener, closer, headings, and dek against the recent Word of the Day
library (zugzwang, shibboleth, quisling, bowdlerize, etc.) for the shapes the
commission flagged: definition-as-claim openers, "coined in YEAR" openers,
who-did-what-when deks, eponym-correction shapes. Break any repeated shape.

## Output
Write `editorial-review.md` here with the three required lines (`Skeptic:`,
`Cut:`, `Reader:`), your direct edits, any required work by owner, and the final
decision. If you make edits, the writer reruns the proof
(`nb check .../sprezzatura.html --series word-of-the-day --library /home/user/library`)
— but for cuts/small fixes you may confirm the article still reads clean; note if
a re-proof is needed. Return `DONE editor <path>` only if no redraft is required,
else `REQUEST writer/researcher <one-sentence>`.
