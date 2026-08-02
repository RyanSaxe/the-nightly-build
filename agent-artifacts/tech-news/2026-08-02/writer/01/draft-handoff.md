# Draft handoff: tech-news/2026-08-02 (writer, round 01)

## Original work
This article's one act of original work: no cited source draws the contrast
this piece's spine rests on. Each source covers exactly one development in
isolation. The writer built the explicit comparison between the EU's Article
50 deadline landing on schedule (with a Commission FAQ and independent
compliance guidance already published around it) and the US executive
order's parallel 60-day deadline passing with nothing public to show, and
used that comparison as the frame connecting item 1 and item 3. The writer
also converted each item's raw quotes and figures into one governing
judgment sentence per item that no single source states as a verdict: that
OpenAI's own case studies and the outside researchers criticizing them
converge on the same validation gap from opposite directions (item 2), and
that the number worth trusting about DeepSeek's release is the independent
benchmark run two days later, not the vendor's own release notes (item 4).

## Paths changed
- `/home/user/the-nightly-build/.nb-work/tech-news/2026-08-02/library/tech-news/2026-08-02.html`
  (edited the initialized skeleton in place; no new assets or chart scripts
  were created — no chart or source asset cleared the evidence record's bar
  for use).

## Proof result
`nb check ... --series tech-news --library /home/user/library` →
**BLOCK: 0, WARN: 0, verdict: PUBLISHABLE**.

Along the way: item 1 initially cited two sources the evidence record
classifies as primary (the artificialintelligenceact.eu mirror of Article
50's text, and the European Commission's own Article 50 FAQ), which tripped
the series' one-primary-per-item rule. Resolved by judgment, not by relabeling
to dodge the count: digital-strategy.ec.europa.eu is the regulator's own
institutional domain stating its own enforcement position, the truest primary
for the penalty and grace-period facts drawn from it, while
artificialintelligenceact.eu is a third-party tracker site that reproduces
the operative text faithfully but is not itself an EU institution — closer to
an independent secondary reproducing the primary language. Six
W-SENTENCE-DENSITY warnings and one W-CITE-ORDER warning were fixed by
splitting run-on sentences and renumbering two source pairs to match true
first-citation order. No warnings were left standing.

## Sourcing notes carried from the evidence record
- Item 2's primary (openai.com/index/scientific-computing-agentic-ai) was
  retried directly and still returns HTTP 403 (confirmed bot-blocking, not a
  dead link). Per the brief, it is cited as the primary of record; every
  figure in the item is attributed to the two independent sources that read
  the report directly (The Decoder, michaelbriancotter.wordpress.com), and
  the 99.8% aligner-parity figure is attributed to The Decoder by name, not
  asserted as OpenAI's own confirmed number. The unverified "1,610→27
  seconds" figure was not used.
- Item 3 frames the missed deadline as "as of July 31, per Forkast's
  reporting" rather than a flatly established government failure, per the
  evidence record's caution that only one independent account confirms it.
  The unverified Kush Desai quote was not used.
- Item 4 leads on Artificial Analysis's independent benchmark run, not the
  release event, per the brief. "Open-weight release" is not asserted as
  settled; the item states the unresolved weight-availability question
  directly, attributed to digitalapplied.com, and flags the Terminal Bench
  figure as vendor-stated and unreproduced.

## Remaining questions
None outstanding for this round. If a revision surfaces new evidence needs
(e.g., independent confirmation of the EO 14409 "missed deadline" claim, or
resolution of the DeepSeek weight-availability contradiction), those would
need a new researcher artifact rather than the writer expanding the claim
set independently.
