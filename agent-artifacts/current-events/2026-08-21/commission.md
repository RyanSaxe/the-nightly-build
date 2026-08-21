# Commission: current-events/2026-08-21

## Assignment
The US front page for Friday, 2026-08-21. Four to six items, each an event that
changes law, public policy, public institutions, or people's material
conditions on or around this date. Significance selects the items; there is no
topic quota and no world-news quota. Include an international item only where
omitting it would mislead the US reader.

## Boundaries
- Template `brief`: 4-6 items, per-item citation. Minimum 5 sources overall.
- Each item carries its primary record and at least one independent account
  (per-item sources: primary exactly 1, secondary 1 or more). Prefer a reputable
  US newsroom for the independent account; use the primary record whatever its
  country; use non-US reporting when it is closer to the event or holds the
  original reporting.
- Put a technology story here only when its *public* consequence is the news.
  A development inside the field belongs to Tech News, which runs the same night.

## Required contribution
Each item explains why it matters in this paper's terms: the reported facts are
premises for a one- or two-sentence analysis, not a recap of the headline.
Commit to the consequence the evidence supports.

## Coordinate with tonight's edition
- Tech News (2026-08-21) runs the same night. Do not duplicate its items; if a
  story has both a public-consequence angle and a field angle, take only the
  public-consequence angle here and leave the field angle to Tech News.
- Unbiased (2026-08-21) is running a deep two-position piece on the Maryland
  data-broker privacy complaint (brokers selling ALPR/location data to police
  and ICE). If that story warrants a spot here, keep it to one plain factual
  item and do not argue the two sides; the Unbiased desk owns that treatment.

## Do not repeat recent coverage
The last two weeks already covered: record White River flooding / Indiana
emergency, the childhood-vaccine-schedule narrowing, the egg recall, measles
elimination status, Somali TPS termination, Tohono O'odham border-wall ruling,
the mail-voting SCOTUS filings, the birthright-citizenship order and ACLU suit,
the Epstein records unsealing, the July payrolls drop, and the Blanche
confirmation. Select this date's own developments; a genuine new turn in one of
those threads is fine, a restatement is not.

## Production record
- Correspondent (coach + research + draft + self-proof): model
  `claude-sonnet` tier, high effort for research.
- Editor (fresh eyes, required): model `claude-opus-4-8`, high effort.
- nb-meta: harness `claude-code-routine`, model `claude-opus-4-8`, date
  `2026-08-21`.
- Proof: `nb check .nb-work/current-events/2026-08-21/library/current-events/2026-08-21.html --series current-events --library /home/user/library-checkout`

## Recent patterns to break (from the last two weeks' briefs)
The editor holds the draft against these; a catchphrase shows only across issues.
- Dek: avoid the two-clause dek joined by "and" with an "on a day that also…"
  or "ruling that…" tail. Write one dek that identifies this date's lead.
- Openers: avoid the flat official-plus-date lede ("President Trump approved an
  emergency declaration for Indiana on August 16…") as an item's first sentence.
- Closers: avoid ending each item on an editorializing "X, and Y" parallel
  synthesis sentence. Let the analysis land inside the item, not as a stamped tag.
- Headlines: vary construction; recent items nearly restate the dek as an
  active-verb clause naming the official ("Trump approves…", "Judge Leon
  denies…"). Not every item headline should be actor-verb-object.
- "As of [day]" and running casualty/outage tallies as a closing beat have
  recurred; do not reuse a prior day's item facts verbatim.
