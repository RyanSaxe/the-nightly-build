# Voice guide: feature/agent-eval-cost-frontier (01)

## How this piece should sound

This is a five-minute piece for engineers who ship ML systems, and it reads like one of them explaining a measurement to a colleague who will check the arithmetic. The register is level. Dan Luu and Simon Willison both put the number or the worked sum where another writer would put an adjective, and neither tells the reader a figure is large or surprising. A cost per problem, an accuracy, a ratio between two of them: give the figure, then give the one thing it licenses. The Epoch passage shows the other half of the habit, which is stating what a number does not cover in the same plain voice as the number itself.

Treat the reader as someone who can follow a division. Where the piece derives accuracy per dollar, or reads a point off the frontier, write the calculation out in a sentence the way Willison does with his photo library, so the reader can redo it. Where a measurement has a limit, name the limit concretely, as Luu does with the display that advertises 1 ms and takes 10. The cost figures here are measured inference cost under one environment and not retail prices, which is a limit of exactly that kind, and the material may call for saying so once, in the sentence where the figure first appears.

Keep the prose short around the figures, since the figures carry the argument. Luu's paragraphs read a chart aloud (which line, which percentile, what the gap is) and then stop. A sentence that points at the drawn diagram or the scatter should say what to look at in it, in the piece's own terms: agent, frontier, budget, cost per problem. The material may also call for a plain first-person judgment, as in Willison's remark that his own benchmark is a pale imitation of a real one, where a writer who has looked at the data says what they think of it and why. Keep that to places where the data supports it.

A reader who does not trust the first number should be able to see where it came from. Where the sources disagree or a cost accounting looks weak, say so in the voice of the rest of the piece, without alarm and without performed care.

## Dan Luu, "Computer latency: 1977-2017"

Source: https://danluu.com/input-lag/

> "I've had this nagging feeling that the computers I use today feel slower than the computers I used as a kid. As a rule, I don’t trust this kind of feeling because human perception has been shown to be unreliable in empirical studies, so I carried around a high-speed camera and measured the response latency of devices I’ve run into in the past few months."

Checked: https://danluu.com/input-lag/, retrieved 2026-10-31
He states the suspicion, says why he distrusts it, and names the instrument he used instead, all in one run of plain sentences. The person on the page is someone who does not accept his own impression and goes to measure it.

> "I have a display that advertises 1 ms switching on the box, but if we look at how long it takes for the display to actually show a character from when you can first see the trace of it on the screen until the character is solid, it can easily be 10 ms. You can even see this effect with some high-refresh-rate displays that are sold on their allegedly good latency. At 144 Hz, each frame takes 7 ms."

Checked: https://danluu.com/input-lag/, retrieved 2026-10-31
The advertised number and the measured number sit in the same sentence, with the definition of what was measured in between. The sentence is long, but each clause adds one fact, and the next one starts from a figure.

## Dan Luu, "Some latency measurement pitfalls"

Source: https://danluu.com/latency-pitfalls/

> "Since a few or even one such node can determine the tail latency for a cluster, taking the average across all nodes can be misleading, e.g., if we have a 100 node cluster where tail latency is up by 10x on one node, this might cause our average of cluster-wide latencies to increase by a factor of 0.99 + 0.01 * 10 = 1.09 when the actual increase in tail latency is much larger."

Checked: https://danluu.com/latency-pitfalls/, retrieved 2026-10-31
The loose reading (the average moved a little, so little happened) is refuted with a one-line sum a reader can redo. He uses the practitioner's own terms, tail latency and cluster-wide, without glossing them for an audience that already holds them.

> "For example, if we look at 99%-ile latency, we can see that it's ~16ms when measured at the server and ~240ms when measured at the client, a factor of 15 difference. Alternately, if we look at a fixed latency, like 240ms, and look up the percentile, we see that's 99%-ile latency on the client, but well above 99.9%-ile latency on the server."

