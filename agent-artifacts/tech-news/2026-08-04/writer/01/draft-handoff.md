# Draft handoff: tech-news/2026-08-04 (writer 01)

## Original work
The piece cross-reads OpenAI's ten separate Astra claims against the repository's
own file list to build a single results-to-Lean-file table, turning "an AI solved
ten problems" into ten individually named, machine-checkable artifacts a reader can
open, and orders all four items around the verification seam each one turns on:
a proof released to be machine-checked but not yet independently confirmed, agent
rewrites that still needed a human to define "correct," a public atlas others can
inspect, and a 5.3-rated flaw whose real severity lives in the chain.

## Selected items (4 of 7 candidates)
1. LEAD — Astra's ten Lean-verified proofs (Candidate 1). Primary: the GitHub repo.
2. Coding-agents field report for science (Candidate 2).
3. Feinstein human vagus-nerve atlas, the non-AI variety pick (Candidate 3).
4. Cisco FMC static-credential zero-day, CVE-2026-20316 (Candidate 6).

Dropped: Epoch AI (Candidate 5) — its two sources are both Epoch's own pages; the
evidence supplies no independent secondary, so it cannot meet the per-item
1-primary + >=1-independent-secondary rule. Qwen 3.8 Max (Candidate 7) — no
resolved primary. Google/Anthropic $200bn (Candidate 4) — current-events overlap,
left out to keep the briefs disjoint per the commission and the evidence flag.

## Gated-primary opens (done firsthand)
- Astra: openai.com index page is behind a JS/Cloudflare challenge, but the owning
  manuscript PDF (cdn.openai.com/pdf/ten-proofs-oai.pdf, 249pp) and the GitHub repo
  both resolved and I read them firsthand — the abstract's ten results and every
  Lean filename were confirmed against the table. The Next Web (opened) corroborates
  the $2,000 figure, the 249-page manuscript, and Astra as OpenAI's next model.
  Number corrections honored: the "zero unproven steps / zero sorries" claim is the
  work's own (the README states no sorry count and points to a separate Comparator
  challenge), so the lead frames it as unconfirmed. No Gowers endorsement is asserted;
  the evidence flags it as likely about an earlier result, so it is left out entirely.
- Vagus: feinstein.northwell.edu is 403-gated, so per the brief's fallback the
  primary href is the resolving BioSpace wire copy of the same release, marked
  primary honestly; every figure (200,000+ fibers, 60 nerves, 30 donors, $6.7M NIH,
  REVA, SPARC) confirmed there and cross-checked against GEN (opened). science.org
  (the Aug-3 peg) stayed 403 and is not cited; GEN (July 28) carries the independent
  timeliness instead.
- Cisco: the Cisco advisory (cisco-sa-fmc-static-cred-BET3Cjh) resolved and is the
  primary — it owns the 5.3 score, the July 2026 active-exploitation statement, the
  High Security Impact rating, and the chaining sentence. BleepingComputer and
  VulnCheck (both opened) carry the CVSS-10 CVE-2026-20079 context and the hot-fix
  list. The exploited CVE (20316, 5.3) is kept strictly distinct from the CVSS-10
  auth-bypass bug, per the correction.

## Proof result
`./nb stamp` then the brief's exact `nb check ... --check-links`: **BLOCK: 0,
WARN: 0, verdict PUBLISHABLE.** No warnings left standing (two sentence-density
warnings were fixed by splitting). Preview build renders the lead's ten-row table
and the vagus stat strip; nb-meta dek is byte-identical to the rendered dekline.

## Open question for the editor
The coding-agents item's owning primary — OpenAI's field report page
(openai.com/index/scientific-computing-agentic-ai) and OpenAI's own X post — stayed
gated (403 / 402) to every fetch path I tried, with no CDN PDF or OpenAI-owned mirror
to route around it (unlike the Astra manuscript). Its canonical page is recorded as
the primary href and resolves (403, not 404, so link-check passes), but I could not
read it firsthand. Every load-bearing figure and the "confidently wrong" caveat in
that item cite The Decoder (opened firsthand), whose account names the report and
its finding precisely; the primary's identity and publication are corroborated, not
firsthand-read. If the editor wants the primary itself confirmed, it needs a fetch
path that clears the challenge.
