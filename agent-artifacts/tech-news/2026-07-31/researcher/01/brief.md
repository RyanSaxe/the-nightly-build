# Researcher brief — tech-news/2026-07-31 (01)

## Role
Load and follow `skills/researcher/SKILL.md`. High effort. Web access. Select AND
verify tonight's technology slate.

## Begin with these exact inputs
- `agent-artifacts/tech-news/2026-07-31/editorial-direction.md`
- `agent-artifacts/tech-news/2026-07-31/commission.md`

## Task
Find the 4-6 most consequential technology developments of ~2026-07-30/31
(AI-central, but significance decides). Start from the commission's candidate
slate (Gemini Robotics 2; EU AI Gigafactory call; China's AI-agent rules; plus
others), verify each against its PRIMARY (the vendor's/agency's own announcement,
technical report, paper, or regulatory text), discard promotion/incremental
releases, and add any bigger development missed. Respect the AVOID list (the five
recent tech-news items; no emergence/scaling item — Paper of the Day owns that;
no US-policy-consequence story — that's Current Events).

## Per-item evidence requirement
For EACH recommended item, record:
- The **primary** record (announcement / technical report / paper / release /
  regulatory text) — opened and read, with the exact capability/number/claim it
  owns and a locator. Classify `primary`.
- At least one **independent secondary** account (reputable newsroom or
  independent evaluation) — opened and read. Where the claim is a
  capability/benchmark, prefer an independent evaluation over the vendor's own
  number, and note any gap between vendor claim and independent result.
- Classify `data-nb-kind` honestly. Every URL resolves; never record an unread
  URL (a 403/paywall is gated — find the primary or an open account).

## Output (write only this)
`agent-artifacts/tech-news/2026-07-31/researcher/01/evidence.md`
A ranked slate of 4-6 items, each with: proposed headline, 1-3 sentence technical
core, primary (URL, kind, locator, verified claim/number), independent secondary
(URL, kind), and any vendor-vs-independent discrepancy. Add a "considered and
dropped" list with reasons and flag anything borderline for the correspondent.

## Control signal
Return exactly one line:
`DONE researcher agent-artifacts/tech-news/2026-07-31/researcher/01/evidence.md`
or `REQUEST correspondent <need>` / `BLOCKED researcher <reason>`.

## Scope discipline
`./nb` (after `export PATH="$HOME/.local/bin:$PATH"`) and web tools for focused
work. `./nb history --library /home/user/library --series tech-news` to avoid
repeating recent items. Do not tour the repo/archive otherwise.
