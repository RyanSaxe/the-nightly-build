# Commission: feature/ai-buildout-debt

Series: feature (template article, strict). Words 600 to 1200; 2 to 4 flex sections, each
built around a visual; at least five sources. Authorized by the scheduled `nb duty` result
for 2026-11-19 (open section). Topic chosen by the orchestrator from a scouting pass.

## The story

The Federal Reserve's Financial Stability Report of 13 November 2026, Box 2.2 (pp. 23–25),
measures how the AI data-center buildout is financed. Scout's reading, to be verified by the
researcher against the PDF: debt raised for advanced computing above $680 billion by
October 2026 against about $130 billion in all of 2023; about 31% of investment-grade
nonfinancial corporate issuance (under 6% in 2023); public debt outstanding above
$1.1 trillion; leases not yet commenced above $1 trillion and guarantees and take-or-pay
commitments above $2 trillion (undiscounted); large bank holding companies' exposure near
$1 trillion. Box 5.1 (pp. 49–50) reports AI as the most-cited risk among market contacts,
spring against fall.

## The finding the piece must establish (subject to the evidence)

How much of the financing sits off the borrowers' balance sheets, as leases, guarantees and
take-or-pay contracts, against the debt on them, and through which chain (hyperscaler lease
or residual-value guarantee, special-purpose vehicle, private credit, insurers, banks) the
exposure reaches lenders. If the PDF does not support a figure, the piece drops it.

## Visuals (the writer chooses among these; at most four)

- Issuance by instrument, 2022–2026, from the Fed's figure data.
- On-balance-sheet debt beside lease and guarantee commitments.
- A drawn diagram of the financing chain from hyperscaler to final holder.
- The spring-against-fall shift in cited risks, if the values can be read from the Fed's
  accessible data and not from press coverage.

## Sources to use

Primary: the November 2026 FSR PDF and its accessible figure data; the May 2026 FSR as the
before; the OCC Fall 2026 Semiannual Risk Perspective (12 Nov) for the bank-supervisor
view; one or two hyperscaler 10-Q notes on lease commitments not yet commenced, which the
Fed names as its Figure C source. A rival position, stated fairly: a company or analyst who
argues the commitments are serviceable from cash flow, in their own words.

## Boundaries

- Not about electricity prices or grid load (the paper covered that on 6 November and
  16-18 November). Not about Nvidia's leadership or export rules (daily briefs).
- No forecast of a crash. Say what the Fed measured and what it says it cannot measure.
- Neighbouring articles in this edition: the daily brief for 19 November and an RL lesson on
  specification gaming. The brief must not run the FSR as a technology or news item.

## Recent pattern notes (last five features)

- Deks keep using "Set beside...", "By X's arithmetic", "Across ...". Do not.
- Headlines repeatedly pair a named party with a counted figure in "X's Y counts/trades Z"
  form. Find a different construction.
- First sections open with a definitional heading ("A dialogue counts only if...", "Two
  studies of..."). Open with the finding itself, as the series prompt asks.
- Closing sections have been "The test X set" or a past-projection check. Vary it.

## Production

Policy: writing coach capable/low, researcher capable/high, writer capable/high (series
override), editor inherit/high (required). Subagents run on the session model.

## Decisions after research (orchestrator)

- The angle is revised to what the evidence supports. The finding: for the seven firms the Fed
  counts, commitments off the balance sheet (about $1tn of leases not yet started and about
  $2tn of take-or-pay contracts and residual value guarantees, both undiscounted) are about
  3.5 times the debt on it at 2026:Q2, but the filings show that most of the $2tn is purchase
  commitments to suppliers, and the guarantees that reach lenders and can be identified come
  to about $198bn. The Fed does not publish the split and says the totals are not directly
  comparable with discounted debt; the piece says so.
- The 2026 issuance figure is January to October 2026, not a running total.
- Chart values read from the PDF's bars are captioned "read from the Fed's published chart",
  never as Fed-published numbers. Charts are rendered with `nb chart` from committed scripts.
- The Fed's own reading that the large firms may absorb losses, Barr's "less concerned about
  direct losses", and the OCC's "senior ... often secured" are the fair statement of the
  serviceable view, alongside the companies' 10-Q liquidity statements. Oracle's negative
  free cash flow is the counterexample, in its own figures.
- Do not lean on the survey jump (87% against 50%); the categories and pools changed. Use it
  at most as one sentence with that caveat, or drop it.
- The debt-bar conflict with Barr's "exceed $800 billion before year's end" is noted where the
  debt figure appears, or the figure is given as a chart reading with that caveat.
- The financing-chain diagram names the holders the Fed names and sizes only what the Fed or
  a filing sizes.
