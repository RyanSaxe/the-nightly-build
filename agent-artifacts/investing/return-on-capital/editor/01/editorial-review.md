# Editorial review — investing/return-on-capital (01)

Fresh-eyes gate on the lesson. Three ordered reads. All numbers recomputed
against the evidence record; conventions, deferral of WACC/valuation, the two
bookends, the Background linkage, and teaching completeness checked. Final proof
is BLOCK: 0, WARN: 0, PUBLISHABLE.

## Skeptic

Skeptic: thesis "a single worked ratio, NOPAT over invested capital, turns three
financial statements into one comparable judgment, and that judgment only means
something once it is set against the cost of capital — which is why Costco
(37.4%) and AEP (~5-6%) land on opposite sides of the value-creation line though
both are profitable"; tested 6 claims; broke: none.

Recomputed every figure against the evidence record and both primaries:

- Costco invested capital: 5,788 debt + 29,164 equity − 14,161 cash = **20,791**. ✓
- Costco NOPAT: effective tax 2,719/10,818 = 25.13%; 10,383 × 0.7487 = **7,773**. ✓
- Costco ROIC: 7,773/20,791 = **37.4%**. ✓
- Alternates: net short-term investments too → 19,668 → **39.5%**; no cash netting
  → 34,952 → **22.2%**; averaging year-end balances → 20,202 → **38.5%**. All ✓.
- AEP invested capital: 48,830 debt + 32,218 equity (incl. NCI) − 197 cash =
  **80,851**, which is 3.89× Costco's — "nearly four times" is fair. ✓
- AEP NOPAT/ROIC three ways: 3.46% → 5,135 → 6.4%; 21% → 4,202 → 5.2%; ~25% →
  3,989 → 4.9%. Band **4.9-6.4%**. All ✓.
- AEP effective rate 129/3,724 = 3.46%. ✓
- Cost-of-capital references: retail WACC 7.27% ("about 7.3%"), utility WACC
  4.36%, all present in source 7; Costco clears retail by ~30 points (37.4 − 7.27).
  ✓

Convention honesty: the invested-capital choice is stated **as a convention, not
the one true formula** — cash-only netting, year-end (not averaged) balance, and
operating leases left as expense, each with its one-clause reason and its actual
swung number, closing on "None of these choices is the one true formula." This is
disclosure, not hedging, exactly as the voice guide asks. WACC computation and
full valuation are **explicitly deferred** to a later lesson in the final section
("its own calculation, for a later lesson").

Regulator ROE precision: the article says AEP **requested** 10.9% (Ohio), 10.8%
(Oklahoma), 10% (Kentucky), each pending, and that West Virginia **explicitly
authorized** 9.25% — matching the evidence record's instruction not to call all
four "authorized." ✓

`data-nb-kind` audit: s1 Damodaran ROIC paper (primary — owns the definitions),
s2 Costco 10-K (primary), s5 AEP 10-K (primary), s7 Damodaran sector dataset
(primary — his own compiled data), s3 CFI / s4 Wall Street Prep / s6 Enerdynamics
(secondary). Every label matches the evidence record's classification. Article
source numbering (s1-s7) differs from the evidence record's numbering but is
internally consistent and correctly cross-referenced. No sourcing failure.

Hardest test — the AEP cost-of-capital comparison. ROIC is a return on *total*
invested capital, while a regulator's allowed ROE is a cost on the *equity* slice
only, so comparing them is not strictly apples-to-apples; the technically clean
comparator for ROIC is WACC, and against the sector WACC (4.36%) AEP's 4.9-6.4%
narrowly *clears* its cost of capital. I pushed on whether elevating the ROE as
"the more direct comparison" retires the lesson's own thesis. It does not, for
three reasons the draft handles in the open: the article shows both yardsticks
and states plainly that they "measure different things," naming the ROE as what
"AEP's equity investors need" (so the equity-only basis is surfaced, not hidden);
it justifies "more direct" on company-specificity grounds (AEP's own filing vs. a
14-firm sector average), which is a valid distinction; and it lands not on a false
verdict but on "Costco's gap ... is wide and positive, AEP's is narrow, and by
its own regulators' math, still open." The taught conclusion is that AEP sits
*near* its cost of capital and the answer is genuinely ambiguous — which is
correct — and precise WACC is deferred. This is the framing the evidence record
itself recommended, presented with its tension intact. Defensible teaching, not a
broken premise. Recorded here for the record, not as a required change.

