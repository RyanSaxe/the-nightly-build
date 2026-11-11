# Voice guide: feature/covid-test-negative-sequelae

## How this piece should sound

This is a methods story told to readers who build models for a living. They know what a confounder is, what selection does to a training set, and why a held-out set has to look like production. What they may not hold is the epidemiology vocabulary: test-negative design, comparison group, sequelae, false negative as a source of misclassification. Define each of those once, in a clause, where it first does work, and then use the same word every time. "Comparison group" and "control group" should not trade places for variety.

The register is the one Julia Rohrer and the Data Colada authors hold: a working methodologist explaining a design choice to colleagues, plainly, with the numbers in the sentence. Rohrer's sake-cup passage shows how far a single concrete case can carry a bias explanation before any formal term appears. This article's mechanism, who gets a PCR test and who never does, can be walked through the same way: one kind of patient, which group the design puts them in, and what that does to the count. The term arrives after the reader has already seen the problem.

Data Colada's "This is much more problematic than it may appear" paragraph shows how to state a strong methodological conclusion: the claim, then the reason it follows, with no softening. Where the counts by window support saying the untested-control design is measuring something other than infection, the piece can say so at that strength. Where they do not, the same plainness applies to what remains unsettled, such as how much a test-negative control shrinks a real effect.

Kucharski's polio paragraph and his V0/V1/V2 comparison show the fair-counterpoint register this piece needs. He states what each approach gets right before saying where it goes wrong, and he names the specific mistake ("mistaking a mediator for a confounder"). The earlier broad-control studies and the test-negative design can be treated that way: each stated in its authors' terms, each with the direction its comparison group pushes the estimate.

The five-minute budget and the visuals decide the rest. Prose between figures should say how to read the figure and what follows from it, at the length Rohrer gives her setup paragraphs, and not repeat what the chart already shows. A light touch of wit is available where it comes from the subject's own facts, as Rohrer's comes from the cup itself, but this is a health story with patients in it, and the jokes in her footnotes belong to a blog, not to this page.

## Julia Rohrer, "My Immortal Time Bias"

Source: https://www.the100.ci/2026/08/08/my-immortal-time-bias/

> "Imagine you have data from the Japanese population and  calculate how long those who received the cup and those who never received the cup live, on average. Unsurprisingly, those who received the cup have a life expectancy over 100 — because they needed to turn 100 to receive the cup in the first place. Those who never received the cup have a considerably lower life expectancy, maybe somewhere around 80 — the usual Japanese life expectancy, minus every cupper."

Checked: https://www.the100.ci/2026/08/08/my-immortal-time-bias/ (raw HTML via curl), retrieved 2026-11-11
A selection bias is shown with a case so concrete that the wrong answer is obvious before the bias has a name. The numbers are rough and labelled as rough ("maybe somewhere around 80"). "Minus every cupper" is her: a small coinage that also states exactly who is missing from the comparison group.

> "This scenario is an (extreme) example of immortal time bias. What is happening here is that the “outcome clock” starts before the treatment occurs: Our outcome is life expectancy and we count that starting from birth; the treatment occurs a century later. Essentially, everybody in the treatment group gets 100 years “for free” before they are even given the treatment."

Checked: same URL, retrieved 2026-11-11
The term is introduced only after the example, and then defined by one working image, the outcome clock, tied straight back to the case. Each sentence moves from the label to the mechanism to the consequence. She marks her own example as extreme in parentheses, which is the methodologist's honesty about the illustration.

> "Apparently, immortal time bias is a really common problem in health research. That is not because the researchers involved are stupid, but because in the usual scenario, it is a lot less obvious – the relevant bits of information to spot it aren’t handed to you in a silver cup – and harder to avoid."

Checked: same URL, retrieved 2026-11-11
She is fair to the researchers who make the error and says why a competent person makes it. The cup returns once, as a callback, inside the sentence that carries the point.

## Uri Simonsohn, Joe Simmons and Leif Nelson, "[109] Data Falsificada (Part 1): “Clusterfake”"

Source: https://datacolada.org/109

> "There is no way, to our knowledge, to sort the data to achieve this order. This means that these rows of data were either moved around by hand, or that the P#s were altered by hand. We will see that it is the former."

Checked: https://datacolada.org/109 (raw HTML via curl), retrieved 2026-11-11
Three short sentences: an observation with its limit stated ("to our knowledge"), the two possibilities it leaves, and a commitment to which one. The authors are visible in that last sentence, which promises the reader evidence and does not hedge.

> "If this data tampering was done in a motivated fashion, so as to manufacture the desired result, then we would expect those suspicious observations to show a particularly strong effect for the sign-on-the-top vs. sign-on-the-bottom manipulation.
>
> And they do."

Checked: same URL, retrieved 2026-11-11
A prediction is stated before the data are shown, so the reader can see the test is fair. The answer gets a three-word paragraph. The confidence comes from having said in advance what would count against them.

> "A little known fact about Excel files is that they are literal zip files, bundles of smaller files that Excel combines to produce a single spreadsheet [4]. For instance, one file in that bundle has all the numeric values that appear on a spreadsheet, another has all the character entries, another the formatting information (e.g., Calibri vs. Cambria font), etc."

Checked: same URL, retrieved 2026-11-11
Technical background is given exactly when the argument needs it and no earlier, with the specific detail (the font names) that makes it concrete. It assumes a capable reader who simply has not seen this file format from the inside.

## Adam Kucharski, "Confounded by confounders"

Source: https://kucharski.substack.com/p/confounded-by-confounders

> "In reality, temperature influenced both ice cream consumption and polio transmission. Temperature was a confounder: it influenced both the exposure (ice cream) and the outcome (polio), creating a correlation that wasn’t a cause."

Checked: https://kucharski.substack.com/api/v1/posts/confounded-by-confounders (body_html field, raw), retrieved 2026-11-11
The definition is attached to the example it explains, with the general terms (exposure, outcome) mapped onto the particular ones in parentheses. An epidemiologist's vocabulary is used exactly and taught in one line.

> "If one variable is correlated with another, it can still be useful information: if the pattern is consistent, we make predictions about what tends to occur. But we can’t say what will happen if we change something."

Checked: same URL, retrieved 2026-11-11
He gives the confounded correlation its due before stating its limit, which is fairness to a method he is about to criticise. The distinction between prediction and intervention is one an ML reader already holds, and he states it in two plain sentences.

> "V2: Estimate when variable descriptions are hidden: This produces a substantial underestimate, because the purely data-driven approach misidentified some relationships, including mistaking a mediator for a confounder, skewing the estimate."

Checked: same URL, retrieved 2026-11-11
Each design is reported with the direction of its error ("underestimate") and the specific cause, so the comparison across designs is about mechanisms and not only about which number was closer.
