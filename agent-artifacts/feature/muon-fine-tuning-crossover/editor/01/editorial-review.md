# Editorial review: feature/muon-fine-tuning-crossover (editor/01)

## Correct

Thesis: in the CMU preprint (arXiv 2611.03633v1), the budget at which AdamW pretraining overtakes Muon on the learning-forgetting frontier tracks a token count more closely than a token-to-parameter ratio. Every production model pretrained with Muon sits far past that count, but nothing tests the placement and the one matched production comparison went the other way. Claims under it:

1. Muon pretrains to lower loss in every cell, and past a crossover budget AdamW gives the better fine-tuning trade. This held against Section 3.2, Appendix D.1 and Appendix C.2 of the preprint's HTML, which I opened. The pooled fine-tuning optimizer for Muon models is stated as the paper states it.
2. The 20 crossovers in Table 2 sit between 2.4B and 19.2B tokens, and the pooled log-log slope is -0.97. I read Table 2 in the preprint and recomputed both: the token conversions, the per-set slopes (-0.64, -1.02, -1.17, -1.07) and the pooled -0.97. The 128-fold and 8-fold spreads, the 8x and 64x falls and the Alpaca rise from 4.8B to 12B all check. The paper prints the 600M GSM8K value as "5". The ring and "at or below" caption follow from the paper's own definition (the smallest budget with G_FT > 0, and 5 is the smallest budget run), so they stand.
3. Production models are 300 to 1,500 times past the band, and the parameter convention moves only K2. I recomputed 475 and 15 TPR for K2, 5.7T/19.2B = 297, 28.5T/19.2B = 1,484 and 40B/600M = 67, and checked the K2, GLM-5, Kimi Linear and Moonlight counts in their PDFs. The opener said "hundreds of times" and the first revision said "at least 300", but 5.7T is 297 times 19.2B. It now says "about 300 times as many or more".
4. Moonlight's twin runs favor Muon at 1.2T tokens. I checked Table 6 and the Moonlight-A and pre-cooldown passages on pp. 8 and 10 of arXiv 2502.16982. The table matches. The draft said Wen et al. warn that "cooldown" can mislead. Their abstract says that comparing intermediate checkpoints can mislead because rankings flip during learning-rate decay. I narrowed the sentence to that wording.

No claim broke. One citation sat loose. The draft cited 2606.16899 for shrinking gains under constant weight decay but never said why that matters. The preprint's Section 3.2 names Muon's shrinking pretraining advantage as one of its two hypothesized causes of the falling crossover. The paragraph now says so, cited to the preprint, so the weight-decay point changes the reading as the commission asked.

