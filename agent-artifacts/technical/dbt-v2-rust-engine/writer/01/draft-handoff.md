# Draft handoff: technical/dbt-v2-rust-engine (writer 01)

## Original-work sentence

The article pins down, on one re-run DuckDB project, which compile-time check is new in dbt v2 (the misspelled column, not the missing ref), where it lives (proprietary `dbt`, refused by Apache dbt OSS) and what turns it on (`--static-analysis strict`), against a launch message that bundles open source, the new check and speed together.

## Proof

`nb check` (exact brief command, links included): BLOCK: 0, WARN: 0, PUBLISHABLE. No warning left on purpose.

## What I ran versus took from the record

- I re-ran in clean venvs: dbt 2.0.6, dbt-oss 2.0.5, dbt-core 1.12.5 with dbt-duckdb 1.11.0. Reproduced exactly: baseline compile passes, strict fails dbt0227 at models/b.sql:1:12, `dbt run` fails in DuckDB (v2, OSS, v1), OSS strict prints dbt1000 and compiles, and the missing `ref` fails at parse on all three.
- Taken from the researcher's record, not re-run by me: the 3,000-model timing series (chart-1), and the `desciptin` YAML key result on dbt OSS (stated as "a separate run"; v1 behavior is explicitly left unestablished in the text).
- Listing output is trimmed (Rust stack frames, banners, timing lines) and the captions say so.

## Notes for the editor

- The pipeline figure is my drawing (pipeline.png, captioned as a drawing); there is no source SVG kept because the proof requires a local PNG. Its text is in the alt and caption.
- Chart caption cites source 1 only to say dbt Labs' benchmark used a different project. Chart data is in chart-1.py.
- The first-person "I" is the paper's author voice for runs; the timing series was recorded by the researcher on the same 4-core machine class. If the editor wants that attributed differently, it is one sentence in the speed section.
- Source 14 (duckdb.org post), 6 (alpha blog), 18 (byteiota), 19 were not cited; 15 sources are used.

## Open questions

None blocking. Unverified in the record and so left out: whether dbt-core 1.12.5 warns on `desciptin`; the exact license clauses (I cite only "proprietary, prohibits reverse engineering" per the record's summary; the editor may want the license page re-opened).
