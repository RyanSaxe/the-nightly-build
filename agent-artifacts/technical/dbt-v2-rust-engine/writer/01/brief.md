# writer brief: technical/dbt-v2-rust-engine (01)

Inputs (read all; do not tour the repo or history beyond these):
- editorial-direction.md (../../editorial-direction.md) — the binding standard
- commission.md (../../commission.md) — the assignment AND the "Post-research
  correction" section, which is binding and supersedes the earlier angle
- voice-guide.md (../../writing-coach/01/voice-guide.md) — how this should sound
- evidence.md (../../researcher/01/evidence.md) — the complete claim set; treat
  it as the only facts available, including the researcher's own local run
- commission.md "Recent patterns" section — desk habits to break

Article to edit (in place):
/home/user/the-nightly-build/.nb-work/technical/dbt-v2-rust-engine/library/technical/dbt-v2-rust-engine.html

Output: draft-handoff.md (./draft-handoff.md)

Proof (run verbatim, links included, until BLOCK: 0):
/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/technical/dbt-v2-rust-engine/library/technical/dbt-v2-rust-engine.html --series technical --repo /home/user/the-nightly-build

Work from these inputs. Where something you need is missing, ask me (the
orchestrator); do not invent evidence or widen the claim set yourself.

This is a hands-on walkthrough, not a release write-up. The spine is the
commission's Post-research correction: the single Rust rewrite lets dbt parse
and type-check its SQL, which enables a compile-time, column-level check the
Python engine could not do — but that check lives only in the proprietary `dbt`
distribution (dbt OSS, the Apache build, refuses it), fires only under
`--static-analysis strict`, and the thing people assume is new (catching a
missing `ref`) already worked in v1. The new, demonstrable contrast is the
misspelled column. Pull those apart on a real dbt-duckdb run.

Non-negotiables from the evidence and corrections:
- Use the GA names exactly (dbt v2; the proprietary default `dbt`; the Apache
  build dbt OSS). Never call the open-source build the thing that does the
  column check.
- Run the experiment (or reuse the researcher's recorded outputs verbatim) and
  show it in an nb-code listing: baseline compile passes, strict compile fails at
  models/b.sql:1:12 with available columns (error dbt0227), dbt run fails in
  DuckDB, and dbt OSS prints that it does not include the static-analysis engine.
  Name versions. Trim Rust stack traces and say you trimmed them.
- Speed is one honest paragraph at most. Attribute 70s->17s (~4x) to dbt Labs'
  GA post; do not state "up to 10x" as fact; if you chart anything, chart the
  researcher's own labeled 3k-model measurement with scope in the caption, built
  with nb chart from the recorded series. Do not build a chart from the vendor's
  two prose numbers as if it were data.
- A parse -> compile -> run pipeline diagram (nb-figure) likely carries the
  mechanism faster than prose; label it as a drawing. No official diagram was
  verified, so do not capture one as a source asset.
- State the real limits: proprietary vs Apache boundary, strict-vs-baseline,
  DuckDB adapter status muddiness, thin independent adoption, no independent
  speed reproduction.

Form and standards:
- Template `article`: orientation anchor + 2-6 flex sections named for this
  argument, last section the piece's own conclusion. Min 8 sources, per-section
  citation, numbered in first-citation order, data-nb-kind honest (dbt Labs blog
  = primary for its claims; the Fivetran/dbt press release is not independent).
  Add data-nb-locator where the record gives one.
- Break the desk habits in recent-patterns.md: no "X does A; Y does B" semicolon
  headings, no "source-based trace, not a test run" framing (you ran it), no "the
  useful conclusion is specific:" closer or tidy tricolon of negations.
- Your prose meets spec/slop.md before handoff; check headline/dek/subheads
  against the evidence and spec/headlines.md; make the nb-meta dek and the
  rendered dekline identical; fill nb-meta dates/harness/model; run nb stamp then
  the proof. Put the one-sentence original-work statement in draft-handoff.md.
