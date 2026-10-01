# Editorial review: feature/micron-fy2026-memory-scarcity (editor/01)

## Correct

From the draft alone, the thesis is that higher memory prices explain Micron's exceptional profitability, while customer agreements have not established that the current margin will persist. Four claims support it: revenue increased much faster than cost of goods sold; accelerator and host-memory constraints provide specific reasons for technical demand; contractual sales, customer financing and recognized revenue have different meanings; and the economics of new factories depend on prices and costs when production arrives.

The first reading tested those claims against the printed sources. The SEC Q4 release owns the unaudited results, fiscal period and guidance. The prepared remarks explicitly report stronger price growth than bit growth and conventional DRAM margins above HBM margins. That breaks a simple explanation based on a universally higher-margin AI product mix, and the article retains the contrary finding. The two workload papers support their respective memory-capacity mechanisms, with Micron authors in both and Meta authors in the host-memory paper. They provide no independent validation of management's scarcity forecast. I made the fixed-compute assumption explicit in the approximately 1.4-times HBM4 projection.

The May-quarter filing and FY2025 accounting policy support the distinction between enforceable future volumes, liabilities from deposits, and revenue recognized on transfer of control. The September remarks report $150 billion in minimum-price remaining performance obligations, $32 billion in financial commitments and approximately $12.3 billion in Q4 deposits. These values are neither additive sales nor already earned profit. The annual cash-flow statement places customer-deposit proceeds in financing activities; its reconciliation gives Q4 operating cash flow of $43.973 billion and adjusted free cash flow of $33.199 billion. The article does not subtract deposits from operating cash flow a second time.

Two source-record problems required correction. The disclosure of coverage exceeding 35% is a lower bound, so it cannot establish the draft's assertion that most projected revenue remains outside the agreements. Root agreed with this correction. I removed that inference, retained the absence of a disclosed company-wide earnings floor, and rewrote the dek to refer to undisclosed contract prices and future costs. This narrows an unsupported calculation; it does not hide the lack of individual contract terms. The FY2025 Revenue Recognition passage is on printed page 71, not page 68 as recorded in the input. I corrected the citation locator and notified root. The researcher artifact remains unchanged as the original reporting record.

All eight citation hrefs were reopened exactly as printed. The SEC Q4 release, May 10-Q, FY2025 10-K and three q4cdn PDFs returned HTTP 200 at the same canonical addresses, with the expected statements or papers. Web extraction failed for the Q4 release and both technical PDFs, so I independently downloaded and read the documents. The two Micron IR earnings URLs returned 403 to shell curl, but web open landed on each exact release, with the correct title, date and financial tables. None redirects to an overview or substitutes an endpoint. All eight data-nb-kind values correctly identify primary material: SEC hosting does not create another author, and Meta coauthorship does not make its joint experiment an independent assessment of Micron's financial forecast.

I recomputed every displayed calculation. Q4 revenue less cost of goods sold is $47.047 billion, and the ratio is 86.756%, rounding to 86.8%. The year-earlier differences are $42.914 billion of revenue and $921 million of cost, leaving 97.854 cents of incremental gross profit per added revenue dollar. Sequential reported revenue growth is 30.811%; $54.229 billion over fourteen weeks versus $41.456 billion over thirteen gives $3.8735 billion and $3.188923 billion weekly, with 21.467% growth. Annual revenue and cost growth are 256.327% and 14.126%; the respective annual GAAP margins round to 80.7% and 39.8%. I added the thirteen-week year-earlier denominator and the fifty-three versus fifty-two week annual comparison.

The four quarterly table rows subtract to $7.646, $17.755, $35.056 and $47.047 billion of gross profit. The earlier rows match the Q2 and Q3 releases and the last row the Q4 release. The guidance beat is $3.229 billion and $1.42 of adjusted EPS. The guidance table keeps GAAP and adjusted figures separate and labels the future quarter as a forecast. Its revenue midpoint implies $52.85925 billion in GAAP gross profit, above the reported Q4 total despite the lower percentage. Cloud plus core-data-center revenue is $34.285 billion, 63.2226% of the total; that is not AI-attributed revenue. Operating cash flow less net capex is $33.199 billion. The fixed-cost sensitivity loses $5.4229 billion of gross profit, 11.5266% of the original gross profit, rounded as printed. The inference of annual net capex above roughly $50 billion is explicitly conditional arithmetic on approximate guidance, not an annual budget. I clarified that the spending forecast is net of anticipated government incentives and that the scarcity forecast uses calendar 2028.

Headline, dek, section headings, dates, periods, quantities and source labels were checked against their owning documents. There are no named executive roles to verify in the prose. No quotations are used. The source-budget audit counts source-specific narrative and adjacent source-specific interpretation, while separating our recomputed arithmetic, numeric table cells and labels, and general explanations of memory and accounting. Each document stays within its 200-word narrative allowance: the prepared-remarks reporting and immediate interpretation total approximately 190 words, the most concentrated source allocation. The two papers remain below 200 even when their adjacent mechanism explanations and author-affiliation sentences are included. Reopening a document did not increase its allowance.

