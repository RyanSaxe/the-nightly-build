# Commission: unbiased/maryland-data-broker-privacy

## Assignment
Present the genuinely contested question opened by the consumer complaint filed
Wednesday, 2026-08-20, in which a coalition of privacy and civil-rights groups
asked Maryland's attorney general to investigate and enforce against data
brokers (named include Penlink/Webloc, Flock Safety, Thomson Reuters, LexisNexis,
Motorola Solutions, Insight LPR) for collecting and selling Marylanders'
location and license-plate-reader data to law enforcement, and for selling data
to entities that assist federal immigration enforcement. The event is documented
by original US reporting (NPR, 2026-08-20). The paper has extra appetite for a
story that runs through technology, and this one does.

## The contested question
Does selling this data to police and to entities that assist ICE violate
Maryland's data-broker privacy law, or is it lawful conduct the statute does not
reach? Present two evidence-backed positions and no house verdict.

- **Position A (the complaint's side).** The sales violate the statute:
  geolocation and ALPR data are the sensitive personal information Maryland's law
  covers; the law's distinctive bar on selling to entities assisting immigration
  enforcement, and its warrant-not-subpoena rule, reach exactly these transfers;
  the AG should investigate and enforce. Draw on the filed complaint, the statute
  text, and the advocates' documented factual claims about the named companies'
  contracts.
- **Position B (the skeptical/defense side).** The sales are lawful or the
  complaint overreads the law: publicly sourced and ALPR-captured data may fall
  outside the covered categories; brokers respond to warrants and lawful process;
  the First Amendment protects the sale of truthful information (Sorrell v. IMS
  Health, 2011); and license-plate readers serve legitimate policing. Steelman
  this from the companies' own positions, the commercial-speech precedent, and
  any statutory-scope argument, not a strawman.

Steelman both before the reader weighs them. The template presents the two
positions without a house verdict; that is the form, not a missing conclusion.

## Boundaries
- Template `unbiased`, **strict mode**: structure and citation are hard gates.
  1200-3500 words, exactly two flex side sections built from the `nb-side-camp`,
  `nb-side-thesis`, `nb-side-argument`, and `nb-side-champion` components (read
  the skeleton and the furniture context for the exact contract). Minimum 10
  sources: at least 4 primary and at least 3 secondary.
- Primary sources to secure: Maryland's data-broker/privacy statute text, the
  filed complaint, company statements or contract records, and Sorrell v. IMS
  Health for the commercial-speech argument. Independent reporting anchors the
  event; the primary record carries the legal claims. Every source URL must
  resolve.

## Coordinate with tonight's edition
Current Events (2026-08-21) may carry this as one plain factual item. This desk
owns the two-position treatment; the framing here should not read as an echo of
a news item.

## Production record
- Correspondent (coach + research + draft + self-proof): model `claude-opus-4-8`
  (raised from the balanced default for the strict gates, the 10-source
  two-position sourcing, and the legal precision; recorded as a deviation the
  run owns), high effort.
- Editor (fresh eyes, required): model `claude-opus-4-8`, high effort.
- nb-meta: harness `claude-code-routine`, model `claude-opus-4-8`, date
  `2026-08-21`.
- Proof: `nb check .nb-work/unbiased/maryland-data-broker-privacy/library/unbiased/maryland-data-broker-privacy.html --series unbiased --library /home/user/library-checkout`

## Recent patterns to break
- Title/dek: avoid the blunt-statement-then-reframe two-sentence combo
  ("Congress Voted to End the Iran War. The Vote That Would Have Counted
  Failed.") and the dek that closes on a "leaving X open" / "where Y left it"
  participial clause. Avoid the phrase "leaving open whether".
- Opener: do not open by naming the court/official and date of the latest ruling
  before the underlying dispute; open on the dispute.
- Side headings: avoid two short opposing noun phrases as the two side-argument
  headings ("An appropriation is a ceiling" / "The power of the purse"). Build
  them differently from each other.
- Structure: the recent mold is framing section → two evenly balanced side
  sections → Sources, ending mid-argument. Keep the no-verdict close, but vary
  the beats so the non-conclusion does not read as a stamp; avoid the pure
  dueling-quote (one figure's words vs. an opposing scholar's) as the only device.
