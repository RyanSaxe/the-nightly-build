# Commission: daily-brief/2026-11-19

Series: daily-brief (template brief, strict). Six items in the series order: Word of the
Day, three news items, two technology items. Words 300 to 700, at least six sources.
Authorized by the scheduled `nb duty` result for 2026-11-19 (rolling, slug is the date).

## Assignment

- News: the three most important US developments reported 17 to 19 November 2026, or a
  change in that window on a running story. An international or New York item displaces
  a national one only on importance.
- Technology: two developments from the same window: a release, a capability, a
  research result or a policy change that alters what builders can do.
- Word: a word with a documented coinage or a traceable story, one a well-read person
  has probably not met. Not a common word with an ordinary etymology.

## Boundaries

- Do not repeat stories the paper ran on 16 to 18 November as items: the NSANet outage
  and the week of US outages, the Crimean Bridge strike, Nvidia's board and Huang, the
  Commerce data-center chip rule, the Nature Sustainability data-center electricity
  study, California's suit against OpenAI, the $50 billion air-traffic-control request.
  A material new development on one of them qualifies only if it changed in the window.
- Words already used, which may not return: sprezzatura, apophenia, waldo,
  ultracrepidarian, nocebo, psephology, and every word in the word-of-the-day series
  (`nb history --series word-of-the-day`).
- The Feature and the Reinforcement Learning lesson in this edition do not touch the
  brief's ground; the lesson is on specification gaming in RL, the feature topic is set
  separately and will be added below.

## Recent pattern notes (from the last five briefs)

- Leads open "X goes down / X sues / X and Y press" with the actor first; vary it.
- Deks recently lean on "Officials blame...", "The complaint, filed in..." and a
  dated-filing construction. Do not reuse those molds.
- News items repeatedly close on a third sentence of who-blamed-whom; close an item on
  what follows only where the source states it.

## Decisions

- One strong source per item; the primary record where it can be opened.
- Model and effort: writing-coach and researcher run as subagents on the session model
  (the policy asks for a "capable" model at low/high effort; recorded as served by this
  runtime's default subagent model). Editor inherits the orchestrator model at high
  effort as required.

## Decisions after research (orchestrator)

- Items accepted as in researcher/01/evidence.md: snowclone; Anthropic IPO pricing; PAHO
  withdraws US measles elimination; US strike on Qeshm and Iran's strike on Ali Al Salem;
  Java4Shell; GPT-6.2 Astra and Sol.
- Iran stays over the Peltola Senate call: the US striking Iranian territory and Iran striking
  Kuwait is a change in the war, which outranks a called race. Lead with the new facts, not
  the war's background; attribute every Iranian claim to Iran, and say no Kuwaiti or CENTCOM
  statement was available if the item would otherwise read as confirmed.
- GPT-6.2 prices rest on secondary reports because OpenAI's post was gated; attribute them.
- The Anthropic valuation of about $1.5 trillion is CNBC's calculation; attribute it or omit
  it. Do not call it the largest IPO on record without the SpaceX qualification.
- The measles item reports PAHO's formal decision and that it covers three countries; the
  15 November feature already reported the loss as coming.
- Snowclone is a word about stamped phrasing; do not build the item on the eggcorn item's
  structure (31 October).
- Trump–Xi–Putin: no outcome at research time; not included.
