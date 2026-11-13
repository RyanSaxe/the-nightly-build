# Editorial review: feature/cloudflare-quepaxa (editor/01)

## Correct

Thesis, from the draft alone: after a leader failure, Raft stops committing for
about an election timeout, while QuePaxa keeps deciding at a reduced rate until
the leader is replaced. Three claims sit under it.

1. Raft's stall is the price of its election timeout, and the timeout cannot be
   cut toward the round-trip time without losing liveness. Held. I reopened the
   Raft paper (ATC 2014 PDF): §5.6 has "unavailable for roughly the election
   timeout; we would like this to represent only a small fraction of overall
   time" and "Typical server MTBFs are several months or more". §5.2 has
   followers starting an election only after the election timeout, and §8.3 has
   the 150–300 ms recommendation. The QuePaxa paper's §7.5 (bford.info PDF)
   carries "rapidly lose throughput and ultimately liveness", "With a timeout
   above 330ms", "at least about 1.8 times" and "fail to stabilize at all"
   word for word. etcd's tuning page carries "at least 10 times the round-trip
   time" and the 1000 ms default.
2. QuePaxa's leader decides in one round trip, any proposer in three, and later
   rounds are leaderless with a per-round floor of 1/2. Held against §3.3 and
   §3.5. The bound is stated as the worst-case floor for leaderless rounds, as
   the decision requires, and it is not set against Cloudflare's 95%.
3. In Cloudflare's evaluation the rate stepped down to about 65% over the 53
   seconds before replacement, above Cloudflare's derived 33% limit. Held
   against the November post's caption ("around 65%", "a minute after
   failing", "At no point did the system halt") and the "down to at most a
   third" passage. The July post's "Meerkat is not deployed to production" is
   quoted. The piece never calls the run production.

Breaks and fixes:

- "then runs at full speed" (opening). No cited source measures Raft's rate
  after an election. Applied the orchestrator's decision: the sentence now reads
  "commits nothing until it elects a new one, roughly an election timeout
  later", which §5.2 and §5.6 support. The Fig. 3 label "new leader, full rate"
  had the same fault and now reads "new leader commits". The aria-label was
  changed to match.
- The dek said the rate "never reached zero". Cloudflare's chart cannot show a
  sub-second gap, the article itself says Cloudflare publishes no
  crash-to-first-decision gap, and Fig. 3's QuePaxa panel draws the paper's
  303–473 ms drop to zero. The dek contradicted the article's own figure. It
  now says the failure "cut the decision rate to about 65% of normal". This
  narrowed the claim to what the record supports.
- The closer said "the log never stopped", the same overreach, now attributed:
  "Cloudflare reports that the system never halted". The closer also said the
  slower running "cost at most about a third of the decision rate". That used
  "a third" in the opposite sense from Cloudflare's "down to at most a third"
  two paragraphs earlier, which is the ambiguity that produced the commission's
  wrong two-thirds figure. It now gives the measured low, about 65%.
- "The paper" appeared right after "this paper's inference" in the two-shapes
  section and in the closer, so a reader could not tell The Nightly Build from
  the QuePaxa paper. Each one now says "the QuePaxa paper".
- Dek check (brief item 4): "commits nothing until its election timeout fires"
  is supported. §5.2 says a follower starts an election only after the election
  timeout passes without hearing from a leader, and only a leader commits. Kept.

Labels: the headline's "a minute" is Cloudflare's own caption wording for the
53 seconds. The dek names the evaluation and Meerkat's experimental status.
Every figure in the body names its owner where it appears, and Fig. 3 labels
each value by who measured or derived it.

Citations: every `href` opened. Cloudflare's three posts, Decentralized
Thoughts, the etcd tuning page and the USENIX presentation page return 200 and
hold the cited passages. The DOI resolves to ACM's page, which serves a bot
challenge to curl but is the version of record. The GitHub changelog link was
blocked by this session's proxy. The same file fetched raw holds "Turned on
--pre-vote by default" under v3.5.0 (2021-06). Howard and Abraham's "Yes." to
the PreVote-and-CheckQuorum question supports "keeps a stable leader under
partial connectivity". The 2020 postmortem has "read-only until the faulty
switch recovered" and "Six minutes later". All eight `data-nb-kind="primary"`
markings pass: each source is cited for its author's own claim, and the piece
claims no independent confirmation from the three Cloudflare sources.

