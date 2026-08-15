# editor review-brief: build-from-scratch/flash-attention (editor/01)

Inputs (all under this article's artifact root, plus the article):
- editorial-direction.md
- commission.md — the subject, the reconstruction, boundaries, habits to break
- writer/01/brief.md
- writing-coach/01/voice-guide.md (read first)
- researcher/01/evidence.md — the confirmed math and claims, and its thin spots
- writer/01/draft-handoff.md — the original-work sentence and two judgment calls
- the article:
  .nb-work/build-from-scratch/flash-attention/library/build-from-scratch/flash-attention.html
  and the committed chart provenance beside it
- template context under .nb-work/build-from-scratch/flash-attention/.nb-context/

Recent-pattern notes (watch these):
- The rotary-position-embeddings piece (2026-08-08) closed on "What relative
  position does not buy" with a closing nb-note verdict. Do not let this piece
  copy a "what X does not buy / what would have to change" closer or a default
  closing nb-note-strong verdict box. No colon-subtitle headline. Vary heading
  construction.

Round's focus:
- Sources floor: the proof left W-SOURCES-MIN standing (4 sources against the
  series floor of 8). Never pad citations. But judge whether the reconstruction
  genuinely stands on only these four primaries or whether legitimate additional
  sources exist that a researcher could actually read and cite (for example the
  attention/transformer origin, a GPU memory-hierarchy reference, memory-efficient
  attention predecessors, the softmax numerical-stability standard, a production
  implementation's docs). If real sources would strengthen the piece and meet the
  owner's floor, route to the researcher for a round-02 evidence addition rather
  than approving under the floor. If the four truly carry it, say so explicitly.
- The runnable experiment is the argument: confirm every number the article
  asserts is actually produced by the committed code and reported honestly (the
  equivalence diffs, the peak-memory series and crossover, the overflow count),
  and that the piece does not overclaim (exact math and memory scaling, not the
  kernel's wall-clock speedup; the papers' memory-Big-O exclusions differ).
- The writer set the single annotated nb-math equation as the scalar
  Milakov-Gimelshein recurrence rather than the block-tiled FlashAttention form;
  judge whether that is the right "one equation the article is about."
- Preview note (not a defect to fix here): KaTeX/Prism did not load under the
  local sandbox's egress policy, so typeset math and code highlighting could not
  be visually confirmed; the engine ships these pinned in the built site, and
  nb render-check reported no page errors. Flag it to watch at CI, not to edit.
