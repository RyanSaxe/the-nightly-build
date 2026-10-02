# Commission: technical/dbt-v2-rust-engine

## The assignment

A Technical walkthrough for 2 October 2026 of dbt Core v2.0, the version of dbt
built on a single engine rewritten in Rust (the "Fusion" engine), released as
generally available at dbt Summit 2026 (September 2026) under Apache 2.0. It
qualifies for this series: recent (GA within the last 90 days), materially
changed (a full engine rewrite, not a point release), and in use (dbt is widely
deployed and v2.0 is the GA line where future work goes). The series prompt asks
for a walkthrough that opens the work with a concrete example, diagram, code, or
experiment, and explains enough of the design and behavior that a reader could
try it, question it, or build on it.

## The angle (the original work)

The headline is "dbt rewrote its engine in Rust and it parses 10x faster." Speed
is the easy part. The walkthrough's job is to show *what the single Rust engine
can do that the Python engine could not*, and why that follows from the rewrite:
a single engine that actually parses and understands SQL can resolve references
and catch a class of errors at compile time, before any query hits the
warehouse, where the Python engine (which treated SQL largely as templated text)
could only surface them at run time. Show that mechanism on a concrete example,
then say plainly what the reader can verify versus what is dbt Labs' own claim,
and what the move costs (adapter coverage, what is open-source versus what needs
the paid platform, migration friction from v1).

Put the original-work sentence in the handoff: the piece shows, on a worked
example, the specific class of error the Rust engine catches before execution
that the Python engine deferred to the warehouse, and bounds that gain with what
the GA release does and does not yet cover.

## Concrete example (required; form is the writer's call)

A walkthrough needs something concrete, not just prose. Best form, if
reproducible in the run environment: actually install dbt Core v2.0 with a local
adapter (dbt-duckdb avoids any external warehouse), build a tiny project, and
show the engine catching a bad column/ref at parse time versus the old
run-time behavior, with the real command output in a code listing. This also
sets the piece apart from the recent OpenShell piece, which was an explicit
"source-based trace, not a test run"; prefer a real run here if it reproduces.
If a faithful local run is not reproducible, build the example from the official
documentation's own commands and outputs, and say it is illustrative. Either
way, cite the behavior to a primary record, and a diagram of the parse ->
compile -> run pipeline may carry the mechanism faster than prose.

## Boundaries

- One engine, one mechanism. Do not drift into a general dbt tutorial or a
  feature tour of dbt Summit announcements. The static-analysis-from-a-real-
  parser mechanism is the spine.
- Separate dbt Labs' marketing claims (benchmark numbers, "agent-ready", etc.)
  from what the walkthrough independently shows. Benchmark figures are the
  vendor's unless reproduced; attribute them.
- The Daily Brief is barred from dbt tonight, so there is no overlap to manage;
  do not reference the brief.

## Required contribution

A reader finishes able to try v2.0 on a toy project, understands why a Rust
parser enables compile-time checks a template engine cannot, and knows the real
limits of the GA release (adapters, open-source boundary, migration). The
teaching test: a reader can explain to a colleague what class of mistake v2.0
now catches earlier and why.

## Template and structure

Template `article` (chosen over `paper`; this is a walkthrough of a shipped tool
across several primary records, not the reconstruction of one research paper).
Orientation anchor plus 2-6 flex sections, last one the piece's own conclusion.
Name sections for this argument. Reach for a code listing (nb-code) for real
command output, a figure (nb-figure) for the pipeline diagram, and a table
(nb-table) only where a comparison reads faster than prose.

## Source policy (nb source-policy --series technical)

Template `article`: min 8 sources, per-section citation. Anchor on primary
records: dbt Labs' v2.0 release notes and the v2 announcement/roadmap document,
the dbt docs for the engine and the language spec, the GitHub repository and its
license, and the dbt-duckdb adapter docs if used. Independent adoption/benchmark
reporting is secondary and attributed. Carry primary/secondary into
`data-nb-kind` honestly (dbt Labs' own blog is primary for its claims; a vendor
partner press release is not independent).

## Production (nb production-policy --series technical; balanced profile)

- writing-coach: capable (Claude Sonnet), low
- researcher: capable (Claude Sonnet), high
- writer: capable (Claude Sonnet), medium
- editor: inherit (Claude Opus), high, required

No required directive was traded down.

## Neighbouring articles this run

- daily-brief/2026-10-02 (barred from dbt)
- feature/medicaid-lawful-immigrant-funding (unrelated domain)

## Post-research correction (orchestrator decision, binding; supersedes above)

The researcher's record changes the angle in ways I have decided, not the
writer. Follow these over any conflicting wording earlier in this commission.

1. **Naming (use the GA names).** At GA (16 Sep 2026) dbt Labs renamed things.
   "dbt v2" is the release. Its default distribution is `dbt`, under a
   proprietary dbt product license with Apache-2.0 code underneath. The
   Apache-2.0-only build is **dbt OSS** (formerly "dbt Core v2"). The Rust engine
   (formerly "Fusion") is just the v2 engine now. Do not call the open-source
   build "dbt Core v2.0 under Apache 2.0 with Fusion"; that conflates the two
   distributions. The slug stays `dbt-v2-rust-engine`; the piece is about the
   engine and what it enables.

