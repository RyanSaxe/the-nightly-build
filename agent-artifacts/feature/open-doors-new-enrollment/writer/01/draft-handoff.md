# Draft handoff: feature/open-doors-new-enrollment (writer 01)

**Original work.** The article splits IIE's year-on-year change in the total into its four levels (OPT, graduate, undergraduate, non-degree) and then the 2025/26 graduate and OPT changes into India, China and all other places, so it shows that the enrolled fall (-73,135) is 94% graduate-and-India and that India's OPT rise alone offsets 52.6% of it, a split IIE's own text does not print. IIE supplies the lag point (its OPT-growth sentence and its forecast); the article credits it.

**Proof.** `nb check ... --series feature --repo /home/user/the-nightly-build` (links included): BLOCK 0, WARN 0, PUBLISHABLE. Stamped 1,091 words, 5 min, 10 sources. No warning left.

**Visuals.** Fig. 1 and Fig. 2 are `nb chart` PNGs from committed `chart-1.py` and `chart-2.py` (the data is in the scripts, taken from the record's tables; "Other places" in Fig. 2 is world minus India minus China, by subtraction). Fig. 3 is an inline-SVG flow drawing, labelled conceptual, with only observed IIE counts and no projection. All three were looked at at 375 px and 1280 px in light and dark through `nb preview`; no horizontal overflow. The chart PNGs use large type so they stay readable on a phone.

**Choices the editor may check.**
- Opening avoids a count-against-baseline first sentence and the close avoids a two-period figure, per the brief.
- Headline claim "more than half" is this paper's arithmetic: 38,461 / 73,135 = 52.6%. It is shown in section 2 with a cited note.
- The cohort projection is dropped, per the commission. The only lag-ratio sentence states the OPT / new-graduate ratio at 1.61 (2017/18) and 1.91 (2025/26) as a division of IIE's counts, with no forecast.
- Snapshot non-degree is omitted from the table because the Snapshot text (-15%) and its Figure 2 (-14%) disagree; the table caption says so.
- NAFSA's dollar estimate is omitted (commission allowed omission). Causes are attributed to institutions' reported reasons in the Snapshot, with IIE's own two qualifiers.
- The researcher's Snapshot-against-census backtest is presented in Table 1 as a comparison of IIE's published figures, with "one year of one survey" stated; it is not attributed to IIE.

**Open questions.** None on evidence. One voice note: the guide's first-person habit (Evans, Dynomight) was used lightly; the article has no "I" and states what was computed in captions and notes instead.
