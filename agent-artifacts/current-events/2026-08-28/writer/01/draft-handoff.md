# Writer draft handoff: current-events/2026-08-28 (01)

## Original-work sentence

The article picks the day's four most consequential U.S. developments and, on
the two contested ones, sets each official claim beside the party that disputes
it — reporting inflation from the BEA's PCE index (3.7% headline / 3.3% core)
rather than the more-quoted CPI reading, and framing CENTCOM's "cleared lanes"
against Iran's four conditions and the Joint Maritime Information Center's still-
SEVERE rating — so the reader can tell an owned figure from an asserted one. The
evidence record lists these contradictions in the abstract; the article turns
them into the reader-facing frame of each item.

## Proof result

Command run (links included):
`./nb check .nb-work/current-events/2026-08-28/library/current-events/2026-08-28.html --series current-events --library /home/user/library-checkout`

Result: **BLOCK: 2, WARN: 0** (link-check clean; DOJ primary returns 403, which
the proof treats as non-blocking).

Both blocks are the same structural gap, not prose:

- `B-SOURCE-KIND  item #3 cites 0 primary source(s)` — the Hormuz item.
- `B-SOURCE-KIND  item #4 cites 0 primary source(s)` — the White House ballroom item.

I could not clear these honestly. The series enforces exactly one primary per
item (`nb source-policy --series current-events`: primary [1,1], secondary
[1,null], min 5 sources). Two items reach that bar cleanly from the opened
evidence: the China-hacking seizure (DOJ primary + Reuters) and the
inflation/sentiment item (BEA primary + Reuters). The other two have **no
linkable primary in the evidence record**:

- **Hormuz (item 3).** The owning primary is Adm. Cooper's CENTCOM video
  statement. The researcher recorded it "NOT OPENED" with no URL ("posted to
  CENTCOM's official channels (X)"), only instructing that the writer link the
  statement itself. gCaptain and Al Jazeera (both secondary) are all the opened
  evidence carries. I did not invent a CENTCOM URL or self-research one, since
  that would add a claim/source outside the researcher's opened set and cite a
  video I cannot verify.
- **Ballroom (item 4).** The owning primary is the Roberts administrative-stay
  order on the SCOTUS docket, also "not opened here" and with no URL; only
  SCOTUSblog (secondary) is opened. This item is additionally **stale** (the
  stay issued Aug 21, a week before this brief) and was not among the fresh
  materials the brief named — it is the most disposable of the four.

Warnings intentionally left: none. The one W-SENTENCE-DENSITY the proof first
raised was fixed (split three list-heavy sentences; removed the ballroom
semicolon).

## Open evidence question (owner: researcher / orchestrator)

The template floor is 4 items, but the opened evidence supports only 2 fully
compliant ones. To reach a proven 4-item brief without loosening the source
rule, I need, per item that currently blocks:

1. **A resolvable primary URL for the CENTCOM / Adm. Cooper mine-clearing
   statement** (the X post or a CENTCOM/DVIDS page carrying it). With it, item 3
   is complete as written — add the source entry as a new primary and cite it in
   the item's first paragraph.
2. **Either** a resolvable primary URL for the Roberts administrative-stay order
   (SCOTUS docket; prior coverage on 2026-08-16 referenced No. 26A203) if the
   desk accepts the week-old item, **or** a fresh fourth development documented
   with its own primary + secondary to replace the stale ballroom.

Splitting the inflation/sentiment item into two does not help: the UMich portal
(the sentiment owner) was opened but did not carry the August 51.0 print, so a
standalone sentiment item would rest its headline number on the Reuters
secondary — gaming the primary slot. Keeping inflation and sentiment as one
BEA-primary item is the honest structure.

All prose, furniture (economy stat strip; Hormuz "Iran's terms" note), nb-meta,
and the two valid items are finished, so supplying the two URLs is a
short path to BLOCK: 0.
