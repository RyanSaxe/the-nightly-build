# researcher brief: technical/dbt-v2-rust-engine (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md) — the binding standard
- commission.md (../../commission.md) — the assignment and the angle

Output: evidence.md (./evidence.md)

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

Establish, from primary records you open and read, the material for a walkthrough
of dbt Core v2.0's Rust engine, built on the angle in commission.md.

Read the sources, not the coverage:
- dbt Labs' own v2.0 release notes and the v2 announcement / roadmap document.
  Record the GA date, the Apache 2.0 license, that it is a single Rust engine
  (the Fusion engine) replacing the two-engine era, and any stated behavior
  (static SQL analysis, compile-time reference/column checks, typed
  understanding of SQL).
- The exact parse/performance claim ("up to 10x faster" on a stated project
  size). Record the number, who stated it, and the stated scope/benchmark. This
  is dbt Labs' claim unless independently reproduced; mark it so.
- The dbt documentation for the engine and the language spec: what the engine
  now validates at parse/compile time versus run time, and what a user runs
  (the relevant commands).
- The GitHub repository: the license, and what is open-source versus what
  requires the paid platform (adapters, the VS Code extension, cloud features).
  Record the real open-source boundary; this bounds the piece's claims.
- Adapter coverage: which adapters the v2 engine supports at GA, and whether
  dbt-duckdb (a local, warehouse-free adapter) is supported, since the writer
  may run a local example with it. Record the install path and the minimal
  commands.

Then:
- Find independent evidence of adoption or use (practitioner write-ups, migration
  reports, issue activity) distinct from dbt Labs' own marketing. Secondary and
  attributed.
- Look for what breaks the angle: reports that the compile-time checking is
  partial, that migration from v1 breaks real projects, that the "open-source"
  framing is contested, or that the speed claim does not hold outside the
  vendor benchmark. Record in full.
- Classify every source primary or secondary by authorship and stake. dbt Labs'
  blog and docs are primary for dbt Labs' claims; a partner press release is not
  independent.
- Source assets: any official diagram of the parse/compile/run pipeline or a
  benchmark chart, and what a crop must keep. Note if a chart could be rebuilt
  from a verified series.

Minimum eight sources, anchored on primary records. In Limits, state clearly
whether a faithful local run of v2.0 with dbt-duckdb is reproducible from the
documented install path, so the writer knows whether to run a real experiment or
build the example from documented commands.
