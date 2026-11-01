# Editorial review: feature/jepsen-particledb (editor 01)

## Verdict

**SETTLED.** Every required change was a direct cut I made. No writer round is
owed. The article is ready for the orchestrator to stamp and prove.

Proof after cuts: `nb check ... --series feature` → BLOCK 0, WARN 0, verdict
PUBLISHABLE.

## Direct cuts I made

1. **Section heading 1**, orientation: "Six guarantees tested one node at a
   time" → "Guarantees tested one node at a time". Three of the four flex
   headings led with a bare cardinal ("Six guarantees...", "Four of six
   claims...", "Ten issues..."), and headings 1 and 2 echoed "six" across
   adjacent lines. `spec/headlines.md` requires headings built differently from
   each other; dropping the lead number breaks the most-stamped adjacency while
   keeping the step (these guarantees, tested single-node). "Four of six" and
   "Ten" stay because each number is the finding of its section and the two are
   non-adjacent and differently built.

2. **Article's last sentence**, deleted: "The dashed ends of the four open bars
   mark that claim, which Jepsen has not tested." It was a figure-mechanics
   pointer in the position the slop standard says to test hardest. Its content
   (the rc.13 claim is untested) is already carried by "Jepsen has not evaluated
   any build after rc-22" earlier in the paragraph and by the Fig. 2 legend
   ("Orkes says fixed in rc.13, untested"), so nothing is orphaned. The piece now
   ends on "Jepsen's report names the build as 1.1.19-rc.13," which lands on the
   concrete gap between the vendor's "1.1.19" and Jepsen's "rc.13" — a stronger,
   non-generic close.

Both cuts remove text only; the band (stamped 1074) holds near ~1059, well
inside 600-1200.

## Required changes for the writer

None.

## Correctness and citations (against researcher/01/evidence.md)

Clean. Checked both halves of the matrix and every build/mode/anomaly claim:

- Matrix rows match the evidence section-by-section (caption map 3.8.7 / 3.8.8 &
  3.8.14 / 1.1 / 3.8.16 / 1.1 / 3.2.3):
  - Row 1 "Full ACID. 159K TPS." → committed-write loss, G1a, P4 across
    1.1.4–1.1.18.9, every mode, no faults (3.8.7). ✓
  - Row 2 "snapshot isolation" → G-single #73 rc-1→rc-22, A5A #106 table-2pl
    rc-18 (3.8.8, 3.8.14). ✓
  - Row 3 "formally proven" TLA+ → could not be checked, no spec (1.1/2.9). ✓
  - Row 4 occ "Jepsen-safe" → #110, 31 lost of ~20,000 keys, every few minutes,
    rc-18→rc-22, both interfaces (3.8.16). ✓
  - Row 5 groupsync "same durability as sync" → labeled a documentation
    conflict, **not** a measured failure; "stronger durability" (public docs) vs
    current live "same guarantee" (2.10/A7). ✓ Honors the nuance exactly.
  - Row 6 prepared statements "work as expected" → JDBC exception, "essentially
    unusable," #2, 1.1.4–1.1.18.9, fixed by rc-1 (3.2.3). ✓
- Anomaly definitions on first use (G1a, P4/Lost Update, G-single, A5A, stale
  read) match the Jepsen phenomena pages and are each cited to the right source
  (s2–s5, s7). ✓
- "Jepsen-safe" is correctly attributed as Orkes's own label with Jepsen's "not
  clear how to interpret" caveat (A5). ✓
- WHERE 4 = 5 (#18) wording, example rows (4,5)/(5,6), fix at 1.1.18.4, and the
  WHERE TRUE qualifier (inside a transaction, 1.1.4–1.1.18.8, improved 1.1.18.9,
  #35) are all precise (2.6). Fig. 1's rewrite lane is disclosed as drawn for the
  article, not copied from the planner.
- rc-22 section: "all but ten" resolved; stale read #109 ~every 300,000 txns at
  rc-18; Lost Update #107 under process kills same mode; the rc-18/rc-22 split
  and the "may have been renamed serializable" note are carried in the Fig. 2
  caption (2.2, 2.3, 2.12). ✓
- Original work confirmed: the piece does what the handoff claims — collapses a
  96-issue report into a six-row advertised-vs-measured matrix, then draws one
  anomaly's workings and places the still-open findings on the tested builds. No
  fabricated or decorative citation; the two descriptive Source labels (s6, s8)
  are honest descriptions, not invented page titles, and both URLs are recorded
  as resolving.

Feature-specific gates all met: each advertised claim appears in the vendor's own
quoted words before the measured result; Orkes funding disclosed; the 1.1.19-rc.13
fix attributed to Orkes and marked untested; single-node scope stated; min-5
sources (8 present); each flex section built around one cited visual; no
generalization to "databases" or "marketing" as a class ("migrate to other
databases" is Jepsen's own quoted recommendation about ParticleDB, not a class
claim).

## Headlines (spec/headlines.md + commission recent-pattern notes)

- **Headline** "Jepsen finds ParticleDB's default mode losing committed writes
  among 96 issues" — subject, fresh verb, surprise first; specific record; no
  colon subtitle, no question; number where it is the surprise. Different
  construction from the recent declarative-finding headlines. ✓
- **Dek** — adds the WHERE 4 = 5 detail the headline left out, does not restate
  it; no semicolon reversal, suspended question, or comma triad; does not reuse
  the recent "only as X" / "only in one Y" mould. ✓
- **Section headings** — no "What ..." openers (commission ban honored); after my
  cut they are built differently from each other. ✓

## Slop (spec/slop.md)

Edges tested at every paragraph, section, and the article. The how-to-read-the-
visual lines (matrix intro, bar-reading line) are the series-directed guidance
prose and name their real nouns, so they stay. No empty conclusions, performed
carefulness, puffery, vague attribution, self-reference, or decorative figures of
speech survive. The one "X, not Y" label (row 5: "a conflict between documents,
not a measured failure") corrects a real misconception stated in the piece and is
allowed. The two slop risks — the numeric-lead heading formula and the figure-
pointer closing sentence — are cut above.

## Counted bans (also confirmed by the proof)

- em-dash: 0 (max 4) ✓
- leverage: 0 (max 1) ✓
- load-bearing: 0 (max 0) ✓
- mechanism / mechanisms: 0 (press max 1) ✓
