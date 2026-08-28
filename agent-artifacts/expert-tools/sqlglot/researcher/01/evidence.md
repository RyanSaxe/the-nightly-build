# Evidence: expert-tools/sqlglot (01)

The evidence strongly supports the core angle: SQLGlot parses SQL into a real
abstract syntax tree and regenerates SQL from that tree, so a program can read,
rewrite, and reason about a query as a data structure rather than a string. I
installed SQLGlot 30.17.0 (the current release) and ran every capability the
commission names against it: transpilation between named dialects with genuine
semantic rewrites, `find_all` metadata extraction, the optimizer (`qualify` plus
star expansion, constant folding, predicate simplification), column lineage
across a subquery, `diff`, and programmatic `select().from_().where()` building.
All ran and produced the outputs recorded below. The documented costs are firm
and quotable: the parser is lenient by design ("a transpiler, not a validator"),
transpilation is best-effort with an explicit unsupported-feature path, and
dialects sit in three support tiers with different maintenance priority.

The one place the commission is out of date is its performance framing. It asks
for "performance vs. sqlglotrs," the Rust tokenizer. As of the installed
30.17.0 source, `sqlglotrs` is deprecated and "no longer compatible with
sqlglot"; the current accelerator is the mypyc-compiled build `sqlglot[c]`
(distributed as the `sqlglotc` wheel). The Rust-tokenizer story is real history,
not the present cost. This does not weaken the AST-versus-string angle, but the
writer must frame the speed cost against `sqlglot[c]`, not `sqlglotrs`, or the
article will be wrong about the shipping tool. Flagged again in the report as a
missing input decision.

