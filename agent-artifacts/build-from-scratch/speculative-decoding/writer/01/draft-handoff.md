# Draft handoff — build-from-scratch/speculative-decoding (writer, round 01)

## Original work

This piece builds two explicit, fully enumerable probability models (a
character bigram target and a target/unigram-mixture draft), implements
standard autoregressive sampling and the full speculative draft-then-verify
loop from scratch against them, and then runs both to the point of empirical
proof: it checks the accept/reject sampler's single-token and joint
two-token output frequencies against the exact target probabilities computed
directly from the same tables (not estimated, summed), and it checks the
measured acceptance rate and tokens-per-target-call against an exactly
computed acceptance rate and against Leviathan et al.'s own formula — none of
which the evidence record or the cited papers do for the reader; the papers
state and prove the theorem symbolically, they do not hand over a runnable
instantiation with its own committed numbers. That is the one thing this
article does to the evidence that the evidence does not do itself.

## Paths changed

- `library/build-from-scratch/speculative-decoding.html` — the article.
- `library/build-from-scratch/speculative-decoding/speculative_decoding.py` —
  the complete, runnable implementation (target/draft tables, baseline
  sampler, `speculative_step`/`speculative_generate`, exact `beta`/`alpha`
  computation, all print statements). Stdlib only (`random`); no numpy was
  available in this workspace, so the stationary-distribution computation
  used for the exact `alpha` is a hand-written power iteration.
- `library/build-from-scratch/speculative-decoding/run_output.txt` — the
  exact, reproducible stdout of that script, committed for provenance. Every
  number quoted in the article (the single-token table, the joint-pair
  table, and the five-row acceptance-rate table) is copied verbatim from
  this file. Reproduce with `python3 speculative_decoding.py` from that
  directory (seeded, deterministic; re-running produced byte-identical
  output in this session).

## Proof result

`nb check library/build-from-scratch/speculative-decoding.html --series
build-from-scratch --repo /home/user/the-nightly-build` (the brief's exact
command, link-checking on) → **BLOCK: 0**, 1 warning, verdict PUBLISHABLE.

Warning intentionally left:
- `W-SENTENCE-DENSITY`, one 59-word sentence with punctuation score 35. This
  is the verbatim quotation of Leviathan et al.'s accept/reject rule from
  Section 2.3 ("keeping it if q(x) ≤ p(x), and in case q(x) > p(x) we reject
  the sample with probability 1 − p(x)/q(x)..."). House style requires
  quoting exactly what was read rather than paraphrasing a primary source's
  stated rule, so the sentence was left whole rather than split or trimmed.

All other findings from the first check run (15 sentence-density warnings,
36 em-dashes against a limit of 4, 2 uses of the banned term "mechanism"
against a limit of 1) were fixed by rewriting, not suppressed: sentences
were split, dashes were replaced with periods/colons/semicolons or cut
outright, and the "mechanism" sentence was reworded.

## Voice and furniture notes

- Every flex section carries at least one inline citation (`cite_rule:
  per-section` satisfied); the two founding papers (Leviathan et al., Chen
  et al.) and the six follow-ons (Medusa, EAGLE, Draft & Verify, Lookahead,
  PyTorch's `gpt-fast` post, vLLM's blog) are cited in first-appearance
  order matching the evidence record's own numbering, so sources 1–8 above
  need no renumbering.
- The one annotated equation (furniture limit: at most one per article) is
  the accept/reject rule and its residual (Fig. 2). The proof identity and
  the acceptance-rate definition ride as bare, uncaptioned equations, cited
  in the surrounding prose, per the furniture doc's rule for a step the
  prose fully carries.
- No chart was used. The evidence record itself recommends treating the
  founding papers' own result tables as furniture rather than image assets
  since the data is already discrete numbers; the same reasoning applied to
  this piece's own run, so all quantitative results are `nb-table`, not
  `nb chart` output. No source image asset was captured: nothing in the
  evidence's "Source assets" list met the bar of "the argument spends what
  it shows" better than the equations and this piece's own tables already
  do.
- Measured `nb-meta` values: 8 sources, 3,764 words, 19 reading minutes —
  all taken directly from the engine's own `Article.word_count` and source
  count on the final file (`PYTHONPATH=engine python3 -c "from nb.article
  import Article; ..."`), not estimated.

## Open items

None outstanding for evidence or voice. The notation swap between the two
founding papers (p/q meaning reversed between Leviathan et al. and Chen et
al.) is stated once, early, and never left implicit next to code.
