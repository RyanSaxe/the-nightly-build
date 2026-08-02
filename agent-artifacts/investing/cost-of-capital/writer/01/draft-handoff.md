# Writer handoff: investing/cost-of-capital (01)

## Original work

This draft turns three separate primary-source strands — Damodaran's
three-question definition of cost of capital, Fama and French's own verdict
that CAPM's "empirical problems probably invalidate its use in applications,"
and FERC's 2018 order averaging four competing return-on-equity models on the
same utilities — into one teachable argument: cost of capital is the
opportunity-cost hurdle a business's return has to clear, built from an
after-tax cost of debt and an estimated (not observed) cost of equity, blended
by market-value weights into WACC, and closed with Damodaran's own live
Utility-vs-Semiconductor data so the hurdle's size is shown to depend on how a
business is financed, not asserted as one number. None of the sources states
that throughline; assembling it, and pairing it with Intel's FY2025 net loss
(the hurdle biting) and McKinsey's firm-size ROIC-WACC spread data (the
general claim generalizing beyond one company) to keep the teaching
transferable rather than a company tour, is this draft's work.

## Proof result

Final run:

```
./nb check .nb-work/investing/cost-of-capital/library/investing/cost-of-capital.html \
  --series investing \
  --library /tmp/claude-0/-home-user-the-nightly-build/e4c39d18-3bf5-5a96-80b8-fc87ffc0a494/scratchpad/library-checkout

BLOCK: 0
WARN:  0
verdict: PUBLISHABLE
```

`nb stamp` wrote words=2190 (within the 1200-2200 band), sources=11,
reading_minutes=10. No warnings were left in place; none needed a recorded
exception.

## Evidence handling per the brief's caveats

- Cost of equity is treated as an estimate throughout, not a fact: the body
  states the Fama-French standard-error range (3.5%-13.1%), the FERC
  four-model-averaging episode, and closes the "what a company's own
  regulators call fair" callback through the Hope Natural Gas opportunity-cost
  standard, exactly as the brief asked.
- No company example does double duty as a clean WACC walkthrough. Intel's
  FY2025 result (net loss against $14.6B gross capex, $46.6B debt) is used
  only for the qualitative claim that a net loss cannot clear any positive
  hurdle; its 98.3% effective tax rate never appears and is never used for the
  after-tax cost of debt step. That step instead uses a fully hypothetical,
  round-number case (borrow at 6%, 25% statutory rate) so no unverified
  statutory-rate figure needed independent verification.
- The Utility-vs-Semiconductor contrast uses Damodaran's live industry
  dataset. The access date (August 2, 2026) appears in the table caption
  along with an explicit note that the dataset is continuously updated and a
  later reader will see different numbers.
- Costco is not used anywhere in the piece; AEP does not appear either. The
  company examples are Intel (used narrowly, per the brief) and the two
  generic industries from Damodaran's dataset.

## Open questions

None. All commission requirements, brief caveats, and voice-guide licenses
(the "you" worked-example license used once in the cost-of-debt section only;
the multi-lens convergence used once at cost of capital's first full
definition; the population-level evidence license used once for the
McKinsey ROIC-WACC spread) were applied within their stated bars.
