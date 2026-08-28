# writer brief: paper-of-the-day/mamba (01)

Inputs:
- editorial-direction.md — house standard, citation rules, press voice, series prompt (artifact root)
- commission.md — the paper, the claim, what to examine and weigh, recent habits (artifact root)
- writing-coach/01/voice-guide.md — how this reconstruction should sound
- researcher/01/evidence.md — the verified equations, empirical claims, figure provenance, and post-publication record
- the initialized article: .nb-work/paper-of-the-day/mamba/library/paper-of-the-day/mamba.html
- template context under .nb-work/paper-of-the-day/mamba/.nb-context/

Output: .nb-work/paper-of-the-day/mamba/agent-artifacts/paper-of-the-day/mamba/writer/01/draft-handoff.md
Proof: ./nb check .nb-work/paper-of-the-day/mamba/library/paper-of-the-day/mamba.html --series paper-of-the-day --library /home/user/library-checkout

Rebuild the argument in your own order and examples: the SSM recurrence and
discretization, the selection mechanism, and why selectivity forecloses the
global convolution so the hardware-aware scan is what makes it practical. Set the
math the reconstruction leans on using the template's equation furniture rather
than paraphrasing it. Bring the paper's own figures the claim turns on into the
article as source assets with `nb asset` (the ones the evidence names: the
associative-recall/induction result, the LM scaling curves, the throughput
figure), each with a factual cited caption and prose that says what it settles.
Weigh the evidence as a reviewer and state a verdict before the sources: what
Mamba established, what the record since confirmed or qualified (Mamba-2, hybrids,
the recall/copying limits), and where the claim stops. Assume the reader knows
attention is memory- and compute-bound; flash-attention was covered on 08-21.

Recent habits to break (detail in commission): keep a claim-first headline but
find Mamba's own; do not narrate the figures — derive and weigh with them.
