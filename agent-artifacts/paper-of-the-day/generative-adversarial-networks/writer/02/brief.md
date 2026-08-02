# Writer brief: paper-of-the-day/generative-adversarial-networks (02) — dek recast + re-proof

## Why this exists
The editor (`../../editor/01/editorial-review.md`) approved the article except
for one item that is new prose (yours): the **dek** reuses the voice guide's
explicit do-not-reuse formula, "proved X for a setting practice never occupied."
The editor also made four direct cuts, which left the `nb-meta` `words` count
stale — a re-proof is required.

## The exact fix
1. **Recast the dek** off the banned "proved X for a setting practice never
   occupied" mold (and its close cousins). Write a true, sharp dek that commits to
   something the piece establishes — the theory-vs-practice gap, the paper naming
   its own failure ("the Helvetica scenario"), or the fair-budget verdict — in the
   piece's own nouns, not a stamped shape. Not an effect-size hook, not a
   "N follow-ups disagree" line. Update it in **both** the `nb-meta` `dek` field
   and the rendered dekline (they must match).
2. **Refresh `nb-meta` `words`** (and `reading_minutes` if it shifts) to the
   post-edit measured count.

## Constraints
Change only the dek and the stale nb-meta counts. Preserve the editor's four
direct cuts and all settled work (the verbatim abstract, the equations/theorems,
the tables). Do not introduce new claims.

## Prove and hand off
Re-run to `BLOCK: 0`:
`/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/paper-of-the-day/generative-adversarial-networks/library/paper-of-the-day/generative-adversarial-networks.html --series paper-of-the-day --library /home/user/library`
Write `../02/draft-handoff.md` (the new dek, why it clears the banned formula,
proof result, confirmation the editor's cuts were preserved). Return
`DONE writer <path-to-02/draft-handoff.md>` after `BLOCK: 0`.
