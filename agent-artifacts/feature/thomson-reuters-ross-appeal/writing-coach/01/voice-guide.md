# Voice guide: feature/thomson-reuters-ross-appeal (01)

## How this piece should sound

This is a reader's report on one appellate opinion, written for people who are comfortable with a loss function and uncomfortable with "the court reasoned that." The register is that of Samuelson on the Kluwer Copyright Blog and Cooper and Grimmelmann in the Chicago-Kent Law Review: a person who has read the opinion closely tells you what it decided, in the opinion's own terms, and stops when the opinion stops. It is neither a law-review note, with its string cites and "arguably," nor a press release, with its "landmark."

The reader knows machine learning and has no reason to know what a headnote is, what the four fair-use factors are, or why "interlocutory" matters. Cooper and Grimmelmann show the move: they define the technical term in a few plain sentences (the classifier that outputs "cat" or "dog," as against the model that emits more of what it was trained on) and then use it as a working distinction for the rest of the piece. Define each legal term of art once, where the reader first needs it, in the vocabulary a practitioner would use, and then keep using that word. A synonym for "transformative" or "market harm" halfway through reads as a second concept, and a lawyer reviewing the piece will take it as one.

Separate what the court held from what it said along the way. Samuelson does this in running prose with no label: the Court "affirmed the Second Circuit only on the narrow issue" of one licence, "sidestepped" the dispute over the original creation, and the broader question "must await another case." Each of those states a limit as a fact about the opinion. Do the same for the Third Circuit where the opinion itself marks a limit on its holding, and quote the opinion's words at that point, since the line is the piece's subject. Where the opinion is silent, say it is silent, and say what a later court would have to decide. Where something is inference, name the person making the inference, you included, in a plain clause. A reader who sees a ruling described flatly will assume the writer checked it, so check it.

Treat ROSS's side the way Cooper and Grimmelmann treat OpenAI's: state the argument as its holders would recognise it ("On this view, ...") and carry it through to its consequence before answering it. Do this for the intermediate-copying argument and for whatever else the opinion records ROSS as arguing, in the form the opinion gives it. Lay out what the district court did on each factor in the same plain way, so a reader can see where the Third Circuit agreed and where it added something.

Report each point at the strength the opinion supports. Cooper and Grimmelmann close a long argument with a sentence that says exactly what has been shown and what has not ("Saying that regurgitation is copying says nothing about when regurgitation happens"). That sentence is a scope statement, and it is firm. Where the opinion shows the generative-AI question was not decided, say so in that voice, with no softening verb in front of it. Where it did decide something broad, say that just as flatly.

Prefer one concrete example to a paragraph of principle. Samuelson reaches for a movie made from a novel to show why "new meaning or message" cannot carry the whole transformative-use test, and the reader can run the case in their head. A single instance from the record, such as what a Westlaw headnote looks like next to the judicial passage it summarises, or what ROSS's tool returned for a query, does this work better than a restatement of the factor. Use the tool's actual inputs and outputs where the record gives them, and describe the system in terms an engineer would accept.

Case names and procedure get stated once, exactly, and then shortened the way lawyers shorten them. Quotation from the opinion is for the sentences where the court chose its words with care. Everywhere else, paraphrase accurately and cite the page. A piece of this length can hold a table of the factors if the comparison is easier to read as a grid. The prose around it should still say what the grid cannot.

Keep to the paper's slop rules. The subject supplies enough: "affirmed," "remanded," "summary judgment," "certified for interlocutory appeal." Words like "landmark," "watershed" or "sends a message" are what a reader who just saw the headline already expects, and none of them is a finding.

## Pamela Samuelson, "How to Distinguish Transformative Fair Uses From Infringing Derivative Works?"

Source: https://copyrightblog.kluweriplaw.com/2023/06/05/how-to-distinguish-transformative-fair-uses-from-infringing-derivative-works/

> "Many copyright professionals had hoped that the Court’s Goldsmith decision would articulate a workable standard for distinguishing transformative fair uses from infringing derivative works. Those hopes were largely dashed when the Court issued its decision in Andy Warhol Foundation for the Visual Arts, Inc. v. Goldsmith. The Court affirmed the Second Circuit only on the narrow issue of whether the Warhol Foundation (which controlled the rights to Andy Warhol’s works) had made a transformative use of Goldsmith’s photograph …"

Checked: https://copyrightblog.kluweriplaw.com/2023/06/05/how-to-distinguish-transformative-fair-uses-from-infringing-derivative-works/ (raw HTML via curl, tag-stripped), retrieved 2026-10-04. The ellipsis marks the rest of that sentence, which names the 2016 licence to Condé Nast; the words before it are consecutive in the source.
She says what the audience wanted from the case, says it did not get it, and then names the one narrow question the Court answered, all in the first three sentences. The parenthetical explains who the Foundation is without stopping the sentence. Her view is visible in "largely dashed," a plain report of how the field reacted.

> "The Court’s Goldsmith decision clarified that whether a second work has a “new meaning or message” may be relevant to whether a second comer’s use of a first work is fair, but on its own, it does not suffice. After all, many derivative works (say, a movie made from a novel) will add something new and convey some new meanings or messages. However, such uses must be licensed or be held unfair."

Checked: https://copyrightblog.kluweriplaw.com/2023/06/05/how-to-distinguish-transformative-fair-uses-from-infringing-derivative-works/ (raw HTML via curl, tag-stripped), retrieved 2026-10-04.
The first sentence states what the opinion established in two clauses: relevant, not sufficient. The next gives one everyday example that shows why. "After all" is the writer reasoning with the reader. The parenthetical "(say, a movie made from a novel)" is a person choosing an example.

