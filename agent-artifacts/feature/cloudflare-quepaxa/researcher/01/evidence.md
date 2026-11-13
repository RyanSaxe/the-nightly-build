# Evidence: feature/cloudflare-quepaxa (researcher 01)

The evidence supports a narrower angle than the commission states. Cloudflare's
11 November post does show a QuePaxa cluster that kept deciding through a leader
failure: the relative decision rate fell to about 65% and came back after the
leader was replaced 53 seconds later (15:00:32 to 15:01:25 UTC). The commission
gets three things wrong, and the piece has to correct them. First, this is not a
production measurement. Cloudflare calls it "our own evaluations of Meerkat",
and its July post says "Meerkat is not deployed to production". Second, "at most
a third of the usual rate" is a bound Cloudflare states from round-trip counts
(three round trips in place of one). Its own chart shows the rate bottoming near
65% while about 100% of decisions took the slow path, so the measured cost was
about a third of throughput, not two-thirds. Third, the paper's 303 to 473 ms
"recovery time" is the time from a leader crash until any proposer makes
progress again. Cloudflare's minute is the time the system ran degraded before
the leader was replaced. The two numbers measure different events and must not
be compared. The 95% and the 1/2 bound measure different things and do not
conflict. The 95% is Cloudflare's share of decisions made on the leader's
one-round-trip fast path. The 1/2 is the paper's worst-case lower bound on the
chance that a leaderless round (round 2 or later) decides. Cloudflare's chart
shows no decisions after round 1 at all. Fig. 9 of the paper is usable only
with care. Its text and its plotted values disagree in four places, so quote the
text and label any chart reading approximate. The thin spots: Cloudflare gives
no cluster size, RTT, workload, hedge timeout, aggregation window or replacement
mechanism for its chart, and nobody has measured Raft in Cloudflare's setting.

## Sources

```text
URL:         https://blog.cloudflare.com/choosing-quepaxa/
Kind:        primary for Cloudflare's design choices and its own Meerkat measurement
             (Cloudflare wrote it and ran the evaluation). Secondary for what the
             QuePaxa paper says (it paraphrases the paper).
Establishes: Meerkat uses QuePaxa; Cloudflare's implementation moves the hedge wait
             from replicas to clients; the leader-failure chart and its caption; the
             95% fast-path share; the "at most a third" statement; Meerkat is
             "experimental"; Cloudflare is extending QuePaxa from crash-stop to crash
             recovery and is formally verifying its Rust implementation.
             It merely repeats: the paper's per-round probability (and misstates it,
             see Contradictions); the 2020 incident.
Paraphrase:  Authors João Pedro Leite, Bob Halley and James Larisch, dated
             11 November 2026. Opens by calling Meerkat "an experimental distributed
             consensus service designed to manage our internal global control
             plane". Argues leader-based protocols stall when the leader fails and
             need fault detection whose timeout cannot go below network latency.
             It says Raft "is commonly deployed with an election timeout of five to
             ten times the network round-trip time", with no citation. QuePaxa
             rounds have four phases; the leader can decide in phase 0 (one round
             trip); otherwise proposers can decide in phase 2. Clients send to every
             replica, and non-leaders wait a hedge timeout. In Meerkat, clients wait
             the hedge timeout "instead of the replicas ... but the overall result is
             the same". Hedging "isn't free": more proposers mean more broadcasts and
             a greater chance a round fails to decide. The chart caption reads:
             "QuePaxa falling back to Phase 2 decisions due to a leader failure. The
             decision rate decreases to around 65% of its original rate, and returns
             to 100% when the faulty leader is replaced, a minute after failing. At
             no point did the system halt." Following text: "Most decisions —
             upwards of 95% — are made by the leader in the first phase ... In the
             instances where a decision isn't reached in the first phase, the
             throughput drops momentarily, down to at most a third of the usual rate,
             signaling that three round trips — so three phases — were needed".
Locators:    sections "The challenges of consensus at a global scale" (2020 incident);
             "When fault detection is slow" (5 to 10x RTT); "Why QuePaxa is the right
             fit" (hedging, client-side deviation, 5 ms vs 100 ms example); "How
             QuePaxa works under the hood" (four phases; "50% chance" sentence in
             "Moving to the next round"); "How QuePaxa makes Meerkat possible"
             (evaluation, chart, caption, 95%, "at most a third"); "What we'll be
             showing next" (crash recovery extension, verification).
Quote:       "In our own evaluations of Meerkat, where we had servers spanning nearly
             all continents" (the wording is the evidence that the chart is from an
             evaluation, not production).
Quote:       "The QuePaxa paper predicts that each round has a 50% chance of deciding,
             but in practice, that probability is much higher, thanks to convergence."
             (the wording is evidence of a misparaphrase; see Contradictions).
```

