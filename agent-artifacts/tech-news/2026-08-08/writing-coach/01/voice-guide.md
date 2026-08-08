# Voice guide: tech-news brief (technical developments, hype-skeptical)

## Directive

Write each item as a specialist wire brief for a peer who already saw the
headline. The reader is an ML engineer who has read enough vendor announcements
to smell a self-reported number before the sentence finishes. Do not sell the
development to them; tell them the one thing that decides whether it changes
their field's practice or knowledge, and let them weigh it.

The house register (calm, precise, first-principles) stays. Three things it
does not supply on its own, and this brief needs:

- **The first sentence of an item is the verified consequence, not the event.**
  Not that a company announced a fab or a paper posted a result, but what the
  development, if it holds, lets a field now do or know. The actor, the figure,
  and the date follow the consequence; they do not open the item.
- **Every load-bearing claim carries its warrant inside the sentence.** Who
  established it and by what means travels with the claim, so the reader can
  discount a self-reported benchmark or a filing's projected spend without
  leaving the line. Attribution here is not decoration; it is the quantity the
  reader is actually pricing.
- **A source's own characterization never enters the paper's voice unmarked.**
  A company blog is a primary for what the company said, not for whether it is
  true; a preprint is a primary for what the authors measured, not for whether
  it replicates. Keep the paper's assertions to what a primary establishes, and
  hand everything softer back to its claimant by name.

Compression is the template's job, and this brief holds the line hard: one
development per item, the caveat carried in the same breath as the claim rather
than saved for a closing turn, and no final sentence that restates the stakes or
hands the point back to the reader. When an item's last line could be deleted
without loss, it was the recap the format forbids.

## Licenses

form: significance-first opening
move: the studied briefs open on what a result changes for the field's practice
      or knowledge (a capability threshold crossed, a baseline moved, a cost
      structure shifted) and only then name who did it and by how much. The
      Import AI issue leads with the interpretive stake of a benchmark before
      the number; Willison opens on the practical threshold a class of tools
      crossed, not on any one release.
bar:  the opening sentence names a specific, verified change to what a field can
      do or know. An opening that names only the announcement, the actor, or the
      round figure has not yet said why the item exists and fails.

form: the claim-versus-record seam
move: the exemplars set a source's characterization beside what the primary
      actually verifies, in plain attribution, so the gap is visible without
      editorializing. The Register places a vendor's "works as intended" next to
      the documented absence of a CVE; the effect is forensic, not rhetorical.
bar:  both sides are real and sourced, and the seam corrects a genuine gap
      between a claim and the confirmed record, never an invented contrast. This
      is an earned use of the contrast the house bans by reflex, so at most one
      or two per piece, and each must name the claimant. If the "claim" side is a
      strawman the sentence built, cut it.

form: deflation carried by a fact, not a verdict
move: the exemplars puncture a hyped claim by stating the unglamorous specific
      that shrinks it (the number is the vendor's own, the benchmark is
      self-reported, the fab is a projection with no ground broken) and let that
      fact do the work with no adjective on top. Willison retires his own test
      the moment it stops discriminating rather than defend it.
bar:  the deflation is a concrete, sourced fact the reader can check, and the
      sentence adds no sneer, no modifier, and no knowing aside. If the skepticism
      survives only through tone once the fact is removed, it was not earned.

## Simon Willison, "The last six months in LLMs in five minutes"
Source: https://simonwillison.net/2026/may/19/5-minute-llms/
Craft:
- cadence: short observation sentences that name an observable threshold, then a
  clause on what it enabled; urgency comes from specificity, not volume.
- argument: capability claims are grounded in when a change became usable and
  what it unlocked in practice, not in a release's marketing.
- evidence: personal, checkable use as the test; a benchmark is kept only while
  it still separates models and dropped openly when it stops.
- stance: enthusiast who audits his own enthusiasm and says so; skepticism aimed
  as readily at his own tools as at vendors'.
- notice: the moment a metric goes saturated or a tool crosses from
  sometimes-works to daily-driver.
- diction: plain, threshold-oriented words; capability stated as a state the
  reader could verify, not a superlative.
- reader: a peer inside the same enthusiasm, invited into shared skepticism
  rather than lectured from authority.
- the important move: deprecating his own instrument in public, which converts
  the writer from salesman to auditor and makes the surviving claims credible.

## Jack Clark, "Import AI 455: Automating AI Research"
Source: https://importai.substack.com/p/import-ai-455-automating-ai-research
Craft:
- cadence: an item states the development, then a distinct beat of analysis that
  says why it matters; the two are structurally separated, not blended.
- argument: temporal marker, then a capability claim, then a human or prior
  baseline the number is measured against, so a figure never floats free.
- evidence: results reported with their source attached by citation; speculative
  leaps are marked as leaps ("if you squint", "you could argue") and not sold
  as findings.
- stance: takes progress seriously without adopting a vendor's framing; treats a
  company's stated goal as a fact about the company, not about the world.
- notice: which benchmark is a real proxy for a general capability and which is
  narrow, and says which before drawing the implication.
- diction: technical terms used exactly, bridged with a plain gloss where the
  declared reader would not already hold them.
- reader: a technical peer who wants the significance argued, not asserted.
- the important move: the explicit fact-then-significance seam, which keeps the
  reported result and the writer's synthesis visibly distinct so the reader can
  accept one and reject the other.

## The Register, "AI vendors' response to security flaws: It wasn't me"
Source: https://www.theregister.com/2026/04/19/ai_vendors_response_to_security/
Craft:
- cadence: short declaratives alternating with longer evidence chains; the flat
  sentence lands the fact and the longer one supplies the record behind it.
- argument: the gap between what vendors say and what they did is built from
  documented specifics (no CVE, no advisory, a quiet doc change), not asserted.
- evidence: a vendor's exact characterization quoted, then set against the
  action or inaction that contradicts it.
- stance: forensic rather than indignant; the pattern is named as a pattern, and
  the naming is the argument.
- notice: the seam where a company's framing ("working as intended") does the
  work a fix should have done.
- diction: the plain word for the evasion; the specific missing artifact named
  rather than gestured at.
- reader: a stakeholder who absorbs the downstream risk, addressed as someone
  entitled to the unlaundered record.
- the important move: quarantining the vendor's voice behind attribution so the
  paper never asserts the claim it is examining, which is exactly the
  claim-versus-record discipline this brief runs on vendor figures.

## Self-test

A writer who ignored this guide and kept only the house default would produce
calm, precise, correctly sourced items that still open on the announcement,
launder a vendor's projected figure into the paper's own voice, and close on a
tidy restatement. This guide changes those three sentences: it moves the verified
consequence to the front, pins each figure to who established it and how, and
strips the closing recap. What the brief should sound like beyond the default is
a specialist wire report where the seam between what was claimed and what a
primary establishes is visible inside the sentence, and the reader can price the
claim without trusting the paper to have done it for them.
