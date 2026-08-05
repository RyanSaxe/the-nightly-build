# Commission: current-events/2026-08-05

## Authorized work
Scheduled duty for UTC 2026-08-05 returned `current-events` (rolling, `brief`
template) for the unpublished date 2026-08-05. Publish exactly one brief for
that date. This is the only current-events article this run.

## What this brief is
The US-focused general-news front page for 2026-08-05: 4-6 selected items, each
stating the finding with its actors named and saying why it matters. This is a
*rolling news* piece: the subject is the day's actual developments, so selection
happens in research against live reporting, not from a pre-chosen topic. The
researcher assembles the candidate set from the primary records and reputable
independent reporting; the writer selects and orders the final 4-6.

## Selection standard (from the series prompt)
- Favor developments that change law, public policy, public institutions, or
  people's material conditions. No topic quota. Routine political theater and
  merely-popular stories do not qualify.
- Include an international story only when leaving it out would make the brief
  misleading, sized to its importance.
- Put technology here only when its *public consequences* are the news;
  developments in the field itself belong to Tech News (see non-overlap below).

## Sourcing
`brief` template: 4-6 items; per item exactly 1 primary + at least 1 independent
secondary; `min_sources: 5` overall. Every number verified against the primary
that owns it; every name, title, and role exact (a wrong title in display text is
the costliest error). Accusations need two independent confirmations by parties
in a position to know. Confirm every URL resolves to the source's own page, not a
fetch endpoint or aggregator.

## Template and policy
- Template: `brief` (fixed).
- Production policy (balanced): editor required at high effort, model inherit.
  Researcher/writer models = capable; writing-coach = capable, low effort.
  Actual harness recorded per role in each brief.

## Boundaries — do not repeat, and non-overlap with this edition
- Recent current-events slugs are dated 2026-07-26 … 2026-08-04 (consecutive).
  Do not re-file a story already covered as if new; carry a genuinely new
  development or a new, sourced turn in a running story. Use
  `nb history --structure current-events/2026-08-04` (and a couple of prior
  days) to see what the last briefs led with, and break those shapes.
- **Non-overlap with tech-news (same run):** a pure AI/technology/science field
  development (a new model, chip, or research result) belongs in tech-news. It
  appears here only when its *public or policy consequences* are the news.
- **Non-overlap with the opinion desk (same run):** the opinion piece this
  edition argues US frontier-AI disclosure policy off the EU AI Act's GPAI
  obligations (applicable 2026-08-02). Do NOT argue AI governance here. If a
  US-facing AI-policy action is independently the day's news, report it
  factually in one item; the argument belongs to opinion, not this brief.
- Headlines/deks: state the finding with actors named; avoid colon subtitles,
  the comma-triad dek, the semicolon-reversal dek, the suspended-question dek,
  and scaffolding subheads ("Background", "What's next"). Check recent deks
  before settling.

## Neighbors this edition
Full edition: current-events (this), tech-news, expert-tools/visidata,
investing/free-cash-flow, opinion/mandate-frontier-ai-disclosure,
paper-of-the-day/denoising-diffusion, word-of-the-day/ultracrepidarian.
Current-events and tech-news are the two Daily Reading briefs; keep their item
sets disjoint.
