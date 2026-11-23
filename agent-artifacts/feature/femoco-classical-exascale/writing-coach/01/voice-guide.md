# Voice guide: feature/femoco-classical-exascale (01)

## How this piece should sound

This is a five-minute feature for readers who build systems and read papers, and who have never had to think about an active space. The register to hold is that of a colleague who ran the numbers and is walking you through the figure. Dan Luu's cache post is the closest model. He states what the table shows, says which cell surprised him, and says which comparison he could not make because the workloads differed. A reader trusts him because the limit sits in the same sentence as the result. The FeMoco comparison turns on exactly this kind of limit (same active space or not, same accuracy target or not), so state each caveat where the number it qualifies appears and in the words of the thing being compared. Luu's last passage below shows the plain form: "it's in the right ballpark, but it was characterized on a different workload using a different simulator."

The reader is treated as capable and unhurried. Colah never apologises for the difficulty and never talks down. He says the thing looks mysterious, says it is a familiar object seen differently, and shows the unrolled picture. Where this article has to introduce CAS(113e,76o), chemical accuracy or a fault-tolerant run, the model is to define the term in a clause at the point the figure needs it, in the practitioner's own vocabulary, and then use that one word from there on. Quanta's hash-table piece shows the move at its best: it takes "how full the table is", converts it into the number x researchers actually use, and gives two worked values (x of 100 is 99 percent full, x of 1,000 is 99.9 percent) before using it. A quantity the reader has never met can be handed over by an instance in that way.

The visuals carry the structure, so the prose around each one can be short and say how to read it. Luu and Colah both write directly beside a figure: Luu tells you which columns to compare and in which direction lower is better, and Colah tells you what the pink circles and yellow boxes are before he uses them. Do the same with each drawing or plot here, as far as the figure calls for it.

Rival positions are best reported the way Quanta reports Kuszmaul and Farach-Colton: each person speaks in a sentence or two of their own, with what they said and what they were sceptical about, before anyone disagrees. Where a researcher's reaction is plain and vivid, a short direct quote shows the dispute better than a summary. Where nobody quoted is available, leave the position out and do not paraphrase it into something sharper.

Wit, where it comes, comes from the material. Luu's "I admit I cheated and looked at some zoomed in plots" is a fact about his method that happens to be funny. A feature on a contested benchmark has room for perhaps one remark like that, and only if the sources supply it. The persona to avoid is any single writer's: Luu's first-person lab notebook and Colah's "we" are not this article's voice, and the person on the page here is a reporter checking a claim against its documents.

A figure stays beside the figure it is compared to. A projection or a time-to-solution is much easier to scale when the reader is given the thing it is being compared with in the same sentence, as Kuszmaul does with "around 100 different positions" for a table 99 percent full.

## Dan Luu, "Caches: LRU v. random"

Source: https://danluu.com/2choices-eviction/

> "Random and FIFO are both strictly worse than either LRU or 2-random. LRU and 2-random are pretty close, with LRU edging out 2-random for the smaller caches and 2-random edging out LRU for the larger caches."

Checked: https://danluu.com/2choices-eviction/ (raw HTML fetched with curl and read), retrieved 2026-11-23
Two sentences read off a table, each stating a ranking and then the exception to it. He uses the field's names (LRU, FIFO, 2-random) without glossing them, because the post defined them above. The person visible here is the one who looked at the numbers and reports them flatly.

> "A possible downside to this metric is that if we have some very low miss rates, those could dominate the mean since small fluctuations will have a large effect on the ratio, but we can look the distribution of results to see if that's the case."

Checked: https://danluu.com/2choices-eviction/ (raw HTML fetched with curl and read), retrieved 2026-11-23
He criticises his own choice of metric, says what the flaw would do, and says what he will look at next to test it. The sentence is long and holds together because each clause is a step in the check. The text as published reads "look the distribution", and it is quoted as written.

> "For any comp arch folks, from this data, I suspect that 2-random doesn't keep up with adaptive policies like DIP (although it might — it's in the right ballpark, but it was characterized on a different workload using a different simulator, so it's not 100% clear)."

