# Commission: tech-news/2026-08-10 (rolling)

## The brief

Select the day's most consequential developments in technology for 2026-08-10:
four to six items. Artificial intelligence is central to the brief, but
significance decides the mix. Product promotion, incremental releases, and online
attention do not qualify on their own. Science and health belong when a result
changes technical knowledge or practice enough to deserve attention here; treat
the research itself as the development.

## Candidate raw material (verify and select; not a required list)

The week's record around this date includes: a new frontier model release with
agentic-reasoning claims; an FDA authorization creating a class of "autonomous
diagnostic AI" that makes a diagnostic call without a physician in the loop; and
continuing rollout of AI-transparency rules requiring systems to identify
themselves to users. Confirm each against the primary record — the model card or
vendor documentation, the FDA authorization document, the regulation's own text —
and select by consequence, not by this list. The autonomous-diagnostic-AI item is
a strong candidate because the change is in what the technology is permitted to
do, not in a benchmark.

## Do not re-report

The 2026-08-08 and 2026-08-09 briefs already led on the pentalayer-graphene
superconductivity result and the Black Hat finding that a single untrusted GitHub
issue reached remote code execution through coding-agent harnesses. Cover new
developments or materially new turns, not restatements of those.

## Required contribution

Each item earns its place by consequence and carries the reader to what actually
changed and why it matters, with the primary record cited. Where an item is a
model or a benchmark claim, report the number the vendor's own chart omits when
the independent record supplies it.

## Template, sources, furniture

Template: `brief`. Each item is its own section with `nb-brief-item`; the lead
item sets the brief's headline and dek. Per the source policy, every item carries
exactly one primary record and at least one independent account. Use `nb-table`
only where an item's numbers are clearer shown than told.

## Recent habits not to inherit

Recent tech briefs led with a model-or-lab claim and a dek that supplies the
figure the vendor left out, which is a good instinct — keep the skepticism, but
write each headline and dek fresh against `spec/headlines.md`, avoiding the
negative-parallelism and comma-triad dek molds, and vary how item headings are
built.

## Runtime

Harness `claude-code-routine`; model Opus 4.8 for every role. Production policy
asks researcher/high, writer/medium, writing-coach/low, editor/high (required).
Per-invocation reasoning effort is not separately settable through this runtime's
child launches, so each role runs at the session's effort; the editor gate is
preserved in full. Writer records `harness: claude-code-routine` and
`model: Opus 4.8` in nb-meta.
