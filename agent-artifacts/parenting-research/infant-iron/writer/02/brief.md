# Writer brief: parenting-research/infant-iron (02) — dek precision fix

## Why this exists
The editor (`../../editor/01/editorial-review.md`) approved the article except
for one publication-blocking issue in the **dek** (display text), which conflates
two distinct findings from the Chilean cohort. The editor already made four
surgical cuts and one factual narrowing in the body directly — PRESERVE those.

## The exact fix (dek only)
The dek must be factually precise about which finding is which (evidence record
`../../researcher/01/evidence.md`, sources S6-S8):
- The **social-emotional / adaptive-behavior BENEFIT** is the **10-year** analysis
  (Lozoff 2014, S7). Do NOT attribute it to the 16-year follow-up.
- The **16-year follow-up** (East 2023, S8) measured **neurocognition only**
  (visual-motor integration, quantitative reasoning) — the persistence of the
  *cognitive* harm signal, not adaptive behavior.
- The **baseline-iron dependence** (high-Hb worse, low-Hb better — the sign-flip)
  tracks only the **cognitive/visual-motor** outcomes. Do NOT assign the
  baseline-Hb dependence to the cognitive-vs-adaptive domain split; the domain
  split (cognitive harm vs social-emotional benefit) is a separate axis from the
  baseline-Hb interaction.
Rewrite the dek so it states a true, sharp claim consistent with these
distinctions (a stance, not a comma-triad, not an effect-size hook).

## Apply in both places
Update the dek in **both** the `nb-meta` `dek` field and the rendered dekline
(they must match — the proof checks this). Refresh `nb-meta` `words` if the count
changed.

## Constraints
Change only the dek (and its nb-meta twin / word count). Preserve the editor's
four body cuts and the factual narrowing, the sign-flip chart, and all settled
work. Do not introduce new claims.

## Prove and hand off
Re-run to `BLOCK: 0`:
`/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/parenting-research/infant-iron/library/parenting-research/infant-iron.html --series parenting-research --library /home/user/library`
Write `../02/draft-handoff.md` (the new dek, why it is now precise, proof result,
confirmation the editor's edits were preserved). Return
`DONE writer <path-to-02/draft-handoff.md>` after `BLOCK: 0`.
