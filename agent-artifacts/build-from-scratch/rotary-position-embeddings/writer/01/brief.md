# writer brief: build-from-scratch/rotary-position-embeddings (01)

Inputs:
  ../../editorial-direction.md              house + headline standard, press voice, series prompt
  ../../commission.md                       the subject, the angle, boundaries, recent shapes to break
  ../../writing-coach/01/voice-guide.md     craft standard and licenses for this piece
  ../../researcher/01/evidence.md           the complete evidence record; the only claim set available
  the initialized article and its .nb-context (article template contract + furniture catalogs)
Output: agent-artifacts/build-from-scratch/rotary-position-embeddings/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/build-from-scratch/rotary-position-embeddings/library/build-from-scratch/rotary-position-embeddings.html --series build-from-scratch --library /tmp/claude-0/-home-user-the-nightly-build/5348099f-bd2a-54d6-a1ef-dbfbbb236392/scratchpad/library

The article file to edit is at:
  .nb-work/build-from-scratch/rotary-position-embeddings/library/build-from-scratch/rotary-position-embeddings.html
Run the proof with --no-check-links while iterating, then with links included until BLOCK: 0.

This round's focus (1500-4500 words; the code carries the argument):
- Build the demonstration in `nb-code` and let it produce the real numbers: show that
  attention logits between two tokens are invariant to a shared shift of both positions
  (relative-only) and that they decay with distance. Use the code furniture per its
  contract; the output shown must be a real run, never invented. Set the math the record
  supplies (the 2-D rotation, the relative-offset identity, `theta_i = 10000^(-2(i-1)/d)`,
  the decay) as objects the prose reasons from, with the RoFormer equation locators.
- Cover both production conventions honestly (Meta interleaved vs HuggingFace half-split)
  and the base constant in the wild (Mistral-7B = 10000, Llama-3-8B = 500000), then YaRN's
  one-line base change and its honest cost.
- Two evidence cautions to obey: (1) do NOT read RoFormer's "flexibility of sequence
  length" as usable long-context extrapolation — rotary degrades ~200 tokens past training
  length (ALiBi), and the community disagrees on *why* base-scaling helps; present this as
  the honest limit, and this candor is a strong candidate for the piece's original work.
  (2) Attribute carefully: the origin NTK-aware Reddit post could not be read firsthand
  (blocked), so cite YaRN's peer formalization for that formula, not the Reddit post as if
  opened; cite resolvable config pages (the record used open NousResearch mirrors of the
  gated Meta configs — use the address that resolves).
- Compare prototype to the real system and say what the toy leaves out. Break the recent
  BFS dek mold ("a from-scratch reproduction confirms X"). Outline the reasoning before
  naming the 2-6 flex sections.
- Set nb-meta harness = "claude-code-routine" and model = "Opus 4.8".
