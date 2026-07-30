# Editor review brief — word-of-the-day/bowdlerize (invocation 01)

## Inputs (begin here)
- `editorial-direction.md`, `commission.md`.
- The exact writer brief: `writer/01/brief.md` (for prompt-leakage detection).
- `writing-coach/01/voice-guide.md`; `researcher/01/evidence.md`;
  `writer/01/draft-handoff.md`.
- Article: `library/word-of-the-day/bowdlerize.html`; `.nb-context/`.

## Task
Give the draft three ordered reads (skeptic, cut, reader). Make surgical cuts and small
fixes directly; past a word or clause, return new writing to the writer; evidence gaps
to the researcher. Record `Skeptic`, `Cut`, `Reader` lines, edits made, required work by
owner, and the decision. Write `editor/01/editorial-review.md`.

## Watch items specific to this piece
- Keep etymology (history) distinct from the present sense (a separate claim).
- Audit every `data-nb-kind`; confirm no primary label hides a missing independent
  source.
- The writer omitted the OED (gated 403, unread) and substituted Merriam-Webster +
  Online Etymology Dictionary — confirm this honors "cite only what you have read" and
  still meets the dictionary/etymology obligation.
- Hard word band 550–800; confirm the engine measure sits inside it after any cuts.
- Headline/dek: no colon subtitle, no "X is not Y; it is Z", no banned dek molds.
- Proof: `./nb check .nb-work/word-of-the-day/bowdlerize/library/word-of-the-day/bowdlerize.html --series word-of-the-day --repo . --library ../library` to BLOCK: 0.

## Note on production
Single-context, no isolation (harness has no child-agent spawn). The editor read is run
in the same context immediately after the writer proof, per PROTOCOL's degraded path;
the writer proof and editor gate are preserved in full.
