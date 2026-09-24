# Writer handoff

## Original work

The article turns Apple’s API record into an adoption test: first identify a
primary/secondary relationship, then test the selected geometry and ratio
preference across split, overlay, axis fallback, and reserved-region states,
and finally bound the decision with the reported Duo simulator bug.

## Thesis

`ArrangementView` is a good fit for a meaningful primary/secondary relationship
whose placement should respond to aspect ratio or a reserved division region.
Its split and overlay styles express different visibility relationships, and
its ratio modifier is a preference rather than a fixed width. That makes it a
useful system container for this narrow problem, not a universal replacement
for stacks, custom `Layout`, or grids.

## Section outline

1. **ArrangementView turns geometry into a two-view decision** — define an
   arrangement as inputs-to-placement, establish iOS 27.1 availability, and
   set the primary/secondary boundary.
2. **The primary and secondary closures carry the design** — show the exact
   `ArrangementView` initializer and explicit split style with a player and Up
   Next panel.
3. **Split keeps both views visible; overlay gives one view the foreground** —
   show horizontal-axis restriction and the documented single-view fallback,
   then contrast overlay semantics and `overlayArrangementZIndex`.
4. **The ratio asks for a proportion, then yields to geometry** — show
   `splitArrangementLayoutRatio(0.3)` as a preference and derive a test matrix
   from aspect ratio and reserved regions.
5. **Test the fold before choosing the abstraction** — report the bounded Duo
   simulator issue and `VStack` workaround, then close with the adoption rule
   for `ArrangementView`, stacks, custom `Layout`, and grids.

The HTML uses four named flex sections after the orientation section. The ratio
discussion is a separate flex section so the final section can carry the
testing boundary and conclusion.

## Source use

- **1 — Apple Tech Talk:** arrangement inputs and outputs, iOS 27.1
  availability, initializer shape, split axis behavior, overlay behavior,
  z-index semantics, navigation/scrolling boundaries, and Apple’s choice
  guidance.
- **2 — Apple SwiftUI updates:** dates the ArrangementView API family to the
  September 2026 SwiftUI update.
- **3 — Apple ArrangementView documentation:** supports the container’s
  primary/secondary API identity.
- **4 — Apple split style documentation:** supports the split style reference
  used with the Tech Talk’s axis behavior.
- **5 — Apple overlay style documentation:** supports the overlay style link
  and its separate placement semantics.
- **6 — Apple `splitArrangementLayoutRatio(_:)` documentation:** supports the
  preferred-ratio wording and the `0.3` modifier listing.
- **7 — Apple ReservedRegion documentation:** supports the reserved-region
  terminology used for hinge/division geometry.
- **8 — Apple `overlayArrangementZIndex` documentation:** supports the
  environment value and its use in the overlay listing.
- **9 — Apple Developer Forums:** one dated Duo simulator report, Apple’s
  known-bug diagnosis, the `zIndex > 0` condition, and the scoped `VStack`
  workaround. It is marked secondary and is not generalized into a framework-
  wide reliability claim.

All source links are in first-citation order. The article contains no direct
source quotations; quote count: **0**. API names and Swift literals are kept in
code formatting or code listings rather than reconstructed as quotations.

## Metadata decisions

- Title: `SwiftUI’s ArrangementView Adapts Two Views Around Device Geometry`.
- Series/slug: `technical` / `swiftui-arrangement-view`.
- Date: `2026-09-24`, the selected duty date.
- Template: `article`; mode: `open`.
- Source count: `9`.
- Draft metadata estimate: `1510` words and `8` minutes. `nb stamp` was not run
  by assignment.
- Harness/model: `Codex Work Mode` / `GPT-5`.
- Production directive: writer `model: capable`, `effort: medium`; the
  orchestrator policy records researcher `capable/high` and editor
  `inherit/high`.

## Unresolved risks and handoff notes

- `nb stamp` and `nb check` were intentionally not run, so the displayed word
  count and reading time remain the writer’s metadata estimate and the HTML has
  not received deterministic proof.
- The snippets are illustrative integration shapes. `PlayerView`, `UpNextView`,
  `UpNextList`, `Controls`, and `DetailView` are app-owned views; no benchmark
  or compile result is claimed.
- The Apple documentation pages for the new APIs are JavaScript-backed in the
  retrieval surface. The Apple Tech Talk transcript and the linked API records
  were used for the exact spellings and behavior; the article keeps claims
  within those records.
- The workspace supplied a writing-coach brief but no separate `voice-guide.md`.
  The draft follows the brief, editorial direction, and slop/headline rules.
- The forum workaround is deliberately scoped to the reported Duo simulator
  environment and must be validated against the target SDK, simulator version,
  and hardware during editorial proof.
