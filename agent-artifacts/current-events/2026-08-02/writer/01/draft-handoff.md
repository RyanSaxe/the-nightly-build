# Draft handoff: current-events/2026-08-02 (writer 01)

## Original work

The article's original act is the selection-and-consequence judgment: of the
six candidates the round-2 record supports, choosing the five that clear the
commission's law/policy/institution/material-conditions bar and, for each,
stating the specific reason it matters inside the same sentence that carries
its evidence rather than after it — Trump's own disputed words as the entire
basis for a canceled strike, the unnamed suspect behind a live multi-state
water-utility intrusion, the drought figure that produced a National Guard
callout, the pilot's real deterrent effect on legitimate travelers set
against its stated purpose, and the unresolved scope of a federal
preemption ruling whose felony stakes stay paused only as long as the order
holds. Twin Falls was tested against the "no routine tragedy" standard and
dropped: the evidence found only standard emergency-response mobilization,
no policy or institutional consequence.

## Items selected

1. Iran — Trump claims a deal, cancels a strike; Iran denies it (lead)
2. Water-system cyberattacks in Michigan/Minnesota; FBI probes Iran link
3. Washington wildfire emergency, Spokane Area Fires complex
4. Visa bond program made permanent (Federal Register final rule)
5. Federal court blocks Minnesota's prediction-market ban

Twin Falls dropped per the researcher's recommendation and the commission's
"no routine tragedy" test.

## Proof result

`nb stamp` run; final `nb check ... --series current-events --library
<checkout>` (links included): **BLOCK: 0**, verdict PUBLISHABLE.

One warning intentionally left:

- **W-PLACEHOLDER** — `'OPENING OF THE HORMUZ'` flagged as a surviving
  all-caps run. This is not an unfilled slot: it is Trump's own verbatim
  capitalization from the cited Truth Social post ("Immediate, Complete, and
  Total OPENING OF THE HORMUZ STRAIT"), quoted intact because the emphasis is
  part of what the primary source actually says. Rewriting it to mixed case
  would misquote the primary. Left standing on purpose.

No other warnings survived; sentence-density and citation-order issues found
during iteration were fixed by splitting the flagged sentences and
reordering the Minnesota item's two secondary citations to match
first-appearance order.

## Open questions for the editor

- **Iran mirror primary (item 1).** The primary source is
  `trumpstruth.org/statuses/40453`, a verified real-time mirror of Trump's
  Truth Social post — Truth Social's own domain returns HTTP 403 to
  automated fetches on every attempt across both research rounds. I cited
  the mirror as `data-nb-kind="primary"` (its content is confirmed accurate
  and unmediated) and attached a `data-nb-note` disclosing the mirror status,
  with `data-nb-url` pointing to the canonical `truthsocial.com` permalink
  for a reader who wants the platform's own page. If house standard requires
  the citation `href` itself to be the originating domain rather than a
  mirror, that citation needs to move to `truthsocial.com` even though it
  won't resolve for an automated check — flagging for editorial judgment
  per the brief.
- **Water-system PSA and Minnesota court order (items 2 and 5).** Both
  primaries are real, existing federal/court documents whose text this
  writer could not read directly — the PSA returns a real PDF that
  couldn't be decoded, and the court order returned HTTP 403 at every host
  tried. Both are still cited `data-nb-kind="primary"` (they are the
  documents that own the claims), each with a `data-nb-note` disclosing
  that access was via secondary corroboration/quotation, and the specific
  quoted language in item 5 is cited to NBC News (the outlet that actually
  quotes the order), not to the order itself. If the paper's standard reads
  "primary" as requiring the writer's own direct read of the text rather
  than a corroborated-primary posture, both notes should be reviewed against
  that bar.
