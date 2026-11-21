# Voice guide: daily-brief/2026-11-21 (01)

## How this piece should sound

This is a three-minute read for engineers and mathematicians who build machine learning systems and read the news like anyone else. Hold the register of a good wire desk with a dictionary editor's ear for words: plain declarative sentences, the exact noun, the figure where there is one, and an attribution that says who made the claim and in what document. Nobody is performing for the reader and nobody is lecturing. The reader is treated as someone who is smart, has not seen the story, and would like to be done in two or three sentences.

Each news and technology item has room for three sentences, so each sentence carries one job and there is no room for a windup. The Willison passage below shows the habit to look at: it opens by saying who did the work and what it does, quotes the contributor's own words where they are the most precise statement of the claim, and then gives the author's own observation in the first person and in the same flat tone, so a reader can tell the reporting from the judgment. Where an item turns on a claim somebody has not proven, the material may call for attributing it in the claimant's words, as Willison does with "99% of the code", and keeping the writer's own voice out of it.

Technical terms go in at the level the practitioner uses them. Willison writes "SIMD instructions" and "dot product functions" without a gloss, and the exact vocabulary is part of why he sounds like someone who works with the thing. For this audience, name the model, the library, the statute section or the dollar figure, and explain only what a reader outside that field could not infer.

The word story is the one place the piece may be playful. The Merriam-Webster passages are the model: a definition in one plain sentence, then a story told in short declaratives, with one dry turn where the word's own history supplies it ("someone calling you stolid would not be doing you a solid"). The joke works because it sits on the word's meaning and would be pointless on any other word. The story can begin anywhere the word allows. The hobbyhorse passage starts from the reader's own hobby and walks the senses of the word forward in order, and the stolid passage starts from how the word is used now and then reverses to what it used to mean. Either shows an opening that is not a dated scene. Where the word has a known coiner and a first-use citation, give the person and the document, as the meet-cute citation does, and leave it unembroidered. Three or four sentences cannot hold a second joke or a moral at the end.

Across the whole brief, let the items differ from one another in how they open and close. Six items shaped the same way read as a template however good each sentence is.

## Merriam-Webster, "Word of the Day: Stolid" (17 November 2026)

Source: https://www.merriam-webster.com/word-of-the-day/stolid-2026-11-17

> "Stolid describes someone or something that has or expresses little or no emotion."

Checked: https://www.merriam-webster.com/word-of-the-day/stolid-2026-11-17 (raw page, tags stripped), retrieved 2026-11-21
The definition is one sentence of ordinary words with no hedge and no etymology in it. The register is that of a dictionary editor who knows the reader came for the meaning.

> "Today, a person described as stolid may simply be someone who doesn't wear their feelings on their sleeve, who appears unemotional or uninterested in what is happening around them. Its use is usually descriptive, rather than disparaging. Once upon a time, however, someone calling you stolid would not be doing you a solid."

Checked: https://www.merriam-webster.com/word-of-the-day/stolid-2026-11-17 (raw page, tags stripped), retrieved 2026-11-21
The paragraph moves from present use to the word's earlier sting in three sentences, and the last one is a pun on the reader's own idiom. The editor is visible in the small joke and in the "however" that turns the sentence.

> "Stolid comes from the Latin adjective stolidus, meaning "dull" or "stupid." It is also distantly related to the word stultify, meaning "to cause to appear or be stupid, foolish, or absurdly illogical." The earliest examples of usage for stolid, which date back to the 17th century, indicate that it too was originally associated with a lack of smarts; it was used to describe people considered foolish for their relative impassivity."

Checked: https://www.merriam-webster.com/word-of-the-day/stolid-2026-11-17 (raw page, tags stripped), retrieved 2026-11-21
The sourcing is stated as sourcing: the Latin form, the cognate, then what the earliest citations show. The first-person authority of a lexicographer comes from the specific facts and not from adjectives.

## Merriam-Webster, "Word of the Day: Hobbyhorse" (18 November 2026)

Source: https://www.merriam-webster.com/word-of-the-day/hobbyhorse-2026-11-18

> "Hobbyhorse refers to a topic that someone dwells on, returning to again and again, especially in conversation."

Checked: https://www.merriam-webster.com/word-of-the-day/hobbyhorse-2026-11-18 (raw page, tags stripped), retrieved 2026-11-21
The definition uses the participial phrase "returning to again and again", which is itself the meaning acted out. It is a plain sentence a reader can repeat to someone else.

> "Does your favorite hobby involve a horse? Whether it does or not, the word hobby is undeniably equine: it's a shortening of the older term hobbyhorse."

Checked: https://www.merriam-webster.com/word-of-the-day/hobbyhorse-2026-11-18 (raw page, tags stripped), retrieved 2026-11-21
The story opens on something the reader already has, a hobby, and gives the surprising fact in the next breath. The one-word joke "equine" is anchored in the subject's own noun.

> "By the mid-1500s, hobby horse was being used to refer to a horse costume worn by a person participating in a morris dance or other performance, and then to a toy consisting of a stick with a toy horse's head at one end that a child pretends to ride. By the next century the literal horse was unneeded, and hobbyhorse could refer to a favorite pursuit or pastime—that is, our modern hobby."

Checked: https://www.merriam-webster.com/word-of-the-day/hobbyhorse-2026-11-18 (raw page, tags stripped), retrieved 2026-11-21
Each sense gets a date and a concrete object, a costume and then a stick with a horse's head, so the reader can follow the shift of meaning without being told it was a shift. The closing "that is, our modern hobby" returns to where the passage began.

## Simon Willison, "ggml : x2 speed for WASM by optimizing SIMD" (link post, 27 January 2025)

Source: https://simonwillison.net/2025/Jan/27/llamacpp-pr/

> "PR by Xuan-Son Nguyen for llama.cpp : This PR provides a big jump in speed for WASM by leveraging SIMD instructions for qX_K_q8_K and qX_0_q8_0 dot product functions."

Checked: https://simonwillison.net/2025/Jan/27/llamacpp-pr/ (raw page, tags stripped; link text spacing differs from the page), retrieved 2026-11-21
The opening names the contributor, the project, what the change does and the technical objects it touches, in one sentence. The vocabulary is a practitioner's and none of it is explained.

> "They shared their prompts here, which they ran directly through R1 on chat.deepseek.com - it spent 3-5 minutes "thinking" about each prompt."

Checked: https://simonwillison.net/2025/Jan/27/llamacpp-pr/ (raw page, tags stripped), retrieved 2026-11-21
He reports what the contributor did and a measured duration, with the scare quotes around "thinking" used once, on the term that earns them. The sentence is plain and states what a reader could go check.

> "(It thought about model_map a lot before finally deciding to eliminate it, which was also my preferred resolution.)"

Checked: https://simonwillison.net/2025/Jan/27/llamacpp-pr/ (raw page, tags stripped), retrieved 2026-11-21
This is the author stating his own position in a parenthetical, flat and short, after the quoted material has made its case. The person is visible as someone who has done the same task and says which result he preferred.
