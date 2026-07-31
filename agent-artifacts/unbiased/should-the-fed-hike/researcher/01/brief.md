# Researcher brief — unbiased/should-the-fed-hike (01)

## Role
Load and follow `skills/researcher/SKILL.md`. High effort. Web access. This is a
STRICT unbiased piece: min 10 sources, ≥4 primary, ≥3 secondary. Gather the
evidence for BOTH positions with equal rigor.

## Begin with these exact inputs
- `agent-artifacts/unbiased/should-the-fed-hike/editorial-direction.md`
- `agent-artifacts/unbiased/should-the-fed-hike/commission.md`

## Verify the event (primary record)
- The **July 2026 FOMC statement** and implementation note (federalreserve.gov):
  the exact target range, the decision, and the recorded dissents/vote.
- The **dissenters**: confirm the three names (Hammack, Kashkari, Logan) and that
  each favored a 25bp HIKE; the "most dissents since September 2016" claim.
- **Chair Powell's press-conference** remarks / statement for the majority's hold
  rationale.
- Inflation data: **CPI and/or PCE** releases (BLS/BEA) establishing inflation
  above 2% for 5+ years and the recent tariff-/energy-driven pressure.
Record exact numbers with locators; classify each `primary`.

## Build each position's case (equal scrutiny)
- **Raise now (Position A):** find the best-documented dissenter rationale — a
  speech, statement, or interview by Hammack, Kashkari, or Logan explaining WHY
  they wanted a hike (expectations un-anchoring, five years above target, real
  rate not restrictive). A direct, cited quote from a named holder is required.
  Add supporting evidence/economists making the hawkish case.
- **Hold (Position B):** find the majority/Powell rationale (supply-shock nature
  of tariff/energy inflation, labor-market cooling, policy lags) as a direct cited
  statement, plus at least one named economist arguing that hiking into a
  supply/relative-price shock is a mistake. A direct, cited quote from a named
  holder is required.
- For BOTH: verify the consequential factual claims (vote, names, range,
  years-above-target, tariff/energy attribution) against reputable independent
  reporting (WSJ, Bloomberg, NYT, FT, NPR, CNBC) — these are your secondary
  sources (≥3).

## Source floor & classification
≥10 sources, all read and resolving; ≥4 primary, ≥3 secondary. Classify each with
a one-line reason and locator. A 403/paywall is gated — use the Fed's own site,
BLS/BEA, transcripts, or open reporting; never record an unread URL.

## Output (write only this)
`agent-artifacts/unbiased/should-the-fed-hike/researcher/01/evidence.md`
Organize by: (1) the verified event facts with primary locators; (2) Position A
evidence with the named holder's exact cited quote(s) and supporting data;
(3) Position B evidence likewise; (4) the shared factual claims each side agrees
on; (5) full source list classified primary/secondary with reasons; (6) discarded
sources. Give the writer a direct, quotable, cited statement from a named holder
for EACH side.

## Control signal
Return exactly one line:
`DONE researcher agent-artifacts/unbiased/should-the-fed-hike/researcher/01/evidence.md`
or `REQUEST correspondent <need>` / `BLOCKED researcher <reason>`.

## Scope discipline
`./nb` (after `export PATH="$HOME/.local/bin:$PATH"`) and web tools for focused
work. Do not tour the repo/archive as background.