2. **The real spine.** The single Rust rewrite lets dbt actually parse and
   type-check the SQL it generates, and that enables a compile-time,
   column-level, type-aware static-analysis check the Python engine could not do.
   But three things, which the headline blurs, are the piece's own work to pull
   apart:
   - That static-analysis check ships **only in the proprietary `dbt`
     distribution**. dbt OSS (the Apache-2.0 build) refuses to run it and says so
     at the command line. So the piece must not say "the open-source Rust engine
     catches column errors before the warehouse." It says: the single Rust code
     base parses and understands SQL; the column/type check is the proprietary
     distribution's SQL-comprehension layer.
   - Even in that distribution, the default `baseline` mode did not flag a plain
     misspelled column in the researcher's run; only `--static-analysis strict`
     did.
   - Catching a **missing `ref`** before the run is **not new** (v1.12.5 already
     did it). The genuinely new, demonstrable contrast is the **misspelled
     column**: a run-time error in v1 and in v2 baseline, a compile-time error
     only under v2 `strict` with the full distribution. Build the walkthrough on
     that contrast, not on the ref check.

   Original-work sentence to carry into the handoff: the piece pins down exactly
   which check is new, where it lives (proprietary `dbt` vs Apache dbt OSS), and
   what turns it on, against a launch message that runs open-source, the new
   check, and raw speed together, and it shows the distinction on a real run.

3. **Run the experiment.** A faithful local run with dbt-duckdb is reproducible
   (`pip install dbt`, a `type: duckdb` profile, no login, no warehouse). Use the
   researcher's recorded run: baseline compile passes, `strict` compile fails at
   `models/b.sql:1:12` with the available columns, `dbt run` fails inside DuckDB,
   and dbt OSS refuses static analysis. Name the exact versions (dbt 2.0.6, dbt
   OSS 2.0.5, dbt-core 1.12.5 with dbt-duckdb 1.11.0). Trim the Rust stack traces
   in any listing and say they were trimmed. The writer may re-run to confirm;
   the record's outputs are usable as-is and are the researcher's own
   measurement, not dbt Labs'.

4. **Speed, honestly.** Do not state "10x" as fact. dbt Labs' own GA post gives
   70 s -> 17 s compile on a 10k-node project (~4x) and "2x or more" on normal
   projects; the press release's "up to 10x parse" is unmethoded and
   unreconciled with it. No independent reproduction exists. The researcher's own
   ~7x on a synthetic 3,000-model project is a separate, labeled own-measurement,
   not a confirmation of the vendor benchmark. Attribute every figure to its
   owner. Speed is not the spine; keep it to one honest paragraph or a clearly
   labeled own-measurement chart, not the headline.

5. **Adoption / "in use."** dbt is widely deployed and v2 is the GA line, and it
   runs today, so it clears the series' "not just a pitch" bar. But independent
   adoption evidence of v2 specifically is thin (one production-migration field
   report relayed through a dbt Labs repo PR; summit attendees repeating the
   claims). Say that plainly; do not inflate adoption.

6. **DuckDB adapter status.** The primary record is inconsistent (one page lists
   "DuckDB (CLI only)" under GA, another under beta; static analysis "may not
   infer schemas" for `read_csv()`/`read_parquet()` reads). Note it where it
   bears on the example; do not present DuckDB as a clean GA adapter.


## Recent patterns (what not to repeat)

_Folded in from the orchestrator's recent-pattern notes; the writer and editor were briefed on these._

### Section headings

The Technical desk has leaned hard on the two-clause semicolon heading:
"The agent chooses; the runtime checks", "The Gateway sets policy; the
Supervisor decides egress", "Landlock narrows files; seccomp helps route network
calls" (openshell, 1 October). That mold now reads as the desk's signature.
`spec/headlines.md` bans the comma-and-"and" heading for the same reason. Build
this piece's headings differently from each other and do not use the
"X does A; Y does B" semicolon pattern as a heading at all.

### Openers and framing

The recent piece opened by declaring its method as a limit: "This walkthrough
follows one illustrative task ... It is a source-based trace, not a test run."
If this piece runs a real experiment, it is not a source-based trace; do not
borrow that framing. Open on the concrete thing the engine does, not on a
disclaimer about method.

### Closers

The recent piece closed on "The useful conclusion is specific:" followed by an
"It does not X, Y, or Z" list. That self-grading opener ("built to be quoted",
`spec/slop.md`) and the tidy tricolon of negations are the mold to avoid. End on
what the walkthrough established and the one real limit, in the piece's own
nouns, without announcing that the conclusion is specific.

### The careful-status move

Marking what the evidence does not establish is correct desk discipline and
stays. Separate dbt Labs' claims from what you show, and state checkable limits
(which adapters are covered, what is open-source, what a benchmark measured),
not performed carefulness.
