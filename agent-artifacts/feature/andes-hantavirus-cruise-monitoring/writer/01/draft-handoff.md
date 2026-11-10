# Draft handoff: feature/andes-hantavirus-cruise-monitoring (writer 01)

## Original work

The article puts the dates of the 42-day decisions next to WHO's later coverage estimate and the Epuyén incubation data. It traces "42" through the citation chain to a study that reports 39. It also computes the article's own bound on what zero of 88 rules out, and sets that bound against the Chilean household attack rates: zero of 88 excludes the sex-partner rate (17.6%) but not the household rate (3.4%).

## Proof

`nb check ... --series feature --repo /home/user/the-nightly-build` (links included): BLOCK 0, WARN 0, PUBLISHABLE. Words 1,187 against a strict 1,200 cap, so an edit that adds text has about 13 words of room.

Figures checked with `nb preview` and Playwright at 390 px and 1,280 px in light and dark themes. Nothing overflows and no labels collide. The chart PNGs use larger fonts than the house default so they stay legible at phone width.

## Choices an editor may question

- Fig. 2 plots the Epuyén bins as unjoined cumulative points at each bin's upper edge, with no fitted curve. The arithmetic "gamma with Epuyén moments leaves 0.8% past day 42" is stated in the prose and labelled as the paper's own.
- Fig. 3 marks only the 88 and the 40 high-risk contacts. The record's global bounds (653, 317) are left out because several of the 13 cases were themselves monitored contacts, so a "zero of n" bound does not apply to that cohort.
- The index-onset date is not used. The text says "since the index patient fell ill", so the 3 vs 6 April conflict never arises.
- The UK's 2 June move from 45 to 42 days was cut to meet the word cap. Fig. 2 still draws a 45-day line. The prose just above it explains that line (WHO's 4 May advice), but the caption does not, for lack of words.
- Source labels for Ferrés 2007, Iglesias 2022 and the UKHSA evidence summary are short descriptors, not full titles. The Ferrés title was not verified in the record, so it is not given.

## Open questions

- WHO's "probability of safe release" is read as the share of infected contacts symptomatic by that day. The article says WHO does not define the phrase. Assumed acceptable. Tell me if the orchestrator wants that interpretation dropped.
- The UKHSA bin count of 34 includes the Epuyén index case. The Fig. 2 caption says so, and UKHSA does not explain it.
