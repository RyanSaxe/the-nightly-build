# researcher brief: expert-tools/outlines (01)

Inputs:
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/agent-artifacts/expert-tools/outlines/editorial-direction.md
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/agent-artifacts/expert-tools/outlines/commission.md  — the tool, mechanism, and source obligations

Establish, from owning sources: what the Outlines library guarantees and for which
target formats (regex, JSON schema, choice sets, context-free grammars), read from
its own documentation and repository; the mechanism, read from the implementation
and the paper "Efficient Guided Generation for Large Language Models" (Willard and
Louf, 2023) — how the target is compiled to a finite-state machine, how the FSM
state selects a mask over the tokenizer vocabulary at each step, and what the
precomputed index buys at inference time; where the real costs sit (index
construction, tokenizer-vocabulary alignment, grammar classes that are awkward or
unsupported, backend and model-access constraints, local-model versus hosted-API);
and the maintenance signals (latest version, release cadence, commit and issue and
PR activity, maintainer or company behind it). Capture a small, runnable Python
example from the documentation that constrains output to a schema or regex, and
record its exact API surface so the writer can reproduce it faithfully.

Read at least one alternative far enough to place Outlines against it: the
constrained-decoding support in vLLM or llama.cpp, `guidance`, `jsonformer`, or
XGrammar/`llguidance`. Record contradictions or limitations the project's own
issues or independent write-ups raise (performance overhead, correctness edge
cases, version churn). Verify every version number and quantitative claim against
the primary that owns it. Classify each source primary or secondary and why; at
least 6 sources; confirm every URL resolves to the source's own page.
