# Draft handoff: expert-tools/outlines (writer 01)

## Original work

The article rebuilds Outlines' token masking as a five-rung climb (unconstrained
sampling, an FSM-derived mask, the O(N) full-vocabulary scan that mask implies,
the precomputed state-to-token index that collapses it to an O(1) lookup, and the
memory that index costs), then uses that reconstruction to fold four findings the
evidence records as separate and in tension (the guarantee is backend-dependent,
vLLM/SGLang may run XGrammar rather than Outlines, the paper's speed leadership is
stale, and the structural guarantee is settled while the accuracy effect is not)
into one adopt-or-not judgment the evidence never assembles: depend on it where you
own the logits, treat its speed as adequate not leading, and keep the accuracy
question open. The work is visible in the ladder in the-index section, the
backend/serving-stack split, the engine-comparison table, and the closing verdict.

## Final proof

`./nb check ... --series expert-tools --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 1. verdict: PUBLISHABLE.**
Stamped: words 2039, reading_minutes 9, sources 13 (all primary).

## Warning intentionally left

One `W-SENTENCE-DENSITY` (47 words, 2 clause joins) on the use-case sentence in
"Reach for it when you own the model and the schema." It is a single lead clause
followed by a colon-introduced list of four pipeline sites (extraction, tool-call
arguments, agent output contracts, evaluation harnesses). The colon is doing
exactly the job the punctuation standard sanctions, the list is parallel and
scannable, and splitting it would add a throat-clearing lead ("Four places
qualify:") that reads worse. Left as one sentence deliberately.

## Open evidence / voice questions

None. Two scoping choices worth flagging for the editor, both resolved in-text:

- The worked example uses the local `from_transformers` path (not the hosted
  `from_openai` snippet the evidence also carries), because that is the only path
  where the by-construction guarantee actually holds. The headline says "as a
  model decodes" and the dek plus the backend section state the hosted-API caveat
  explicitly, so the guarantee is not overclaimed across backends.
- The paper (s2) is cited once as a single source with per-citation
  `data-nb-locator` values for its sections, rather than as two entries (abs and
  pdf) as the evidence record lists it, to avoid the appearance of padding one
  document into two sources.
