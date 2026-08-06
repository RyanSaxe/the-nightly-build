# Commission: tech-news/2026-08-06

## Authorized work
Scheduled duty for 2026-08-06 returned `tech-news` (rolling, daily) with slug
2026-08-06 unpublished. This run commissions exactly that dated brief.

## Subject and selection
The technology front page for Thursday, 2026-08-06. Select the day's most
consequential technology developments. Artificial intelligence is central, but
significance decides the mix; product promotion, incremental releases, and
online attention do not qualify on their own. Science and health belong when a
result changes technical knowledge or practice enough to deserve attention here;
treat the research itself as the development rather than forcing a category.

## Template and geometry
Template `brief` (shortread). Items band [4, 6]. Cite rule per-item. Each item
is a full-sentence claim headline that says why it matters, then explains it.
Use nb-brief-item per item; add nb-table / nb-stat where an item's evidence has
that shape (recent editions used a small table to compare model claims).

## Sources (per item)
Per-item floor: primary [1,1] (the paper, the release, the filing that owns the
claim) and secondary [1, null] (at least one independent account). Template
brief floor min_sources 5 overall. For a research result, the paper/preprint is
the primary and must be read, not its write-up. Prefer a reputable US newsroom
for independent reporting of comparable quality; use non-US or primary sources
where they are closer to the event. Verify every benchmark number and claim
against the owning primary; a lab's self-reported score is a claim, label it as
one.

## Coordination with the sibling Current Events brief (same run, same date)
Both briefs publish for 2026-08-06. Do not double-cover the same story. This
brief owns field/industry technology and AI/science research developments.
Public-consequence news (law, policy, courts, elections, disasters, public
health as public policy) belongs to current-events. If a development is a
research result that changes practice, it is this brief's even if it also has
public resonance.

## Production policy (resolved via `nb production-policy`)
- writing-coach: model capable, effort low
- researcher: model capable, effort high
- writer: model capable, effort medium
- editor: model inherit, effort high, REQUIRED

Actual harness: roles run as isolated Claude subagents on model
`claude-opus-4-8` (capable tier; required editor "inherit" resolves to this
correspondent model). Deviation recorded: this runtime's subagent launcher does
not expose a per-invocation reasoning-effort control, so the required editor
"high effort" is approximated by the most capable available model at the harness
default effort. No model was traded down.

## Neighboring articles this run
current-events/2026-08-06 (sibling brief), company-analysis/eli-lilly,
paper-of-the-day/instructgpt, parenting-research/teething,
word-of-the-day/luddite. The InstructGPT longread already owns RLHF/alignment
reconstruction; if an AI item touches alignment, keep it to the day's news and
do not duplicate that piece's territory.

## Recent tech-news coverage and habits not to inherit
Recent editions (2026-08-01..05) led with: Alibaba's Qwen3.8-Max release
without weights, OpenAI's Lean-verified proofs for ten open problems, a
misconfigured multi-model test, GPT-5.6 rewriting its own serving code, Claude
finding a post-quantum crypto weakness. Do not re-lead with a story already
covered unless there is a genuinely new 2026-08-06 development. Habits to break:
- Recent leads are all frontier-lab AI model releases/capability claims. If the
  day's firmest results are peer-reviewed science/health, let significance —
  not an AI quota — set the lead (a recent edition did exactly this).
- Vary item-headline and dek cadence; avoid the same-shaped clause stack.
Required furniture (nb-brief-item, Sources) is not a habit to avoid.

## Original contribution expected
A selective, correctly-sourced technology front page for 2026-08-06 where each
item's significance is argued and rests on the primary that owns the claim,
with lab self-reports labeled as claims rather than facts.
