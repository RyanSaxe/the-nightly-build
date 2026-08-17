# editor review-brief: expert-tools/beartype (01)

Inputs:
- editorial-direction.md   ../../editorial-direction.md
- commission.md            ../../commission.md
- writer brief             ../writer/01/brief.md (the exact brief the writer worked from)
- voice-guide.md           ../writing-coach/01/voice-guide.md
- evidence.md              ../researcher/01/evidence.md
- draft-handoff.md         ../writer/01/draft-handoff.md (carries the original-work sentence and the writer's open questions)
- article (edit in place)  /home/user/the-nightly-build/.nb-work/expert-tools/beartype/library/expert-tools/beartype.html
- effective contract       /home/user/the-nightly-build/.nb-work/expert-tools/beartype/.nb-context

Output: /home/user/the-nightly-build/.nb-work/expert-tools/beartype/agent-artifacts/expert-tools/beartype/editor/01/editorial-review.md

Recent-pattern notes (compare edges, headings, dek, furniture against these for formula):
- The recent expert-tools dek mold is a headline claim immediately undercut by a shrinking caveat ("the guarantee holds on X and thins to Y"; "covers less than the word suggests").
- The recent headline mold is "Tool verbs your noun."
- Recent tools were Python-heavy; watch for a generic "useful library" framing that any tool would fit.

This round's focus:
- Verify the article locates beartype's distinctiveness correctly and does not overclaim: random-only O(1) sampling (the full-walk strategy is unimplemented) plus decoration-time code generation and zero dependencies, NOT "samples instead of walks" (typeguard also samples). Check this against the evidence Contradictions.
- Confirm every overhead figure is attributed as beartype's own unreplicated self-benchmark, never as neutral fact.
- Two writer decisions to judge (see draft-handoff): (1) the writer omitted beartype's "typeguard 107 minutes" competitor self-benchmark entirely — decide whether that omission is right or whether an attributed version is owed; (2) the two code listings are illustrative and follow beartype's documented violation shape, but beartype was not executed, so there is no captured REPL traceback — verify the code and the caught-bug claim are honest and match beartype's documented behavior, and that nothing reads as a real captured run that was not one.