## Cut

Cut: 4 edits, ~65 words; worst tell: a one-sentence paragraph captioning the
Costco ROIC result after the arithmetic had already delivered it.

Direct edits made (prose/structure only):

1. Deleted the paragraph "That is what the business kept, after tax, for every
   dollar its lenders and shareholders had at work in it that year, before a
   single dollar of that profit is compared to anything else." It restated the
   37.4% the sentence above had just produced (the exact caption-after-a-
   calculation the voice guide bans) and signposted the next section, which
   opens with that pivot on its own. The ROIC section now ends on the number.
2. Cut ", which shows how much the choice matters" — a self-grading tag on the
   22.2% alternate; the paragraph's own close ("None of these choices is the one
   true formula ...") already earns the point.
3. Cut "Those choices move the number enough to matter." — announces importance
   before the very demonstration (39.5%, 22.2%) that proves it.
4. Trimmed "and that disagreement is worth sitting with rather than resolving by
   picking whichever number fits the story" to "." — self-congratulatory
   method-narration; the substance (the two estimates measure different things)
   is carried by the sentences that follow.

Updated `nb-meta` `words` 2027 → 1962 to match the recount after cuts (engine
`word_count` = 1962; within band 1200-2200). No other markup touched.

Prompt-leakage sweep against the writer brief: the section names ("The money
behind the profit", "Thirty-seven cents on the dollar", "The number growth has to
clear") are this lesson's own argument steps, not the brief's planning labels; no
selection rule, assignment-fulfilled claim, or scaffold heading survived into
copy. Bookends carry no citations. No leak found.

## Reader

Reader: this gives me a single ratio that fuses an income statement and a balance
sheet into one number I can compare across two very different businesses, the
discipline that the number is meaningless until measured against what the capital
could earn elsewhere, and — through the AEP case — the honest lesson that the
cost-of-capital side is not always one clean figure. The sources alone (Damodaran's
definitions, two 10-Ks, a sector WACC table) never make this comparison; the
article builds it. This matches the draft handoff's original-work sentence, which
survives. Voice sits with the Damodaran/Mauboussin exemplars — worked calculation
in plain declaratives, conventions disclosed in a clause each — not a median AI
summary.

Bookends read back to back: "Why this matters" opens on the real confusion (two
businesses, same profit, different investments) and promises the worked calc plus
the "is the return actually good" test; "The takeaway" resolves it ("Profit by
itself never answers whether a business is good. Return on invested capital
does...") and hands back the two-step comparison plus the Costco/AEP verdict,
using only terms the body set and no citations. Setup and resolution; neither
could be moved to another lesson.

Background band links the three prior lessons (how-a-business-earns-a-profit,
profit-versus-cash, what-a-company-owns-and-owes), each with a one-line note tying
it to a number this lesson uses; the lesson is self-contained for a reader who
opens none (invested capital's debt/equity/cash pieces are defined inline). Go
deeper points beyond the paper (Damodaran's paper and sector dataset). Teaching is
complete across three ideas — invested capital, the ROIC calculation, the
cost-of-capital test — each with a plain statement, a real worked example, and its
reason, not six things in passing.

Headline as largest claim: "Costco turns each invested dollar into 37 cents of
profit" — subject, fresh verb, the number as the surprise, no colon; defended by
the 37.4% the body computes. Dek adds the AEP contrast without restating the
headline and makes a claim about the world (AEP's return below what its regulators
call fair), not a grade of the article's method. Both pass `spec/headlines.md`.

## Required work by owner

None. No researcher or writer request.

## Decision

Approve. All edits were surgical cuts within the editor's scope; proof is
BLOCK: 0, WARN: 0, PUBLISHABLE.
