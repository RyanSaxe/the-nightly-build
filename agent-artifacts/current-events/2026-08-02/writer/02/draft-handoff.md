# Draft handoff: current-events/2026-08-02 (writer 02) — round 02 revision

## Original work

Unchanged from writer/01: the article's original act is the selection-and-
consequence judgment applied to each surviving item. This round narrows that
set by one (item 5 cut) and corrects two claims to match what their sources
actually say; it does not add a new candidate or expand the claim set.

## Editorial items resolved

- **Item 5 (Minnesota prediction-market injunction) — CUT.** Researcher
  round 3 exhausted every route (CourtListener docket/API, both
  CourthouseNews filenames, PacerMonitor, Bloomberg Law, the Minnesota AG's
  own memo bytes, CFTC's press room, web.archive.org, DocumentCloud/Scribd)
  and still could not produce a read primary; the order's holding survives
  only through secondaries. Removed the COURTS item div and its three
  sources (former s11/s12/s13) cleanly. The remaining citations (s1-s10)
  were already in first-citation order before the cut, so no renumbering
  beyond the deletion was needed — no orphaned source IDs, no gap in the
  sequence. Four items remain (Iran, water cyberattacks, wildfire, visa
  bond), which satisfies the 4-6 band.
- **Dek — replaced.** The prior dek asserted the Minnesota freeze, which no
  longer exists in the article. New dek: "The same day, federal
  investigators were probing a suspected Iran link in a hacking campaign
  against water utilities in at least seven states." One lean sentence,
  states a fact the headline doesn't carry, avoids the three banned dek
  molds (no semicolon reversal, no suspended question, no comma triad).
  Confirmed by direct comparison: nb-meta `dek` and the rendered
  `.nb-dekline` text are character-identical.
- **Item 1 Saudi sentence — recast.** Replaced "phoned him urging the
  cancellation" with NPR's actual language: Mohammed bin Salman "spoke with"
  Trump and "emphasized the necessity of prioritizing dialogue to
  de-escalate tensions," still cited to NPR (s2). This is new prose per the
  editor's routing, not a reversion of either of the editor's two direct
  cuts (the Mehr descriptor and the visa-bond "same terms" clause both stay
  cut).
- **Item 2 (s4) note — corrected.** The `data-nb-note` no longer claims the
  PSA "could not be decoded directly." It now reads: "This PSA's text is
  readable and directly supports the incident details cited to it here;
  AP/ABC News independently corroborates the scale and the suspected Iran
  link." `data-nb-kind="primary"` on s4 is unchanged, per the editor's
  acceptance.
- **Iran mirror-as-primary (s1) and the all-caps "OPENING OF THE HORMUZ"
  quote — untouched**, per the brief and the editor's sourcing calls
  1 and 3.

## Headline/dek/lead display-text check

- Headline references no item count and no item-5 content; unchanged and
  still accurate to the 4-item article.
- Dek rewritten as above; no longer references Minnesota or item 5.
- No item heading or lead sentence in the surviving four items referenced
  Minnesota or a five-item count.

## Proof result

`nb stamp`: words=532, reading_minutes=2, sources=10.

`./nb check .../2026-08-02.html --series current-events --library
<checkout>` (links included): **BLOCK: 0**, verdict PUBLISHABLE.

One warning intentionally left, carried from round 1 unchanged:

- **W-PLACEHOLDER** — `'OPENING OF THE HORMUZ'` flagged as a surviving
  all-caps run. This is Trump's own verbatim capitalization from the cited
  Truth Social post, quoted intact per the editor's sourcing call 3 (keep
  verbatim; paraphrase would misquote the primary or assert a disputed term
  as the paper's own). Left standing on purpose, same as round 1.

No open evidence or voice questions remain for this round.
