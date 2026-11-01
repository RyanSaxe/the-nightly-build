# editorial-review: daily-brief/2026-11-01 (editor 01)

## Verdict: SETTLED

Every change this piece needed was a direct cut I made. No writer round is
owed. The article is left ready for the orchestrator to re-stamp (my cuts make
the stamped `words: 627` stale) and prove. `nb check` returns BLOCK 0, WARN 0,
PUBLISHABLE both before and after my edits.

## Direct cuts I made

1. **Arch item, unsupported claim removed.** The item closed "...approves the
   arch at its meeting that day, and its chairman has said he plans to vote for
   it." The NCPC chairman's stated voting intention is nowhere in
   `researcher/01/evidence.md`, nor in the writer's own re-fetch notes of the
   cited Spokesman-Review source (`draft-handoff.md` lists what that source
   supports and the chairman detail is not among them). A one-citation item
   cannot carry a claim the citation does not support, so I cut the clause. The
   item now ends on the sourced fact: when construction could begin.
2. **Arch item, standalone date.** Changed "Construction could begin Thursday"
   to "Construction could begin 5 November." A reader arriving from a link has
   no anchor for "Thursday"; the date is in the cited source and reads the same
   for everyone.
3. **Arch item, tense.** Changed "They asked Judge Tanya Chutkan" to "They ask"
   to match the item's own present-tense "sue ... on 31 October" and the house
   present-tense-for-events rule. This keeps the researcher's required "ask
   Judge Chutkan" framing (not "is weighing") and does not reintroduce any
   claim that the case is assigned to her.
4. **VOLTA item, trimmed to three sentences.** Cut the fourth sentence, "Talos
   says the fallback chain shows the operator expected refusals." The series
   caps each item at two or three sentences and this item ran to four. The
   preceding sentence already states the failover-on-refusal behavior, so the
   inference added length without adding a fact the reader could not already
   draw. The item now ends on the concrete behavior.
5. **Nordhaus item, dead metaphor.** Changed "He died after a battle with
   glioblastoma" to "He died of glioblastoma." "Battle with" is decorative and
   says nothing the plain verb does not.

## Required changes for the writer

None.

## Correctness and citations

Checked each claim against `researcher/01/evidence.md`. The five researcher
corrections flagged in the writer brief are all honored in the draft:

- **Alaska.** The "sham" characterization is attributed to DOJ and its New York
  Times basis, not stated as fact. The item says the only immediate relief
  sought is preserving and segregating ballots (ECF No. 67, p.19) and does not
  claim the state moved to dismiss for the first time on 31 October (it does not
  mention the state's filing at all). NVRA preemption is attributed to the
  filing.
- **Arch.** "They ask Judge Tanya Chutkan to halt the project," not "is
  weighing." No TRO language. No claim the case is assigned to her.
- **bafflegab.** Coinage dated "1952" with no month. No "possibly" hedge
  attributed to Merriam-Webster; M-W carries the definition (gobbledygook) and
  the newspaper date (19 January 1952) sits with the coinage history source.
- **VOLTA.** "The model ranks the victim's own assets by monetization value" —
  the victim's own assets, not victims against each other.
- **Cursor.** "uninstalling the extension may not be sufficient," the source's
  wording, not "does not remove." "About 11 hours" stated loosely per the
  researcher's arithmetic; no affected-user figure printed.

Each of the six items carries exactly one citation (the Word of the Day carries
two: Merriam-Webster for the definition, Worldwide Words for the coinage), seven
sources total, each `data-nb-source` resolving to the item it supports. No
fabricated or decorative citation. The two technology items are framed as
findings reported by their sources (Talos, Cursor), neutral and with no
self-reference; Cursor's statement that Anthropic did not build the modified
versions is carried. The original work the handoff claims — reporting DOJ's
narrowed relief as the day's lead rather than the certification fight — holds.

## Headlines

- **Title.** "Justice Department says it now seeks only to segregate Alaska
  ballots" — subject, verb, the surprise ("now ... only") first. No colon
  subtitle, no question. Defensible from ECF No. 67 p.19.
- **Dek.** "Its 30 October filing in federal court cites a second candidate
  named Dan Sullivan, days before Election Day." Adds the who and the stakes the
  title left out, does not restate it, and is built on none of the three banned
  molds (no semicolon reversal, no suspended question, no comma triad).
- **Section headings.** All five are concrete, in each item's own nouns, and
  built differently from one another; none is a scaffolding slot. The first
  heading and the title both lead with "Justice Department" because the title
  promotes the lead news item, but they report different facets (the narrowed
  relief versus the underlying allegation), which the Daily Brief format
  intends.

## Slop

Tested every item's first and last sentence and the article's last sentence.
After the cuts above, each item opens on a concrete development and closes on a
checkable fact, none hands the point back, and none survives the placeholder
test as a reusable pattern. No empty conclusion, no performed carefulness, no
puffery, no vague attribution ("experts," "observers"), no self-reference. The
Nordhaus "battle with" metaphor was the one decorative figure and is gone.

## Banned terms

Counted in the prose, not only in the proof: em-dash 0 (limit 4), "leverage" 0
(limit 1), "load-bearing" 0, "mechanism"/"mechanisms" 0 (limit 1). Inline
`<code>` is used only for strings a reader would match or type
(`Anthropic.claude-code`, `authorized_keys`), not for product or model names.