Labels: the headline, dek and subheads carry no title or affiliation that the sources contradict. Every href lands on its arXiv abstract page (opened by curl, and the proof's link check passes). Exact titles, from each abstract page: the preprint is "Pretraining Data Scale Reverses the Muon-AdamW Fine-Tuning Gap" (hyphen, not en dash). The others are "Kimi K2: Open Agentic Intelligence" (correct from memory), "Kimi Linear: An Expressive, Efficient Attention Architecture", "Arcee Trinity Large Technical Report", "GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models", "GLM-5: from Vibe Coding to Agentic Engineering", "Fantastic Pretraining Optimizers and Where to Find Them" and "Fantastic Pretraining Optimizers and Where to Find Them II: Hyperball Optimization". The Stanford label stays on 2509.02046 only, because the record gives no affiliation for 2606.16899. All nine data-nb-kind values are primary, each cited for its own model or experiment. The two Wen papers share authors, and the piece does not present them as independent corroboration.

## Reads well

Cut:
- "Read StackMathQA first." It said nothing and is a lecture opener (spec/slop.md, Fluff). The paragraph now starts on the number.
- "In practice," a filler connective.
- "Take the lowest-pretraining-loss 60M model..." This imperative opener was recast as what the paper does.
- "...the fall the paper reports". The citation already carries the attribution.
- The two closing sentences that restated "every Muon-pretrained production model with published counts has seen trillions" nearly word for word from the orientation. The closer now carries only the weighing: production models sit trillions further on, and the one matched test there favored Muon without measuring forgetting.
- To fit the hard 1,200-word band after the chart rebuild, I also removed: Muon's one-clause mechanics (the linked earlier piece covers them), the MMLU and HumanEval margins (the table shows them), the table caption's duplicate caveats (the prose has them), "No trend is extended past 600M" (no trend line is drawn), and the long author lists in the source labels.

Recent record: the headline no longer runs past 15 words (14 now). It states a finding in words with no lead number. The dek has no trailing "where" clause and holds one figure, the band. It no longer opens the same way as the first sentence ("In a CMU preprint" twice). The first section does not restate a headline number, because the headline has none. The headings mix a sentence, a fragment, a noun phrase and a comma phrase. The close ends on the scope of the finding, not on an attribution caveat.

Lifted: the mechanism paragraph now says what the ratio does ("the more wrong answers stay below the right one when fine-tuning perturbs the outputs"). The draft had a softer "keeps more wrong answers below". The Kimi K2 sentence says it is a mixture-of-experts model before it splits the denominator.

## The experience

At 390 px, Figs 2 and 3 were unreadable. Their labels rendered at about 5 px because `nb chart` exports a fixed 1200x675 canvas. I replaced both with inline SVG drawn from the same series (Table 2; the production counts in the evidence record). The SVG uses theme variables and a viewBox about 400 units wide, as `press/editorial.md` specifies. Fig 2 is two panels that stack on a phone. Its legend, the slope-of-minus-one band on the ratio panel and the flat band on the token panel are unchanged, and the censored point is ringed in both panels. Fig 3 is one compact dot plot with shared row labels. Its right axis now uses decade ticks (10B to 10T) because the old 2.4B/19.2B and 5.7T/28.5T labels collided. I checked both at 390 and 1280 px in light and dark through `nb preview` and Playwright. Labels read at about 9 to 11 px on a phone, the charts now follow the dark theme, and neither width scrolls sideways. One trade-off: the engine counts SVG label text as words, which forced the cuts listed above. The writer's chart-1/2 .py and .png files were removed from the bundle because nothing references them. Copies and the generator script are in my scratch directory. Fig 1 is the preprint's own figure at the resolution `nb asset pdf` produces. On a phone its panel labels are small but the curves are clear, and I left it.

Beyond the sources: the piece shows that the paper's falling crossover ratio is close to a fixed token count of a few billion (slope -0.97 against -1). It then places every Muon-pretrained production model against that count under both parameter conventions and weighs Moonlight's matched run against the extrapolation. Neither the preprint nor the model reports does any of that. This matches the original-work sentence in the handoff. The headline claims a "similar token count at every size tested". The piece supports that and states the 8-fold spread and the grid precision.

## Edits

- Headline: "...after a similar number of tokens at every model size tested" became "...after a similar token count at every size tested" (title and nb-meta).
- Dek rewritten. It now carries the who (CMU preprint, 30M to 600M), the one figure band and the production contrast. It no longer opens like the first sentence.
- Orientation: dropped Muon's mechanics clause, and "hundreds of times past that" became "about 300 times as many or more".
- Section 2: "Take the..." became "The paper fine-tunes...". The crossover definition and pooling sentence were tightened. The mechanism paragraph was tightened, with the ratio's effect stated.
- Fig 2: the PNG (chart-1) was replaced with two inline SVG panels. The caption was shortened, and the band is now labeled in the chart.
- Section 3: cut "Read StackMathQA first." and "the fall the paper reports". "Seven grid steps / three" became "128-fold / 8-fold". The Chinchilla sentence was tightened and "In practice" cut.
- Section 4: the K2 sentence was recast. Fig 3's PNG (chart-2) was replaced with one inline SVG dot plot. The caption gained "on log scales". "On the left/right" became "On the ratio/token scale" because panels stack on a phone. "Without computing their ratios" was cut.
- Section 5: "Moonshot's report" became "Moonshot AI's report on Moonlight". The table caption's duplicate caveats were cut. The MMLU and HumanEval margins were cut. The Wen 2509.02046 sentence was narrowed to its abstract's claim about intermediate checkpoints. The weight-decay paragraph now ties 2606.16899 to the preprint's own size hypothesis. The closer was rewritten to drop the repeated sentence.
- Sources: exact titles for s1, s4, s5, s6, s7, s8 and s9. Shorter author labels. "Stanford" kept only where the record supports it.
- Removed chart-1.py, chart-1.png, chart-2.py and chart-2.png from the asset directory.
- Ran nb stamp: 1,194 words, 5 min, 9 sources.

## Decision

approve. The argument holds against the primary sources, every fix was made in place, and the proof with links is BLOCK 0, WARN 0, PUBLISHABLE.
