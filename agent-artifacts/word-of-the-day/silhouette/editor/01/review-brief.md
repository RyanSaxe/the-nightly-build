# editor review-brief: word-of-the-day/silhouette (editor/01)

Inputs:
- editorial-direction.md (artifact root) — the standard to enforce
- writer/01/brief.md (the exact writer brief — for instruction-leakage detection)
- commission.md (artifact root) — the word, its documented origin, the competing-accounts wrinkle
- writing-coach/01/voice-guide.md — the voice, licenses, do-not-reuse list
- researcher/01/evidence.md — the evidence to open as an opponent
- writer/01/draft-handoff.md — open the original-work sentence only on the third read
- The article at `library/word-of-the-day/silhouette.html` (workspace root) and `.nb-context/` template context
Output: editor/01/editorial-review.md

Recent-pattern notes: published words include apophenia, hysteresis, solastalgia,
etc.; the coiner-plus-year opener and the "X means Y" title mold are barred.

Round focus:
- Verify the definition card is cited to Merriam-Webster (with the pronunciation)
  and stands first with no heading above it (word-template rule).
- Verify the contested origin is handled honestly: the three accounts (mockery
  of his economies, his profile-cutting hobby, his brief tenure) each get their
  best case; the 1758 pre-ministry attestation is ATTRIBUTED to its secondary
  (Word Histories via Dulaurens) and flagged unconfirmed, never asserted in
  display text; the first-English-use date is presented as a range (MW 1783 vs
  OED/etymonline 1798), not a settled year.
- Confirm the present sense rests on the two cited Doyle usages, and audit every
  data-nb-kind (3 primary / 5 secondary claimed).
- Open every citation href as printed; it must resolve to the source itself.
- Word band 550-800 (currently 782). Make surgical cuts; route any redraft.
  After direct cuts run `./nb stamp <article-path>` (file arg).
