# writer brief: feature/jepsen-particledb (01)

Inputs:
- `../../editorial-direction.md` — the full standing editorial standard.
- `../../commission.md` — the story, the finding, the disclosure, the visuals, and the recent-pattern notes to break.
- `../../writing-coach/01/voice-guide.md` — how the piece sounds.
- `../../researcher/01/evidence.md` — the anchored claims and findings; cite from here.
- The article file to write into (already initialized, do not recreate its skeleton):
  `/home/user/the-nightly-build/.nb-work/feature/jepsen-particledb/library/feature/jepsen-particledb.html`
Output: `draft-handoff.md` (beside this brief) AND the finished article HTML at the path above.
Proof: `/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/jepsen-particledb/library/feature/jepsen-particledb.html --series feature --repo /home/user/the-nightly-build`

Work from these inputs. Do not tour the repository or the archive; you may open
the engine/press furniture catalogs named in the editorial direction for the
exact HTML of `nb-table`, `nb-figure` and inline-SVG furniture. Where something
you need is missing, ask me (the orchestrator).

This is a five-minute Feature (600-1200 words, the series is STRICT so the band
is a hard limit; flex sections 2-4, each cited). Open with the finding in two or
three sentences, then build each section around one visual with short prose on
how to read it and what follows.

The piece: hold ParticleDB's advertised guarantees against what Jepsen measured
in its 2026-10-31 report. The central visual is the claim-versus-evidence matrix
(`nb-table`): each row a documented guarantee (Full ACID; snapshot isolation;
"formally proven" via TLA+; `occ` "Jepsen-safe"; `groupsync` durability equal to
`sync`; prepared statements "work as expected"), each cell the Jepsen result
that falsified or could not confirm it, with the citation in the caption. Add at
least one more visual that shows a mechanism, not a list — a small inline-SVG of
one concrete anomaly (the default-mode lost committed write, or the `WHERE 4 = 5`
predicate bug resolving to a primary-key lookup), drawn with theme variables
(`var(--ink)` etc.), `aria-label`, `style="width:100%;min-width:34rem;height:auto"`,
figure `overflow-x:auto`. Define each isolation anomaly in plain words on first
use (Lost Update, read skew / A5A, G-single, aborted read / G1a, stale read).

Non-negotiable fairness and accuracy:
- State each advertised claim in ParticleDB/Orkes's own words (from `evidence.md`)
  before giving the measured result.
- Disclose that Orkes, the vendor, funded the analysis.
- Report Orkes's statement that a later candidate build (1.1.19-rc.13) resolves
  the issues as the vendor's attributed, unverified claim (Jepsen did not test it).
- Note the scope: single-node only (replication not provided).
- Do not generalize to "databases" or "marketing" as a class. Stay on this
  report and these claims. No self-reference, no newsroom voice.

Citations: every section carries at least one cite to a Sources entry drawn from
`evidence.md` (min 5 sources). Keep the `nb-meta` JSON and the fixed chrome
(`<body class="nb-article">`, `<h2>Sources</h2>`) intact; fill title, dek, date
(2026-11-01), two-to-four named flex sections, and Sources. Do not stamp counts
by hand. Headlines/deks/headings obey `spec/headlines.md` and the commission's
recent-pattern notes (no "What …" headings, no recent dek mould, build headings
differently from each other).

Run the proof yourself and fix what it reports before handing off. In
`draft-handoff.md` record: the proof result, the one-sentence statement of the
piece's original work, and any claim you could not source (ask me rather than
guess). Meet `spec/slop.md` throughout; test the first and last sentence of each
section and the article's last sentence hardest.

## Source nuances the researcher established (honor these exactly)

- The live ParticleDB/Orkes pages were REWRITTEN and no longer carry the
  advertised wording ("Full ACID. 159K TPS.", "snapshot isolation", "formally
  proven", `occ` "safe under concurrency"/"Jepsen-safe", "stronger durability").
  The record for those claims is the Jepsen report's own quotations of them (and
  the web.archive.org snapshots it cites). Attribute each advertised claim to the
  Jepsen report as the source of record; do NOT write that a live page currently
  says it. You may add an archive URL only if it actually resolves — do not add a
  source you have not confirmed resolves, because the proof checks links.
- The `sync` vs `groupsync` item is a DOCUMENTATION inconsistency (the docs
  contradict the operator guide), not a measured durability anomaly. Label that
  matrix row accordingly; do not present it as an observed failure.
- `WHERE TRUE` returned nothing only INSIDE a transaction, on versions 1.1.4
  through 1.1.18.8 (issue #35). Keep that qualifier.
- Lost Update after process kills (#107) was reproduced under
  `strict-serializable` at rc-18; the report notes that mode "may have been
  renamed" `serializable` in rc-22. Stale reads (#109) have the same rc-18/rc-22
  split. State the mode and version precisely; do not flatten these.
- The `occ` default-mode lost-write and the wrong-predicate result (`WHERE 4 = 5`
  matching primary key 5) are the cleanest, best-attested findings — good
  anchors for the central visual and the mechanism diagram.
- Sources (min 5), all must resolve: the Jepsen report; the Orkes blog post
  (`https://orkes.io/blog/particledb-database-built-for-ai-agents`, which states
  "As of ParticleDB 1.1.19, we report that all identified issues have been
  addressed"); and Jepsen's anomaly-definition pages (P4 / A5A / G-single / G1a /
  stale read) for the vocabulary. Draw them from `evidence.md`, which has the
  exact URLs the researcher confirmed resolve.
