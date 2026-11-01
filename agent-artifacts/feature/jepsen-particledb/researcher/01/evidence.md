# Evidence record: feature/jepsen-particledb (researcher 01)

Retrieved 2026-11-01. "Report" below means https://jepsen.io/analyses/particledb-1.1.4.

## 0. Gate: is the report real?

Yes. `https://jepsen.io/analyses/particledb-1.1.4` returns HTTP 200 on jepsen.io, titled "ParticleDB 1.1.4", author Kyle Kingsbury, dated 2026-10-31, with a PDF at `/analyses/particledb-1.1.4.pdf` linked from the page. I downloaded the full HTML (about 144k characters as text) and read every section: intro, 1 Background, 2 Test Design, 3 Results (3.1 to 3.9 and the summary table), 4 Discussion (4.1 to 4.6), and the Appendix A headings. Every finding and quote below comes from a passage I read in that text. Section numbers are the report's own.

Where the vendor's original page text is quoted below, it is quoted as Jepsen printed it. The live vendor pages have since been rewritten (see section 1), and the Wayback captures Jepsen links could not be opened from this environment (connection reset by web.archive.org through the proxy). So the vendor-side wording is sourced to the Report, with the archive URL Jepsen cites, and is not independently re-read on the archived page.

## 1. The advertised claims

Each row: the vendor's wording, where Jepsen printed it, the URL Jepsen cites for it, and what I could verify myself.

| # | Claim (verbatim) | Source and location | URL Jepsen cites | Verified by me |
|---|---|---|---|---|
| A1 | "Full ACID. 159K TPS." Home page "proudly claimed" it. | Report 1.1 Safety, para beginning "ParticleDB's home page proudly claimed" | `https://web.archive.org/web/20260518203012/https://particledb.ai/` (the 1.1 link for the home page, captured 2026-05-18) | Report text read. Archive page not openable. Live `https://particledb.ai/` (HTTP 200) no longer contains "Full ACID", "159K" or "formally"; it now says "SQL, joins and ACID transactions". |
| A2 | "snapshot isolation", in the text immediately below "Full ACID. 159K TPS." Jepsen adds that this "is not fully isolated" and links its Snapshot Isolation page. | Report 1.1 Safety, same paragraph | Same archived home page | Report text read. Jepsen's SI page (`https://jepsen.io/consistency/models/snapshot-isolation`, HTTP 200) says the most notable phenomena SI allows are write skews. |
| A3 | "formally proven" with a TLA+ proof. Report 4.4 also gives "formally verified" by a TLA+ proof. | Report 1.1 Safety (first para) and 4.4 Documentation | Same archived home page | Report text read. Archive not openable. Note the two spellings: 1.1 says "formally proven", 4.4 says "formally verified". |
| A4 | occ "safe under concurrency" (transaction-modes table, "When to use" column: "General OLTP — safe under concurrency"). | Report 1.1 Safety, the four-mode table, and 4.4 | `https://web.archive.org/web/20260518193013/https://particledb.ai/architecture/transaction-engine/#transaction-modes` (4.4 links a second capture of `getting-started/concepts`) | Report text read. Live `https://particledb.ai/architecture/transaction-engine/` (HTTP 200) now only redirects to `/sql/transactions/`. |
| A5 | occ "Jepsen-safe": the CLI reference table described `occ` and `table-2pl` as "Jepsen-safe"; `fast` was not. | Report 1.1 Safety, para beginning "The CLI reference page" | `https://web.archive.org/web/20260518193140/https://particledb.ai/operations/cli-reference/` | Report text read. Live `https://particledb.ai/operations/cli-reference/` (HTTP 200) has no "Jepsen-safe" text. Jepsen's own comment: "Since Jepsen evaluates safety with respect to documentation and marketing claims, it is not clear how to interpret these terms." |
| A6 | `particledb start --help` described occ as "Table locks + commit-time validation (safe for most OLTP)". Jepsen: "'safe for most OLTP' undermines the claim that occ was 'safe under concurrency'". | Report 1.1 Safety | none (CLI output) | Report text read. |
| A7 | Docs described `sync` as offering "stronger durability" than `groupsync`. The CLI help said groupsync means "COMMIT waits for flush". Orkes' unpublished operator guide said groupsync gives the "same durability as sync". | Report 1.1 Safety, WAL paragraph | Docs: `https://web.archive.org/web/20260518193013/https://particledb.ai/architecture/transaction-engine/#wal-sync-modes`. CLI help and operator guide: no URL (the guide was unpublished). | The "stronger durability" quote is a public-docs claim. The "same durability as `sync`" quote is from an unpublished guide, so the contradiction is between public docs and a private document. Current live wording (changed since): `https://particledb.ai/operations/modes/#durability---durability` says "groupsync and sync give the same guarantee; groupsync is faster under concurrency because one flush covers many commits." |
| A8 | "prepared statements, parameterised queries, and extended-query pipelining all work as expected." | Report 3.2 Broken Features, block quote after "the internal operator guide concurred" | The paragraph links the public page `https://web.archive.org/web/20260519195820/https://particledb.ai/connectivity/pg-wire/` for "broad support for Postgres features". The block quote itself is attributed to the internal operator guide. | Do not attribute this exact sentence to a public page. Live `https://particledb.ai/connectivity/pg-wire/` (HTTP 200) has no match for "prepared" or "work as expected". |
| A9 | "1087x faster than PostgreSQL". | Report 4.6 Future Work | none | Optional. Not in the commission matrix. |

