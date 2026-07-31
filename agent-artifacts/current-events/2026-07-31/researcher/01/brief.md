# Researcher brief — current-events/2026-07-31 (01)

## Role
Load and follow `skills/researcher/SKILL.md`. High effort. Web access. You are
selecting AND verifying tonight's US news slate.

## Begin with these exact inputs
- `agent-artifacts/current-events/2026-07-31/editorial-direction.md`
- `agent-artifacts/current-events/2026-07-31/commission.md`

## Task
Find the 4-6 most consequential US developments of ~2026-07-30/31 that fit the
brief's selection judgment (law, public policy, institutions, material
conditions). Start from the commission's candidate slate (Blanche AG nomination
revolt; a federal terrorism conviction in the 2022 Rushdie stabbing; plus
others), verify each against its PRIMARY record, discard weak/merely-trending
ones, and add any bigger story the slate missed. Respect the AVOID list (do not
re-report the July 29 Fed hold — Unbiased owns it tonight; don't over-cover the
Iran strikes unless a specific new 7/30-31 development moved them; don't duplicate
Tech News's AI/tech-field items).

## Per-item evidence requirement
For EACH item you recommend, record:
- The **primary** record (official statement, filing, ruling, agency release, or
  the party's own words) — opened and read, with the exact fact/number it owns
  and a locator. Classify `primary`.
- At least one **independent secondary** account from a reputable (preferably
  US-based) newsroom — opened and read. Classify `secondary`.
- The one headline-worthy development + the number or caveat the headline
  dropped. Confirm every figure against the primary. Note if a story develops one
  already covered (so the writer can say so and build on it).
Every URL must resolve; a 403/paywall is gated — find the primary or an open
independent account; never record an unread URL.

## Output (write only this)
`agent-artifacts/current-events/2026-07-31/researcher/01/evidence.md`
Structure it as a ranked slate of 4-6 items, each with: proposed one-line
headline, 1-3 sentence factual core, primary source (URL, kind, locator, verified
fact), independent secondary (URL, kind), and any "develops a prior story" note.
Add a short "considered and dropped" list with reasons, and flag any item you are
unsure clears the consequence bar so the correspondent/writer can decide.

## Control signal
Return exactly one line:
`DONE researcher agent-artifacts/current-events/2026-07-31/researcher/01/evidence.md`
or `REQUEST correspondent <need>` / `BLOCKED researcher <reason>`.

## Scope discipline
`./nb` (after `export PATH="$HOME/.local/bin:$PATH"`) and web tools for focused
work. `./nb history --library /home/user/library --series current-events` to
check what was already covered (avoid repetition; note developing threads). Do
not tour the repo/archive otherwise.
