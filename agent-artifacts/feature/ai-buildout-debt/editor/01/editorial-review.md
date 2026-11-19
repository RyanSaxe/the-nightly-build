# Editorial review: feature/ai-buildout-debt (editor/01)

## Correct

Thesis, from the draft alone: on the Fed's Figure C, seven AI firms' undiscounted
leases yet to start and guarantees and contract commitments are about 3.5 times their
discounted debt. The Fed does not split guarantees from purchase orders. Four 10-Qs
name about $198 billion of guarantees against $768 billion of supplier orders. The
leases reach lenders through developers and SPEs, and of the three tenants tabled
only Oracle spends more than its operating cash flow. Each claim held against the
sources, with the breaks below. I reopened the November FSR (pp. 23–25), the Barr
speech, the OCC report and all five 10-Qs cited.

- Headline. "Filings show $198 billion of guarantees in Big Tech's $2 trillion of
  commitments" did not hold. "In" places the filings' guarantees inside the Fed's
  2026:Q2 bar. Nvidia signed the $105 billion SB Energy guarantee in August 2026
  (Nvidia 10-Q, Note 10, p. 19), after the Fed's quarter, and every filing is dated
  July to September. The sentence also reads as the whole of the credit support in
  the bar, although Amazon, Broadcom and Microsoft contribute nothing to the
  $198 billion. "Big Tech" was a looser label than the Fed's seven named firms.
  I rewrote the headline to state the comparison the filings support. The
  $768 billion to $198 billion ratio is 3.88, so "nearly four to one" holds.
- The same implication in the body. "Guarantees are ... under a tenth of the Fed's
  total" treated the named guarantees as all the guarantees in the bar. I narrowed
  it to the guarantees these filings name, and said the unitemized $1.1 trillion
  includes the three firms not counted and could be either kind. The Fig. 2 caption
  now says the filings postdate the Fed's 2026:Q2. The chart's two lower bars now
  read "named in three filings", and I re-rendered it with `nb chart`. This is a
  narrowing to what the record supports. The record itself says the split is
  unknown (Limits), so nothing is hidden by it.
- "Whoever finances the venture funds a campus whose tenant can leave after four
  years, and the guarantee covers that gap." Meta's 10-Q names no lender, and
  "covers that gap" mixed up a gap in tenancy with a shortfall in value. I replaced
  it with what Note 5 (p. 18) says: the residual value guarantee is given to the
  venture, and if Meta ends or does not renew the lease it pays the shortfall
  between fair value and the threshold. "Shows why the guarantee exists" claimed a
  purpose the filing does not state, so it went too.
- The serviceable view was unfair to Oracle. The draft had Meta and Microsoft
  expecting "cash flow and funds on hand" to suffice, and singled out Oracle's
  "potential access to additional financing". Meta's statement includes "financing
  activities" (p. 50) and Microsoft's includes "access to capital markets" (p. 37),
  so all three count on financing. The sentence now gives all three and cites
  Oracle p. 35. I cut Oracle's separate liquidity quotation. Oracle stays the
  counterexample on its own figures: capex over operating cash flow and the
  $19.9 billion share sale.
- Oracle's bond fair value ($105.7 billion against $125.0 billion face) went. It
  reads as a market judgment on Oracle's credit, and the filing does not say
  whether rates or spreads caused the gap (it was $114.4 billion against
  $128.1 billion in May).
- Capex definitions. Only Meta's was stated. The table caption now gives all three:
  Meta's purchases of property and equipment plus finance lease principal,
  Microsoft's additions to property and equipment, and Oracle's capital
  expenditures from its free cash flow table. The heading's "only Oracle" holds on
  those definitions.
- Locators. Oracle's $34.2 billion is in Note 6, "Unconditional Obligations", p. 13.
  The filing describes it as "unconditional purchase and certain other
  obligations", mostly component supply and data-center power. The leases are also
  Note 6, p. 13. The free cash flow table is p. 34 and the liquidity text pp. 33–35.
  Nvidia's guarantees are in Note 10, p. 19 (the draft said Note 14, which is
  leases). Meta's liquidity statement is p. 50, not p. 49. Microsoft's cash flow
  figures are on p. 6. The Barr page numbers were PDF pages. The locators now say
  "PDF p. 4 (printed p. 3)" and "PDF p. 7 (printed p. 6)", with `#page=` links.
