# Writer brief: current-events/2026-08-02 (02) — targeted repair

## Why this exists
The editor (`../../editor/01/editorial-review.md`) approved the brief except for
one publication-blocking issue in **item 3 (measles)**: the elimination-status
determination is OWNED by PAHO (its Regional Verification Commission is the body
that certifies elimination status — "CDC does not itself declare elimination
status"), but the item cites CDC as the source for that determination in the
**headline** and tags PAHO `data-nb-kind="secondary"` to satisfy the brief
template's one-primary-per-item cap. A wrong owner in display text undercuts the
item's own correction.

## Begin with these exact inputs
- This brief; `../../editor/01/editorial-review.md` (the editor's required change
  and the three direct fixes it already made — preserve those);
- your prior draft handoff `../../writer/01/draft-handoff.md`;
- evidence record `../../researcher/01/evidence.md` (item 3 sources: CDC case
  data = S11; PAHO elimination-status determination = S12; KFF structure = S13);
- the article (already carries the editor's item-2/3/4 fixes):
  `/home/user/the-nightly-build/.nb-work/current-events/2026-08-02/library/current-events/2026-08-02.html`.

## The exact fix (item 3 only)
1. Attribute the **elimination-status determination** (the Americas region lost
   it Nov 2025; the US national status is under review, decision due Nov 2026) to
   **PAHO** — including in the item's **headline/display text**. PAHO owns this
   claim; CDC owns the case *data*, not the status determination.
2. Re-tag sources honestly to reflect ownership, keeping the per-item geometry (1
   primary + 1+ independent secondary): **PAHO = `data-nb-kind="primary"`** for
   the elimination-status determination; **CDC** (case counts 2,371/37/94%,
   MMR coverage 95.2%→92.5%) and **KFF** (dual-verification structure/definition)
   as the independent **secondary** support. Do not tag to satisfy the cap;
   attribute each claim to the body that owns it.
3. Keep the corrected region-vs-US distinction and every verified number; keep
   the editor's already-applied fixes to items 2 and 4 untouched.

## Constraints
Change only what this repair requires; preserve all settled item-1/2/4 work and
the editor's direct edits. Do not add new claims. Renumber sources only if
first-citation order actually changes.

## Prove and hand off
Re-run to `BLOCK: 0`:
`/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/current-events/2026-08-02/library/current-events/2026-08-02.html --series current-events --library /home/user/library`
Write `../02/draft-handoff.md` recording the fix applied, the proof result, and
confirmation the editor's other edits were preserved. Return
`DONE writer <path-to-02/draft-handoff.md>` after `BLOCK: 0`.
