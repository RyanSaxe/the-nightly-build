# Commission: daily-brief/2026-11-20

Run: scheduled edition of 2026-11-20 (Friday). Neighbours in this edition: reinforcement-learning/potential-based-shaping (a lesson on reward shaping) and feature/top500-ageing-installed-base (the November 2026 TOP500 list). The brief does not carry the TOP500 list as an item.

## Assignment

Six items in the series order: Word of the Day, three news items, two technology items, as the series prompt sets. Selection of the items is delegated to the researcher under the series prompt's rules and these decisions:

- News window: events of 18–20 November 2026, or what changed in that window on a running story.
- Running stories the last three briefs covered (17–19 November): Iran–US strikes around Bahrain, Kuwait and Qeshm; measles elimination lost in the US, Mexico and Bolivia; Anthropic's IPO; Nvidia's board and Jensen Huang; the NSA/federal outages; California v. OpenAI; Commerce chip-license rule; Java4Shell; GPT-6.2 Astra system card; Qwen4-Max. Return to one of these only if something material changed after the last brief, and then report only the change.
- Word of the Day: a coinage with a documented inventor and date, per the series prompt. Recent words to avoid repeating in kind or in item: snowclone, sprezzatura, grue, and every word in the word-of-the-day series (the researcher can list them with `nb history --series word-of-the-day`). Prefer a word outside linguistics and philosophy, since the last three came from there.
- Technology items: avoid two items about frontier-model releases; at most one item from AI labs.
- The headline is built from the strongest of the six items, chosen by the writer.

## Production

- Policy (not required): writing-coach low, researcher high, writer medium, editor high (required). Actuals: all roles run as subagents on the orchestrator's model; the coach and writer at the closest available effort (low, medium), the researcher and editor at high.
- min_sources 6, one per item. Strict word band 300–700.

## Recent-pattern notes for writer and editor

- The last three headlines each came from the lead technology or news item and named an actor plus a number ("Sixty-five characters of Base64 can corrupt memory...", "The NSA's classified network goes offline...", "California sues OpenAI, alleging..."). Keep the headline a plain claim, but do not reuse the "<count> ... can ..." or "<Actor> sues ..., alleging" builds.
- Word items have recently ended on a quoted remark from the coiner ("Wonder if it'll catch on?") or a quoted line from the source text. Do not end the word item on a quotation by default.
- News items often end on "X says/said ..." reaction lines. Use a reaction only where it is news.

## Decisions after research (researcher/01)

- Items accepted as selected: soliton; Senate permitting bill; Shenzhen declaration; ICJ Myanmar judgment; nginx security releases; Gemini 4 Neon.
- ICJ: the Court's own text is blocked to us, so the item attributes the vote and holdings to the reports that carry them (ASIL, The Conversation) and states nothing beyond them.
- nginx: the 19 November brief led with an AI-found memory bug in OpenJDK. Report the nginx fixes on their own terms (versions, CVEs, nginx's severity ratings against the researchers' claim). Do not frame it around AI discovery unless the primary says so, and do not let it lead the brief.
- Gemini 4 Neon: benchmark figures are Google's own; attribute them or leave them out. Price and context window can be stated from Google's page.

## Decision during drafting (writer/01)

- Shenzhen item: the comparison with the 13 November White House line on "the reduction of nuclear weapons" is dropped, since its only source in hand was this paper's own 15 November brief. Decided: the item reports what the signed declaration contains and lacks, from the declaration itself. Not restored.
