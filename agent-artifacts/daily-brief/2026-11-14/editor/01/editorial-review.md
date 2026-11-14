# Editorial review: daily-brief/2026-11-14 (editor/01)

## Correct

Thesis, from the draft alone: Iran and US Central Command gave incompatible accounts of an attack on Bahrain on 13 November. The other five items each report one event and whose account it is. Claims under the lead: the IRGC says it destroyed a US radar in Bahrain in reply to an "enemy" strike at Sirik; CENTCOM says two drones were shot down with no damage and does not mention Sirik; Trump says five Gulf states asked him to hold off. All three held against RFE/RL and IBT, read past the quoted lines.

Breaks, with the source and the fix:

- Iran. The sentence "nothing independent confirms either account" was cited to RFE/RL, which does not say it. IBT does say the circumstances at Sirik "have not been independently established", and that Bahrain made no immediate comment. The sentence now says no independent source has established what happened at Sirik, cited to RFE/RL and IBT. The IRGC quotation had a stray comma inside the closing mark. It now ends at "Sirik," and the clause after it places Sirik as "a port near the Strait of Hormuz" (RFE/RL). CENTCOM's line now keeps its own attribution of the launch to the Guard Corps. Trump is now "President Donald Trump". "Which not all of them have confirmed" had no clear referent and now reads "an account not all five have confirmed" (IBT). The item now has three sentences, where it had four. No sentence says who struck Sirik.
- Microsoft, order of statements. The draft said Microsoft first rolled back a network change and then said no recent change correlated with impact. PPC Land dates the "not identified any recent change" post to about 20:00 to 21:00 UTC on 12 November, with talk of reverting configuration updates an hour later. UptimeRobot puts the revert overnight. The draft had the order backwards, and the sentence now follows the sources.
- Microsoft, mechanism stated as cause. "It said an overwhelmed connection process caused the outage" overstated SecurityWeek, which reports the overwhelmed secure-connection process as a symptom and says Microsoft "had yet to confirm the root cause". It now reads "reported an overwhelmed secure-connection process on affected servers".
- Microsoft, 16:17 UTC. The incident-open time was cited to SecurityWeek, which does not contain it. Only UptimeRobot has it, and that source is not in the article. The first fact is now Microsoft's first public post at 17:54 UTC (PPC Land, quoting it). "About 26 hours" rested on the 16:17 time and was cut. The closing post's 18:05 UTC timestamp is confirmed in the X page metadata (2026-11-13T18:05:19Z).
- Microsoft, report status. "No post-incident report has been published" was cited to the X post, which cannot show it. It now reads that Microsoft has promised a post-incident report with the root cause. That is Microsoft's own status-page wording, quoted by SecurityWeek.
- AMD. "With no independent measurement published" was wrong. The 9996 and Xeon 6980P figures are published SPEC results that AMD's footnote links, and a Phoronix review of the 9996 exists (403 to the researcher). The footnote shows a different limit, which the record missed: the Nvidia Vera score is "AMD estimate 1459", with no published Vera result. I recomputed the ratios: 5470/1459 = 3.75, 5470/2510 = 2.18, 0.367/0.180 = 2.04. The benchmark is SPECrate2017_int_base, not "SPEC CPU2017" in general. The sentence now names the benchmark and says the Vera score is AMD's own estimate. This narrows the claim to the document's own footnote, and it is cited for the same claim as before. "256 cores" is now direct: the release's footnote 9xx6-086A gives "EPYC 9996 (256 cores ...)".
- Word card. "A man too weak to move his limbs" overstated the story, in which Jones has "what little strength he had" and moves easily when weightless. It now reads "a man with crippling muscular weakness", from the story's "pathological muscular weakness is an almost totally crippling condition". The definition's "copies the motions of its operator" comes from the story (secondaries "paralleled" the primaries), not HDSF, so it now cites both. The HDSF sentence's "it" had no clear referent. The sentence now says HDSF gives the story as its earliest citation and still asks for an earlier one (its "Research requirements: antedating 1942").
- Waldo quotation. I checked it against the scan, not the OCR. The Internet Archive page image for leaf n14 is printed page 16. The passage is in column 2 and reads "Waldo had resented the nickname the public had fastened on them—it struck him as overly familiar". The quotation is exact, and so is the locator "p. 16, col. 2". The printed href now opens that page (`/page/16/mode/1up`) where it used to open the item landing page. The OCR's "Pat. #296,001.437" is "#296,001,437" on the scan. The article does not use it.
- FAA. The quotation "due to extraordinary circumstances and for reasons of safety" was correct (WCVB/AP). I replaced it with the FAA's stated trigger, a telecommunications outage at its air route traffic control centers (Al Jazeera, WCVB quoting Duffy). That tells the reader more for the same words. Al Jazeera gives "more than four hours", so the heading now says that and no longer says "about four hours".
- Gemini. All figures match the blog (published 2026-11-12T18:00Z). The refusal figure is on printed page 7 of the model card (PDF page 8), +5.57pp, and the card's prose says "unjustified refusals are higher". The parenthetical "(lower is better)" went, because "higher unjustified refusals" already reads as a loss.

