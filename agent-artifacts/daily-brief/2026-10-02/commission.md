# Commission: daily-brief/2026-10-02

## The assignment

The Daily Brief for Friday, 2 October 2026. Six items, in the fixed order the
series prompt sets: Word of the Day, three news items, two technology
developments. The `brief` template enforces exactly six tagged items, a citation
on every item, and at least twelve sources. Per item: one primary source and at
least one secondary.

## Date and freshness

The brief is dated 2026-10-02. Report what happened on or just before that date.
Prefer developments from 1-2 October 2026 that are still news; an older item
earns a place only when something on those dates changed its status. The
preceding edition (daily-brief/2026-10-01) already covered the BEA Q2 GDP third
estimate, the Court of International Trade forced-labor tariff hearing, Hegseth's
proposed Autonomous Warfare Command, Qt 6.12 LTS, and OpenStack 2026.2
"Hibiscus." Do not re-report any of those. Find the day's own developments.

## Selection

News: choose for the importance of what happened, not the attention it drew.
Favor the United States. An international or New York-region story earns a slot
only when it outweighs a national one. Attribute any unverified claim to its
source and state the status of the evidence plainly, the way the 1 October
edition did ("The announcement sets a goal; it does not establish that the
command is operating"). Vary that evidence-status construction item to item;
see recent-patterns.md.

Technology: two recent developments (a release, a new capability, a research
result). Give what was announced, who is claiming it, and what the record adds.
Link the underlying record and independent reporting where both exist.

## Boundaries that keep the edition from overlapping itself

Tonight's paper also runs a Feature and a Technical piece. Keep the brief off
their ground:

- The **Feature** owns the 1 October end of federal Medicaid/CHIP matching funds
  for many lawfully present immigrants under the 2025 reconciliation law. Do not
  use that as a news item here.
- The **Technical** piece owns dbt Core v2.0 (the Rust rewrite). Do not use it,
  or dbt, as a technology item here.

Choose different subjects for all six items.

## Leads to investigate (verify independently; none is required)

These surfaced in orchestrator scouting and may be wrong or stale. The
researcher confirms each against the document that owns it and may discard any
of them for better-sourced developments.

- A completed U.S. military withdrawal from Iraq ending the counter-ISIS
  coalition mission.
- The SNAP (food assistance) administrative cost share shifting to states
  beginning 1 October under the 2025 budget law. (Distinct from the Feature's
  Medicaid topic; usable here only if it holds up and reads as its own story.)
- A halt to Tennessee executions after a failed lethal-injection attempt.
- A California law banning child marriage.
- An ICE memo setting limits on vehicle stops.
- Technology: a model release in the window (confirm date and primary record);
  an open-source adoption milestone (for example OpenTofu or Kubeflow SDK
  download counts) carried by a primary record a reader can pursue. Pick the two
  best-sourced that are not dbt.

The word: choose one with a precise present-day meaning and a documented origin
worth knowing. Give part of speech, pronunciation, a one-sentence definition
cited to a dictionary authority, then the origin and one telling moment, cited
to an independent word history. Do not reuse "quiddity" (1 October) or any word
in the recent record.

## Required contribution

Each item earns its place by telling a reader what happened, who says so, and
how firm the evidence is, with a primary record and independent reporting so the
reader can go further. The brief's original work is selection and the honest
status line on each item, not analysis.

## Source policy (nb source-policy --series daily-brief)

Template `brief`: min 12 sources; per item primary [1,1], secondary [1, null].
Every item cited; number sources in first-citation order; carry primary/secondary
into `data-nb-kind`.

## Production (nb production-policy --series daily-brief; balanced profile)

- writing-coach: model capable (Claude Sonnet), effort low
- researcher: model capable (Claude Sonnet), effort high
- writer: model capable (Claude Sonnet), effort medium
- editor: model inherit (Claude Opus, the correspondent's model), effort high, required

No required directive was traded down.

## Neighbouring articles this run

- feature/medicaid-lawful-immigrant-funding (health policy)
- technical/dbt-v2-rust-engine (data tooling)

The brief shares no subject with either.


## Recent patterns (what not to repeat)

_Folded in from the orchestrator's recent-pattern notes; the writer and editor were briefed on these._

### Dek

The 1 October dek was a joined list: "BEA lifts second-quarter growth to 2.2%; a
trade court hears a tariff challenge, while Qt and OpenStack publish new
releases." It stacks items with a semicolon and a "while" clause. Do not build
the 2 October dek as a semicolon-or-comma list of the day's items. Write one
lean sentence that gives the reader the single reason today's brief is worth
reading, or names the through-line, without the three-clause roundup mold.
`spec/headlines.md` bans the semicolon reversal and the comma triad in deks.

### The evidence-status line

The careful "status of the evidence" caveat is house discipline and stays. But
the 1 October edition closed two separate items on the same mold, a semicolon
reversal: "His stated target is October 1, 2027 ... the announcement sets a goal;
it does not establish that the command is operating" and "it is not growth from
Q2 2025." Keep the caveats; vary their construction. Do not let two items in
this edition end on the same "X; it does not establish Y" shape.

### Item headlines

Recent item heads are plain subject-verb lines naming the actor and the change
("BEA raises its Q2 GDP estimate to 2.2%", "Qt 6.12 adds QML hot reload under a
five-year LTS"). Keep that register. Avoid the colon-subtitle machine tell and
the triad of paired adjectives.

### Word of the Day

The word card is fixed furniture. The recurring risk is the origin paragraph
settling into one shape ("X used Latin Y ... English later developed a sense
of ..."). Tell this word's history in whatever order its story wants.
