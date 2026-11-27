# Commission: feature/microsoft-365-gateway-cascade

Run date: Friday 2026-11-27 (scheduled, from `nb duty`). Template: article. Strict:
600-1200 words, 2-4 flexible sections, at least five sources.

## What the article is

A five-minute feature on Microsoft's final post-incident review (PIR), dated
20 November 2026, of the Microsoft 365 outage of 12-14 November 2026. The piece explains
the failure as a mechanism: a latent lock-contention defect, present since a July
deployment and visible only on newer high-core-count gateway servers, fired when
routine conditions coincided (about 14% of gateway capacity out for maintenance, a
Teams failover, the US-East morning peak); traffic redistribution meant to contain a
failing unit carried the overload to the remaining units and then across regions; and
recovery took about a day because servers that rejoined were knocked over again by
reconnecting clients, a loop the repair list addresses only with an undated item for
admission control.

The finding to open on: why a defect that sat quietly for months took the service down
worldwide within about four hours and kept it down for a day, in the PIR's own
account. The piece's original work is to assemble the PIR's scattered timeline and
causal factors into one drawn mechanism and one timeline, and to set the preliminary
(15 November) report's account beside the final one's, saying what the final added.

## Angle boundaries

- This is a mechanism and timeline piece. It is not a "the vendor's number is wrong"
  piece; recent features all took that shape (see the pattern notes).
- The PIR is Microsoft's own account. Say so once, plainly, and separate what the PIR
  states from what the piece infers. Where the piece draws on the general literature on
  metastable failures (Bronson et al., HotOS 2021; Huang et al., OSDI 2022) to name the
  recovery loop, cite it and keep the PIR's facts separate from the literature's frame.
- Provenance: the final PIR circulates as a mirror of the admin-center document
  (EX1550543 / MO1550821). The researcher must establish the best available copy and
  how it is known to be the document Microsoft issued (matching text in Microsoft's own
  pages, the Microsoft 365 Status account, press quoting it). If authenticity cannot be
  established, the article cites the mirror and says what it is.
- The 14 November daily brief reported the outage before the cause was known; this piece
  must stand on its own and need not reference it.

## Visuals the piece is built around

1. An inline-SVG mechanism diagram: defect plus load conditions, failing units, traffic
   shift, cross-region spillover, and the rejoin-overload recovery loop.
2. A UTC timeline from the first event on 12 November to resolution on 14 November.
3. Optionally, a compact comparison of the preliminary and final reports' causal
   factors, or the 13 repair items by category and due date. Choose one; do not add
   both if the word band cannot carry them.

## Production record

- Writing coach low/capable; researcher high/capable; writer high/capable (series
  override); editor inherit/high (required).
- Neighbours this run: daily-brief/2026-11-27 (must not carry the M365 PIR) and
  reinforcement-learning/factored-action-spaces.
- Recent-pattern notes: `.nb-work/notes/recent-patterns.md`.
- Scout's downloaded copies of both PIRs: `researcher/01/source-copies/` (unverified;
  the researcher confirms them against their sources).

## Orchestrator amendments after research (researcher/01)

These supersede the "What the article is" section where they conflict.

- Spread timing: use the PIR's own words and starting point (p.8): broad North American
  failures from about 16:00 UTC on 12 November, and every region affected within about
  two hours of that. Drop "about four hours".
- Length of recovery: lead with the PIR's own three reasons from its Executive Summary
  (p.2): locating a change made months earlier, restarting each server twice, and
  rolling the fix across the fleet. The rejoin-overload finding comes from the body
  ("Why recovery took longer", p.8) and Next Steps row 8; present it as one of the
  PIR's findings, not as the main cause.
- "Metastable": the piece may use the term only as its own reading, labelled as such,
  and must say that in the PIR the rejoined servers failed again while the defect was
  still deployed, which differs from Bronson et al.'s definition (persisting after the
  trigger is removed). If the label cannot be used honestly in a sentence or two, leave
  it out and describe the loop plainly.
- Admission control: the one repair item written against the rejoin finding is TBD; say
  that exactly, and do not count the CY27 Q1 recovery-procedures item as addressing it.
- Provenance: cite the 365Fanatic copy as a third-party copy of the admin-center
  document, with the corroboration recorded in the evidence (status-account posts,
  Lamanna's post for the preliminary). State once that every figure is Microsoft's own.
- Figure 1 tension (unhealthy servers rising steeply only after about 17:20 UTC against
  "broad failures at approximately 4:00 PM"): do not reproduce the figure as data; if
  the timeline needs the discrepancy, state it in one sentence.

## Record note

The scout's PDF copies named in researcher/01/brief.md as `source-copies/` were moved
out of the artifact record to the workspace's `source-copies/` before publication; the
artifact contract allows only each role's brief and output. The editor confirmed the
cited 365Fanatic and next.ink PDFs match them by SHA-256.
