# Writer brief: paper-of-the-day/generative-adversarial-networks (03) — dek date fix

## Why this exists
The editor (`../../editor/02/editorial-review.md`) confirmed the recast dek clears
the banned mold but flagged one factual error: the dek misdates its subject. The
fair-budget study (Lucic et al.) is **2017**, three years after the 2014 GAN
paper — not "a decade later."

## The exact fix (dek only)
Correct the time interval in the dek so it is factually accurate (Lucic et al.
2017 is ~three years after the 2014 paper; if the dek instead means the
diffusion displacement, Dhariwal & Nichol is 2021, ~seven years — use the true
interval for whichever finding the dek actually names). Keep the dek off the
banned "proved X for a setting practice never occupied" mold. Update it in
**both** the `nb-meta` `dek` field and the rendered dekline (they must stay
identical). Refresh `nb-meta` `words`/`reading_minutes` if the count shifts.

## Constraints
Change only the dek and the stale nb-meta counts. Preserve all settled work
(abstract, equations, tables, the editor's prior cuts). No new claims.

## Prove and hand off
Re-run to `BLOCK: 0`:
`/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/paper-of-the-day/generative-adversarial-networks/library/paper-of-the-day/generative-adversarial-networks.html --series paper-of-the-day --library /home/user/library`
Write `../03/draft-handoff.md` (the corrected dek, the true interval used, proof
result). Return `DONE writer <path-to-03/draft-handoff.md>` after `BLOCK: 0`.
