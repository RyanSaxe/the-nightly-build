# editor brief: technical/dbt-v2-rust-engine (editor/01)

Inputs (read all):
- editorial-direction.md (../../editorial-direction.md) — the binding standard
- voice-guide.md (../../writing-coach/01/voice-guide.md) — read first
- commission.md (../../commission.md) — the assignment AND the binding
  "Post-research correction" section
- the exact writer brief (../../writer/01/brief.md)
- evidence.md (../../researcher/01/evidence.md) — open when a concern calls for it
- draft-handoff.md (../../writer/01/draft-handoff.md) — the writer's original-work
  sentence, proof result, and open notes
- commission.md "Recent patterns" section — desk habits to compare against

Article to decide and edit (in place):
/home/user/the-nightly-build/.nb-work/technical/dbt-v2-rust-engine/library/technical/dbt-v2-rust-engine.html

Output: editorial-review.md (./editorial-review.md)

Proof (rerun after any edit, links included, until BLOCK: 0):
/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/technical/dbt-v2-rust-engine/library/technical/dbt-v2-rust-engine.html --series technical --repo /home/user/the-nightly-build

You decide whether this publishes and edit it until it can. Change anything to
get there except the facts. Fix what you can from the evidence record and this
checkout; send back only if it needs a different argument no editing reaches.

Press hard on the piece's spine, because the whole value is the distinctions:
- The compile-time column check must be attributed to the proprietary `dbt`
  distribution, never to the Apache dbt OSS build. Confirm the article never
  says or implies the open-source engine does the column check.
- Confirm the new-capability claim rests on the misspelled COLUMN (run-time in
  v1 and in v2 baseline; compile-time only under v2 `strict` with the full
  distribution), and that the article does NOT present the missing-`ref` catch as
  new (v1 already did it).
- Confirm `strict` vs default `baseline` is stated correctly (baseline did not
  flag the column in the run).
- Confirm every speed figure is attributed and "up to 10x" is not stated as
  fact; any chart is a labeled own-measurement with scope in the caption.
- Confirm the command-output listing is honest (trimmed stack traces noted,
  versions named) and that any pipeline figure is labeled a drawing.
- Audit data-nb-kind: the Fivetran/dbt press release is NOT independent; dbt
  Labs' blog/docs are primary for dbt Labs' claims. Open every citation href as
  printed and confirm it lands on the source.

Writer's open notes to judge: the article cites the license page only for
"proprietary" and "prohibits reverse engineering" from the record's summary (the
writer flags that you may want the page reopened before trusting those exact
words); and the dbt-core 1.12.5 behavior for a misspelled `desciptin` YAML key is
unverified and the article does not claim it. Decide each.

Cut slop against spec/slop.md, reading the edges and the last sentence most
carefully, and compare openers/closers/headings against recent-patterns.md (no
"X does A; Y does B" semicolon headings; no "source-based trace" framing since it
was a real run; no "the useful conclusion is specific:" closer). Last, state in
one sentence what the piece gives beyond its sources, compare it to the writer's
original-work sentence, and reread the headline as its largest claim. If you edit
prose, rerun stamp/check. Write editorial-review.md in the required shape and end
with approve or redraft.
