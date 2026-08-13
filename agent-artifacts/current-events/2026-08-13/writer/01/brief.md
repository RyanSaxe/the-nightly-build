# writer brief: current-events/2026-08-13 (01)

Inputs:
- editorial-direction.md (house standard, slop, headlines, press voice, brief
  template identity, series prompt) — at the artifact root
- commission.md (the beat, the selection standard, the split with tech-news) — at
  the artifact root
- writing-coach/01/voice-guide.md (how the items should sound)
- researcher/03/evidence.md (the COMPLETE record — use researcher/03; the final
  4-item slate is here, all fully sourced)
- the initialized article: library/current-events/2026-08-13.html
- template context under .nb-context/

Output: writer/01/draft-handoff.md

Proof: ./nb check .nb-work/current-events/2026-08-13/library/current-events/2026-08-13.html --series current-events --library /home/user/library-checkout

The slate (from researcher/03), four fully-sourced items, each with exactly one
primary and at least one independent secondary labelled honestly with
data-nb-kind: (1) three states executing inmates the same day, the first since
2010; (2) the birthright-citizenship order narrowing recognition for four
categories; (3) the memorandum authorizing vetted private companies to run
offensive cyber operations against foreign criminal organizations; (4) the NFA
registration injunction taking effect, with the first unregistered transfers
completed at 12:01 a.m. on 08-13.

Two accuracy bounds the record forces (item 4): the injunction is party-specific,
not nationwide (the court cited Trump v. CASA's bar on universal injunctions), so
do not describe it as striking the requirement down for everyone; and DOJ's reason
for not appealing is not established by any source — report the silence as fact,
do not speculate on the cause. Order items by consequence; lead with the one that
matters most. Each item's "why it matters" does analysis, not recap; assume the
reader already knows the day's headlines.

Recent shapes to break (from the commission): the brief headlines on the single
most consequential item's finding, not a thematic summary line (that is the
tech-news habit). Vary deks/headings from the recent record.

nb-meta: date "2026-08-13", harness "claude-code-routine", model "claude-sonnet".
Run `nb stamp` before the final links-checked proof.
