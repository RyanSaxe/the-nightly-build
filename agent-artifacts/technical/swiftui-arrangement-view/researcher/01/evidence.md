# Evidence

Checked 2026-09-24. This packet was completed in the orchestrator context after the researcher child was unavailable. Resolved directive: researcher capable/high; actual model is harness-inherited and not exposed here. API claims use Apple's own technical records; the forum report is treated as a narrowly scoped implementation report.

## 1. Apple Tech Talk: arrangement model and `ArrangementView`

URL: https://developer.apple.com/videos/play/tech-talks/111463/

Kind: primary technical record. The talk says an arrangement maps inputs such as size classes, view aspect ratio, and active division regions to outputs such as whether to show a view and what frame it receives. It says iOS 27.1 makes system-provided arrangements available in apps. Locator: transcript lines 257–259 and the indexed summary at lines 478–487.

The talk states that `ArrangementView` takes a primary and secondary view, and shows a player plus up-next view inside a `NavigationStack`. It says `.arrangementViewStyle` chooses the preferred arrangement and that split is the default style. Locator: lines 259–264.

For split, the talk says the system divides the provided bounds between primary and secondary. It defaults to horizontal when the view is wider than tall and vertical when taller than wide. Restricting axes can cause the arrangement view to show only the primary view when the primary axis cannot be used. Locator: lines 264–271 and summary line 483.

For overlay, the talk says the style prefers content above or below, can move to side by side when a device folds, and exposes `overlayArrangementZIndex` so content can switch between collapsed and expanded states. Locator: lines 272–280 and summary lines 484–485.

The talk's selection guidance maps existing `HStack`/`VStack` patterns to split and `ZStack` foreground/background relationships to overlay. It recommends split for main/detail content that should not be obscured and overlay where partial obscuring is acceptable. Locator: indexed summary lines 486–487.

Attribution boundary: these are Apple's demonstrated semantics and guidance. The talk does not prove performance, universal device support, or that every layout should migrate.

## 2. SwiftUI updates page

URL: https://developer.apple.com/documentation/Updates/SwiftUI?changes=_2_3_2&language=objc

Kind: primary API-change record. The indexed page reports September 2026 additions for ArrangementView and ArrangementViewStyle, split arrangement sizing, `splitArrangementLayoutRatio`, reserved-region queries, and iPhone Duo hinge changes. Use this source to date the API family and tie it to the September update. The rendered page requires JavaScript in the web browser, so individual API pages and Apple's Tech Talk supply the accessible semantics.

## 3. Ratio and split-style API records

URL: https://developer.apple.com/documentation/swiftui/view/splitarrangementlayoutratio(_:)

Kind: primary API record. The search result describes `splitArrangementLayoutRatio(_:)` as setting a preferred size ratio for an arrangement view. Apple's forum example applies `.splitArrangementLayoutRatio(0.3)` to the primary child inside `ArrangementView`, then uses the secondary closure. Treat `0.3` as a preferred ratio, not a fixed pixel width or guarantee.

URL: https://developer.apple.com/documentation/swiftui/arrangementviewstyle/split

Kind: primary API record. Apple's search result describes split as an arrangement style that places primary and secondary views side by side along one or more axes. Pair it with the Tech Talk for the aspect-ratio fallback behavior.

URL: https://developer.apple.com/documentation/swiftui/reservedregion

Kind: primary API record. Apple's search result describes a reserved region as an area where content splits into separate regions, such as at the fold of a hinge. Do not expand this article into a complete hinge API survey.

## 4. Apple Developer Forum: real implementation boundary

URL: https://developer.apple.com/forums/thread/848029

Kind: primary practitioner report and Apple staff answer. A developer's September 24, 2026 post uses `ArrangementView` with `.arrangementViewStyle(.overlay)` and reads `@Environment(\.overlayArrangementZIndex)`. The post reports that the Duo simulator did not return a distinct z-index while other iPhone simulators did. Apple's DTS engineer identifies it as a known bug and says the expected test is whether `zIndex > 0`, with a workaround wrapping the controls in `VStack` in the primary closure. Locator: opened page lines 19–21, code lines 23–58, and staff answer lines 65–89/110–128.

Attribution boundary: this is one report in a named simulator environment, not a prevalence measurement or proof that the API is unreliable. State the environment and keep the workaround attached to the reported bug.

## 5. Release record

URL: https://developer.apple.com/news/releases/?id=01182023e

Kind: primary release record. Apple's release page lists Xcode 27 and iOS 27.0 on September 14, 2026, with Xcode 27.1 beta on September 18 and iOS 27.2 beta on September 21. The Tech Talk and update page identify the ArrangementView API as iOS 27.1 material. Use the release page only to anchor the current release cadence; do not infer API availability from the release list alone.

## Implementation guidance

- Verify the exact closure syntax in Apple's Tech Talk or current SDK before publication. The documented shape is `ArrangementView { Primary() } secondary: { Secondary() }`.
- Use a compact player/up-next example and show `.arrangementViewStyle(.split)` first. Add `.split.axes(.horizontal)` only to explain the single-view fallback.
- Use `.splitArrangementLayoutRatio(0.3)` as a preference on the child whose size is being expressed; do not claim that it fixes a width.
- Use `@Environment(\.overlayArrangementZIndex) private var zIndex` only for overlay ordering, and explain `zIndex > 0` in the context of the Apple forum report.
- No source provides a benchmark. Do not invent measurements or call the code tested in this Linux environment.
