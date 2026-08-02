# Researcher brief: tech-news/2026-08-02 (01)

## Your job
Produce `evidence.md` here: the verified evidence record for tonight's technology
brief (4-6 items). Same-day brief — discovery and verification are your job.

## Begin with these inputs
- This brief; `../../commission.md` (leads, selection standard, per-item source
  rule); `../../editorial-direction.md` (house floor + brief identity + series
  prompt: AI central, significance decides, research counts as the development).

## Procedure
1. For each candidate lead, open the **primary** (paper/preprint, official
   release, filing) and confirm a genuine, still-live 2026-08-02 development.
   Verify version numbers, org names, and every benchmark/figure against the
   primary; note where a vendor chart omits an unfavorable number. Find **at
   least one independent** account (independent testing or reporting).
2. Drop stale/thin/promotional items. Discover the day's most consequential
   technology developments by searching the record. Keep public-consequence
   stories out (route to current-events); keep tech-field results here. Do not
   duplicate the paper-of-the-day subject (an older ML paper covered in depth).
3. For a research result, read the actual paper's cited claim and its numbers,
   not the abstract or the press release. Prefer independent replication/testing
   as the secondary.
4. Classify each source primary/secondary with a reason. Search for
   contradictions to each item's framing and record them.

## Output: evidence.md
Overview paragraph (what the day supports, where thin), then Sources (URL that
resolves, primary/secondary + reason, firsthand vs repeated, verbatim locators,
exact names/versions), Contradictions, Numbers (owning primary, exact reading,
unit, denominator, period; preserve full series if a chart may help), Source
assets (or `None found`), Discarded. Group Sources by proposed item with each
item's primary + independent account, and recommend a 4-6 item slate and lead
order.

## Constraints
Minimum 5 sources; per item exactly 1 primary + 1+ independent secondary. Never
record an unverified URL.

Return `DONE researcher <path>`; `REQUEST orchestrator <need>` for a selection
call; `BLOCKED researcher <reason>` if primaries are unreachable.
