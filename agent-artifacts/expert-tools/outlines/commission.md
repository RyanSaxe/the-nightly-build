# Commission: expert-tools/outlines

## Assignment

One tool for the Expert Tools desk. Template `article` (1200-3000 words, min 6
sources). Authorized scheduled work from `nb duty`: open slot, one article, on the
Wednesday cadence slot. Do not repeat a published tool.

## The tool and why it qualifies

Outlines (the `outlines` Python library, dottxt-ai) constrains a language model's
generation so the output is guaranteed to match a schema: a regular expression, a
JSON schema, a context-free grammar, or a fixed set of choices. It qualifies for
the desk because it changes a real workflow that most practitioners still solve by
retry-and-parse, and because its power sits in an implementation worth reading past
the README: it compiles the target format into a finite-state machine and, at each
decoding step, uses the FSM's current state to build a mask over the tokenizer's
vocabulary, zeroing the logits of every token that could not continue a valid
string. The indexing that makes this cheap at inference time is the contribution
the 2023 write-up "Efficient Guided Generation for Large Language Models" (Willard
and Louf) describes, and it is what separates the tool from a slow
validate-and-resample loop.

This is squarely in the desk's AI-harness family and fits the paper's
machine-learning reader. Recent desk entries were a shell-history tool (Atuin), a
Neovim search-and-replace buffer (grug-far), a table explorer (VisiData), and an
agent language-server (Serena); a structured-generation library is a distinct
family and a distinct workflow.

## What the article must do

Show the part that changes the work in a small, real Python example: generate
output constrained to a JSON schema or a regular expression and show that the
result is valid by construction, then contrast it with the ordinary
prompt-and-hope path it replaces. Read past the README into the implementation and
explain the mechanism the reader needs to trust it: the FSM-over-vocabulary
approach, the index that makes masking cheap, and where the cost actually lives
(building the index, tokenizer alignment, the classes of grammar it does and does
not handle well). Explain where it enters a workflow (extraction, tool-call and
function-argument generation, agent output contracts, evaluation harnesses), what
it replaces or enables, and what adopting it costs (backend and model-access
constraints, the local-model versus hosted-API story, dependency and maintenance
weight). Judge maintenance honestly from real signals: release history, issue and
PR activity, maintainer, and version. Name the tool and the work it changes in the
headline and section titles. The example proves the tool's value; it is not an
installation tutorial.

## Sources

`min_sources` 6. Anchor to: the Outlines repository and its documentation
(structured-generation, regex, JSON-schema, and CFG guides); the "Efficient Guided
Generation for Large Language Models" paper for the indexing mechanism; the
project's release history and issue tracker for the maintenance read; and at least
one independent point of comparison or critique (an alternative such as the
constrained-decoding features in llama.cpp or vLLM, `jsonformer`, `guidance`, or
XGrammar/`llguidance`, read far enough to say where it lands). Read the
implementation, not only the docs, for any claim about how masking works. Every URL
resolves to the source's own page.

## Required contribution

A practitioner finishes knowing exactly what Outlines guarantees and how (valid
output by construction via FSM-guided token masking), when the guarantee is worth
its cost, where it fits in an existing pipeline, and whether the project is
maintained well enough to depend on. The article earns its keep by reconstructing
the masking mechanism from the implementation rather than restating the promise on
the box.

## Boundaries with the rest of tonight's edition

No overlap with the other pieces. The Paper of the Day desk covers the 2017
mixture-of-experts paper tonight; Tech News covers the day's news. This is a
present-day tool walkthrough and shares no subject with them.

## Habits not to inherit

- Recent desk headlines run a "tool does the thing your old tool can't" mold
  ("Atuin makes your shell history answer questions bash can't"). State what
  Outlines does in its own terms without stamping that shape.
- The closing section on recent pieces weighs adoption under near-identical
  headings ("When the swap pays off", "What it costs, and whether to trust it").
  Write the cost-and-trust close in this article's own nouns; do not reuse those
  headings.
- Show one focused example that proves the value. Do not let it grow into a
  step-by-step install and setup walkthrough.

## Production record

- Profile: balanced (`press/production.yaml`).
- writing-coach: capable tier realized as Claude Sonnet, effort low.
- researcher: capable tier realized as Claude Opus, effort high.
- writer: capable tier realized as Claude Opus, effort medium.
- editor: inherit (Claude Opus), effort high, required.
- Harness sets reasoning effort at the session level; per-role effort is the
  policy target on the closest available runtime setting. No `required` model or
  effort directive applies, so no deviation is owed.
