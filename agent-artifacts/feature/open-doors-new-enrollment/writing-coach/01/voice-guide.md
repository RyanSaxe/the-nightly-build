# Voice guide: feature/open-doors-new-enrollment (01)

## How this piece should sound

This is a data explainer for readers who build and evaluate models for a living. They know what a sum of components is and what a lag is. They do not know the series, the agency that publishes it, or the vocabulary of the people who argue about it. The register is a competent colleague showing a table and saying what is in it. It is plain, specific and a little dry, and it assumes the reader will check the arithmetic.

Dan Luu's Ballmer passages show how to carry a claim about a total: set the disputed figure against a comparison the reader already holds, name the test that would settle it, and apply it. His number is placed between two named things so it can be scaled. Where this piece has a total and parts, the same move may apply: say which part moved, by how much, and what the reader should compare it with. The dryness in his last sentences comes after the figures and depends on them.

Julia Evans's buffering post explains a lag as a mechanism: a quantity builds up to a threshold before anything is passed on, and the reader is shown the earlier wrong model, the cause and the number. If the material includes cohorts entering a stock and leaving it years later, her order of old guess, then mechanism, then size may suit it, and so may her habit of marking where a rule stops holding. She writes "I can't think of any program that behaves that way" where she could have written nothing. Qualifications in this piece can be that kind: what the writer did not find, said in the writer's own words.

Dynomight shows what to do when the numbers come from somebody else's series. He says what he did to the published figures, what the result suggests, how far to trust it and for what reason, and whether a second source agrees. A reader trained in mathematics can take a formula with its symbols defined in the sentence, so an expression may stand where a paragraph would otherwise paraphrase it. Jokes in these passages are at the writer's own expense or on a long list the reader has also faced, and never at the people whose data it is.

From the brief and the audience: the commission's subject sits close to higher-education advocacy and immigration politics, and none of the three exemplars uses that vocabulary. The piece may name what the series counts, define each category once where it first appears, and use that word for that category throughout. Where a source gives a reason for a change, the sentence can say whose reason it is and stop. A reader who cannot tell from a sentence which instrument produced a figure has been given less than the figure.

