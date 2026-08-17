# Editorial review: expert-tools/beartype (editor/01)

## Skeptic

Thesis: beartype enforces a function's type hints at the call boundary by
generating a wrapper at decoration time that checks one randomly chosen item per
container level, which buys near-constant-time cost at the price of false
negatives, and its distinctiveness sits in that random-only sampling (the
full-walk mode is unimplemented) plus a zero-dependency code-generation design,
not in "sampling" as such.

The claims it stands on, tested against the primaries by opening every printed
href:

- **beartype checks one randomly selected item per nested level; O(1) is
  independence from container width, not zero cost, and not depth-independence.**
  Held. The FAQ (s5) carries "one-way random tree walk over the expected nested
  structure of those objects at call time" verbatim, and api_decor (s6) carries
  the O1 docstring "type-checking a single randomly selected item of each
  container." The article correctly separates width-independence from the real
  per-call wrapper and from depth cost.

- **Sampling is the only implemented container mode; On and Ologn are declared
  but unimplemented.** Held. api_decor (s6) marks both On and Ologn "This
  strategy is currently unimplemented." This is the load-bearing differentiator
  versus typeguard, and the article rests the angle there rather than on
  "samples instead of walks." This satisfies the round's focus: the piece does
  not overclaim "samples instead of walks," and it says plainly that typeguard
  also samples.

- **typeguard also samples by default (first item), keeps ALL_ITEMS, and rewrites
  the AST.** Held on substance, but the citation was wrong. The userguide (s7)
  supports ALL_ITEMS, the AST rewrite, and the innermost-decorator warning, but
  it does NOT state the first-item default or "since version 3." Those live in
  typeguard's changelog (versionhistory: 3.0.0, 2023-03-15, "check the first
  item by default"), which the evidence record recorded but the article did not
  print. Fixed: added s14 (typeguard version history) and pointed the first-item
  and "since version 3" claims at it, in the prose sentence and the comparison
  table caption.

- **The overhead figure is beartype's own unreplicated benchmark.** Held, and
  handled honestly. The FAQ (s5) frames "around 1µs" as the project's own
  measurement; the article prints it as "a number the project measured on
  itself, with no independent reproduction I could find. Read it as beartype's
  claim about beartype." This is the only overhead figure in the piece, and it
  is attributed as required. The typeguard "107 minutes" figure was omitted
  (see Reader for the decision).

- **Zero install/runtime dependencies; decoration-time code generation.** Held.
  eli5 (s2) carries "Beartype has no install-time or runtime dependencies" and
  the memoization/dynamic-code-generation cost model. The article quotes the
  dependency line exactly and does not overstate it into "zero dependencies of
  any kind" (the README notes test-time and doc-time deps, which the article's
  supply-chain claim correctly sidesteps by scoping to adoption).

- **Trust facts.** Held. PyPI (s11) confirms 0.22.9, 2025-12-13, requires-python
  >=3.10, MIT, author Cecil Curry. Releases (s12) confirm 0.23.0rc0 as a
  pre-release and the "one million @beartype downloads a day" milestone phrasing,
  which the article attributes as self-reported. Issues (s13) show 108 open,
  clustered on advanced-hint and edge cases. codemain.py (s4) resolves and
  imports getrandbits with ARG_NAME_GETRANDBITS, supporting the random-index
  claim.

Display text checked descriptor by descriptor. Headline "beartype type-checks a
whole list by reading one random item of it" is the true O1 behavior for a flat
list and is defended in the body. The dek describes the reliably-caught case (a
list uniformly of the wrong type slips past mypy, trips beartype, names the
item), not the false-negative case, which is the honest choice. Every subhead is
an argument step in the piece's own nouns; none is a scaffolding slot. All
fourteen sources carry data-nb-kind="primary" and each is genuinely primary for
what it owns (typeguard/pydantic docs are primary for their own tools).

Citations opened and resolved. One redirect: s8 (pydantic) 301-redirects from
docs.pydantic.dev to pydantic.dev/docs; a browser follows it transparently to
the owning page, which carries the quoted coercion sentence, so it lands on the
source itself. The evidence record already notes this redirect. Acceptable, not
routed.

Fig 1's illustrative traceback matches beartype's current message shape (class,
function, parameter and value, hint, offending item by index and value); its
wording differs from the older README example ("@beartyped ... not str") but the
caption claims only that it "follows the shape beartype documents," which the
shape does. Fig 2 shows no output at all, only comments describing the
documented false negative. Neither reads as a captured run, and the honesty
requirement of the round's focus is met.

## Cut

Four sentences failed the slop or punctuation test and were fixed in place; one
recurring habit named.

- **Signpost opener** in the random-walk section: "Here is the part that makes
  leaving the decorator on affordable." A "Here is the part that..." frame that
  announces the benefit the heading already states and the paragraph then earns.
  Deleted; the section now opens on the mechanism.

