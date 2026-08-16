# writer brief: word-of-the-day/defenestration (02)

Prior artifacts to apply, not re-derive:
- Editorial review that routed this: `agent-artifacts/word-of-the-day/defenestration/editor/01/editorial-review.md` (the editor already made three direct edits in the article; apply only the routed 1419 item below)
- New evidence: `agent-artifacts/word-of-the-day/defenestration/researcher/02/evidence.md` — adds a read source establishing the 1419 deaths
- Original evidence: `agent-artifacts/word-of-the-day/defenestration/researcher/01/evidence.md`
- Article (already carries the editor's direct edits): `library/word-of-the-day/defenestration.html`

Single required fix (blocking, from the editor): the 1419 "to their deaths" / "did not survive the crowd waiting below" claim was cited to a source that establishes the throwing but not the deaths. Re-cite the 1419 deaths to the new source in researcher/02 (New World Encyclopedia, "Defenestrations of Prague"), which states seven councillors were killed by the crowd below. Attribute the count as approximate/attributed (about seven), not a settled figure, since sources differ on how many were thrown versus killed. Keep the 1419-killed versus 1618-survived contrast intact now that it carries a citation. Add the new source as a numbered source entry in first-citation order.

Do not add any other claim or source. Preserve the editor's direct edits (the removed fabricated Quinion quote and its neutral rewrite, the ~45 ft / thirty cubits height, the "three men thrown, all survived" dek) and everything else. Change only what this fix requires.

Output: a new `agent-artifacts/word-of-the-day/defenestration/writer/02/draft-handoff.md` with one line recording the resolved item.

Proof (rerun complete, links on, until BLOCK: 0):
`./nb check .nb-work/word-of-the-day/defenestration/library/word-of-the-day/defenestration.html --series word-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/980fb41b-a65b-5e72-a2d0-4a92f8c0f978/scratchpad/library-checkout`
Run `./nb stamp` on that path before the final check. Keep nb-meta `dek` identical to the rendered dekline; if a new source shifts counts, re-stamp.