Not sourced as a live vendor page: A1, A2, A3, A4, A5, A7 (public-docs half), A8 (public half). The original marketing and docs pages were rewritten before 2026-11-01. The Report is the only readable record of the exact wording, and the archive captures it links are the primary sources a reader can check. I could not open them.

## 2. Matched Jepsen findings

Versions: the report tested 1.1.4 through 1.1.18.11.rc-22. "Fixed in" values below are from the report's summary table and are Orkes' claims where they name a 1.1.19 build.

### 2.1 Default `occ` loses committed writes (matches A4, A5, A1 "Durability")

- Report 3.8.16 "Lost Writes (#110)": "In version 1.1.18.11.rc-18 through 1.1.18.11.rc-22, a healthy ParticleDB node running occ-v3, zero-copy-occ, table-2pl, or serializable-ssi would occasionally discard acknowledged writes." Example: "Out of approximately 20,000 keys, 31 lost writes", run with WAL mode `sync`. "This occurred every few minutes in our tests, with both the Postgres and ParticleDB interfaces." Fix: "Orkes released version 1.1.19-rc.13, and believes that it fixes this issue".
- Report intro: "ParticleDB continued to lose committed writes during normal operation with the default occ transaction mode".
- Report 4 Discussion: "The default occ mode regularly lost data in normal operation (#110)."
- Earlier builds: 3.8.7 "A Thousand Tableaus": "We routinely observed the loss of committed writes, internal consistency violations, G1a (Aborted Read), G1b (Intermediate Read), and P4 (Lost Update)" in 1.1.4 through 1.1.18.9, "These issues occurred with a single server and without faults, and affected every transaction mode, interface, and WAL mode tested."
- Default identification: Report 1.1: "Sources disagreed about the default transaction and WAL sync modes, but in general, occ-v3 and groupsync appeared to be the default." The #110 example ran under `sync`, not `groupsync`.

### 2.2 `serializable`: Lost Update after process kills (matches the strongest-mode claim)

