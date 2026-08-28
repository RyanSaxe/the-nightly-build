# Editorial review: expert-tools/sqlglot (editor/01)

## Skeptic

Thesis: SQLGlot earns its place because it parses a query into a real syntax
tree a program can read, rewrite, and reason about, where string manipulation
can only match text; a single Spark-to-Snowflake date migration proves it, and
the piece is straight about the costs (lenient parser, tiered dialect coverage,
pure-Python speed) before landing a reach-for-it-or-not verdict.

Claims it stands on, and how each held:

- **Parsing to an AST rewrites structure, not just spelling.** The headline's
  "two casts" is the load-bearing claim. Fig. 1's Spark-to-Snowflake output is
  `SELECT DATEADD(DAY, 1, CAST(CAST(a AS TIMESTAMP) AS DATE)) FROM t` — a
  genuine double cast SQLGlot inserts, not a rename. Matches the evidence's
  local run verbatim; the DuckDB/Hive divide-by-1000 and MySQL/Postgres format
  rewrite match too. Held.
- **The same tree supports inspection, lineage, and optimization.** `find_all`
  tables `['x','y']` / columns `['a','b']`, the lineage trace of `c` through
  `y.c` to `t.a`, and the optimizer's star expansion plus `1 = 1` folding all
  match the evidence outputs exactly. Held.
- **The parser is deliberately lenient (accepts engine-invalid SQL).** README
  FAQ quote verified on the primary ("intentionally lenient... a transpiler,
  not a validator"). The `SOMEUDF`/bad-group-by acceptance and the
  `SELECT FROM WHERE` ParseError match the local run. Held.
- **Speed is pure Python vs. `sqlglot[c]` (~3-5x); the Rust `sqlglotrs` path is
  retired.** README benchmark values (tpch 0.27, values 0.24, complex_where
  0.20) verified against the primary. tokens.py carries the exact deprecation
  string. The 20.3.0 / 30-40% Rust history (Tobiko) and the mypyc retirement
  reasons (Fivetran) both verified. Framed correctly against `sqlglot[c]`, not
  the deprecated Rust package. Held.
- **Maintenance: weekly cadence, funded backer, maintainers' own product
  depends on it.** PyPI JSON confirms 30.17.0 on 2026-08-12, MIT, Python >=3.9,
  with 30.16.0 (08-10), 30.15.0 (08-04), 30.14.0 (07-27) in the preceding
  weeks. TechCrunch confirms the $21.8M raise and SQLGlot/SQLMesh as Tobiko's
  open-source core. Held.

Display text checked descriptor by descriptor. Headline: "two casts" is
accurate output and "SQLGlot writes them" is what the transpile emits. Dek's
"no-dependency," "more than 30 SQL dialects," and the leniency caveat are all
claims about the tool verified on the primary; not a self-grade of the
article's method. Dialect-tier counts in body prose (18 official, 14 community,
"a couple more" plugins) verified against the raw README table: exactly 18 / 14
/ 2. The fetch-model's dialect counts disagreed with the article on first pass;
counting the raw table by hand settled it in the article's favor.

Every `data-nb-kind` audited. Source 2 ("Local run against sqlglot 30.17.0") is
correctly labeled primary: a first-hand verification run is primary evidence.
The secondary labels (Tobiko, Fivetran, TechCrunch) are correct — write-ups
about the project, not the project's own artifact.

Every citation href opened as printed. All ten resolve and land on the source
they are cited for: the tagged README and tokens.py blobs, the API docs, the
three PyPI package pages, the version-pinned 30.17.0 page, and the two blog
posts plus TechCrunch. No miscitations found; nothing to fix or route.

Two writer-flagged items judged:

- **(a) W-PLACEHOLDER left standing.** The flagged all-caps run
  (`AS TIMESTAMP AS DATE FROM`) is the interior of Fig. 1's transpile output
  comment `# SELECT DATEADD(DAY, 1, CAST(CAST(a AS TIMESTAMP) AS DATE)) FROM t`.
  This is genuinely what SQLGlot 30.17.0 emits (verified against the evidence
  run and consistent with the tool's default keyword-uppercasing generator).
  The caption states the outputs are "what 30.17.0 prints," so lowercasing the
  keywords would misrepresent the tool's real output and make the example
  wrong. The warning is a true false positive from the prose scanner reading
  code-listing text as prose. Confirmed accurate and acceptable to leave.
- **(b) Source 2 citation.** Its href points at
  `pypi.org/project/sqlglot/30.17.0/` (resolves; the exact version-pinned
  distribution page), and the link text names it "Local run against sqlglot
  30.17.0 (pip install sqlglot==30.17.0)." The source itself is a local run
  with no URL of its own; the href points at the exact reproducible artifact and
  the label is transparent about what it is and how to reproduce it. Honest and
  adequately labeled. No change needed.

## Cut

Made a slop pass over every sentence, then walked the edges out of order, then
read cold as an arriving reader, then ran the delete test.

Cuts and repairs (5 direct changes, all prose/punctuation, no facts touched):

- Cut "That chapter is closed." in the speed section — an unearned mini-punchline
  and signpost: the deprecation sentence that follows carries the actual fact,
  and "That X is closed" survives the placeholder test as a line about anything.
  The "As of 30.17.0..." turn carries the transition on its own.
- Trimmed "and the record is concrete" from the maintenance opener — it grades
  the reporting rather than reporting; the release-cadence facts that follow
  speak for themselves.
- Three semicolons converted to periods, per the house punctuation default
  (plainest mark; period when a period would not over-separate): in the
  leniency anti-pitch, the `sqlglot[c]` build sentence, and the verdict's last
  line. None was the rare tightly-bound case that earns a semicolon.

Two failed the slop test outright (the two content cuts above). No dangling
referents: the opener introduces its own nouns ("a working Spark query and a
Snowflake warehouse"). No prompt leakage — the verdict and cost framing are in
the article's own terms, not the commission's. No borrowed phrasing from the
voice-guide exemplars; the honesty moves (Willison's fiddling, Evans's "what it
can't do," Gallant's anti-pitch) are echoed in structure, not wording.

One pattern noted but not cut: five earned negative-parallelism constructions
("not just another function," "structure and not only spelling," "not a rubber
stamp," "not arbitrary text," "not a volunteer's spare hours"). Each corrects a
real, named misconception, so each earns its place under `spec/slop.md`; the
accumulation is a mild stylistic tic worth the writer's awareness on the next
piece, not a revise item here.

Furniture reads as evidence, not decoration: stat strip carries the thesis
numbers (each cited nearby), two code listings are the worked proof, the
benchmark table is the honest speed basis (a 3-row table beats a 3-bar chart
here), the note quotes the project's own caveat, and the strong note is the
earned verdict. No component is idle and none makes the piece read as a stack.

Headline construction breaks the recent series rhythm: the last four Expert
Tools headlines lead "Tool + verb + mechanism"; this one leads with the work
("Moving a date from Spark to Snowflake takes two casts") and names the tool
second. Section headings vary in build (where-, what-, gerund, declarative,
noun-phrase, whether-). Not stamped.

## Reader

Read straight through as the paper's ML-engineer reader: what I have that the
sources alone would not give me is a single decision. The piece turns ten
scattered facts into one argument — that a query is an editable tree, shown on a
real migration, then weighed against leniency, coverage, and speed into a
reach-for-it-or-not rule with a stated falsifier. No single source hands you
that synthesis. The draft-handoff original-work sentence claims exactly this
line, and the article delivers it. The reading-the-tree section brushes the
"feature tour" line the voice guide warned about (find_all + lineage +
optimizer in one section), but stays on the right side: all three are
subordinated to the one thesis ("each capability is one more walk over the same
parse tree") rather than paraded as a catalog, and only one is shown in a
listing. Prose sits closer to the voice-guide exemplars than a median summary:
plain concrete sentences, first-person only where the local run makes it honest,
and the anti-pitch conceded outright. The headline reads as its largest claim
and it is true.

## Edits

- Removed the sentence "That chapter is closed." from the speed-cost section.
- Removed "and the record is concrete" from the maintenance-section opener.
- Changed "SQLGlot cannot answer it; that check belongs to the engine" to a
  period between the clauses.
- Changed "compiling the same Python with mypyc; installing it overlays" to a
  period, capitalizing "Installing."
- Changed the verdict's "the weekly cadence; a stall in releases" to a period,
  capitalizing "A stall."

## Required work

- **writer** — Re-run `./nb check` to reconcile the `nb-meta` word count (the
  cuts remove ~9 words from the recorded 1629; reading time is unchanged at 7
  min). Routine re-proof after editor edits, not a content defect.

No researcher work. No blocking content issues.

## Decision

approve — every claim held against the reopened primaries, all ten hrefs
resolve to their sources, the round focus is met (one worked example, honest
costs, speed framed against `sqlglot[c]`), both writer-flagged items are
legitimate, and the remaining changes were mine to make.