```text
URL:         https://blog.cloudflare.com/meerkat-introduction/
Kind:        primary (Cloudflare on its own project's status and requirements).
Establishes: Meerkat's status, purpose, scale of proofs of concept, and Cloudflare's
             stated reasons for leaving Raft.
Paraphrase:  "Introducing Meerkat- an experiment in global consensus", by James
             Larisch, Bob Halley and João Pedro Leite. Cloudflare's Research team has
             built Meerkat "for the past year". It is "an experimental consensus
             service that is still in development", designed first for small pieces
             of control-plane state, "kept internal-only for the immediate future".
             It says "To our knowledge, this will be the first industrial deployment
             of QuePaxa at global scale." It says QuePaxa needs one round trip when
             the leader proposes and three when a non-leader does ("+ extra
             broadcast"), and more under contention. It says Cloudflare has "seen
             these exact issues" with Raft timeouts in its own systems. It claims the
             QuePaxa authors found "much higher (~10x) throughput than Raft and
             Multi-Paxos" under attack (see Contradictions). Status, in its words:
             "Meerkat is not deployed to production, but we have run multiple
             proofs-of-concept with up to 50 replicas distributed around the world,
             to great success. Leaders in our proof-of-concept clusters constantly
             fail, and the cluster keeps operating with no increase in error-rate."
Locators:    opening section (experimental, internal-only, first industrial
             deployment); "How Meerkat's consensus algorithm provides higher
             availability than Raft"; "Assessing Meerkat's performance" (1 vs 3 round
             trips); "What's next" (production status, 50 replicas).
Quote:       "Meerkat is not deployed to production" (status must be given in
             Cloudflare's words).
```

```text
URL:         https://doi.org/10.1145/3600006.3613150 (version of record, ACM DL, SOSP '23,
             pp. 281-297); full text read at https://bford.info/pub/os/quepaxa/quepaxa.pdf
             (27-page PDF hosted on co-author Bryan Ford's site, linked from
             https://bford.info/pub/os/quepaxa/ as the SOSP paper; includes appendices)
Kind:        primary (the authors' own protocol, proofs and experiments).
Establishes: the mechanism (four-phase rounds, leader fast path, hedging), the 1/2
             per-round bound and what it applies to, the Fig. 9 experiment and its
             stated results.
Paraphrase:  "QuePaxa: Escaping the Tyranny of Timeouts in Consensus", Pasindu
             Tennage and Cristina Băsescu (EPFL, marked equal contribution),
             Lefteris Kokoris-Kogias (ISTA and Mysten Labs), Ewa Syta (Trinity
             College), Philipp Jovanovic (UCL), Vero Estrada-Galiñanes (EPFL), Bryan
             Ford (EPFL). SOSP '23, 23-26 October 2023, Koblenz.
             Mechanism: each slot is decided in rounds of four phases (0 to 3); step
             = 4 x round + phase; each step is one round trip between a proposer and
             a majority of recorders (§3.3, Fig. 2, p. 4). The leader tags its
             proposal with the reserved highest priority H; if it is first to reach
             a quorum in phase 0 it decides after one round trip (§4.2.5, p. 9). The
             leader is used only in round 1; if round 1 fails, later rounds are
             leaderless (§4.2.5). Any proposer can decide in phase 2 of any round
             (§3.3). "Rounds 2 and higher in each slot are leaderless and fully
             asynchronous, each round guaranteed to succeed independently with
             probability at least 1/2" (§3.3, p. 4). "subsequent rounds are
             leaderless and fully asynchronous, guaranteeing at least 1/2 success
             probability each round" (§3.5, p. 4). Liveness theorem: "terminates with
             probability 1 in less than two rounds in expectation"; the bound rests
             on a content-oblivious network adversary (§4.1.3, p. 6; §3.2).
             Hedging: the leader has delay 0; the next proposer waits δ, the third
             2δ, and so on; a later proposer acts only if it has not seen progress
             (§5.2, p. 9). A timeout "serves to detect a likely failure
             retroactively"; hedging "initiates non-interfering parallel effort"; "A
             hedging delay of zero not only makes sense but is common" (§5.1, p. 9).
             If hedging is set very small, "consensus remains live, the only costs
             being redundant proposer effort and lower fast-path success
             probability" (§3.5, p. 4). Leader choice is tuned by a multi-armed-bandit
             process over fixed-length epochs (§5.3, p. 10). The prototype is crash-stop
             (Abstract, §1).
             Fig. 9 experiment (§7.5, p. 13): five replicas in the WAN setting (AWS
             Tokyo, Mumbai, Singapore, Ireland, São Paulo, §7.1, p. 11); measured
             average RTT 180 ms; five submitters inject a constant aggregate 25k
             cmd/s; the leader is crash-stopped at t = 15 s; "recovery time" is "the
             time it subsequently takes for a new leader or alternate proposer to
             resume making progress". Raft and Multi-Paxos are the authors' own
             implementations [82] because the existing Multi-Paxos/EPaxos code did
             not handle leader failure (§7, p. 11); their Raft does not pipeline
             (§7.1). Stated results: QuePaxa "consistently delivers throughput of 25k
             cmd/sec ... regardless of hedging delay"; "the main cost of hedging in
             QuePaxa is increased bandwidth use"; Multi-Paxos and Raft "rapidly lose
             throughput and ultimately liveness when their view-change timeout is
             close to or less than the average network round-trip time"; "With a
             timeout above 330ms, Multi-Paxos and Raft deliver 25k cmd/sec"; they
             "depend on their view-change timeout being correctly configured to at
             least about 1.8 times the network round-trip time"; "for all hedging
             delays, QuePaxa exhibits a recovery time after leader failure between
             303ms and 473ms"; lowest "with a hedging delay around 200ms"; "Below
             200ms timeouts, Multi-Paxos and Raft fail to stabilize at all and hence
             have no recovery time"; "With delays more than 500ms, all protocols
             converge to a recovery time roughly equal to network round-trip time
             plus the timeout". Intro: QuePaxa "maintains full performance even when
             its hedging delays are only 1/3 the underlying round-trip time" (§1, p. 2).
Locators:    Abstract and §1 (pp. 1-2); §3.3 and §3.5 with Figs. 2-3 (p. 4); §4.1.3
             (p. 6); §4.2.5, §5.1, §5.2 (p. 9); §5.3 (p. 10); §7 and §7.1 (p. 11);
             §7.4 Fig. 8 and §7.5 Fig. 9 (p. 13). Page numbers are the bford.info PDF's.
Quote:       Fig. 9 caption: "Impact of timeout/hedging delay configuration on recovery
             time (upper) and throughput (middle)." (it names only two of the three
             panels; see Contradictions)
```

