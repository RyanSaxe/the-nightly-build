# Writing-coach brief — tech-news/2026-08-21

## What this piece is
A five-item brief template. Each item is a self-contained judgment about one
development inside technology, cited to a primary record plus at least one
independent account. The house register is Mitchell Hashimoto's technical
writing: calm, precise, argued from first principles. The reader is
technical — math/CS degrees, an ML-engineering career, well-read — so terms
of art in this domain (zero-day, sandbox escape, memristor, flexoelectricity,
warrant vesting) do not need lay definitions, but the mechanism behind each
one still has to be shown, not asserted.

## The specific failure this paper has been running into
The last two weeks of tech-news read the recent library back to front before
drafting. Four repeating tics showed up:

1. **The two-lab "X while Y" dek.** Aug 17's dek is the clearest case. This
   edition has no natural two-lab contrast to force into that shape, and none
   should be manufactured.
2. **Release-date-then-vendor-benchmark opener.** Aug 15, 16, and 17 all open
   an item with a release date and pivot straight to a number the lab
   reported about itself. None of this edition's five items lean on a
   self-reported benchmark as their evidentiary spine — the strongest
   sources here are a forensic account from the victim of an intrusion
   (Hugging Face), a regulatory filing (Marvell's 8-K), an independent
   security researcher's own write-up (Endor Labs), and two peer-reviewed
   papers. That is a structural fix, not just a phrasing one: pick items
   where the interesting number was measured or filed by someone other than
   the entity it flatters.
3. **"Unverified," "own numbers," "no independent evaluator" as the default
   frame.** The commission calls this out directly as a house tic now. This
   edition earns the caveat exactly once — the OpenAI item, where OpenAI's
   own "cannot rule out Critical capability" assessment is self-reported and
   should be marked as such once. Nowhere else does a vendor-benchmark
   qualifier belong, because nowhere else is the load-bearing number a
   vendor's own claim about itself.
4. **Terse "X, not Y" aphoristic closers.** Every item below closes on a
   specific, checkable consequence (a revised depth estimate, a required
   older release, a device that doesn't exist yet) rather than a summary
   line that hands the point back to the reader.

## Headline variety
Five items, five different constructions: a plain subject-verb-object news
lede (the OpenAI item), a mechanism-first headline built around the
conditional structure of a deal (Marvell), a "what broke" security headline
built around the artifact (isolated-vm), a number-led surprise headline
(graphene), and a consequence-led headline that states the payoff before the
method (diamond/fusion). No two open the same way, and none is a colon
subtitle or a question.

## Register notes specific to this edition
- The OpenAI item involves an AI agent acting without human direction. Do
  not anthropomorphize it further than the sources support — "the model
  found," not "the model decided" or "the model wanted." Hugging Face's own
  account is careful about this; match that care.
- The Marvell item is a financial-structuring story wearing a technology
  story's clothes. Keep the analysis on the mechanism (a purchase incentive
  disguised as an equity grant) and not on stock-price color, which is
  reported once and dropped.
- The two science items (graphene, diamond) are each one step past a single
  paper. Do not oversell either into a working device or a solved reactor —
  say plainly what has not yet been shown.
