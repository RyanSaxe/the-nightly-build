# Draft handoff: feature/covid-test-negative-sequelae (writer 01)

## Original work

The article puts the PNAS paper's two designs, its placebo-case run and the
earlier VA, Maccabi and RECOVER studies in one comparison, sorted by which way
each comparison group pushes its estimate. It then uses the negative-control
results to separate what the claims establish (most of the unrestricted
design's second-year count comes from its comparison group) from what they do
not (any share of the VA studies' own findings).

## Proof

`nb check ... --series feature --repo /home/user/the-nightly-build` with links:
BLOCK: 0, WARN: 0, verdict PUBLISHABLE. Stamped at 1184 words, 10 sources,
5 minutes. That is close to the strict 1200 ceiling. The proof counts the
title, SVG labels, table cells and source labels, so an edit that adds words
needs a matching cut.

Visuals were checked with `nb preview` and Playwright (system Chrome) at 390px
and 1280px, light and dark. Neither width scrolls horizontally. On a phone the
four-column table scrolls inside its own wrapper, as the runtime intends.

## Judgment calls for the editor

- Fig. 2 shows the SI Fig. S5 shares (RR ≥ 1.1, no significance filter) and
  not the Bonferroni counts. The caption says so. The commission did not
  specify a placebo visual. I drew one because the placebo run is the
  strongest evidence for the comparison-group explanation.
- The table's "Toward the null" for RECOVER applies Ayoubkhani's general
  statement ("any control group defined by negative tests") to RECOVER's
  negative-test-indexed uninfected group. RECOVER's own bias direction is not
  measured anywhere in the record.
- "Nobody has rerun the VA data with a test-based design" and "No researcher
  outside the team has commented publicly yet" come from the researcher's
  Limits. Neither has a citation of its own. The second sits beside CIDRAP's
  9 November report, which quotes only the authors.
- I dropped the Leskovec "wrong question" quote to stay under 1200 words. I
  had verified its wording against the healthcare-in-europe.com reprint of
  the Stanford release, since EurekAlert! returns 403. Source 6 (the release)
  now backs only the point that claims miss uncoded fatigue and cognitive
  symptoms.
- The Cai 2024 three-year VA paper was cut for length. The VA row covers the
  2021 and 2023 papers.
- Source 2 links to the PMC article with a `#supplementary-material` fragment.
  The link check passed, but I did not confirm that the anchor lands on the
  supplement block. The note names the SI file.

## Open questions

None blocking.
