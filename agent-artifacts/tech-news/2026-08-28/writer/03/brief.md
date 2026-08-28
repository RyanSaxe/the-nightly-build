# writer brief: tech-news/2026-08-28 (03)

Round-02 satisfied the "date it as prior news" fix but the one-primary-per-item
proof rule forced dropping the repository as primary, which lost the item's
distinctive value (the machine-checkable Lean 4 certificates / verification, not
just discoveries). Restore that value using the alternative you already
identified.

Apply: make the openai/ten-proofs repository the item's ONE primary again (it is
the artifact that owns the Lean 4 certificates / Apache-2.0 / verification
angle), and cite an independent secondary (The Decoder) for the item. Take the
manuscript's date ("about four weeks ago", Aug 1 / updated Aug 6) from that
secondary's dateline so the item still reads as prior work now made public, not
the day's development, and keep the "not peer-reviewed" close. Retag the item
back to reflect the formal-verification substance now that it is sourced again.

Inputs:
- writer/02/draft-handoff.md and editor/01/editorial-review.md — the fix history and the editor's direct edits (preserve them)
- researcher/01/evidence.md — carries both the repository and The Decoder with their kinds and the date
- the article: .nb-work/tech-news/2026-08-28/library/tech-news/2026-08-28.html

Output: writer/03/draft-handoff.md
Proof (rerun complete, links included):
./nb check .nb-work/tech-news/2026-08-28/library/tech-news/2026-08-28.html --series tech-news --library /home/user/library-checkout
until BLOCK: 0 (nb stamp if counts change). Preserve all three other items and the editor's edits.
