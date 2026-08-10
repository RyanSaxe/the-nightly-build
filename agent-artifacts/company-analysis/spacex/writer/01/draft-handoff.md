# Draft handoff: company-analysis/spacex (writer 01)

## Original-work sentence

The article reconstructs a segment decomposition the filing never prints. It
annualizes the one reported quarter, sets the public market cap against the
February 2026 deal marks that priced SpaceX and xAI separately, and bounds the
profitable Connectivity business by a revenue multiple, to show that the
documented, profitable segment can account for at most a fifth of today's price
while the majority rests on the unprofitable AI unit and on Starship optionality
the filing gives no number to.

The work is visible in the two tables (the three dated market marks; what each
segment must assume), in the revenue-versus-capex chart that carries the
inversion, and in the "tenth to a fifth" bounding argument in "Splitting $1.75
trillion across three segments."

## Recast honored

Followed the commission's "Recast from research," not the superseded
two-business spine. Three reported segments (Space with Starship inside it,
Connectivity, AI); AI is the cash frontier (86% of Q2 capex), not Starship;
Starship treated as an unquantified sub-item of Space. No buy/sell/allocation
call.

Caveats honored: market cap stated as a range ($1.75-1.8T basic to ~$2.3T fully
diluted); lock-up figures quarantined in an "As reported" note attributing them
to coverage that cites the prospectus, since the prospectus body was unread; the
net loss ($541M) and operating loss ($143M) that carry weight are cited to both
the 10-Q and the earnings release, so no single fetch-converted GAAP line stands
alone under a headline; Connectivity's profitability is attributed to Sacra (a
secondary estimate), with the text stating the filing is not confirmed to break
out profit by segment.

## Proof result

`./nb check ... --series company-analysis --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 0**, verdict PUBLISHABLE. No warnings left
standing. Zero em-dashes. 2533 words, 11 sources (4 primary, 7 secondary), one
chart (chart-1.py + chart-1.png, revenue vs capex by segment, inspected).

## Open evidence / voice questions

1. **Segment profitability is not confirmed disclosed.** The whole
   operating-business bound leans on Connectivity being the one profitable
   segment, which rests on Sacra's estimate, not the 10-Q. If the 10-Q's segment
   note in fact discloses operating income by segment, a later round should
   replace the Sacra estimate with the primary and could tighten the "tenth to a
   fifth" range. Worth a researcher check against the filing's Segment
   Information note.

2. **The 10x-20x Connectivity multiple is illustrative, not sourced.** It is
   framed explicitly as the reader's lever ("pick the multiple yourself"), and
   the conclusion is built to hold at either end. Flagging that this is reasoned
   bounding rather than a cited comparable, in case the editor wants a sourced
   comparable added or the framing tightened.

3. **Headline carries a single market-cap figure ($1.75 trillion) while the body
   states the range.** Judged acceptable because $1.75T is the reported
   basic-share figure and the orientation and scaling sections give the full
   $1.75-2.3T range. Editor should confirm the single figure in display text is
   acceptable against the "state as a range" caveat.
