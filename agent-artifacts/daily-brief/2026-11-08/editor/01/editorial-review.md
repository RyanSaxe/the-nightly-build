# Editorial review: daily-brief/2026-11-08 (editor/01)

## Correct

Thesis, from the draft alone: the CDC's 2026 measles count (5,182 as of 5 November) is the highest since 1991. Under it sit five items, each a claim set beside the document that owns it: Trump's 7 November order to the Justice Department and Slotkin's quoted words; Trump's account of "minor strikes" with no Central Command statement; DeepMind's leading-order 1/58 and 30x with the paper's "no fan factory has been implemented"; libghostty-vt 1.0's stable C ABI and JetBrains' adoption; and the word card on ultracrepidarian.

I reopened every source at the printed href (curl for status, WebFetch where curl got 403 from CDC and UPI, the PDF and Gutenberg text downloaded and grepped).

- Measles. The CDC page gives 5,182 as of 5 November, 4,993 of 5,182 (96%) outbreak-associated, 4 deaths, 2,289 for 2025, updated 6 November. It carries no 1991 comparison. The MMWR gives 9,643 for 1991. Break: the draft wrote "AFP reports that the CDC calls this its highest count since 1991" and attributed the eight state deaths to AFP. The Euronews page is bylined Nela Heidner and has no AFP credit for its text. AFP appears only as the outlet a pediatrician spoke to. Its sentence is that the figure "represents the highest number reported by the CDC since 1991", which is Euronews's characterization, not a CDC statement. Fix: both claims now attributed to Euronews, worded as Euronews worded them, and the source label changed from "Euronews with AFP" to "Euronews". Second break: the 4,993 and the four deaths sat under the Euronews citation. They are CDC figures, and I moved them to source 6. The headline's "most since 1991" stands on Euronews plus the CDC's own 1991 and 2025 figures. I kept it because the commission chose it and nothing I opened contradicts it.
- Trump post. Every quoted phrase matches the trumpstruth.org archive copy (status 117576401180733840, 12:45 PM EST, 7 November). The heading "look into Democrats' threats" adopted Trump's characterization as fact. It now reads "letters he calls threats". The Fox quote and its 13 October date match the Fox page.
- Iran. Break: the draft spliced "We do minor strikes, but they knock out" onto "a little bit of an anti-aircraft device", which makes "knock out" take an object Trump did not give it. UPI's text is "We do minor strikes, but they knock out. They built a little bit of an anti-aircraft device, and we knocked it out in about 15 minutes, maybe five." I now quote "We do minor strikes" and the whole second sentence. "UPI reports no US Central Command statement" claimed UPI reported an absence. UPI only prints none on the strike (its one CENTCOM mention is a bounty post), so it now reads "UPI quotes no US Central Command statement." The CBS entry confirms Thursday 5 November for the decision remark. Qeshm stays Iranian-reported, per the commission.
- DeepMind. The abstract confirms 5 November, 1/58 of an NFS run, 30 times less than MNFS, "since 1993", and the 2048-bit sentence. The "Open questions" section confirms "no fan factory has been implemented". Break in the heading: "30 times lower cost for each further 1024-bit RSA key" dropped the comparator and the precomputation. The heading now says what the paper estimates (a lower cost for factoring 1024-bit integers in bulk) and the body names MNFS as Coppersmith's 1993 method, which the paper's reference list dates.
- libghostty. The post (6 November) and the JetBrains post ("Starting with 2026.3 ... now runs on libghostty") match.
- Word card. Dictionary.com confirms the pronunciation, parts of speech and "ultrā crepidam". Hazlitt's sentence is on p. 368 of the Waller and Glover volume. Note 368 sits in the notes after the p. 457 anchor. Pliny 35.85 matches the Latin. The DNB confirms the apprenticeship. Break: "the earliest printed use found" had no finder and claimed a priority the record does not establish. I cut it, since the record establishes only that the 1819 letter is a printed use. Second break: "credited the phrase to 'a friend of mine,' 'perhaps Lamb.'" put the editors' guess in Hunt's mouth. It now says the editors guess "perhaps Lamb". Hazlitt is still not credited as coiner.
- Hrefs. Every printed href returns 200 except CDC (both) and UPI, which return 403 to curl and serve the page to a fetch tool (gated, not dead). Sources 2 and 3 printed the Gutenberg catalogue page, which does not land on the text. Both now point at the edition's HTML text with page anchors (#Page_368 and #Page_457), the same edition and the same passages.
- `data-nb-kind`. All fifteen hold. The Hazlitt letter and the editors' note share one Gutenberg volume but have different authors, so primary and secondary is correct. The archive copy of the post carries Trump's text, and primary is right for what it is cited for.

