# Draft handoff: feature/toolturns-multi-turn-agents (writer 01)

Article: `library/feature/toolturns-multi-turn-agents.html` in the workspace.

## Original work

The paper cubes one model's pooled rate (Opus 4.8); this article multiplies each model's three per-position rates, shows all nine completing 5.8 to 8.4 points above that independence product, and then shows that cubing the opening rate comes within 3.3 points for eight of nine models only because the follow-up decline (factor 0.59 to 0.94) and the clustering (factor 1.19 to 1.51) offset. It also puts the rubric-versus-success rank disagreement at its actual strength (GPT-5.4-mini; p = 0.55 at n = 9).

## Proof result

Command: `nb check ... --series feature --repo /home/user/the-nightly-build` (links included), after `nb stamp` (1,191 words, 5 min, 3 sources).

- BLOCK: 1, WARN: 0.
- The one block is `W-SOURCES-MIN`: 3 sources against the series floor of 5 (the series is strict). I did not clear it, because the evidence record opens only three documents I use (ToolTurns, Laban et al., tau-bench). The fourth, MultiChallenge, was read by abstract only and the researcher recommended against it. It carries no claim in this piece, and adding it, or splitting one paper into several entries, would be padding to satisfy the label. Even with it the count is 4. See the question below.
- Word count is close to the hard ceiling (1,191 of 1,200, counted over title, dek, headings, captions, table, SVG labels and the sources list). Any edit that adds words needs an equal cut.

## Visuals

Four inline SVGs (Fig. 1 dialogue diagram, Fig. 2 position dot plot, Fig. 3 observed against independent, Fig. 4 rank slope) and one table, all computed from the paper's Tables 3 and 4 as transcribed in the evidence record. Each was rendered with `nb preview` and captured with Playwright at 390 px and 1280 px, in light and dark. No overlap, clipped text or sideways page scroll remains. The table scrolls sideways inside its card on a phone (the runtime wraps it).

## Decisions

- Headline and dek avoid the figure-against-figure, "which leaves" and "while" patterns. The opener states the finding. The closer states the conclusion the article builds (the opening-rate cube is close only through offsetting errors), not a limit of the record.
- No claim that failures "cascade". The clustering is stated as positive association whose cause the tables cannot separate. The paper's own two explanations are quoted.
- tau-bench is used only for direction: the paper gives pass^8 only as "below 25%", and independent trials would give 1.9% (0.61^8, my arithmetic), so the article says it cannot test clustering. The researcher's note read the bound as the observed value, which the text does not support.
- Laban et al. appear twice: the Concat control (the control ToolTurns lacks) and the "wrong turn, do not recover" abstract line (the carry-over explanation).
- The paper's checker-fixer is reduced to one clause. The 536-turn and 335-to-197 figures were cut for length.
- GPT-OSS-120B carries a dagger in all figures and the table (protocol non-compliance in 56.1% of dialogues, and it is also the judge model).
- The decline is not presented as a cost of carrying context. The paper's own judge-omission caveat and the missing single-turn control are stated.
- Figures marked "my arithmetic" or "my computations" are the researcher's or mine from the transcribed tables: averages 67.9 and 59.4, the 1.9 to 15.0 fall, the independence products, the sampling error of about one point, Spearman 0.64 without GPT-5.4-mini, the permutation p-value of 0.55 (re-derived by me), and the follow-up and clustering factors.

## Questions for the orchestrator

1. Source floor: I need two more opened primary or secondary sources that carry real claims. Candidates from the commission are the BFCL multi-turn results or the MultiChallenge body, to say whether another benchmark shows per-turn or per-dialogue structure. StableToolBench, ToolBench or API-Bank could back the tool-layer and simulator description, which the paper's design relies on. If the source floor is to be met by evidence, the researcher has to open them. Otherwise please say whether the floor may be waived for this piece, because I will not pad the list.
