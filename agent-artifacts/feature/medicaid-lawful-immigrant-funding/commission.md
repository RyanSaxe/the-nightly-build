# Commission: feature/medicaid-lawful-immigrant-funding

## The assignment

A Feature for 2 October 2026, the day after a dated change took effect. On 1
October 2026, a provision of the 2025 federal reconciliation law stopped federal
Medicaid and CHIP matching funds for several categories of lawfully present
immigrants. The piece is built on the firsthand record: the statute, the federal
agency guidance that implements it, and the primary analyses and state actions
that show what follows.

## The angle (the original work)

The headline version of this story is "immigrants lose Medicaid on October 1."
That is not what the law does, and the gap is the piece. The law ends the
**federal share** of the cost for a defined set of lawfully present groups. It
does not by itself cancel anyone's coverage. Each state now decides whether to
keep covering those groups with its own money, and the answers differ. So what a
lawfully present immigrant actually loses on 1 October depends on the category
they fall in and the state they live in.

The piece's job is to separate three things the coverage runs together: (1) what
the statute changed (which groups lose the federal match, which keep it), (2)
what the implementing guidance tells states to do and when, and (3) what
coverage outcome actually reaches a person, which is a state-by-state decision,
not an automatic cutoff. State it in one sentence the writer puts in the
handoff: the law converts an eligibility question into a fifty-state budget
question, and the piece shows exactly where that conversion happens.

This is not an opinion piece. It establishes the mechanism from the documents
and shows the divergence with specifics. It is fair to the law's own stated
rationale: state it from a primary source before weighing it.

## Boundaries

- One Feature, one angle. Do not widen into a general survey of the whole
  reconciliation law. Medicare changes (reported for January 2027) belong only
  as a dated contrast if the record supports it, not as a second subject.
- The Daily Brief tonight is barred from this topic, so there is no overlap to
  manage; do not reference the brief.
- Keep the claim to what the primary record supports. Where a figure for "how
  many people" is an estimate, attribute it to the body that produced it and
  give its scope. Do not assert a nationwide coverage-loss count as fact.

## Required contribution

A reader finishes knowing: which lawfully present categories lost the federal
match and which did not; what CMS instructed states to do and on what date;
why coverage does not end automatically; and how at least a couple of concrete
states diverge in response. The teaching test: a reader can reason about why two
lawfully present immigrants in different states now face different outcomes.

## Template and structure

Template `article` (chosen over `paper`; this reports a policy change from
multiple primary records, not one research paper). Orientation anchor plus 2-6
flex sections, the last being the piece's own conclusion. Name sections for this
argument, not a stock outline. Reach for a table where the group-by-group match
status or a state-by-state comparison reads faster than prose. A case docket
(`rs-docket`) does not fit; this is statute and guidance, not a single court
case. Build a chart only from a verified series the researcher records.

## Source policy (nb source-policy --series feature)

Template `article`: min 8 sources, per-section citation. Anchor on primary
records: the statute's operative text, the CMS State Health Official letter
(reported as SHO #26-001, 8 April 2026), and official state guidance or
notices. Use primary analyses (for example KFF, Georgetown CCF) as secondary
context and attribute their estimates. Number sources in first-citation order;
carry primary/secondary into `data-nb-kind` honestly (an analysis organization
is secondary even when authoritative).

## Production (nb production-policy --series feature; balanced profile)

- writing-coach: capable (Claude Sonnet), low
- researcher: capable (Claude Sonnet), high
- writer: capable (Claude Sonnet), medium
- editor: inherit (Claude Opus), high, required

No required directive was traded down.

## Neighbouring articles this run

- daily-brief/2026-10-02 (barred from this topic)
- technical/dbt-v2-rust-engine (unrelated domain)

## Post-research refinement (orchestrator decision, binding)

The researcher confirms the state-divergence angle holds in the primary record
(Section 71109 of P.L. 119-21 restricts federal payment, not eligibility; CMS
SHO #26-001 says CMS will not require states to fund the dropped groups; states
diverge: continue — New Mexico, New York, California; lapse — Washington, North
Carolina, South Carolina). Carry these refinements, which sharpen the angle:

1. **Say "federal match," not "Medicaid," for the continuing states.** CMS treats
   state-only coverage as not Medicaid/CHIP at all. "California keeps Medicaid for
   these immigrants" is wrong; "California keeps covering them with state-only
   funds" is right. The whole piece turns on this distinction, so hold it
   precisely throughout.

2. **Divergence is not always a free or soft choice.** North Carolina wrote the
   cutoff into state law (S.L. 2026-1 §3C.4), so it is automatic there;
   California's state-funded coverage itself narrows to restricted scope on 1 July
   2027; a court ruling reportedly compels New York's (the researcher did not open
   the ruling — do not assert its contents). Show that "the state decides" spans
   statute-forced cutoffs, funded continuations, and time-limited ones, not a
   simple keep/drop switch.

3. **The loss falls mainly on non-pregnant adults.** Children and pregnant people
   are largely protected by the CHIPRA 214 option (elected by 39 states, DC, 3
   territories), which keeps the federal match. Name this so the scope is honest.

4. **No primary count of affected people exists.** CMS gives no national number;
   CBO documents were inaccessible. The $6.2B, 100,000-uninsured and 1.4-million
   figures reach us only through CRS, KFF, Georgetown CCF, and the 1.4M is a
   cross-program Georgetown figure, not a Medicaid count. Attribute every number
   to the body that produced it with its scope; state plainly that no primary
   national count exists. Washington's ~14,000 is the state's own estimate.

5. **Nothing in the record says what actually happened on 1 October.** The piece
   reports what the law and guidance do and what states decided, not outcomes on
   the day. Do not imply observed day-one effects.

6. **Two sourcing gaps (see evidence Limits).** California DHCS letters I26-21 and
   26-13 were inaccessible, and the California dollar figure conflicts ($364.9M in
   the Department of Finance summary vs $303.1M in the Assembly floor report) —
   give the figure with its source, or the range with both, do not pick one
   silently.


## Recent patterns (what not to repeat)

_Folded in from the orchestrator's recent-pattern notes; the writer and editor were briefed on these._

### Closers

Recent features close on an antithesis that rates the finding: "an 86.8% gross
margin remains a reported quarter's result rather than an established long-term
earning rate" (micron). The "X remains Y rather than Z" and "the next test is
whether..." molds recur. `spec/slop.md` flags antithesis ("X rather than Y") and
"built to be quoted" closers. End on the conclusion the piece earned, in its own
nouns, without the "rather than" reversal or a line written to be quoted.

### Deks

Recent feature deks hang a qualifier off the finding ("...whose durability
depends on undisclosed contract prices and future manufacturing costs",
"...and neither establishes whether a live alert could have reached people").
The suspended-qualifier dek is close to the banned suspended-question mold. Write
a dek that commits to the one concrete claim of this piece and stops.

### Headings

Recent feature headings are plain subject-verb statements of each step ("Revenue
grows much faster than cost of goods sold", "New fabs must earn their cost").
That register is good; keep it. Do not join two clauses with a comma-and-"and"
across several headings, and do not fall into the semicolon two-clause heading
the Technical desk has been overusing.

### The careful-status move

The desk's discipline of marking what the evidence does not establish is
correct and stays. The failure to avoid is performing it: "the honest position
is", "what the evidence has established". State the checkable limit (what went
unmeasured, who disagrees, what the primary does not disclose), not your own
care.
