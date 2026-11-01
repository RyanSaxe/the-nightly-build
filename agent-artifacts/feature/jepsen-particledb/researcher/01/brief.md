# researcher brief: feature/jepsen-particledb (01)

Inputs:
- `../../editorial-direction.md` — the full standing editorial standard.
- `../../commission.md` — the story, the finding, the matrix the piece is built around, and the disclosure.
Output: `evidence.md` (write it beside this brief).

Work from these inputs. You have web search/fetch. Do not tour the repository.
Where something you need is missing, ask me (the orchestrator).

First task, before anything else: open `https://jepsen.io/analyses/particledb-1.1.4`
and confirm it is a real Jepsen report. Read it in full (about 137,000
characters — page through it; do not stop at the first screen). If the page does
not resolve or is not a genuine report, STOP and tell me immediately; the whole
feature depends on it.

Then assemble the evidence for the claim-versus-evidence matrix. The matrix has
two halves and you must source both:

**The advertised claims (ParticleDB / Orkes's own words).** Find and record the
exact wording and the exact URL for each:
- "Full ACID. 159K TPS." and any "snapshot isolation" wording — the ParticleDB
  or Orkes marketing page.
- The "formally proven" / TLA+ claim.
- The `occ` mode described as "Jepsen-safe" and/or "safe under concurrency" — the
  docs or CLI reference.
- The `sync` vs `groupsync` durability wording (the docs say `sync` gives
  "stronger durability"; the operator guide says `groupsync` gives the "same
  durability as `sync`").
- "prepared statements … work as expected" or equivalent.
Quote each claim verbatim with its URL and retrieval date. If a claim is only
visible inside the Jepsen report (because Jepsen quotes the vendor page), record
that and still try to find the live source page.

**The measured behavior (Jepsen's findings).** For each advertised claim, record
the specific anomaly or result that falsifies or fails to confirm it, with a
short verbatim quote and the report section. Cover at least: lost committed
writes in default `occ`; Lost Update (P4) under `serializable` after process
kills; stale reads under `strict-serializable`; read skew (A5A) with
`table-2pl`; G-single, G1a (aborted read), G1b (intermediate read); the
wrong-predicate results (`WHERE 4 = 5` matching primary key 5; `WHERE TRUE`
returning nothing); ignored `NOT NULL`/`UNIQUE`; WAL-bitflip and misdirected-I/O
data loss; and the TLA+ "formally proven" claim that could not be checked because
no specification was provided.

**The vendor response.** Record Orkes's statement that 1.1.19-rc.13 resolves all
issues (quote it and its location), that Jepsen did not test it, and that Orkes
funded the analysis.

**Anomaly vocabulary (one grounding source).** Find one citable reference that
defines the anomaly terms the piece uses (Jepsen's consistency-models page, or
Kingsbury & Alvaro's "Elle" paper, or Adya's isolation taxonomy). Record a one-
line definition for Lost Update, read skew (A5A), G-single, and aborted read
(G1a) from it, with the URL.

Also note anything disputed or easy to overstate: single-node scope only (no
replication), the funded-by-vendor arrangement, and that "most issues appeared
resolved by the last tested build" while the default mode still lost writes.

Organize `evidence.md` as: (1) the advertised claims with exact quotes+URLs, (2)
the matched Jepsen findings with quotes+sections, (3) the vendor response, (4)
the anomaly definitions, (5) a short list of caveats. Confirm every URL resolves
(min 5 sources for the piece). Your own prose meets `spec/slop.md`. When done,
reply with a 4-6 sentence summary, flag any claim you could NOT source, and
confirm the output path.
