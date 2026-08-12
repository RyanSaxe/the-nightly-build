# writer brief: opinion/vaccine-schedule-order (01)

Inputs:
  /home/user/the-nightly-build/.nb-work/opinion/vaccine-schedule-order/agent-artifacts/opinion/vaccine-schedule-order/editorial-direction.md
  /home/user/the-nightly-build/.nb-work/opinion/vaccine-schedule-order/agent-artifacts/opinion/vaccine-schedule-order/commission.md  — the position, its two grounds, boundaries, and habits not to inherit
  /home/user/the-nightly-build/.nb-work/opinion/vaccine-schedule-order/agent-artifacts/opinion/vaccine-schedule-order/writing-coach/01/voice-guide.md  — how this piece should sound
  /home/user/the-nightly-build/.nb-work/opinion/vaccine-schedule-order/agent-artifacts/opinion/vaccine-schedule-order/researcher/01/evidence.md  — the complete claim set; treat as evidence, not prose; read its Contradictions section closely
  /home/user/the-nightly-build/.nb-work/opinion/vaccine-schedule-order/library/opinion/vaccine-schedule-order.html  — the initialized article to edit in place
  /home/user/the-nightly-build/.nb-work/opinion/vaccine-schedule-order/.nb-context/  — effective template contract and furniture catalogs

Output:
  /home/user/the-nightly-build/.nb-work/opinion/vaccine-schedule-order/agent-artifacts/opinion/vaccine-schedule-order/writer/01/draft-handoff.md

Proof:
  cd /home/user/the-nightly-build && ./nb check .nb-work/opinion/vaccine-schedule-order/library/opinion/vaccine-schedule-order.html --series opinion --library /home/user/library-checkout
  (use --no-check-links while iterating; run the full command, links included, until BLOCK: 0)

nb-meta: set harness to "claude-code-routine" and model to "claude-opus-4-8"; fill
dates; nb stamp writes the counts.

This round's focus — the evidence reshaped the argument; follow it exactly:
- Correct the date: the order was signed 10 August 2026 (the commission said 11
  August). Use 10 August, verified against the order's own text.
- The autism rationale is NOT in the order or the White House fact sheet; it lives
  only in the signing remarks (Trump; RFK Jr.'s "genes don't cause epidemics").
  Attribute it to the remarks, not the order, or the first ground reads as a
  strawman the opposing case will demolish ("you're attacking the ad-libs, not the
  policy"). Make the autism-science airtight where you use it: Hviid 2019 hazard
  ratio 0.93 (95% CI 0.85-1.02, n=657,461); IOM 2011 "favors rejection of a causal
  relationship"; Wakefield retracted 2010.
- Lead the argument on the second, stronger ground: the schedule is set by ACIP
  under Section 222 of the Public Health Service Act, coverage is bolted to those
  recommendations by name (ACA §2713; Vaccines for Children, SSA §1928), and a
  March 2026 federal injunction already found the administration's agency-level
  rewrite likely unlawful under the APA/FACA. The defect is assignment by fiat,
  not the labels used.
- The mandatory counter section must concede what the record concedes: the
  peer-nation premise is partly true (the US recommended against more diseases, 18,
  than the 20-peer average of 13.6), and "shared clinical decision-making" is
  ACIP's own evidence-based category, not an invention of this order. Answer the
  strongest version, then show why the process defect survives those concessions.
- Close on the specific evidence or procedural fact that would change the paper's
  judgment; write that closing heading in the column's own nouns (do not reuse
  "What would change this paper's judgment"). Name the counter section for the
  actual opposing argument, not "The other side".
- The `nb-position` card pins the precise thesis at the top; the body is held to
  the full standard (no reader address outside any template-allowed furniture).
