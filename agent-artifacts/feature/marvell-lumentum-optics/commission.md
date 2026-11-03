# Commission: feature/marvell-lumentum-optics

Authorized by `nb duty` for 2026-11-03 (open section; topic chosen by the orchestrator).
Template: article. Strict: 600–1200 words hard limit, 2–4 flex sections, at least five sources.

## The assignment

On 2 November 2026 Marvell Technology and Lumentum announced a definitive agreement for Marvell
to acquire Lumentum in an all-stock deal (reported terms: 4.5 Marvell shares per Lumentum share,
an implied enterprise value of about $115 billion, ~67/33 ownership split, >$1 billion of
run-rate cost synergies claimed, a $550 billion combined addressable market claimed). The
researcher confirms every term against the filings; these figures are leads, not facts.

The question the piece answers: what, physically and financially, is Marvell paying for, and what
does the price require to be true? The piece places Lumentum's products (lasers, optical
transceiver components, optical circuit switches, co-packaged optics, whichever the filings and
Lumentum's own reports show matter) in the path a signal takes through an AI cluster, beside
Marvell's electrical parts (DSPs, SerDes, custom silicon), and then tests the price against
Lumentum's own reported revenue and growth.

The required original contribution: a drawing of where each company's products sit on one link
of an AI cluster, and a computation from the filings of what the price implies (for example
price over trailing revenue, or what revenue growth the multiple assumes), set against
comparable figures the sources supply. Say in one sentence what the sources did not do.

## Boundaries

- Report what the filings and the companies' own documents state; attribute forecasts and
  addressable-market figures to the party claiming them.
- The CEO email's "approximately $100 billion" against the release's $115 billion enterprise
  value is a lead. Resolve the gap from the filings (equity value against enterprise value, or
  a different share-price date), and report it only if it teaches something.
- Analyst views only with a named analyst and firm, and only for a point the filings cannot make.
- Regulatory review and closing conditions get space only as the filings state them.
- No investment advice, no price targets.

## Visuals

Build each section around a visual: an inline SVG of one optical link (switch ASIC → electrical
SerDes/DSP → laser/modulator → fiber → …) marking whose parts are whose; a computed comparison
of the price against revenue (nb chart or inline SVG); a table only where a comparison of a few
terms is the point.

## Neighbours in this edition

- daily-brief/2026-11-03 is barred from covering this deal.
- feature/micron-fy2026-memory-scarcity (published earlier) covered AI-driven memory supply;
  do not reuse its scarcity framing. This piece is about interconnect.

## Recent patterns to break (from the last four features)

- Deks pack two figures and close on a contrast clause introduced by "where" (Binance: "…where
  Bybit's 2025 haul held no stablecoin…"; AstaBench: "…where its sub-agent…"). Do not use a
  "where" contrast clause in the dek.
- Every recent feature ends on a section about the limits of the evidence ("Binance has walked
  back its breach path, and the attributions are assessments"; "Only three designs have an
  overall cost"; "Ten issues survived to rc-22"). Do not make the final section a caveats
  roundup; put a caveat where the claim it limits sits.
- Headlines built as "X finds Y among N" or "Swapping X moves Y …". Find a different build.

## Production

Policy (balanced, series override writer effort high): writing-coach capable/low, researcher
capable/high, writer capable/high, editor inherit/high (required). Runtime mapping: capable =
sonnet; inherit = this orchestrator's model.

## Run log
- writing-coach/01: sonnet, low effort. Voice guide accepted as is; the domain gap in its exemplars (no free optics/M&A piece) is accepted, and no second invocation was run.
- researcher/01: sonnet, high effort. Evidence accepted.

## Decisions after evidence (orchestrator)

- The "approximately $100 billion" lead is Hurlston's employee FAQ (Rule 425, 000119312526443871).
  The piece may show that both figures reproduce from the Merger Agreement's capitalization
  (common shares only vs fully diluted less cash), labelled as the paper's reconstruction. It may
  not say which one the FAQ meant.
- $115B is a value at Marvell's 28 October price. Say so. The post-announcement moves may appear
  only as CNBC reported them (percentages, attributed). Do not print the Yahoo quote-box prices or
  a dollar value computed from them: no verified close.
- Price-over-revenue multiples are the paper's computation from the filings; label them as such.
  The Marvell-own-multiple comparison is optional and, if used, labelled and dated, with the
  warrant exclusion stated.
- The $550B TAM is the companies' claim; the piece can show what it is built from and that the
  overlap is unstated, attributed to the decks and call.
- The shortage question: quote the named analyst (Arya, BofA) only for the question; Lumentum's
  own filings supply the supply/backlog and customer-concentration facts.
- Reopen any summarizing-fetch page before quoting its wording.
- writer/01: sonnet, high effort. Proof BLOCK 0 WARN 0, 1192 words.
- editor/01: inherit model, high effort. Approved; CNBC share moves cut (403), accepted.
