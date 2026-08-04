# Voice guide: tech-news/2026-08-04 (01)

## Directive

This brief runs the house register — calm, precise, first-principles — at wire
speed: four to six items, each a self-contained verdict, not a mini-essay. The
reader already has the headline. Write for someone who will click through to
the primary record and check you, not someone who needs to be convinced to
care.

Sentences that change under this: open each item on the narrowest concrete
fact (the number, the date, the specific claim) before any word that frames
it. Treat a vendor's own language as a quotation to be inspected, never a
narration to adopt — if the announcement calls something a breakthrough, that
word needs its own citation and its own scrutiny, not a retelling in your
voice. When a claim rests on something checked rather than merely stated, name
the check in the same clause the claim appears in (an independent run, a
reproduction, a named expert's read of the paper), not as a trailing aside.
Keep the analysis inside the report sentence, load-bearing on the fact it
follows, since the template already forbids a closing line that hands the
point back to the reader.

Across five short items back to back, uniform syntax reads as a template even
when each fact is real. Vary how items open: not every item leads with the
actor's name doing the releasing. Let some open on the number, some on the
date, some on the document.

## Licenses

```text
form: earned hedge-contrast ("real, but not a rupture")
move: Timothy B. Lee (Understanding AI) confirms a claim's substance, then
      bounds it in the same breath, on the one item where the vendor's frame
      and the technical content genuinely diverge — e.g., a model solved a
      real open problem by recombining known technique, not a new method.
bar:  Usable once across the whole brief, not once per item. The "but" clause
      must name the specific thing the claim does not do (not "impressive,
      but early"). Cut it if every item would earn the same sentence with the
      vendor's name swapped in.
```

```text
form: the named-verification clause
move: Simon Willison folds the fact that a claim was checked into the
      sentence stating it, in one clause, rather than reciting the vendor's
      benchmark table: what was run, by whom, against what.
bar:  Only when a specific check actually happened and is sourced — an
      independent benchmark, a reproduction, a named expert's assessment of
      the primary document. A generic "researchers say this is significant"
      does not qualify; that is attribution wearing verification's clothes.
```

## Recently used, do not reuse

Per the commission: the run from 2026-07-27 through 2026-08-03 leaned hard on
open-weight model releases, model-vs-model benchmark races, AI-security
CVE disclosures, and Claude/Anthropic cryptography findings. Do not let this
edition's items fall into the resulting default lead shape — "[Company]
released [Model], which beats [Model] on [benchmark]" — even for an item that
is itself a model release; open on the number or the document instead. Do not
re-file any of those running stories without a genuinely new, sourced
development. Avoid a colon-subtitle headline, and avoid the three banned dek
molds by name: the semicolon reversal ("X did A; Y refuses B"), the suspended
question ("...and the real question is whether"), and the comma triad closed
with "and." Vary section-heading and dek cadence item to item; five items
that each open the same way stamp the page as machine-made even when no
single sentence does.

## Simon Willison, "tencent/Hy3"
Source: https://simonwillison.net/2026/jul/6/hy3/
Craft:
- cadence: States the spec before the claim earns a reaction. "295B-parameter
  Mixture-of-Experts model" arrives before any adjective does.
- argument: Doesn't rebut the vendor's framing directly. Runs the model
  himself and lets the result stand next to the vendor's claim, unremarked.
- evidence: A live test (asking it to draw a specific, hard image) functions
  as the citation. The number replaces the adjective: 598GB, not "massive."
- stance: Default skeptical, not adversarial. Vendor copy is quoted, set off,
  and treated as a claim under test, not adopted as narration.
- notice: Catches that this is the second release of the same model line and
  says so, crediting an earlier writer who covered the preview, so the delta
  the reader actually needs (what's new since May) survives instead of the
  release being treated as a fresh event.
- diction: No superlatives of his own. Every strong claim in the post is
  someone else's quoted sentence.
- reader: Writes to someone who can and will go run the model themselves;
  gives the exact place and the exact expiry date to do it.
- the move the axes miss: he narrates his own act of checking as the
  evidence. The post's authority comes from "I had it generate an SVG," not
  from restating the release notes with more confidence.

## Timothy B. Lee, "OpenAI's math breakthrough played to AI's strengths"
Source: https://www.understandingai.org/p/openais-milestone-math-breakthrough
Craft:
- cadence: Opens on the dated, specific record (the conjecture, the age of
  the open problem) before any assessment of what it means.
- argument: Holds two true things apart without letting one cancel the
  other — the result is real, and it is not a new kind of capability. Each
  gets its own sentence, not a single hedged one.
- evidence: Primary sources are named, credentialed, independent mathematicians
  reacting to the actual proof, not company spokespeople paraphrasing it.
- stance: Translator more than judge. Restates what the announcement claims
  more precisely than the announcement did, then separately checks it.
- notice: Catches that the AI-produced proof was subsequently cleaned up and
  extended by human mathematicians, the detail the announcement's framing
  would rather the reader not weigh.
- diction: Hedges are precise and load-bearing ("arguably the first time"),
  never a vague softener stapled on to avoid a claim.
- reader: Assumes the reader already saw the headline claim and wants the
  gap between the claim and the paper checked for them.
- the move the axes miss: he lets a named expert's own words do the
  deflating or confirming. His sentences report what was said and by whom;
  the verdict arrives through the quote's placement, not his adjectives.

## Jack Clark, Import AI (issue 441, "My agents are working. Are yours?" and item block)
Source: https://jack-clark.net/2026/01/19/
Craft:
- cadence: Each item is a closed unit: a compact finding sentence, a
  paragraph of texture, then a distinct turn where the implication is stated
  outright, never left implicit.
- argument: No unifying thesis across items. Each one argues exactly one
  change and stops before it can sprawl into the next.
- evidence: Primary text is quoted directly from the source material, marked
  as a quotation, sitting beside Clark's own compressed restatement of it.
- stance: An analyst embedded in the field, willing to state a consequence
  plainly once the report has earned it, rather than only ever describing.
- notice: Catches the second-order effect a purely technical item would
  skip — what a capability does to labor, trust, or governance once it is
  ordinary rather than new.
- diction: Concrete verbs carry the sentence; adjectives are rare and
  specific ("multiplying me," not "boosting productivity").
- reader: Peer-to-peer. No term of art gets defined; the newsletter assumes
  the reader already tracks the field and wants the week's actual delta.
- the move the axes miss: the analytical turn is structurally separate from
  the report, so a reader skimming only those turns still gets the argument.
  This brief's template forbids that as a closer, so the transferable part is
  the separation of report from implication inside a sentence, not as a
  trailing paragraph.

## Note on the fourth axis (research-as-news)
Quanta Magazine's research desk (e.g. "Why the Legendary Erdős Problems Are
Falling to AI," https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/)
was read for the same reason but is not licensed here: its patient,
narrative-scaffolded build from one dated instance out to a field-wide
pattern fits a feature, not a wire item bounded to one paragraph. The one
transferable habit worth keeping without a license: lead on the single
dated, checkable fact (a specific date, a specific paper) before naming the
broader pattern it belongs to. That is the brief's existing discipline, not a
new one.

## Self-test
A writer following only `press/editorial.md`'s baseline (Hashimoto/Olah/Weng)
would still under-cite verification, since nothing in the default requires
naming the check itself rather than the claim. It would also let every item
converge on the same "Company released Model, beating rivals on Benchmark"
opening, since nothing in the default varies syntax item to item. Both
licenses above, and the directive's opening-syntax instruction, are new
constraints this guide adds — a piece following only the house default would
not reliably produce them.
