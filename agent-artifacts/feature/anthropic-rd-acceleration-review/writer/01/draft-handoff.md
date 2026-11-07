# Draft handoff: feature/anthropic-rd-acceleration-review (writer 01)

## Original work

The article sorts every published estimate of AI-driven acceleration at Anthropic into lanes by the quantity each one measures, and sets them against the RSP's own two-condition definition. That shows only the capability-index lane tests condition (a). For 15 July, METR's two figures in that lane, 1.5 and 1.9, are both under 2, and the July estimates that reach 2 are in the leading-indicator and counterfactual lanes. The article also compares the documents themselves: the Risk Report's "attributable primarily" sets a stricter attribution test than the RSP's "plausible … substantially attributable".

## Proof

`nb check … --series feature --repo …` with links: BLOCK 0, WARN 0, PUBLISHABLE. Words 1,196 against the strict 1,200 ceiling. The count includes SVG text, captions, the table and the source list, so any line an editor adds has to come out of something else.

Both figures are inline SVG using theme variables. I checked them at 390 px and 1,280 px in light and dark through `nb preview` and Playwright. Nothing overlaps, there is no horizontal page scroll, and text labels have a halo so the 2x line does not run through them.

## Provisional decisions

- Headline "No measure of Anthropic's AI-driven acceleration rules out 2x". The basis for each lane: in A, METR's October 1.9 has an interval of 1.5 to 2.8. In B, METR gives 1.3 to 2.8. In C, the private report calls exceeding 2 "plausible". In D, METR's judgment runs from 1.3 to 3. The Opus 5.5 card's own interval (1.20 to 1.82) excludes 2, but it is one estimate in lane A and not the lane's latest.
- Body copy says "the threshold". "Early warning" appears only inside quotations from METR and the Risk Report, with the Risk Report's "functions as a potential early warning" quoted, because the RSP gives the threshold no such label. "Full Substitution" is labelled as METR's term.
- Fig. 1 puts the RSP's 9x/81x example and METR's 15/30 points example side by side, and the caption calls them separate examples. They are not an equivalence.
- Cut to stay in the word band: self-reported uplift (4x, 12x), which stays off the chart and out of the text; the interview tally; and METR's statement that Claude did most of its analysis (optional under the commission). The disclosure is a one-sentence closing note.
- I used the S-1/A as Anthropic's latest public position, quoted and located.
- nb-meta model is `claude-opus-5-5`, the session model. Harness is "Claude Code".

## Questions for the orchestrator

- Please confirm the nb-meta model string format (`claude-opus-5-5`) matches the paper's convention.
- If the editor wants the uplift figures or the Claude-analysis line restored, something of equal length must come out, because the count is at 1,196.