- Report 3.9.3 "Internal Anomalies With strict-serializable and Process Kills (#107)": with `strict-serializable`, `groupsync`, the ParticleDB interface, rc-18, process kills. "Transactions could also exhibit G-single and P4 (G-single), but we suspect these could be due to the same underlying bug." Fix: "Orkes claims this issue (#107) was resolved in version 1.1.19-rc.12."
- Report 4 Discussion: "When we killed ParticleDB, it allowed internal anomalies, P4 (Lost Update), and G-single (#107), even with the new serializable transaction mode." And: "with process kills, sometimes failed to read extant rows. This led to internal anomalies, Lost Update, and more (#107)."
- Naming caveat (footnote 9): `strict-serializable` "may have been renamed to serializable in 1.1.18.11.rc-22". The 3.9.3 test itself ran rc-18 under the name `strict-serializable`. The Discussion's statement about the new `serializable` mode comes from the rc-22 testing, and the report does not give a separate reproduction for rc-22 in 3.9.3.
- Report 4.1: in rc-22 with WAL mode `sync` and `serializable`, the mode "significantly reduced the frequency and severity of these issues, but did not prevent internal anomalies or Lost Update."

### 2.3 `strict-serializable`: stale reads

- Report 3.8.15 "Stale Read With strict-serializable (#109)": "Healthy ParticleDB nodes infrequently but regularly exhibited Stale Read, even with WAL mode sync." Rate: "roughly every 300,000 transactions, using Elle's exponential key distribution and 10 concurrent clients pushing ~80 transactions per second." Result: "a violation of Strong Snapshot Isolation, and therefore Strong Serializability as well." Fix: "Orkes reported that version 1.1.19-rc.10 no longer exhibits stale read".
- Version caveat: 3.8.15 tested rc-18. The Discussion says the new `serializable` mode in rc-22 "still allowed stale read (#109) in normal operation". I found no separate rc-22 reproduction in 3.8.15. Cite the Discussion for the rc-22 statement.

### 2.4 Read skew (A5A) with `table-2pl`; G-single

- Report 3.8.14 "Read Skew With table-2pl (#106)": "version 1.1.18.11.rc-18 exhibited G-single under normal operation" (ParticleDB interface, groupsync). "Since it observed but also failed to observe another transaction, this is A5A (Read Skew)." "Both are violations of Snapshot Isolation." Fixed: "We no longer observed Read Skew with table-2pl (#106) by version 1.1.18.11.rc-19."
- Report 3.8.8 "G-Single (#73)": "With versions 1.1.18.11.rc-1 through 1.1.18.11.rc-22, we occasionally observed G-single, a violation of Snapshot Isolation, in single nodes without faults", on `occ-v3` with `groupsync`, and in `zero-copy-occ` and rc-22's `occ`. Orkes "reports version 1.1.19-rc.13 no longer exhibits G-Single." This is the finding that most directly contradicts the "snapshot isolation" label on the occ modes.
- Report 3.8.11 "Internal Anomalies With occ-v3 (#96)": rc-9.2, `occ-v3`, `groupsync`; one transaction "read nil, then [1, 4] for key 8", which "violates Snapshot Isolation and Serializability". "may have been resolved by 1.1.18.11.rc-19."

### 2.5 G1a (aborted read), G1b (intermediate read)

- Report 3.8.7 (above): G1a and G1b observed in 1.1.4 through 1.1.18.9; "By version 1.1.18.11.rc-1, ParticleDB's most glaring examples of G1a (#66), G1b (#38), internal consistency anomalies (#68), write loss (#69), and so on were much diminished." The report omits detailed examples; the summary table lists #66 and #38.
- Report 3.8.2 "Aborted Transactions Can Commit (#43)": "Between versions 1.1.17 and 1.1.18.4 ... the writes performed by the aborted transaction persisted" via the Postgres interface (after a parse error, COMMIT returned ROLLBACK, yet the insert was visible). Resolved: both interfaces as of rc-18 "returned errors and did not expose the effects of aborted transactions".
- Discussion: "Each transaction and WAL mode exhibited essentially every transactional anomaly our tests could detect: write loss, internal consistency violations, G0, G1a, G1b, G1c, G-Single, G-nonadjacent, P4, A5A, G2, and real-time variants thereof".

### 2.6 Wrong-predicate results (matches "Full ACID" as general correctness; no vendor claim is directly on this)