```text
URL:         https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro
             (PDF read: https://www.usenix.org/system/files/conference/atc14/atc14-paper-ongaro.pdf)
Kind:        primary (Raft's authors on Raft's timing design).
Establishes: the Raft proponents' own case for election timeouts: randomized
             timeouts, the timing requirement, the recommended range, and measured
             election downtime.
Paraphrase:  Diego Ongaro and John Ousterhout, Stanford University, "In Search of an
             Understandable Consensus Algorithm", USENIX ATC 2014. Election timeouts
             are "chosen randomly from a fixed interval (e.g., 150-300ms)" so split
             votes are rare and resolved quickly (§5.2, p. 310). Timing requirement:
             "broadcastTime ≪ electionTimeout ≪ MTBF"; broadcast time "should be an
             order of magnitude less than the election timeout"; "When the leader
             crashes, the system will be unavailable for roughly the election
             timeout; we would like this to represent only a small fraction of
             overall time"; broadcast time 0.5 to 20 ms so the timeout is "likely to
             be somewhere between 10ms and 500ms"; MTBFs of "several months or more"
             (§5.6, pp. 313-314). Measured on five servers with a broadcast time of
             about 15 ms: without randomness, elections "consistently took longer
             than 10 seconds" from split votes; 5 ms of randomness gives "a median
             downtime of 287ms"; 50 ms of randomness gives a worst case of 513 ms
             over 1000 trials; with a 12-24 ms timeout, 35 ms on average (§8.3 and
             Fig. 14, p. 317). "We recommend using a conservative election timeout
             such as 150-300ms; such timeouts are unlikely to cause unnecessary
             leader changes and will still provide good availability" (§8.3, p. 317).
Locators:    §5.2 (p. 310); §5.6 (pp. 313-314); §8.3 and Fig. 14 (p. 317). Printed
             proceedings page numbers.
```

