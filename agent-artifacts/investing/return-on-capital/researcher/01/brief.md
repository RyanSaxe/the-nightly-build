# Researcher brief — investing/return-on-capital (01)

## Role
Load and follow `skills/researcher/SKILL.md`. High effort. Web access.

## Begin with these exact inputs
- `agent-artifacts/investing/return-on-capital/editorial-direction.md`
- `agent-artifacts/investing/return-on-capital/commission.md`

## Verify (open the primaries)
1. **Definitions, from authority.** ROIC, NOPAT, and invested capital, from a
   reputable source (Aswath Damodaran's site/materials; McKinsey *Valuation*; a
   solid finance reference). Record the standard formula(s) AND the real
   conventions that differ: how invested capital is defined (debt + equity − cash,
   vs net operating assets), how to handle excess cash, goodwill, and operating
   leases; how NOPAT applies a tax adjustment to operating profit. The article
   must be honest that these are conventions.
2. **The value-creation test.** Source the principle that value is created only
   when ROIC exceeds the cost of capital (Damodaran / McKinsey). Get a clean,
   quotable statement and its locator.
3. **Worked example — a real company (Costco preferred for course continuity).**
   From Costco's most recent 10-K, pull the exact lines needed: operating income,
   an effective tax rate (to get NOPAT), total debt, total shareholders' equity,
   cash & equivalents (and any figure needed to compute invested capital under the
   convention the lesson will state). Record the fiscal year, the filing date, the
   exact reported numbers, and page/section locators. Compute a defensible ROIC and
   show the arithmetic so the writer can reproduce it exactly.
4. **The contrast — a capital-heavy business.** Pick and verify a real business
   whose ROIC sits near or below its cost of capital (a regulated electric
   utility, a major airline, or a large telecom). Pull the same lines from its
   most recent 10-K and compute its ROIC with the same convention, so the contrast
   is apples-to-apples. Note a credible cost-of-capital ballpark for context
   (sourced, not invented).

## Source floor & classification
Minimum 6 sources, read and resolving. Primary = the 10-K filings (SEC EDGAR) and
your arithmetic from them; the authoritative definition source. Secondary =
explanatory finance references. Classify each with a one-line reason and exact
locators (filing, fiscal year, statement line, page). Never record an unread URL;
use SEC EDGAR for filings.

## Output (write only this)
`agent-artifacts/investing/return-on-capital/researcher/01/evidence.md`
Include: verified definitions with the convention caveats; the full worked ROIC
for Costco with every input number sourced and the arithmetic shown; the same for
the contrast company; the value-creation-test statement with citation; a
cost-of-capital ballpark with source; candidate Background/Go-deeper links (the
three prior lessons are internal Background links: `how-a-business-earns-a-profit`,
`profit-versus-cash`, `what-a-company-owns-and-owes`); contradictions/conventions
flagged; discarded sources.

## Control signal
Return exactly one line:
`DONE researcher agent-artifacts/investing/return-on-capital/researcher/01/evidence.md`
or `REQUEST <owner> <need>` / `BLOCKED researcher <reason>`.

## Scope discipline
`./nb` (after `export PATH="$HOME/.local/bin:$PATH"`) and web tools for focused
work. `./nb history --library /home/user/library --series investing` only to
confirm what the prior lessons established. Do not tour the repo/archive.
