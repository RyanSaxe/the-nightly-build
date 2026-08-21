# Voice guide: grapple.nvim

## Sentence shape

Short, single-purpose sentences carrying the technical claims; longer
sentences reserved for connecting two things the reader needs held
together (a cause and its consequence, a before-and-after). No paragraph
should run more than two sentences past forty words. The draft was checked
against `nb check`'s sentence-density warning and rewritten twice where it
tripped.

## Naming discipline

- The tool is "Grapple.nvim" on first mention in the headline/dek, then
  "Grapple" throughout the body (matching the README's own usage), never
  alternating with "the plugin" as a synonym for variety — "the plugin" is
  used only in the closing section, deliberately, to step back from the
  proper noun for the summary judgment.
- "Tag," "scope," and "resolver" are each defined once, at first use, and
  then reused exactly. Never swapped for "bookmark," "marker," or
  "handler" for variety.
- Harpoon is "harpoon" (lowercase, matching its own README and common
  usage), Grapple is capitalized. Kept consistent throughout.

## What earned analysis looks like here

Every synthesis sentence in the maintenance section follows a specific
figure or dated fact already stated in the same paragraph. None of the
piece's judgments ("adopting the repository roughly as it stood in 2024")
appear before the evidence that supports them.

## Failure modes checked for directly

- Negative parallelism ("not X, it's Y"): none in the draft. Checked by
  search for "not " followed by a contrast clause.
- Vague attribution ("users report," "some say"): none. Every claim about
  usage or sentiment is either cited to a specific PR/issue number or
  dropped.
- Empty conclusions at paragraph and section edges: the last sentence of
  every section states a specific, checkable fact (a file path, a date, a
  behavior), not a mood.
- Em dash count: zero used in the final draft; every place one was drafted
  in, it got replaced by a period or comma on the second pass.
