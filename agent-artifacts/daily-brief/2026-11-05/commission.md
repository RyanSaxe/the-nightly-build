# Commission: daily-brief/2026-11-05

Series: daily-brief (rolling, template brief, strict). Six items in the order the
series prompt sets: Word of the Day, three News, two Technology. Word band and item
count are hard limits; one citation per item minimum; at least 6 sources.

## Assignment

- Selection window: news that happened, or changed on a running story, between
  3 November and 5 November 2026 (US Eastern). Favor national US stories chosen for
  consequence, not volume.
- The 4 November brief led with AP's calls of both chambers for Democrats, the
  Missouri map referendum, and Trump's remark on aid to Israel. Do not repeat those
  as news. A post-election item is allowed only if something new and consequential
  happened since that brief's 1:35 a.m. count (a concession, a certified result
  that changes a chamber's margin, a court ruling, a leadership move), and then it
  reports the new event, not the tally.
- Neighbouring articles tonight: feature (topic still being chosen, will be
  recorded below) and the RL course lesson on SARSA and Q-learning. The technology
  items must not cover reinforcement learning methods, and must not be the feature's
  subject.
- Technology items: a release, capability, research result or similar from the
  window. The 3 and 4 November briefs used two model-internals research results
  (weight editing; state-tracking benchmark) and a training-bug disclosure. Pick at
  least one technology item outside ML research (hardware, security, space,
  infrastructure, software release, policy on technology).
- Word of the Day: a word with a documented story and ideally a known coiner. Run
  `nb history --series daily-brief` / `nb history <word>` to make sure it has not
  appeared. Recent words: psephology, agnotology, nocebo. Avoid election and
  politics themed words three days running; pick from another field.

## Sourcing

One strong source per item; the underlying record (court order, agency release,
paper, official post) where it can be opened. Attribute unverified claims. Record
exact titles and roles as the primary states them.

## Decisions

- Lead item / headline: the most consequential of the three news items, decided by
  the writer from the evidence, and recorded in draft-handoff.md.

## Production record

| Role | Model | Effort | Note |
| --- | --- | --- | --- |
| writing-coach | session model (inherit) | low | policy: capable/low, not required |
| researcher | session model (inherit) | high | policy: capable/high |
| writer | session model (inherit) | medium | policy: capable/medium |
| editor | session model (inherit) | high | policy: inherit/high, required |

## Decisions after research (orchestrator)

- Slate: Word sphexish; News: Vance's statement that the Iran war cost Republicans
  the midterms, Johnson not running for House Republican leader, CVS Health's
  planned split; Technology: CISA's 3 November KEV listing of the exploited
  WordPress core flaw, Google turning Gemini and Search off by default for K-12
  student accounts.
- Sphexish stays even though the series prompt names it as its example: it has not
  run, and it is the kind of word the slot exists for. Tell the documented story,
  including Fabre's own contrary observation, and attribute the 1982 coinage to the
  sources that record it.
- Vance item: quote from NBC as reported. The Brent move goes in only if attributed
  to the reporting outlet; do not mix it with EIA's spot series. If it cannot be
  attributed cleanly, leave it out.
- Johnson item rests on unnamed sources in AP and NBC: attribute it as such in the
  headline and the item, and state he has made no on-record statement.
- CVS: cite the company's SEC filing; omit the share-price move (unconfirmed).
- Google item: the "turn off AI and lose Search" condition is a Google official's
  remark to the NYT, not in Google's post; attribute it, and include Google's later
  clarification.
- Lead and headline: the writer picks among the news items by consequence. The
  researcher recommended Vance; the writer may lead on it if the headline can state
  what he said with attribution.
- Feature tonight is the Ninth Circuit's Sunday Ticket opinion: no overlap.
- Orchestrator decision after editor/01: keep the editor's Google wording (CNBC's
  printed Phillips quote). The "will not have access to search" quote is not
  restored, because no opened page shows it.
