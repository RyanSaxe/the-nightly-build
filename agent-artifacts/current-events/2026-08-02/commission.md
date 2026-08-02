# Commission: current-events/2026-08-02

## Assignment

The US general-news front page for UTC date 2026-08-02, on the `brief`
template. Authorized by the scheduled `nb duty` result (rolling series, selected
UTC date unpublished). One brief, 4-6 items.

## Angle and required contribution

Select the day's most consequential US developments: events that change law,
public policy, public institutions, or people's material conditions. Every item
earns its place by consequence, not popularity. Each item states, in its own
reasoning, why it matters to the reader now, spending the reported facts as
premises rather than recapping a headline the reader already saw. No topic
quota; do not manufacture an item to reach a count. An international story is
included only when leaving it out would make the brief misleading, sized to its
importance.

## Boundaries and neighbors

This edition also runs a Tech News brief for the same date. Split by the press
rule: a development *in* technology (a model, a research result, a security
disclosure, a product) belongs to Tech News; a story whose *public
consequences* are the news (a court ruling, a regulation, a market or
macro-economic event with policy stakes) belongs here. Do not run the same
event in both briefs. If an AI or tech story's public-policy consequence is the
day's real news, it may sit here, but coordinate so the two briefs do not
double-cover it.

Prefer a reputable US newsroom for independent reporting of comparable quality;
use the primary record regardless of country; use non-US reporting when it holds
the original reporting or is closer to the event.

## Recent shapes to break (from the published library)

The last several current-events briefs led on the same macro/institutional
spine: Q2 GDP at 1.5% with Fed dissents (2026-08-01), the Blanche AG nomination
stall (07-31), and direct US-Iran strikes (07-30). Do not re-lead on a framing
already carried unless the day genuinely advanced it materially, and if you do,
lead on what is *new*, not the standing situation. Vary the dek from the
recent molds: the semicolon reversal, the suspended "the real question is
whether," and the comma-triad-with-"and" are banned (see headline standard).

## Source policy

Template floor: `min_sources: 5` overall. Per item: exactly one primary
(`primary: [1, 1]`) and at least one independent secondary (`secondary: [1,
null]`). Every item carries its primary record and at least one independent
account. Verify every URL resolves; a paywall is gated, not dead.

## Production (models and effort)

Balanced profile. Resolved roles and the models this run assigns:

- writing-coach: capable → `sonnet`, effort low (not required)
- researcher: capable → `sonnet`, effort high (not required)
- writer: capable → `sonnet`, effort medium (not required)
- editor: inherit → `opus` (this correspondent's model), effort high, **required**

Runtime caveat: isolated children run at their model's default reasoning effort;
effort tiers are not separately tunable here. Model is set per role above, which
is the honored lever. The required editor runs on the correspondent's model
(`opus`), the closest available option to "inherit at high effort."

## Original work

The brief's distinct value is the selection-and-consequence judgment: which few
events actually matter today and the specific reason each changes the reader's
world. That reasoning, per item, is the article's original work.
