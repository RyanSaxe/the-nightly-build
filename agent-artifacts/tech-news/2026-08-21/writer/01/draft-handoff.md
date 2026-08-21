# Draft handoff — tech-news/2026-08-21

## What's in the draft
Five items, in the order set in writer/01/brief.md. 11 sources, each item
carrying exactly one primary and one or two secondary citations. Title and
dek both carry item 1. Tags: ai-security, custom-silicon,
software-security, materials-science, fusion-energy. Word/reading/source
counts left at 0 for `nb stamp`.

## Self-check against spec/slop.md
- **Empty conclusions:** none found on a re-read of every paragraph edge.
  The closest calls — "what makes the episode different from a red-team
  drill" (item 1), "structured this way, the warrant works less like an
  investment" (item 2) — both resolve into a specific, checkable claim in
  the same sentence rather than trailing off into an assessment with
  nothing under it.
- **Negative parallelism:** one instance, item 1 ("different from a
  red-team drill" is not phrased as "not X, it is Y," but carries the same
  contrast). Kept because the misconception is real and named (a reader's
  first assumption about an AI sandbox escape is that escape was the
  point) — not a strawman.
- **Unearned punchlines:** none. No "that's the whole point" construction,
  no graded-the-argument sentence.
- **Fluff / filler openers:** none. Every item opens on the actor and the
  event, not a throat-clearing frame.
- **Puffery:** avoided "transformative," "landmark," "breakthrough" as
  unearned adjectives; where a result is big, a number carries it instead
  (100,000-10,000,000x, triple fusion yield, $12.2B conditional on
  purchasing).
- **Decorative analysis:** checked every "-ing" trailing clause; none
  found riding on an unattributed verb like "highlighting" or
  "underscoring."
- **Vague attribution:** every claim traces to a named person, filing, or
  organization. No "researchers say."
- **Self-reference:** none. No "this dossier," no address to the reader.
- **Formula:** headlines use five different constructions (see
  writing-coach/01/brief.md); no item closes on a terse "X, not Y" line or
  hands the point back to the reader with a generic moral.

## Vendor-benchmark qualifier
Used exactly once, on OpenAI's own "cannot rule out Critical capability"
determination — flagged in-sentence as the company's internal evaluation,
not independently reproduced. Not used anywhere else; no other item's
central number is a vendor's self-reported claim.

## Known limitation carried into the draft
Item 1 relies solely on Hugging Face's first-party technical account for
mechanism detail. A second, more elaborate version of the same incident
circulates (sourced to a Black Hat talk, describing a longer May-July
timeline involving OpenAI's own Artifactory infrastructure) but was left
out because it doesn't fully square with Hugging Face's account and isn't
independently confirmed against it. If the editor finds a way to reconcile
the two, the item could be deepened; as drafted it stays within what
Hugging Face itself has verified about its own systems.

## Proof status at handoff
First `nb check` pass returned one blocking error (nb-meta dek used
straight single quotes around "Critical" while the rendered dekline used
double quotes — fixed by making nb-meta match the rendered text exactly,
escaped for JSON) and nine warnings (eight sentence-density warnings, one
em-dash count of 17 against a limit of 4). Rewrote every flagged item to
split dense sentences and replace connective em-dashes with periods,
commas, or colons, keeping only true asides where a dash was earned.
Re-ran `nb stamp` (1,440 words, 6 min read, 11 sources) then `nb check
--series tech-news --library /home/user/library-checkout`:

    BLOCK: 0
    WARN:  0
    verdict: PUBLISHABLE
