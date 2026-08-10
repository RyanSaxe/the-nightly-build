# editor review-brief: paper-of-the-day/clip (01)

Inputs:
- `agent-artifacts/paper-of-the-day/clip/editorial-direction.md`
- `agent-artifacts/paper-of-the-day/clip/commission.md` — includes the "Correction from research" section on the framing
- `agent-artifacts/paper-of-the-day/clip/writer/01/brief.md`
- `agent-artifacts/paper-of-the-day/clip/writing-coach/01/voice-guide.md`
- `agent-artifacts/paper-of-the-day/clip/researcher/01/evidence.md`
- `agent-artifacts/paper-of-the-day/clip/writer/01/draft-handoff.md`
- `.nb-work/paper-of-the-day/clip/library/paper-of-the-day/clip.html`
- `.nb-work/paper-of-the-day/clip/.nb-context/`

Output: `agent-artifacts/paper-of-the-day/clip/editor/01/editorial-review.md`

Recent-pattern notes: recent reconstructions headline with a specific surprising
claim and several close on a "what X established / what isn't argued" section with
`nb-note`. Flag that closing mold and any copied opener as formula.

This round's focus, and the load-bearing correctness check: the article must NOT
stage the follow-on (Fang et al., ICML 2022) as overturning a confident CLIP claim
or as a concession CLIP made. The evidence record shows CLIP explicitly hedged in
Section 3.3, naming its pre-training data as a candidate cause and disclaiming a
confident answer, so the after-record confirmed CLIP's own guess. Any sentence
that says or implies CLIP claimed language supervision or zero-shot caused the
robustness is a factual error to fix or route. Verify the contrastive-objective
equation against the paper's Figure 3 pseudocode, the zero-shot ImageNet number,
and that each source-asset figure's caption states what it settles. Check the two
caveats are present (the data-cause result traces to one research lineage; it is
the data distribution, not size, that matters). Source assets and chart provenance
go to the writer; inspect each rendered asset.