```text
URL:         https://github.com/ongardie/dissertation (author's repository; PDF
             stanford.pdf). Stanford copy at
             https://web.stanford.edu/~ouster/cgi-bin/papers/OngaroPhD.pdf could not be
             fetched through this session's proxy (TLS error), so the text was read
             from the author's repository.
Kind:        primary (Raft's author on PreVote).
Establishes: what PreVote does and does not do.
Paraphrase:  Diego Ongaro, "Consensus: Bridging Theory and Practice", Stanford PhD
             dissertation, 2014. §9.6: a partitioned server keeps incrementing its
             term and, on rejoining, forces the leader to step down. In Pre-Vote "a
             candidate only increments its term if it first learns from a majority
             of the cluster that they would be willing to grant the candidate their
             votes". Recommended "in deployments that would benefit from additional
             robustness"; it "does not appear to significantly harm election
             performance". §9.7: with election timeouts drawn from 10 to 20 times the
             one-way latency, leaders are elected "within about 20 times the one-way
             network latency on average"; "99.9% of elections complete in less than 3
             seconds when the one-way network latency is as high as 30-40 ms".
Locators:    §9.6 (pp. 136-137); §9.7 (p. 137).
```

```text
URL:         https://etcd.io/docs/v3.5/tuning/
Kind:        primary (etcd maintainers' operating guidance for their Raft deployment).
Establishes: the practitioner's timeout rule.
Paraphrase:  Defaults: 100 ms heartbeat, 1000 ms election timeout. Heartbeat "around
             0.5-1.5x the round-trip time". "Election timeouts must be at least 10
             times the round-trip time so it can account for variance in the
             network." Upper limit 50 s, "which should only be used when deploying a
             globally-distributed etcd cluster"; US-Japan RTT "around 350-400ms".
Locators:    section "Time parameters".
```

```text
URL:         https://github.com/etcd-io/raft/blob/99f9ffb3d19c2dee73cc802737cd7e1e5f008986/raft.go#L224-L231
             with https://github.com/etcd-io/etcd/blob/1b969e26a2c65733f1ff696e3537373d56b3ae67/server/etcdserver/bootstrap.go#L576-L577
             and https://github.com/etcd-io/etcd/blob/main/CHANGELOG/CHANGELOG-3.5.md (v3.5.0, 2021-06)
             and https://etcd.io/docs/v3.5/op-guide/configuration/ (--pre-vote)
Kind:        primary (etcd's own code, changelog and configuration reference).
Establishes: what PreVote and CheckQuorum do in etcd and their defaults.
Paraphrase:  raft.go Config: "CheckQuorum specifies if the leader should check quorum
             activity. Leader steps down when quorum is not active for an
             electionTimeout." "PreVote enables the Pre-Vote algorithm described in
             raft thesis section 9.6. This prevents disruption when a node that has
             been partitioned away rejoins the cluster." The etcd server sets
             CheckQuorum: true and PreVote from config. CHANGELOG-3.5, v3.5.0
             (2021-06): "Turned on --pre-vote by default ... Should prevent disrupting
             RAFT leader by an individual member." Config reference: --pre-vote
             'true'.
Locators:    raft.go lines 224-231 at commit 99f9ffb; bootstrap.go lines 576-577 at
             commit 1b969e2; CHANGELOG-3.5.md v3.5.0 section; configuration page,
             --pre-vote entry.
```

```text
URL:         https://decentralizedthoughts.github.io/2020-12-12-raft-liveness-full-omission/
Kind:        secondary on Cloudflare's 2020 outage (written by outside researchers),
             primary for its own liveness argument about Raft.
Establishes: Raft without extensions can fail to keep a stable leader under partial
             connectivity; PreVote alone adds a new liveness failure; PreVote plus
             CheckQuorum restores the stable-leader guarantee.
Paraphrase:  Heidi Howard and Ittai Abraham, Decentralized Thoughts, 12 December 2020,
             "Raft does not Guarantee Liveness in the face of Network Faults". Written
             after Cloudflare's postmortem. Five-server example where partially
             connected servers repeatedly force the leader to step down. PreVote
             fixes that, but a partially connected leader can then block elections
             because a follower still hearing from it refuses to pre-vote. Answer to
             "Does Raft with PreVote and CheckQuorum guarantee liveness?": "Yes."
             CheckQuorum makes a leader that loses a majority step down.
Locators:    whole post (three numbered questions).
```

```text
URL:         https://blog.cloudflare.com/a-byzantine-failure-in-the-real-world/
Kind:        primary (Cloudflare's postmortem of its own incident).
Establishes: what the 2020 incident that the November post cites actually involved.
Paraphrase:  Tom Lianza and Chris Snook, 27 November 2020. On 2 November 2020 the API
             and dashboard were impacted "for six hours and 33 minutes"; dashboard
             "as much as 80 times slower". At 14:43 UTC a switch partially failed;
             "Six minutes later, the switch recovered without human intervention."
             In a three-node etcd cluster, node 1 repeatedly started elections while
             node 2 voted for node 3, giving ties; "this made the cluster read-only
             until the faulty switch recovered". etcd going read-only triggered an
             automatic database primary promotion at 14:45; a defect required
             rebuilding all replicas, the remaining primary was overloaded, and the
             first replica finished rebuilding at 21:20 UTC. Postscript: the
             community pointed out it was better called an omission fault than a
             Byzantine fault.
Locators:    timeline headings "14:43 UTC", "14:44 UTC: etcd Errors begin", "14:45
             UTC", "21:20 UTC"; Postscript.
```

