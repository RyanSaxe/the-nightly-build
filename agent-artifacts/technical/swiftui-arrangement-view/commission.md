# Commission

## Assignment

- Produce one Technical article for the open Technical section, using the slug `swiftui-arrangement-view` and the `article` template.
- Explain SwiftUI's iOS 27.1 `ArrangementView` as a semantic container for a primary and secondary view, and show how split and overlay styles change adaptive two-pane interfaces.
- Include a concrete Swift code example and a practical boundary: when `ArrangementView` is right, when ordinary stacks or custom layout remain clearer, and how to handle the device geometry it responds to.
- Keep this distinct from the Feature's AI-governance reporting and the Daily Brief's FAA/Huawei items.

## Editorial thesis and structure

- Establish that an arrangement maps available size, aspect ratio, and active division regions to view placement, then introduce iOS 27.1 availability and the primary/secondary model.
- Section 1: build the smallest player/up-next `ArrangementView`; explain the `secondary` closure and `.arrangementViewStyle(.split)` with exact API spelling.
- Section 2: compare split and overlay as semantic choices. Explain horizontal/vertical axes, the single-view fallback when the requested split axis is unavailable, and `overlayArrangementZIndex`.
- Section 3: show `splitArrangementLayoutRatio(0.3)` as a layout preference rather than fixed pixels, including what happens when geometry cannot honor it.
- Section 4: report Apple's bounded Duo simulator z-index issue and workaround, then conclude with the decision rule for `ArrangementView`, stacks, custom `Layout`, or grids.

## Source plan

- Use Apple's Tech Talk, SwiftUI updates, ratio and style documentation, reserved-region documentation, Developer Forums report, and release record. Open each supporting passage before citing.
- Treat the forum post as a concrete implementation report, not a prevalence claim. Do not invent performance numbers or claim untested snippets compile.

## Form and quality bar

- Use an orientation plus four named sections and a short exact Swift code listing.
- Explain what Apple demonstrates versus what the article infers. Call the ratio a preference and scope the simulator bug to its reported environment.
- Update metadata, source count, word count, reading time, date, title, and dek. Resolved policy: researcher capable/high, writer capable/medium, editor inherit/high.
