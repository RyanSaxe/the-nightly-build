# Writer brief — investing/return-on-capital (01)

## Role
Load and follow `skills/writer/SKILL.md`. Draft from the exact brief, voice guide,
and evidence record; carry it through the proof to BLOCK: 0.

## Begin with these exact inputs (under `.nb-work/investing/return-on-capital/`)
- `agent-artifacts/investing/return-on-capital/editorial-direction.md`
- `agent-artifacts/investing/return-on-capital/commission.md`
- `agent-artifacts/investing/return-on-capital/writing-coach/01/voice-guide.md`
- `agent-artifacts/investing/return-on-capital/researcher/01/evidence.md`
  (7 read sources; Costco FY2025 worked ROIC ≈37.4%; AEP contrast ≈5-6.4% vs a
  ~4.36% utility WACC; Damodaran definitions; honest alternate conventions)
- The initialized article: `library/investing/return-on-capital.html`
- Generated context: `.nb-context/` (contract, runtime-assets, furniture — the
  lesson bookends `nb-bookend` are in `.nb-context/furniture`).

## What to write
`library/investing/return-on-capital.html`. Template `lesson`, **1200-2200 words**.
Fixed order: `why` bookend → body (flex 0-4 sections) → `takeaway` bookend →
`sources`. **Write the body first; write both bookends after**, about THIS
lesson's particulars. Bookends carry NO citations (cite-exempt).
- Teach, in order: (1) **invested capital** (from the balance sheet — the capital
  suppliers' claims / net operating assets); (2) **ROIC = NOPAT / invested
  capital**, worked once end-to-end with Costco's real FY2025 numbers from the
  evidence record (show the arithmetic: operating income $10,383M, ~25.13%
  effective tax → NOPAT ≈ $7,773M; invested capital ≈ $20,791M → ROIC ≈ 37.4%),
  stating the invested-capital convention you use and noting alternates honestly;
  (3) the **value-creation test**: ROIC vs the cost of capital, illustrated by the
  AEP contrast (ROIC ~5-6% against a ~4.36% utility WACC and its ~9-11% allowed
  ROE) — a capital-heavy business whose returns sit near its cost of capital.
  Teach cost of capital only to the depth this test needs; explicitly leave WACC
  computation and full valuation to a later lesson (leave ground for the course).
- Use furniture where it teaches: the worked ROIC is a natural `nb-equation` or a
  small `nb-table` of the inputs; do not decorate. Every number is sourced.
- Background band links the three prior lessons (relative links into this
  library): `how-a-business-earns-a-profit`, `profit-versus-cash`,
  `what-a-company-owns-and-owes`. Go deeper links point beyond the paper
  (e.g. Damodaran). The lesson must work for a reader who opens none of them.

## Permitted changes / decisions you own
- Name the body's flex sections for the steps of THIS lesson (invested capital →
  ROIC worked → the cost-of-capital test), not a generic outline.
- Headline/dek per `spec/headlines.md`. Bookends per the lesson identity: the
  `why` gives a real reason to read (this subject, where it's at work, what the
  reader will understand); the `takeaway` is what they keep, resolving what the
  opener set up; neither summarizes the body or teaches new terms.
- Preserve fixed engine assets/classes/labels/required HTML (incl. the bookend
  chrome: "Why this matters", "The takeaway", "Background", "Go deeper", "optional
  reading"). No added scripts/styles/iframes/forms/handlers/external images.

## Metadata (`nb-meta`)
Real values: `series: "investing"`, `slug: "return-on-capital"`,
`template: "lesson"`, `mode: "open"`, `order: null`, `date: "2026-07-31"`, honest
`tags` (e.g. `["accounting","valuation","roic"]`), measured counts, `dek`,
`harness: "claude-code"`, `model: "claude-sonnet-5"`.

## Proof (run to BLOCK: 0)
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/investing/return-on-capital/library/investing/return-on-capital.html \
  --series investing --library /home/user/library
```

## Also write
`agent-artifacts/investing/return-on-capital/writer/01/draft-handoff.md`: the
lesson's original teaching contribution (turning the three statements into one
judgment via ROIC and the cost-of-capital test, with the Costco/AEP contrast),
final word/source counts, unresolved WARNs.

## Request, don't guess
Missing evidence → `REQUEST researcher <need>`; missing voice → `REQUEST
writing-coach <need>`.

## Control signal
Return exactly one line (DONE only after BLOCK: 0):
`DONE writer agent-artifacts/investing/return-on-capital/writer/01/draft-handoff.md`
or `REQUEST <owner> <need>` / `BLOCKED writer <reason>`.

## Scope discipline
`./nb` and web tools for focused work; the evidence record is your source of truth.
Do not tour the repo/archive.