## Contradictions

1. **Commission vs Cloudflare on production.** The commission calls the chart
   Cloudflare's "first published production measurement". The November post
   calls it "our own evaluations of Meerkat", and the July post says "Meerkat is
   not deployed to production". The November post never says production. The
   piece must call it an evaluation of an experimental system.

2. **Commission's "slow path costs up to two-thirds of throughput" vs
   Cloudflare's chart.** "Down to at most a third of the usual rate" is a stated
   bound reasoned from three round trips against one. During the leader failure
   the chart shows the Phase 2 share reaching about 100%, yet the relative
   decision rate bottomed near 65% (caption: "around 65%"), never near the
   chart's own dotted 33% line. The measured cost was about a third. The
   two-thirds figure is a ceiling Cloudflare stated, not what it measured. The
   post does not explain the gap. Its wording ("down to at most a third") is
   itself ambiguous, and its plain reading is that the rate falls no lower than
   a third.

3. **Cloudflare paraphrase vs the paper on the per-round probability.**
   Cloudflare: the paper "predicts that each round has a 50% chance of
   deciding". The paper states a worst-case lower bound ("at least 1/2"), against
   a content-oblivious adversary, for leaderless rounds 2 and higher only (§3.3,
   §3.5, §4.1.3). It is not a prediction of typical behaviour. Cloudflare's "in
   practice, that probability is much higher" agrees with the bound being a
   floor.

4. **The 95% and the 1/2 do not conflict.** This one is a risk, not a
   contradiction. The 95% is the share of Meerkat decisions made by the leader
   in phase 0 of round 1, with no stated period. The 1/2 is the minimum chance
   that a leaderless round of round 2 or later decides. Cloudflare's chart has
   only two categories, Phase 0 (1 round trip) and Phase 2 (3 round trips), so
   every decision shown was made in round 1. The chart does not exercise the 1/2
   bound at all.

5. **Paper recovery time vs Cloudflare's minute.** The paper's 303 to 473 ms is
   crash-to-first-progress by "a new leader or alternate proposer" (§7.5).
   Cloudflare's 15:00:32 to 15:01:25 window is failure-to-leader-replacement,
   during which decisions continued at a reduced rate. Cloudflare publishes no
   crash-to-first-decision gap, and a chart at this resolution cannot show a
   sub-second one. The paper publishes no figure for how long degraded operation
   lasts or how fast it runs after the crash. Neither source measures the other's
   quantity.

6. **Paper text vs Fig. 9 plotted values, QuePaxa recovery.** The text says
   303 to 473 ms "for all hedging delays", lowest "around 200ms". Values
   extracted from the PDF's vector coordinates run from about 295 ms (300 ms
   delay) to about 397 ms (50 ms delay), with 200 ms reading about 326 ms. No
   plotted point is near 473 ms. The text may report a range across repetitions
   while the chart plots one statistic; the paper does not say.

7. **Paper text vs Fig. 9, recovery at long timeouts.** The text says that above
   500 ms "all protocols converge to a recovery time roughly equal to network
   round-trip time plus the timeout", which is at least 680 ms. The plotted
   recovery times at 500 to 600 ms are about 300 to 400 ms for all three
   protocols, below the configured timeout itself. Do not chart the
   long-timeout values as precise.

8. **Paper text vs Fig. 9, throughput threshold.** The text says "With a timeout
   above 330ms, Multi-Paxos and Raft deliver 25k cmd/sec". The plot shows Raft
   at 25k from 250 ms. Multi-Paxos reads about 450 cmd/s at 350 ms and reaches
   25k only at 400 ms. The "1.8 times" RTT figure (330/180) is the text's joint
   statement.

9. **Paper text vs Fig. 9 bottom panel.** For hedging delays below the 180 ms
   RTT, the text says "the leader still 'wins' most slots and commits in one
   round-trip". The bottom panel shows about 2.8 average steps per slot at 50 ms,
   which is mostly multi-step decisions, and about 1.07 at 100 ms. The text calls
   the bottom panel the bandwidth cost, but its axis is "Average number of steps
   per slot", and the caption omits it. Bandwidth is not plotted directly.

