# Voice guide: feature/sunday-ticket-damages (01)

## How this piece should sound

This is a five-minute feature for readers who can check arithmetic faster than
they can parse a disposition line. The register is a practitioner talking to
another practitioner in a different field: direct, a little dry, sure of the
numbers. The reader is trusted to follow a calculation and is not trusted to
know what "vacate and remand" or "exclusion of an expert" means, so legal terms
get a working definition in the sentence that uses them and then stay fixed.

Say what the Ninth Circuit did before saying how it got there. Kerr gives the
vote, the author, the joiner and the dissenter in two sentences and moves on;
the panel, the disposition on each issue and any separate opinion can arrive
the same way, without a preamble about the case's long history. Where the
opinion's own words carry the holding, quote the opinion, as Kerr does, and let
the commentary come after it.

The damages arithmetic is where this audience will lean in, and the exemplars
show two ways to hold them. Miller sets the wrong formula next to a concrete
counter-example with real-looking counts, so the reader sees the failure before
being told the name of the fix. Vladeck names which part of a fraction everyone
has been arguing about and which part they forgot, then runs the numbers with
the assumptions labelled as his. If the record supports it, the per-subscriber
quantity, list price, average paid and a modelled competitive price, can be
shown the same way: each term named, what it measures stated, and the gap
between what was multiplied and what should have been made visible in one
figure. Label which numbers are the record's and which are illustrative.

When the piece turns to the reinstated models and the NFL's position, give the
strongest version first, as Vladeck does with Judge Bumatay, in that side's
words, then say where it stops holding. Kerr's "medium-important" shows that a
plain, scaled verdict on what the ruling changes is allowed; reach one where the
opinion and the remand posture support it, and say what is still open where
they do not.

Keep the person on the page in small first-person judgments and in the choice of
example, not in jokes. Miller's "Say what:" and Vladeck's "work with me" are
asides that cost one clause each; an aside of that size fits a feature, a
running bit does not.

## Evan Miller, "How Not To Sort By Average Rating"

Source: https://www.evanmiller.org/how-not-to-sort-by-average-rating.html

> "WRONG SOLUTION #1: Score = (Positive ratings) − (Negative ratings)
> Why it is wrong: Suppose one item has 600 positive ratings and 400 negative ratings: 60% positive. Suppose item two has 5,500 positive ratings and 4,500 negative ratings: 55% positive. This algorithm puts item two (score = 1000, but only 55% positive) above item one (score = 200, and 60% positive). WRONG."

Checked: https://www.evanmiller.org/how-not-to-sort-by-average-rating.html (raw HTML via curl), retrieved 2026-11-05
The formula is stated, then broken with two specific items whose numbers the
reader can verify in their head. Miller does not argue that the formula is
wrong; he computes the case where it ranks the worse item higher. The capital
"WRONG." is a programmer's voice, blunt and a little impatient.

> "Say what: We need to balance the proportion of positive ratings with the uncertainty of a small number of observations. Fortunately, the math for this was worked out in 1927 by Edwin B. Wilson. What we want to ask is: Given the ratings I have, there is a 95% chance that the “real” fraction of positive ratings is at least what? Wilson gives the answer."

Checked: https://www.evanmiller.org/how-not-to-sort-by-average-rating.html (raw HTML via curl), retrieved 2026-11-05
Before any formula, he restates what quantity the score should measure as a
plain question. The reader knows what the right answer is for before seeing how
it is computed. "Say what:" anticipates the reader's reaction in two words.

## Orin Kerr, "Accessing Google Location History Records Is Not a Search — At Least When Limited — Fourth Circuit Rules"

Source: https://reason.com/volokh/2024/07/10/accessing-google-location-history-records-is-not-a-search-at-least-when-limited-fourth-circuit-rules/

> "In the new ruling, the Fourth Circuit rules 2-1 that no search occurred. Judge Jay Richardson wrote the majority opinion, and he was joined by Judge Harvie Wilkinson, Judge James Wynn dissented."

