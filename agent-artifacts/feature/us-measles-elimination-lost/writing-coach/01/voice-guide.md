# Voice guide: feature/us-measles-elimination-lost (01)

## How this piece should sound

This is a genomic-epidemiology explainer for readers who build ML systems and are comfortable with graphs, inference and uncertainty, but who have never read an outbreak line list. It should sound like a field practitioner talking to a peer from another field: calm and exact. The tone stays plain however large the news is. Bedford and Branswell both state alarming findings in level sentences and let the dates and the sequence evidence carry the weight. The loss of elimination status is a verdict about one transmission chain, and the prose can treat it as that, not as a moment.

Where the piece explains how a chain is linked, Bedford's method is the model to study: he names the unit (a mutation, a serial interval), shows a toy example, then says what the real data showed and how strong that inference is. This audience will want to know what kind of evidence joins two outbreaks: a shared genotype D8 sequence identifier, a dated epidemiologic link, or an analyst's inference. The piece can grade each link the way Bedford grades his 2/59 coincidence ("not quite conclusive evidence, but still strong evidence"), stated as his own judgment and with the number under it.

Branswell and Mallapaty show how to report what the investigators do not know without hedging the whole piece. They attribute each uncertainty to a named person and say what is missing: the collection dates, the direction of spread, the share of cases sampled. Where the CDC, a state health department or PAHO says a link is unresolved, the piece can say so in that body's words, with the named official, and keep what is established in plain declaratives beside it. Branswell also defines a term of art once ("VDPVs in polio parlance") and then uses it. The piece can treat "genotype", "lineage", "endemic transmission" and "12 months" the same way: define each where it first appears, then hold the word fixed.

The brief decides two things the exemplars cannot. Five minutes and a visual per section leave no room for the long quotations Mallapaty strings together, so a quoted person speaks only where nobody else could say the line. And the timeline is the finding, so the prose around it can read like Bedford's commentary on his tree: what to look at, in what order, and what it supports.

## Trevor Bedford, "Cryptic transmission of novel coronavirus revealed by genomic epidemiology"

Source: https://bedford.io/blog/ncov-cryptic-transmission/

> "Each person’s coronavirus infection will yield a sequence of 30,000 ‘A’, ‘T’, ‘G’ or ‘C’ letters. We can use these sequences to reconstruct which infection is connected to which infection. As an example, if we sequenced three of these infections and found:"

Checked: https://bedford.io/blog/ncov-cryptic-transmission/ (raw HTML via curl), retrieved 2026-11-15
He gives the size of the data and what it is used for in two short sentences, then goes straight to a toy case. The scientist explaining his own lab's method is visible in the "we" and in "As an example", which is how someone at a whiteboard talks.

> "The WA2 case was identical to WA1 except that it had three additional mutations. This tree structure is consistent with WA2 being a direct descendent of WA1. If this virus arrived in Snohomish County in mid-January with the WA1 traveler from Wuhan and circulated locally for 5 weeks, we’d expect exactly this pattern, where the WA2 genome is a copy of the WA1 genome except it has some mutations that have arisen over the 5 weeks that separate them."

Checked: https://bedford.io/blog/ncov-cryptic-transmission/ (raw HTML via curl), retrieved 2026-11-15
The observation comes first and the hypothesis is stated as a prediction it would have to match. "Consistent with" is chosen deliberately: he claims fit, not proof, and the dates are given so the reader can check the arithmetic.

> "Given this low frequency, we’d expect probability of WA2 randomly having the same genetic variant at 2/59 = 3%. To me, this not quite conclusive evidence, but still strong evidence that WA2 is a direct descendent of WA1."

Checked: https://bedford.io/blog/ncov-cryptic-transmission/ (raw HTML via curl), retrieved 2026-11-15
He shows the calculation and then owns the judgment with "To me". The strength of the evidence is graded in words that match the number, and the slightly rough grammar shows a person writing fast during an outbreak.

## Helen Branswell, "U.S. polio case tied to viruses detected in U.K., Israel, suggesting silent spread"

Source: https://www.statnews.com/2022/07/29/u-s-polio-case-tied-to-viruses-detected-in-u-k-israel-suggesting-silent-spread/

> "The case, an unvaccinated man in his 20s who lives in Rockland County, N.Y., recently developed paralysis that was diagnosed as having been caused by a type 2 polio vaccine virus. Health authorities in Rockland County, which is north of New York City, said the man had not traveled outside the country in the time when he would have been infected. That means someone else had to have brought the viruses into the country."

Checked: same URL (raw HTML via curl), retrieved 2026-11-15
Two sourced facts, then a short sentence of her own that draws the necessary inference from them. The reporter who has covered polio for years is visible in how little she needs to say to get from the travel history to the conclusion.

> "Israel uses both OPV and IPV. But the version of the oral vaccine it uses does not include type 2 viruses, which means this chain of transmission began in yet another, currently unidentified country."

Checked: same URL (raw HTML via curl), retrieved 2026-11-15
She reasons from a fact about vaccine composition to where a chain could not have begun. "Currently unidentified" marks the limit of knowledge in two words, without hedging the inference itself.

> "“Clearly they’re linked. It’s hard to infer directionality, especially when you only have a small number of sequences,” he said."

Checked: same URL (raw HTML via curl), retrieved 2026-11-15
The quotation she chose from the CDC branch chief separates what is established from what is not in two sentences. She lets the named official state the limit, so the uncertainty belongs to a source and not to the prose.

## Smriti Mallapaty, "Bird flu virus has been spreading in U.S. cows for months, RNA reveals" (Nature, reproduced in Scientific American)

Source: https://www.scientificamerican.com/article/bird-flu-virus-has-been-spreading-in-u-s-cows-for-months/

> "A strain of highly pathogenic avian influenza has been silently spreading in US cattle for months, according to preliminary analysis of genomic data. The outbreak is likely to have begun when the virus jumped from an infected bird into a cow, probably around late December or early January."

Checked: same URL (raw HTML via curl), retrieved 2026-11-15
The lede states the finding and its basis in one sentence, then dates the start of the chain with exactly the confidence the analysis carries ("likely", "probably around"). Her care shows in "preliminary", placed where a careless reporter would drop it.

> "That’s only one of many data gaps. Scientists lack information about each sample’s precise collection date and the state where it was collected. Such gaps are “very abnormal,” Nelson says."

Checked: same URL (raw HTML via curl), retrieved 2026-11-15
She names exactly which metadata are missing, the two fields a timeline needs, instead of saying "data are limited". The short first sentence moves the section forward from the previous caveat with no throat-clearing.

> "One possibility is that the person was infected by a separate viral lineage, which infected cattle that have not been swabbed. Another less likely scenario, which can’t be ruled out, says Nelson, is that the person was infected directly from a wild bird."

Checked: same URL (raw HTML via curl), retrieved 2026-11-15
Competing explanations are laid out side by side and ranked, and the ranking is attributed. A reporter who understands the phylogenetics is visible in "separate viral lineage" used without apology to a general reader.
