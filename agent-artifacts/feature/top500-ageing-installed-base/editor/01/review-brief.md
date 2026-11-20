# editor brief: feature/top500-ageing-installed-base (01)

Inputs:
- .nb-work/feature/top500-ageing-installed-base/agent-artifacts/feature/top500-ageing-installed-base/editorial-direction.md — standing directions, template contract and series prompt
- .nb-work/feature/top500-ageing-installed-base/agent-artifacts/feature/top500-ageing-installed-base/commission.md — the commission, the revised angle under "Decisions after research", and the recent-pattern notes (headline, dek and heading habits of the last five features)
- .nb-work/feature/top500-ageing-installed-base/agent-artifacts/feature/top500-ageing-installed-base/writer/01/brief.md — the exact writer brief
- .nb-work/feature/top500-ageing-installed-base/agent-artifacts/feature/top500-ageing-installed-base/writing-coach/01/voice-guide.md — voice guide
- .nb-work/feature/top500-ageing-installed-base/agent-artifacts/feature/top500-ageing-installed-base/researcher/01/evidence.md — evidence record; computed series and compute.py in .nb-work/feature/top500-ageing-installed-base/data/
- .nb-work/feature/top500-ageing-installed-base/agent-artifacts/feature/top500-ageing-installed-base/writer/01/draft-handoff.md — writer's handoff (it reports two slips it corrected in the evidence record's wording)
- The article: .nb-work/feature/top500-ageing-installed-base/library/feature/top500-ageing-installed-base.html, charts beside it
Output: .nb-work/feature/top500-ageing-installed-base/agent-artifacts/feature/top500-ageing-installed-base/editor/01/editorial-review.md
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/top500-ageing-installed-base/library/feature/top500-ageing-installed-base.html --series feature --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

The draft is at 1,179 of a strict 1,200 words. Recompute the headline and dek figures from series.csv and cohort_survival.csv (rerun compute.py if needed). The writer reports chart tick labels are small at phone width; look at the rendered page (`nb preview`, pre-installed Playwright; do not run playwright install) and fix through `nb chart` if it hurts reading. After any edit rerun `nb stamp` and the proof until BLOCK: 0. Prefix nb commands with `export UV_SYSTEM_CERTS=1; unset UV_NATIVE_TLS;`.
