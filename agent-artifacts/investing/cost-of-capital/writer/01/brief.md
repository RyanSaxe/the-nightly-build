# Writer brief: investing/cost-of-capital (01)

## Your job
Draft the `lesson` on **the cost of capital (the hurdle rate)** — 1200-2200
words — then prove it to `BLOCK: 0`. Draft only from the evidence record and
voice guide. Teach 2-3 ideas completely; do not summarize a textbook.

## Begin with these exact inputs
- This brief; `../../commission.md`; `../../editorial-direction.md`.
- Voice guide: `../../writing-coach/01/voice-guide.md` (reread before drafting).
- Evidence record: `../../researcher/01/evidence.md` (your complete claim set and
  its caveats — obey every one, especially the basis-mismatch and ERP cautions).
- Initialized article:
  `/home/user/the-nightly-build/.nb-work/investing/cost-of-capital/library/investing/cost-of-capital.html`
  (edit; do not recreate the skeleton).
- Template context: `../../../../.nb-context/` (lesson geometry: fixed order —
  "Why this matters" bookend, body, "The takeaway" bookend; write BOTH bookends
  AFTER the body; bookends are apparatus, exempt from citation; furniture in
  `.nb-context/furniture/` and the lesson `furniture.md`).

## Where this sits in the course (build on it; do not re-teach)
Prior published lessons, in order (they exist in the library):
`how-a-business-earns-a-profit`, `profit-versus-cash`,
`what-a-company-owns-and-owes`, `return-on-capital`. The `return-on-capital`
lesson ended on "the test that decides whether a company's growth creates value
or destroys it" — this lesson supplies that test. Link `return-on-capital` (and
optionally the balance-sheet lesson) in the **Background** band rather than
re-teaching ROIC; the sibling path is `return-on-capital.html` (same library/
investing/ directory as this article — verify the relative href resolves). The
lesson must still work for a reader who opens none of the links, so restate ROIC
in one plain sentence before using it.

## The 2-3 ideas to teach completely (all verified in the evidence record)
1. **Cost of capital = opportunity cost = required return (the hurdle).** Build it
   from a number the reader already trusts: the risk-free rate (10-Yr US Treasury
   par yield **4.75%**, as of 2026-07-31, Treasury.gov), then add a premium for
   risk. Damodaran (authoritative): the cost of capital is simultaneously an
   opportunity cost, a discount rate, and a hurdle rate.
2. **Where the number comes from: WACC, at a high level.** A firm is funded by
   debt and equity; the cost of capital is the weighted average of what each
   requires. Cost of debt ≈ its borrowing rate, after tax (real anchor: AEP's
   2025 senior unsecured notes issued at **5.38%-5.85%** pretax); cost of equity
   is higher because equity is paid after debt (the residual claim). Worked cost
   of equity, stated as an illustration with the assumption named plainly (β = 1):
   4.75% + an equity risk premium of **4.23%** ≈ **~9%**. CAVEAT (obey): present
   4.23% as Damodaran's *dated* implied estimate (start of 2026), not "the" ERP —
   the historical ERP runs ~3.9%-6.2% depending on window; say the number moves.
   Teach the intuition and the weighting; do NOT derive CAPM/beta — say what you
   are simplifying.
3. **The value-creation rule: ROIC vs the hurdle.** Value is created only when
   ROIC exceeds the cost of capital; growth amplifies value above the line and
   destroys it below (Damodaran: across 40,000+ firms, "growth... is more likely
   to destroy value than to add it"). Make it real with two contrasting cases:
   - **Costco**: after-tax operating income $10,383M × (1−25.1%) ≈ $7,777M over
     ~$18.4B invested capital → **ROIC ≈ 42%**, far above any plausible hurdle →
     growth creates value.
     (Use FY2025 10-K figures from the evidence record; either timing basis gives
     ~40%.)
   - **A regulated utility at its hurdle — American Electric Power.** Use AEP's
     own like-for-like **operating earned ROE vs approved ROE** (its investor
     "Rate Base and ROE's" disclosure), NOT a naive ROIC-vs-authorized-ROE
     comparison. Concretely: APCo/West Virginia (WPCo) earned **7.9-8.2%** against
     an approved ROE of **9.75%**; Kentucky Power earned just **4.4%** against
     **9.75%** — a regulated business earning below the return its own regulators
     authorize, where growth in the rate base does little for value. This is the
     mirror image of Costco.

## Caveats from the evidence record (obey exactly)
- Do NOT compare AEP's consolidated ROIC (~6-7%, on total debt+equity capital) to
  its authorized ROE (on equity only) as if like-for-like — basis mismatch. If
  you mention AEP's ROIC at all, label it "return on AEP's total capital" and keep
  it separate from the earned-vs-approved-ROE comparison, which is the clean one.
- AEP's effective tax rate is 3.37% (production tax credits from wind/solar), not
  the 21% statutory rate — if any AEP after-tax/ROIC number appears, name why.
- Do NOT cite the unverified Feb 2026 West Virginia PSC order or the "$15M"
  figure. The 9.75% approved ROE itself is independently confirmed (AEP's own
  disclosure) — use that.
- Keep reported fact, estimate (the worked ~9% cost of equity), and synthesis
  distinct. Round transparently; use the real numbers, don't invent clean ones.

## Bookends (write AFTER the body)
"Why this matters" gives the reader a real reason grounded in this lesson's
particulars (the hurdle, why ROIC alone is not a verdict). "The takeaway" is what
they keep — resolves what the opener set up, teaches nothing new, uses no term the
body did not set. Read them back-to-back as setup and payoff. Fixed chrome (name
lines, band labels "Background"/"Go deeper", "optional reading") stays exact.

## Furniture
A **comparison table** ("who requires what / earned vs approved ROE by
jurisdiction", or a compact Costco-vs-AEP hurdle contrast) is well-justified from
AEP's own table — use documented furniture, keep the "as of" date, don't fabricate
columns. A chart only if from a verified series and it earns its place. No
article-authored scripts/styles/iframes/forms/external images.

## Universal rules
Minimum 6 sources; per-section citation (bookends exempt); carry evidence-record
kinds into `data-nb-kind` (Treasury, SEC filings, AEP disclosures, Damodaran's
own implied-ERP post = primary for their own facts; Damodaran's synthesis papers =
authoritative secondary — classify as the evidence record does). Number sources in
first-citation order; add `data-nb-locator`/`data-nb-url` only where supplied.
Fill `nb-meta`: series investing, slug cost-of-capital, template lesson, mode
open, order null, date 2026-08-02, tags (accurate, e.g.
["valuation","cost-of-capital","roic"]), measured sources/words, a real dek (a
stance, not a comma-triad), harness "claude-code", model "claude-sonnet-5".

## Prove and hand off
Run to `BLOCK: 0`:
`/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/investing/cost-of-capital/library/investing/cost-of-capital.html --series investing --library /home/user/library`
Treat warnings as revision notes. Use `nb preview` if you add a table/chart.

Write `draft-handoff.md` here: original-work sentence, paths changed, proof
result and warnings left, remaining questions. Return `DONE writer <path>` after
`BLOCK: 0`, or a REQUEST/BLOCKED line.
