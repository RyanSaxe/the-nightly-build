# Draft handoff: tech-news/2026-08-12 (01)

## Original-work sentence

The article resolves the evidence record's flagged thin-day tension into a
stated through-line — with model releases quiet across 10-12 August, the
window's advances that change what a field can do were three laboratory and
observational results — then orders them by consequence and dates each to its
own publication day (Dyna-1, 10 Aug; azine C-H coupling, 11 Aug; the eclipse
campaign, 12 Aug) rather than laundering the earlier two into the 12 August
anchor.

## Final proof result

`./nb check ... --series tech-news --library /home/user/library-checkout`
(full run, links included):

- **BLOCK: 3** — all `B-SOURCE-KIND`, one per item: each item cites 0 secondary
  sources; this series requires every item to cite exactly 1 primary and at
  least 1 secondary (`per_item_sources`: primary [1,1], secondary [1,null]).
- **WARN: 2** — `W-LENGTH-LOW` (3 items, band is 4-6) and `W-SOURCES-MIN`
  (3 sources cited, series floor is 5).

`BLOCK: 0` is not reachable from the current evidence record. The three blocks
are not fixable by the writer: the evidence supplies a verified primary for each
in-scope item but no independent secondary for any of them, and the only
secondaries in the record (TechCrunch and the techstartups roundup, both on the
declined Anthropic-watermark story; phys.org on the discarded 29-July centromere
paper) do not cover the eclipse campaign, Dyna-1, or the azine coupling.
Attaching any of them to these items would be a fabricated citation, which
`spec/editorial.md` ("cite only what you have read") and the writer role both
bar. Per the brief, this is reported as a researcher request rather than written
around.

## Warnings intentionally left

None left by choice. Both WARNs are downstream of the same missing-secondary
gap and resolve when the researcher request below is filled:

- `W-SOURCES-MIN` clears automatically once each item gains its secondary
  (3 primaries + 3 secondaries = 6 cited sources, above the floor of 5).
- `W-LENGTH-LOW` clears only if a fourth in-scope, honestly-dated item is added
  (see the open question); a 3-item edition is defensible under the brief
  ("four strong, honestly dated items beats six with filler"; the band is a
  WARN, not a BLOCK), but that is an editor/orchestrator call, not the writer's.

## Open questions / researcher request

1. **Independent secondary per item (blocking).** Add one independent secondary
   account to the evidence record's Sources block for each of the three items,
   with a resolving URL and the exact passage that supports the item's
   load-bearing claim, marked `Kind: secondary`:
   - Dyna-1 (Nature s41586-026-10989-4, 10 Aug) — a reputable newsroom or
     independent write-up covering the model and its missing-assignment premise.
   - Azine C-H coupling (Nature s41586-026-10991-w, 11 Aug) — independent
     coverage of the phosphine-mediated water/ammonia coupling.
   - Eclipse coronal campaign (NASA "Soars", 12 Aug) — an independent newsroom
     account of the WB-57 / balloon observing campaign (NASA's second page is
     not independent of NASA).
   The researcher's note calls each item "primary-plus-secondary sound," so the
   secondaries were likely verified but not recorded; recording their URLs and
   supporting passages unblocks all three items and clears `W-SOURCES-MIN`.

2. **Fourth in-scope item (WARN, decision needed).** The record verifies only
   three in-scope, honestly-dated developments for the 10-12 August window; the
   band floor is four. Either accept a 3-item edition (leaving `W-LENGTH-LOW`)
   or have the researcher verify one additional in-scope, in-window development.
   This is an orchestrator/editor decision.