Checked: https://danluu.com/2choices-eviction/ (raw HTML fetched with curl and read), retrieved 2026-11-23
He gives a guess, marks it as a guess with "I suspect", and then lists the specific reasons the comparison is not like for like. The uncertainty is a list of differences in workload and simulator, so a reader can see what would settle it.

## Christopher Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "These loops make recurrent neural networks seem kind of mysterious. However, if you think a bit more, it turns out that they aren’t all that different than a normal neural network. A recurrent neural network can be thought of as multiple copies of the same network, each passing a message to a successor. Consider what happens if we unroll the loop:"

Checked: https://colah.github.io/posts/2015-08-Understanding-LSTMs/ (raw HTML fetched with curl and read), retrieved 2026-11-23
He names the reader's likely unease, then replaces it with a plainer description of the same object and points straight at the picture. The vocabulary is ordinary and the technical term appears only once it is needed. The person is a teacher who has seen the confusion before.

> "In the above diagram, each line carries an entire vector, from the output of one node to the inputs of others. The pink circles represent pointwise operations, like vector addition, while the yellow boxes are learned neural network layers."

Checked: https://colah.github.io/posts/2015-08-Understanding-LSTMs/ (raw HTML fetched with curl and read), retrieved 2026-11-23
A legend written as prose, in the order the eye meets the shapes, with colour and shape each tied to one meaning. He tells the reader how to read the figure and nothing more about it.

> "Let’s go back to our example of a language model trying to predict the next word based on all the previous ones. In such a problem, the cell state might include the gender of the present subject, so that the correct pronouns can be used. When we see a new subject, we want to forget the gender of the old subject."

Checked: https://colah.github.io/posts/2015-08-Understanding-LSTMs/ (raw HTML fetched with curl and read), retrieved 2026-11-23
An abstract mechanism (cell state, forgetting) is tied to one concrete case, a pronoun and a changed subject, in three short plain sentences. The example is small enough that the reader can check it in their head.

## Quanta Magazine, "Undergraduate Upends a 40-Year-Old Data Science Conjecture"

Source: https://www.quantamagazine.org/undergraduate-upends-a-40-year-old-data-science-conjecture-20250210/

> "Martín Farach-Colton, a co-author of the “Tiny Pointers” paper and Krapivin’s former professor at Rutgers, was initially skeptical of Krapivin’s new design. Hash tables are among the most thoroughly studied data structures in all of computer science; the advance sounded too good to be true. But just to be sure, he asked a frequent collaborator (and a “Tiny Pointers” co-author), William Kuszmaul of Carnegie Mellon University, to check out his student’s invention. Kuszmaul had a different reaction."

Checked: https://www.quantamagazine.org/undergraduate-upends-a-40-year-old-data-science-conjecture-20250210/ (raw HTML fetched with curl and read), retrieved 2026-11-23
A claim that sounds too good is met with a named sceptic, a stated reason for scepticism, and a named person asked to check. Each person is placed by institution and relation in a clause. The writer reports the sceptical reaction before the person who disagreed with it.

> "Fullness can be described in terms of an overall percentage — this table is 50% full, that one’s 90% — but researchers often deal with much fuller tables. So instead, they may use a whole number, denoted by x, to specify how close the hash table is to 100% full. If x is 100, then the table is 99% full. If x is 1,000, the table is 99.9% full."

Checked: https://www.quantamagazine.org/undergraduate-upends-a-40-year-old-data-science-conjecture-20250210/ (raw HTML fetched with curl and read), retrieved 2026-11-23
A working unit is defined by why researchers use it, and then pinned with two worked values. A reader with a CS background can scale the quantity afterwards without being told the field's conventions.

> "Researchers have long known that for certain common hash tables, the expected time required to make the worst possible insertion — putting an item into, say, the last remaining open spot — is proportional to x. “If your hash table is 99% full,” Kuszmaul said, “it makes sense that you would have to look at around 100 different positions to find a free slot.”"

Checked: https://www.quantamagazine.org/undergraduate-upends-a-40-year-old-data-science-conjecture-20250210/ (raw HTML fetched with curl and read), retrieved 2026-11-23
The formal statement comes first and a researcher's plain sentence puts a figure the reader can hold beside it. The quote is chosen because it says something the writer's own sentence could not, which is how a practitioner would count it.
