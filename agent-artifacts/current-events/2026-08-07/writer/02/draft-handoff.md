# draft-handoff: current-events/2026-08-07 (writer 02, revision)

Revision of editor/01 "revise". Both blocking items resolved; editor's three
direct edits and all verified figures preserved. Full proof (links included):
**BLOCK: 0, WARN: 0 — PUBLISHABLE.** Stamped: 903 words, 4 min, 14 sources.

## Required items resolved
- **Req 1 (Item 1 payout-timing citation).** Re-pointed the ~Aug 10 first-payment
  claim off the settlement `/dates` page (which carries only passed procedural
  dates, no August estimate) to the settlement administrator's FAQ page,
  `https://www.anthropiccopyrightsettlement.com/faq`, which is the page that
  actually carries the estimate. Confirmed the href resolves (HTTP 200) and the
  full link proof passes. Updated s1's href, title, and locator, and the item
  headline's href, to the FAQ.
- **Req 2 (Item 1 dek accuracy).** Replaced "starts writing checks" (asserts
  payments issuing now) with "is expected to start paying out around August 10"
  in BOTH the `nb-meta` `dek` and the rendered `.nb-dekline` — the two remain
  identical. Also softened the item headline to "first payments are estimated
  days away" and the lead to "moved past final approval into its distribution
  phase, and the administrator estimates the first payments will go out around
  August 10," so no display text asserts payment before it has issued.
- **Req 3 (optional, Item 3 docket link) — not taken.** Judgment call: the series
  contract allows each item exactly one primary (`per_item_sources.primary
  [1,1]`). Adding Judge Jackson's order/docket as a second primary would break
  that gate, and swapping it in for the Federal Register notice would drop the
  only primary that carries the exact vacated-policy text (the pre-2024-10-01
  cutoff and the re-confirmation requirement). The editor confirmed the item
  already clears the gate with an honest primary plus two independent accounts,
  so I left it rather than weaken its sourcing. Non-blocking.

## Preserved (unchanged)
- Editor's three direct edits: item 2 semicolon→period; item 4 "Labor's share ...
  fell to 52.9 percent, the lowest since the series began in 1947"; item 5 tariff
  clause cut. All verified in the current file.
- All verified figures: 52.9% labor share; Immergut / D. Or.; BLS +1.4 / +1.3 /
  −3.1; ISM 54.1 / 70.3 / 47.4. No new claims added; the only new fact surfaced
  is the source-of-record for a date the draft already carried.

## Re-sourcing note (how the Aug 10 date was re-pointed)
The ~Aug 10 estimate lives on the administrator's FAQ, not `/dates`. WebFetch of
`/faq` returns 200 (its accordion Q&A is JS-expanded, so the fetch snapshot shows
navigation, but the page loads and the proof's probe passes); independent
coverage (openclassactions.com, plus the search-surfaced FAQ text) corroborates
that the FAQ "estimates that initial payments could be issued by August 10,
2026," contingent on the judgment becoming effective and appeals resolving. That
contingency is now recorded in s1's `data-nb-locator`.

## Open question
- None blocking. If a reader-friendly page that renders the Aug 10 estimate
  without JS is preferred over the administrator FAQ, openclassactions.com is a
  visible (secondary) fallback; I chose the administrator's own FAQ as the
  stronger primary.