- The lede's bar was "leases yet to start and other contract commitments", which
  left guarantees out of the bar the piece is about. It now names all three parts.
- Held, but noted. "About 31 percent" sits beside the $680 billion in the Fed's own
  sentence order (p. 23). The Fed does not say whether the share's numerator is the
  whole $680 billion, so the article follows the Fed's construction and adds
  nothing to it. The 3.5 times ratio in the subhead is the article's own division
  of chart readings. The body says the Fed prints no ratio and calls the amounts
  "not directly comparable", and it notes Barr's lower debt figure where the bar
  appears.
- Hrefs. The Fed FSR, the Barr PDF and all five SEC filings return the document.
  The OCC address serves the PDF to a browser request but bounces scripted page
  loads to the OCC homepage, as the researcher recorded. The quoted OCC passages are
  on printed pp. 1 and 3. Every `data-nb-kind="primary"` holds: each source is the
  author of the statement or figure it is cited for, and no secondary is claimed.

## Reads well

The draft was plain and close to the voice guide's register. Little needed cutting.

- Cut the lede sentence "The Fed does not separate guarantees ... from orders"
  because the new dek says the same thing. The itemized figures now carry the
  definitions in the same sentence.
- Cut "Meta's Louisiana campus shows why the guarantee exists". It was a stated
  purpose with no source behind it, built as a setup line.
- Renamed "special-purpose vehicles" to "special-purpose entities" in the heading,
  to match the Fed's term, the prose and the diagram.
- "The Fed's chart has three bars" became "three series", since Fig. 1 draws two
  bars per year.
- The new dek is a single sentence with one subject. It avoids "Set beside", "By X's
  arithmetic" and "Across". The old "On the Federal Reserve's chart" opener was the
  same attribution mould as "By X's arithmetic". The new headline avoids the
  recent "X's Y counts Z" shape, and the first section opens on the finding.

## The experience

All three visuals and the table were captured with `nb preview` and Playwright at
390 px and 1280 px, in light and dark. No page scrolls sideways. The diagram's
arrows reach their boxes and its labels do not collide in either theme. The charts
keep their white plot panel in dark mode, as `nb chart` renders them. Axis and
detail text on both charts is small at phone width but legible. Fig. 2 now labels
its lower bars as three filings each, so the short guarantees bar no longer reads
as the guarantee share of the Fed's total.

The piece gives the reader something the sources do not. It splits the Fed's
undivided "guarantees & contract commitments" bar with the companies' own notes,
which shows that most of what can be itemized is owed to suppliers. It also shows,
from Meta's filing, what a residual value guarantee on a four-year lease commits
the guarantor to. That matches the writer's original-work statement. The headline
now states that finding and nothing larger.

## Edits

- Headline (title, meta, h1) rewritten: "Supplier orders outweigh credit guarantees nearly four to one in four AI firms' filings".
- Dek rewritten as one sentence on the Fed's count and the missing split.
- Lede: "and other contract commitments" became "guarantees and contract commitments". The separate "does not separate" sentence was folded into the itemization sentence.
- Section 2: "three bars" became "three series".
- Section 3 close: narrowed to the guarantees these filings name, with the unitemized $1.1 trillion described.
- Fig. 2 caption: the filings are dated after the Fed's 2026:Q2. chart-2.py labels read "named in three filings", chart-2.png was re-rendered, and the alt text was updated.
- Section 4 heading: "vehicles" became "entities".
- Louisiana paragraph: the inferred financing sentence was replaced with the filing's RVG terms.
- Section 5: the serviceability sentence now covers Meta, Microsoft and Oracle with access to financing, and adds a citation to Oracle p. 35.
- Section 5: Oracle's fair-value clause and separate liquidity quotation were cut, and the capex paragraph tightened.
- Table caption: all three firms' capex definitions are stated.
- Locators: Oracle is Note 6, p. 13 (three places plus Unconditional Obligations twice), and the free cash flow table is p. 34 with MD&A pp. 33–34. Nvidia is Note 10 (three places). Meta's liquidity is p. 50. Microsoft's cash flow statements are p. 6. Barr's are PDF and printed pages, with `data-nb-url`.
- Re-stamped at 1,190 words, 5 minutes, 8 sources. Proof: BLOCK 0, WARN 0, PUBLISHABLE.

## Decision

approve. The headline and the one body sentence that overstated the $198 billion are now bounded to what the filings name, and nothing left for the writer needs a different argument.
