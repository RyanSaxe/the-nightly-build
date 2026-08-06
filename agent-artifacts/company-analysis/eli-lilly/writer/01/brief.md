# writer brief: company-analysis/eli-lilly (01)

Inputs:
- .nb-work/company-analysis/eli-lilly/agent-artifacts/company-analysis/eli-lilly/editorial-direction.md
- .nb-work/company-analysis/eli-lilly/agent-artifacts/company-analysis/eli-lilly/commission.md  (the market question and the beat)
- .nb-work/company-analysis/eli-lilly/agent-artifacts/company-analysis/eli-lilly/writing-coach/01/voice-guide.md
- .nb-work/company-analysis/eli-lilly/agent-artifacts/company-analysis/eli-lilly/researcher/01/evidence.md  (the only claim set; every figure verified to Lilly's own filings)
- .nb-work/company-analysis/eli-lilly/library/company-analysis/eli-lilly.html  (the initialized article to edit in place)
- .nb-work/company-analysis/eli-lilly/.nb-context/  (effective template contract, furniture catalogs, runtime assets)

Output: .nb-work/company-analysis/eli-lilly/agent-artifacts/company-analysis/eli-lilly/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/company-analysis/eli-lilly/library/company-analysis/eli-lilly.html --series company-analysis --library /tmp/claude-0/-home-user-the-nightly-build/976dc2e8-9069-59ea-94ea-a08d4d77fd63/scratchpad/library-checkout
(run from repo root /home/user/the-nightly-build; use --no-check-links while iterating, then links-included until BLOCK: 0)

Commission decisions resolved (the evidence record flagged these — apply exactly):
- TARIFF FRAMING: treat the 100% branded-drug tariff as a CONTINGENT FUTURE
  RISK that Lilly is presently largely exempt from, NOT a live US-price
  overhang. The 10-Q states pharma is exempt from certain of these tariffs, and
  the onshoring (20%) and MFN-pricing-agreement (0% until Jan 2029) paths appear
  to cover Lilly; no filing quantifies any tariff cost. Correct the date to the
  proclamation's own effective date for Annex III large companies (July 31,
  2026), not the 2026-08-04 date in the commission. Do not overstate this;
  give it only the space a contingent, largely-exempt risk earns.
- DECOMPOSITION HONESTY: the article's decomposition repeats Lilly's OWN
  reported volume and price percentages, which cannot be independently
  reconstructed from the filings. Lilly discloses no unit volumes and no
  separate numeric "mix" leg, and the stated splits do not sum to reported
  revenue growth (worldwide +60% volume, -13% price vs +48% reported), leaving
  an unquantified FX/other residual. Say this plainly: present it as
  volume-vs-price (with the residual acknowledged), corroborated by the internal
  consistency of the per-product and geographic tables, not as an independently
  derived fact. Do not manufacture a "mix" number the filing does not give.

The analysis the evidence actually supports (this is the finding — build the
piece on it, do not soften it into a beat recap):
- "Volume outruns price" holds as a DESCRIPTION of the quarter (worldwide +60%
  volume vs -13% price; ex-US +113% volume vs -36% price; China revenue roughly
  doubled to ~$941M despite the NRDL price cut).
- The DURABILITY half is where the story is: worldwide realized price fell 13%
  in BOTH Q1 and Q2 (persistent, not a one-off); ex-US erosion is DEEPENING
  (-25% then -36%); the headline US -3% price is flattered by rebate/discount
  estimate adjustments and masks an underlying ~9% decline (Lilly's own caveat,
  repeated by the CFO); US volume growth is DECELERATING (+49% then +37%); and
  July 2026 generic ANDA filings against Mounjaro/Zepbound plus the low-price
  oral pill's mix shift argue for a volume ramp running against structurally
  eroding price. Judge the raised guidance against that, with the evidence shown
  (the coach's stance: take the number apart on the page so the reader watches
  the subtraction). Do not issue a buy, sell, or allocation call.

Furniture / charts (chart-forward desk): use a chart or table where a trend or
decomposition is the point (e.g. quarter-over-quarter realized-price change by
geography, or the volume-vs-price split). Build charts ONLY from the evidence
record's verified series with `nb chart`, inspect the rendered PNG, commit its
provenance, and cite the data source in the caption. Furniture carries the
evidence, not decoration. Teach the business (what tirzepatide is; why realized
price and volume move oppositely) where it clarifies the argument.

Recent-pattern habits to break (do not inherit; full list in commission.md):
- Do not open with the beat-versus-bar headline number shape (recent Reddit/
  Apple openers). Enter through the price/volume durability question.
- Do not march quarter-metric by quarter-metric, and do not close on a "two ways
  to read it" or compounder thesis-check shape.
Required furniture and the Sources section are not habits to avoid.