> "What we know for sure is that a “new meaning or message” in secondary works is only relevant to, but not dispositive of, transformative purposes. In the aftermath of Goldsmith, courts will be asking putative fair users to justify each use of pre-existing works. The larger question of how courts should distinguish infringing derivatives from transformative fair uses must await another case to be definitively answered."

Checked: https://copyrightblog.kluweriplaw.com/2023/06/05/how-to-distinguish-transformative-fair-uses-from-infringing-derivative-works/ (raw HTML via curl, tag-stripped), retrieved 2026-10-04.
The last paragraph is a ledger: what is settled, what changes in practice, what is left open. She says the open question is open without apologising for it. The firm "what we know for sure" and the plain "must await another case" are in the same voice.

## A. Feder Cooper and James Grimmelmann, "The Files Are in the Computer: On Copyright, Memorization, and Generative AI"

Source: https://arxiv.org/abs/2404.12590 (published as 100 Chi.-Kent L. Rev. 141 (2025))

> "To the Times and its lawyers, these examples of “memorization” were blatant copyright infringement. But to OpenAI and its defenders, there was nothing to see here. OpenAI responded, both in court and online, casting the Times’s behavior as “adversarial” —that these examples were “misuse,” “not typical or allowed user activity.” On this view, any copying (and thus any resulting infringement) resulted from the prompts the Times used. If the Times had not specifically manipulated ChatGPT into generating Times articles, there would have been no copying, and no copyright infringement."

Checked: https://arxiv.org/pdf/2404.12590 (raw PDF via curl, text extracted with pdftotext), retrieved 2026-10-04. Footnote numbers in the PDF are omitted from the quotation.
Each side's position gets a sentence in terms its holders would accept, with their own words in quotation marks, before the authors say anything of their own. "On this view" hands the argument to the people who hold it and then follows it to its consequence. "Nothing to see here" is the one colloquial phrase, and it sits where a human would say it.

> "Second, these models are all generative: they produce outputs of the same modality as their training data. This second point is what distinguishes generative-AI models from other machine-learning (ML) models. A classifier (a type of discriminative model) will typically be trained on information-rich training examples, such as a collection of JPEG images of cats and dogs. When the trained classifier is used to perform inference on a new JPEG input, it will output either a simple label of cat or dog, based on whether it predicts that the JPEG is more likely to be an image of a cat or an image of a dog."

Checked: https://arxiv.org/pdf/2404.12590 (raw PDF via curl, text extracted with pdftotext), retrieved 2026-10-04. Footnote number omitted from the quotation.
A term is defined by contrast with its neighbour, using the engineers' own vocabulary (modality, classifier, discriminative, inference), and the example is small enough to see whole. Two lawyer-authors who work with ML researchers write as people who know both fields, and the register does not drop into explaining down.

> "All told, our first point in this Section is simply that regurgitation is copying in the sense with which copyright law is concerned. Indeed, this is precisely why copyright complaints in generative-AI cases emphasize regurgitation: it establishes a prima facie case of infringement. How often regurgitation occurs, and under what circumstances, is a factual, empirical question. It depends on the model in question and how it is prompted. Saying that regurgitation is copying says nothing about when regurgitation happens; we are saying only that when regurgitation does happen, it is copying."

Checked: https://arxiv.org/pdf/2404.12590 (raw PDF via curl, text extracted with pdftotext), retrieved 2026-10-04. Footnote number omitted from the quotation.
The claim is stated, given its legal consequence, and then bounded in a single closing sentence that says what was not claimed. The qualification is checkable, because it names which question remains empirical. The authors state the narrower claim firmly and do not hedge it.

## Peter Henderson, Xuechen Li, Dan Jurafsky, Tatsunori Hashimoto, Mark A. Lemley and Percy Liang, "Foundation Models and Fair Use"

Source: https://arxiv.org/abs/2303.15715

> "Alternatively, they can be used for non-generative purposes. These would typically output one value, rather than having a longer free-form output. For example, they might classify text in different ways, or predict a numerical value from an image."

Checked: https://arxiv.org/pdf/2303.15715 (raw PDF via curl, text extracted with pdftotext), retrieved 2026-10-04.
The sentences are short, and each carries one fact about what the system returns, which is the fact the legal question depends on. The unit of description is the output ("one value" versus "free-form output"), so the reader can tell which kind of system is under discussion without any legal vocabulary. This is how a machine-learning paper writes when a lawyer is a co-author.

> "Consider a generative foundation model trained on copyrighted books. In the extreme case if the model is trained on a book such that it can verbatim reproduce the entire book consistently (no matter what input is provided), then this is not transformative and could be problematic. Would this be any different than redistributing the book if you provide a mechanism to store and output the book? In the more common scenario, foundation models used for generative tasks will fall into a gray area where they produce some content that looks similar to the original training data and some content that looks substantially different."

Checked: https://arxiv.org/pdf/2303.15715 (raw PDF via curl, text extracted with pdftotext), retrieved 2026-10-04.
The passage goes from an extreme case to the ordinary one, so the reader sees where a clear answer ends and a gray area starts. The rhetorical question here is real: it tests the extreme case against a familiar act (redistributing a book). The authors say what the law does not yet cover ("a gray area") without padding it. The opening "Consider" works in this paper as a worked-example cue. It is the paper's habit, so do not copy it as a tic into a feature.