## Reads well

The Raft side was weighed before it was stated. "It cannot shrink to fit the
network" and the QuePaxa paper's test came in the third sentence, ahead of the
2020 outage and the PreVote and CheckQuorum account. The section now gives
Raft's designers their own argument first, quoting the full §5.6 sentence with
"only a small fraction of overall time". The designers' remedy follows: a
timeout orders of magnitude below MTBF. Next come the 2020 outage and the Raft
fixes, ending on what the fixes do not remove. The weighing, the table and the
derived 1.8 s close the section. The old line "They keep it small by setting
the timeout well above broadcast time" gave the wrong reason for a small cost:
broadcast time keeps elections stable and has nothing to do with how small the
cost is. It went.

The placeholder test found no slop sentence to delete. The edges hold: the
opener starts on the failure, and each section's first and last lines carry the
piece's own nouns. "costs bandwidth, not liveness" stays as an antithesis
because the misconception it corrects, that a short timer costs liveness, is
stated and measured two sentences earlier. Nothing in the prose lifts from the
commission's sentences or the voice guide's quoted passages.

Recent record: the headline carries no lead figure, the dek opens with neither
"By ... arithmetic" nor a stack of figures, and the closer does not open "On
this evidence". The four headings are built differently from each other and
from the recent pairs.

## The experience

Rendered with `nb preview` and Playwright (system Chrome) at 390 and 1280 px in
light and dark. Nothing overlaps, no arrow stops short, the page has no
sideways scroll, and the table scrolls inside its own wrapper on a phone. Fig. 3
is the piece's strongest element. Its caption now says the side-by-side is this
paper's drawing from separate sources, so a reader who skips the prose still
sees that. The table header now reads "Rule or finding", because the QuePaxa row
is a measured threshold and not a rule.

What the piece gives beyond its sources: one labelled drawing separating the
QuePaxa paper's sub-second gap, Cloudflare's measured 65% low and Cloudflare's
derived 33% limit, beside Raft's timeout stall, which neither source draws. The
handoff's original-work sentence says the same. The headline, reread last,
holds as the trade the piece shows.

## Edits

- Dek (meta and page): "the decision rate bottomed near 65% of normal and never reached zero, where" became "a failed leader cut the decision rate to about 65% of normal, while".
- Opening: "commits nothing for roughly an election timeout and then runs at full speed" became "commits nothing until it elects a new one, roughly an election timeout later".
- Election-timeout section: quoted §5.6 in full and replaced "They keep it small ..." with "They keep it so by setting the timeout orders of magnitude below server MTBFs of "several months or more"."
- Election-timeout section: moved the 2020-outage and PreVote/CheckQuorum paragraph ahead of the weighing, then opened the weighing with "That timeout cannot shrink to fit the network."
- Table header: "Rule" became "Rule or finding".
- "At the paper's 180 ms round trip, etcd's rule means a timeout, and so a stall, of at least 1.8 seconds" became "At the QuePaxa paper's 180 ms round trip, etcd's rule implies a stall of at least 1.8 seconds".
- "The measured rate held about twice that" became "The measured low was about twice that".
- Fig. 3 Raft label "new leader, full rate" became "new leader commits", and the aria-label was changed to match.
- Fig. 3 caption became "Two failure shapes, drawn by this paper from separate sources and not to scale."
- "The paper's 303 to 473 ms" became "The QuePaxa paper's 303 to 473 ms".
- "the liveness failure the paper measured" became "the liveness failure the QuePaxa paper measured".
- Closer: "the slower running cost at most about a third of the decision rate, and the log never stopped" became "the decision rate fell no lower than about 65%, and Cloudflare reports that the system never halted".
- Sources renumbered to first-citation order after the move: postmortem 5, Howard and Abraham 6, etcd changelog 7, etcd tuning 8.
- Re-stamped: 1,190 words, 5 minutes, 8 sources.

## Decision

approve. The argument holds on the evidence, and every remaining fault was an
edit I could make from the record.
