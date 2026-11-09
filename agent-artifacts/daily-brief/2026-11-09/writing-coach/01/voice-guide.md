# Voice guide: daily-brief/2026-11-09

## How this piece should sound

This is a three-minute read for engineers and mathematicians who build machine learning systems. Write it in the register of a good wire correspondent: plain declarative sentences, the actor and the verb up front, and numbers given at the precision the source gives. Briggs and Stephens show the shape a news item can take in two or three sentences. The first states what changed, the next gives the measured figure with the source's own uncertainty attached, and a qualification arrives as a named person saying something specific. Their uncertainty is a stated fact ("considerable uncertainty around that estimate"), never a mood. Where an item's source leaves something open, say what is open in the same flat terms. Where the source settles the matter, end the item on the fact itself and not on a "says" sentence.

The Word of the Day is the one item allowed a little warmth. Quinion tells a word's history as a short piece of detective work: who used the word, who claims to have coined it, what the record actually shows, and where the record runs out. He corrects a published origin claim with a quoted witness, and he says plainly when the ultimate source is unknown. If today's word has a disputed or partial origin, that is how to tell it. Recent editions told their words through a quoted letter, so the story here should rest on a different kind of record. His one dry personal line ("You had best skip this item if you're eating") works because it is about the word itself. Any wit in this item should come from the word's own story in the same way.

The two technology items are for readers who could build the thing themselves. Willison names the mechanism exactly (the PEP, the tool, the command) and defines a term only where the jargon is genuinely ambiguous, in one sentence. Use the release's own vocabulary and state what it does in concrete terms. A capability claim that only the vendor has made should be credited to the vendor in the sentence that states it. These readers lose trust fast at puffery, so describe what shipped and leave the significance to them.

Across all six items, assume the reader arrived from a link and knows nothing of yesterday's edition. Introduce each person and body by what they are in a few words, as the BBC piece does with "the conservation charity People's Trust for Endangered Species (PTES)".

## Helen Briggs and Kate Stephens, "A glimmer of good news for Britain's sleepy dormouse" (BBC News)

Source: https://www.bbc.com/news/articles/c85ynn0p5k71o

> "The National Dormouse Monitoring Programme, led by the conservation charity People's Trust for Endangered Species (PTES), has been monitoring sites in England and Wales since 1998. It found that since 2000, dormouse numbers have fallen by almost 60%, equivalent to an average annual decline of 3.5%."

Checked: https://www.bbc.com/news/articles/c85ynn0p5k71o (raw HTML), retrieved 2026-11-09
The source is introduced by what it is and how long it has been measuring before any figure appears, so the number arrives with its authority attached. The second figure converts the first into a rate a reader can hold. The writers' care shows in "almost 60%": they keep the source's precision and do not round it into a cleaner claim.

> "More recently, however, there are signs that trend may be reversing. The data suggests the population increased by almost 10% between 2020 and 2025, although researchers stress there is considerable uncertainty around that estimate."

Checked: https://www.bbc.com/news/articles/c85ynn0p5k71o (raw HTML), retrieved 2026-11-09
The good news and its limits are in the same sentence, and the limit belongs to the researchers, not the reporters. The writers do not overstate the reversal, and they do not bury it under hedges either.

> "But he added: \"We mustn't lose sight of the bigger picture: populations remain almost 60% lower than they were in 2000.\""

Checked: https://www.bbc.com/news/articles/c85ynn0p5k71o (raw HTML), retrieved 2026-11-09
The counterweight comes from a named report co-author, and it carries a figure, not a general caution. The writers chose a quotation that does work in the piece. They did not pick one for its tone.

## Michael Quinion, "Snarge" (World Wide Words)

Source: https://www.worldwidewords.org/weirdwords/ww-sna1.htm

> "There are usually bits of mixed-up bird remains on the aircraft, such as blood, beaks, feathers, and flesh. This is snarge, a term widely known among US air-accident investigators. Analysing the remains can often tell its species."

Checked: https://www.worldwidewords.org/weirdwords/ww-sna1.htm (raw HTML), retrieved 2026-11-09
He defines the word by showing the thing first, in a concrete list, and naming it only afterwards. He also says who uses the word, which places it in a real community of speakers. The sentences are short and plain even though the subject is grotesque.

> "An article in the magazine Flying Safety in 2003 says that the term snarge was invented at the Lab. However, one of its researchers, Carla Dove, says they didn't but instead borrowed it from the experts who prepared bird specimens for the collections"

Checked: https://www.worldwidewords.org/weirdwords/ww-sna1.htm (raw HTML), retrieved 2026-11-09
The history is presented as two dated, named claims set against each other, and a person at the source corrects the printed account. Quinion reports the disagreement and lets the better witness settle it, without commenting on either side.

> "Its ultimate source is unknown. The only reference I can find to the word is in a 1925 British book, Soldier and Sailor Words and Phrases, by Edward Fraser and John Gibbons, in which they gloss it as \"any ugly or unpleasant person\"."

Checked: https://www.worldwidewords.org/weirdwords/ww-sna1.htm (raw HTML), retrieved 2026-11-09
He states the limit of the record in five words and then shows the earliest evidence with full bibliographic detail. The first person ("I can find") is the researcher reporting the extent of his own search, which is the only place he appears in the passage.

## Simon Willison, "Building Python tools with a one-shot prompt using uv run and Claude Projects"

Source: https://simonwillison.net/2024/Dec/19/one-shot-python-tools/

> "(In LLM jargon a “one-shot” prompt is a prompt that produces the complete desired result on the first attempt. Confusingly it also sometimes means a prompt that includes a single example of the desired output format. Here I’m using the first of those two definitions.)"

Checked: https://simonwillison.net/2024/Dec/19/one-shot-python-tools/ (raw HTML), retrieved 2026-11-09
He defines a term only because it is ambiguous, gives both meanings, and says which one he means. "Confusingly" is the one word of opinion, and it is a fair verdict on the jargon.

> "This is an example of inline script dependencies, a feature described in PEP 723 and implemented by uv run. Running the script causes uv to create a temporary virtual environment with those dependencies installed, a process that takes just a few milliseconds once the uv cache has been populated."

Checked: https://simonwillison.net/2024/Dec/19/one-shot-python-tools/ (raw HTML), retrieved 2026-11-09
The feature is named by its specification and by the tool that implements it, and then the mechanism is described in one sentence with the condition attached ("once the uv cache has been populated"). A practitioner could check every part of it.

> "The pattern here that’s most interesting to me is using custom instructions or system prompts to show LLMs how to implement new patterns that may not exist in their training data. uv run is less than a year old, but providing just a short example is enough to get the models to write code that takes advantage of its capabilities."

Checked: https://simonwillison.net/2024/Dec/19/one-shot-python-tools/ (raw HTML), retrieved 2026-11-09
He marks his judgment as his own ("most interesting to me") and then supports it with a fact about the tool's age. The claim is limited to what he observed.
