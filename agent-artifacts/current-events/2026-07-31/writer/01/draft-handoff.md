# Draft handoff — writer/01 — current-events/2026-07-31

## Original work
The evidence record is 13 independently verified facts and quotes spread
across four unrelated stories, with no argument or prose structure of its
own. The writer's one act of original work: turning that record into four
self-contained wire items that each satisfy the series' hard per-item
citation rule (`primary: [1,1]`, `secondary: [1,null]`), even where the
underlying story had two candidate primary documents (Item 1's Senate
Judiciary notice vs. DOJ Anti-Weaponization Fund release; Item 4's two
CENTCOM releases) — a real allocation decision the evidence record left
open, resolved here by choosing the primary source that owns the item's
lede fact and pulling any remaining figures the item needs from an
independent secondary that also verified them. The writer also converted
the researcher's flagged sourcing gap (Trump's Truth Social quote, gated at
403, verified only by convergent secondary) into prose that names NPR as
the source of the quote rather than presenting it as independently read
primary speech.

## Article and paths
- Article: `.nb-work/current-events/2026-07-31/library/current-events/2026-07-31.html`
- No chart or source asset used. The evidence record's Source assets note
  flagged two BEA bar charts as available for Item 3 and a possible
  political timeline for Item 1, but a 4-item wire brief with one-to-three
  sentence items had no argument that needed a chart to carry weight the
  prose couldn't; the numbers (1.5% vs. 2.1%, 3.9% vs. 1.7%, 5.7% vs. 3.6%,
  3.4% vs. 4.4%) are compact enough to state directly with their
  comparisons. No asset was added.

## Selection judgment (why these 4)
Followed the researcher's recommended 4-item slate exactly — Blanche AG
revolt, Rushdie federal terrorism conviction, Q2 GDP advance estimate, and
the Iran conflict's westward widening — because the researcher had already
verified each against a primary and searched hard for a fifth or sixth
without finding one that cleared the law/policy/institutions/material-
conditions bar inside the 7/30-31 window (see evidence.md's Discarded
section: TSA privatization pending a final vote, the CDC outbreak with no
fresh update, the Interlochen investigation as a private matter, HHS/Title
VI actions outside the window). Padding to 5-6 would have meant a weaker
item; the commission explicitly permits 4.

## Per-item source composition (as cited)
- Item 1 (Blanche): primary = Senate Judiciary Executive Business Meeting
  page (#1); secondary = CBS News on Judge Williams's collusion finding and
  the $1.776B figure (#2), NPR on Trump's Truth Social post (#3). The DOJ's
  own Anti-Weaponization Fund release (evidence source #2) was read and
  verified by the researcher but not cited in this item, since citing it
  alongside the Senate Judiciary page would have put two primary sources on
  one item against the series' exactly-one-primary rule; the $1.776B figure
  instead came from CBS, which states the same exact figure independently.
- Item 2 (Rushdie): primary = DOJ press release 26-866 (#4); secondary = NPR
  (#5).
- Item 3 (GDP): primary = BEA Report 26-35 (#6); secondary = Fox Business,
  carrying the LSEG forecast miss and the Pearce/Oxford Economics caveat
  (#7).
- Item 4 (Iran widening): primary = CENTCOM's Iraq-strikes release (#8);
  secondary = Saudi Gazette (#9, PMF's self-reported and explicitly
  unconfirmed casualty claim, and the U.S. ownership detail on the Damietta
  facility), CNBC (#10, the Damietta strike and the muted Brent reaction).
  CENTCOM's second release on the direct U.S.-Iran strikes (evidence source
  #11) was treated as prior-established context per the evidence record's
  own note and not re-cited; the item's news is the Iraq and Egypt
  widening, not the already-reported exchange itself.

## Handled honestly
- Item 1's Trump quote is attributed as "In a Truth Social post reported by
  NPR and other outlets," not presented as independently read primary
  speech, per the researcher's flag (Truth Social returned 403 to direct
  fetch).
- Item 4's PMF casualty claim (20 killed, 32 wounded) is attributed
  explicitly to Iraq's Popular Mobilization Forces and flagged as
  unconfirmed by CENTCOM or Saudi Arabia, per the researcher's contradiction
  note.
- Item 4 stays short and factual per the researcher's own uncertainty flag
  on whether this item clears the "consequence" bar; it explicitly builds
  on "the open exchange of fire" already covered in current-events rather
  than re-litigating the whole war, and does not touch the July 29 Fed hold
  (Unbiased's item tonight).
- Item 3 does not mention the Fed rate decision.

## Proof
```
./nb check .nb-work/current-events/2026-07-31/library/current-events/2026-07-31.html \
  --series current-events --library /home/user/library
```
Result: **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE.**

First run surfaced 4 BLOCKs (uppercase/spaced nb-meta tags — fixed to
lowercase slugs) and 2 WARNs (two run-on sentences at 62 and 57 words —
split each into two sentences) plus a stale word count in nb-meta (fixed
to the counted total, 786 words / 4 min). No warnings left unresolved.

## Remaining questions
None. Evidence and voice guide were sufficient for all four items; no
researcher or writing-coach request needed.
