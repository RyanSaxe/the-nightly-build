# Voice guide: feature/marvell-lumentum-optics (01)

## How this piece should sound

The register is a working engineer explaining to other engineers what a chip company bought and what the price assumes. The reader builds ML systems and knows what a cluster is, but may not know where a laser sits relative to a DSP, or how an all-stock exchange ratio turns into a multiple. Define the optics terms where they first appear and move on. Do not explain what a data center is.

The two semiconductor exemplars below handle a comparison the same way. Chester Lam (Chips and Cheese) states each side's number in the same sentence, so a reader holds both at once: 1024 branches against 128, 3 cycles against 4. He says what the number costs the design and gives the designer's likely reason, and marks it as a guess ("probably"). Where this piece sets Marvell's electrical parts against Lumentum's optical ones, or the implied price against Lumentum's reported revenue, put both figures side by side in the sentence and say what the difference means for the link or the multiple. Where the filings do not give a reason, say a reason is inferred.

Ben Thompson (Stratechery) explains a business through the physical economics under it: node cost, who has the volume, whose margin is whose. His paragraphs go from a cost to what that cost forces. That is the move for the question of what the price requires to be true. Start from what the target earns and grows, then say what the multiple needs on top of it. His passages are also a warning: he is arguing a position, and this piece reports what the filings support and attributes forecasts to the party making them.

Brian Potter (Construction Physics) shows how to run a computation in prose. He says what was assumed, gives the result with its units, and puts the limit of the simulation in the sentence after the result it limits. That matches the commission's rule to put a caveat where the claim sits and not in a closing roundup. Where the price-to-revenue computation leaves something out, such as a growth path or a share-price date, say so beside the figure.

The three writers are visible as people in small ways. Lam calls a design choice "baffling" and says he is giving the benefit of the doubt. Thompson says "you know what's coming!" to the reader. Potter writes "For reference" and hands the reader a second number to scale the first. Judgments are short and plain and sit next to the evidence for them. Nothing here needs a joke. Plain surprise at a number is enough when the number earns it.

Do not copy their dashes or stacked parentheses. The house punctuation rules apply.

The piece is short and built around drawings. Prose beside a figure says how to read it and what follows. A figure of one optical link does the work of a paragraph of description, so the prose can go straight to what the drawing cannot say: why a part sits where it does and what changes if it moves.

Note on sources: no free exemplar was found by a writer working on optical interconnect or on this deal, and paywalled pieces could not be read in full. The Potter piece is from energy, chosen for how it handles a computed comparison. Treat it as showing method and not subject vocabulary.

## Chester Lam, "Popping the Hood on Golden Cove"

Source: https://chipsandcheese.com/p/popping-the-hood-on-golden-cove

> "However, Zen 3 can still have a speed advantage in some cases. It can track up to 1024 branches and handle them back to back, with no lost cycles between them. Golden Cove can handle 128 branches with roughly 1-per-cycle throughput. That’s equivalent to Haswell’s ability, but is a regression compared to Sunny Cove. Intel probably made tradeoffs to get such a large BTB working above 5 GHz."

Checked: https://chipsandcheese.com/p/popping-the-hood-on-golden-cove, retrieved 2026-11-03
Both designs get a number in consecutive sentences, and a third reference point (Haswell, Sunny Cove) tells the reader whether 128 is good. The last sentence offers a reason and marks it with "probably". The writer gives a verdict on the design and does not claim to know the designer's intent.

> "This cache latency explains why Golden Cove needs larger out of order resources. Remember the “long latency instructions” mentioned earlier? The most common ones are simply memory accesses that miss cache. Let’s look at ROB size and memory access latency together, with a little application of Little’s Law. This law states that queue length is equal to arrival rate multiplied by latency. We’re going to apply this to instruction throughput, and use ROB size as queue length (assuming other queues are properly sized to prevent them from filling before the ROB)."

Checked: https://chipsandcheese.com/p/popping-the-hood-on-golden-cove, retrieved 2026-11-03
He recalls an earlier point of the article, states the law in one sentence, and says what he assumes in a parenthesis before using it. The vocabulary (ROB, long latency instructions) is used without gloss because the reader is a practitioner, while the one general result needed, Little's Law, is stated.

> "From our testing, it actually seems a bit smaller on Golden Cove. Intel probably didn’t shrink this important structure, so I’m giving them the benefit of the doubt. In any case, Intel’s decision to not equip Golden Cove with more integer registers is baffling."