Checked: https://danluu.com/latency-pitfalls/, retrieved 2026-10-31
He reads the chart aloud in two directions, first fixing the percentile and then fixing the latency, and gives the ratio in words. It shows how to describe a figure so the reader can find the point on it.

## Simon Willison, "Things we learned about LLMs in 2024"

Source: https://simonwillison.net/2024/Dec/31/llms-in-2024/

> "Today $30/mTok gets you OpenAI’s most expensive model, o1. GPT-4o is $2.50 (12x cheaper than GPT-4) and GPT-4o mini is $0.15/mTok—200x cheaper than GPT-4, nearly 7x cheaper than GPT-3.5 and massively more capable than that model."

Checked: https://simonwillison.net/2024/Dec/31/llms-in-2024/, retrieved 2026-10-31
Each price is followed by the comparison to something the reader already knows, as a multiple. The reader never has to hold a bare dollar figure.

> "Here’s a fun napkin calculation: how much would it cost to generate short descriptions of every one of the 68,000 photos in my personal photo library using Google’s Gemini 1.5 Flash 8B (released in October), their cheapest model?
> Each photo would need 260 input tokens and around 100 output tokens.
> 260 * 68,000 = 17,680,000 input tokens
> 17,680,000 * $0.0375/million = $0.66
> 100 * 68,000 = 6,800,000 output tokens
> 6,800,000 * $0.15/million = $1.02
> That’s a total cost of $1.68 to process 68,000 images. That’s so absurdly cheap I had to run the numbers three times to confirm I got it right."

Checked: https://simonwillison.net/2024/Dec/31/llms-in-2024/, retrieved 2026-10-31
The arithmetic is written out line by line, with the inputs stated first, so the total is checkable. His reaction to the result is one plain sentence, and he gives the reason he trusts it, which is that he reran it.

> "I’m still trying to figure out the best patterns for doing this for my own work. Everyone knows that evals are important, but there remains a lack of great guidance for how to best implement them—I’m tracking this under my evals tag. My SVG pelican riding a bicycle benchmark is a pale imitation of what a real eval suite should look like."

Checked: https://simonwillison.net/2024/Dec/31/llms-in-2024/, retrieved 2026-10-31
He says what he does not know and what his own benchmark is worth, in two short statements. A judgment of his own work is stated flatly, and the one joke is built from his own benchmark.

## Ben Cottier (Epoch AI), "Trends in the dollar training cost of machine learning systems"

Source: https://epoch.ai/blog/trends-in-the-dollar-training-cost-of-machine-learning-systems

> "The cost estimates have large uncertainty bounds—the true costs could be several times larger or smaller. The cost estimates are themselves built on top of estimates (e.g. training compute estimates, GPU price-performance estimates, etc.). See the Methods section and Appendix J for discussion of the uncertainties in the respective estimates."

Checked: https://epoch.ai/blog/trends-in-the-dollar-training-cost-of-machine-learning-systems, retrieved 2026-10-31
The limits are stated as facts about the estimate, with the size of the error given ("several times") and a pointer to where the reader can inspect it. There is no apology in the tone.

> "The cost estimates only cover the compute for the final training runs of ML systems—nothing more."

Checked: https://epoch.ai/blog/trends-in-the-dollar-training-cost-of-machine-learning-systems, retrieved 2026-10-31
One sentence draws the boundary of what the dollar figure includes. It is the form a note takes when the number is a cost and the reader might read it as a price.

> "Using a dataset of 124 machine learning (ML) systems published between 2009 and 2022, I estimate that the cost of compute in US dollars for the final training run of ML systems has grown by 0.49 orders of magnitude (OOM) per year (90% CI: 0.37 to 0.56)."

Checked: https://epoch.ai/blog/trends-in-the-dollar-training-cost-of-machine-learning-systems, retrieved 2026-10-31 (superscript footnote numbers after "2022," and "0.56)" omitted)
The finding comes with its sample size, its date range, its unit defined in parentheses and its interval, in one sentence. The first person ("I estimate") marks who made the estimate.
