# Editorial review: technical/dbt-v2-rust-engine (editor/01)

## Correct

Thesis, stated from the draft alone: dbt v2's single Rust rewrite lets the engine
parse and understand the SQL it generates, and that enables a compile-time,
column-level check the Python engine could not do; but the check ships only in
the proprietary `dbt` distribution, fires only under `--static-analysis strict`,
and is a genuinely new catch only for a misspelled column, since a missing `ref`
already failed before the run in v1.

Claims under it, and how each held:

1. The misspelled column is the new contrast: run-time in v1 and in v2 baseline,
   compile-time only under v2 strict. Held. The orientation listing (dbt 2.0.6)
   shows baseline compile passing, `strict` failing at dbt0227 /
   `models/b.sql:1:12` with a's two columns named, and `dbt run` failing inside
   DuckDB; the v1 listing (dbt-core 1.12.5) shows compile passing and the same
   DuckDB Binder Error at run. All of this matches the evidence record's recorded
   run line for line (evidence "My local reproduction").

2. The ref check is not new. Held, but the draft overstated the run. It claimed
   the missing `ref` was "compiled on all three installs" and that "dbt OSS 2.0.5
   and dbt 2.0.6 both failed with `[DependencyNotFound (dbt1048)]` at
   `models/b.sql:1:16`." The evidence record runs the ref case on only two builds
   (dbt-core 1.12.5 and dbt OSS 2.0.5) and records no `dbt 2.0.6` result and no
   `1:16` locator for it; the recorded dbt-oss message is "Ref 'missing_model'
   not found in project," with no file:line:column. The added build and the
   invented locator are facts no input supports. Fix: narrowed the sentence to
   the two builds the record tested and dropped the invented locator. The
   pipeline figure carried the same overclaim ("missing ref (dbt-core 1.12.5,
   dbt OSS 2.0.5, dbt 2.0.6)"); I rebuilt pipeline.png from a new committed
   `pipeline.py` so the parse box names only the two tested builds. The argument
   (the ref catch predates v2) rests on v1 catching it, which the record
   supports, so it survives the narrowing intact.