Checked: https://chipsandcheese.com/p/popping-the-hood-on-golden-cove, retrieved 2026-11-03
The writer reports a measurement, doubts it, says he is giving the benefit of the doubt, and then gives a plain judgment. "I" appears where he is making a call, and the call is one short sentence.

## Ben Thompson, "Intel Problems"

Source: https://stratechery.com/2021/intel-problems/

> "The damage this did to the company went deeper than foregone profits; over the last two decades the cost of building ever smaller and more efficient processors has sky-rocketed into the billions of dollars. That means that companies investing in new node sizes must generate commensurately more revenue to pay off their investment. One excellent source of increased revenue for the industry has been billions of smartphones sold over the last decade; Intel, though, hasn’t seen any of that revenue, even as PC sales have flatlined for years."

Checked: https://stratechery.com/2021/intel-problems/, retrieved 2026-11-03
A cost is stated, then what it forces on a company, then which company lacks the revenue to meet it. Each sentence is a step the next depends on. The semiconductor economics are explained in ordinary words to a reader who is expected to follow the arithmetic.

> "The key thing to understand about chips is that design has much higher margins; Nvidia, for example, has gross margins between 60~65%, while TSMC, which makes Nvidia’s chips, has gross margins closer to 50%. Intel has, as I noted above, traditionally had margins closer to Nvidia, thanks to its integration, which is why Intel’s own chips will always be a priority for its manufacturing arm."

Checked: https://stratechery.com/2021/intel-problems/, retrieved 2026-11-03
The claim is given with two companies' margins as the instance, then the consequence for a third. The figures are ranges as the source gave them. The "as I noted above" shows a writer keeping the reader's place.

> "Yes, integrating design and manufacturing was the foundation of Intel’s moat for decades, but that integration has become a strait-jacket for both sides of the business. Intel’s designs are held back by the company’s struggles in manufacturing, while its manufacturing has an incentive problem."

Checked: https://stratechery.com/2021/intel-problems/, retrieved 2026-11-03
He grants the strength of the opposing view ("Yes, ...") in its own terms before stating the problem, and the problem is stated for each side separately. The metaphor "strait-jacket" is the only one, and it carries the claim that integration now constrains both halves.

## Brian Potter, "Can We Afford Large-Scale Solar PV?"

Source: https://www.construction-physics.com/p/can-we-afford-large-scale-solar-pv

> "We see here the exact same diminishing returns that we saw when simulating a single family home. Each additional watt of solar PV capacity and watt-hour of battery storage gets used less and less frequently, and contributes a smaller amount to meeting overall electricity demand. And as we approach 100% electricity demand, the infrastructure requirements become enormous to deal with the occasional long stretch of cloudy days and low panel output."

Checked: https://www.construction-physics.com/p/can-we-afford-large-scale-solar-pv, retrieved 2026-11-03
He tells the reader what the graph above shows, in units a reader can picture, and then carries the abstract pattern (diminishing returns) down to the concrete cause (a cloudy stretch). "We see" puts the writer and reader at the figure together.

> "Without gas turbine charging, our 160+gigawatt solar PV and 16-hour battery system still required over 27 gigawatts of gas turbine capacity to meet demand. With gas turbine charging, that falls to 8 gigawatts. And those turbines run a lot more often: the 27-gigawatt system only generated around 1.4 million megawatt hours, or less than 1% of total demand. The 8-gigawatt, battery-coupled system generated almost 10 times that. (For reference, California currently has about 39 gigawatts of gas turbine capacity, though this will be both combined cycle plants and simple cycle plants used for peaking.)"

Checked: https://www.construction-physics.com/p/can-we-afford-large-scale-solar-pv, retrieved 2026-11-03
Two cases are given with their figures in matching sentences, and the difference is stated as a ratio. The closing parenthesis puts a number the reader can hold next to the results, and says what that number does and does not include.

> "They also only look at costs, and not prices: what generators would actually charge, which could easily be much higher. (More generally, they ignore electricity market dynamics, which are very complex.) And they totally ignore the fact that in the real world states can share electricity, further damping demand peaks."

Checked: https://www.construction-physics.com/p/can-we-afford-large-scale-solar-pv, retrieved 2026-11-03
The limits are listed as specific things left out, each with its direction of effect. They are checkable ("states can share electricity") and not a general statement of humility. The writer states them plainly and moves to his takeaways.