10. **Cloudflare chart internals the post does not explain.** For about 40 s
    after the marked "leader failure", Phase 0 decisions still make up about 97%
    of the share. Only the leader can decide in phase 0, and the Phase 2 share
    reaches about 100% only around 15:01:15 to 15:01:30. The decision rate also
    climbs to about 108% of baseline by 15:09. The post defines neither the
    aggregation window nor the kind of failure (crash, disconnection or
    slowness). Record these as unexplained. Do not interpret them.

11. **Cloudflare's 2020 account vs its postmortem.** The November post says the
    switch failure caused "the dashboard to operate 80x slower than usual, for
    six hours" and the consensus system was "unavailable for writes until the
    issue was resolved". The postmortem puts etcd's read-only period "until the
    faulty switch recovered", which happened six minutes after 14:43. The
    six-hour impact came from the database failover cascade (replica rebuild
    finished at 21:20). The November post compresses two stages into one.

12. **Raft side: the 2020 failure mode has a known Raft fix.** Howard and
    Abraham, writing in response to that outage, show that Raft with PreVote and
    CheckQuorum keeps a stable leader under partial connectivity. etcd always
    sets CheckQuorum and turned PreVote on by default in v3.5.0 (June 2021). The
    postmortem does not say whether PreVote was enabled in 2020. Neither
    extension removes the election timeout after a leader crash, which is the
    cost QuePaxa's hedging targets.

13. **Timeout rules of thumb differ.** Raft paper: broadcast time an order of
    magnitude below the timeout; 150 to 300 ms recommended in its roughly 15 ms
    broadcast setting. etcd: at least 10x RTT. Cloudflare (uncited): "commonly"
    5 to 10x RTT. The QuePaxa paper measured its own Raft working at roughly 1.8x
    RTT or more (or 250 ms per its plot). At the paper's 180 ms WAN RTT, etcd's
    rule would mean an election timeout of at least 1.8 s, and so roughly that
    much write unavailability per leader crash by the Raft paper's §5.6. That is
    a derived figure, not a measurement.

14. **July post vs paper on attack throughput (minor).** The July post says the
    authors found "~10x" higher throughput than Raft and Multi-Paxos under
    attack. The paper (§7.4) reports QuePaxa at least 75k cmd/s against
    Multi-Paxos and Raft saturating at 2.5k, which is 30x.

15. **Paper versions (minor).** The bford.info landing-page abstract says "600k"
    LAN cmd/sec; the PDF abstract says "584k". Not relevant to the angle.

## Numbers

```text
Figure: leader failure marked at 15:00:32 UTC; leader replaced at 15:01:25 UTC (53 s apart; caption: "a minute after failing")
Owner:  Cloudflare, choosing-quepaxa, chart labels (also in its alt text)
Scope:  one evaluation run of Meerkat with servers "spanning nearly all continents"; date, cluster size, RTT, load not given
```

```text
Figure: relative decision rate falls to "around 65%" of its original rate (chart minimum reads about 64%)
Owner:  Cloudflare, chart caption; minimum read off chart
Scope:  rate relative to pre-failure baseline (100%); aggregation window not stated; during the 53 s window
```

```text
Figure: relative decision rate series, read off chart (approximate): about 100% until 15:00:32; about 94% then 89% to about 15:00:58; about 69% at 15:01:06; about 64% from about 15:01:13 to 15:01:25; about 68% then 72% after replacement; about 96% by 15:02:00; about 100% by about 15:02:40; about 108% by 15:09
Owner:  Cloudflare chart (values are readings, not stated)
Scope:  14:58 to 15:09 UTC; y-axis 0 to 110%; dotted reference line at 33%
```

```text
Figure: share of decisions by phase, read off chart (approximate): Phase 0 100% before failure; about 97% Phase 0 from 15:00:32 to about 15:01:10; Phase 2 about 100% around 15:01:15 to 15:01:30; about 92% Phase 0 shortly after replacement; about 100% Phase 0 from about 15:02:50
Owner:  Cloudflare chart (values are readings, not stated)
Scope:  two categories only: Phase 0 (1 round trip) and Phase 2 (3 round trips)
```

```text
Figure: "upwards of 95%" of decisions made by the leader in the first phase
Owner:  Cloudflare, choosing-quepaxa, "How QuePaxa makes Meerkat possible"
Scope:  share of all Meerkat decisions; period and denominator not stated
```

```text
Figure: slow-path throughput "down to at most a third of the usual rate"
Owner:  Cloudflare, same section
Scope:  stated bound from 3 round trips vs 1; not a measured value
```