- `WHERE 4 = 5`: Report 3.3.3 "WHERE 4 = 5 (#18)": "ParticleDB 1.1.4 through 1.1.17 aggressively interpreted WHERE something = x as a primary-key lookup of x, regardless of the value of something." Example with `t(a int primary key, b int)` rows (4,5) and (5,6): `SELECT * FROM t WHERE 4 = 5;` returned the row `5 | 6`. Fixed: "By version 1.1.18.4, ParticleDB had learned that not every equality comparison involved a primary key".
- `WHERE TRUE` returning nothing: Report 3.3.4 "SELECT in a Transaction Returns Nonsense (#35)": inside `BEGIN`, in 1.1.18.8, `SELECT * FROM t WHERE TRUE;` returned `(0 rows)` and `WHERE 3 = 3` returned `(0 rows)`, while `WHERE a = 1` returned the row with `a = 2`. This was inside a transaction, versions 1.1.4 through 1.1.18.8. "seemed improved by ParticleDB 1.1.18.9." Wording to avoid: the commission says "sometimes returning nothing"; the supported statement is "within a transaction, in 1.1.4 through 1.1.18.8". A separate nondeterministic case (3.8.13, #31) had `SELECT * FROM t_876 WHERE TRUE` return one of two rows, versions 1.1.18.8 through rc-22; Jepsen says it "may be artifacts of a bug in the test suite".
- Also 3.3.1 (#40): `SELECT 5 WHERE FALSE;` returned `5`, 1.1.4 to 1.1.18.9.

### 2.7 Ignored constraints

- Report 3.4.1 "Not-Null Constraints Allow Null (#8)": "versions 1.1.4 through 1.1.17 ignored them"; `INSERT INTO t (a) VALUES (NULL)` into `a BOOLEAN NOT NULL` returned `INSERT 0 1`; "In version 1.1.18.4, ParticleDB started to enforce null constraints".
- Report 3.4.2 "Unique Constraints Allow Duplicates (#9)": "versions 1.1.4 through 1.1.18.4 simply ignored them"; "In version 1.1.18.6, ParticleDB partially enforced unique constraints".
- Also 3.4.3 (#29) duplicate primary keys via UPDATE, 1.1.4 to 1.1.18.8; and Discussion 4.2: ParticleDB checks unique constraints "after all have been updated", unlike Postgres.

### 2.8 WAL bitflips and misdirected I/O (durability, A1 "D")

- Report 3.9.1 "Data Loss on WAL Bitflips (#108)": rc-18. After two single-bit errors in a `.wal` file, "ParticleDB would discover that its data files were corrupt, then start up anyway, serving data to clients." Key 1754 held 44 elements, then `[81]` after restart. "Several other keys also lost some or all of their acknowledged writes." Orkes "reports 1.1.19-rc.12 detects bitflips correctly and refuses to start"; Jepsen has not tested it.
- Report 3.9.2 "Total Data Loss With Simulated Misdirected Reads/Writes (#112)": rc-22. The harness shuffled "13 four-kilobyte chunks of the first .wal file" (about one-tenth of the file). On restart ParticleDB logged "No data found in storage — starting fresh", then "ERROR: table not found for every query". "It appears that ParticleDB may have deleted the contents of its WAL file." Orkes believes rc-12 resolves it.
- Scope: Section 3 intro: "All but three of these issues occurred in healthy, single-node instances". The three are the fault-injection findings in 3.9.

### 2.9 "Formally proven" / TLA+ (A3)

- Report 1.1: "However, during our collaboration no TLA+ specification was available. It is unclear what properties might be proven, or whether they described ParticleDB as built."
- Report 4.4: "The TLA+ proof was not published, and in any event did not prevent disaster—perhaps it was incorrect, formalized the wrong properties, or did not describe the system as built."
- So the claim was not checkable, not shown false. Say "could not be checked", as the commission does.

### 2.10 `groupsync` equals `sync` (A7)

Jepsen's finding here concerns the documentation, not measured behavior. Report 1.1 reports the contradiction between the public docs ("stronger durability") and CLI help and the unpublished guide ("same durability as sync"). I found no result in the report that tests a durability difference between `sync` and `groupsync`. The harness had LazyFS (loss of un-fsynced writes) and "ran ParticleDB using each transaction mode and all three WAL sync modes" (Report 2), but no `sync` vs `groupsync` loss comparison is reported. The row in the matrix should say "documentation contradicts itself; Jepsen reports no durability comparison". Jepsen's data-loss findings used both modes: #110 under `sync`, #107 and #96 under `groupsync`.

### 2.11 Prepared statements (A8)

- Report 3.2.3 "Malformed Responses for Prepared Statements (#2)": "In ParticleDB 1.1.4 through 1.1.18.9, any attempt to execute a prepared statement using the Postgres JDBC driver caused an exception like Execution error (NoSuchElementException) at java.util.ArrayDeque/removeFirst." The JDBC driver switches to prepared statements "after the first few calls to execute()", "this rendered the database essentially unusable." Jepsen disabled client prepared statements as a workaround. "By version 1.1.18.11.rc-1, this issue (#2) appeared fixed." Jepsen's verdict on the quoted claim: "These claims were somewhat optimistic."

### 2.12 Report's overall verdicts (for the opening)

- Intro: "found that ParticleDB's claims of 'Full ACID' were somewhat premature. We present 96 issues ... By version 1.1.18.11.rc-22, all but ten of those issues appeared resolved." I counted the ten from the summary table: #83, #111, #54, #73, #31, #109, #110, #108, #112, #107, the ones whose "Fixed in" is a 1.1.19 build.
- Report 4.1 Impact: "Jepsen recommends users halt further deployment of ParticleDB and migrate to other databases as soon as possible."
- Report 4 Discussion: "While 1.1.18.11.rc-22 was significantly safer than 1.1.4, we were still finding new issues."
- Report 4.6: "As of 1.1.18.11.rc-22, our append and rw workloads were still finding anomalies in every transaction mode."

## 3. Vendor response and funding

- Funding: Report intro, repeated at the end of 4.6: "This research was funded by Orkes, Inc., and conducted in accordance with the Jepsen ethics policy." Policy page `https://jepsen.io/analyses/ethics` (HTTP 200). The Orkes blog post does not mention funding.
- Orkes' claim, as Jepsen reports it: intro, "Orkes, the makers of ParticleDB, have since released version 1.1.19-rc.13; they claim that it resolves all remaining issues discussed in this report." Linked to `https://orkes.io/blog/particledb-database-built-for-ai-agents`.
- Report 4 Discussion: "Jepsen has not evaluated versions of ParticleDB after 1.1.18.11.rc-22, and cannot speak to these isolation levels or concurrency control modes. However, Orkes claims that all issues from this report have been addressed as of version 1.1.19-rc.13." Report 3.2.5 says the same for #111: "While Jepsen has not tested this version".
- Orkes' own statement, opened at `https://orkes.io/blog/particledb-database-built-for-ai-agents` (HTTP 200, "Last updated: October 30, 2026"), section "What we learned from Jepsen": "Jepsen tested ParticleDB versions 1.1.4 through 1.1.18.11.rc-22, identifying 96 issues spanning SQL correctness, transaction isolation, concurrency anomalies, and data loss." and "We took these findings seriously and worked through the reported issues. As of ParticleDB 1.1.19, we report that all identified issues have been addressed." Note the version precision differs: Orkes' blog says "1.1.19", Jepsen says "1.1.19-rc.13". The blog links the Jepsen report.
- The fix claims are spread over several builds in the report's summary table: rc.10 (#109), rc.12 (#83, #108, #112, #107), rc.13 (#111, #54, #73, #31, #110).
- Orkes' later documentation change, which Jepsen disputes (Report 4 Discussion): "Orkes updated ParticleDB's documentation to claim that every transaction mode discussed here was 'experimental'. This claim is difficult to support. To the best of Jepsen's knowledge, none of the ParticleDB documentation described these modes as experimental or unsupported during our engagement." Orkes' live page: `https://particledb.ai/operations/modes/#experimental-modes-not-in-current-release-builds` says the modes "were never a supported configuration" and "Independent testing of those builds found safety errors in them." The live release page `https://particledb.ai/installation/releases/` calls the tested builds "Unsupported pre-release builds" and lists 1.1.19-rc.16 (2026-10-30) as current. Jepsen on that label: "It is not clear how users would have understood versions like 1.1.4 or 1.1.18.9 as 'pre-release'" (4.4).
- Orkes' explanation (Report 4.1): the issues "were likely due to an extensive refactor of ParticleDB in spring 2026", and Orkes and its customers, "who continued to run an earlier version, were likely unaffected." Jepsen briefly tested an internal 1.0.0 build: it "did not seem susceptible to most of the serious safety errors we found in 1.1.4".

## 4. Anomaly definitions (one grounding family: Jepsen's phenomena pages, which cite Adya and Berenson et al.)

All URLs opened, HTTP 200, on 2026-11-01.

- Lost Update (P4): `https://jepsen.io/consistency/phenomena/p4`. "Phenomenon P4, or Lost Update, occurs when the effects of a committed transaction are effectively lost." Berenson et al.: Ti reads xi, then writes a new version while a second transaction Tj writes xj in between. Because Ti did not observe xj, Tj's write is effectively lost. It "is therefore a special case of G-single." (The site has no `phenomena/lost-update` page; that URL returns 404.)
- Read skew (A5A): `https://jepsen.io/consistency/phenomena/a5a`. "A5A, also known as Read Skew, happens when a transaction both observes and fails to observe the effects of another transaction." Special case of G-single. Allowed by Read Committed, proscribed by Snapshot Isolation.
- G-single: `https://jepsen.io/consistency/phenomena/g-single`. "a cycle containing exactly one read-write dependency between transactions." Intuition: "a single transaction observes ... another transaction, but also misses some effect of that same transaction." Proscribed by Snapshot Isolation and stronger. Formal definition from Adya's thesis (section 4.1.1): a directed cycle in the DSG with exactly one anti-dependency edge. P4 and A5A are specific kinds of G-single.
- Aborted read (G1a): `https://jepsen.io/consistency/phenomena/g1a`. "occurs when a write performed by an aborted transaction is read by a committed transaction." Proscribed by Read Committed.
- Stale read: `https://jepsen.io/consistency/phenomena/stale-read`. A real-time phenomenon in which "a read fails to observe the consequences of an earlier completed write." Prohibited by Strict Serializability and Linearizability, permitted by plain Serializability.
- Snapshot isolation and why "snapshot isolation" is weaker than "Full ACID" isolation: `https://jepsen.io/consistency/models/snapshot-isolation`: "The most notable phenomena allowed by snapshot isolation are write skews".
- Cited inside those pages but not opened by me: Adya's thesis `https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TR-786.pdf`; Berenson et al. `https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-95-51.pdf`. Cite the Jepsen pages unless someone opens them.

G1b (intermediate read) is named in the report (3.8.7) but I did not fetch its Jepsen page. `https://jepsen.io/consistency/phenomena/g1b` is the pattern of the other URLs and I did not verify it. Do not cite it unverified.

## 5. Caveats and easy-to-overstate points

1. Funded by the vendor. Orkes paid for the analysis; the report says so twice. Jepsen published 96 issues and recommended users "halt further deployment". The arrangement is Jepsen's normal one (Report intro, ethics page). The commission's framing stands.
2. Single node only. Replication (Raft) was available only in enterprise cloud deployments, and "The builds Orkes provided did not support replication, so this report covers only single-node behavior" (Report 1; 4.1). Nothing here speaks to clusters.
3. What was resolved by the last tested build. By rc-22, "all but ten" issues appeared resolved. Do not write "ParticleDB lost data in all modes at the end": the report says `occ` (default) regularly lost data (#110), `serializable` allowed stale read and Lost Update after kills, and `append`/`rw` still found anomalies "in every transaction mode" (4.6).
4. Versions differ per finding. #18 (`WHERE 4 = 5`) was fixed by 1.1.18.4; #35 by 1.1.18.9; #8 by 1.1.18.4. A piece that lists these in one table must carry a "last version affected" or "fixed in" column, or readers will think they were present at rc-22. The seven in the ten still open at rc-22 that matter to the matrix: #73, #31, #109, #110, #108, #112, #107. The other three (#83, #111, #54) are a Postgres-interface failure in rc-7 to rc-19, a protocol-state error in rc-18 and rc-19, and join column names.
5. Rc-22 renamed modes. `strict-serializable` (rc-18) "may have been renamed to serializable" in rc-22; `table-2pl` and `serializable-ssi` were dropped (Discussion). Use the mode name with the version.
6. Vendor claims are unverified. Orkes' 1.1.19-rc.13 resolution claim is not tested by Jepsen. Orkes' blog says "As of ParticleDB 1.1.19", while Jepsen's text names rc-13. The live modes page makes it unclear whether removed modes were removed or renamed (Jepsen, 4 Discussion: "It is not clear whether these modes were removed or simply renamed").
7. "Jepsen-safe" is a vendor label, not a Jepsen verdict. Jepsen printed the label and said it did not know how to interpret it (Report 1.1). Do not imply Jepsen rated anything.
8. Quote attribution. The "same durability as sync" and "work as expected" quotes come from an unpublished operator guide that Orkes gave Jepsen, not from public pages. A reader cannot check them except through the report.
9. Original marketing text is no longer live. The home page and docs now read differently. Cite the Report for the original wording, and the Wayback URLs Jepsen gives as the pointers a reader can try. I could not open them.
10. The `groupsync`/`sync` row is a documentation inconsistency, not a measured anomaly (section 2.10). The commission's matrix row for it should say that.
11. The `WHERE TRUE` case was inside a transaction in 1.1.18.8 and earlier (section 2.6).
12. Jepsen's scope disclaimer (4 Discussion): "we can prove the presence of bugs, but not their absence."
13. Report 4.5 and 4.3 speculate about LLM-assisted development ("Perhaps engineers entrusted Large Language Models with the work of testing"). That is Jepsen's conjecture and not part of the commission; do not repeat it as a finding.

## 6. Source list with verification (HTTP status when fetched on 2026-11-01)

1. Jepsen report: `https://jepsen.io/analyses/particledb-1.1.4` (200). Read in full.
2. Orkes blog, vendor response: `https://orkes.io/blog/particledb-database-built-for-ai-agents` (200). Read the "What we learned from Jepsen" section.
3. ParticleDB modes page (current live wording on groupsync/sync and the "experimental" claim): `https://particledb.ai/operations/modes/` (200).
4. ParticleDB release history: `https://particledb.ai/installation/releases/` (200).
5. Jepsen P4: `https://jepsen.io/consistency/phenomena/p4` (200). G-single: `https://jepsen.io/consistency/phenomena/g-single` (200). A5A: `https://jepsen.io/consistency/phenomena/a5a` (200). G1a: `https://jepsen.io/consistency/phenomena/g1a` (200). Stale read: `https://jepsen.io/consistency/phenomena/stale-read` (200). Snapshot isolation: `https://jepsen.io/consistency/models/snapshot-isolation` (200).
6. Jepsen ethics policy: `https://jepsen.io/analyses/ethics` (200).
7. Wayback captures cited by Jepsen for the original claims (A1 to A8), not opened: `https://web.archive.org/web/20260518203012/https://particledb.ai/`, `https://web.archive.org/web/20260518193013/https://particledb.ai/architecture/transaction-engine/`, `https://web.archive.org/web/20260518193140/https://particledb.ai/operations/cli-reference/`, `https://web.archive.org/web/20260519195820/https://particledb.ai/connectivity/pg-wire/`, `https://web.archive.org/web/20260518193025/particledb.ai/getting-started/concepts`. Connection reset from this environment, so I cannot confirm they resolve.
