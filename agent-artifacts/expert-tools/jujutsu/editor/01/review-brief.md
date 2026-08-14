# editor review-brief: expert-tools/jujutsu (editor/01)

Inputs:
- ../../editorial-direction.md — house standard, slop, headlines, article-template identity, series prompt
- ../../commission.md — the tool, the one workflow change to prove, the honest-cost requirement, the reader
- ../../writer/01/brief.md — the exact writer brief (to catch leakage)
- ../../writing-coach/01/voice-guide.md — read first
- ../../researcher/01/evidence.md — the verified model, command sessions (jj 0.44.0), costs, backing ambiguity
- ../../writer/01/draft-handoff.md — the writer's original-work sentence and construction notes
- the article: /home/user/the-nightly-build/.nb-work/expert-tools/jujutsu/library/expert-tools/jujutsu.html
- /home/user/the-nightly-build/.nb-work/expert-tools/jujutsu/.nb-context — template contract, furniture catalogs

Output: ./editorial-review.md
Fresh proof after direct edits is run by the orchestrator; new prose/evidence
goes back to the writer.

Recent-pattern notes (compare dek and section headings against these):
- Recent expert-tools deks follow a capability-then-caveat mold ("... thins to the
  provider's own feature the moment you point it at a hosted API"; "... covers less
  than the word suggests"; "... still can't run a match statement"). A dek in that
  mold is a formula here; the honest cost belongs in the body.
- The series requires the tool and the work it changes named in the headline and
  section titles; confirm that is real naming, not a slot.

This round's focus:
- Verify the demonstration against the evidence: the code listing must reproduce
  the evidence's verified botched-rebase-then-undo session (commit/operation IDs,
  observable output) with nothing invented. The writer ties `jj undo`'s behavior
  to release v0.33.0 and tested against 0.44.0 — confirm both version claims are
  supported by the evidence, and that no command output is fabricated.
- The honest-cost section must carry real weight: the four named costs (Git-backend
  index corruption, lossy same-change conflict resolution, missing hooks / no
  `--fixup`, bookmark-push and colocation friction), each sourced.
- The backing question: confirm the article states the README-vs-paid-contributors
  contradiction and the governance-cap math honestly, without defaulting to
  "Google's tool" or "a funded startup's tool."
- Any inline <code> is for literal strings the reader would type; check it is not
  used as technical emphasis. Verify headline/dek/subheads descriptor by descriptor
  against the evidence, and open every citation href as printed.