Every printed href returned 200 to curl, and I read each page's text, the model-card PDF and the scan image. Kinds were audited: s2, s7, s10, s11 and s12 are documents by the party making the claim (primary), and the rest are secondary. Al Jazeera and WCVB/AP are separate newsrooms. I found nothing mislabelled.

## Reads well

Cut: the stray comma in the IRGC quotation and "(lower is better)". Microsoft's middle sentence chained three clauses with commas and is now one ordered sequence. The FAA item's closing sentence was a comma triad, and its finding clause ("the FAA has published no finding") is gone. The two officials' statements now stand as a pair.

The IRGC item heading, "IRGC claims a radar kill in Bahrain, and CENTCOM counts two drones shot down", repeated the headline's two-clause structure one line below it. It now states the item's actual finding: "Iran and the US give opposite accounts of an Iranian attack on Bahrain". "Radar kill" was a decorating figure. The Gemini heading did not say why outscoring Argon was news. The body now gives Hydrogen as Google's fast-execution model and Argon as its frontier model, from the blog's own terms. The heading stays short.

Nothing in the draft came from the commission's sentences or the voice guide's quoted passages. Against recent-patterns.md, no item uses the "<Outlet> reports that" third sentence, and the word card has four sentences and one quotation.

## The experience

The page has no figures, and none would help: each item is two or three sentences, and there is no series to plot. The dek was the main change. The old dek, "Two outages on 12 and 13 November, one at Microsoft 365 and one at the FAA, have no established cause", grouped the two outages under one predicate. That is the link the commission forbids, and WCVB shows the link was a live question that night: Mullin both denied a connection to Microsoft and said nothing was ruled out. The new dek gives the lead what the headline left out: the IRGC's Sirik justification, which CENTCOM's statement does not mention. Neither outage appears above the items. Each stands under its own heading with nothing tying the two together.

What the piece gives beyond its sources: it puts each side's Iran claims next to each other and marks where the record stops. It puts Microsoft's cause statements in their actual order. It carries two numbers the companies' own headlines leave out: Hydrogen's refusal regression and the estimated Vera score behind AMD's 3.7x. The handoff's original-work sentence matched this, except that it said "shifting cause statements in order" when the draft had the order wrong. The piece now does what that sentence claims.

The headline holds. It is the largest claim, and each half is attributed to the party making it.

## Edits

- Dek: replaced the two-outage line with the IRGC's Sirik justification and CENTCOM's silence on it (header and nb-meta).
- Word card: definition cites s1 and s2; "too weak to move his limbs" changed to "a man with crippling muscular weakness"; HDSF sentence rewritten with a clear subject.
- s2 href now opens printed page 16 of the scan.
- Iran heading rewritten; item cut from four sentences to three; stray comma removed; Sirik located; independent-confirmation sentence re-sourced to IBT; Trump given his title; dangling "which" fixed.
- Microsoft heading rewritten; 16:17 UTC and "about 26 hours" removed; first post at 17:54 UTC added; order of the no-correlated-change and rollback statements corrected; mechanism no longer stated as cause; "no post-incident report" replaced by Microsoft's promise of one.
- Sources 5 and 6 swapped so they are numbered by first citation (PPC Land is now s5, SecurityWeek s6); PPC Land's note updated.
- FAA heading "about four hours" changed to "more than four hours"; first sentence now gives the telecommunications outage at the traffic control centers; reopening and cancellations merged into one sentence; triad closer cut.
- Gemini heading shortened; Hydrogen and Argon given their roles from the blog; "(lower is better)" removed.
- AMD: "has 256 cores" and the price shortened; benchmark named as SPECrate2017_int_base; "no independent measurement published" replaced with the Vera score being AMD's estimate.
- `nb stamp`: 693 words, 12 sources, 3 minutes. Proof: BLOCK 0, WARN 0, PUBLISHABLE.

Assumption, for the orchestrator to confirm or overrule: the Vera-estimate detail and the corrected Microsoft order come from the cited sources (AMD's footnote, PPC Land) but are not in the evidence record. I treated them as narrowing to what the cited document prints. I did not treat them as a record-versus-source conflict, because the record does not contradict them. Its Contradictions entry gives the Microsoft order the other way round, and the sources do not support that order.

## Decision

approve. Every break was fixable from the cited sources. The argument and the slate stand as commissioned, and the proof is clean at 693 words.
