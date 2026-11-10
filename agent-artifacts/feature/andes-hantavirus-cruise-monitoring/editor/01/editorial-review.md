# Editorial review: feature/andes-hantavirus-cruise-monitoring (editor/01)

## Correct

Thesis, from the draft alone: the 42-day watch on Andes virus contacts was fixed by WHO, CDC and ECDC in early May, and WHO estimated what it covers only on 28 May. The claims under it:

1. CDC's 88 US contacts came from the ship (28, all high risk) and two 25 April flights (60, 12 high risk), and each was watched for 42 days from last exposure. Held. Fig. 1's counts, risk split, end dates and the quoted footnote match MMWR Table 2, the "Monitoring and Testing" section and footnote §, which I reopened.
2. The 42 days came before the estimate, and the number traces to a citation that does not match its source. Held. DON599 says "45 days" (4 May). DON600 says 42 (8 May). HAN 00528 is dated 8 May and says "within 4-42 days". ECDC's 9 May PDF has "the full range of possible onset". DON604 has the 96%/91% sentence and "reaffirms". Martinez-Valdebenito 2014 has "18.5 (range 7–42) days (3)" and Vial 2006 has "7–39 days". UKHSA Annexe D has the bins 5/10/13/6, the 9–40 range and mean 21.6 (SD 7.0). Iglesias 2022 has "range 9–40 d". I recomputed the gamma tail with those moments: 0.80% past day 42.
3. Zero of 88 bounds the per-contact attack rate at 3.35% (one-sided 95%). That excludes the Chilean partner rate (17.6%) and reaches the household rate (16/476). Partly held. The arithmetic is right: 1 − 0.05^(1/88) = 3.347%, 3/88 = 3.41%, 40 contacts give 7.2%, 0.988^88 = 0.35, and 248 contacts would exclude 1.2%. The words around it were not. 16/476 is 3.36%, a hair above the bound, so at 95% the 88 do exclude it, just. The closing line said the bound excluded "the Chilean partner rate, not the household one", which is false at the printed precision. The orientation said the 88 "cannot tell 'no risk' apart from" the household rate, which overstates the same point. I reworded both to "meets the household one" and "bound the risk only down to the rate...". The dek's "level with" was already right. The record's own summary has this slip ("the same as the household attack rate"). It needs no orchestrator call, because the editor's change follows the record's numbers, not its prose.

Headline, the round's focus. "WHO chose 42 days ... before estimating what it would catch" names one actor for a three-agency decision. It also leaves out that the US monitoring the piece measures was CDC's. On the documents, WHO did not originate the figure. It moved from 45 to 42 on 8 May, the same day CDC's HAN used 4–42, and the earliest 42-day recommendation in the record is the 2014 Chilean paper. The "before" order holds, since the only estimate is WHO's of 28 May. The order of who adopted 42 first cannot be settled from the record: DON600 and HAN 00528 share a date. I changed the headline to "Health agencies set 42 days of Andes virus monitoring before WHO estimated what it would catch". It keeps the order the documents support and puts WHO only where WHO acted alone. The commission's "CDC already used 4–42" is not shown by the record either. The HAN is dated 8 May, not earlier, so "By then CDC was telling clinicians" became "On 8 May CDC told clinicians".

The 3.35% label. Before editing it was labelled in the dek ("On this paper's arithmetic"), in the section that derives it, and in Fig. 3's caption, but not in the closing paragraph. The dek also called a 95% bound a "cap" without the 95%. Both now carry the label and the confidence level. Fig. 3's caption now says "at 95%" as well.

The other labels in the headline, dek and subheads were checked against MMWR, UKHSA and the WHO DONs. Those are the 88, 42, 3.35%, "everyone who had been aboard", "two days past Epuyén's longest incubation" (40) and 13 cases / 3 deaths. CFR attributions also hold: ECDC "20% to 35%" (threat brief annex), MMWR "approximately 40%", and DON600/DON604 "40-50%".

Citations. I opened every href as printed. All the WHO, ECDC, EID, UKHSA and Elsevier links return 200 on the source. MMWR and HAN 00528 return 403 to curl from this proxy, and both load in a fetching browser agent with the cited text in place. Ferrés (doi 10.1086/516786) and NEJM (10.1056/NEJMoa2009040) resolve to OUP and NEJM publisher pages that 403 to bots. I checked their cited text through the PubMed abstracts, which the locators name. The proof's link check passes. I added a citation to UKHSA [11] on the gamma sentence, whose mean and SD it supplies. Kinds hold: UKHSA and Iglesias are rightly secondary for figures extracted from the NEJM paper, and no secondary is presented as independent of its primary.

## Reads well

Nothing in the body failed the placeholder test badly enough to cut. The sentences carry their nouns. I found no lifted clauses from the voice-guide passages and no commission sentences taken whole. "The 88 rule out the partner rate and stop at the household rate" went: the closing paragraph says the same thing more exactly, and its wording was the version that broke on 3.36%. The draft is not running flat. The Fig. 2 and Fig. 3 paragraphs work numbers through in the way the guide asks.

Against the recent record: the old headline avoided the "no / did not" frame, and so does the new one. The dek is one figure set against one reference rate, not a two-figure "and/so" pair. The headings are differently built clauses. The closing paragraph restates the two findings rather than adding a moral, which is acceptable for the reading budget.

## The experience

Desktop (1,280 px) and phone (390 px), light and dark, from `nb preview` with Playwright: no horizontal scroll, and backgrounds switch with the theme. Fig. 1's connectors land in the right boxes and its bar widths are in 40:48 proportion. Fig. 2's labels clear each other, and the 45-day line, previously unexplained in its caption, is now named there. Fig. 3's annotations do not collide. The 9 px sublabels in Fig. 1 are small on a phone but readable. What the piece gives beyond its sources: it lines up the adoption dates against the one coverage estimate, traces "42" back to a paper that reports 39, and computes what a clean result in 88 contacts can and cannot exclude. No source does all three. That matches the handoff's original-work sentence.

## Edits

- Headline (title, nb-meta, h1): "WHO chose 42 days of Andes virus monitoring before estimating what it would catch" → "Health agencies set 42 days of Andes virus monitoring before WHO estimated what it would catch".
- Dek (meta and page): now "By this paper's arithmetic, CDC's 88 uninfected US contacts put a 95% upper bound of 3.35% on the per-contact attack rate, level with ...".
- Orientation: "cannot tell 'no risk' apart from the rate" → "bound the risk only down to the rate".
- Day-42 section: "By then CDC was telling clinicians" → "On 8 May CDC told clinicians".
- Day-42 section: UKHSA citation [11] added after "21.6 and 7.0 days".
- Fig. 2 caption: added "Dotted lines: 35 days and WHO's first 45."
- Zero-of-88 section: cut "The 88 rule out the partner rate and stop at the household rate."
- Fig. 3 caption: added "at 95%".
- Closing paragraph: the bound is now labelled as the paper's 95% bound and "the Chilean partner rate, not the household one" → "rules out the Chilean partner rate and meets the household one". "The only estimate" → "The only published estimate"; "published 20 days after" → "issued 20 days after".
- `nb stamp`: 1,198 words, 14 sources, 5 minutes.

## Decision

approve. The argument holds on the documents, and the two breaks were wording a direct edit fixed: one actor in the headline, one rate on the wrong side of the bound.
