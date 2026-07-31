# Writer brief — unbiased/should-the-fed-hike (01)

## Role
Load and follow `skills/writer/SKILL.md`. Draft this STRICT two-position piece
from the exact brief, voice guide, and evidence record; carry it through the
strict proof to BLOCK: 0.

## CRITICAL correction from research (do not repeat the commission's error)
The commission assumed Chair **Jerome Powell** ran the July 29 meeting. The
researcher verified against federalreserve.gov that **Kevin Warsh** took the oath
as Fed Chair on **2026-05-22** and chaired this meeting. Use **Warsh**, not
Powell, throughout. Do not misattribute the cleaner "don't hike into a supply
shock" economic argument to Warsh — his own rationale is more equivocal; the
sharper version comes from named economists (Mark Zandi/Moody's, Janet Yellen).

## Begin with these exact inputs (under `.nb-work/unbiased/should-the-fed-hike/`)
- `agent-artifacts/unbiased/should-the-fed-hike/editorial-direction.md`
- `agent-artifacts/unbiased/should-the-fed-hike/commission.md` (note the
  Powell→Warsh correction above overrides the commission)
- `agent-artifacts/unbiased/should-the-fed-hike/writing-coach/01/voice-guide.md`
- `agent-artifacts/unbiased/should-the-fed-hike/researcher/01/evidence.md`
  (14 read sources: 7 primary + 7 secondary; event verified; Logan's speech for
  raise; Warsh + Zandi/Yellen for hold; inflation cross-checked vs BLS/BEA)
- The initialized article: `library/unbiased/should-the-fed-hike.html`
- Generated context: `.nb-context/` (contract, runtime-assets, the `nb-divide`/
  `nb-side` furniture).

## What to write
`library/unbiased/should-the-fed-hike.html`. Template `unbiased`, STRICT.
Structure exactly:
- `orientation`: the context the reader needs before the two positions (the
  July 29 2026 FOMC hold at 3.5%-3.75%, the 9-3 vote, the three hike-dissents
  Hammack/Kashkari/Logan, inflation above 2% for 5+ years, the supply-shock
  attribution). Define terms of art at first use (dual mandate, real rate,
  relative-price/supply shock, expectations anchoring) for a technical-but-not-
  economist reader.
- The `nb-divide` with **exactly two** `nb-side` sections, each with the four
  mandatory slots in order:
  - **Position A — "Raise now"** (`nb-side-left`, rename `data-nb-section`/`id`
    e.g. `raise-now`): camp name, concise thesis, argument (five-plus years above
    target risks un-anchoring; real policy not restrictive enough; better modest
    restriction now than severe later), and named holder **Lorie Logan** (Dallas
    Fed) with her cited July 16 2026 statement ("Better modest restriction now
    than severe restriction later") and her standing (a dissenter who favored +25bp).
  - **Position B — "Hold"** (`nb-side-right`, rename e.g. `hold-the-line`): camp
    name, thesis, argument (the inflation is a tariff/energy supply/relative-price
    shock a hike cannot fix and would worsen by squeezing a cooling economy;
    policy acts with long lags), and a named holder who actually holds it — the
    FOMC majority via **Warsh's** own cited hold statement, and/or a named
    economist (Zandi or Yellen) with a direct cited statement making the
    supply-shock case. Represent the position through a real cited quote from
    someone who holds it; keep Warsh's equivocation honest.
- `sources`: numbered in first-citation order, honest `data-nb-kind`.

Apply equal scrutiny to both sides; give each its strongest cited case and no
support the record does not hold. **No house conclusion. No component-vocabulary
headings** ("camp/thesis/argument/holder" as visible text). Title = the contested
question stated neutrally; dek = one sentence framing the disagreement, no side,
no hedged-contrast mold.

## Source obligations (strict gates)
min 10 sources, **≥4 primary, ≥3 secondary** (the record has 7+7). Verify the
vote, names, range, years-above-target, and tariff/energy attribution as the
evidence record does (FOMC statement cites "supply shocks… including energy"
without naming tariffs; tariffs appear in Warsh's remarks, Logan's speech, Moody's
modeling ~0.17pp vs ~0.66pp energy). Every URL resolves.

## Metadata (`nb-meta`)
Real values: `series: "unbiased"`, `slug: "should-the-fed-hike"`,
`template: "unbiased"`, `mode: "open"`, `order: null`, `date: "2026-07-31"`,
`tags: ["economics","monetary-policy"]`, measured counts, neutral `dek`,
`harness: "claude-code"`, `model: "claude-sonnet-5"`.

## Proof (run to BLOCK: 0 — strict)
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/unbiased/should-the-fed-hike/library/unbiased/should-the-fed-hike.html \
  --series unbiased --library /home/user/library
```

## Also write
`agent-artifacts/unbiased/should-the-fed-hike/writer/01/draft-handoff.md`: the
original contribution (assembling the two strongest cited cases with equal
scrutiny and the precise tariff-vs-energy attribution), final word/source counts,
unresolved WARNs.

## Request, don't guess
Missing evidence → `REQUEST researcher <need>`; missing voice → `REQUEST
writing-coach <need>`.

## Control signal
Return exactly one line (DONE only after BLOCK: 0):
`DONE writer agent-artifacts/unbiased/should-the-fed-hike/writer/01/draft-handoff.md`
or `REQUEST <owner> <need>` / `BLOCKED writer <reason>`.

## Scope discipline
`./nb` and web tools for focused work; the evidence record is your source of truth.
Do not tour the repo/archive.
