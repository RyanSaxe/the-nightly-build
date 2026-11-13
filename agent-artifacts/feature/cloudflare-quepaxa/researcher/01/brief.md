# researcher brief: feature/cloudflare-quepaxa (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/feature/cloudflare-quepaxa/agent-artifacts/feature/cloudflare-quepaxa/editorial-direction.md: the standing directions, including the series prompt
- /home/user/the-nightly-build/.nb-work/feature/cloudflare-quepaxa/agent-artifacts/feature/cloudflare-quepaxa/commission.md: the topic, the angle to test and its known risks
Output: /home/user/the-nightly-build/.nb-work/feature/cloudflare-quepaxa/agent-artifacts/feature/cloudflare-quepaxa/researcher/01/evidence.md

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

Starting documents (opened by a scout; verify every figure yourself):
- https://blog.cloudflare.com/choosing-quepaxa/ (2026-11-11)
- https://blog.cloudflare.com/meerkat-introduction/ (2026-07-08)
- https://bford.info/pub/os/quepaxa/quepaxa.pdf (SOSP 2023; also the ACM DL
  version and arXiv if available)
- Raft: Ongaro and Ousterhout, USENIX ATC 2014, on election timeouts; etcd's
  PreVote/CheckQuorum documentation for the practitioner's mitigation.
For each figure in the commission's angle, record what it measures, its unit,
its owner, and the exact passage or figure. Resolve the two known risks
(what the 95% and the 1/2 bound each measure; what the paper's recovery time
and Cloudflare's dip each measure) and say plainly whether the angle
survives. For Fig. 9 of the paper, give the values the text states and say
which are only readable off the chart. Note any image worth capturing with
`nb asset` (URL and what it shows).