Three exemplars are about other subjects (a company's revenue, a terminal pipe, air particulates) and none carries a finding about this one. What they have in common is that every sentence has something checkable in it and the writer is audible in the choice of what to say next.

## Dan Luu, "Steve Ballmer was an underrated CEO"

Source: https://danluu.com/ballmer/

> "When people point to a long list of failures like Bing, Zune, Windows Phone, and HoloLens as evidence that Ballmer was some kind of buffoon who was holding Microsoft back, this demonstrates a lack of understanding of the tech industry. This is like pointing to a list of failed companies a VC has funded as evidence the VC doesn't know what they're doing. But that's silly in a hits based industry like venture capital. If you want to claim the VC is bad, you need to point out poor total return or a lack of big successes, which would imply poor total return."

Checked: https://danluu.com/ballmer/ (raw HTML fetched with curl and stripped to text), retrieved 2026-11-22
He sets the claim against a comparison the reader already holds (a VC's failed investments), then states the test that would settle it, poor total return. The vocabulary is the field's own and the sentences are plain. The person is visible in the flat, slightly impatient "But that's silly".

> "Even Bing, widely considered a failure, on last reported revenue and current P/E ratio, would be 12th most valuable tech company in the world, between Tencent and ASML. When attacking Ballmer, people cite Bing as a failure that occurred on Ballmer's watch, which tells you something about the degree of success Ballmer had. Most companies would love to have their successes be as successful as Bing, let alone their failures."

Checked: https://danluu.com/ballmer/ (raw HTML fetched with curl and stripped to text), retrieved 2026-11-22
A figure is placed between two named companies so a reader can scale it, and the inference drawn from it is stated in one sentence. The dry turn in the last sentence is where he is audible. It comes after the numbers and depends on them.

## Julia Evans, "Why pipes sometimes get "stuck": buffering"

Source: https://jvns.ca/blog/2024/11/29/why-pipes-get-stuck-buffering/

> "If log lines are being added to the file relatively slowly, the result I’d see is… nothing! It doesn’t matter if there were matches in the log file or not, there just wouldn’t be any output.
>
> I internalized this as “uh, I guess pipes just get stuck sometimes and don’t show me the output, that’s weird”, and I’d handle it by just running grep thing1 /some/log/file | grep thing2 instead, which would work."

Checked: https://jvns.ca/blog/2024/11/29/why-pipes-get-stuck-buffering/ (raw HTML fetched with curl and stripped to text), retrieved 2026-11-22
She reports her own earlier wrong model in her own words, so the reader sees what the confusion looked like before the explanation arrives. The exact command is on the page, in the vocabulary of someone who uses it daily. The person is visible in the quoted "uh, I guess".

> "The reason why “pipes get stuck” sometimes is that it’s VERY common for programs to buffer their output before writing it to a pipe or file. So the pipe is working fine, the problem is that the program never even wrote the data to the pipe!
>
> This is for performance reasons: writing all output immediately as soon as you can uses more system calls, so it’s more efficient to save up data until you have 8KB or so of data to write (or until the program exits) and THEN write it to the pipe."

Checked: https://jvns.ca/blog/2024/11/29/why-pipes-get-stuck-buffering/ (raw HTML fetched with curl and stripped to text), retrieved 2026-11-22
The mechanism is a quantity that accumulates to a threshold before anything passes through, which is the shape of a lag. She gives the mechanism, the number (8KB) and the reason in three plain sentences. The capitals on VERY and THEN are emphasis she would put in speech.

> "(as an aside: “programs do not use 8KB output buffers when writing to a terminal” isn’t, like, a law of terminal physics, a program COULD use an 8KB buffer when writing output to a terminal if it wanted, it would just be extremely weird if it did that, I can’t think of any program that behaves that way)"

Checked: https://jvns.ca/blog/2024/11/29/why-pipes-get-stuck-buffering/ (raw HTML fetched with curl and stripped to text), retrieved 2026-11-22
She marks the limit of a rule she just stated: a convention, not a necessity. The casual "like" and the admission that she cannot think of a counterexample keep the claim at the size she can support.

## Dynomight, "Better air quality is the easiest way not to die"

Source: https://dynomight.net/air/

> "It’s hard to prioritize health advice. I’m told I should limit salt and eat cruciferous vegetables and do cardio and sleep well and limit alcohol and reduce stress and go for regular checkups. But how much does each of these matter? If you’re a fallible hairless ape, what should you do first?
>
> To answer this, we need numbers."

Checked: https://dynomight.net/air/ (raw HTML fetched with curl and stripped to text), retrieved 2026-11-22
The reader's position is put as a list long enough to be funny, and the question it raises is answered by the next sentence, which says what is needed. Short sentences and a joke at the writer's own species, not at the reader.

> "I took their estimates and multiplied them by the WHO’s life expectancy figures to get an estimate of the total DALYs a person loses over a lifetime. Here we compare these to particle levels.
>
> The straight line shows a fit. It suggests that if you are exposed to 33.3 PM2.5 for your whole life, you’ll lose around 1 DALY as a result. I wouldn’t put too much faith in this exact number. It varies from country to country, and this is all built upon some very tricky observational statistics. Still, the estimate is reassuringly close the the number from the 2013 paper."

Checked: https://dynomight.net/air/ (raw HTML fetched with curl and stripped to text), retrieved 2026-11-22
He says what he did to the published series, in the first person, then what the fit suggests, then how far to trust it and why (it varies by country, the statistics are observational), then a second source that agrees. The doubt names its cause. His wording of the check is the person on the page.

> "Put another way, if you breathe particles at a concentration of 2500, you double the speed at which you move towards your (disability-adjusted) destiny. If you’re exposed to a level of x for h hours, then you lose h × (x / 2500) hours."

Checked: https://dynomight.net/air/ (raw HTML fetched with curl and stripped to text), retrieved 2026-11-22
A rate is restated in plain terms and then as a formula with every symbol defined in the sentence. A reader trained in mathematics gets the expression without a gloss on what an expression is, and the first sentence is still readable without it.