```text
Figure: leader decides in 1 round trip; non-leader in 3 (+ an extra broadcast); more under contention
Owner:  Cloudflare, meerkat-introduction, "Assessing Meerkat's performance"; matches paper §3.3/§4.2.5
Scope:  per decision
```

```text
Figure: Meerkat proofs of concept with up to 50 replicas
Owner:  Cloudflare, meerkat-introduction, "What's next"
Scope:  proofs of concept, not production
```

```text
Figure: per-round decision probability at least 1/2
Owner:  QuePaxa paper, §3.3 and §3.5 (p. 4), §4.1.3 (p. 6)
Scope:  leaderless rounds (round 2 and higher), worst case against a content-oblivious adversary; expected rounds < 2
```

```text
Figure: QuePaxa recovery time after leader crash 303 ms to 473 ms "for all hedging delays"
Owner:  QuePaxa paper, §7.5 (p. 13)
Scope:  crash-stop at t = 15 s to first resumed progress; 5 replicas, AWS WAN, average RTT 180 ms, 25k cmd/s offered load
```

```text
Figure: Multi-Paxos and Raft need timeouts of at least about 1.8x RTT (above 330 ms) for 25k cmd/s; below 200 ms they "fail to stabilize at all"
Owner:  QuePaxa paper, §7.5 (p. 13); §1 (p. 2)
Scope:  same setup; authors' own Raft and Multi-Paxos implementations
```

```text
Figure: QuePaxa throughput 25k cmd/s at every hedging delay tested; full performance at hedging delays 1/3 of RTT
Owner:  QuePaxa paper, §7.5 and §1
Scope:  offered load was a constant 25k cmd/s, so this shows keeping pace with load, not capacity (WAN saturation is about 250k, Abstract)
```

```text
Figure: Fig. 9 series read off the PDF's vector coordinates (approximate, label as read off chart)
Owner:  QuePaxa paper, Fig. 9 (p. 13)
Scope:  x = leader timeout / hedging delay, ms, log scale; 180 ms RTT marked
  Recovery time (ms, log axis 100-3000):
    QuePaxa: 50→~400, 100→~315, 150→~300, 200→~325, 250→~305, 300→~295, 350→~330, 400→~305, 450→~335, 500→~335, 550→~300, 600→~300
    Raft: 350→at the 3000 axis top; 400→~345, 450→~355, 500→~365, 550→~370, 600→~355; none plotted below 350
    Multi-Paxos: off the top below 500; 500→~1000, 550→~340, 600→~395
  Throughput (cmd/s, log axis 5-25000):
    QuePaxa: 25000 at all delays
    Raft: 200→~100 (line rises from off-axis below); 250 and above→25000
    Multi-Paxos: 150→5, 200→5, 250→~60, 300→~175, 350→~450, 400 and above→25000
  Average steps per slot (QuePaxa only): 50→~2.8, 100→~1.07, 150 and above→1.0
```

```text
Figure: under simulated attack, QuePaxa at least 75k cmd/s under 380 ms median latency; Multi-Paxos and Raft saturate at 2.5k cmd/s
Owner:  QuePaxa paper, §7.4 (p. 13)
Scope:  WAN, 5 replicas, minority egress latency raised up to 500 ms in 5 s epochs
```

```text
Figure: Raft election timeout 150-300 ms recommended; downtime after crash roughly the election timeout; median 287 ms with 5 ms randomness; worst case 513 ms with 50 ms randomness
Owner:  Ongaro and Ousterhout, ATC 2014, §5.2, §5.6, §8.3/Fig. 14
Scope:  five servers, broadcast time about 15 ms (LAN), 1000 trials per line
```

```text
Figure: etcd election timeout at least 10x RTT; defaults 100 ms heartbeat, 1000 ms election timeout; maximum 50 s
Owner:  etcd tuning docs v3.5, "Time parameters"
Scope:  operator guidance
```

```text
Figure: 2020 incident: switch misbehaved 14:43 UTC, recovered six minutes later; API/dashboard impact 6 h 33 min; dashboard up to 80x slower
Owner:  Cloudflare postmortem, 27 November 2020
Scope:  etcd read-only until the switch recovered; the long tail was the database cascade
```

## Limits

- Cloudflare does not give, for its chart: cluster size, replica locations, RTTs,
  offered load or whether the workload is open- or closed-loop, the hedge timeout
  in use, the aggregation window, the date of the run, or the type of leader
  failure.
- Cloudflare does not say how the leader was replaced: automatically (the paper's
  bandit tuning) or by an operator.
- No crash-to-first-decision gap is published for Meerkat, so the paper's 303 to
  473 ms cannot be checked against Cloudflare's run.
