# Writer brief — paper-of-the-day/emergent-abilities (01)

## Role
Load and follow `skills/writer/SKILL.md`. Draft from the exact brief, voice
guide, and evidence record, then carry it through the proof to BLOCK: 0.

## Begin with these exact inputs (all under `.nb-work/paper-of-the-day/emergent-abilities/`)
- `agent-artifacts/paper-of-the-day/emergent-abilities/editorial-direction.md`
- `agent-artifacts/paper-of-the-day/emergent-abilities/commission.md`
- `agent-artifacts/paper-of-the-day/emergent-abilities/writing-coach/01/voice-guide.md`
- `agent-artifacts/paper-of-the-day/emergent-abilities/researcher/01/evidence.md`
  (10 verified sources; both papers read from PDF; verbatim Wei abstract inside)
- The initialized article: `library/paper-of-the-day/emergent-abilities.html`
- Generated context: `.nb-context/` (template-contract, runtime-assets, furniture).

## What to write
The article at `library/paper-of-the-day/emergent-abilities.html`. Template
`paper`, **1800-3400 words**, flex sections 2-8 (last lands the verdict).
- `abstract` section: the `nb-paper-card` with the focal paper's title as
  published, full authors, venue (TMLR) + arXiv id + year, "Read the paper" link,
  and the **Wei et al. abstract VERBATIM** exactly as the evidence record captured
  it (the researcher cross-checked it against the raw PDF — use that text, do not
  paraphrase or lightly edit it), cited.
- Reconstruct Wei et al.'s claim in your own words and order (define "emergent
  ability" as they did), then weigh it against Schaeffer et al.'s mirage argument
  and the afterlife (Wei's own blog rebuttal, Barak's qualified defense, the
  2024/2025 follow-ons). Separate the metric artifact from the real phenomenon.
- Include ONE concrete worked example of the metric effect. NOTE the researcher's
  honest flag: Schaeffer's central arithmetic figure has **no numeric table**, so
  build the worked example on the real named thresholds (FLOPs/parameters, the
  specific InstructGPT/GPT-3 integer-arithmetic task, exact-match vs a continuous
  metric) rather than inventing digitized curve points. Do not fabricate numbers.
- Anchor turning points with honest `data-nb-locator`/`data-nb-note` on cites;
  use `nb-excerpt` (see `.nb-context` furniture) only where an exact sentence
  earns display.

## Permitted changes / decisions you own
- Name the flex sections for the steps of THIS reconstruction; no
  Background/Method/Results/Verdict scaffold. Vary the opener (avoid "N years
  later, follow-on work shows exactly where…" and the "the paper's own table
  already recorded the catch" reveal — both flagged in the commission).
- Headline/dek per `spec/headlines.md`: state the finding; no colon-subtitle
  machine tell; the dek adds what the headline left out and takes a stance.
- Preserve fixed engine assets/classes/labels/required HTML. No added
  scripts/styles/iframes/forms/handlers/external images. A chart is allowed only
  if a real numeric series warrants it and is rendered via `nb chart` from
  committed provenance — given the no-table flag, prose is likely better than a
  fabricated chart; do not chart digitized curve points.

## Metadata (`nb-meta`)
Real values: `series: "paper-of-the-day"`, `slug: "emergent-abilities"`,
`template: "paper"`, `mode: "open"`, `order: null`, `date: "2026-07-31"`,
honest `tags` (e.g. `["research"]`), measured `sources`/`words`/`reading_minutes`,
`dek`, `harness: "claude-code"`, `model: "claude-sonnet-5"`.

## Proof (run to BLOCK: 0)
From checkout root (`export PATH="$HOME/.local/bin:$PATH"` first):
```
./nb check .nb-work/paper-of-the-day/emergent-abilities/library/paper-of-the-day/emergent-abilities.html \
  --series paper-of-the-day --library /home/user/library
```
Drive to **BLOCK: 0**; treat WARNs as revision notes.

## Also write
`agent-artifacts/paper-of-the-day/emergent-abilities/writer/01/draft-handoff.md`:
the article's visible act of original work (the clean separation of metric
artifact from real phenomenon, and the precise map of where Wei and Schaeffer
actually agree/disagree), final word/source counts, unresolved WARNs with reasons.

## Request, don't guess
Missing evidence → `REQUEST researcher <need>`; missing voice → `REQUEST
writing-coach <need>`. Do not fill gaps yourself.

## Control signal
Return exactly one line (DONE only after BLOCK: 0):
`DONE writer agent-artifacts/paper-of-the-day/emergent-abilities/writer/01/draft-handoff.md`
or `REQUEST <owner> <need>` / `BLOCKED writer <reason>`.

## Scope discipline
`./nb` and web tools for focused work only; the evidence record is your source of
truth. Re-open a source only to confirm exact wording you are about to quote.
