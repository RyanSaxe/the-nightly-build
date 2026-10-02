# writer brief: feature/medicaid-lawful-immigrant-funding (01)

Inputs (read all; do not tour the repo or history beyond these):
- editorial-direction.md (../../editorial-direction.md) — the binding standard
- commission.md (../../commission.md) — the assignment AND the "Post-research
  refinement" section, which is binding
- voice-guide.md (../../writing-coach/01/voice-guide.md) — how this should sound
- evidence.md (../../researcher/01/evidence.md) — the complete claim set; treat
  it as the only facts available
- commission.md "Recent patterns" section — desk habits to break

Article to edit (in place):
/home/user/the-nightly-build/.nb-work/feature/medicaid-lawful-immigrant-funding/library/feature/medicaid-lawful-immigrant-funding.html

Output: draft-handoff.md (./draft-handoff.md)

Proof (run verbatim, links included, until BLOCK: 0):
/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/medicaid-lawful-immigrant-funding/library/feature/medicaid-lawful-immigrant-funding.html --series feature --repo /home/user/the-nightly-build

Work from these inputs. Where something you need is missing, ask me (the
orchestrator); do not invent evidence or widen the claim set yourself.

The angle: the 2025 reconciliation law ended the federal Medicaid/CHIP match for
a defined set of lawfully present groups on 1 October 2026; it did not cancel
coverage; each state now decides whether to fund those groups itself, and the
answers diverge. The original work is separating three things the coverage runs
together — what the statute changed, what CMS told states to do, and what
coverage actually reaches a person (a state decision) — and showing the
divergence with specific states.

Hold these precisely (from the Post-research refinement):
- "Federal match," not "Medicaid," for continuing states. State-only coverage is
  not Medicaid/CHIP. The whole piece turns on this; never blur it.
- "The state decides" spans statute-forced cutoffs (North Carolina),
  state-funded continuations (New Mexico, California, New York), and
  time-limited ones (California narrows 1 July 2027). Show that range, do not
  flatten it to keep/drop.
- The loss falls mainly on non-pregnant adults; children and pregnant people are
  largely protected by the CHIPRA 214 option. Name the scope.
- No primary national count of affected people exists. Attribute every estimate
  ($6.2B, 100,000, 1.4M cross-program) to its body (CRS, KFF, Georgetown CCF)
  with scope, and say plainly there is no primary count. Washington's ~14,000 is
  the state's own estimate.
- Nothing in the record says what happened on 1 October; do not imply day-one
  outcomes.
- California dollar figure conflicts ($364.9M Dept of Finance vs $303.1M
  Assembly floor report); give the figure with its source or both as a range,
  never pick one silently. Do not cite the inaccessible DHCS letters or the NY
  court ruling's contents (not opened).
- Be fair to the law's own rationale: state it from a primary source before
  weighing it.

Form and standards:
- Template `article`: orientation anchor + 2-6 flex sections named for this
  argument, last section the piece's own conclusion. Min 8 sources, per-section
  citation, numbered in first-citation order, data-nb-kind honest (statute and
  CMS letter and state notices = primary; KFF/CCF/CRS analyses = secondary even
  when authoritative). Add data-nb-locator for the section/page the record gives.
- A table likely carries the group-by-group match status or the state-by-state
  responses faster than prose (nb-table); use it where it does. No rs-docket
  (this is statute/guidance, not one court case). Build a chart only from a
  verified series in the record.
- Break the desk habits in recent-patterns.md: no "X remains Y rather than Z" or
  "the next test is whether" closer, no suspended-qualifier dek, no performed
  carefulness. State checkable limits, not your own care.
- Your prose meets spec/slop.md before handoff; check every title/role/date/
  number in headline/dek/subheads against the evidence and spec/headlines.md;
  make the nb-meta dek and rendered dekline identical; fill nb-meta
  dates/harness/model; run nb stamp then the proof. Put the one-sentence
  original-work statement in draft-handoff.md.
