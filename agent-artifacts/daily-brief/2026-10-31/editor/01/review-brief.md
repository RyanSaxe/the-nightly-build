# editor review-brief: daily-brief/2026-10-31 (editor/01)

Inputs:
- `../../editorial-direction.md`
- `../../commission.md` (the edition's decisions and the recent-record notes)
- `../../writer/01/brief.md` (the exact writer brief, with the six binding caveats)
- `../../writer/01/draft-handoff.md`
- `../../writing-coach/01/voice-guide.md`
- `../../researcher/01/evidence.md`
- The article: `/home/user/the-nightly-build/.nb-work/daily-brief/2026-10-31/library/daily-brief/2026-10-31.html`
Proof: `/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/daily-brief/2026-10-31/library/daily-brief/2026-10-31.html --series daily-brief --repo /home/user/the-nightly-build`
Output: `editorial-review.md` in `editor/01/`

Decide whether this brief publishes, and edit it until it can. The writer reports
a clean proof at 676 words with 12 sources.

Check hardest on the binding caveats from the writer brief; a brief fails readers
fastest when a display line overstates a court order or a figure:
- California item: the restraining order's geographic scope must NOT be stated
  (reports disagree). Confirm the 2-1 Ninth Circuit vote and the ~20,000 ballots
  against the cited pages; the writer added a CBS source for the subpoenas and a
  second NBC page for the Ninth Circuit, so audit each citation's href and kind.
- Economy item: the 3.4% annualized Q3 GDP and the 3.6% twelve-month September
  PCE must not be conflated with the 2.1% annualized-quarterly PCE. One framing.
- Veterans item: NPR's own framing (payments up at least $150/month for 15,000+
  veterans after VASP ended; analysis, not new policy). The word "steered" must
  not appear.
- robots.txt item: a proposal with no IETF standing, wildcards do not count as an
  opt-out, Google support only planned (2027). Not an adopted standard.
- Mistral item: benchmark figures are Mistral's own; attributed or omitted.
- Word item: eggcorn's definition (Merriam-Webster) and the coinage story
  (Pullum, late Sep 2003, Language Log); the story rests on Language Log/OED as
  the record pins, not the unopened 2003 post.

Recent-record notes to judge formula against (the writer cannot see the library):
recent brief titles lean on a reflexive "Supreme Court ..." lead and on a
bare-date roundup line ("Six developments for Thursday, October 1"); recent deks
have used the comma-triad and the semicolon reversal. The current title leads on
the California order. Judge the title, the dek and the six item headlines against
spec/headlines.md and against these habits, and confirm the six headlines are
built differently from one another.

Strict series: the word band 300-700 and the banned-term limits (em-dash 4,
leverage 1, load-bearing 0, mechanism 1) BLOCK, so keep your edits inside the
band and re-run the proof. Make the edits you can from the evidence record and
this checkout; after direct cuts, run `nb stamp` and the proof command yourself
and return to me (the orchestrator) only if a change needs a fact nobody
gathered. Write `editorial-review.md` with your findings, every edit, and the
decision. Report the review path and the decision (approve | redraft).
