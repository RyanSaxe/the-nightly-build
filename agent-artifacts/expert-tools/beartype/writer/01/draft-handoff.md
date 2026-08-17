# Draft handoff: expert-tools/beartype (01)

## Original-work statement

The article turns the evidence's scattered claims and contradictions into one
cost-benefit argument, pairing each of beartype's capabilities with the exact
limit the project documents against itself, and locating the tool's
distinctiveness in random-only sampling with no implemented full-walk mode
rather than in the "fast sampling" beartype markets.

## Proof result

`./nb check ... --series expert-tools --library <checkout>` (links included):
**BLOCK: 0, WARN: 0** after `nb stamp` (words=1900, reading_minutes=8,
sources=13, all primary). No warnings left standing.

## Decisions worth the editor's eye

- **Distinctiveness relocated per the brief's focus.** The piece does not rest
  the angle on "samples instead of walks" (the evidence Contradictions show
  typeguard also samples per call). It builds the argument on random-only
  sampling, the `On` full-walk strategy being unimplemented (so sampling is the
  only container check available today), and the decoration-time code-generation
  design with zero dependencies. Sections "random-item-per-level",
  "false-negatives", and "alternatives" carry this.

- **Benchmarks attributed, not asserted.** The article cites only beartype's
  ~1µs self-benchmark and labels it self-measured with no independent
  reproduction. I deliberately left out the "typeguard 107 minutes" figure
  entirely: it is beartype's own pathological-case benchmark of a competitor,
  and repeating it even attributed would dignify a self-serving comparison. Flag
  in case the editor wants it restored with attribution.

- **Self-documented limitation quoted against the tagline.** The FAQ's "invites
  false negatives ... homogeneous ... without evidence" admission sits in a note
  in the tool's own words, next to a runnable example of the false negative.

- **Two examples chosen for honesty.** The orientation example uses a uniformly
  wrong list (all bytes), which random sampling catches every call; the
  false-negatives example uses a lone bad item, which it can miss. The dek and
  headline describe the reliably-caught case, not the "hidden item" case (an
  early dek draft got this wrong and was corrected).

- **Star count omitted** deliberately (evidence: counts read inconsistently
  across fetches; do not cite a precise figure). The "million downloads a day"
  milestone is included but attributed as the project's own self-reported claim.

- **Headline/dek molds varied** per the brief: not "Tool verbs your noun" (the
  surprise, one random item, is inside the headline), and the dek states the
  value plainly without the "guarantee holds on X, thins to Y" undercut.

## Open questions

- **No captured REPL.** The two code listings are illustrative and follow the
  violation shape beartype documents (the evidence itself labels them
  illustrative, not captured sessions). beartype was not executed in this round.
  If the editor wants a verbatim captured traceback, that needs a run.

- No open voice question. Register follows the voice guide's Leach/Wayne/Willison
  model: benefit stated first then earned by design, limits stated flatly as
  findings, appreciation carried by the figures rather than graded.
