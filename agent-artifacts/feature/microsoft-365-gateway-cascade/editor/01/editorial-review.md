# Editorial review: feature/microsoft-365-gateway-cascade (editor/01)

## Correct

Thesis, from the draft alone: by Microsoft's own final report, a lock-contention defect shipped to gateway servers in July sat harmless for months until three ordinary load conditions coincided on 12 November, and the gateways' designed traffic redistribution then carried the failure across North America and into every region within about two hours. Claims under it:

1. The trigger. The defect hit only newer, higher-core servers, and it fired when about 14% of capacity was out for deployment, Teams had failed over at 01:07 UTC, and the North American peak arrived. Held against final PIR pp.2 and 6-7 (365Fanatic copy, SHA-256 identical to the researcher's file). The draft joined "more cores allow more contention" and "load tests ran on older hardware" under one "because", so the second clause read as a cause of the first. Split into two sentences.
2. The spread. Intra-region rerouting moved load onto fewer servers carrying the same defect, then cross-region redirection reached regions running the same update. Held against p.8 and Next Steps row 1. The preliminary's "separate issue" bulkhead quote checked against the next.ink copy p.3. The table's four rows match both reports' wording.
3. The recovery. The Executive Summary's three reasons lead, and the rejoin loop is presented as the body's added finding (p.8), corroborated by @MSFT365Status 00:06 UTC 13 Nov, as the commission amendments require. "The revert worked when applied to whole groups" claimed a success condition the PIR does not state. The PIR describes a strategy: large groups of capacity units taken out of rotation, recovered and returned. Narrowed to that.
4. The repair list. The admission-control row is TBD (p.15) and the recovery-procedures row is CY27 Q1 and concerns distributing the fix. Both correct. The draft called rows 1 and 4 "the two items written against how this failure spread", but rows 2 (smaller fault zones) and 9 (retries spreading issues) are also blast-radius items and both are TBD. The definite article claimed an exclusivity the table does not support. Changed to "Two items". The closing line, "a quarter on stopping the next spread", overstated for the same reason. Narrowed to the cross-region cascade fix (row 1, CY26 Q4) against the rejoin fix (row 8, TBD), which is what the list shows.

Headline attribution, as the brief asked. "Microsoft says its own traffic rerouting turned a latent July defect into a global outage" credited the rerouting with converting the latent defect into an outage. The PIR gives that role to the three load conditions (p.2, p.7) and says redistribution "expand[ed] and accelerat[ed] the impact" and "further spread the impact to other regions (which had the same performance regression)" (pp.2, 8). Within North America, it says redirected load "increased the likelihood of triggering the same Windows performance regression on other gateway servers". So "set off a latent July defect in every region" is Microsoft's statement. "Turned it into a global outage" was the piece's compression. Headline changed. With "global outage" gone, the dek's "the 12 November outage" had no antecedent for a reader arriving from a link, so the dek now names it as the Microsoft 365 outage.

Timestamps and figures in both SVGs, checked against the PIR's pages. Fig. 1: ~14% (p.6), 01:07 (p.6, p.9), ~16:00 (p.7), >80% North America (p.8), ~2 h to every region (p.8), 07:20 revert (p.12), group recovery (p.8). One label was off. The PIR's 23:55 entry is when Microsoft "determined" that returned servers were failing again, not when the failures began, so "from 23:55" became "found 23:55" in Fig. 1 and "found failing again" in Fig. 2. Fig. 2 is drawn at 10 units per hour, and every tick and band edge recomputes: 00:25, 01:07, 16:00, 16:20, ~18:00 (inferred, as captioned), 19:20, 23:55, 07:20, 16:10, 04:15. Band lengths are 14 h 53 min, 2 h, 13 h 20 min, 8 h 50 min and 12 h 5 min, and the impact bracket is 23 h 50 min. The prose called the 18:00-07:20 band "the longest band", but the pre-outage gray band (14 h 53 min) is longer. Changed to "the third band". The caption now says the times are UTC.

Subheads: "Fifteen hours after the failover" matches the PIR's own timestamps (14 h 53 min) and the preliminary's "approximately fifteen hours". The prose already reports the final's "~16 hours" against it. "Took Exchange Online down for a day" matches the 23 h 50 min impact window.

Every printed href opened. The 365Fanatic and next.ink PDFs return 200, and their SHA-256 hashes match the source copies. The Bronson PDF returns 200, and the §1 passages are on p.221-222 as located. Both x.com posts return pages whose title and og:description carry the cited text: Lamanna's "abridged version" line, and the status account's "can become unresponsive again once they receive traffic". WebFetch itself got 402 from x.com, but a plain browser request lands on the post.

Kinds: all five are marked primary. That is right for the two Microsoft reports, the status account and Lamanna's post as Microsoft statements, and for Bronson et al. as the owners of the definition. The piece claims no independent corroboration beyond the status account's timing match, and that account is Microsoft's own, which the text already says ("Every figure here is Microsoft's").

The metastable paragraph called the label "an outside reading", a phrase that names nobody. It now says plainly that Microsoft does not use the term, then gives the paper's definition and the reason it fits only in part, per the commission amendment.

No disagreement between the record and a source I opened needed the orchestrator.

## Reads well

Went or changed:
- "The body of the report adds panel B of Fig. 1." The report does not add a panel. Now "adds the loop in panel B".
- Section 2 heading "Each rerouted unit pushed more load onto the next". Units were not rerouted, their traffic was. Now "Each failing unit pushed its load onto the next".
- The preliminary-versus-final paragraph spent two sentences paraphrasing what the table's last row already shows. Compressed to one sentence plus the repair-finding quote, which recovered words for the fixes above.

Briefing leakage: I read the commission's "What the article is" and amendment sentences against the prose. No clause appears lifted. The amendments are applied in the article's own wording. No voice-guide passage is echoed. The Luu-style arrow chain in Fig. 1 ("fewer healthy servers → more load on each → more lockups") is a chain of quantities, which the guide permits, and none of its wording is borrowed.

Recent record: the dek is not the feature mold (a second number with an undercutting clause), and the piece is not built as a correction of a vendor's number. None of the flagged phrases appear. A "Microsoft says" headline has no recent feature precedent.

Edges: I read every paragraph's first and last sentence out of order. "Panel A reads from the top" tells the reader how to read the drawing, which the voice guide asks for. Kept. The article's last sentence passes the placeholder test because its nouns carry it, and it states the conclusion the repair-list paragraph builds. It was overstated, and it is now narrowed (see Correct). The draft never ran flatter than the guide's register, so no lift was needed beyond the precision fixes.

## The experience

At 375 px and 1280 px, in light and dark, the page scrollWidth equals the viewport width. Fig. 1's labels are clear of each other and every arrow meets its box. Fig. 2's day labels sit above their rules, and the impact bracket and band colors read in both themes. Fig. 2's colors match Fig. 1's: red for the defect and spread, amber for the lockups. The table scrolls sideways inside its wrapper on a phone, so the 20 November column is off screen at first. That is the documented nb-table behavior, and the four rows are short enough to compare after one swipe. I left it.

What the piece gives beyond its sources: one drawing that joins the PIR's four factors, spread section and recovery section, a to-scale timeline with the phase lengths computed, and a check of the 13-row repair list against the two loops in that drawing. That check shows the cross-region fix carries a date and the rejoin fix does not. This matches the writer's original-work sentence. The headline, reread last as the largest claim, now says only what Microsoft says.

## Edits

- Headline (h1, title, nb-meta): "turned a latent July defect into a global outage" → "set off a latent July defect in every region".
- Dek (and nb-meta dek): "the 12 November outage" → "the 12 November Microsoft 365 outage".
- Section 2 heading: "Each rerouted unit pushed more load onto the next" → "Each failing unit pushed its load onto the next".
- Section 2, para 1: split the "because ... and load tests" sentence into two.
- Section 2, preliminary paragraph: compressed to "The preliminary report blamed that last step on bulkheads between partitions that failed 'due to a separate issue'. The final drops it, and its first repair finding reads ...".
- Fig. 1 panel B label: "from 23:55" → "found 23:55".
- Fig. 2 label: "fail again" → "found failing again".
- Fig. 2 caption: added "in UTC".
- Section 3 prose after Fig. 2: "The longest band" → "The third band".
- Section 4, para 2: "adds panel B of Fig. 1" → "adds the loop in panel B of Fig. 1". Replaced "The revert worked when applied to whole groups..." with "Microsoft recovered by patching large groups of capacity units at once, held out of rotation."
- Section 4, metastable paragraph: "That label is an outside reading ... Their bad state outlasts its trigger" → "Microsoft does not use the term, and it fits only in part. In the paper's definition the bad state persists after the trigger is removed. These servers failed again while the defect was still deployed, and the report never shows a patched server overwhelmed."
- Section 4, repair paragraph: "The two items written against how this failure spread ... Teams failing over worldwide" → "Two items written against how far this failure reached ... one region's Teams fault failing over worldwide".
- Last sentence: "Microsoft has put a quarter on stopping the next spread and none on keeping a restarted server up." → "Microsoft has dated the fix for the cross-region cascade and not the one for servers knocked over as they rejoin."
- Restamped with nb stamp: 1194 words, 5 sources, 5 min.

## Decision

approve. The argument holds and is the PIR's own. Every break was a label, attribution or scope fix that I made in place, and the proof passes (BLOCK 0, WARN 0, PUBLISHABLE, links checked).
