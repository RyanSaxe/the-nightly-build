# editor review-brief: feature/binance-hack-freeze (01)

Inputs (all absolute):
- Editorial direction: .../agent-artifacts/feature/binance-hack-freeze/editorial-direction.md
- Commission (holds the recent-feature patterns to enforce): .../commission.md
- The exact writer brief: .../writer/01/brief.md
- Evidence: .../researcher/01/evidence.md
- Voice guide (read first): .../writing-coach/01/voice-guide.md
- Draft handoff: .../writer/01/draft-handoff.md
- Article to judge/edit: /home/user/the-nightly-build/.nb-work/feature/binance-hack-freeze/library/feature/binance-hack-freeze.html

Output: editorial-review.md in .../editor/01/

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/binance-hack-freeze/library/feature/binance-hack-freeze.html --series feature --repo /home/user/the-nightly-build

Decide whether this feature publishes, and edit it until it can. Change anything except the facts; send back only if it needs a different argument.

Correct (this is a live, provisional incident — be hard here): state the thesis (the freeze-ceiling finding) and its claims from the draft alone. Reopen the cited sources and read past the quoted passage. Verify every figure against the owning document and its scope: the stolen total (Binance vs TRM ranges), the frozen total, and above all the asset/chain composition that the freeze-ceiling argument depends on — if the piece asserts a per-asset split the evidence marks provisional, it must say so, and if the record cannot support the split, the claim must be narrowed to what it supports (narrowing to hide thin reporting is not allowed; the review says which happened). Confirm the North Korea attribution is presented as TRM's assessment in TRM's words, not as settled fact, and that Binance's breach finding is attributed as an initial finding. Check every number/title/date in the headline, dek and subheads. Open every citation href — it must land on the source, not a homepage. Audit every data-nb-kind (a news outlet repeating a figure is not an independent primary for it).

Reads well / slop: hold the whole piece to spec/slop.md, hardest at the edges and the last sentence. Enforce the recent-feature patterns in the commission: no colon-subtitle or question headline; dek not built on the banned negative-parallelism molds and not a mechanical copy of the recent "one figure in a subordinate clause" cadence; headings varied and in the piece's own nouns. Read once as someone who arrived from a link with no briefing (every term and the incident introduced in-article).

Experience: read the rendered page (nb preview). Each section should be built around a visual that earns its place; check the stolen-vs-frozen comparison and the mechanism SVG against the evidence and for overlapping labels / arrows short of target. Answer in one sentence what the piece gives beyond its sources and compare with the writer's original-work sentence.

Write editorial-review.md in the skill's shape (Correct / Reads well / The experience / Edits / Decision). After direct cuts, if the proof needs only a restamp I (orchestrator) will run nb stamp and nb check; return to the writer only where the proof fails on something needing new prose. Report the review path and the decision.
