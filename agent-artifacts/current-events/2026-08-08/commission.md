# Commission: current-events/2026-08-08

## Subject
The US-focused general-news brief for **Saturday, August 8, 2026**: four to six
of the day's most consequential developments, selected for impact on law, public
policy, public institutions, or people's material conditions — not a topic quota
and not what is merely trending.

## Selection standard (writer/researcher own the final slate)
Favor developments that change law, policy, institutions, or material
conditions. Include an international story only where omitting it would make the
brief misleading, sized to its importance. Put technology here only when its
*public consequences* are the news; developments in the field belong to the
tech-news desk today. Routine political theater does not qualify.

## Candidate leads to verify or reject (not a required slate)
The researcher selects and verifies the day's real slate; these are starting
points seen in early scouting for on/around Aug 7-8, 2026, each to be confirmed
against a primary record and rejected if thin:
- The **Right to Worship Act** buffer-zone bill introduced Aug 7 (Cruz, Slotkin,
  Knott, Suozzi). Report it as news only — neutral, primary-sourced. Today's
  opinion desk argues it; this brief must **not** editorialize or duplicate that
  argument.
- Reports that U.S. precision-missile stockpiles are severely depleted after the
  Iran conflict, and the administration's pushback — verify the underlying report
  and the response separately.
- A major air-traffic-control outage closing Midwest airspace (FAA/DOT record).
- A U.S. intelligence assessment on Russia's willingness to take provocative
  "gray zone" action toward NATO (include only if it clears the international bar).
- Any court ruling, agency action, or economic release dated Aug 7-8 that meets
  the standard.

## Boundaries
- `brief` template; 4-6 items; **exactly one primary source per item** and **at
  least one independent secondary** (series per_item policy). min_sources 5
  (template floor); real slate will exceed it.
- Every item carries its primary record and an independent account; prefer a
  reputable US newsroom for the independent account when quality is comparable,
  and use the primary regardless of country.
- Each item explains why it matters (consequence), not just what happened.
- The paper assumes the day's headlines; do not recap, analyze the consequence.

## Neighbors in this run
Opinion (right-to-worship-act) argues the buffer-zone bill; tech-news
(2026-08-08) covers field developments (Terafab, AI-datacenter power, etc.).
Keep the buffer-zone item here to neutral reporting, and keep field-tech stories
in tech-news, not here, unless their public/policy consequence is the news.

## Habits not to inherit (recent current-events)
Recent briefs sometimes led with a dated-title headline ("Current Events, August
1, 2026") and sometimes with a claim headline; use a real claim headline naming
the day's single most consequential development, not a date label. Vary item
lead shapes; avoid the comma-triad dek mold.

## Production
Harness: claude-code, isolated role subagents. Models by resolved policy —
writing-coach (low), researcher (high), writer (medium) at capable tier; editor
(high) required, inherits. No deviation. Writer sets `nb-meta` harness/model to
match the current published library exactly.
