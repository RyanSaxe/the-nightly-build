# Draft handoff: current-events/2026-08-06 (writer 02)

Revision applying editor/01's required writer items with researcher/02's corrected
Michigan sourcing. Items 1, 2, 3, 5 and the editor's own item-2/item-5 fixes were
left intact except for the citation renumber forced by the item-4 source change.

## Editor requests resolved
- **Item-4 primary href (both headline `<a>` and s10).** Replaced the invalid
  `mvic.sos.state.mi.us` (a voter-lookup tool) with the ClickOnDetroit (WDIV)
  AP-widget results page,
  `https://www.clickondetroit.com/.../abdul-el-sayed-wins-2026-michigan-us-senate-democratic-primary-election-ap-projects/`,
  kept as `data-nb-kind="primary"`. It returns 200, lands on this exact race, and
  carries the Associated Press count (AP is the owning count authority; AP's own
  projects deep link, `apnews.com/projects/election-results-2026/michigan/`, 404s
  and could not be printed). The separate independent newsroom account (NBC News
  narrative report) stays as the secondary, s11.
- **Exact figures with reporting share and status.** The item now reports the AP
  count as El-Sayed 742,017, Stevens 727,091, McMorrow 61,344, at 86 percent of
  precincts reporting, stated "unofficial, pending the state canvass" (one
  snapshot, not mixed with NBC's ~98.8% percentages). Arithmetic checks:
  48.5 / 47.5 / 4.0 percent, margin 14,926 votes ≈ 0.98 point. The ~$65M outside
  money (>$30M AIPAC-affiliated) and ~9:1 ad advantage are kept as a separate,
  secondary-sourced (NBC) context number, distinct from the count.
- **Item-4 verdict recast.** Dropped the unsupported causal magnitude ("moved the
  result by roughly a point"). It now reads: "That advantage did not prevent a
  loss of about one point" — the supportable read (a ~9:1 ad edge failed to
  prevent a ~1-point loss), drawing on the count (s10) and the spending (s11).
- **Dek recast and synced.** Dropped the "front page" self-reference and the
  "held to account vs spared" theme the energy/elections items did not support.
  New dek (identical in `nb-meta` and `nb-dekline`): "A judge ends the last
  January 6 prosecution under protest, calling the dismissal an epilogue that
  excuses what that day did to the peaceful transfer of power." A committed claim
  about the day's lead event; no comma-triad, no hedged contrast, no self-grading.

## Other change
Removing the now-unused NBC results page (the second Michigan snapshot) dropped
the source count from 14 to 13, so item 5's citations renumbered: AJRCCM primary
s13→s12, NPR secondary s14→s13 (headline and body sups updated to match).

## Source kind note (item 4)
The evidence record labels the AP projects page "primary (owning authority)" and
the newsroom results pages "secondary." Because AP's own URL 404s, I followed the
editor's explicit directive and labeled the printed results page that carries the
AP count as the item's `primary`; it is the owning count (AP) a clicking reader
can actually reach. NBC's independent report remains the secondary. Per-item
sourcing holds: exactly one primary plus one independent secondary.

## Proof
`./nb check ... --series current-events` **with links included: BLOCK: 0, WARN: 0,
verdict PUBLISHABLE.** No warnings left standing. (An intermediate W-CITE-ORDER
from the renumber — the item-5 headline sup still pointing at the old s13 — was
fixed to s12.) `nb stamp`: words=956, reading_minutes=4, sources=13.

## Open question (non-blocking, carried from editor/01)
The editor flagged that NPR's own text may not carry HHS's "offered Acacia new
terms it refused" account that the evidence record attributes to it (item 2). The
researcher documented it and the editor did not block; unchanged this round, but
worth a confirming read on any future pass.
