# Writer brief — paper-of-the-day/grokking (01)

## Your job
Draft the paper-reconstruction from the commission, voice guide, and evidence
record, then prove it to BLOCK: 0.

## Exact inputs (start here)
- `agent-artifacts/paper-of-the-day/grokking/commission.md`
- `agent-artifacts/paper-of-the-day/grokking/editorial-direction.md`
- `agent-artifacts/paper-of-the-day/grokking/writing-coach/01/voice-guide.md`
- `agent-artifacts/paper-of-the-day/grokking/researcher/01/evidence.md`
- Initialized article: `library/paper-of-the-day/grokking.html`
- `.nb-context/` (template contract, runtime assets, furniture incl. paper card)

## Write
1. `library/paper-of-the-day/grokking.html`:
   - `paper` geometry: `abstract` anchor (the `nb-paper-card` with title, authors,
     venue/arXiv id, working link, and the abstract **verbatim** from the evidence
     record) + `orientation` + 2–8 flex sections you name + `Sources`. Words
     **1800–3400** (measured). Every section cited.
   - Reconstruct the argument in your own words and best teaching order (not the
     paper's): the modular-addition task, the delayed-generalization phenomenon,
     and — the piece's spine — separate the 2022 phenomenon from the mechanism the
     after-record supplied (Nanda et al. 2023 Fourier/rotation + three phases; the
     fragility/weight-decay line). Define each concept where first spent.
   - Anchor turning-point claims on the citation itself with honest
     `data-nb-locator` / `data-nb-note` (section/figure numbers from evidence).
     Quote the original's exact sentence in a note only where it earns display.
   - Land a reviewer's verdict before Sources: what was measured, where the claim
     stops, what the after-record settled vs. left open.
   - Furniture: an equation for modular addition / the Fourier formulation where
     it clarifies; a worked example (p from the evidence). Do NOT fabricate a
     grokking curve — describe it in prose unless you have real transcribed, cited
     data points for `nb chart` with committed provenance.
   - `nb-meta` ACTUAL values: title, dek, date `2026-08-01`, mode `open`, order
     null, tags e.g. `["research"]`, measured sources/words/reading_minutes,
     harness `claude-code`, model `claude-sonnet-5`.
   - Number sources in first-citation order; honest `data-nb-kind`. The focal
     paper is primary for its own claims; only cite verified sources.
2. `writer/01/draft-handoff.md`: the visible original work (the phenomenon-vs-
   mechanism separation and the verdict it earns), warnings resolved, open items.

## Prove it
`/home/user/the-nightly-build/nb check library/paper-of-the-day/grokking.html --series paper-of-the-day --repo /home/user/the-nightly-build` → **BLOCK: 0**.
Treat warnings as revision notes.

## Rules
- Documented furniture only; no active content; preserve fixed engine
  assets/classes/labels. Begin with named inputs; `REQUEST researcher/writing-coach`
  rather than invent. Do not read arbitrary repo/archive files.

## Report
End with: `DONE writer library/paper-of-the-day/grokking.html`
