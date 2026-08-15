# Editorial review: tech-news/2026-08-15 (editor/01)

## Skeptic

As a brief, the piece stands on four item-level claims, one per heading, and the
lead item supplies the article headline and dek.

**Lead item — DeepSeek V4 Pro (headline/dek).** Headline claim: DeepSeek shipped
V4-Pro-0813 to general availability with zero independently verified benchmark
scores. Dek claim: the version string appeared first in DeepSeek's own price
list, with no separate announcement. Both hold. I opened the DeepSeek changelog
(s1): it announces GA and the Aug 16, 16:00 UTC pricing change with off-peak at
half peak. I opened Digital Applied (s3): it documents the price-list-first
finding and the ~32-hour window, and states plainly that no independent
reproduction of any GA figure exists. Params (1.6T total, 49B active, 1M
context, MIT) verified against Unite.AI (s2). Pricing (flat $0.87 output to peak
$3.96) verified against evidence and s2. The item's skepticism about the vendor
table is well earned and correctly attributed.

- One miscitation, fixed directly: the "roughly 32-hour window" is Digital
  Applied's forensic finding (s3), not the DeepSeek changelog's (s1); I added the
  s3 citation to that clause.
- **One break routed (fabricated quotation).** The article prints, in quotation
  marks as the source's exact words: *"None of these columns has yet been
  replicated by an independent evaluator for the 0813 build."* That sentence is
  **not on the Digital Applied page.** I fetched the page twice and pulled the
  actual wording verbatim: *"At the time of writing, no independent reproduction
  of any GA-specific figure exists — normal for a release this fresh, and still
  the single most important caveat on the table."* The evidence record's s3
  Quote field carries the same wrong wording (its Establishes field, by
  contrast, matches the page). The underlying claim is true and is already
  carried by the headline and the table caption, but a quoted sentence must be
  the source's own. I did not rewrite the quote myself: quotation accuracy is
  reporting the writer/researcher own. Routed with the verified replacement text
  supplied so nobody rewords around it.

**IBM/OpenAI item.** Every claim verified against IBM's release (s4) and
TechCrunch (s5): GPT-5.6 plus Codex and ChatGPT Work in IBM Consulting
Advantage; the "OpenAI Practice" with "thousands of consultants and engineers";
the "Elite" partner tier (exact name confirmed); the three focus areas and four
named industries; no dollar figure, headcount, or term disclosed; the July
revenue-forecast cut; the Infosys and TCS comparison. Clean.

**Gemini 3.7 Flash item — break routed (load-bearing figures uncited).** The
item's entire reason to run is the independent GDPVal-AA v2 result. The two
sentences that carry it — "scores 1,525, a 103-point gain," and "trails three
named rivals... Muse Spark 1.2 at 1,628, Claude Sonnet 5 at 1,598, GPT-5.6 Terra
at 1,578" — are cited to s7 (the Artificial Analysis model page). **Those
numbers are not on the s7 page.** I fetched it: it carries only the Intelligence
Index (56, #17/188, median 34), which does check out. The evidence record itself
says the GDPVal-AA numbers came from "a separate page (via X/Artificial
Analysis)" — a source the article never cites. So the item's headline claim
("trails three rivals") is uncited as printed. The URL resolves, but not to the
claim. Routed to the researcher for the resolvable source and confirmation of
the figures.

**Science item — both round-focus bars fail; routed.** I opened the Nature
primary (s8): the href resolves to the article (paywalled abstract). Two
problems.

1. *Primary contradicts the article's central claim.* The heading ("cuts
   platinum loading") and lead ("hold a sharply reduced platinum loading")
   assert reduction. The Nature abstract describes keeping sub-5nm ordered
   L1-zero PtCo particles *"even at high platinum loading of 40 weight percent,"*
   and phys.org (s9) is careful to say the same: dispersion is held *"even with
   the industry-preferred high platinum content,"* with overall *usage* reduced
   through efficiency, not a lower loading percentage. The primary governs; the
   "reduced/cuts loading" framing misstates it and requires a change.
