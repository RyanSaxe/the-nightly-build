# Draft handoff: feature/muon-fine-tuning-crossover (writer 01)

## Original work

The article converts the preprint's 20 crossover ratios into tokens. It shows them sitting in one 2.4B–19.2B band, with a pooled slope of −0.97 against the −1 a fixed token count gives. It then puts Muon-pretrained production models on both parameter conventions beside that band, so the reader sees that the convention changes their ratios and never their tokens.

## Proof

`nb check ... --series feature --repo /home/user/the-nightly-build` (links included): BLOCK 0, WARN 0, PUBLISHABLE. Stamped at 1,174 words, 5 min, 9 sources. The band is strict at 1,200, so there is little room for additions.

No warnings were left.

## Choices the editor should know

- Visuals: Fig. 1 is the preprint's Figure 1, captured from PDF p2 with `nb asset pdf` (all four panels, legend and axis arrows kept). Fig. 2 (`chart-1.py`) draws Table 2 as printed and in tokens. Fig. 3 (`chart-2.py`) is a dot plot of production models in TPR (active and total) and in tokens. I dropped a first scatter version of Fig. 3 because K2, Trinity Large and the two GLMs overlapped at near-equal token counts. The Moonlight Table 6 numbers are a table. There is no mechanism drawing. The mechanism gets one paragraph, per the commission's "one short treatment at most".
- The figures pass at 1280 px. At 390 px, Fig. 1 and the two-panel charts render small because `nb chart` exports a fixed 1200×675. They need a pinch-zoom to read on a phone. I raised every chart font to 17–21 px, and with that canvas I could not do better. Both themes look right, and neither width scrolls sideways.
- The "best-frontier slope −0.95" and the Liu et al. 2605.06654 independent run were cut to stay inside 1,200 words. Liu et al. supported the direction at about 123M and 8B tokens. Qu et al. 2605.10468 and Ruan et al. are not used.
- The "≤5" GSM8K 600M value is drawn as an open ring and named in the caption as censored.
- Chart 1 points are offset a few percent sideways per fine-tuning set. The caption and the script docstring both say so.
- The earlier piece is linked as `../the-paper/muon-optimizer.html`. The link check passed.
- Source titles for Kimi Linear, Trinity, GLM-4.5, GLM-5, 2509.02046 and 2606.16899 are descriptive labels, not the exact paper titles. The evidence record does not give them. Kimi K2's title ("Open Agentic Intelligence") is from memory and is worth one look.

## Open questions

- None on evidence. One voice question: the "Read StackMathQA first." opener under Fig. 2 is a direct instruction, in the Horace He mode the guide allows. Cut it if the editor reads it as a lecture opener.
