# Commission

## Assignment

Publish a Paper of the Day article on Dirk Bergemann, Andrew Koh, and Stephen Morris, “Mechanism Design for Alignment and Control” (arXiv:2609.01595, September 2026).

## Editorial decision

Headline: Sandbagging turns capability tests into menus

Dek: Bergemann, Koh, and Morris model an AI’s hidden preferences and capabilities as a private type, then show why a test can earn trust only when the permissions it buys are incentive-compatible.

Central claim: A capability evaluation is not a neutral measurement once its score changes what an AI is allowed to do. The focal paper’s contribution is to put the evaluation, the report, the reward or permission menu, and the eventual action in one mechanism. Its sharpest lesson is directional: under one-sided evidence, a more capable agent can imitate a less capable one, so a deployment policy must be designed around the reports an agent can make and the actions it can later take. The paper gives a rigorous benchmark for this design problem. It does not validate a deployed safety protocol, establish that current models optimize stable preferences, or show that real evaluations satisfy its verification order.

## Reader and register

Write for ML engineers and technically literate AI-safety readers who know basic probability, optimization, and model evaluation, but may not know mechanism-design terminology. Use the house serious-paper register: calm, precise, first-principles, and concrete. Define “type,” “verification order,” “direct mechanism,” “obedience,” “double deviation,” and “cyclical monotonicity” at first use. Explain the quadratic toy model with a worked interpretation rather than leaving the result as notation.

## Planned reconstruction

1. The score already buys something. Start from current frontier-safety practice: capability thresholds and evaluation outcomes select safeguards, deployment restrictions, or permission tiers. Explain why that makes an evaluation part of a mechanism.
2. The hidden type has three ways to surprise you. Reconstruct the tuple of preference, feasible actions, beliefs, and information, and distinguish the paper’s revealed-preference abstraction from mechanistic interpretability. Use evaluation-awareness, scheming, and alignment-faking work only to show why the private-type problem is live.
3. A truthful report can still produce a bad action. Explain the direct mechanism, the revelation principle, and the requirement that honesty and obedience survive together, including report-then-disobey double deviations.
4. One-sided evidence makes sandbagging directional. Use the focal paper’s Figure 1 as a local source asset. Work through nested action sets, capability understatement, the monotone cap result, and the distinction between falling and rising bias.
5. The best cap sees the square of the bias. Set the focal paper’s optimal-cap equation, explain the root-mean-square term, and use Figure 8 to show how changing the training technology changes the preferred control level. State carefully what “alignment” and “interpretability” mean in this model.
6. The paper’s control claim is conditional. Cover the multi-agent extensions briefly, then weigh their assumptions against AI Control and iterated amplification. End with a narrow verdict: the paper identifies an incentive-compatibility condition that evaluation-and-permission systems should satisfy, but the hard empirical work is measuring types, verification order, and robustness to strategic behavior.

## Furniture and source assets

- Keep the template’s paper card and verbatim abstract.
- Capture Figure 1 from page 12 of the focal PDF as `asset-1.png`; the crop should include the nested action sets and the sandbagging/counterfeiting labels, without the printed caption or page furniture.
- Use one annotated equation for the optimal cap, with the legend explaining mean bias, variance, and average squared bias.
- Capture Figure 8 from page 35 as `asset-2.png`; the crop should include the three plotted panels and axes, without the printed caption or page furniture.
- Captions for both assets must cite the focal paper with exact page/figure locators and explain what the artifact settles in the reconstruction.
- Do not add a hand-drawn chart or an image that is only decorative.

## Source plan

Use at least eight read primary sources. The focal paper owns the theoretical claims. Use the following sources only where they change the interpretation:

1. Focal paper: https://arxiv.org/abs/2609.01595
2. Anthropic, Responsible Scaling Policy: https://www.anthropic.com/responsible-scaling-policy
3. Google DeepMind, Updating the Frontier Safety Framework: https://deepmind.google/blog/updating-the-frontier-safety-framework/
4. OpenAI, Preparedness Framework v2: https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf
5. van der Weij et al., AI Sandbagging: https://arxiv.org/abs/2406.07358
6. Needham et al., Large Language Models Often Know When They Are Being Evaluated: https://arxiv.org/abs/2505.23836
7. Greenblatt et al., Alignment Faking in Large Language Models: https://arxiv.org/abs/2412.14093
8. Meinke et al., Frontier Models are Capable of In-context Scheming: https://arxiv.org/abs/2412.04984
9. Greenblatt et al., AI Control: Improving Safety Despite Intentional Subversion: https://arxiv.org/abs/2312.06942
10. Christiano, Shlegeris, and Amodei, Supervising Strong Learners by Amplifying Weak Experts: https://arxiv.org/abs/1810.08575

## Guardrails

Do not call the focal paper a solution to alignment. Do not infer stable goals or consciousness from “preferences”; report that the authors use revealed preference as an abstraction. Keep empirical claims tied to the cited experimental papers and their stated setups. Do not use exact numbers from a source unless the source has been read and the number is verified. Separate the focal paper’s theorem statements from the article’s synthesis. Avoid copying recent Paper of the Day headline/dek molds or repeating the recent “What holds up” structure. The article should be 2,300–3,000 words including the abstract card, with 6 flex sections and a concise Sources section.
