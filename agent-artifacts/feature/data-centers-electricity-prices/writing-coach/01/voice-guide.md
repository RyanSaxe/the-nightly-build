# Voice guide: feature/data-centers-electricity-prices (01)

## How this piece should sound

The reader builds production ML systems and has met a regression and a fixed effect. They have not met a rate case. They will read the way they read a postmortem or a benchmark writeup: they want to know what was measured, against what baseline, and whether the number would survive a different setup. The register is that of a colleague walking through someone else's evaluation, plain and committed, with the figures stated and the methods named in the words the economists use. Treat the reader as able to follow a counterfactual and a denominator without a lecture on either, and define a term of art once, where it first matters.

Lucas Davis's walk through the Brown tracker is the nearest model for how to handle an estimate. He announces what he is going to check, as a list of questions about assumptions, then follows the calculation in the order it is computed: actual price, counterfactual price, quantity. He says which assumption is strong, which one he likes and why, and which direction the omitted piece would push the total. When the material gives the writer a comparable question for a study (what is the counterfactual here, which price is this, which direction does the unmodeled part push), asking it in the same plain way suits this piece. Davis also says "I like this" and "my vote would be", so the judgment is visibly his. Where the documents support a ranking of the studies, state it in the first person plural or singular and show the reasoning from the design.

Hannah Ritchie's piece shows how to handle several numbers that all look like rebuttals of each other. She takes the figure everyone shares, grants what is true in the reply, and then splits the quantity by what it is made of, so the disagreement turns out to sit in a denominator or a category. Her footnote reports a series that looked wrong, what she suspected, and what she cross-checked it against. Where this piece finds that one study's number is built on a different price, unit or period from another's, say which, and put the two on a shared scale where the documents allow. When a figure had to be repaired or reclassified to be comparable, say what was done to it.

James Sallee's piece shows a short account of a result that flips under a condition, and a threshold stated with its units. He gives the intuition in a worked example with small round numbers, then names the case where it fails. For this piece, the mechanism by which a large new load can lower or raise a rate is the place for that kind of worked case, in the subject's own terms (kilowatt-hours, fixed network costs, capacity prices, load growth). Prose in all three passages stays short and carries numbers with their units, and none of them reaches for a closing moral. Their paragraphs end on the figure or the finding.

Because the piece is built around visuals, the prose is the caption's companion. Davis and Ritchie each tell the reader what the chart or equation is and what to read off it before saying what follows. Sallee does the same with a figure he did not draw, naming the regions of it. A sentence that says how to read a figure can carry the labels and units in the words the figure uses.

Two directions come from the brief and not from the exemplars. The piece is five minutes long, so the most a section can hold is one claim and the evidence that carries it, and a study that does not bear on the comparison need not appear. Studies commissioned by an interested party are named with their sponsor in the sentence that reports them, in the same flat tone as the others, with no comment on motive unless the document gives a reason.

## Lucas Davis, "Pain at the Pump: $130 Billion and Counting"

Source: https://energyathaas.wordpress.com/2026/10/12/pain-at-the-pump-130-billion-and-counting/

> "For today’s post, I want to dig into the IWECT. I know that gasoline and diesel prices are up sharply, but I want to better understand the methodology behind the IWECT. What are the key assumptions? Are these assumptions reasonable? What do these calculations include and not include?"

Checked: https://energyathaas.wordpress.com/2026/10/12/pain-at-the-pump-130-billion-and-counting/, retrieved 2026-11-06
He states what he already accepts (prices are up) and then lists the questions he will put to the method. The questions are about assumptions and coverage, so a reader knows what the post will test before it starts.

> "The counterfactual price is hard. What would gasoline and diesel prices have been without the Iran war? For this, they use the actual AAA price as of February 28, 2026, the day the Iran war began, adjusted for seasonal variation."

Checked: https://energyathaas.wordpress.com/2026/10/12/pain-at-the-pump-130-billion-and-counting/, retrieved 2026-11-06
A four-word judgment, then the question it poses, then the tracker's exact choice with its date. The person is visible in the short flat verdict and in the fact that he reports the choice instead of paraphrasing it.

> "I also mostly like the decision to use the historical five-year average, and appreciate its simplicity. A more complete calculation would incorporate the price elasticity of demand. Already there is growing evidence that U.S. fuel consumption will be somewhat lower in 2026, due to higher prices. By not accounting for this demand elasticity, the IWECT modestly overstates the consumer burden."

Checked: https://energyathaas.wordpress.com/2026/10/12/pain-at-the-pump-130-billion-and-counting/, retrieved 2026-11-06
He says what he likes, what a fuller version would add, and which way the omission pushes the total, with "modestly" as the only size word. The first person ("I also mostly like") is how a reader learns this is a judgment and whose it is.

