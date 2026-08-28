# Commission: expert-tools/sqlglot

## Assignment

An Expert Tools article on **SQLGlot** (github.com/tobymao/sqlglot), the
pure-Python SQL parser, transpiler, and optimizer. The subject is the one
capability that changes advanced work: SQLGlot parses SQL into a real syntax
tree and transpiles between 20-plus dialects with no dependencies, so a program
can read, rewrite, and reason about SQL as a data structure instead of a string.
Show where that enters a real workflow (dialect migration, query linting or
rewriting, column-level lineage, building a query programmatically, optimizing
or normalizing SQL) with a small, concrete Python example that proves the value
rather than teaching installation.

## Angle and boundaries

- Read past the README. Inspect the implementation, the dialect system, the
  optimizer, `sqlglot.diff`/lineage, the docs, the issue history, and real usage
  (who depends on it and for what). Name honestly what adopting it costs (parser
  coverage gaps, dialect fidelity limits, performance vs. sqlglotrs) and whether
  maintenance is healthy enough to trust.
- Name the tool and the work it changes in the headline and section titles.
- The example should be minimal and prove one thing the reader could not easily
  do with string manipulation or a database-bound parser.
- This is the paper's declared reader: a machine-learning engineer with a
  math/CS background who touches data and SQL. Do not over-explain SQL itself.

## Neighboring articles this edition

None overlap. Seven articles run this edition (two daily briefs, plus lessons in
investing, a paper reconstruction, an unbiased desk, and a word). No other
touches developer tooling.

## Sources

Template floor (article): at least 6 sources. Primary sources are the SQLGlot
repository, its documentation, its source code, and its issue/PR history;
secondary sources are independent write-ups or dependents' documentation. Cite
only code and docs you actually opened, at a resolvable URL.

## Production

Profile balanced. Researcher: effort high, model claude-opus-4-8. Writer: effort
medium, model claude-opus-4-8. Editor: effort high, model claude-opus-4-8.
Writing coach: effort low, model claude-opus-4-8. Harness: claude-code-routine.

## Recent habits to break

Recent Expert Tools headlines all take the shape "Tool does one surprising
specific thing" (Grapple.nvim tags a file by name...; beartype type-checks a
whole list by reading one random item; Atuin makes your shell history answer
questions bash can't). The construction is fine, but do not copy the exact
rhythm of the last one; find SQLGlot's own surprising specific. Recent pieces
lead with the mechanism in the dek. Vary how the dek is built.

## Required contribution

The reader finishes knowing exactly where SQLGlot earns its place in an expert
data workflow, what it replaces, what it costs, and whether to trust it, proven
by one example they could adapt. Not an install tutorial and not a feature tour.