I asked the orchestrator nothing. No disagreement between the record and an opened source needed a fact changed. The AFP-to-Euronews correction follows the source as printed, and the evidence record already calls the item "Euronews with AFP" without quoting an AFP credit.

## Reads well

What went:
- "is the earliest printed use found" went because it came from the research process ("found"), not from a document.
- "It says ... It says" in the Trump item went. The first "It" had no antecedent after a sentence whose subject was Trump.
- "The CDC's report on 1992 put 1991 at 9,643 cases, and its page gives 2,289 for 2025" was two sources' bookkeeping read aloud. The figures now sit in the clause they support.
- The impeachment clause in the Trump item went for length. The letters are what the order names as "this criminal act".
- "in the Suza area of" and "a new round of" went for length.

What I lifted:
- The word card was told as a sequence of citations ending on the Pliny anecdote, which explained the pun last. It now runs in the order its record supports: the Latin, Pliny's shoemaker (with the detail that he moved from the sandal to the leg, which is the point of the proverb), Hazlitt's 1819 use against a former shoemaker's apprentice, then the unresolved coiner. That also breaks the recent "X coined it in YEAR, in WORK" mold.
- The measles heading repeated the body's numbers as a sentence fragment. It now states the comparison: more than double 2025's.
- The dek's "where state agencies report" became "against at least eight reported by state health authorities", the source's own noun. The dek is not built as ", and" plus an attribution, so it does not repeat the recent record.

The Trump and Iran items run four sentences, against the series' two or three. Each sentence carries a separate fact or caveat, and at 698 words nothing can be added to fold them together, so I left them.

## The experience

The page renders cleanly at phone and desktop width in both themes with 0px overflow. On desktop the headword broke mid-syllable ("ultracrepid / arian"). Soft hyphens now break it as "ultracrep- / idarian", and on a phone it fits on one line. No chart or asset would show anything faster in a six-item brief, so I added none.

Beyond its sources: the brief sets each claim against the document that owns it. The CDC's count goes against its own 1991 figure and the gap between its death tally and the states'. Trump's paraphrase of Slotkin goes against her quoted words, and his strike remarks against the missing Central Command statement. DeepMind's 30x goes against its own "not implemented". The word card connects a Latin proverb, a pamphlet insult and Gifford's apprenticeship that no single source connects. That matches the handoff's original-work sentence. The headline is the brief's largest claim, and it holds on the CDC, MMWR and Euronews.

## Edits

- Word card prose rewritten in record order (Latin, Pliny, Hazlitt, Hunt via the editors). "Earliest printed use found" cut. "Perhaps Lamb" attributed to the editors.
- Headword given soft hyphens (ultra&shy;crep&shy;idarian) for the desktop break.
- Measles heading changed to "2026's measles count is already more than double 2025's".
- Measles body: "highest since 1991" and "at least eight" attributed to Euronews, not AFP. The 4,993/96 percent and four deaths cited to the CDC (s6). The 1991 figure folded into the comparison sentence.
- Dek reworded: "against at least eight reported by state health authorities" (meta dek matched).
- Trump heading changed to "...look into letters he calls threats". Body recast so the post is the subject, impeachment clause cut, "of Michigan" cut, Fox sentence shortened.
- Iran: the spliced quotation replaced with UPI's full sentence. Day and occasion added (Friday 6 November). "UPI reports no ... statement" changed to "UPI quotes no ... statement". "In the Suza area of" cut. The CBS sentence shortened to "On Thursday".
- DeepMind heading changed to "DeepMind paper cuts the estimated cost of factoring 1024-bit integers in bulk". The body names Coppersmith's MNFS as the 1993 method.
- libghostty sentence restructured so the date and actor lead. "Core of the" cut. JetBrains clause shortened.
- Sources renumbered in order of first citation (Pliny 2, DNB 3, Hazlitt 4, editors 5).
- Sources 4 and 5 hrefs changed from the Gutenberg catalogue page to the edition's HTML text at #Page_368 and #Page_457, with page numbers added to the locators.
- Source labels: "Euronews with AFP" changed to "Euronews". Fox label changed to "Slotkin's 13 October remarks". Trump label shortened.
- Restamped at 698 words, 15 sources.

## Decision

approve. The argument and the six items hold, every break was a fix inside the record, and `nb check --check-links` returns BLOCK: 0, WARN: 0, PUBLISHABLE.
