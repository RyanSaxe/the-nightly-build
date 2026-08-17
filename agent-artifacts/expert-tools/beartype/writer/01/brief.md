# writer brief: expert-tools/beartype (01)

Inputs:
- editorial-direction.md   ../../editorial-direction.md (house standard, press voice, series prompt, template identity)
- commission.md            ../../commission.md (assignment, boundaries, recent-pattern habits to avoid)
- voice-guide.md           ../writing-coach/01/voice-guide.md (how this piece should sound; exemplar passages)
- evidence.md              ../researcher/01/evidence.md (the complete claim set; read Contradictions closely)
- article (edit in place)  /home/user/the-nightly-build/.nb-work/expert-tools/beartype/library/expert-tools/beartype.html
- effective contract       /home/user/the-nightly-build/.nb-work/expert-tools/beartype/.nb-context (template contract, runtime assets, furniture catalogs)

Output: /home/user/the-nightly-build/.nb-work/expert-tools/beartype/agent-artifacts/expert-tools/beartype/writer/01/draft-handoff.md

Proof (run from /home/user/the-nightly-build, links included, until BLOCK: 0):
  ./nb check .nb-work/expert-tools/beartype/library/expert-tools/beartype.html --series expert-tools --library /tmp/claude-0/-home-user-the-nightly-build/b3d5d9d7-6994-5933-851f-0ef1bb302a4b/scratchpad/library-checkout

This round's focus (decisions the evidence record carries but must not be lost):
- Locate beartype's distinctiveness precisely. Per the evidence Contradictions, typeguard also samples containers, so "checks a sample instead of walking the structure" is not by itself the differentiator. The genuine differentiators the evidence supports: the sample is random (not positional), sampling is the only implemented mode (the linear-time strategy is unimplemented), and the decoration-time string-code-generation architecture with zero dependencies and broad PEP coverage. Build the argument there.
- Treat beartype's dramatic overhead numbers (its ~1µs figure; typeguard's "107 minutes" worst case) as the project's own self-serving micro-benchmarks with no independent reproduction. Attribute them as such in prose; do not present them as neutral, independently verified fact. Name the honest limitation the project self-documents (random sampling "invites false negatives"; the homogeneity assumption held "without evidence").
- The code example proves the tool's value (a real type violation caught at a call boundary that static checking would miss at runtime); it must not become an installation walkthrough.
- Name the tool and the work it changes in the headline and section titles, per the series prompt.

Recent habits to break (do not copy prior structure): the recent expert-tools dek mold is a headline claim immediately undercut by a shrinking caveat ("the guarantee holds on X and thins to Y"); the recent headline mold is "Tool verbs your noun". Vary both. Fill nb-meta harness and writer-model fields; nb stamp writes counts.
