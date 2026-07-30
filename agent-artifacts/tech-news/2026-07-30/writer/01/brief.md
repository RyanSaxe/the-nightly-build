# Writer brief — tech-news/2026-07-30 (invocation 01)

## Inputs
- editorial-direction.md (governing stack; do not edit)
- commission.md (selection rules, geometry, non-repetition, neighbors)
- writing-coach/01/voice-guide.md
- researcher/01/evidence.md
- Article to edit: .nb-work/tech-news/2026-07-30/library/tech-news/2026-07-30.html
- Template context under .nb-work/tech-news/2026-07-30/.nb-context/

## Output
- The article HTML (edit the initialized skeleton; do not recreate it).
- writer/01/draft-handoff.md (original-work sentence, paths, proof result,
  warnings left, and — because no child agents are available — the line
  `Production: single-context, no isolation.`)

## What to build
A `brief` front page, five items, in this order (significance first):
1. Anthropic Claude Mythos cryptanalysis (HAWK + reduced AES).
2. MIT VLASH anticipatory robot motion planning.
3. NASA Swift wandering off-nuclear tidal disruption event (AI-flagged).
4. University of Michigan "electron lighthouse."
5. Twisted-light chirality discrimination (Tata/IIT, Science Advances).

Each item: a headline that names the development (no colon subtitles, no triad),
then 2–4 sentences carrying the number/mechanism the headline dropped and one
honest limit. Every claim traces to the evidence record. Use the Numbers section
exactly; do not invent figures or the electron-lighthouse semiconductor material.

## Source geometry and citations
Each item cites exactly one primary and one independent secondary. Number source
entries in first-citation order across the whole brief. Planned mapping (verify
as you place them):
- Item 1: s1 Anthropic (primary), s2 CyberScoop (secondary)
- Item 2: s3 MIT News (primary), s4 Interesting Engineering (secondary)
- Item 3: s5 NASA Science (primary), s6 Universe Today (secondary)
- Item 4: s7 U-Michigan News (primary), s8 ScienceAlert (secondary)
- Item 5: s9 Science Advances (primary), s10 Phys.org (secondary)
Carry `data-nb-kind="primary"/"secondary"` honestly. The headline link is the
primary; cite the secondary inline in the item's prose so every item shows both.
Do not add `data-nb-locator`/`data-nb-url`/`data-nb-note` (no source asset).

## Required caveats (do not overclaim)
- Item 1: no deployed system is affected; the AES result is reduced-round only and
  needs >400 octillion messages; it does not break full AES.
- Item 3: the AI angle is the ZTF detection; the result is the record off-nuclear
  offset. Do not call it Earth-threatening or nearby beyond the cited distance.
- Items 4–5: primaries return 403 (gated); claims verified via secondaries — keep
  to what the evidence states.
- Item 2: multi-institution robotics result; do not frame as an Nvidia story.

## nb-meta (actual values)
protocol 1.1; series tech-news; slug 2026-07-30; template brief; mode rolling;
order null; date 2026-07-30; tags []; harness claude-code; model
claude-opus-4-8. Set title, dek, sources (measured = 10), words (measured),
reading_minutes (measured). Keep nb-meta dek identical to the rendered dekline.

## Proof
export PATH="/root/.local/bin:$PATH"
./nb check .nb-work/tech-news/2026-07-30/library/tech-news/2026-07-30.html \
  --series tech-news --repo . --library ../library
Drive to BLOCK: 0; treat WARN as revision notes.
