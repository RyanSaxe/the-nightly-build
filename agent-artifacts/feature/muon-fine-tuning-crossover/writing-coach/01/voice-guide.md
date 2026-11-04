# Voice guide: feature/muon-fine-tuning-crossover

## How this piece should sound

This is a researcher explaining an empirical result to people who already train models. It should sound like Dettmers and nostalgebraist writing about someone's paper, or their own: one practitioner talking to others in first person plural or plain declaratives, with the exact vocabulary of the field (token-to-parameter ratio, pretraining loss, fine-tuning set, forgetting, active versus total parameters) left unsoftened. The press reader has a CS or math degree and ships models, so skip the definitions they hold and define only what the paper itself introduces, such as its margin-to-spread account.

Where the material has a concrete instance, the piece can work from it the way Dettmers works from one hidden-state vector before and after quantization: a specific model size, a specific ratio, a specific fine-tuning set, with the general statement after. Horace He does the same with a single `x.cos().cos()` call. For a five-minute feature built around visuals, that habit is what the prose under each figure is for: say what one point or one curve on it means before saying what the whole shows.

The limits belong in the same voice as the finding, not in a separate cautious register. nostalgebraist says how far off his numbers could be and in which direction, in one plain sentence, and moves on. Dettmers marks which observations were too hard to verify and keeps going. Where the paper's range stops short of production models, or a result depends on the fine-tuning set, the piece can say so at that level of exactness, saying which way the uncertainty runs, with no display of carefulness around it.

Personality here comes from reaction to the material, and it stays short. nostalgebraist's irritation at a vague data section, Horace He's "Hey! This is a very stupid arrangement" and "Much better." are each one or two sentences inside an explanation, reacting to a specific thing on the page. A piece this short has room for that only where something in the paper or the comparison actually provokes it. It does not need jokes about the reader, and the house rules on figures of speech still hold.

## Tim Dettmers, "LLM.int8() and Emergent Features"

Source: https://timdettmers.com/2022/08/17/llm-int8-and-emergent-features/

> "In other words, even if we use vector-wise quantization, we squish a lot of information to zero and have large errors. On average, vectors without outliers have a mean error of 0.015. This vector has an error of 0.12. Do this for a couple of layers, and we remove all information and end up with pure noise."

Checked: https://timdettmers.com/2022/08/17/llm-int8-and-emergent-features/ (raw HTML via curl), retrieved 2026-11-04
He has just printed one actual vector before and after quantization, and this passage reads the numbers off it: the typical error, this vector's error, and what repeating it across layers does. "Squish" and "pure noise" are his words, a researcher talking casually about his own method without losing the figures.

> "Many other findings did not make it into the paper because these were too difficult to verify robustly, but I wanted to share them here anyway. Since these results are less robust, take them with a grain of salt."

Checked: https://timdettmers.com/2022/08/17/llm-int8-and-emergent-features/ (raw HTML via curl), retrieved 2026-11-04
He separates what the paper established from what he observed but could not verify, in two plain sentences, and says why the second group is weaker. The person is visible in "I wanted to share them here anyway": he admits the motive instead of dressing it up.

> "But training and using 6.7B transformers can be pretty painful. At Facebook AI research, I had a 1.3B parameter baseline and I would usually run 2-3 of those models on 128 GPUs each for a total of 384 GPUs. Despite these massive resources it would still feel “slow” in that my research progress was mostly hindered by compute."

Checked: https://timdettmers.com/2022/08/17/llm-int8-and-emergent-features/ (raw HTML via curl), retrieved 2026-11-04
A practical cost is stated through his own setup, with GPU counts a practitioner can compare against their own cluster. The claim "pretty painful" is backed immediately by numbers.

## nostalgebraist, "chinchilla's wild implications"

Source: https://www.lesswrong.com/posts/6Fpvch8RR29qLEWNH/chinchilla-s-wild-implications

> "So you should take the exact numbers below with a grain of salt.  They may be off by a few orders of magnitude (but not many orders of magnitude)."

Checked: https://www.lesswrong.com/posts/6Fpvch8RR29qLEWNH/chinchilla-s-wild-implications (raw HTML via curl), retrieved 2026-11-04
The caveat gives a size for the uncertainty instead of a general warning. The parenthesis is where the writer shows: a dry correction of his own hedge, which tells the reader how much the caveat should cost them.

> ""Dialogs data from public forums"?  Which forums?  Did you use all the forum data you could find, or only 0.01% of it, or something in between?  And why measure words instead of tokens -- unless they meant tokens?"

Checked: https://www.lesswrong.com/posts/6Fpvch8RR29qLEWNH/chinchilla-s-wild-implications (raw HTML via curl), retrieved 2026-11-04
He has just quoted a paper's data section in full, and here he asks the questions it leaves open, each one specific enough that the paper could have answered it. The irritation is audible, and it is aimed at missing facts, so it does the work of criticism.

## Horace He, "Making Deep Learning Go Brrrr From First Principles"

Source: https://horace.io/brrr_intro.html

> "So, you want to improve the performance of your deep learning model. How might you approach such a task? Often, folk fall back to a grab-bag of tricks that might've worked before or saw on a tweet. "Use in-place operations! Set gradients to None! Install PyTorch 1.10.0 but not 1.10.1!""

Checked: https://horace.io/brrr_intro.html (raw HTML via curl), retrieved 2026-11-04
The opening names the folk practice his readers actually follow, in their own words, before offering anything better. The last fake tip, with its exact version numbers, is the joke, and it only works for people who have lived it.

> "Hey! This is a very stupid arrangement. Why are we sending the same data to global memory and then back to the compute units, over and over? We should just keep the data at the factory, perform all of our compute, and then send it back!"

Checked: https://horace.io/brrr_intro.html (raw HTML via curl), retrieved 2026-11-04
This sits under a diagram and tells the reader what to notice in it. He reacts to the figure as a person would, then states the fix in one sentence, so the reaction leads straight into the technical point.

> "So... until you're doing about a hundred operations in your unary operator, you'll be spending more time performing memory accesses than actual compute."

Checked: https://horace.io/brrr_intro.html (raw HTML via curl), retrieved 2026-11-04
After a short calculation from A100 numbers, he reduces it to one threshold a practitioner can hold onto. The figure is approximate and says so ("about"), and nothing in the sentence is decorative.