- **Method signpost** in the alternatives section: "The clearest way to see the
  difference is to hand each one the same annotation and the same wrong value."
  This narrated the method the table's own caption already states. Cut. The
  paragraph's first sentence also read "Three runtime tools invite comparison
  with beartype," which placed beartype outside its own trio; rewritten to name
  the three tools and the axis the table compares them on.

- **Imprecise count:** "typeguard is the closest of the three" implied beartype
  compared itself; changed to "closest to beartype."

- **Reflex semicolon** joining two independent clauses in the trust section
  ("...downloads a day; treat the exact figure..."). The editorial direction
  defaults to the period; changed to a period.

The recurring temptation across the draft's edges is the benefit-announcing
opener that the following sentences then earn. The voice guide wants benefit
stated first, so this is a near-miss rather than a fault; the fix is to let the
heading carry the frame and open the paragraph on the fact.

No prompt leakage: the article does not echo the commission's or brief's framing
("distinctive claim," "where the guarantee thins"). No borrowed phrasing from the
voice-guide exemplars. First person appears once ("no independent reproduction I
could find"), which the voice guide explicitly sanctions and which does honest
epistemic work rather than narrating the piece. The FAQ blockquote omits a
leading "Sadly," and a trailing definitional parenthetical; both are faithful
excerpting that does not alter the admission, so left as is. Furniture earns its
place: two code listings, one comparison table, a self-documented-limitation
note, and a verdict, none decorative. The PEP-coverage thinning is handled in one
prose sentence rather than a second table, which is right given the piece already
carries one table.

## Reader

Read straight through as the paper's declared ML engineer: what I have that the
sources alone would not give me is a single cost-benefit ruling on where to leave
beartype on (values crossing from untyped into typed code), what to trust it for
(a uniformly-wrong container, caught every call) and not (a lone bad item in a
large one), how it sits against typeguard and pydantic on one worked value, and
what would raise the verdict (implementing On, or a second maintainer). The
sources hold these facts scattered; the article is the synthesis. The
original-work statement claims exactly this pairing of each capability with the
limit the project documents against itself, and the article delivers it. Both
answers survive, so the piece is not a restatement of its sources.

On the writer's two flagged decisions:

- **Omitting the "typeguard 107 minutes" figure is correct, and no attributed
  version is owed.** It is beartype's own pathological-case benchmark of a
  competitor's opt-in exhaustive walk. Since the article's honest finding is that
  the two tools' per-call cost is similar by default (both sample one item), a
  107-minute figure would describe typeguard's non-default ALL_ITEMS mode and
  would misrepresent the comparison the piece actually makes. The cost beartype
  avoids is already shown, un-self-servingly, by the width-independence point (a
  list of ten and a list of ten million cost the same check).

- **The illustrative listings are honest.** Fig 1's traceback matches beartype's
  documented violation shape and is captioned as such, not as a captured run;
  Fig 2 shows only descriptive comments about the documented false negative. The
  round's honesty test is met.

The prose sits closer to the voice-guide exemplars than to a median summary:
mechanism explained in order (Leach), benefit stated then earned (Wayne),
limitation named as a flat finding (Willison/Wayne), and appreciation carried by
the attributed figures rather than graded over them.

## Edits

- Added source s14 (typeguard documentation, Version history) to the sources list.
- Cited the typeguard "first item by default / since version 3" claim to s14 in the alternatives prose sentence.
- Added s14 to the comparison-table caption citation (covers the typeguard first-item row).
- Added s7 to the verdict's "typeguard's ALL_ITEMS can" clause, which had cited only s6 (a beartype-only source).
- Deleted the signpost opener "Here is the part that makes leaving the decorator on affordable." in the random-walk section.
- Replaced the alternatives lead-in (method signpost plus the "three runtime tools invite comparison with beartype" miscount) with a single sentence naming beartype, typeguard, and pydantic and the axis the table compares.
- Changed "typeguard is the closest of the three" to "the closest to beartype."
- Changed the reflex semicolon in the trust section to a period ("...downloads a day. Treat the exact figure...").

## Required work

- **orchestrator:** re-stamp before the PR. The added source makes the true count
  14, but nb-meta still reads `"sources": 13`; `nb stamp` recomputes it. This is
  the routine post-edit stamp, listed so the count is not shipped stale.
- **writer:** re-run the link-included proof (`./nb check ... --series
  expert-tools --library <checkout>`) after the citation additions, to confirm
  s14 (typeguard versionhistory) passes the link check. No reporting, redraft,
  asset, or chart work is owed; the two illustrative listings and the omitted
  competitor benchmark are approved as they stand.
- **researcher:** none.

## Decision

approve — the argument holds on the primaries, the distinctiveness and overhead
attributions are exactly right, and the two miscitations were fixable in place
from sources already in the record; the only remaining items are the routine
re-stamp and link re-proof any edit triggers.
