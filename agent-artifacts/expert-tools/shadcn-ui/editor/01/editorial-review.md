# Editorial review: expert-tools/shadcn-ui (editor/01)

## Correct

The thesis is that UI tooling should make the ownership boundary explicit: keep the visual source local, borrow difficult behavior, and inspect the resulting states in a workshop. The claims under it are conditional rather than universal: shadcn/ui is a source-distribution layer; Base UI, Radix, React Aria and Zag/Ark UI are behavior foundations with different tradeoffs; MUI, Mantine, Chakra and Catalyst optimize for breadth or speed; Storybook makes the local system inspectable.

The source links pass the repository's link check. The current-status claims about Base UI becoming shadcn/ui's default, Radix remaining supported, and React Aria being a first-class base are cited to the relevant shadcn/ui changelogs. The table separates source ownership, behavior ownership and styled-library breadth instead of pretending they are comparable products. The code listing makes the copy/edit/diff workflow concrete. Manual updates and the limits of headless accessibility are stated beside the recommendation.

The headline and dek are supported by the article's argument. Quotations are short, attributed and linked: shadcn/ui documentation, Brad Frost and Mitchell Hashimoto. No unverified social-post quotation is used.

## Reads well

The draft keeps the opening failure concrete—the component that is almost right and becomes a wrapper stack—then moves through source distribution, behavior foundations, styled starting points and the feedback loop. It does not borrow the recent Expert Tools stat-strip opening or the archive's recurring “what holds up” furniture. The comparison table carries the repeated distinctions faster than another series of library summaries would.

I cut the unsupported MUI Base aside so the MUI paragraph stays within the current source's documented claim about Material UI's breadth and customization. I also moved the Catalyst paragraph next to the other styled starting points so citations arrive in first-use order and the ownership argument reads in one place.

## The experience

The preview site rebuilt with the draft in place, and the deterministic render probe found no Chrome executable in this environment, so it skipped browser probing. The source proof still passes with `BLOCK: 0` and `WARN: 0`; the HTML contains one decision-useful comparison table, one shell listing and one verdict note. The article gives the reader a decision rule and a maintenance workflow rather than a vendor ranking.

## Edits

- Removed the unsupported MUI Base comparison from the styled-library section.
- Moved the Catalyst paragraph from the source-distribution section into the styled-starting-points section.
- Reordered citation IDs and the source list to match first appearance.
- Confirmed the stamped metadata and the link-enabled proof after the edits.

## Decision

approve
