# Writer draft handoff: investing/cost-of-capital (01)

## Original-work sentence
This lesson takes evidence the researcher recorded as disconnected facts
(a Treasury yield, an AEP bond-rate range, Damodaran's dated ERP estimate,
AEP's own capital structure, and its per-jurisdiction approved-vs-earned ROE
table) and performs the arithmetic none of those sources performs together:
it builds an actual worked cost of capital (risk-free rate + equity risk
premium ≈ 8.98%; AEP's own ~60/40 debt-equity blend ≈ 6.2%), states plainly
why that blended, company-wide figure is the *wrong* thing to compare against
AEP's regulator-approved ROE (a basis mismatch the evidence flags but no
source states as a teaching point), and then applies the correct return
computed on the same basis (ROIC vs. cost of capital for Costco; earned vs.
approved ROE, jurisdiction by jurisdiction, for AEP) to reach a verdict on
value creation that no single source in the evidence record draws.

## Paths changed
- Article (edited in place, skeleton preserved):
  `/home/user/the-nightly-build/.nb-work/investing/cost-of-capital/library/investing/cost-of-capital.html`
- No chart or asset files added (none warranted; the brief's suggested
  furniture, a comparison table, was built directly from AEP's own
  "Rate Base and ROE's" disclosure — see `<table class="nb-table">` in the
  AEP section).

## Proof result
`nb check ... --series investing --library /home/user/library` →
**BLOCK: 0, WARN: 0, verdict: PUBLISHABLE** (after splitting three
sentences flagged by W-SENTENCE-DENSITY on the first pass; no warnings
left outstanding).
`nb preview` built cleanly (150 articles) and both Background-band links
(`return-on-capital.html`, `what-a-company-owns-and-owes.html`) resolve to
real files in the built site's `library/investing/` directory.

## Brief caveats obeyed
- ERP 4.23% presented explicitly as Damodaran's own dated (start-of-2026)
  implied estimate, "not a fixed constant," with the historical 3.9-6.2%
  range cited alongside it.
- AEP's approved-vs-authorized comparison uses only its own like-for-like
  "operating earned ROE vs. approved ROE" by jurisdiction (S9/S10). AEP's
  ROIC on total capital is never computed or stated anywhere in the
  article; the wrong ROIC-vs-authorized-ROE comparison is used only as a
  named, explicitly rejected hypothetical to teach the basis mismatch, then
  set aside.
- AEP's 3.37% effective tax rate is not used or named, since no AEP
  after-tax operating income or ROIC figure appears in the piece. The 21%
  federal statutory rate that does appear is used only for the generic
  debt tax-shield convention (AEP's own bond rates plus the standard
  federal rate), never presented as AEP's effective rate.
- The unverified February 2026 West Virginia PSC order and the "$15
  million" figure are not cited. The 9.75% APCo/WPCo approved ROE comes
  only from AEP's own S9/S10 investor disclosures.
- Reported fact (Treasury yield, bond rates, 10-K figures, AEP's own
  approved/earned ROE table), estimate (the ~9% and ~6.2% worked costs of
  capital, labeled "illustrative" and their simplifications named: beta=1,
  book-value weights, 21% statutory tax convention), and synthesis (the
  value-creation calls for Costco and AEP) are kept visibly distinct
  throughout.

## Warnings left outstanding
None. WARN count is 0.

## Remaining evidence or voice questions
None outstanding. One editorial judgment call worth flagging for the
editor: the article never computes or states a numeric AEP ROIC (on total
capital), even though the evidence record supplies one (~6-7%), because
every way of using it risked the basis-mismatch comparison the brief
forbids. If the editor wants that number surfaced for completeness, it
would need its own clearly separated frame (its own paragraph, its own
non-ROE comparison) rather than sitting near the 9.75% approved-ROE
figures.
