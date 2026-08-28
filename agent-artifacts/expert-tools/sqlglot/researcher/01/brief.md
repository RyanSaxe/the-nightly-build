# researcher brief: expert-tools/sqlglot (01)

Inputs:
- commission.md — the assignment, the angle, the cost/trust questions to answer
- editorial-direction.md — house standard, citation rules, press voice, series prompt

Output: .nb-work/expert-tools/sqlglot/agent-artifacts/expert-tools/sqlglot/researcher/01/evidence.md

Read SQLGlot past its README: the repository, the documentation, the source
(parser, dialect definitions, optimizer, `diff`, `lineage`), and the issue/PR
history for known limitations and real usage. Establish, with resolvable
primary citations:

- What SQLGlot actually does that string handling and database-bound parsers do
  not, and the exact API for one small proof example (parse, transpile between
  two named dialects, and one of: optimize/normalize, column lineage, or
  programmatic build). Verify the example runs as described.
- The real costs: dialect-coverage gaps, transpilation fidelity caveats the
  project itself documents, and performance including the sqlglotrs (Rust)
  tokenizer.
- Maintenance health: release cadence, maintainer, dependent projects that rely
  on it in production.

This round's focus: get the API details and version-specific behavior exactly
right, and record any behavior the project documents as unsupported so the
article does not overclaim. Confirm every URL resolves to the source's own page.
