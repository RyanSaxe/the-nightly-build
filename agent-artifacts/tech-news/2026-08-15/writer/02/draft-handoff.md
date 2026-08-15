# Writer handoff: tech-news/2026-08-15 (writer/02)

## Original work

Beyond assembling the corrected record, the article now makes an editorial
judgment researcher/02 only set up: it drops the fuel-cell item the editor
flagged as both stale and primary-contradicting, and runs the AMOC
tipping-rate item instead, on the researcher's own comparison of the two
candidates' freshness and primary-readability — a selection call the evidence
record recommended but did not make for the article.

## Editorial-review items resolved

- DeepSeek quotation (lead item): replaced the fabricated sentence with the
  verbatim quote from Digital Applied — "At the time of writing, no
  independent reproduction of any GA-specific figure exists — normal for a
  release this fresh, and still the single most important caveat on the
  table." — and added the corrected locator (Section 03, "Label every
  number") to that citation.
- Gemini GDPVal-AA figures: re-cited the 1,525 score, the +103 gain, and the
  three named rival scores to the resolvable leaderboard page
  (artificialanalysis.ai/evaluations/gdpval-aa, now s7); the Intelligence
  Index page (now s8) is cited only for its own Intelligence Index figures
  (the score of 56, rank 17/188, and the 34-point median).
- Science item: replaced the platinum-loading fuel-cell item with the AMOC
  tipping-rate item (van Westen, Börner & Dijkstra, Nature Climate Change,
  Aug 13), citing the paper directly (s9) for the +4.0°C prior estimate, the
  rate-dependent +5.5°C/+2.0°C finding, and the mechanism, and Utrecht
  University's release (s10) for van Westen's quote and the 0.3°C/decade
  figure, which is flagged in the prose as absent from the paper's own
  abstract.

## Incidental fixes made while reproving

- The DeepSeek item's s2/s3 citations were swapped (Digital Applied is now
  s2, Unite.AI is now s3) to fix a W-CITE-ORDER warning the editor's own
  direct edit (adding the s3 citation to the "32-hour window" clause)
  introduced; no source content or claim changed, only which number labels
  which entry.
- Split one over-length sentence in the new AMOC item (W-SENTENCE-DENSITY) in
  two places without changing what it claims.

## Proof result

`./nb check --series tech-news .nb-work/tech-news/2026-08-15/library/tech-news/2026-08-15.html --library /home/user/library-checkout`
(links checked, after `nb stamp`): **BLOCK: 0, WARN: 0**, verdict
PUBLISHABLE. No warnings left in place.

## Open questions

None. The researcher's fallback fuel-cell record was not needed; the
recommended AMOC replacement carried the item cleanly once the acronym was
defined and one sentence was split for length.
