# Commission: feature/jepsen-particledb

The day's Feature. Scheduled run for 2026-11-01.

## The story and the finding

On 2026-10-31 Jepsen (Kyle Kingsbury) published an analysis of ParticleDB, a
Postgres-compatible database its maker Orkes advertises as "Full ACID. 159K TPS"
and "formally proven" with TLA+. Testing single nodes across versions 1.1.4
through 1.1.18.11.rc-22, Jepsen reported 96 issues. The default `occ`
transaction mode, documented as "Jepsen-safe", lost committed writes;
`serializable` still allowed Lost Update after process kills;
`strict-serializable` returned stale reads; and the query engine returned
wrong-predicate results, including `WHERE 4 = 5` matching the row with primary
key 5 and `WHERE TRUE` sometimes returning nothing. The "formally proven" claim
could not be checked at all, because no TLA+ specification was available.

The finding, the piece's original work, in one sentence: take each guarantee
ParticleDB advertises and name the specific Jepsen anomaly that falsifies it,
so the gap between the marketing and the measured behavior is a single legible
table rather than a 96-item list.

## Disclosure and fairness (do not omit)

Orkes, the vendor, funded the analysis. State that plainly. Orkes also says a
later candidate build (1.1.19-rc.13) resolves every issue in the report, which
Jepsen did not test; report that as the vendor's claim, attributed, and say it
is unverified. Be fair: a funded Jepsen report that publishes 96 issues is the
normal Jepsen arrangement, and the report's value is the method, not a verdict
on a company. State the claim in the vendor's own words before measuring it.

## Boundaries

- This is a database-correctness story for a CS/ML audience fluent in
  distributed systems. Define each isolation anomaly on first use in plain words
  (Lost Update, read skew / A5A, G-single, aborted read / G1a, stale read under
  strict serializability) — the reader knows transactions and concurrency but is
  not expected to carry the ANSI/Adya anomaly taxonomy by heart.
- Five-minute read, 600-1200 words (the series is strict, so stay inside the
  band). Open with the finding in two or three sentences, then build each
  section around one visual with short prose on how to read it and what follows.
- Stay on what Jepsen measured and what ParticleDB documents. Do not editorialize
  about Orkes beyond the evidence, and do not generalize to "databases" or
  "marketing" as a class — that is exactly the slop the standard forbids.
- Read the Jepsen report in full (it runs ~137k characters; the orchestrator only
  sampled the first 100k). Base every claim on a passage you read.

## Visuals (each section built around one)

- The central visual is a **claim-versus-evidence matrix** (`nb-table`): rows are
  the documented guarantees (Full ACID; snapshot isolation; "formally proven"
  TLA+; `occ` "Jepsen-safe"; `groupsync` durability equal to `sync`; prepared
  statements "work as expected"), and each row names the Jepsen result that
  falsified or could not confirm it, with the citation. Keep prose cells short;
  put the source in the caption.
- At least one more visual showing a mechanism, not just a list: e.g. a small
  inline-SVG diagram of one concrete anomaly (the default-mode lost committed
  write, or the `WHERE 4 = 5` predicate bug turning a comparison into a primary-
  key lookup), drawn with theme variables; or a version timeline (1.1.4 →
  rc-22) marking which guarantees stayed broken at the last tested build. Prefer
  the diagram that teaches the reader why the anomaly is possible.
- Look at every visual rendered before handing on; the proof catches neither an
  overlapping label nor an arrow that stops short.

## Sources (min 5)

1. The Jepsen report (primary): `https://jepsen.io/analyses/particledb-1.1.4`.
2. ParticleDB's own marketing page carrying "Full ACID. 159K TPS." — the
   researcher finds the exact Orkes/ParticleDB URL.
3. ParticleDB documentation / CLI reference carrying the `occ` "Jepsen-safe" /
   "safe under concurrency" and the `sync`/`groupsync` durability wording.
4. Orkes's statement that 1.1.19-rc.13 resolves the issues (vendor response) —
   find where Jepsen quotes it or where Orkes states it.
5. One reference grounding the anomaly vocabulary — Jepsen's own consistency-
   models page, or Kingsbury & Alvaro's "Elle" paper, or Adya's isolation
   taxonomy — so terms like G-single and P4 land on a definition.

The researcher verifies each URL resolves and records the exact wording of each
advertised claim (it is the other half of the matrix). Never cite a homepage as
a stand-in for the page that carries the claim.

## Recent-pattern notes (break these; check the recent feature library)

Recent feature headlines are declarative findings with a specific number
("Swapping the model moves AstaBench's overall score twice as far on average as
swapping the loop"; "Micron earns more from each dollar of memory sales"), and
recent deks add a twist on a specific figure ("addresses generative AI only in
one footnote"; "the released dataset reproduces only as 20.06%"). Writing a
declarative finding headline is the series style and is fine; do not copy a
previous headline's construction wholesale, and do not reuse a recent dek's
"only as X" / "only in one Y" twist mould. Recent section headings include "What
a score of 58 averages", "What the shares are shares of", "What the 30% and the
6.9 hours will bear" — do NOT open headings with "What …" here, and build the
headings differently from each other. The `rs-docket` furniture belongs to legal
pieces; this one uses `nb-table` and inline SVG.

## Production (model and effort; tier→model deviations recorded)

Tiers map to named subagents: "inherit" → Opus (orchestrator's model),
"capable" → Sonnet (closest available). Recorded actuals:
- writing-coach: Sonnet, low.
- researcher: Sonnet, high.
- writer: Sonnet, high (policy: capable / high).
- editor: Opus, high, required (policy: inherit / high — honored).

## Edition neighbours

Published alongside: a Daily Brief (word of the day plus election-law and tech
items) and the Reinforcement Learning course lesson on finding optimal policies.
This Feature shares no ground with either; keep it on ParticleDB and Jepsen.
