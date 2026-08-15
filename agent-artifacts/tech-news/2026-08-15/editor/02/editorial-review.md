# Editorial review: tech-news/2026-08-15 (editor/02)

Confirmation read after the three-finding repair (researcher/02 + writer/02). I
did not reopen the four items editor/01 cleared or the settled sub-points; I
verified the three routed fixes, checked that nothing regressed around them,
confirmed the citation-order swap, and confirmed the replacement science item
clears the two bars round one set. Every changed citation was opened as the
article prints it.

## Skeptic

**DeepSeek quotation (was a fabricated quote, routed to researcher/writer).**
Resolved. The article now prints, in quotation marks: "At the time of writing,
no independent reproduction of any GA-specific figure exists — normal for a
release this fresh, and still the single most important caveat on the table." I
fetched the Digital Applied page fresh: the sentence appears verbatim, word for
word. The added locator is accurate — the page has an "03 — Benchmarks" section
with a "Label every number" subsection, and the page confirms both the
price-list-first finding and the ~32-hour Wayback-bounded window (Aug 12 03:00
UTC to Aug 13 11:10 UTC). The quote is the source's own words now, correctly
attributed and located. Fix holds.

**Gemini GDPVal-AA figures (were cited to a page that did not carry them).**
Resolved. The 1,525 score, the +103 gain, and the three rival scores are now
cited to s7, the GDPVal-AA v2 leaderboard. I opened it: Gemini 3.7 Flash (high)
1,525 (rank 24), Gemini 3.6 Flash (high) 1,422 (rank 36, so +103 is exact),
Muse Spark 1.2 1,628, Claude Sonnet 5 1,598, GPT-5.6 Terra 1,578 — all five
match the printed figures exactly. I also opened the Intelligence Index model
page (now s8): it carries the 56 / #17 of 188 / median 34 that the article
cites it for, and it does not carry the GDPVal-AA numbers — confirming the split
is correct and the leaderboard page is the right owner. Both pages land. Fix
holds.

**Science item — replacement (AMOC tipping-rate paper).** The fuel-cell item
that misstated its primary and failed the dating bar is gone; the AMOC item runs
in its place. Both round-one bars clear:

1. *Fresh and consequential.* Published Aug 13, inside the same cluster as three
   other items (not nine days out). It overturns a specific, widely cited number
   — the "+4.0°C fixed collapse threshold" — by showing the threshold concept
   itself does not hold: the same model stays stable past +5.5°C under slow
   forcing and collapses at +2°C under fast forcing. That is a change in
   understanding of a live tipping-point question, not an incremental update.
2. *Primary resolves.* The s9 href is the paper's canonical Nature Climate
   Change URL. It 303-redirects to Nature's own login IDP for the full text —
   the standard paywall, not a broken or wrong-target link — and Crossref on the
   DOI confirms the href points to the right paper: title "Failure to track a
   stable AMOC state under rapid climate change," authors van Westen, Börner,
   Dijkstra, published 2026-08-13. The researcher read the abstract directly
   this session, and every load-bearing claim in the item (the +4.0°C prior
   estimate and 1.4-8°C range, the +5.5°C/+2.0°C rate-dependent result, the
   0.5 ppm/yr ramp, the adjustment mechanism) traces to that abstract.

The one figure absent from the abstract — the 0.3°C/decade critical warming
rate — is correctly handled: it is attributed to Utrecht's own release (s10, a
phys.org-hosted Utrecht press release, byline Rosa van den Dool, "Provided by
Utrecht University," confirmed on fetch) and the prose flags it explicitly as
"the figure does not appear in the paper's own public abstract." The van Westen
quote ("not necessarily a fixed temperature... depends on how fast the climate
is changing") is on the s10 release verbatim. Display text checks: the heading's
"2°C to 5.5°C" swing and the dek-level framing match the abstract's own numbers
and direction. Item clears the bar.

**Citation-order swap (s2/s3).** Correct. Digital Applied is now s2 and Unite.AI
s3, so the DeepSeek item's first citation of the forensic source (the ~32-hour
window and price-list finding, s1+s2) precedes the model-card spec citation
(Unite.AI, s3) in reading order — ascending, which is what clears the
W-CITE-ORDER warning my editor/01 edit had introduced. No claim or source
content moved, only the labels. Every s2/s3 reference in the body now points at
the intended source: the window/price-list/quote clauses and the caption cite
Digital Applied (s2); the parameter and license figures cite Unite.AI (s3). Both
remain data-nb-kind secondary, correct.

**Prior direct edits still stand.** The caption reads "...for the V4-Pro-0813
build. No independent evaluator has reproduced any of them." (period, not the
semicolon splice). The Gemini Intelligence Index sentence carries "the model
scores 56, ranking 17th of the 188 models... above the 34-point median" — the
comparison term I added is intact. Both survived the writer's rework.

No regression around the changed items, and the four items editor/01 cleared
(the IBM/OpenAI verifications, and the untouched Apple/Alibaba, GPT-5.6-Cyber,
Muse Glimmer records carried forward) were not disturbed.

## Cut

No new slop pass — this is a confirmation read, not a fresh full review. I read
the two rewritten items (DeepSeek closing paragraph, the whole AMOC item) for
regressions only. The AMOC item ends on a fact (the 0.3°C/decade pace with its
explicit abstract-absence caveat), not a hand-back to the reader, matching the
commission's habit-to-break and the register of the cleared items. The writer's
noted sentence-split in the AMOC item reads clean and changes no claim. No new
sentence failed the slop test; no edit needed.

## Reader

The replacement strengthens the piece rather than merely patching it: the AMOC
item gives the reader a judgment the sources alone do not hand over — that a
single widely quoted tipping "threshold" is the wrong frame, because rate, not
peak, governs — with the one institution-glossed figure honestly fenced off. The
lead item's editorial refusal to launder an unreproduced vendor table now rests
on the source's actual words. The prose still sits closer to the voice-guide
exemplars than a median summary: each self-reported number keeps its
who-measured-it and its dropped caveat.

## Edits

- None. This round required no direct edits; the three fixes and the swap all
  hold as delivered.

## Required work

- None blocking. All three routed items are resolved with primary/owner-page
  evidence I opened this session, the citation-order swap is correct, and the
  writer's proof reports BLOCK 0 / WARN 0, PUBLISHABLE.

## Decision

approve — the fabricated DeepSeek quote is now the source's verbatim sentence
with a correct locator, the Gemini GDPVal-AA figures are cited to the leaderboard
page that carries them (all five confirmed exact), and the AMOC replacement
clears both round-one bars (fresh, consequential, primary resolves) with its one
abstract-absent figure correctly flagged and attributed; the swap and my prior
edits stand and nothing regressed.
