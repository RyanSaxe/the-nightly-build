# Writer handoff: feature/jepsen-particledb (01)

## Original work

The piece takes each guarantee ParticleDB advertised (Full ACID, snapshot isolation, "formally proven", `occ` "Jepsen-safe", `groupsync` equal to `sync`, prepared statements "work as expected") and names the Jepsen anomaly, build and mode that falsified or could not confirm it, so a 96-issue report reads as one six-row matrix, then draws one anomaly's mechanism (`WHERE 4 = 5`) and places the findings still open at rc-22 on the tested builds.

## Proof result

- `nb stamp`: words=1074, reading_minutes=5, sources=8 (the counter includes table, SVG text, header and Sources, so the 600-1200 band holds on the strictest count).
- `nb check <article> --series feature --repo /home/user/the-nightly-build` (links included): **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE.**
- Em-dash count 0; no "What ..." headings; no "only as X" dek mould.
- Both SVGs were rendered in headless Chrome (light and dark theme tokens) and inspected: no overlapping labels, arrows land on their targets. The full page and the matrix table were not rendered through the site build; only the nb-table markup from the furniture catalog is used.

## Article shape

Orientation plus three flex sections (within the 2-4 band): the matrix (nb-table, six rows), Fig. 1 `WHERE 4 = 5` lane diagram, Fig. 2 build-range chart (7 findings, 4 open at rc-22, dashed ends for Orkes's untested rc.13 claim). Sources: 8 (Jepsen report, Jepsen G1a, P4, G-single, A5A, stale-read pages, ParticleDB modes page, Orkes blog), all from evidence.md section 6 and confirmed 200 by the researcher; the link check in `nb check` passed.

## Source nuances honored

- Advertised wording is attributed to the Jepsen report as the record; the text says Orkes has since rewritten the pages. No Wayback URL is cited (researcher could not open them).
- `groupsync`/`sync` row is labeled "A conflict between documents, not a measured failure."
- `WHERE TRUE` stated as inside a transaction, 1.1.4 through 1.1.18.8, "seemed improved" in 1.1.18.9.
- #107 and #109 are stated as reproduced under `strict-serializable` at rc-18, with the report's "may have been renamed `serializable`" note in the Fig. 2 caption; rc-22 statements are attributed to the report's Discussion.
- Funding disclosed in the second sentence block of the orientation; single-node scope stated there; Orkes's rc.13 claim attributed, called untested by Jepsen, and quoted from the Orkes blog ("As of ParticleDB 1.1.19, we report ..."), with Jepsen's rc-13 naming noted. TLA+ row says "could not be checked."

## Claims I could not source or sourced at one remove

- The home-page, docs and CLI wordings ("Full ACID. 159K TPS.", "snapshot isolation", "formally proven", "Jepsen-safe", "stronger durability") rest on the Jepsen report's quotations only; the archived pages were unreadable to the researcher. The "same durability as sync" and "all work as expected" wordings come from an unpublished operator guide, which the matrix caption says.
- Titles of the Orkes blog post and the ParticleDB modes page in the Sources list are descriptive labels, because evidence.md records their URLs and a section name but not their page titles. The editor may want to correct them against the live pages.
- The "Fig. 1" right-hand lane (rewrite of `something = x` into a key lookup) follows the report's one-sentence description; the caption says it is drawn for the article and not taken from ParticleDB's planner.
- Report sections cited in locators (e.g. §3.3.3, §3.8.16) come from evidence.md; I did not re-read the report.

## Open questions

None blocking.
