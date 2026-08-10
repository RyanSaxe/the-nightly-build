# writer brief: paper-of-the-day/clip (01)

Inputs:
- `agent-artifacts/paper-of-the-day/clip/editorial-direction.md` — house standard, press voice, series prompt, declared reader
- `agent-artifacts/paper-of-the-day/clip/writing-coach/01/voice-guide.md` — how this piece should sound
- `agent-artifacts/paper-of-the-day/clip/researcher/01/evidence.md` — the complete claim set available to you
- `.nb-work/paper-of-the-day/clip/library/paper-of-the-day/clip.html` — the initialized paper article to edit in place
- `.nb-work/paper-of-the-day/clip/.nb-context/` — effective template contract, runtime assets, furniture catalogs

Output: `agent-artifacts/paper-of-the-day/clip/writer/01/draft-handoff.md`
Proof: `./nb check .nb-work/paper-of-the-day/clip/library/paper-of-the-day/clip.html --series paper-of-the-day --library /home/user/library-checkout`

Focus this round: rebuild the argument with the paper's own artifacts. Set the
contrastive objective as `nb-math`/`nb-math-eq` (symmetric cross-entropy over
scaled cosine-similarity logits, from the Figure 3 pseudocode the evidence record
quotes) and show how a zero-shot classifier is built from label text at inference.
Bring the figures the claim turns on into the article as source assets (`nb
asset`, `nb-figure`): the Figure 1 method summary and the Figure 13 robustness
plot (Figure 14 as support), each with a caption and prose that say what it
settles. Capture source assets only from figures the evidence record identifies in
a cited primary; inspect each rendered asset.

Framing correction — read the commission's "Correction from research" section and
follow it. CLIP did NOT claim the language objective or zero-shot protocol caused
the robustness; it named its pre-training data as a candidate cause and said it
had no confident answer (Section 3.3). Do not stage the follow-on (Fang et al.,
ICML 2022) as overturning a confident CLIP claim or as a concession. The accurate
story: CLIP demonstrated a robust zero-shot classifier and was careful about why;
controlled follow-on then isolated the training distribution as the cause and
ruled out the "language supervision buys robustness" reading, confirming CLIP's
own hedge. Carry the two caveats from the evidence record: the data-cause result
traces largely to one research lineage and has not been reproduced by an unrelated
lab, and it is the data distribution/composition (Nguyen et al.), not sheer size,
that matters.

Recent habits to break (see commission): write a concrete, surprising headline the
reconstruction defends, without echoing recent papers' sentence shape, and reach
the verdict without copying the "what X established / what isn't argued" closing
mold.
