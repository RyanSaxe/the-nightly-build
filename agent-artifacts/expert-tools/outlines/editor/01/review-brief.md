# editor review-brief: expert-tools/outlines (01)

Inputs:
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/agent-artifacts/expert-tools/outlines/editorial-direction.md
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/agent-artifacts/expert-tools/outlines/commission.md
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/agent-artifacts/expert-tools/outlines/writer/01/brief.md
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/agent-artifacts/expert-tools/outlines/writing-coach/01/voice-guide.md
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/agent-artifacts/expert-tools/outlines/researcher/01/evidence.md
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/agent-artifacts/expert-tools/outlines/writer/01/draft-handoff.md
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/library/expert-tools/outlines.html  — the article to edit in place
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/.nb-context/  — effective template contract and furniture catalogs

Output:
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/agent-artifacts/expert-tools/outlines/editor/01/editorial-review.md

Recent-pattern notes (compare against these to catch formula the draft cannot show
alone): recent Expert Tools headlines run one mold — "<Tool> <verb>s the work your
old tool can't" ("Atuin makes your shell history answer questions bash can't";
"VisiData turns each new question about a table into a keystroke"; "Serena gives a
coding agent a language server"). The closing section repeats under near-identical
headings ("When the swap pays off"; "What it costs, and whether to trust it") over
an nb-holdsup + nb-note-strong pair. Section headings tend to "<Tool> does X". Flag
the headline, the closer heading, or any section heading if it is stamped to those
shapes; require this piece's own nouns.

This round's focus:
- The by-construction guarantee is backend-dependent: masking runs on local/
  open-weight backends; on hosted APIs Outlines delegates, and inside vLLM/SGLang
  the default engine is often XGrammar. Confirm the draft does not overclaim the
  guarantee across backends, and that the example's backend is stated.
- Speed framing: Outlines should be weighed against the retry-and-parse path it
  replaces, not asserted as today's fastest engine (XGrammar/llguidance claim to
  beat it). Check the draft keeps that distinction, and keeps the structural
  guarantee separate from the contested accuracy side-effect.
- Attribution: the 2023 paper's byline is Normal Computing; the library is now
  dottxt-ai. Check neither is conflated.
- Audit the code example for correctness against the evidence record's captured
  API surface, and audit every data-nb-kind (the draft reports 13 all-primary —
  test whether the alternative-engine comparison is genuinely a primary and
  whether an independent critique is represented).
- Inspect the captured Figure 1 source asset: the crop retains the evidence the
  prose spends and the caption is a factual cited label.

Standard gate applies: only an editorial review with no required change settles the
article. Editor edits prose, structure, and documented furniture directly; routes
reporting, source assets, chart provenance, and any broken central claim to the
writer.
