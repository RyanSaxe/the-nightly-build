# Writer handoff: feature/microsoft-365-gateway-cascade (01)

## Original work

The article takes the final report's four factors, its spread section, its recovery section and the Actions Taken table, which are spread across 14 pages, and draws them as one mechanism with two loops (Fig. 1) and one UTC timeline drawn to scale with computed phase lengths (Fig. 2). It sets the preliminary report against the final in a four-row table, and checks the repair list against the two loops: the spread items are dated and the rejoin item is TBD.

## Proof

`nb check ... --series feature --repo /home/user/the-nightly-build` with links: BLOCK 0, WARN 0, PUBLISHABLE. Stamped 1188 words, 5 sources, 5 min. No warnings were left standing.

The word count includes SVG label text, the table and the source list, about 450 words together. To fit the 1200 cap I cut the timeline to 10 events (00:30 connection-negotiation finding and 08:00 stability confirmation dropped), cut the table to four rows (Teams-failover row dropped), and kept prose to roughly 700 words.

## Commission amendments applied

- Spread timing: about 16:00 UTC broad failures, every region within about two hours. "Four hours" appears nowhere.
- Recovery: the three Executive Summary reasons lead. The rejoin loop is presented as the report body's added finding (p.8), corroborated by the @MSFT365Status 00:06 UTC post.
- "Metastable" is labelled as an outside reading. The text says that it fits only in part, because the servers re-failed while the defect was still deployed, and that the report never shows a patched server overwhelmed.
- Admission control is stated as TBD. The CY27 Q1 recovery-procedures item is described as covering the slow rollout of the fix, not the loop.
- Provenance: the 365Fanatic copy is named as a re-save of the admin-center document and corroborated by the status account. Lamanna is cited for the preliminary. "Every figure here is Microsoft's" is stated once.
- Figure 1 tension: left out. The commission made it optional, and Fig. 2 does not reproduce the PIR chart.
- Contradictions handled in prose: ~16 h against the computed 14 h 53 min; 23 h 50 min of impact against 35 h 55 min to resolution; the 14% cause and the bulkhead "separate issue" (in the table and the text).

## Visual checks (nb preview + Playwright, Chromium)

Fig. 1, Fig. 2 and the table were captured at 375 px and 1280 px, each in light and dark (`colorScheme` emulation). In all four cases the page scrollWidth equals the viewport width, so there is no horizontal page scroll. Fixes made after looking:

- The day separators in Fig. 2 struck through the "13 Nov" and "14 Nov" labels. The labels now sit above their lines.
- The healthy phase in Fig. 2 was drawn in the red series color. It is now a neutral gray, and the colors match Fig. 1: red for the defect and spread, amber for lockups, green for the revert.

Labels do not overlap and arrows reach their boxes in all four captures. On a phone the table scrolls sideways inside its runtime wrapper to show the 20 November column, which is the documented `nb-table` behavior.

## Open questions

None blocking. The editor may want to restore the 08:00 "patched capacity holds" event if the word budget is rebalanced. The 07:20 event and the prose already state the revert.
