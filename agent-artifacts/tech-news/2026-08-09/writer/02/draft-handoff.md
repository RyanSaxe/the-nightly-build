# Draft handoff: tech-news/2026-08-09 (writer 02)

## Original work

This Sunday edition audits the week's biggest claimed advances by what has held
up to outside checking as of the weekend: it leads with the one peer-reviewed
result (rhombohedral-graphene superconductivity) and, for the OpenAI Astra
proofs, separates what can be checked now (the Lean certificates, plus the first
informal outside read) from what still cannot (peer review). The ordering and
each item's caveat placement are that act.

## Editor / orchestrator items resolved

- Qwen3.8-Max item dropped entirely (orchestrator selection). Its two sources —
  the Qwen release post and the Bloomberg report — were removed and the source
  list renumbered; the false "that week has arrived and the weights have not"
  timing hook is gone with it. Edition lands at four items, eight sources
  (4 primary + 4 secondary; one primary + one independent secondary per item),
  inside the 4-6 band and above the 5-source floor.
- Astra reframed as an explicit build-on of the paper's 08-04 coverage (editor
  repetition item + orchestrator direction). The item now opens on our prior
  coverage ("When this paper covered OpenAI's ten machine-checked proofs on
  August 4, no one outside the company had read them"), leads with the genuinely
  new development — Thomas Bloom's first outside read and the sharpened
  refereeing status (Lean-checkable, still not peer-reviewed) — and only then
  recaps the underlying August 1 claim in compressed form rather than
  re-reporting the full specs as new. Bloom is framed as a working
  mathematician's reaction, not as verification of the proofs; the Lean
  certificates remain the checkable object.
- Graphene lead, GPT-4 social-science-forecasting item, and Langflow RCE item
  left as they stood (editor already approved).
- Long Ju attribution (non-blocking): left as the careful "MIT physicist Long Ju
  and collaborators"; the gated Nature author list was not reachable, so no
  stronger first-author frame was adopted.

## Display text

Edition headline and dek are graphene-only and never referenced Qwen, so both
stand unchanged and match the evidence record (three states, ~8.5 T, "tens of
times"). The Astra subhead "Lean-checkable and still unrefereed" matches the
reframe. Every date, number, and name in the changed Astra prose checks against
the record and history: our 08-04 prior coverage (confirmed via `nb history`),
the August 1 announcement, ~$2,000 Sol compute, the non-sofic group, Gromov
1999. nb-meta dek and the rendered dekline are identical.

## Proof

`./nb check … --series tech-news --library <checkout>` (links included):
BLOCK: 0, WARN: 0, PUBLISHABLE. Stamp: 8 sources, 916 words, 4 min.
No warning left standing.

The `nb render-check` / preview visual probe was not run (no Chrome in this
environment); the one furniture piece (the GPT-4 `nb-stat-strip`) was untouched
this round and uses catalog markup verbatim.

## Open questions

None blocking. The only standing evidence limit is unchanged from writer 01:
Long Ju's name and role rest on the graphene-info secondary because the Nature
author list is gated to automated fetch.
