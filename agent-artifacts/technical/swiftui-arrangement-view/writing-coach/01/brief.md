# Writing-coach brief: technical/swiftui-arrangement-view (01)

Inputs:

- `commission.md`: article assignment, sequence, API scope, source plan, and quality bar.
- `agent-artifacts/technical/swiftui-arrangement-view/editorial-direction.md`: exact editorial, slop, template, press, and series directions.
- `.agents/skills/nb-writing-coach/SKILL.md`: role and artifact constraints.

Output: `.nb-work/technical/swiftui-arrangement-view/agent-artifacts/technical/swiftui-arrangement-view/writing-coach/01/brief.md`

Directions only. Do not edit the generated HTML or supply draft prose.

## Audience

- Write for a widely read audience with strong mathematics and computer science knowledge.
- Assume the reader can read Swift and understands ordinary stacks, but introduce `ArrangementView`, primary/secondary semantics, arrangement styles, aspect ratio, reserved regions, and layout preference at first use.
- Optimize for a reader deciding whether this abstraction fits an adaptive two-pane interface and wanting enough implementation detail to test that decision.
- Keep the explanation technically exact without turning the piece into a catalog of every new SwiftUI geometry API.

## Teaching sequence

- Use the orientation to define an arrangement as a relationship that maps available size, aspect ratio, and active division regions to view placement; then establish the iOS 27.1 availability and the primary/secondary model.
- Section 1: move from the smallest player/up-next example to the meaning of the `secondary` closure and the `.arrangementViewStyle(.split)` choice. Explain only the setup required to understand the later behavior.
- Section 2: compare split and overlay as different semantic choices. Cover horizontal and vertical axes, the single-view fallback when the requested split axis is unavailable, and `overlayArrangementZIndex` when content moves in front.
- Section 3: use `splitArrangementLayoutRatio(0.3)` to teach proportional preference rather than fixed-pixel sizing. State what the framework may do when current geometry cannot honor the preference.
- Section 4: use the reported Duo simulator z-index issue and Apple's workaround as a bounded implementation edge. Close by applying the adoption rule to `ArrangementView`, ordinary stacks, custom `Layout`, and grids.
- Make each section depend on the concept established before it. Do not open with generic responsive-design advice or defer the concrete example until after API taxonomy.

## Code-example goals

- Include a compact, code-shaped Swift example for a player as primary content and an up-next panel as secondary content.
- Preserve the documented spelling and casing of `ArrangementView`, the `secondary` closure, `.arrangementViewStyle(.split)`, `.splitArrangementLayoutRatio(0.3)`, the overlay style, and `overlayArrangementZIndex`.
- Show the smallest useful split implementation first; add only the lines needed to demonstrate style selection, proportional sizing, overlay ordering, or the relevant axis behavior.
- Explain a line only when its layout effect is not apparent from the API name. Keep code literals exact and use a code listing rather than scattering API tokens through prose.
- Treat the listing as an implementation example, not a measured benchmark. Do not invent performance, memory, or device-behavior results.
- Verify initializer and modifier signatures against Apple's current documentation before publication; do not fill gaps with plausible SwiftUI syntax.

## API boundaries

- Present `ArrangementView` as the framework abstraction for a meaningful primary/secondary relationship, not as a replacement for every multi-panel layout.
- Treat `.split` and overlay as arrangement-style decisions with different placement semantics; cover the documented axis behavior and the documented single-view fallback without generalizing beyond the source.
- Describe `splitArrangementLayoutRatio(0.3)` as a layout preference. Do not describe it as a fixed width, guaranteed fraction, or pixel measurement.
- Use `overlayArrangementZIndex` only for the overlay ordering problem described by the source. Do not conflate it with a claim that all SwiftUI z-index behavior has changed.
- Keep reserved-region or hinge behavior tied to the geometry inputs that matter for this article. Do not expand the piece into a survey of Duo APIs.
- Scope availability statements to the documented iOS 27.1 release and supported targets. Do not imply that earlier systems or every device expose the same behavior.
- Preserve the boundary between `ArrangementView` and ordinary stacks, custom `Layout`, and grids. The latter remain appropriate for linear or arbitrary multi-panel composition.

## Practical decision rule

- Recommend `ArrangementView` when the interface has one primary view and one secondary view whose relationship should adapt to available geometry, aspect ratio, or a reserved division region.
- Prefer an ordinary stack when the composition is a straightforward linear arrangement with no primary/secondary semantics or system-selected fallback to explain.
- Prefer custom `Layout` or a grid when the composition needs arbitrary panel counts, independent placement rules, or geometry behavior outside the documented arrangement model.
- Treat a requested ratio as a preference and test narrow, wide, split, overlay, hinge, and fallback geometries before relying on the result.
- Keep the reported simulator workaround attached to the specific Duo simulator bug and environment. Do not turn one forum report into a general adoption verdict.

## Source discipline

- Use Apple's Tech Talk as the main technical record for arrangement inputs and outputs, primary/secondary semantics, split behavior, overlay behavior, z-order, and Apple's choice guidance.
- Use Apple's current SwiftUI updates page for the September 2026 additions and Apple's individual documentation pages for the ratio modifier, split style, and reserved-region concept.
- Use Apple's release record only for availability dating, not for API semantics.
- Use the Apple Developer Forums report as a concrete implementation report: preserve its environment, exact bug diagnosis, and workaround; do not infer prevalence or framework-wide unreliability from it.
- Open every cited source and locate the supporting passage before writing. Prefer the primary Apple record over summaries, and preserve the distinction between what Apple's demonstration establishes and what the article infers for adoption.
- Verify API names, signatures, availability, axes, fallback behavior, ratio semantics, and workaround details against their owning documents. Cite claims a reader could dispute, and cut or qualify any claim the sources do not reach.
- Do not use social posts, influencer commentary, or third-party summaries as authority for API behavior. Use practitioner evidence only when it is firsthand, relevant, and independently checkable.

## Ending requirement

- End the final section with the concrete adoption boundary: semantic primary/secondary relationship and adaptive system geometry favor `ArrangementView`; simple linear or arbitrary composition favors stacks, custom `Layout`, or grids.
- Include the testing implication for new device geometry and the narrowly scoped simulator limitation before the decision, so the conclusion follows from the walkthrough rather than from a generic recommendation.
- Do not close on a reading list, a pointer to another article, a generic lesson about responsive design, or an uncheckable claim about the future of SwiftUI.

## Slop watchlist

- Cut generic responsive-design openings, filler transitions, throat-clearing, and hypothetical-reader address.
- Test every opening, section ending, and final sentence for an empty conclusion or a subject-swappable claim.
- Avoid vague attribution such as “developers,” “experts,” or “the community”; name the Apple document, forum author, or observed environment.
- Avoid inflated claims that `ArrangementView` is transformative, universal, automatic, or a complete replacement for custom layout.
- Avoid metaphor, decorative framing, rhetorical questions, self-reference, and formulaic “what this means” transitions unless the specific material requires them.
- Check every `not X but Y`, `not just X`, three-part cadence, repeated section-heading pattern, inflated copula, and trailing `highlighting` or `underscoring` clause.
- Do not hide uncertainty behind careful-sounding qualifications. State the exact unsupported geometry, reported bug, missing measurement, or source limit.
- Keep fixed API names in code formatting where exact spelling matters; do not turn ordinary technical nouns into decorative inline code.
- Do not add prose merely to meet a word count, source count, or section-ending formula.
