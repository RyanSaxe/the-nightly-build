# Commission — unbiased/should-the-fed-hike

## Assignment
One Unbiased article on a genuinely contested US question made timely by a
current event: **Should the Federal Reserve be raising interest rates now, or was
it right to hold?** The event: the July 29, 2026 FOMC meeting, at which the Fed
held its target range (reported 3.5%-3.75%) by a **9-3 vote**, with three regional
presidents — **Beth Hammack (Cleveland), Neel Kashkari (Minneapolis), and Lorie
Logan (Dallas)** — dissenting in favor of a 25bp hike, the most dissents in one
direction since September 2016, against inflation that has run above the 2% target
for more than five years amid tariff- and energy-driven price pressure.

Present the strongest evidence-backed case for EACH answer. The paper does not
choose. No house conclusion.

## The two positions (define from the real disagreement, name as serious holders would)
- **Position A — Raise now (break the persistence).** Inflation above target for
  five-plus years risks un-anchoring expectations; real policy is not restrictive
  enough; waiting lets a supply shock become embedded. Named holder: one of the
  three dissenters with a cited statement of their rationale (Hammack, Kashkari, or
  Logan) — use the dissenter whose public reasoning is best documented.
- **Position B — Hold (don't hike into a supply shock).** The current inflation is
  driven by tariffs and an Iran-linked energy spike, which are relative-price /
  supply shocks that a rate hike cannot fix and would worsen by squeezing a
  strained economy and a cooling labor market; monetary policy acts with long lags.
  Named holder: the FOMC majority position via Chair Jerome Powell's cited
  statement / the meeting communication, and/or a named economist making the
  hold case.

Apply the same standard of evidence and scrutiny to both. Fairness is not false
symmetry: give each the strongest support the record allows and no support it
does not. Steelman each before the reader weighs it.

## Reader / register
Paper's declared reader (math/CS, ML-engineering career, well-read; quantitatively
comfortable). Define any monetary-policy term of art at first use (dual mandate,
core vs headline, real rate, relative-price shock, expectations anchoring). Do not
assume economics training; do not talk down.

## Template / paths / metadata (strict)
- Series `unbiased`, mode `open`, template `unbiased`, STRICT.
- Structure: `orientation` (context before the two positions) → the `nb-divide`
  with **exactly two** `nb-side` sections, each carrying the four mandatory slots
  in order (camp name `nb-side-camp`, thesis `nb-side-thesis`, argument
  `nb-side-argument`, named holder `nb-side-champion` with a cited statement and
  standing) → `sources`. No extra sections, no house conclusion, no stock headings
  from the component vocabulary.
- Title = the contested question stated neutrally; dek = one sentence framing the
  disagreement, taking no side, no hedged-contrast mold.
- nb-meta: `mode: "open"`, `order: null`, `date: "2026-07-31"`, tags e.g.
  `["economics","monetary-policy"]`, `harness: "claude-code"`,
  `model: "claude-sonnet-5"`, measured counts.
- Article: `library/unbiased/should-the-fed-hike.html`.

## Source obligations (strict)
- **min 10 sources**; **primary ≥ 4**, **secondary ≥ 3**.
- Primary = the party's own record: the FOMC statement and implementation note
  (July 2026), the meeting's press-conference transcript, individual Fed
  presidents' own speeches/statements of their dissent rationale, BLS/BEA
  inflation releases (CPI/PCE), and any position holder's own words. Secondary =
  reputable independent reporting/analysis (WSJ, Bloomberg, NYT, FT, reputable
  economists) documenting the camps and verifying consequential factual claims.
- Represent EACH position through a direct, cited statement from at least one
  credible named person or institution that holds it. Verify consequential facts
  (the vote count, the dissenters' names, the target range, the years-above-target
  figure, the tariff/energy attribution) against reporting or the primary record.
- Carry honest `data-nb-kind` on every source entry.

## Relevant prior coverage / non-overlap
- Prior Unbiased pieces (do not repeat framing): election-betting-preemption,
  four-day-workweek, wealth-tax, rent-control, firing-the-regulators (removal
  power, NOT rate policy), etc. This is the first Fed rate-policy question.
- Tonight's Current Events will NOT report the Fed decision (this desk owns it);
  ensure the piece argues the policy question rather than merely narrating the
  meeting.

## Structures NOT to repeat
Recent Unbiased titles are a mix of neutral questions and stated tensions; write a
neutral question title in the piece's own nouns. Do not publish the component
vocabulary ("camp", "thesis", "argument", "holder") as headings or prose. Name
the two `data-nb-section`/`id` anchors for the actual positions (e.g. `raise-now`
and `hold-the-line`).

## Harness / model (balanced profile)
coach sonnet/low; researcher sonnet/high; writer sonnet/medium; editor opus/high.

## Publication bar
10+ real read sources (≥4 primary, ≥3 secondary); two genuinely strong,
symmetrically scrutinized, cited cases with named holders; no house verdict;
`nb check --series unbiased` BLOCK: 0 (strict gates); editor DONE.
