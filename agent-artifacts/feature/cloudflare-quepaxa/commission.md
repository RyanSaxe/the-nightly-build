# Commission: feature/cloudflare-quepaxa

Series: feature (open, strict). Template: article. Slug: cloudflare-quepaxa.
Bands: 600 to 1,200 words (hard limit), 2 to 4 flex sections, at least 5
sources. Five-minute read: open with the finding in two or three sentences,
then one visual per section with short prose on how to read it and what
follows.

## Topic

On 11 November 2026 Cloudflare published "Choosing QuePaxa, an unusual
consensus algorithm" (blog.cloudflare.com/choosing-quepaxa/), explaining why
the replicated log under its control plane (the Meerkat project, introduced
2026-07-08) uses QuePaxa (Tennage, Basescu, Kokoris-Kogias, Syta, Jovanovic,
Estrada-Galiñanes, Ford; SOSP 2023) in place of Raft or Multi-Paxos. QuePaxa
keeps deciding when a leader fails without relying on a timeout to elect a
new one; leader-based protocols stall until a timeout fires, and a timeout
set too short makes them lose liveness.

Why now: Cloudflare's 11 November post, with its first published production
measurement of a leader failure.

## The angle to test

Working angle: QuePaxa trades timeout fragility for extra rounds and
bandwidth, and Cloudflare's leader-failure measurement shows what that trade
looks like on a real network: the decision rate dips but never halts, while
the slow path costs up to two-thirds of throughput. The piece sets the paper's
claims (randomized rounds deciding with probability at least 1/2 each;
hedging delays in place of timeouts; Fig. 9's recovery under different
timeouts against Multi-Paxos and Raft) beside Cloudflare's numbers (over 95%
of decisions on the leader's fast path; the 15:00:32 to 15:01:25 UTC failure;
decision rate falling to about 65%; slow path at most a third of normal
throughput).

The angle must survive the evidence. Known risks: the paper's
probability-per-round bound and Cloudflare's 95% fast-path share measure
different things, and the piece must not set them against each other as if
they disagreed; the paper's sub-second recovery and Cloudflare's minute-long
dip may measure different events (recovery of throughput vs time to replace a
leader). Find out exactly what each figure measures before comparing. Raft
and Multi-Paxos numbers read off a chart are approximate and must be labelled
so. Meerkat is not yet in production per its July post; say what Cloudflare
says about its status, in its words. State the Raft side fairly: a Raft
proponent's account of why timeouts are a reasonable cost (e.g. Ongaro and
Ousterhout's Raft paper on election timeouts, or PreVote/CheckQuorum in etcd)
before weighing it.

If the evidence shows the measured failure says little about the trade, the
headline says what the evidence does support.

## Original work

One drawn account that places the paper's mechanism (a round's phases, the
hedging delay) and its benchmark beside Cloudflare's production timeline, with
each figure labelled by what it measures and who measured it, which neither
source does alone.

## Visuals

Writer's choice, per press/editorial.md preferring drawn mechanisms: a
QuePaxa round drawn as inline SVG (proposers, recorders, the phases, the fast
path through the leader) beside a Raft election stalled on its timeout; a
timeline of Cloudflare's failure; a comparison of recovery versus timeout from
the paper's Fig. 9 (values as stated in the paper's text, or captured with
`nb asset` where the original figure shows it best). Charts only from verified
numbers.

## Boundaries

- Not a Cloudflare profile and not a general consensus tutorial; teach only
  what the comparison needs, for readers who know distributed systems at a
  CS-degree level (they may not know QuePaxa).
- No speculation about motives. Never write that anyone hinted or signalled.
- Tags: distributed-systems, consensus, cloudflare.

## Recent patterns to break

From the last five features:
- Headlines have opened with or carried a large figure ("Glasswing's 2
  November ledger reveals 235 of the 5,087", "...from 369 to zero", "...6.3
  million"). Tonight's headline carries a number only if the number is the
  surprise.
- Deks have opened "By this paper's arithmetic"/"By METR's arithmetic" and
  have stacked three figures in one sentence. Do neither.
- Section headings have been either bare figure pairs ("629 patched, 235
  checkable") or full declarative clauses of similar length. Vary their build.
- Closing lines have opened "On this evidence, ...". Do not.

## Neighbours in this edition

- daily-brief/2026-11-13: its technology items must not cover QuePaxa,
  Meerkat or Cloudflare's consensus work.
- reinforcement-learning/observation-scale: no overlap.

## Production

Roles: writing-coach (policy: capable, low), researcher (capable, high),
writer (capable, high, from series.yaml), editor (inherit, high, required).
Subagents run on the orchestrator's model with the Agent tool's effort set to
the policy value.

## Decisions during production
Revised angle, decided by the orchestrator after researcher/01:

- Framing: Cloudflare's measurement is an evaluation of Meerkat, an
  experimental consensus service not in production (July post: "not deployed
  to production"; November post: "our own evaluations"). Never call it a
  production measurement.
- The piece's finding is the shape of a leader failure. Raft (and
  Multi-Paxos): no commits for about an election timeout, then full speed
  (Raft paper §5.6, 150-300 ms recommended, etcd's ≥10× RTT guidance).
  QuePaxa: a sub-second gap in the paper's test (303-473 ms crash to first
  progress, §7.5), then slower running until the leader is replaced; in
  Cloudflare's evaluation the decision rate held near 65% for the 53 s before
  replacement, well above the 33% limit Cloudflare derives from round-trip
  counts (a derived limit, not a measurement). Say plainly that putting the two
  shapes side by side is this paper's inference from separate sources, and
  that nobody has measured Raft in Cloudflare's setting.
- Do not set Cloudflare's 95% fast-path share against the paper's 1/2 bound.
  If the bound appears, state it correctly (worst-case minimum per leaderless
  round, round 2 onward) and note in one clause that Cloudflare's post calls it
  a "50% chance" the paper predicts, only if space allows.
- The Raft side, fairly and first: the 2020 incident is Cloudflare's own
  motivation. State it from the 2020 postmortem (etcd read-only about six
  minutes, the longer slowdown from a database failover cascade), noting the
  November post's "six hours" refers to the dashboard. Then Howard and
  Abraham's account that PreVote and CheckQuorum keep a stable Raft leader
  under partial link failure, and etcd's default since v3.5.0. Those fixes do
  not remove the election timeout after a leader crash; that is where
  QuePaxa's design differs.
- Fig. 9: chart or table only the paper's stated figures (303-473 ms; 1.8×
  RTT / 330 ms; "fail to stabilize" below 200 ms). Do not chart values read
  off the plot, and do not reproduce Fig. 9 itself; its plot and text
  disagree. One sentence may say so.
- Cloudflare's two-panel chart may be captured with `nb asset` with a caption
  that states the evaluation's unknowns (no cluster size, RTT, load, hedge
  delay or averaging window given). The drawn mechanism remains the lead
  visual: a QuePaxa round with its fast path beside a Raft election timeout,
  and/or a drawn timeline of the two failure shapes, labelled schematic.
- Headline direction: the trade itself (a timeout stall vs. a minute of
  slower deciding), not the 95% or the 33%. The writer decides the words
  under spec/headlines.md.
Decided after writer/01:
- "then runs at full speed" for Raft after an election goes beyond §5.6.
  Soften it to what the Raft paper supports (the cluster commits again once a
  leader is elected); the editor makes the cut directly.
- Fig. 1's idle proposer 3 is acceptable as a schematic following §5.2, as
  labelled.
- The 65% is described as the low point of a step-down, per the evidence, not
  a plateau. Accepted.
