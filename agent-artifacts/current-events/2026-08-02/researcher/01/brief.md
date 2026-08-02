# Researcher brief: current-events/2026-08-02 (01)

## Your job
Produce `evidence.md` here: the verified evidence record for tonight's US news
brief (4-6 items). You verify and select the record; the writer drafts only from
it. This is a same-day brief, so discovery is part of your job.

## Begin with these inputs
- This brief; `../../commission.md` (candidate slate, selection standard,
  per-item source rule); `../../editorial-direction.md` (house floor + brief
  identity + series prompt).

## Procedure
1. For each candidate item in the commission, open the **primary** record
   (official statement, filing, ruling, agency dataset, or the party's own
   words) and confirm it is a genuine, still-live development as of 2026-08-02.
   Read the cited passage; verify every number, name, title, and date against
   that primary. Then find **at least one independent** account (a newsroom or
   party with no stake in the primary's author).
2. Drop any candidate that is stale (predates the window with no 08-02
   development), thin, or fails the significance bar. Discover replacements by
   searching the day's record so the final slate is the day's *most consequential*
   US developments (law, policy, institutions, material conditions).
3. Keep tech-*field* stories out (route to tech-news); keep only tech with public
   consequences. Coordinate: do not select an item the tech-news brief will run.
4. Classify each source primary/secondary with a reason (authorship + stake).
   Two retellings of one origin count as one source. Accusations need two
   independent confirmations by parties in a position to know.
5. Search for what contradicts each item's framing; record it.

## Output: evidence.md
Open with one paragraph on what the day's record supports and where it is thin.
Then, per the researcher skill's stable sections:
- **Sources**: one entry per source read — URL (must resolve), primary/secondary
  + reason, what it establishes firsthand or repeats, verbatim locators, exact
  titles/roles of named people/bodies.
- **Contradictions**, **Numbers** (every figure: owning primary, exact reading,
  unit, denominator, period), **Source assets** (or `None found`), **Discarded**.
- Group Sources by proposed item so the writer sees each item's primary + its
  independent account, and note your recommended 4-6 item slate and lead order.

## Constraints
Minimum 5 sources; per item exactly 1 primary + 1+ independent secondary. Never
record an unverified URL; a paywall/403 is gated, try a browser fetch first.

Return `DONE researcher <path>`; `REQUEST orchestrator <need>` if the slate needs
a selection decision; `BLOCKED researcher <reason>` if the day's primaries are
unreachable.