Where the record is thin: I could not open GitHub's API for a live star or
open-issue count (unauthenticated 403 / rate limit), so maintenance health rests
on release dates, the commercial backer, and the dependent list rather than a
popularity number. The "Used By" list is SQLGlot's own claim about who depends on
it; I verified the strongest case (SQLMesh, the maintainers' own product) but did
not open each dependent's source to confirm production use.

## Sources

```text
URL:         https://github.com/tobymao/sqlglot/blob/v30.17.0/README.md
Kind:        primary — the project's own description of itself, at the exact
             release tag. Read as the 30.17.0 PyPI sdist (byte-identical release
             artifact); the tagged blob is the source's own page and I confirmed
             it resolves and carries the same FAQ and benchmark content.
Establishes: what SQLGlot is, its feature surface, the documented limitations,
             the dialect support tiers, the benchmark table, the "Used By" list,
             and the canonical short examples.
Paraphrase:  SQLGlot is "a no-dependency SQL parser, transpiler, optimizer, and
             engine" that translates between "over 30 dialects" and "aims to
             read a wide variety of SQL inputs and output syntactically and
             semantically correct SQL in the targeted dialects." The FAQ states
             the parser is deliberately lenient and that SQLGlot "is a
             transpiler, not a validator." mypyc-compiled install is "roughly
             3-5x faster than the pure Python version." Transpilation between
             some dialect pairs is best-effort: an unsupported feature emits a
             warning and does a best-effort translation by default, raisable via
             error level.
Locators:    Header paragraph; FAQ section; "### Unsupported Errors"; "### SQL
             Optimizer"; "### AST Diff"; "### Metadata"; "## Benchmarks";
             "## Supported Dialects"; "## Used By".
Quote:       "The parser is intentionally lenient, so it can accept queries that
             a real engine would reject. SQLGlot is a transpiler, not a
             validator. A query that parses successfully may still fail at
             execution time."
             "It may not be possible to translate some queries between certain
             dialects. For these cases, SQLGlot may emit a warning and will
             proceed to do a best-effort translation by default."
             "SQLGlot parses queries into an AST and generates SQL back from it,
             so it preserves the meaning of a query rather than its exact text.
             Cosmetic details can change in the process."
```

```text
URL:         https://github.com/tobymao/sqlglot/blob/v30.17.0/sqlglot/tokens.py
Kind:        primary — the shipping source that owns the tokenizer-backend
             selection. Read in the installed 30.17.0 package; confirmed the
             same text resolves at the tagged raw blob.
Establishes: the current accelerator picture and the deprecation of the Rust
             tokenizer. `sqlglotc` ships compiled `.so` files overlaid onto
             sqlglot's own modules (there is no importable `sqlglotc` module);
             the code detects it via the compiled core. If `sqlglotrs` is
             importable and `sqlglotc` is not, SQLGlot warns that the Rust path
             is deprecated and incompatible.
Paraphrase:  The base pip install is pure Python; `sqlglot[c]` overlays
             mypyc-compiled extensions; the old `sqlglot[rs]` Rust tokenizer is
             deprecated and will not work with current sqlglot.
Locators:    Module top, tokenizer-backend import block (the `SQLGLOTC_INSTALLED`
             detection and the `try: import sqlglotrs` warning).
Quote:       "sqlglot[rs] is deprecated and no longer compatible with sqlglot.
             Please use sqlglotc instead for faster parsing: pip install
             sqlglot[c]"
             "The sqlglotc distribution ships no importable `sqlglotc` module; it
             overlays compiled .so files onto sqlglot's modules, so detect it via
             the compiled core."
```

```text
URL:         https://sqlglot.com/sqlglot.html
Kind:        primary — the project's generated API documentation.
Establishes: exact top-level function signatures. `parse_one(sql, read=None,
             dialect=None, into=None, **opts) -> Expression`; `transpile(sql,
             read=None, write=None, identity=True, error_level=None, **opts) ->
             list[str]`; `parse(sql, read=None, dialect=None, **opts) ->
             list[Expression | None]`. Confirms the DuckDB->Hive `EPOCH_MS`
             example and `transform()` AST-rewrite usage.
Paraphrase:  `parse_one` parses one statement into a syntax tree; `transpile`
             parses in the read dialect and returns a list of SQL strings in the
             write dialect; `transform` walks the tree applying a node-rewriting
             function.
Locators:    Module docstring / function reference at top of the page.
```

```text
URL:         https://pypi.org/project/sqlglot/
Kind:        primary for release metadata — the maintainer's own distribution
             record.
Establishes: latest version 30.17.0, released 2026-08-12; MIT license; author
             Toby Mao; requires Python >=3.9; frequent minor releases (30.16.0
             on 2026-08-10, 30.15.0 on 2026-08-04, 30.14.0 on 2026-07-27,
             30.13.0 on 2026-07-20), i.e. a roughly weekly-to-biweekly cadence.
Paraphrase:  SQLGlot ships new minor versions on the order of every one to three
             weeks and is at 30.17.0 as of late August 2026.
Locators:    Header (version, date, license); "Release history" sidebar.
```

```text
URL:         https://pypi.org/project/sqlglotrs/
Kind:        primary for the package's own status — its distribution page.
Establishes: `sqlglotrs`, the Rust tokenizer, is marked "Deprecated: use
             sqlglotc instead." Its last release is 0.13.0 (2026-02-23). MIT,
             maintained by Toby Mao, linked to the main repo.
Paraphrase:  The standalone Rust tokenizer package is deprecated and stopped
             updating in February 2026; users are pointed to `sqlglotc`.
Locators:    Page header banner and release history.
```

```text
URL:         https://pypi.org/project/sqlglotc/
Kind:        primary for the package's own status — its distribution page.
Establishes: `sqlglotc` is the "mypyc-compiled extensions for sqlglot" build,
             versioned in lockstep with sqlglot (30.17.0, 2026-08-12), MIT,
             Python >=3.10, prebuilt wheels for Windows/Linux/macOS across
             CPython 3.10-3.14. This is what `pip install "sqlglot[c]"` pulls.
Paraphrase:  The current native-speed path is a mypyc build released alongside
             every sqlglot version, not a separate Rust component.
Locators:    Page header and description.
```

```text
URL:         https://www.tobikodata.com/blog/sqlglot-jumps-on-the-rust-bandwagon
Kind:        secondary, but maintainer-adjacent — written by Iaroslav Zeigerman,
             a SQLGlot co-maintainer and Tobiko Data co-founder, about work he
             did on the project. Owns the historical Rust-tokenizer benchmark it
             reports; secondary as to present-day behavior.
Establishes: the Rust tokenizer landed in SQLGlot 20.3.0 (post dated
             2024-01-23), migrated the tokenization step to Rust for a claimed
             30-40% overall parsing improvement, installable then via
             `pip install "sqlglot[rs]"`.
Paraphrase:  In early 2024 the maintainers rewrote only the tokenizer in Rust
             and measured a 30-40% end-to-end parsing speedup, larger on longer
             inputs.
Locators:    Benchmark table and the "30-40%" claim in the body.
Quote:       "the tokenization step has been completely migrated to Rust,
             resulting in a 30-40% improvement in overall parsing speed
             (depending on the input query)."
```

```text
URL:         https://www.fivetran.com/blog/how-we-accelerated-transpilation-by-compiling-sqlglot-with-mypyc
Kind:        secondary — written by Evangelos Danias, a Fivetran engineer (a
             dependent, not a maintainer), 2026-05-01. Reports the mypyc work
             and the reasons for retiring the Rust path.
Establishes: mypyc-compiling SQLGlot gives roughly 5x on parsing (tokenizer +
             parser), ~2.5x on SQL generation, and ~2-2.5x on the optimizer, and
             the team retired the Rust tokenizer to keep a single pure-Python
             codebase.
Paraphrase:  Compiling the existing Python with mypyc matched or beat the Rust
             tokenizer while removing a separate Rust build, Rust expertise
             requirement, and an independent release cycle.
Locators:    Performance list and the "It worked, but came with real drawbacks"
             paragraph.
Quote:       "the versioning was a headache since `sqlglotrs` had its own release
             cycle independent of sqlglot."
```

```text
URL:         https://techcrunch.com/2024/06/05/with-21-8m-in-funding-tobiko-aims-to-build-a-modern-data-platform/
Kind:        secondary — trade press reporting Tobiko Data's funding.
Establishes: SQLGlot has a funded commercial backer. Tobiko Data (co-founded by
             Toby Mao, Tyson Mao, and Iaroslav Zeigerman) raised $21.8M and
             builds SQLMesh and SQLGlot as its open-source core.
Paraphrase:  The project is not a lone side-project; a venture-funded company
             whose flagship product depends on it sponsors its development, which
             explains the aggressive release cadence.
Locators:    Lede and funding paragraph.
```

```text
Source:      Local verification run — sqlglot 30.17.0 installed from PyPI into a
             fresh venv, executed with CPython 3.11.
Kind:        primary verification (no public URL; the runnable proof behind the
             examples). Anyone can reproduce with `pip install sqlglot==30.17.0`.
Establishes: every commissioned capability runs on the current release and
             produces the outputs below. This is the "verify the example runs"
             check.
Paraphrase / recorded outputs:
  transpile, semantic rewrite across dialects:
    transpile("SELECT EPOCH_MS(1618088028295)", read="duckdb", write="hive")[0]
      -> 'SELECT FROM_UNIXTIME(1618088028295 / POW(10, 3))'
    transpile("SELECT DATE_ADD(a, 1) FROM t", read="spark", write="snowflake")[0]
      -> 'SELECT DATEADD(DAY, 1, CAST(CAST(a AS TIMESTAMP) AS DATE)) FROM t'
    transpile("SELECT STR_TO_DATE(x, '%Y-%m-%d') FROM t", read="mysql",
              write="postgres")[0]
      -> "SELECT TO_DATE(x, 'YYYY-MM-DD') FROM t"
  metadata extraction:
    parse_one("SELECT a, b FROM x JOIN y USING (id)").find_all(exp.Column)
      -> column names ['a', 'b']; find_all(exp.Table) -> ['x', 'y']
  optimizer (qualify + star expansion + folding + predicate simplify):
    optimize(parse_one("SELECT * FROM t"), schema={"t":{"a":"INT","b":"INT"}}).sql()
      -> 'SELECT "t"."a" AS "a", "t"."b" AS "b" FROM "t" AS "t"'
    optimize(parse_one("SELECT a FROM (SELECT a, b FROM t) AS x WHERE x.a > 1 AND 1 = 1"),
             schema={"t":{"a":"INT","b":"INT"}}).sql()
      -> 'SELECT "t"."a" AS "a" FROM "t" AS "t" WHERE "t"."a" > 1'
      (the "1 = 1" is folded away and the subquery is flattened)
  column lineage across a subquery:
    lineage("c", "SELECT y.c AS c FROM (SELECT t.a AS c FROM t) AS y",
            schema={"t":{"a":"INT"}})
      -> root node "c"; downstream "y.c" traced to source "SELECT t.a AS c FROM t AS t"
  semantic diff:
    sqlglot.diff(parse_one("SELECT a + 1 AS x FROM t"),
                 parse_one("SELECT a + 2 AS x FROM t"))
      -> edit list of Keep/Remove/Insert/Update objects (one Update on the literal)
  programmatic build:
    exp.select("a","b").from_("t").where("a > 1").sql()
      -> 'SELECT a, b FROM t WHERE a > 1'
  leniency confirmed:
    parse_one("SELECT SOMEUDF(x) OVER () FROM t").sql() parses an unknown
    function without complaint; parse_one("SELECT a FROM t GROUP BY 1, 2, 3")
    parses a group-by that references non-existent positions.
  parse errors still raised for true syntax breakage:
    parse_one("SELECT FROM WHERE") raises sqlglot.errors.ParseError
    ("Expected table name but got ... WHERE"). So "lenient" means it tolerates
    engine-invalid-but-well-formed SQL, not arbitrary garbage.
  installed backend:
    base install is pure Python (sqlglot/parser.py is a .py, not a .so);
    `import sqlglotrs` raises ModuleNotFoundError; the Dialects enum reports 33
    registered members.
Locators:    Reproducible from the version pin above.
```

## Contradictions

- **Commission premise vs. shipping tool.** The commission frames the
  performance cost as "vs. sqlglotrs." The installed 30.17.0 source
  (`sqlglot/tokens.py`) and the `sqlglotrs` PyPI page both say the Rust
  tokenizer is deprecated and no longer compatible; the live accelerator is the
  mypyc build `sqlglot[c]`. The two maintainer-side write-ups agree on the arc:
  Zeigerman's 2024 post introduces the Rust tokenizer; Danias's 2026 post
  records its retirement in favor of mypyc. No source defends `sqlglotrs` as
  current. The writer should treat the Rust tokenizer as history and the cost
  question as "pure Python vs. `sqlglot[c]`."

- **Magnitude of the speedup, by source.** The Rust post claimed a 30-40%
  overall parsing improvement (tokenizer only). The mypyc post claims ~5x on
  parsing, and the README FAQ claims "roughly 3-5x" for the whole `sqlglot[c]`
  build. These are not in conflict: the Rust number is tokenizer-only end-to-end
  parse time in 2024; the mypyc numbers cover the whole compiled pipeline in
  2026. The README benchmark table (below) is the primary, current figure and
  should anchor any number the article prints.

- **"No dependencies" vs. the accelerators and dateutil.** SQLGlot's headline is
  "no-dependency," and the base wheel is genuinely pure Python with nothing
  required. But `sqlglot[c]` pulls a compiled `sqlglotc` wheel, and the optimizer
  silently skips simplifying literal timedelta expressions if `dateutil` is not
  installed. The zero-dependency claim holds for the core parser/transpiler, not
  for peak speed or full optimizer behavior. State it precisely.

- **A real adoption cost the marketing does not lead with.** The FAQ notes that
  subclassing a dialect "may not work properly with `sqlglot[c]` installed, so
  custom dialects may require the pure Python version." A reader who both writes
  a custom dialect and wants native speed cannot straightforwardly have both.
  This is a genuine, documented tension worth surfacing rather than a strawman.

## Numbers

```text
Figure: 30.17.0 (current release), published 2026-08-12
Owner:  PyPI sqlglot project page (maintainer's distribution record)
Scope:  latest stable at time of research; minor releases land ~weekly-biweekly
```

```text
Figure: "over 30" SQL dialects; support-tier table lists 18 Official + 14
        Community in-repo, plus 2 external Plugin dialects (YDB, MaxCompute)
Owner:  README v30.17.0, "## Supported Dialects" table
Scope:  Official = maintained by the core team with higher fix/feature priority;
        Community = community-maintained, lower priority; Plugin = third-party,
        no core-team support. The installed Dialects enum reports 33 members.
```

```text
Figure: sqlglot[c] runs each benchmark in ~0.20-0.33x of pure-Python time
        (i.e. ~3-5x faster). Examples, seconds, Python 3.14.3:
          tpch    sqlglot 0.002709 (1.00) | sqlglot[c] 0.000740 (0.27)
          values  sqlglot 0.466734 (1.00) | sqlglot[c] 0.113762 (0.24)
          complex_where sqlglot 0.032710 (1.00) | sqlglot[c] 0.006602 (0.20)
Owner:  README v30.17.0, "## Benchmarks" table (benchmarks/parse.py)
Scope:  parse-only microbenchmark; relative factor in parentheses is vs. pure
        Python = 1.00. Rust bindings sqloxide/polyglot-sql are in the same
        ballpark as sqlglot[c]; the sqlglotrs column has been removed from the
        table. Pure-Python sqlparse is 4-20x slower and sqlfluff 40-175x slower
        on the same queries.
```

```text
Figure: Rust tokenizer (historical) — 30-40% overall parsing speedup; e.g. tpch
        0.00944 -> 0.00590 s (0.625x)
Owner:  Tobiko Data blog, 2024-01-23 (Iaroslav Zeigerman)
Scope:  SQLGlot 20.3.0, tokenizer-only, superseded by sqlglot[c]. Use only as
        historical context, not as the current cost.
```

```text
Figure: mypyc speedups — ~5x parsing, ~2.5x SQL generation, ~2-2.5x optimizer
Owner:  Fivetran blog, 2026-05-01 (Evangelos Danias, Fivetran)
Scope:  component-level, secondary/dependent-reported; corroborates the README's
        "3-5x" for the whole build.
```

## Source assets

```text
Asset: The "## Benchmarks" table in README v30.17.0 (pure sqlglot vs sqlglot[c]
       vs sqltree/sqlparse/sqlfluff vs the Rust-binding parsers sqloxide and
       polyglot-sql), per-query seconds with a relative factor.
Shows: exactly what adopting the compiled build buys (~3-5x) and how a pure
       Python parser lands next to Rust bindings and next to the far slower
       Python alternatives. This is the honest, primary basis for any speed
       chart.
Crop:  If rendered as a chart, keep the relative factor (=1.00 baseline) and the
       sqlglot / sqlglot[c] pair; the writer must build the chart from the
       committed chart-N.py per house rules, not screenshot the table. Retain
       the "Python 3.14.3, seconds, parse-only" caveat in the caption.
```

```text
Asset: The "## Supported Dialects" tier table in README v30.17.0.
Shows: the coverage-gap cost concretely — which databases are first-class
       (Official), which are community-maintained at lower priority, and which
       are unsupported-in-core plugins. Better than prose for the "what it costs"
       section.
Crop:  Keep the three tier labels and their definitions; a reader needs the tier,
       not all 34 rows, to grasp the gap.
```

```text
Asset: None found beyond the two tables. SQLGlot's value is textual (SQL in, AST
       out, SQL out); the strongest visual evidence is the transpile input/output
       pair and the lineage trace, which belong in a code listing or a small
       annotated tree, not an image.
```

## Discarded

```text
URL: https://raw.githubusercontent.com/tobymao/sqlglot/main/sqlglotrs/README.md
     — 404. No standalone sqlglotrs README at that path in current main;
     consistent with the Rust component having been retired. Deprecation is
     instead documented in sqlglot/tokens.py and on the sqlglotrs PyPI page.
```

```text
URL: https://api.github.com/repos/tobymao/sqlglot
     — 403 unauthenticated (rate limit); could not read a live star / open-issue
     count. Maintenance health is sourced from release dates and the funded
     backer instead. Not cited.
```

```text
URL: https://deepwiki.com/tobymao/sqlglot/2.1-parser-and-tokenizer
     — auto-generated third-party wiki, not authored by the project; surfaced in
     search but not opened as a citable source. Superseded by the primary source
     (tokens.py) for the same claims.
```

```text
URL: https://crates.io/crates/sqlglot-rust / https://lib.rs/crates/sqlglot-rust
     — an unrelated third-party Rust crate named "sqlglot-rust", not the
     project's own `sqlglotrs` tokenizer. Rejected to avoid conflating it with
     the maintainers' deprecated component.
```

```text
URL: Various LinkedIn posts by Toby Mao surfaced in search — self-promotional,
     not needed once the funding (TechCrunch) and the technical posts (Tobiko,
     Fivetran) are in hand. Not opened for citation.
```
