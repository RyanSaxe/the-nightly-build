# Commission: feature/covid-test-negative-sequelae

Run: scheduled edition 2026-11-11. Template: article. Strict band 600-1200 words, 2-4 flex sections, at least 5 sources.

## The story
A Stanford-led paper in PNAS (doi 10.1073/pnas.2604414123, published about 10 November 2026) analyzed 14.4 billion insurance claims for 244.7 million US patients (March 2020 to March 2021 enrollment) across 614 outcomes in three windows after infection (1-4, 5-12, 13-24 months). With a test-negative design, comparing PCR-positive to PCR-negative patients enrolled at their first test, it linked 43 outcomes to COVID in the early window, 5 in the middle and 0 in the late. The same data analyzed with a comparison group that includes untested people linked 262, 286 and 369. (Figures from CIDRAP's report; the researcher confirms each against the paper.)

## Angle
The piece is about the comparison group. The same claims, with only the control group changed, turn hundreds of apparent long-term effects into a handful, and the count in the untested-control design rises with time while the test-negative count falls to zero. Explain the mechanism: people who get tested differ from people who don't (they were sick enough, or in contact with care), so an untested control is healthier at baseline and the gap is charged to COVID. Then the fair counterpoint: a test-negative control is not neutral either. A PCR-negative patient was tested because something was wrong, false negatives and later unrecorded infections contaminate the controls, and both can shrink a real effect. Line this up against the prominent earlier estimates that used broader controls (for example the VA cohort studies by Al-Aly and colleagues, and RECOVER or other designs the researcher finds), stating each in its authors' terms. Conclude only what the evidence supports about how much of the earlier long-tail signal is a comparison-group artifact.

The original work: put the two designs' counts side by side by window and show which way each control group biases the estimate, which the paper and coverage do not lay out together with the earlier studies' designs.

## Visuals (owner prefers drawn mechanism over basic bars)
- The counts by window under both designs (a computed chart, nb chart, or inline SVG).
- A diagram of who lands in each comparison group and where the bias enters.
- If the paper gives organ-system or outcome-level results, a small comparison of which survive.

## Boundaries
Not a medical-advice piece. No claim that long COVID is not real; the authors themselves say it remains a serious concern. Exact figures only from the paper or the owning document. Attribute critics by name; if no independent expert has commented, say no one has yet and do not invent the reaction.

## Neighbouring articles this run
daily-brief/2026-11-11 must not use this PNAS study as an item. reinforcement-learning/semi-gradient-td is unrelated.

## Recent-pattern notes (for writer and editor)
- Two of the last four feature deks began "By X's arithmetic, ..." ("By METR's arithmetic", "By this paper's arithmetic"). That opener is a house catchphrase now; do not use it.
- Recent headlines: "Health agencies set 42 days...", "Four state redistricting votes in 2026 move no House district line", "Cutting Lp(a) as far as one genetic study required did not reduce cardiovascular events". Several are "<subject> <verb> no/not <thing>" negative findings; avoid making this one another "X did not Y" construction if a positive statement of the finding works.
- Recent first section headings narrate the setup ("Six weeks of watching 88 people", "Two maps blocked, one rule loosened, one limit refused"). The second was a numeric triad; avoid triads in headings.
- Closing sections of recent features were "What zero infections in 88 contacts can rule out" / "Seats the blocked maps targeted": ending on a bounding "what X can rule out" section is becoming a habit. Close on the conclusion in a different shape.

## Production record
Writing coach (low effort), researcher (high), writer (high), editor (high, model inherit) run as subagents on the orchestrator's model; the "capable" tier is met by that model. No deviation.

## Decisions after research (orchestrator, 2026-11-11)
- Naming: follow the paper. Call the broad comparison the paper's term for it (its "unrestricted" control design), and define its controls exactly: people with no COVID diagnosis, tested or not. Do not call it an "untested" control. The test-negative design compares people diagnosed within 7 days of a first PCR test to people whose first test was negative, all enrolled at the test.
- The angle is corrected: the two designs differ in the case group and the enrolment point as well as the controls. Say so; do not write "only the control group changed". The comparison-group mechanism remains the main explanation the authors give, and the piece can show it, but it must state both differences.
- Dates: paper online 27 October 2026 (PNAS issue of 3 November). The news peg is the coverage this week; do not say the paper came out this week.
- Scope of the conclusion: the evidence supports that most of the late-window signal in a VA-style design run on these claims is attributable to the comparison group, shown by its negative-control outcomes. It does not support a share of the VA studies' own findings being artifacts; the VA papers passed their own negative-control checks. Present the VA, RECOVER and Mizrahi (BMJ 2023) results fairly, including that other test-anchored designs still find later effects.
- No independent expert reaction exists yet; say that plainly if reaction is mentioned. Al-Aly's 2023 criticism of test-negative controls is about the Maccabi study and must be attributed as such.
- Organ-system counts are unavailable; the third visual, if any, uses the five named outcomes that survive into the middle window.
