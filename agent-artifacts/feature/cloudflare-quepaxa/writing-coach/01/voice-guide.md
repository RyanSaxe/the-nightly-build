# Voice guide: feature/cloudflare-quepaxa (01)

## How this piece should sound

This is a five-minute explanatory feature for engineers who know distributed systems at a CS-degree level and have run systems in production. The register is a practitioner's: plain, exact, and unhurried about the one mechanism that matters. Kingsbury, Brooker and Evans all write as people who have watched the system misbehave and want the reader to see what they saw. The page talks to a peer who can follow a protocol trace without being walked through quorums, and who does not need persuading that a leader failure is a real event.

Name the parts of the protocol in their own words and keep each word fixed once chosen: proposer, recorder, round, leader, fast path, slow path, hedging delay, election timeout, decision rate. Kingsbury's Redis-Raft passages show the payoff. Each anomaly is stated by what a client observed, a read missing a write that finished seconds earlier, and only then named. Where the material calls for it, the same order suits this piece: what the decision rate did during the failure, and then what the paper calls that behaviour. Every figure should carry who measured it and what it counts, said once in the sentence where it appears, the way Kingsbury attributes each fix to a version and each diagnosis to the team that made it.

The visuals carry the argument, and the prose around each one tells the reader how to read it, as Evans does when she lists what in dig's output is confusing and then shows the same information laid out so its sections are visible. Her point that the clear version is "not dumbed down" applies to the drawings: a QuePaxa round or a Raft election drawn without its real phases teaches less than one with them labelled.

Brooker shows how to weigh a design choice fairly. He states a paper's claim in its authors' words, agrees where he agrees, and says plainly where he thinks it is debatable, with the reason. The Raft side of this comparison deserves that treatment: give the case for election timeouts as its proponents make it before saying what QuePaxa changes. A judgment can be firm and short when the evidence supports it. Where two figures measure different things, the piece can say so in a sentence and move on, without performing caution.

Five minutes leaves room for a short aside or a dry line when one comes from the material, as Brooker's "Up, but down" does. It leaves no room for a paragraph of background that no visual needs.

## Kyle Kingsbury, "Jepsen: Redis-Raft 1b3fbf6"

Source: https://jepsen.io/analyses/redis-raft-1b3fbf6

> "Versions d589127 and 8da0c77 also exhibited stale reads in normal operation, without any faults. For instance, consider this pair of transactions, where T1 completed 3.25 seconds before T2 began: ... If Redis-Raft were linearizable, then T1's append of 11 to key 1 should have been visible in T2's read—but instead, T2 observed only [5 8 9]. This is a stale read: a view into the past."

Checked: https://jepsen.io/analyses/redis-raft-1b3fbf6 (raw HTML), retrieved 2026-11-13
The anomaly is shown as concrete observed history, with versions, keys and a timing, before it gets its name, so the term is defined by the instance. The closing gloss, "a view into the past", is Kingsbury's own compression, and it is the only flourish in the paragraph.

> "This code is simple, and works correctly some of the time. However, in Redis-Raft, calls to DISCARD can (and often do!) fail, e.g. for NOLEADER, NOTLEADER, etc. This leaves the connection in the MULTI state, with operations buffered by Redis. Subsequent calls will execute in the previous MULTI context, which could lead to confusing results"

Checked: https://jepsen.io/analyses/redis-raft-1b3fbf6 (raw HTML), retrieved 2026-11-13
He walks a failure forward one state at a time, from a failed call to the connection's state to what the next call does. The dry "works correctly some of the time" and the parenthetical "(and often do!)" are where a person with opinions shows through an otherwise formal report.

> "Redis Sentinel, Redis Cluster, and Active-Active Geo-Distribution all allow lost updates—at least for some workloads. ... So, does Redis Enterprise lose updates? Or is it "full ACID"?"

Checked: https://jepsen.io/analyses/redis-raft-1b3fbf6 (raw HTML), retrieved 2026-11-13
He sets a vendor's claim, in its own quoted words, against what the mechanism allows, and asks the question the following paragraph answers with the vendor's clarification. The qualification "at least for some workloads" is exact about scope, not a hedge.

## Marc Brooker, "Metastability and Distributed Systems"

Source: https://brooker.co.za/blog/2021/05/24/metastable.html

> "That increased latency causes clients to time out before the system responds to them. Clients continue to send work, and the system continues to complete that work. Throughput is great. None of the work is useful, though, because clients aren't waiting for the results, so goodput is zero. The system is mostly stable in this state, and without an external kick, could continue going along that way indefinitely. Up, but down. Working, but broken."

Checked: https://brooker.co.za/blog/2021/05/24/metastable.html (raw HTML), retrieved 2026-11-13
A causal chain told in short sentences, each one a step a reader could draw. He separates two quantities, throughput and goodput, at the moment the difference matters, and the two fragments at the end are an operator's shorthand for a state he has clearly seen.

> "The rest of their proposed solutions are more debatable. Changing policy during overload introduces modal behavior that can be hard to reason about (and modes are bad). Prioritization and fairness are good if you can get them, but many systems can't, either because their workloads are complex interdependent graphs without clear priority order, or because the priority order is unpalatable to the business."

Checked: https://brooker.co.za/blog/2021/05/24/metastable.html (raw HTML), retrieved 2026-11-13
He grants the paper's ideas their value and then says exactly why each fails in practice. "(and modes are bad)" is a builder's conviction stated without argument, and it reads as earned because the reasons around it are specific.

> "If you're only looking at your day-to-day error rate metric, you can be lead to believe that adding more retries makes systems better because it makes the error rate go down. However, the same change can make systems more vulnerable, by converting small outages into sudden (and metastable) periods of internal retry storms."

Checked: https://brooker.co.za/blog/2021/05/24/metastable.html (raw HTML), retrieved 2026-11-13
He shows how one measurement can point the wrong way, naming the metric and the change. It is addressed to someone who runs a weekly metrics review, which is where his own experience shows.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "When you make a DNS request on your computer, the basic story is: your computer makes a request to a server called resolver the resolver checks its cache, and makes requests to some other servers called authoritative nameservers Here are some things you don't see: the resolver's cache. What's in there?"

Checked: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/ (raw HTML; list items run together in the extracted text), retrieved 2026-11-13
She gives the two-line visible story, then lists the parts of the system the reader cannot see. The question "What's in there?" is her own curiosity, asked in the reader's voice.

> "This makes the structure of the DNS response more clear – there's the header, the question, the answer, and the additional section. And it's not "dumbed down" or anything! It's the exact same information, just formatted in a more structured way. My biggest frustration with alternative DNS tools that they often remove information in the name of clarity."

Checked: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/ (raw HTML), retrieved 2026-11-13
She states a position on explanation itself: clarity comes from layout, not from dropping detail. The exclamation and "My biggest frustration" put her preferences on the page plainly, next to a worked example that backs them.