2. *Dating and primary-readability.* The paper posted Aug 6, nine days before
   the 15th, while the other three items cluster Aug 12-13. The researcher never
   read the primary (gated), so the durability figures (85% after 150,000
   cycles, ~25,000 hours, sub-5nm at 1,000°C) rest only on the secondary. The
   source entry also reads "Wu et al." while the first author is Gao (Wu is
   senior author); the recorded description is not the paper's actual title
   ("Radial nanochannel-array carbon enables high-performance intermetallic fuel
   cell catalysts").

The four-item floor means this cannot simply be cut to three. It needs either a
genuine reconciliation against the primary or, better, a stronger item actually
dated on or around the 15th.

**data-nb-kind.** s1/s4/s6/s8 primary and s2/s5/s9 secondary are all correct.
s7 is labeled secondary; for its own Intelligence Index measurement Artificial
Analysis authors the claim and is primary-grade, but the live issue is the
missing GDPVal-AA source above, which the researcher should settle when supplying
the correct URL.

## Cut

No sentence-level slop of consequence. Every item ends on a fact or a figure,
not a line handing the point back to the reader — the commission's habit-to-break
is respected throughout, and the register matches the voice guide: each
self-reported number carries who measured it and the caveat the headline
dropped. Zero body sentences failed the slop test outright.

Direct edits in this pass:
- Caption: replaced a semicolon splice with a period, per the house punctuation
  default ("build; no independent" to "build. No independent").
- Gemini Intelligence Index sentence: "above the 34-point median" was a
  comparison missing its own term — the model's Index score (56) was never
  stated. I added "scores 56" (on the s7 page and in the evidence), so the 56
  vs. 34 comparison is complete rather than dangling.

One soft pattern, not blocking: two of four headings foreground an absence with a
matching preposition ("...with zero independently verified benchmark scores" /
"...without disclosing deal terms"). Each works alone; the echo is mild. If the
IBM heading is touched for other reasons, vary the construction.

Marginal: "the two scores measure different things rather than confirming or
disputing each other" uses the "X rather than Y" shape, but it corrects a real
reader assumption (that the independent index validates or contradicts Google's
numbers) and carries a reasoning step, so it stays.

No prompt leakage: headings name developments in the piece's own nouns; the
price-list dek and the non-reproduction caption are reporting, not lifted
framing.

## Reader

What the piece gives beyond its sources: the DeepSeek item's editorial refusal
to launder a vendor benchmark table (GA shipped with zero independent
reproduction, version string surfaced in a price list), and the IBM item's
pairing of a headline "Elite tier" deal with total non-disclosure of terms
against a fresh revenue-forecast cut. Both are judgments no single source hands
you. The prose sits closer to the voice-guide exemplars than to a median summary
— it consistently attaches the who-measured-it and the dropped condition to each
figure. The Gemini item earns its place only if the GDPVal-AA sourcing resolves;
the science item, as written, mostly restates phys.org and misstates the primary.

## Edits

- Item 1, table caption: changed the semicolon to a period (house punctuation).
- Item 1, first sentence: added the s3 citation to the "roughly 32-hour window"
  clause, whose source is Digital Applied, not the s1 changelog.
- Item 3, Intelligence Index sentence: added the model's own Index score ("scores
  56") so the "above the 34-point median" comparison is complete; supported by s7
  and the evidence record.

## Required work

- **researcher** — DeepSeek s3 quotation: the evidence record's s3 Quote field is
  not the source's wording. The source's verbatim sentence is: "At the time of
  writing, no independent reproduction of any GA-specific figure exists — normal
  for a release this fresh, and still the single most important caveat on the
  table." Correct the record.
- **researcher** — Gemini GDPVal-AA: supply the resolvable source that actually
  carries the 1,525 score, the +103 delta, and the three rival scores (Muse Spark
  1,628 / Claude Sonnet 5 1,598 / GPT-5.6 Terra 1,578); the cited s7 page does not
  contain them. Confirm the figures against that source. If no resolvable
  independent source exists, the item's fresh hook collapses and the item must be
  reconsidered.
- **researcher** — Science item: read the Nature primary past the gate and (a)
  reconcile the "reduced/cuts platinum loading" claim, which conflicts with the
  primary's "high platinum loading of 40 weight percent"; (b) verify the durability
  figures against the paper itself, not only phys.org; (c) correct the source entry
  (first author Gao, not Wu; actual paper title). Then decide with the writer
  whether the item survives, given it is dated Aug 6 (nine days out) — a stronger
  item dated on or around Aug 15 is the better outcome. The four-item floor bars a
  silent cut to three.
- **writer** — after the record is corrected: replace the DeepSeek direct quote
  with the verified verbatim sentence above (or cut the quote and let the caption
  carry the claim); re-cite the Gemini GDPVal-AA figures to the researcher's
  supplied source; rewrite the science item's heading and lead to match the
  primary (or replace the item); rerun the proof.

## Decision

revise — a fabricated direct quotation in the lead item, the Gemini item's
load-bearing figures cited to a page that does not carry them, and a science item
that both misstates its primary and fails the round's dating bar each block
publication until the researcher corrects the record and the writer reworks
items 3 and 4.
