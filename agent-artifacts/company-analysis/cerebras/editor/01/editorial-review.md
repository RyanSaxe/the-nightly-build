# Editorial review: company-analysis/cerebras (editor/01)

## Skeptic

Thesis: Cerebras's customer concentration did not ease this quarter, it
rotated. The two related-party customers that carried 88% of first-half 2025
revenue fell to 59% in first-half 2026, but a newly disclosed customer took
20-32% of the base, so the top few relationships still command 79% and the
underlying risk has moved rather than shrunk. Two supporting threads: the same
quarter carries two gross margins (GAAP 14.2%, the company's "core" 41%),
reconcilable to specific disclosed items; and the $25.4B RPO backlog is not
broken out by customer, which the piece treats as the binding limit.

The claims it stands on, tested:

1. **The rotation (central claim).** I recomputed every concentration figure
   against the owning primary. H1 2025 Customer A 47% + Customer D 41% = 88%;
   H1 2026 A 49% + D 10% = 59%; add Customer B's 20% and the three largest =
   79%, nine points below 88%. Q2 2026 A 34%, B 32%, C 10%, D <10%. Every
   figure matches the Q2 10-Q, which I opened and confirmed line by line
   (revenue $180.1M/$103.3M, gross profit $25.6M → 14.2%, the lettered table,
   the related-party sentence, the $56.8M/$74.4M OpenAI-arrangement revenue,
   $25.4B RPO, 750MW/1.25GW, warrants $822.9M/$149.4M through October 2031,
   stock comp $376.8M with the $273.6M catch-up, the $11.8M inventory charge).
   The Q1 10-Q confirms the letter reassignment the article's table caption
   flags: Q1's "Customer B" (11%) is Q2's "Customer D." The claim holds, and
   it rests entirely on the filing's own lettered figures, not on any name.

2. **The named-customer inference.** This was the round's first focus, so I
   traced every place a name appears. The thesis needs no names — it is built
   on Customers A/B/C/D, which are filing facts. Names enter only as flagged
   context: (a) the S-1/A risk factor that itself lists "OpenAI, G42, MBZUAI,
   and AWS" as significant customers (I opened it; the quote is exact), which
   the piece correctly presents as the field the four letters "most plausibly
   draw from" without mapping any name to any letter; (b) OpenAI as the named
   party to the Master Relationship Agreement and OpenAI/G42 as named warrant
   holders, both genuinely the filing's own; (c) the arithmetic inference that
   OpenAI = Customer B, quarantined in its own "What the filing does not
   confirm" note and closed with "This is an inference from the numbers, not a
   statement the filing makes"; (d) the FY2025 G42/MBZUAI split, labeled a
   secondary summary the primary does not confirm; (e) the historical G42
   83%/87%, hedged as "reported at the time as G42" from a withdrawn filing.
   No named attribution anywhere reads as the concentration table's own fact.
   The argument does not over-rest on the inference: strip every name and the
   thesis is unchanged. This focus passes.

3. **The contested margin.** GAAP 14.2% (from 31.1%) and core 41% (from 31.2%)
   both verify. The gap is tied to three dollar-specific disclosed items, each
   confirmed in the 10-Q. The piece presents both fairly — "neither is wrong on
   its own terms," GAAP "includes real, disclosed costs that core is built to
   exclude," and core "cannot make the excluded items permanent" — rather than
   leaning on whichever flatters the argument. I checked the one place the
   sourcing could have slipped: the sentence that the Q1 release "guided the
   market to expect a decline to 36-38%" is cited to the Q1 earnings release
   (s9), while the evidence record had attributed that number to a secondary
   (tradingkey). I opened s9: it states "Core gross margin in the range of 36 -
   38%" as Q2 guidance directly. The citation is correct and primary — better
   than the evidence record captured. No change needed.

4. **The backlog limit.** RPO $25.4B, timing 22%/43%/35%, 750MW committed vs
   1.25GW optional, and "a significant amount... attributable to" the OpenAI
   agreement with no per-customer figure — all confirmed, and the piece reports
   the non-disclosure as the limit it is. No earnings-call color is attributed
   anywhere; both management quotes come from the earnings release (s8), which
   I opened. This focus passes.

Sourcing: I opened all ten hrefs. Every one resolves and lands on the source
itself, including the writer-corrected Q2 earnings-release URL. Every
`data-nb-kind` is correct (s5, s7, s10 secondary; the rest primary, including
company press/earnings releases as primary for the company's own figures and
quotes). Ten cited sources against a floor of eight, all genuinely opened. No
buy, sell, or allocation call — the "Strong Buy" consensus and price target
that sit in the evidence record are deliberately absent.

One break sent to no one because I fixed it: the headline claimed Cerebras
"swaps its longtime dominant customers for a new one," which the record
contradicts. Customer A stayed the single largest (47% → 49%); only the
second-largest slot changed hands (D → B). A false label in the largest display
text. Rewritten in place to the accurate finding.

## Cut

Direct slop and edge failures, four sentences plus a heading pattern:

- Two orientation signposts. The first paragraph closed on "The comparison
  complicates the story the headline revenue number alone would suggest," a
  told-not-shown signpost the very next paragraph does by the numbers; cut. The
  section's final paragraph ("Making sense of why concentration keeps finding a
  new customer to attach itself to starts with what Cerebras actually sells")
  front-loaded an unearned claim as a transition; cut, since the next section
  stands on its own and ties back.
- Two hypothetical-reader gestures. "puts... in front of a reader at once"
  became "at once"; "A reader who wants evidence that it has genuinely
  diversified needs two things" became "Showing that it has genuinely
  diversified would take two things." Both remove the gesture the slop standard
  rules out while keeping the fact.

Heading construction was the clearest pattern. Four of six headings joined two
clauses with a comma and "and"/"or" ("What the August 10-Q changes, and what it
doesn't"; "The rotation, and the names the filing won't give it"; "$25.4
billion, and one number it won't break out"; plus the comma in H2/H4).
spec/headlines names repeated heading construction as a machine tell. I rebuilt
three into different shapes — a declarative ("The customer table complicates a
strong quarter"), a noun phrase ("The rotation the filing won't name"), and an
interrogative noun phrase ("What the $25.4 billion backlog won't break out") —
leaving the set varied.

Against the recent library (SpaceX, Palantir, and six others via `nb history`):
the required breaks hold. This piece headlines on concentration, not price;
opens on the customer table, not "the quarter the price has to justify"; runs a
concentration/margin/backlog middle, not a valuation multiple; and closes on a
risk verdict, not "where the two reads part." I steered the new headline off the
recent "[Company] did X and Y" comma-and mold (Reddit) as well.

The negative-parallelism constructions that remain are earned: "The pattern is
not more customers sharing the revenue. It is the same small number of very
large relationships" corrects a misconception the prior sentence names (2026 as
the year the base diversified), and "the risk has not shrunk, it has moved"
corrects the named claim it quotes. No borrowed phrasing from the voice-guide
exemplars; no prompt leakage — "rotation" and "the risk has moved" are the
reported finding, not lifted instructions.

## Reader

What the piece gives beyond its sources, in one sentence: a reader learns that a
74%-growth quarter hides a concentration that rotated rather than eased, why the
same quarter honestly carries a 14.2% and a 41% margin, and that the backlog's
customer make-up is the one thing the filing withholds — a synthesis no single
source states and that the raw lettered table does not hand you. The
draft-handoff's original-work claim (turning three separate evidence-record
findings into one argument, with the paired comparisons, three charts, and the
quarterly letter table as the visual evidence) survives the read. The prose sits
closer to the voice-guide exemplars than to a median summary: the reported
number lives in the sentence that makes the claim, and the concentration
mechanism ("a customer that starts as a modest order and converts to a large,
metered commitment inside a year") is walked through once, Rubinstein-style,
rather than asserted.

Charts. I inspected each `chart-N.py` and its rendered PNG. Chart 1 (Hardware
vs Cloud, Q2 2025 vs Q2 2026: 70.3/54.1, 33.0/126.0) matches the 10-Q, zero-
based axis, honest. Chart 2 (H1 share by lettered customer: A 47/49, B 0/20, D
41/10, stacking to 88 then 79) matches; omitting Customer C is correct, since C
is not in the six-month table. Chart 3 (GAAP vs core: 31.1/44.6/14.2 and
31.2/47/41) matches the 10-Qs and earnings releases, zero-based axis, and the
divergence it shows is real. All three captions are factual cited labels with
the correct source numbers. No chart correction needed.

## Edits

- Rewrote the headline from "Cerebras swaps its longtime dominant customers for
  a new one, and concentration barely falls" to "Cerebras's revenue
  concentration barely fell as its second-biggest customer changed" (accuracy:
  Customer A stayed largest; only the No. 2 slot rotated). Updated the `<title>`,
  the `nb-meta` title, and the `<h1>` identically.
- Fixed the dek's dangling "the same quarter" to "the second quarter's revenue"
  (the 88%/59% figures are half-year, not a quarter). Updated `nb-meta` dek and
  the visible dekline.
- Retitled three section headings off the repeated comma-and mold: "What the
  August 10-Q changes, and what it doesn't" → "The customer table complicates a
  strong quarter"; "The rotation, and the names the filing won't give it" → "The
  rotation the filing won't name"; "$25.4 billion, and one number it won't break
  out" → "What the $25.4 billion backlog won't break out."
- Cut the orientation signpost sentence "The comparison complicates the story
  the headline revenue number alone would suggest," and trimmed "in front of a
  reader at once" to "at once."
- Cut the orientation closing transition paragraph ("Making sense of why
  concentration keeps finding a new customer to attach itself to...").
- Reworded the garbled "750MW is the floor of what OpenAI owes Cerebras revenue
  for" to "750MW is the floor, the capacity OpenAI is contractually committed to
  buy," keeping the floor/ceiling claim intact.
- Added the missing question mark to the interrogative "...or has it just changed
  shape?"
- Removed the hypothetical-reader gesture in the verdict: "A reader who wants
  evidence that it has genuinely diversified needs two things" → "Showing that it
  has genuinely diversified would take two things."

`nb check --no-check-links` after edits: BLOCK 0, PUBLISHABLE, one warning — the
46-word W-SENTENCE-DENSITY sentence quoting the company's own three-part
definition of "core" margin verbatim, which the writer intentionally left and I
agree should stay: splitting a regulatory definition risks misstating it.

## Required work

None. Every defect was editor-fixable and is fixed in place. No evidence gap for
the researcher, no chart correction or redraft for the writer. The orchestrator
runs the final `nb stamp` and links-checked proof.

## Decision

approve — the numbers, citations, and charts are accurate against the primaries,
the named-customer inference is properly quarantined everywhere and the argument
does not depend on it, and the display-text, heading-formula, and slop defects I
found were all repaired in place.
