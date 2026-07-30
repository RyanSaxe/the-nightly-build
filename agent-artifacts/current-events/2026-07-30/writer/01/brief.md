# Writer brief — current-events/2026-07-30 (brief template)

## Inputs (begin here, write only the named outputs)
- editorial-direction.md (governing stack) — in this artifact dir.
- voice-guide.md — writing-coach/01/.
- evidence.md — researcher/01/. This is the complete claim set. Do not add
  claims or sources beyond it.
- Initialized article: `.nb-work/current-events/2026-07-30/library/current-events/2026-07-30.html`
- Template context: `.nb-work/current-events/2026-07-30/.nb-context/`.

## Build
- Author 4 items (band is 4-6; significance, not count, decides — evidence
  supports exactly these four cleanly). Order by consequence:
  1. Iran/US direct military exchange (tag: National Security)
  2. Fed holds 9-3, three governors dissent for a hike (tag: Monetary Policy)
  3. CMS ends the Part D premium-stabilization subsidy (tag: Health Policy)
  4. Consumer confidence slides a third month on present conditions (tag:
     Household Economy)
- Each item: exactly ONE primary + at least ONE independent secondary, per the
  evidence record. Number sources in first-citation order. Carry honest
  `data-nb-kind` (primary/secondary). Every cited URL must resolve.
- Each item is a judgment about why it matters, not a recap. Follow the voice
  guide: open on the development; state the judgment as a fact; carry each number
  with a comparison; end on the consequence, not a line handed back to the reader.
- Address the record's contradictions in the prose: the Fed hold is a *hawkish*
  hold (show the 9-3 split and the chair's "no tolerance" line); confidence's
  real signal is the sub-indexes, not the -1.4 headline; CMS "could/likely"
  raise premiums, not "will by $X"; Iran attack was July 28 (intercepted), US
  strikes late July 29.
- No source asset, no chart (evidence recommends none). No active content.
- Fill nb-meta with actual values: title, dek, measured words, measured sources
  (8), reading_minutes, tags array, harness "claude-code", model
  "claude-opus-4-8", date "2026-07-30", series "current-events", slug
  "2026-07-30", template "brief", mode "rolling", order null, protocol "1.1".
- Title: a headline that names the day's biggest development or the through-line
  (a Middle East war meeting a strained US economy). No colon-subtitle. Dek adds
  what the title leaves out; no hedged-contrast mold; check it is a claim, not a
  grade of the selection.

## Non-repetition
No re-run of the 07-28 SCOTUS voter-list, 07-27 Rogoff suit, 07-26 Iran
"officials say." The Iran item here is the actual exchange, a genuine new
development; note the continuity in a clause if useful, then give the new fact.

## Original work
Name the piece's one act of original work in draft-handoff.md (the front-page
judgment the four verified developments make together, which no single source
states). Single-context run: record production mode honestly.

## Proof
export PATH="/root/.local/bin:$PATH"
./nb check .nb-work/current-events/2026-07-30/library/current-events/2026-07-30.html --series current-events --repo . --library ../library
Drive to BLOCK: 0; treat WARN as revision notes.

## Outputs
Edit the article HTML; write writer/01/draft-handoff.md.
