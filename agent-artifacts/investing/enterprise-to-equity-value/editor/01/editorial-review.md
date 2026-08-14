# Editorial review: investing/enterprise-to-equity-value (editor/01)

## Skeptic

Thesis: enterprise value does not become a price per share by one subtraction;
you cross a two-step bridge (enterprise value to equity value, equity value to
per share), and on Uber's own Q2 2026 filing the stakes in other companies move
the per-share number more than debt and dilution move it the other way.

The claims it stands on, tested:

- **The bridge arithmetic reconciles to Uber's market cap.** Rebuilt every line
  from the evidence's 10-Q figures. Net debt = total debt $12,723M − cash
  $4,870M − short-term investments $521M = $7,332M (−$3.59/share). NCI $1,083M
  (−$0.53). Equity stakes = investments $8,759M + equity-method $3,773M =
  $12,532M (+$6.13). Back-solved EV = market cap $154,989M + $12,723M + $1,083M −
  $4,870M − $521M − $12,532M = $150,872M, matching the table. Running it forward
  from that EV returns $154,989M exactly, and 2,042,560,121 × $75.88 =
  ~$154,989M. Per-share divisions all reproduce the printed −3.59 / −0.53 / +6.13
  / 75.88. Held.

- **The thesis claim — stakes add more per share than debt and dilution take
  away combined.** Add-back +$6.13 against net debt −$3.59, NCI −$0.53, and
  dilution −$0.67 (the article's own $75.88→$75.21 step), summing to −$4.79. 6.13
  > 4.79, and 6.13 also clears debt-plus-dilution alone (4.26). The headline
  (stakes > debt) and dek (stakes > debt and dilution) are both true on the
  recorded numbers. Held.

- **The diluted-count step.** Reconciliation table sums correctly (2,044,279 +
  13,343 + 10 + 810 + 2,321 = 2,060,763). The $75.21 recompute is right
  (154,989,000 / 2,060,763 = 75.21, down $0.67). The article divides equity value
  by the diluted weighted-average while the market quote uses the point-in-time
  count, so the drop is ~0.88%, not the 0.80% basic-to-diluted gap; the article
  names that difference explicitly (one-day count vs. six-month average) rather
  than hiding it. Honest and correct. Held.

- **Convertible-note dilution.** 23.8M shares at the stated rate (13.7848 ×
  1,725,000), 4.6% spread ((75.88−72.54)/72.54), ~1M economically dilutive,
  consistent with the filing's +810K six-month if-converted addition. All trace
  to the evidence. Held.

Back-solved EV transparency (review focus): stated as illustrative in four
places — orientation prose ("not a discounted-cash-flow answer... this market
price with the bridge unwound"), the table row and caption, and the Verdict note
("solved backward from the market price, not forward from a forecast"). It is
nowhere passed off as an independent valuation. Confirmed.

The seven contested judgment points (review focus), each checked against the
evidence's Contradictions:
- Treasury-stock method contested by Damodaran — taught as judgment ("a sloppy
  alternative... Damodaran's objection on the record rather than settled"). Honest.
- Operating leases in net debt — taught as a live call (Damodaran converts them;
  the lesson leaves them out because the ROU asset already sits in the cash
  flows, "said plainly rather than asserted as settled"). Honest.
- Restricted cash/investments — the $2,307M and $9,486M are named as insurance
  collateral excluded from the add-back. Honest.
- Aurora collateralized exchangeable note — the note component explains the
  debt and the stake are two views of the same collateral, with the caveat that
  the bridge still lists them apart. Honest.
- Preferred inside NCI — the Series A/A-1 preferred is flagged as a real claim
  with no line of its own that a textbook bridge could miss. Honest.
- Non-operating stakes' true independence — Delivery Hero (signed acquisition),
  Aurora (integrated), Careem (former subsidiary) vs. passive Grab, taught as
  individual judgment calls. Honest.
- Book vs. fair value of debt ($12,723M book vs. $12.9B fair) — the one point
  not surfaced. The article uses book value, which the evidence records as
  conventional practice and its own default, so nothing is asserted as settled
  falsely; this is an omission of a minor nuance (~$0.09/share), not a
  dishonest treatment. Not routed; noted as an observation.

Citations: opened all nine hrefs as printed. Every one lands on the source
itself, not an endpoint. Descriptors verified — the Damodaran 2013 post title,
the SEC 10-Q identity, the two Damodaran PDFs (resolve to the real source files;
titles/quotes corroborated by the evidence record), Wall Street Prep's
"all contributors of capital" line, AnalystPrep, WallStreetMojo, and CFI's
n(1−K/P) formula (which matches the equation furniture). The stockanalysis.com
page independently confirms the body's live figures: $75.88 close, $154.99B
market cap, August 13, 2026. Every `data-nb-kind` matches the evidence's Kind
field; the Damodaran materials are primary for the reasoning they own, the
aggregators and explainers secondary. No sourcing failure found.

## Cut

Slop pass, sentence by sentence including display text and furniture: the piece
holds. The two bookend cards use their allowed direct address and still carry
content (the opener states the concrete gap between an EV and a quote and what
the reader will be able to do; the takeaway states the finding — each filing's
bridge has a different dominant term). Edge sentences read alone: the takeaway
closer ("The bridge does not change from one filing to the next. Which line
dominates it does...") is the earned conclusion, not a signpost, and survives
the delete test. "The bridge is two steps, not one" is negative parallelism, but
the "one" it corrects is the net-debt shortcut the piece names and spends a
paragraph on, so the contrast is earned. No empty conclusions, decorative
analysis, puffery, or vague attribution surfaced. Compared distinctive phrasing
against the voice-guide quotations (Damodaran/Mauboussin/Buffett): no borrowed
clauses — the piece follows their method (each figure produces the next in a
parenthetical the reader can re-derive) without lifting their wording. No prompt
leakage against commission or brief.

One sentence failed the density heuristic (the single unresolved
W-SENTENCE-DENSITY the writer could not isolate). It was not in the
source/bookend region the writer guessed but in the claims-ahead section: a
40-word, three-join sentence beginning "Cash beyond what operations need is the
plainest example, and so is a cross-holding..." Split into three sentences,
preserving every fact, the citation, and the register. Warning cleared; the
proof now reads BLOCK 0, WARN 0.

Recent-record comparison of edges and headings: the dek escapes the recent
investing mold — the last several deks are one-line quantified "A does B" claims
and several use the two-company contrast (Coca-Cola/Verizon, Copart/Crocs); this
one opens on the filing basis, names the two-step method, and stays on Uber
alone. Good. But one heading, "Uber's bridge, line by line," is built on the
same "[subject], line by line" pattern as the free-cash-flow lesson's "Building
Apple's number, line by line." Retitled to "Walking Uber's bridge in real
dollars," which names the section's work in the piece's own nouns and breaks the
formula. The `data-nb-section` label still mirrors it. No other heading repeats a
prior article's construction.

## Reader

Read straight through as the course's reader: what I have that the sources alone
would not give me is Uber's scattered 10-Q lines — the debt note, the
investments and equity-method notes, the NCI note, the basic-to-diluted
reconciliation — assembled into a single two-step bridge that shows, from the
company's own numbers, that its strategic stakes outweigh its debt and dilution,
plus the resolution of a mismatch the filing never flags (the point-in-time
share count behind the market quote vs. the period-averaged diluted count in the
EPS footnote). That matches the draft-handoff's original-work sentence, and
neither answer is a restatement of any one source. The prose sits closer to the
voice-guide exemplars than to a median summary: every dollar traces back to a
line the reader has already seen, and the parentheticals let the reader
re-derive each step rather than take the sentence's word. The headline, read as
the largest claim, is one the piece defends.

## Edits

- Split the 40-word, three-join sentence in the claims-ahead section ("Cash
  beyond what operations need is the plainest example, and so is a
  cross-holding...: a passive holding earns no place...") into three sentences,
  clearing the last W-SENTENCE-DENSITY warning without changing any fact or the
  citation.
- Retitled the third body heading from "Uber's bridge, line by line" to "Walking
  Uber's bridge in real dollars" to break the "[subject], line by line" formula
  shared with the free-cash-flow lesson.

## Required work

None. Both remaining items were editor-owned and made directly. No claim broke,
no evidence gap was found, and no prose failure needs new reporting. The
orchestrator re-runs the proof and re-stamps after these edits.

(Observation for the record, not routed: the book-vs-fair-value-of-debt judgment
point is the one of the seven the lesson does not surface; the article uses book
value, consistent with the evidence's own stated default, and asserts nothing as
settled, so it is honest as written and needs no change.)

## Decision

approve — the bridge arithmetic reconciles to the filing, the back-solved EV and
the seven judgment points are handled transparently and honestly, every citation
lands on its source with descriptors verified, and the two editor fixes (the
sentence split and the heading retitle) leave the proof at BLOCK 0, WARN 0.
