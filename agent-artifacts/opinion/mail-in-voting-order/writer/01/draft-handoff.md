# Draft handoff — opinion/mail-in-voting-order (writer, round 01)

## Original work

The evidence record contains three separate documents that each defend
Executive Order 14399 for a different reason and on different grounds — the
Solicitor General's application (standing/ripeness only), the intervenor
states' application (a citizenship-data/election-integrity framing), and
Judge Dunlap's partial dissent (a citizenship-verification-is-distinguishable
theory) — without any single document stating all three together, and the
evidence's own "Contradictions" section flags this as a real gap between what
the government filed and what would actually rebut the Elections-Clause
holding. The piece's original work is assembling those three into one
accurate composite counter, keeping the standing argument (the government's
actual filed position) distinct from the merits-adjacent arguments (which the
government itself does not make), and then answering each on its own terms
rather than treating "the administration says" as a single position. That
separation is visible in the counter section's structure: one paragraph for
Sauer's standing/ripeness argument, a second for the intervenor states' and
Dunlap's merits-adjacent arguments, and two rebuttal paragraphs that answer
each on the ground it was actually made on (ripeness already resolved by
Talwani's June 18 order; Dunlap's distinction not addressed to who holds the
power to compel the list in the first place).

## Files changed

- `library/opinion/mail-in-voting-order.html` — full draft. Position card +
  three flex sections (`clause-question`, `two-commands`, `scope`) + mandatory
  `counter` + `Sources`. 1,645 measured words, 8 sources (all primary,
  first-citation order 1–8), reading time 8 min.
- No chart or source asset: the evidence record found no visual asset in any
  primary document ("`None found`" across every source assets entry), so none
  was added.

## Proof result

`nb check library/opinion/mail-in-voting-order.html --series opinion --repo
/home/user/the-nightly-build` → **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE.**
No warnings intentionally left; the one sentence-density warning from an
earlier pass (44 words, 2 clause joins) was fixed by splitting the sentence
rather than left standing.

One source-URL correction made against the evidence record: evidence source 1
lists `https://www.federalregister.gov/public-inspection/2026-06601` for EO
14399, but that exact URL now 302-redirects to an `unblock.federalregister.gov`
interstitial — the same failure mode the evidence file's own Discarded section
already documents for the `www.federalregister.gov` host, which is why the
researcher used the `public-inspection.federalregister.gov` PDF instead. The
article cites the working PDF URL the evidence describes
(`https://public-inspection.federalregister.gov/2026-06601.pdf`), which
resolves and is the same FR Doc. 2026-06601 the researcher read in full — not
a new document, a corrected copy of the same citation.

## Source-count note

`min_sources` for this series is 8 (WARN-only floor, `strict: false`). The
evidence record explicitly found no eighth verifiable primary/secondary source
beyond the 7 legal documents (an academic defender of EO 14399's
constitutionality could not be sourced; see evidence's Discarded section). To
reach 8 real sources without inventing one, the piece cites the operative text
of the Elections Clause itself (U.S. Const. art. I, §4, cl. 1) as source 8,
verified directly against Cornell's Legal Information Institute in this
session (one short, targeted fetch of stable constitutional text, not a
re-read of any large document) since it is the textual anchor the whole
argument turns on and was not separately numbered in the evidence file.

## Editorial requests addressed

None — this is round 01, no prior editorial-review.md exists yet.

## Open items for the editor

- Confirm the SG application's filing date. The evidence file notes the exact
  calendar date of the SG's filing (No. 26A124) was not independently
  re-verified against the SCOTUS docket in the research pass; the article
  avoids stating a specific date for it and only dates the intervenor states'
  application (July 28, per evidence) and uses the commission's "~July 27"
  framing only in this handoff, not in the article body.
- The position card names the 23-states-plus-D.C. plaintiff coalition and
  three of its attorneys general (Bonta, James, Raoul) by name, per the 1st
  Circuit's certificate-of-service list in evidence; it does not name all 23,
  which the evidence itself does not fully enumerate.