## Hannah Ritchie, "Does China have a huge electricity advantage over the United States?"

Source: https://hannahritchie.substack.com/p/china-vs-us-electricity

> "The replies are always the same: China has a much larger population, and when we adjust for that, the US generates far more. That’s certainly true. Here is the same comparison in per capita terms. China has overtaken the European Union in the last few years, but the US is still far ahead."

Checked: https://hannahritchie.substack.com/api/v1/posts/china-vs-us-electricity (raw post body), retrieved 2026-11-06
She concedes the rebuttal in two words ("certainly true") and moves straight to the chart that shows it. Each sentence gives one fact, and the chart is introduced by a plain sentence saying what is being compared.

> "Now, we can argue whether it’s total or per capita generation that matters. If it’s about the living standards of individuals, per capita makes more sense. A country could use a lot of electricity but still have most people living in energy poverty if it has a large population. If it’s about industrial capacity or dominance, total electricity is more revealing: your ability to dominate global solar panel or battery markets, robotics or other manufacturing sectors, is about how much stuff you can build and sell, not how much you can do per person."

Checked: https://hannahritchie.substack.com/api/v1/posts/china-vs-us-electricity (raw post body), retrieved 2026-11-06
She ties each choice of denominator to the question it answers, and she does it in the same register as the rest of the post, with "how much stuff you can build and sell" as the one informal phrase. A reader leaves knowing which measure suits which claim.

> "If you plot the raw IEA series for “Industry” for the US, there is a very large drop in electricity use in the early 2000s. While directionally correct, the magnitude of this drop seemed implausible to me.
>
> After looking at the other sectoral data, this drop happens alongside a substantial rise in electricity use in the “Other end use” category. I think there is a reclassification of some industrial electricity in the US in the IEA dataset around this time, which leads to some odd results."

Checked: https://hannahritchie.substack.com/api/v1/posts/china-vs-us-electricity (raw post body), retrieved 2026-11-06
A footnote reporting a data problem: what looked wrong, what it coincided with, and what she infers, marked as inference by "I think". The dataset, the category name and the decade are given, so the reader could check it.

## James Sallee, "Rethinking Linking"

Source: https://energyathaas.wordpress.com/2026/11/02/rethinking-linking/

> "Linking did not link two similar markets. It hitched an ambitious policy environment (Québec) to a slack one (California). In this case, the slack policy was the bigger market, so the net result is that Québec’s price got dragged to California’s floor. The model shows that some allowances that would have gone unsold in California’s regulatory auctions if California was isolated were in fact sold and sent to Québec."

Checked: https://energyathaas.wordpress.com/2026/11/02/rethinking-linking/, retrieved 2026-11-06
The finding comes as a plain description of what happened between two named places, with the cause of the direction ("the bigger market") given in the same sentence. The verbs are physical (hitched, dragged, sent), and the technical terms (allowances, floor, auctions) are the field's own.

> "The theory model says we need to know prices that would have prevailed if there was no linking and no price collars. We can’t just look at data for this, so Thor builds a model to estimate the necessary counterfactuals and conducts a series of statistical analyses."

Checked: https://energyathaas.wordpress.com/2026/11/02/rethinking-linking/, retrieved 2026-11-06
He says what quantity the result depends on, says it cannot be read off the data, and says what the author did about that, in three short sentences with no apology. "We can’t just look at data for this" tells an engineer exactly why the estimate rests on a model.

> "Thor estimates the increase was around 17 million tons of CO2e over the first eight years. This did create cost savings, since some expensive abatement in Québec was avoided. But, if you put a conventional value on carbon, that savings doesn’t cover the increase in pollution damages: Thor shows that you have to value CO2e at a very low level, less than $29 per ton (in 2013 dollars), to conclude that linking was a net gain, assuming this is a net increase and not just a pull forward."

Checked: https://energyathaas.wordpress.com/2026/11/02/rethinking-linking/, retrieved 2026-11-06
The result is a threshold with a unit and a base year, and the closing clause states the one assumption it depends on. The figure, the period and the condition are all in one sentence, so a reader can restate the claim.

## Decisions recorded

- The brief named Borenstein, Wolfram, Roberts, Levine and Our World in Data as examples. Bloomberg was not reachable (403) and the Volts posts that could be opened were podcast transcripts, so I chose Davis and Sallee from the Energy Institute at Haas blog, and Ritchie, the Our World in Data researcher, from her Substack. Borenstein's own recent post on distribution costs (fixed costs spread over more kilowatt-hours) covers this article's mechanism, so I did not quote it, to keep findings out of the guide.
- None of the three exemplars covers data centers.
- Sallee's "hitched" and "dragged" are the most colorful words here. They fit a feature, but the press standard restricts figures of speech to those that explain something, so use them as a model of concreteness and not of metaphor.