## Reads well

The second reading used the voice guide, the commission's recent-pattern notes and spec/slop.md. I read the first and last sentence of each paragraph and component separately, then the full text as someone arriving without the brief. The draft's specific amounts and accounting distinctions largely met the guide's register.

I removed the opening explanation that subtracting manufacturing expense explains the earnings change, because the next sentences already perform that calculation. I deleted the sentence grading the quarter as a stronger starting point, the generic warning about an incomplete earnings model, the repeated calendar-adjustment commentary and the general observation that higher sales can coexist with lower margin. They supplied no additional finding. I also removed the abstract explanation that the cloud result prevents a simple AI-margin story and its repeated mix-versus-price conclusion; the preceding source-specific cloud result makes the point directly.

I replaced 'out-earned HBM on margin' with the precise gross-margin comparison and named higher HBM mix as the offset to higher prices. Cost of goods sold now appears consistently in the opening heading and the price explanation. The SCA paragraph identifies estimated revenue under the agreements as the denominator for three-quarters. LPDDR5X is introduced as low-power DRAM, and solid-state storage replaces an unexplained SSD abbreviation in the workload comparison.

No sentence depended on borrowing the quoted voice exemplars' phrasing. I found no surviving clause copied from the commission's description of the reader's situation. The article uses neither the prior Micron ending's stock-price aside and reading list nor the recent Features' repeated semicolon-reversal headings. I shortened the contract paragraph's sequence of negative qualifications so the positive finding and its specific disclosure limits remain legible. The remaining distinctions about recognized revenue and modeled performance correct actual misconceptions recorded in the reporting.

## The experience

The third reading followed the article's displayed sequence: reported economics, price and quantity, technical memory demand, contract accounting, then factory economics. The exact quarterly table shows the growing revenue-cost gap with less repetition than four prose descriptions. Its caption retains the reporting basis, quarter length and warning against reading cost of goods sold as cost per bit. The compact guidance table makes its actual/forecast and GAAP/adjusted distinctions visible. There is no chart or captured source image in the final article; root authorized the table substitution after Chrome failed locally.

I inspected the three static WeasyPrint PNG pages supplied by root from the writer preview. The title, prose, tables, captions and visible source list were readable, without clipped content. This was supplemental static layout inspection, not browser inspection. I rebuilt the edited preview at /tmp/micron-editor-preview and checked the edited HTML and metadata. Local Chrome cannot start because socket() is denied; I did not retry Chrome or claim a completed local browser check. The mandatory GitHub CI render probe remains the release gate owned by root.

After the final straight-through reading, my original-work sentence is: the article measures how much Micron's revenue-cost gap widened, corrects its extra-week comparison, and tests whether disclosed customer protections and financing can preserve that profitability when new capacity produces memory. Only then did I open the handoff's original-work sentence. It describes the same work, and the published arithmetic and accounting explanation perform it. The ending follows from undisclosed contract prices and future production costs, instead of treating one reported quarter as a demonstrated permanent earning rate. The headline still accurately states the reported gross-margin finding.

## Edits

- Replaced the opening heading's manufacturing-expense wording with cost of goods sold.
- Removed the redundant opening subtraction sentence.
- Added the thirteen-week year-earlier denominator and its fiscal-calendar citation.
- Deleted the sentence grading the quarter as a stronger starting point for forecasts.
- Shortened the weekly-growth paragraph to the reported and normalized calculations.
- Removed the generic earnings-model conclusion and added annual week-count comparability.
- Replaced the colloquial HBM margin comparison with explicit gross-margin and mix language.
- Shortened the price explanation and consistently named cost of goods sold.
- Removed the redundant observation about lower margin and higher earnings.
- Specified constant compute in the modeled HBM4 gain.
- Defined LPDDR5X as low-power DRAM and spelled out solid-state storage.
- Identified SCA revenue as the denominator for the three-quarters pricing disclosure.
- Removed the unsupported majority-of-revenue assertion and repeated contract qualifications.
- Rewrote both metadata and rendered dek around contract-price and manufacturing-cost limits.
- Specified calendar 2028 and net capital expenditure after anticipated government incentives.
- Corrected the FY2025 revenue-recognition locator to printed page 71.
- Renumbered the May filing and June release citations in first-appearance order.
- Restamped metadata to 1,614 words, eight sources and seven reading minutes.
- Rebuilt the edited preview and ran the exact brief proof with links: BLOCK 0, WARN 0, PUBLISHABLE.

## Decision

approve. No required article changes remain; root must obtain the mandatory passing GitHub browser render probe before release.

Role: nb-editor. Runtime: ChatGPT Work. Actual precise model identifier: not exposed. Reasoning effort: HIGH, explicitly supplied for this invocation to meet press production policy.
