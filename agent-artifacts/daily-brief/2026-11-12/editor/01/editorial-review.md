# Editorial review: daily-brief/2026-11-12 (editor/01)

## Correct

Thesis from the draft alone: USDA has proposed narrowing automatic SNAP
eligibility, and by its own estimate 6.3 million people would lose benefits in
FY 2029. Five shorter items sit beside it: the coining of "scofflaw", AP's call
for Colom in Mississippi, the DOJ's Fairford indictment, Google's Decisions API,
and Meta's e-means.

Headline, the round's focus. The rule (91 FR 72459, read in the govinfo PDF of
record) says 16.9% of households, 17.6% of participants, "would no longer
receive SNAP benefits because their income or resources exceed the Federal
statutory limits", or "3.2 million households containing 6.3 million
individuals in FY 2029, the first year the proposed rule is expected to reach
its full effects." "USDA proposes cutting 6.3 million people from SNAP" dropped
both the period and the fact that the figure is USDA's own estimate of the
effect. The rule proposes an eligibility change, not a headcount. Rewritten as
"USDA estimates its SNAP proposal would end benefits for 6.3 million people in
FY 2029". The rule says "in FY 2029", not "by", and the body already said so
correctly. $44.649 billion over the five-year period FY 2027 to FY 2031, the
1.78 million children, the roughly 97% and the 28,000 all match pp. 72459 to
72460. The 10 December comment date matches the DATES line and the FR API.

Breaks and fixes:
- SNAP: "now open to households getting any TANF-funded benefit" overstated the
  current rule. The Summary says TANF benefits include "cash assistance and
  non-cash or in-kind benefits or services from TANF-funded programs", and the
  current regulations set funding-share conditions on some of those programs.
  Changed to "TANF-funded cash or non-cash benefits".
- SNAP: the body gave the 6.3 million without USDA's stated reason. Added the
  rule's own clause, that their income or resources exceed federal limits, so
  the department's case is stated in its own terms. To stay under the length
  limit, the body's spending clause came out. The dek still carries
  $44.649 billion over five years.
- Mississippi: "after counting" made AP the counter. PBS/AP says local election
  officials processed the absentee and affidavit ballots. Changed to "after
  officials counted". AP's 49.2% to 48.7% matches Yahoo. Reconstruction (PBS/AP)
  and 1982 (NBC) are each attributed to the right outlet. NBC states the
  55-seat count and Alaska.
- Indictment: the release says "terrorism-related offenses". Changed from
  "terrorism offenses". It says UK "law enforcement authorities" arrested the
  occupants, so "police" became "authorities". The body called it "the British
  base" without ever naming it, which left the reference dangling for a reader
  who skipped the heading. It now reads "RAF Fairford, a British base housing US
  forces". The rest matches the release: nearly 20 attacks, 18 claimed by HAYI,
  vans with fuel barrels on 26 September, arrests early on 27 September. No
  custody status is given.
- Gemini and e-means: every figure matches the Google post and the arXiv
  abstract. The arXiv HTML confirms the FAIR at Meta and École des Ponts
  affiliations. The project page shows the `faiss.contrib.e_means` import.
  Nothing broke.
- Word: King, the $200, 15 January 1924, 25,000 words from 6,234 people, Dale
  and Butler, the mock entry and the second contest all match the Crimson.
  Merriam-Webster supplies the definition, the pronunciation and "wealthy
  Massachusetts Prohibitionist". Yahoo's own aside, "first Black senator since
  1989", is not used, and the article cites Yahoo only for the percentages.

Hrefs: I opened all ten in Chromium. Nine land on their documents. The Federal
Register href redirects automated clients from this network to
unblock.federalregister.gov, a CAPTCHA page. The FR API confirms that the
printed URL is the document's canonical `html_url`, and the same text is in the
govinfo PDF. The block is a gate for bots. A human click lands on the document,
so the href stays as printed.

Kinds: s2, The Harvard Crimson, was marked primary. The Crimson reports the
judges' announcement from outside the contest and has no stake in it. Under the
authorship-and-stake test it is secondary, and I changed it. The word item now
honestly rests on two secondaries, because the judges' own announcement could
not be opened. s4 (PBS/AP), s5 (Yahoo) and s6 (NBC) are correctly secondary.
s3, s7, s8, s9 and s10 own their claims. s10 has the same authors as s9, so it
is not an independent second source, and the article does not present it as
one.

## Reads well

Nothing had to go as filler. Each item opens on the event in its own nouns.
"Categorical eligibility" was jargon used beside "automatic eligibility" for the
same idea, so the item now uses "automatic" throughout, matching the heading and
the dek. The e-means item never said what e-means replaces, so "Lloyd
iterations" became "Lloyd's k-means iterations". "The department estimates"
came off the end of the dek, because the headline now names USDA as the owner.
The word item closes on King's second contest, which is a fact about the record
and not a dating correction. No opener, heading or dek repeats a recent
pattern. The dek does not lead with a name and has no attributing relative
clause. The new headline does not share its shape with the lead item's heading.

## The experience

I checked the preview at 390 px, light and dark, and at 1280 px. There is no
horizontal scroll and every component is template furniture. No visual was
added, because a 700-word, six-item brief has no room for one. The piece's own
work is to set USDA's 6.3 million beside USDA's own finding that about 97% of
the children losing automatic free meals still qualify on income. It also gives
each estimate to its owner. That holds up against the handoff's sentence.

## Edits

- Headline (h1 and nb-meta title) → "USDA estimates its SNAP proposal would end benefits for 6.3 million people in FY 2029" (non-breaking space before 2029 in the h1)
- Dek: removed ", the department estimates"
- SNAP s1: "categorical eligibility for SNAP" → "automatic SNAP eligibility"; "any TANF-funded benefit" → "TANF-funded cash or non-cash benefits"
- SNAP s2: replaced the $44.649 billion spending clause with "because their income or resources exceed federal limits"
- Mississippi s1: "after counting" → "after officials counted"
- Indictment s1: "terrorism offenses" → "terrorism-related offenses"
- Indictment s3: "toward the British base in September while US forces were stationed there" → "toward RAF Fairford, a British base housing US forces, in September"; "UK police" → "UK authorities"
- e-means s1: "Lloyd iterations" → "Lloyd’s k-means iterations"
- Source s2 (Crimson): data-nb-kind primary → secondary
- Restamped: 694 words, 10 sources, 3 min

## Decision

approve: every number, period and owner now matches the document that holds it,
and the proof passes at 694 words.
