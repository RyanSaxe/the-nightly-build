# Commission — current-events/2026-07-30

## Assignment
Tonight's US-focused general-news front page for **2026-07-30** on the `brief`
template. Select the day's **most consequential** developments — events that
change law, public policy, public institutions, or people's material conditions.
Do not fill a topic quota; routine political theater and merely-popular stories
do not qualify. You must do live web research to establish what actually
happened on/around 2026-07-29 and 2026-07-30.

## Selection rules (from the series prompt)
- 4–6 items. Significance decides the mix, not balance.
- Include an **international** story only when leaving it out would make the
  brief misleading; size it by importance, not a world-news quota.
- Put technology here only when its **public consequences** are the news; a
  development in the field itself belongs to Tech News (which also publishes
  tonight — do not double-run the same story).

## Source obligations (per item — strict geometry)
- Every item carries **exactly one primary** (the ruling, filing, dataset,
  official statement, or a party's statement about itself) **and at least one
  independent secondary** account. For independent reporting prefer a reputable
  US newsroom of comparable quality; use the primary record regardless of
  country; use non-US reporting when it holds important original reporting or is
  closer to the event.
- min_sources 5 overall. Read each source; verify every number/quote against the
  primary that owns it. Record primary/secondary kind + locator per citation and
  carry into `data-nb-kind`. A 403/paywall is gated, not dead — never record an
  unverified URL. Each item is a **judgment about why it matters**, not a recap.

## Prevent repetition (recent current-events items)
Do not re-run or lightly re-angle: 2026-07-28 (Trump admin tells SCOTUS its
voter-list order isn't in effect), 2026-07-27 (Rogoff sues Trump over the
firing), 2026-07-26 (Vance/Caine objected to escalating with Iran). A genuine
new development *in* an ongoing story is fine; a status-recap is not. Vary item
openers and the per-item shape from the recent briefs; no colon-subtitle
headlines on items.

## Tonight's neighbors (avoid collision)
tech-news brief (same night) owns field/technology developments; keep public-
consequence political/economic stories here and coordinate so no single story
runs in both. Also tonight: boeing, knowledge-distillation, nirsevimab,
bowdlerize.

## Output paths
- Article: `.nb-work/current-events/2026-07-30/library/current-events/2026-07-30.html`
- Artifacts: `.nb-work/current-events/2026-07-30/agent-artifacts/current-events/2026-07-30/`

## Runtime for nb-meta
harness `claude-code` · writer `claude-opus-4-8` (capable, high) · editor
inherited `claude-opus-4-8`, high, required. date = 2026-07-30 (UTC), mode
`rolling`.

## Required contribution
A selective, sourced front page where each item earns its place with a reason it
matters, every claim anchored to the primary that owns it.