Checked: https://reason.com/?p=8288617 (raw HTML via curl; canonical URL above), retrieved 2026-11-05
Holding, vote, author, joiner and dissenter in two sentences. There is no
recital of procedural history before the result. A law professor who has read
hundreds of these opinions writes this as routine, which tells the reader the
facts of the ruling are settled and the interesting part comes next.

> "According to Judge Richardson, this does not mean that access to Google location history records is categorically outside the Fourth Amendment.  That is true because Fourth Circuit precedent has adopted the so-called mosaic theory, the idea that whether and when Carpenter kicks in and calls data collection a search depends on how much data collection has occurred.  This warrant asked for only a brief period of records, just a two-hour span, and the majority concludes that was not enough to trigger a mosaic:"

Checked: https://reason.com/?p=8288617, retrieved 2026-11-05
He defines a doctrine in one appositive clause ("the idea that ...") and then
applies it to the case's one concrete number, the two-hour span. The limit on
the holding is stated as plainly as the holding. "Kicks in" is a working
lawyer's phrase, not a textbook's.

> "I think Chatrie is medium-important.  Its importance lies in it being a key reminder that not all location data is protected under the Fourth Amendment after Carpenter.  As I wrote back in 2022, it was puzzling that a lot of lower courts did not want to address this; they wanted to jump straight to how broad warrants could extend over these kind of records.  Chatrie is a key reminder that there's an earlier step.  The collection of location records may not be a search at all."

Checked: https://reason.com/?p=8288617, retrieved 2026-11-05
The verdict on significance is scaled, not inflated: "medium-important" is a
judgment a reader can disagree with. He then names exactly which step of the
analysis the ruling restores. The first person is used for a view he has held
and can point to.

## Steve Vladeck, "260. Elections and the Base Rate Fallacy"

Source: https://www.stevevladeck.com/p/260-elections-and-the-base-rate-fallacy

> "Fights about election “integrity” are, in an important sense, fights about a fraction. We spend almost all of our time arguing about the top half of it. It seems worth taking a minute to talk about the bottom half, too."

Checked: https://www.stevevladeck.com/api/v1/posts/260-elections-and-the-base-rate-fallacy (raw post body), retrieved 2026-11-05
A legal dispute is restated as an arithmetic object, and the sentence says which
part of it has been ignored. The words are plain: "top half", "bottom half",
not "numerator" yet. The voice is a law professor who expects his readers to
find a fraction easier than a statute.

> "Here’s a deliberately simple illustration, using my numbers rather than anyone’s findings: California has about 23 million registered voters. At Georgia’s rate of roughly one noncitizen per 410,000 registered voters, you’d expect something like 56 noncitizens on the rolls. Now assume that DHS has a screening tool with a false-positive rate of just 0.1 percent (I am very skeptical that such a precise tool exists, but work with me). Run across 23 million records, it would flag about 23,000 citizens."

Checked: https://www.stevevladeck.com/api/v1/posts/260-elections-and-the-base-rate-fallacy, retrieved 2026-11-05
He labels the numbers as his own before using them, then steps through the
calculation one multiplication per sentence. The parenthesis states his doubt
about his own assumption and asks the reader to continue anyway, which is where
the person shows.

> "That’s certainly the strongest version of the government’s case. But it rests on an unspoken (and deeply contestable) assumption on which the entire argument depends. When two sets of records disagree about the same person, someone has to bear the risk that the government is wrong, and Bumatay puts that risk on the voter."

Checked: https://www.stevevladeck.com/api/v1/posts/260-elections-and-the-base-rate-fallacy, retrieved 2026-11-05
He concedes the opposing judge's best argument by name before taking it apart,
and the objection is a concrete question of who bears an error, not a
characterization of the judge. The disagreement is located in one assumption
the reader can inspect.
