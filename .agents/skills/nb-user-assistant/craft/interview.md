# Dynamic editorial interview

An interview discovers a coherent paper. It does not collect fields. Maintain
a live model of what is known, uncertain, and contradictory. Ask one compact
question or one related cluster at a time, using the user's previous answer to
choose the next move.

## Required outcomes

Reach confidence on purpose, reader, territory, evidence standard, voice,
recurring series, reading rhythm, how visual the paper should be, how much
production usage the user can sustain, and first-week coherence. These are
goals, not a prescribed order. Skip what the user already made concrete and
revisit an apparent answer when later evidence contradicts it.

When the desired evidence standard depends on sources behind a login or
paywall, surface the constraint immediately: scheduled research reads the
public web, and a source the user is entitled to read but must authenticate
for currently requires significant harness-specific setup, tracked as
upstream issue #127. Settle a source standard the runtime can actually meet,
and treat authenticated access as a separate project the user opts into.

## Settle sustainable production usage

Learn how the scheduled runtime is billed before discussing production cost.
A subscription has provider-specific plan limits. Token totals do not reveal
what share of a weekly or monthly allowance one run will consume. Say that
plainly. Use the provider's usage report after the first normal production run
as the baseline, then help the user adjust the paper from measured experience.
The scheduled-runtime smoke test does not produce articles and cannot supply
that baseline.

A metered API supports a dollar estimate only when the exact provider, models,
and current input, output, and cached-token prices are known. Give an estimate
only when the user asks for one. Include likely repeated role invocations and
identify continuing orchestrator usage as unknown unless the runtime measured
it. Never convert a published token observation into a subscription estimate.

Turn the user's tolerance into editorial and production choices. Article count
and cadence set how much work becomes due. Series boundaries and commissioned
items control how much discovery the researcher must do. Production policy can
assign different model tiers to each role and series. Preserve every editorial
role, evidence requirement, and proof gate when reducing usage.

## Interview loop

1. **Discover.** Ask for the desired reader experience and the frustration or
   curiosity behind the paper. Concrete reading habits reveal more than
   demographic labels.
2. **Form hypotheses.** Offer a small number of distinct interpretations. Name
   the tradeoff in each so the user can react to something real.
3. **Test examples.** Generate representative subjects, headlines, evidence
   situations, and article shapes. Ask which feel inevitable, surprising, or
   wrong and why.
4. **Test counterexamples.** Present plausible work the paper should reject.
   Boundaries sharpen a beat and expose whether two proposed series overlap.
5. **Synthesize.** Reflect the editorial principle in the user's language,
   separating settled choices from open ones. Invite correction of the model,
   not approval of your eloquence.
6. **Simulate.** Lay out a credible first week. Check variety, cumulative
   reading load, repeated structures, source feasibility, and whether the paper
   fulfills its stated purpose.
7. **Approve.** Ask decisions only on remaining consequential alternatives.
   Approval covers the editorial specification, not hidden publication or
   account mutations.

## Question quality

A good question makes two plausible futures distinguishable. "Who is the
audience?" invites a label. "Should an engineer already building retrieval
systems learn more from this paper than a product leader deciding whether to
fund one? What would each consider wasted space?" exposes the knowledge and
decision boundary.

Do not stack ten unrelated questions, force multiple-choice answers when the
space is not understood, or ask the user to restate repository facts. When
their answer is abstract, test it with an example before requesting a better
adjective.

The interview is complete when you can predict how the user will judge a new
article idea and explain why each proposed series belongs in the same paper.
