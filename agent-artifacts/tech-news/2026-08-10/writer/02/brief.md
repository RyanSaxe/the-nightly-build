# writer brief: tech-news/2026-08-10 (02) — revision

Inputs:
- `agent-artifacts/tech-news/2026-08-10/editorial-direction.md`
- `agent-artifacts/tech-news/2026-08-10/writing-coach/01/voice-guide.md`
- `agent-artifacts/tech-news/2026-08-10/editor/01/editorial-review.md` — apply every required item
- `agent-artifacts/tech-news/2026-08-10/researcher/03/evidence.md` — the corrected evidence for the lead item (supersedes 02 for item 1; items 2-5 carried forward)
- `agent-artifacts/tech-news/2026-08-10/writer/01/draft-handoff.md` — your prior handoff
- `.nb-work/tech-news/2026-08-10/library/tech-news/2026-08-10.html` — the article to revise in place (already carries the editor's two in-place fixes: item 2 "thirteen days", item 3's "to line up with the EU" clause removed — preserve them)

Output: `agent-artifacts/tech-news/2026-08-10/writer/02/draft-handoff.md`
Proof: `./nb check .nb-work/tech-news/2026-08-10/library/tech-news/2026-08-10.html --series tech-news --library /home/user/library-checkout`

Apply the editor's required items, no more:

- Lead item (OpenAI ten advances): realign the claims and the dek to researcher/03.
  The two stories were conflated — the August "ten advances" release is distinct
  from the May Erdős unit-distance result that humans verified; do NOT import the
  May event's human verification into this item. Replace the misidentified
  independent source with the Simon Willison post researcher/03 cites (correct
  byline Simon Willison), and fix the s2 source-entry author label. State the
  verification status exactly as researcher/03 records it: the Lean 4 certificates
  are machine-checkable and compile, full peer review is pending, and no named
  mathematician is documented as having worked through the informal arguments.
  Drop the "reaction, not verification" quote and any Gowers/Bloom named reactions
  (those were tied to the misidentified article). Only name "Astra" or cite a
  price figure if researcher/03's record supports it; otherwise keep the earlier
  restraint.
- Item 4 (Terafab, s9 Electrek): confirm the "$119 billion" multi-phase figure
  actually appears at the printed href; if it does not, cut it or cite the source
  that carries it.

Preserve all settled work in items 2-5 and the editor's in-place fixes. Do not
expand the claim set beyond the corrected evidence. Rerun the full proof to
`BLOCK: 0`. In the handoff, add one line per editorial request resolved.
