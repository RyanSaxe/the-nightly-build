# Draft handoff: expert-tools/sqlglot (01)

## Original-work sentence

The article turns the evidence's separate verified outputs into a single
argument, that SQLGlot earns its place by treating a query as an editable syntax
tree, by making one Spark-to-Snowflake migration the proof and then weighing it
against the leniency, dialect-coverage, and pure-Python-versus-`sqlglot[c]` costs
into a concrete reach-for-it-or-not verdict.

## Proof result

`./nb check ... --series expert-tools --library /home/user/library-checkout`
(links included): **BLOCK: 0**, verdict PUBLISHABLE. 1629 words, 10 sources
(7 primary, 3 secondary), reading time 7 min.

### Warning left intentionally (1)

- **W-PLACEHOLDER** — `all-caps placeholder text survives in the prose: 'AS
  TIMESTAMP AS DATE FROM'`. This is a false positive. The flagged run is the real
  transpiled SQL in Fig. 1's output comment: `# SELECT DATEADD(DAY, 1,
  CAST(CAST(a AS TIMESTAMP) AS DATE)) FROM t`, which is exactly what SQLGlot
  30.17.0 emits and is the "two casts" the headline names. The checker
  (`engine/nb/proof/prose.py`) scans code-listing text as prose and treats a run
  of 4+ consecutive all-caps tokens as a leftover placeholder; uppercase SQL
  keywords in a listing trip it. It cannot be cleared without either mangling the
  real output or lowercasing keywords that the tool genuinely uppercases, both of
  which would make the example inaccurate. Left as-is on accuracy grounds. No
  other listing output triggers it (their keyword runs are under four tokens).

## Framing decision applied

Per the brief's correction to the commission: the speed cost is framed as pure
Python vs. `sqlglot[c]` (the current mypyc build), with `sqlglotrs` treated as
retired history (deprecated, no longer compatible). No source defends `sqlglotrs`
as current, so it is not presented as a live cost.

## Open questions

None blocking. One note for the editor: source 2 is the researcher's local
verification run, which has no public URL of its own; its `href` points at the
exact reproducible artifact (`https://pypi.org/project/sqlglot/30.17.0/`) and the
link text names it as a local run reproducible via `pip install
sqlglot==30.17.0`. This is the honest anchor for the example outputs (the exact
`DATE_ADD`/`EPOCH_MS`/`STR_TO_DATE` results and the `find_all`/lineage/optimizer
outputs), which only the run establishes.
