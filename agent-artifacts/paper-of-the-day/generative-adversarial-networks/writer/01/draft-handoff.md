# Writer handoff: paper-of-the-day/generative-adversarial-networks (writer/01)

## Original work

The article's one act of original work: it reconstructs the GAN paper's proof
in the piece's own words (value function, D*, Theorem 1/JSD, and the explicit
"space of arbitrary functions" caveat), then traces each of three specific
places practice departed from that proof's assumptions — the non-saturating
objective swap the paper makes to its own proven objective, the Helvetica
scenario the paper names but does not fix, and the disjoint-support /
vanishing-gradient theorem (Arjovsky & Bottou) that explains *why* a
near-optimal discriminator starves the generator — to a single reviewer's
verdict that keeps the paper's proven result, its unproven assumptions, and
the field's actual fixes (WGAN's objective change, diffusion's displacement)
distinct rather than flattening them into one narrative. No source does this
connective work itself; each source (including the GAN paper) only supplies
one piece of it.

## Paths changed

- Article (edited in place, skeleton preserved):
  `/home/user/the-nightly-build/.nb-work/paper-of-the-day/generative-adversarial-networks/library/paper-of-the-day/generative-adversarial-networks.html`
- No source assets or charts were created (see "Furniture decisions" below).

## Furniture used

- `nb-paper-card` (abstract anchor) with the verbatim abstract quoted from
  `researcher/02/evidence.md`.
- Three `nb-math` equations: the value function (Eq. 1, captioned), the
  optimal discriminator D* (Proposition 1, captioned), and the Theorem 1 /
  JSD reduction as the article's one **annotated** equation (three
  `nb-mc1`-`nb-mc3` terms with a legend), per the brief's furniture guidance.
  Two `nb-math-in` inline spans carry the vanishing-gradient bound
  (Arjovsky & Bottou, Theorem 2.4) and WGAN's Earth-Mover distance
  definition, kept inline rather than as additional full equation blocks so
  the three recommended equations (value function, D*, Theorem-1 result)
  stay the visual center of the proof section.
- Two `nb-table`s: Lucic et al. Table 2 (all four dataset columns, three
  model rows, the "no dominant row" finding) and Dhariwal & Nichol's Table 5
  ADM-G vs. BigGAN-deep FID by resolution.
- One `nb-note` quoting Section 6's "Helvetica scenario" passage verbatim,
  and one `nb-note nb-note-strong` "Verdict" note closing the piece (the
  template's one allowed use).
- **No source asset.** The brief flagged Figure 1's four-panel schematic as
  optional and said to lean toward the equation+table doing the work; the
  article already rebuilds the D*/JSD equilibrium result in its own prose
  and an annotated equation, so a second visual of the same claim did not
  earn its place. Recorded here in case the editor weighs it differently.

## Proof result

Exact brief command:
`/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/paper-of-the-day/generative-adversarial-networks/library/paper-of-the-day/generative-adversarial-networks.html --series paper-of-the-day --library /home/user/library`

Result: **BLOCK: 0, WARN: 0**, verdict PUBLISHABLE (with link checking on,
network reachable in this environment).

`nb-meta` filled with measured values: `words: 2522`, `reading_minutes: 11`
(`max(1, round(2522/230))`), `sources: 8`, `date: 2026-08-02`,
`tags: ["research"]`, `harness: "claude-code"`, `model: "claude-sonnet-5"`.

Five `W-SENTENCE-DENSITY` warnings surfaced on the first proof pass (each a
single sentence over 55 words or 2+ clause joins, all built around a long
quotation run into its own lead-in). Each was fixed by splitting the
sentence — usually giving the quotation its own sentence rather than folding
it after a colon — not by cutting content; no claim or citation was dropped.
Re-ran to BLOCK: 0, WARN: 0.

`nb preview` was run and the built article inspected with Chromium
(`nb render-check` passed: 390px viewport, no horizontal overflow, styles
attached, no page errors). One real layout bug surfaced and was fixed before
that passed: the annotated equation's legend descriptions were originally
full sentences (~15-20 words each), which overflowed the two-column legend
grid at phone width by 16px; shortened each to a true one-line phrase per
`furniture/engine.md`'s own guidance ("WHAT THIS TERM IS, IN ONE LINE"), and
the overflow cleared.

KaTeX itself (loaded from `cdn.jsdelivr.net` per `nb.js`) could not be
confirmed rendering visually in this sandbox: the sandboxed Chromium instance
could not complete a TLS handshake through the environment's outbound proxy
to jsdelivr (`net::ERR_CONNECTION_RESET`), while a plain `curl` through the
same proxy succeeded, so this reads as a browser/proxy interaction specific
to this tool, not an article defect. Every equation string was hand-checked
for balanced braces and valid KaTeX commands, and all use only the
`\htmlClass{...}` construct `nb.js`'s documented `trust` function explicitly
allows, matching `furniture/engine.md`'s own example syntax exactly. The
editor or a later render-check in an environment with normal CDN access
should give this a final visual confirmation.

## Editorial requests addressed

None — this is draft 01, no prior editorial-review.md exists.

## Remaining evidence / voice questions

None outstanding. The evidence record's three "Contradictions" entries are
all addressed in prose: WGAN's "no mode collapse" claim is scoped as
absence-of-evidence in the "assumptions-broke" section; Lucic's finding is
kept distinct from WGAN's contribution ("different questions, neither rebuts
the other") in "the-record-after"; and the paper's own 2014 coinage of the
Helvetica scenario, versus the standard "field discovered it later" story, is
stated directly in "the-failure-named."
