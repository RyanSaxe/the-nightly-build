# Writer brief — build-from-scratch/speculative-decoding (01)

## Your job
Rebuild speculative decoding in real, runnable code and prove the exact-
distribution property, drawing on the commission, voice guide, and evidence
record. Then prove the article to BLOCK: 0.

## Exact inputs (start here)
- `agent-artifacts/build-from-scratch/speculative-decoding/commission.md`
- `agent-artifacts/build-from-scratch/speculative-decoding/editorial-direction.md`
- `agent-artifacts/build-from-scratch/speculative-decoding/writing-coach/01/voice-guide.md`
- `agent-artifacts/build-from-scratch/speculative-decoding/researcher/01/evidence.md`
- Initialized article: `library/build-from-scratch/speculative-decoding.html`
- `.nb-context/` (template contract, runtime assets, furniture incl. code listing)

## Build, then write
1. **Write and RUN real code.** Implement, in Python you actually execute in this
   workspace: (a) standard autoregressive sampling from a target distribution,
   and (b) the speculative draft-then-verify loop with the exact accept/reject
   rule from the evidence record (accept x w.p. min(1, p(x)/q(x)); on rejection
   sample the normalized residual (p−q)_+ ). Use the smallest real setup that
   proves the claim (explicit small distributions / char-level / n-gram — not a
   full LLM). Empirically confirm the speculative sampler's output distribution
   matches the target's over many draws, and measure accepted-tokens-per-step /
   speedup vs draft–target agreement. Keep the script(s) beside the article for
   provenance (e.g. `library/build-from-scratch/speculative-decoding/`), and use
   the real printed output in the piece — do not invent numbers.
2. **Write** `library/build-from-scratch/speculative-decoding.html`:
   - `article` geometry: `orientation` + 2–6 flex sections + `Sources`. Words
     **1500–4500** (measured). Every section cited.
   - Carry the argument with `nb-code` listings (the code that matters, not a
     dump) and an equation for the acceptance rule + residual distribution. Prove
     the equivalence in prose + equation, then show the run's empirical match as a
     small honest table/figure. Then compare the prototype to real LLM-scale
     systems (KV cache, batched verification, draft choice) and state where wins
     and limits come from (acceptance rate, memory-bandwidth-bound decoding),
     cited to the evidence.
   - `nb-meta` ACTUAL values: title, dek, date `2026-08-01`, mode `open`, order
     null, tags e.g. `["llm","inference","engineering"]`, measured
     sources/words/reading_minutes, harness `claude-code`, model `claude-sonnet-5`.
   - Number sources first-citation order; honest `data-nb-kind` (the algorithm's
     papers = primary; measured speedups from the party that ran them = primary).
     Any cited speedup is from a primary source or from your own committed run.
3. `writer/01/draft-handoff.md`: the visible original work (your from-scratch
   implementation and the empirical distribution-match result), how to reproduce
   the run, warnings resolved, open items.

## Prove it
`/home/user/the-nightly-build/nb check library/build-from-scratch/speculative-decoding.html --series build-from-scratch --repo /home/user/the-nightly-build` → **BLOCK: 0**.
Preview to inspect the code listing renders. Check `nb chart --help` if you chart the run.

## Rules
- Documented furniture only; no active content in the HTML (no live scripts) — the
  code is a rendered listing, the run happens offline and its output is quoted.
  Preserve fixed engine assets/classes/labels. Begin with named inputs; `REQUEST
  researcher` for a missing proof step rather than hand-wave. No repo/archive tour.

## Report
End with: `DONE writer library/build-from-scratch/speculative-decoding.html`
