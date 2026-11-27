# Voice guide: feature/microsoft-365-gateway-cascade (01)

## How this piece should sound

The register is that of an engineer explaining to colleagues how a system failed, and the reader is one of them: a computer science degree, production ML experience, no need for a definition of a lock or a failover. Say what a component does in one clause and move on, as Luu does in the cache passage below, where the whole architecture of a cache is a single sentence. Plain declaratives, the subject's own vocabulary (gateway, failover, admission control, lock contention, region), and numbers stated as figures. The tone is level. Nobody in these pieces is shocked by the failure or praises the people who fixed it.

The Cloudflare passages show a way to explain a mechanism: pick a case small enough to count, then walk through it step by step in sentences that each say what happened next. The line "You can see what's coming" is the one place the writer steps out and addresses the reader, and it is there because the reader has by then seen the pattern. Where this piece has a loop (one state leading to the next and then back), this is the model for how to walk it in prose around the drawing. Let a sentence run through one stage and stop. The drawing carries the whole loop. Say how to read it.

The AWS passages show how to keep a sequence of events straight when several things happen at once: name each actor, say what each was doing at that moment, and say which assumption had gone stale. The Luu death-spiral line shows that an arrow chain inside a parenthesis is acceptable when each term is a quantity. Use that where the material is a chain of quantities, and not for decoration.

Keep what an organisation states separate from what the piece infers, in the manner of the Cloudflare writer, who says who saw what and when ("Another team member used strace to confirm"). Attribution in these pieces is specific and short. The person on the page is whoever is doing the reasoning: a writer who says "this is what I would count" or "here is why that matters". They are not performing humility or alarm. A short aside that corrects a likely misreading, as in the first Cloudflare passage, is worth making where a reader would otherwise take the wrong cause away. Do not manufacture a misreading to correct.

At five minutes and a word band of 600 to 1200, there is room for a few of these moves, not all of them. Pick the passage that matches what the section has to do: define a part (Luu), walk a state change (Cloudflare), or order simultaneous events (AWS).

## Dan Luu and Yao Yue, "A decade of major cache incidents at Twitter"

Source: https://danluu.com/cache-incidents/

> "Conceptually, a cache server is a high-throughput, low-latency RPC server plus a library that manages data, such as memory and/or disk and key value indices. For in memory caches, the data management side should be able to easily outpace the RPC side"

Checked: https://danluu.com/cache-incidents/, retrieved 2026-11-27
One sentence defines a cache server as an RPC server plus a data library, and the next sentence says what that implies for where it can be slow. The vocabulary is a practitioner's (QPS per core, RPC stack), and nothing is explained that the audience already knows. The authors use a number to scale a claim (millions of QPS per core against a tenth of that) and keep to one noun for the thing.

> "Cache failure modes are also interesting because, when cache is used to serve a significant fraction of requests or fraction of data, cache outages or even degradation can easily cause a total outage because an architecture designed with cache performance in mind will not (and should not) have backing DB store performance that's sufficient to keep the site up."

Checked: https://danluu.com/cache-incidents/, retrieved 2026-11-27
The sentence states a condition, then the consequence, then the design reasoning behind it, and the parenthetical "(and should not)" is the authors' own judgment placed where it applies. It is one long sentence that stays readable because each clause follows from the one before.

> "Increased cache latency along with the design of tweet service using cache caused shards of the service using cache to enter a GC death spiral (more latency -> more outstanding requests -> more GC pressure -> more load on the shard -> more latency), which then caused increased load on remaining shards."

Checked: https://danluu.com/cache-incidents/, retrieved 2026-11-27
The loop is written as a chain of quantities with arrows in a parenthesis, then the plain-sentence consequence follows. Each term in the chain is a measurable thing (latency, outstanding requests, GC pressure, load), so the reader can check that the chain closes. This passage is about a different system and supplies no finding for this piece. Take only the way a feedback chain is laid out.

## John Graham-Cumming, "Details of the Cloudflare outage on July 2, 2019"

Source: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/

> "Although the regular expression itself is of interest to many people (and is discussed more below), the real story of how the Cloudflare service went down for 27 minutes is much more complex than “a regular expression went bad”."

Checked: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/, retrieved 2026-11-27
The writer says up front that the obvious one-line cause is not the full story, in a parenthesis that names the two places the reader will find the detail. The sentence commits to a figure (27 minutes) and to a claim, and the first person is present in the post in the plural and singular ("we", later "my watch").

> "The Performance Team pulled live CPU data from a machine that clearly showed the WAF was responsible. Another team member used strace to confirm. Another team saw error logs indicating the WAF was in trouble."

Checked: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/, retrieved 2026-11-27
Three short sentences, each naming a different team and a different instrument (live CPU data, strace, error logs) that pointed at the same component. Attribution is concrete: who looked at what. The repetition of "Another team" is deliberate, since three independent confirmations is the point.

> "This time the first .* matches just the first x. But the second .* acts greedily and matches =x. You can see what’s coming."

Checked: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/, retrieved 2026-11-27
After a worked example small enough to count, the writer steps in with one short sentence to the reader and goes on with the next step. It works because the earlier steps have already shown the pattern. The explanation uses the real strings and the real steps, with no analogy in place of them.

## Amazon Web Services, "Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (us-east-1) Region"

Source: https://aws.amazon.com/message/101925/

> "At the same time that this clean-up process was invoked, the first Enactor (which had been unusually delayed) applied its much older plan to the regional DDB endpoint, overwriting the newer plan. The check that was made at the start of the plan application process, which ensures that the plan is newer than the previously applied plan, was stale by this time due to the unusually high delays in Enactor processing."

Checked: https://aws.amazon.com/message/101925/, retrieved 2026-11-27
Two actors are doing two things at once, and the sentences keep them apart: one is slow, the other is fast, and the slow one's earlier check has gone stale. The explanatory clause for the failure ("was stale by this time due to...") sits in the same sentence as the event. This is a corporate post-event summary and the person is mostly absent. Take the ordering of simultaneous events and the placement of the reason beside the event, not the register.

> "The system is split across two independent components for availability reasons. The first component, the DNS Planner, monitors the health and capacity of the load balancers and periodically creates a new DNS plan"

Checked: https://aws.amazon.com/message/101925/, retrieved 2026-11-27
The component is introduced with its job and the reason it is split, in sentences short enough to follow without a diagram. Each new part gets one sentence saying what it does, and the next sentence says how it relates to the one before. This passage describes an unrelated system and is quoted for its structure only.

## Notes on use

All quotations were checked against the raw page text retrieved on 2026-11-27. The three pieces concern a cache, a regular expression and a DNS race. None concerns this article's subject, and nothing in this guide is a fact about the Microsoft 365 outage.