- The 95% has no stated period or denominator.
- No source measures Raft or Multi-Paxos in Cloudflare's environment. The only
  head-to-head is the paper's, using the paper authors' own Raft and Multi-Paxos
  implementations on a 180 ms-RTT AWS WAN at 25k cmd/s.
- Cloudflare's measurement has no independent confirmation. It is one party's
  evaluation of its own system.
- The ACM DL version of record returned 403 (gated) and the EPFL Infoscience
  record returned 429. The paper was read from the bford.info PDF, the extended
  version with appendices. I could not confirm that Fig. 9 and §7.5 match the
  ACM version word for word.
- No arXiv version of the paper was found.
- Fig. 9 cannot give precise Raft or Multi-Paxos values: the text and the plot
  disagree (Contradictions 6 to 9). Any chart from it must say "read off chart,
  approximate".
- The postmortem does not say whether PreVote was enabled in etcd in November 2020.

## Source assets

```text
Asset: Cloudflare's two-panel chart "RELATIVE DECISION RATE" over "SHARE OF DECISIONS BY PHASE",
       14:58-15:09 UTC, in choosing-quepaxa, section "How QuePaxa makes Meerkat possible".
       File: https://blog.cloudflare.com/_emdash/api/media/file/01M73MN2G9VJ180TS373QNGVJJ.png (1999x1150)
Shows: the leader-failure and leader-replaced markers (15:00:32, 15:01:25), the dip to about 65%,
       the 33% reference line, and the flip to Phase 2 decisions
Crop:  keep both panels, both dashed markers with their time labels, the 33% line and the
       phase legend; the chart is Cloudflare's, so the caption must credit it
```

```text
Asset: Cloudflare flowchart of QuePaxa's phases (Phase 0 Propose & Adopt → Leader Fast Path →
       Decide; Phase 1 Spread; Phase 2 Check & Decide; Phase 3 Carry Forward → New Round), same post,
       "How QuePaxa works under the hood".
       File: https://blog.cloudflare.com/_emdash/api/media/file/01M742V4V70RZ0GWP04ZEPQQAS.png
Shows: where the fast path exits and where slow-path decisions happen
Crop:  whole flowchart; better redrawn as the article's own SVG than captured
```

```text
Asset: QuePaxa paper Fig. 9, three panels (recovery time, throughput, average steps per slot vs
       leader timeout / hedging delay, with 180 ms RTT line), bford.info PDF p. 13, §7.5
Shows: QuePaxa flat at about 300-400 ms recovery and 25k cmd/s across delays; Raft and Multi-Paxos
       failing below about 200-400 ms
Crop:  all three panels, the legend and the RTT line; the caption must note the panels' values
       are approximate and that the paper's text and plot differ in places
```

```text
Asset: QuePaxa paper Fig. 2 (slots, rounds of four phases, step = 4 x round + phase) and Fig. 3
       (destructive interference in Paxos vs cooperative concurrency in QuePaxa), p. 4
Shows: the round structure the article's own drawing needs
Crop:  either figure whole; better as a reference for a redrawn SVG
```

```text
Asset: Raft paper Fig. 14, "The time to detect and replace a crashed leader", p. 317
Shows: Raft's election downtime CDFs by timeout randomness and timeout size (LAN)
Crop:  the bottom graph (scaling the minimum election timeout) carries the point; keep its caption
```

```text
Asset: meerkat-introduction, etcd docs, Decentralized Thoughts post, 2020 postmortem
Shows: None found that carries an argument better than prose
Crop:  n/a
```

## Discarded

```text
https://research-explorer.ista.ac.at/record/14743 (and .yaml): metadata only; used to confirm SOSP pages 281-297 and that the DOI is the open-access published version; adds no evidence beyond that
https://infoscience.epfl.ch/record/308891: returned 429 (rate-limited), not read
https://dl.acm.org/doi/10.1145/3600006.3613150: returned 403 (gated), not read; the DOI is still the citation of record
https://aminer.org/pub/65254faa939a5f4082cdfd05/...: aggregator listing, not opened; secondary
https://sec.cs.ucl.ac.uk/projects/PJ-QUEPAXA: project listing, not needed beyond the paper
https://dotat.at/:/PCQP8: mirror of the Decentralized Thoughts post; the original was read instead
https://davecturner.github.io/2017/08/17/paxos-pre-voting.html: search result on pre-voting in Paxos, not needed once Ongaro §9.6 and Howard and Abraham were read
https://blog.cloudflare.com/tag/meerkat/: checked for later Meerkat posts; lists only the two posts above
```