3. The check lives in proprietary `dbt`, not Apache dbt OSS. Held. The oss
   listing shows dbt OSS 2.0.5 printing dbt1000 ("this distribution of dbt OSS
   does not include the static analysis engine") and compiling anyway, matching
   the record exactly; three dbt Labs documents (install page, comparison table,
   June roadmap) are cited for the same boundary. The piece never says or implies
   the open-source build does the column check.

4. `strict` vs default `baseline`. Held. "In my run baseline caught nothing for
   a plain misspelled column, with the default and with `--static-analysis
   baseline` given explicitly" matches the record; the piece does not claim
   baseline flagged it.

5. Speed. Held and honest. 70s->17s (~4x) is attributed to dbt Labs' GA post,
   "up to 10x" to the joint press release as an unmethoded vendor claim, and the
   3,000-model series is a labeled own-measurement with scope in the caption. No
   bare "10x" appears as fact; the headline carries no speed figure. Recomputed
   the chart means against evidence: parse 15.6 / 2.1 / 2.4 and compile ~32 / ~4
   / ~4 all match chart-1.py and the record.

Figures and locators checked: dbt0227 at `models/b.sql:1:12`, a's columns, the
dbt1000 text, the dbt1308/dbt1048 codes, the four version strings, and the dek's
`models/b.sql:1:12` all trace to the record. Headline, dek and subheads check
against the evidence; the nb-meta dek and the rendered dekline are identical.

Citation hrefs: every printed `href` matches the URL the evidence record opened
for that source (the two redirect cases, the upgrade guide and the license page,
are printed at their resolved canonical addresses). `nb check` passes link
validation.

data-nb-kind audit: the Fivetran/dbt press release (s14) is marked primary with
a note that it is the vendors' own claim and not independent, which is how the
evidence record itself classifies it; the piece uses it only as an attributed
vendor claim and defers to the docs on the licensing contradiction, so it is
never treated as independent corroboration. Summit write-up (s4), the agent-
skills PR (s7) and Datacoves (s15) are secondary, each with a note on its stake.
The dbt Labs blogs, docs, repo, roadmap and license are primary for their own
claims. All correct.

Writer's two open notes, decided: (a) License page. The draft cited it for
"proprietary" and "prohibits reverse engineering" from the record's summary,
which the researcher explicitly flagged as not verbatim-verified ("re-open before
quoting clauses"). "Proprietary" is corroborated by three other primaries
(comparison table, README, feature matrix) and stays; "prohibits reverse
engineering" rests on that single flagged summary alone, is a specific legal
assertion, and is not load-bearing, so I cut it rather than state an
unverifiable clause as fact. This removes an unverifiable specific; it does not
hide thin reporting, and the license reporting is noted here as resting on a
summary. (b) dbt-core 1.12.5 behavior for the `desciptin` key: the article does
not claim it ("I did not establish what v1 prints for it"), matching the record's
own caveat. Left as is.

Not altered: the code listings carry a few incidental lines beyond what the
record transcribed (the run-error code dbt1308, a target path, the v1 `Done.`
summary). The writer attests a verbatim re-run, these lines are consistent with
real dbt output and bear on no claim, and I could not re-run to reconfirm them,
so I left the attested transcriptions rather than edit real-looking output I did
not produce. Flagged for the orchestrator.

## Reads well

Cut the ref paragraph's closer, "Coverage that credits the new engine with
catching errors before the warehouse has to point at something other than the
ref check." "Coverage ... has to point" is an abstraction acting, and the
sentence half-survives the placeholder test. Replaced it with a flat statement
that keeps the s4 citation on the circulating claim: "The pre-warehouse catch
that v2 adds is the misspelled column, not the ref." The antithesis stays because
the misconception it corrects (that the ref catch is the new capability) is real
and the section is built on separating the two.

Deleted the license paragraph's topic sentence, "The boundary is a license
boundary." It reduces to "the X is a Y boundary," and the paragraph's first
cited fact (the README: Apache source, with `dbt` a proprietary distribution of
it) carries the point without it. Deleted rather than repaired.

The edges otherwise hold. The opener leads on the concrete thing the engine does,
not on a method disclaimer (recent-patterns). No "X does A; Y does B" semicolon
heading appears; the six subheads are built differently from each other and each
is a step of the argument. The closer ends on a tested limit in the piece's own
nouns ("I did not run that case"), not on a self-grading tricolon of negations.
The observed/attributed/inferred discipline the voice guide asks for is kept
throughout (the v1 compile-pass paragraph is the clearest instance). Nothing read
thinner than the guide in a way editing could lift further.

## The experience

The rendered page builds in argument order: the hook listing, the ref
distinction, the mechanism with the parse->compile->run drawing, the OSS refusal,
one honest speed paragraph with the own-measurement chart, then the limits. Both
figures match the record: the rebuilt pipeline drawing now places the misspelled
column (strict, dbt 2.0.6) at compile and the missing ref (the two tested builds)
at parse, and the chart is a labeled own-measurement with scope in the caption.
The three code listings carry the weight the argument needs and no table is
missing. What the piece gives beyond its sources: on a reproducible run it
disaggregates what the GA post, the press release and the summit coverage bundle
together, pinning which compile-time check is actually new, which distribution
holds it, and what turns it on. That matches the writer's original-work sentence,
and no source does the disaggregation.

## Edits

- Narrowed the missing-`ref` paragraph to the two builds the record tested
  (dbt-core 1.12.5, dbt OSS 2.0.5); removed the unsupported `dbt 2.0.6` result
  and the invented `models/b.sql:1:16` locator.
- Rewrote the ref paragraph's closer to a flat, attributed statement; cut the
  "Coverage ... has to point" abstraction.
- Rebuilt pipeline.png from a new committed pipeline.py so the parse box names
  only dbt-core 1.12.5 and dbt OSS 2.0.5 for the missing-ref catch.
- Cut "prohibits reverse engineering" from the license sentence; kept the
  multiply-sourced "proprietary."
- Deleted the "The boundary is a license boundary." topic sentence.
- Reran `nb stamp` (words 2051) and the exact `nb check`: BLOCK 0, WARN 0,
  PUBLISHABLE.

## Decision

approve: the piece is correct after narrowing two overclaims to the record and is
clean against slop, and its spine (which check is new, where it lives, what turns
it on) is now stated exactly as the evidence supports.
