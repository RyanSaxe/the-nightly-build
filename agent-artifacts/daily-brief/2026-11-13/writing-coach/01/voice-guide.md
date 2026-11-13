# Voice guide: daily-brief/2026-11-13

## How this piece should sound

A desk editor wrote this brief for engineers who build production ML systems and will read it in three minutes. The register is LWN's front-page summaries: each item names who did what, states the mechanism in the field's own terms, and stops. Look at how Corbet's user-namespaces item defines the term in one clause ("processes within a user namespace can appear to have full root access...") and then shows where it breaks. A news or technology item may need one clause like that for a term outside ML, and no more. This audience does not need a release, a ruling or a vote explained to it.

Where the material holds an exact number or a named actor, use it in the item. Clark's DeepMind passage carries the times, the counts and the agent's own name, and a reader can check every part of it. When a source's claim is still unverified, the attribution goes in the sentence ("the researchers write"), as in Clark's agent-wiki item. With two or three sentences per item, the third goes to what follows from the event: the next vote, the deadline, who has to act. If nothing follows yet, the item can end after two.

The word item is the only one with room for personality, and Quinion shows what kind. He gives the record: the earliest citation, the place, the year, the source that contradicts the received story. His dry turns are flat statements of fact or of doubt ("It's a surprisingly late coinage"; "The source must be some other word"). The joke, if there is one, belongs to the word's own history. Where the record stops, say that it stops, as he does with snarge. The definition and first use can carry a date and a named coiner, and a dated quotation is the evidence. Four sentences is enough for the story.

Nothing in the digest editorializes. Clark's "Why this matters" sections are commentary this series does not carry. What to take from him is the compression of the summary paragraphs above them.

## Michael Quinion, "Snarge" (World Wide Words)

Source: https://www.worldwidewords.org/weirdwords/ww-sna1.htm

> "There are usually bits of mixed-up bird remains on the aircraft, such as blood, beaks, feathers, and flesh. This is snarge, a term widely known among US air-accident investigators. Analysing the remains can often tell its species."

Checked: https://www.worldwidewords.org/weirdwords/ww-sna1.htm (raw HTML via curl), retrieved 2026-11-13
He sets out the physical thing in a concrete list before he names the word, and the name lands as a short declarative sentence. The writer is someone who knows which professional community uses the word and says so exactly ("US air-accident investigators"), not "experts".

> "Its ultimate source is unknown. The only reference I can find to the word is in a 1925 British book, Soldier and Sailor Words and Phrases, by Edward Fraser and John Gibbons, in which they gloss it as “any ugly or unpleasant person”."

Checked: same URL, retrieved 2026-11-13
He reports the limit of the record first, then the single dated citation he found, with title and authors. The first person ("I can find") belongs to a lexicographer reporting his own search, and it tells the reader how much the claim is worth.

> "We may reasonably describe the mess that’s left by a collision as both ugly and unpleasant, but a link between live persons and dead avians seems unlikely. The source must be some other word."

Checked: same URL, retrieved 2026-11-13
The humor comes from taking the 1925 gloss literally for one clause, and then he rejects it on the evidence. The dry line and the scholarly judgment are the same sentence.

## Michael Quinion, "Bootleg" (World Wide Words)

Source: https://www.worldwidewords.org/qa/qa-boo1.htm

> "It’s a surprisingly late coinage, first being recorded from Omaha, Nebraska in 1889 (with the related bootlegger being recorded in Oklahoma the same year). Prohibition gave it a huge boost, of course."

Checked: https://www.worldwidewords.org/qa/qa-boo1.htm (raw HTML via curl), retrieved 2026-11-13
The first answer is the date and the place of first record, with the word's judgment ("surprisingly late") built into the same sentence. "Of course" is a person talking, and it is used for the one thing every reader already knows.

> "Bootleg was at first a literal term. In the days when horsemen wore long boots, their bootlegs were good places to hide things."

Checked: same URL, retrieved 2026-11-13
Two plain sentences carry the whole literal sense, and the figurative step follows from it without being argued for. There is no hedging and no ornament.

## Jonathan Corbet and daroc (LWN.net bylines), LWN.net front-page summaries

Source: https://lwn.net/Articles/1103429/ and https://lwn.net/Articles/1103190/ (summaries as published on https://lwn.net/)

> "User namespaces are a key part of the kernel's toolkit for assembling containers; processes within a user namespace can appear to have full root access to the system while gaining no extra privileges in the wider system. At least, that is the intent. In practice, keeping privilege contained within a user namespace has often turned out to be difficult."

Checked: https://lwn.net/ (raw HTML via curl), retrieved 2026-11-13
Corbet defines the term for a reader who may not know it, in the language of the kernel, and then turns on a four-word sentence. The dryness is in "At least, that is the intent", which is a fact about the design stated flatly.

> "Unfortunately, the kernel does not have any way to know that the data it is reading back has not been tampered with, which is why lockdown, an optional kernel feature that attempts to prevent modifications to the running kernel, disables hibernation. Matthew Garrett, who has been working on lockdown for many years, has shared a patch set that aims to fix this problem."

Checked: https://lwn.net/ (raw HTML via curl), retrieved 2026-11-13
The problem is stated as a mechanism, and the next sentence names the person and the concrete artifact ("a patch set"). A reader gets the cause, the actor and the remedy in two sentences, with each technical term glossed in an appositive and not in a separate paragraph.

## Jack Clark, "Import AI 472"

Source: https://jack-clark.net/2026/09/07/import-ai-472-deepminds-cheating-math-agents-populist-ai-policies-and-forethought-theorizes-a-nightwatchman/

> "Google DeepMind has published a paper about how when setting up 100 agents to try and solve some math problems it observed a kind of flash crash whereby some agents learned to cheat, cheating suddenly propagated across others in the swarm, and other agents began to try to counter the cheaters (though lacking the tools to stop it)."

Checked: https://jack-clark.net/2026/09/07/import-ai-472-deepminds-cheating-math-agents-populist-ai-policies-and-forethought-theorizes-a-nightwatchman/ (raw HTML via curl), retrieved 2026-11-13
One sentence gives the actor, the setup and the result for an ML-literate reader, with no background on what an agent is. The choice of "flash crash" is a practitioner's comparison that a technical reader can picture straight away.

> "“The simulation started at 11:18 UTC with 100 autonomous agents collaborating to solve the shared 71 open problems. At 12:15 UTC, after the collective had correctly solved 37 out of the 71 problems, prover-theta discovered an exploit in the autograder system.”"

Checked: same URL, retrieved 2026-11-13
Clark quotes the paper directly at the point where the numbers matter, and does not paraphrase them. The figures are left to make the point.

> "“As part of the task, they were supposed to have the ability to read the internet but not to write on it. They found a way to use their read access to write information to an obscure German wiki,” the researchers write."

Checked: same URL, retrieved 2026-11-13
An unverified claim is attributed in the sentence that carries it. The quoted words state the mechanism, so the attribution does not need commentary added to it.
