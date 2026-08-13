# Draft handoff: company-analysis/cerebras (writer, round 01)

## Original work

The evidence record states the concentration-rotation reading, the GAAP/core
margin split, and the RPO disclosure gap as separate findings in prose. This
draft turns those three into one argument that answers the commission's market
question directly (has Cerebras's structural risk actually shrunk, or only
changed shape), and builds the paired H1-vs-H1 and quarter-vs-quarter
comparisons, the three charts, and the quarterly customer-letter table that let
a reader see the rotation and the margin split at a glance rather than read
them as isolated facts — synthesis and visual evidence the evidence record
itself does not construct.

## Proof result

`./nb check .nb-work/company-analysis/cerebras/library/company-analysis/cerebras.html --series company-analysis --library /home/user/library-checkout`, links checked: **BLOCK: 0**, verdict PUBLISHABLE.

One warning intentionally left:

- `W-SENTENCE-DENSITY` (46 words, 3 clause joins) on the sentence quoting
  Cerebras's own three-part definition of "core" gross margin verbatim
  (`(i) exclude non-cash stock-based compensation; (ii) exclude pass-through
  revenues...; and (iii) add back non-cash amortization from customer
  warrants...`). This is a direct quotation of the company's own regulatory
  language; splitting or trimming it risks misrepresenting the definition it
  exists to state precisely. Left as is.

All other sentence-density, em-dash (was 25, now 0), repeated-term
("mechanism," was 2, now 1), and placeholder (stat-strip labels were
accidentally left in all-caps, now sentence case) warnings from the first
`--no-check-links` pass were fixed by rewriting, not by punctuation
substitution.

One source link needed correction during the links-checked pass: the Q2 2026
earnings release URL in the evidence record
(`.../cerebras-systems-fast-inference-cloud-business-nearly-quadruples-second-quarter-2026`)
404s; the live URL for the same press release, confirmed by web search and a
200 response, drops the `-second-quarter-2026` suffix
(`.../cerebras-systems-fast-inference-cloud-business-nearly-quadruples`). Same
source and same claims as the evidence record cites; only the URL changed.

## Open questions

None blocking. Two things the editor may want to weigh:

- The piece infers that OpenAI is "Customer B" (not the largest customer) and
  that Customer A/Customer D, the related-party pair, are more plausibly
  G42/MBZUAI, from the arithmetic match between the OpenAI-arrangement dollar
  figures and Customer B's disclosed percentages. This is flagged explicitly
  in its own labeled note ("What the filing does not confirm") as an inference
  from the numbers, not a filing statement, per the brief's instruction. Worth
  a second read to confirm the hedge is load-bearing enough given how much of
  the piece's framing leans on it.
- The tradingkey.com claim that Q2 margin compression was expected due to
  Cerebras's reliance on "expensive compute from G42" as a vendor is stated
  and then explicitly dismissed as unconfirmed by the primary record, per the
  evidence record's own caution. No open question here, just flagging that
  the piece states a claim in order to knock it down, which is intentional.
