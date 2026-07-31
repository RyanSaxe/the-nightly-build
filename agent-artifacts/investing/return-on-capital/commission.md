# Commission — investing/return-on-capital

## Assignment
The next lesson in the cumulative investing course. The course has now taught the
three financial statements: the income statement (`how-a-business-earns-a-profit`,
what a business earns), the cash flow statement (`profit-versus-cash`, profit vs
cash), and the balance sheet (`what-a-company-owns-and-owes`, what it owns and
owes). The next most important concept toward independent investment judgment is
**return on invested capital (ROIC)**: the single number that turns
statement-reading into a judgment about whether a business is any good.

## Angle / required contribution
Teach two or three ideas completely, in order:
1. **Invested capital.** The money put into the business to run it, read off the
   balance sheet already taught: roughly the capital suppliers' claims (debt +
   equity), or equivalently the net operating assets those claims fund. Define it
   plainly and show where each piece comes from on a real balance sheet.
2. **ROIC = after-tax operating profit / invested capital.** Define NOPAT
   (operating profit taxed as if the business had no debt) using the income
   statement already taught, divide by invested capital, and work the whole
   calculation once with real 10-K numbers.
3. **The value-creation test: ROIC vs the cost of capital.** A business creates
   value only when it earns more on its capital than that capital costs; when
   ROIC is below the cost of capital, growth destroys value. Teach cost of
   capital only at the level this test needs (the return investors could earn
   elsewhere at similar risk), and explicitly leave its precise measurement (a
   weighted average cost of capital) and full valuation to a later lesson. Leave
   that ground open for the course to build on.

The transferable payload: profit alone cannot tell you if a business is good;
the same profit on a tenth of the capital is a different business. ROIC is how a
reader compares two businesses that both "make money."

## Worked example / real numbers
Work ROIC once, end to end, with real figures from a real filing. Costco keeps
course continuity (prior lessons used it), so Costco is acceptable as the worked
example — but the lesson teaches the concept, not a Costco tour. Then illustrate
the value-creation test with a brief, real contrast: a high-ROIC, capital-light
business vs a capital-heavy business whose ROIC sits near or below its cost of
capital (e.g. a regulated utility, an airline, or a large telecom). The
researcher supplies verified numbers from the actual 10-Ks for both. Keep every
figure sourced; do not invent or round away the source.

## Reader (lesson template)
Smart, reads widely, new to THIS subject. Explain everything the field takes for
granted (what "operating profit," "after-tax," and "capital" mean here) in plain
words at first use, without talking down. Rely on the three prior lessons via
Background links instead of re-teaching them; if a step needs a foundation those
lessons did not lay, teach it here briefly or cut the step.

## Template / structure / paths
- Series `investing`, mode `open`, template `lesson`.
- nb-meta: `mode: "open"`, `order: null`, `date: "2026-07-31"`. (The course is
  cumulative but the lesson template records `order: null`; sequencing lives in
  Background links, not the order field.)
- Article: `library/investing/return-on-capital.html`. Words 1200-2200.
- Fixed order: `why` bookend → body (flex 0-4 sections) → `takeaway` bookend →
  `sources`. Write the body first; write both bookends after, about THIS lesson's
  particulars (invested capital, ROIC, the cost-of-capital test). Bookends carry
  no citations. Background band links the three prior lessons (relative links
  into this library); Go deeper links beyond the paper.

## Source obligations
- Template floor: **min 6 sources**, all read and resolving.
- Every number comes from a primary filing (10-K/annual report) or an
  authoritative reference. Definitions of ROIC/NOPAT/invested capital should rest
  on an authoritative source (a finance text, Damodaran, CFA/Investopedia-grade
  reference read and verified) — but the article teaches in its own words.
- Contested/convention-dependent choices (how to define invested capital, how to
  treat cash, leases, goodwill) must be stated honestly as conventions, not
  presented as the one true formula.

## Starting sources (verify each)
- Costco's most recent 10-K (income statement + balance sheet lines for NOPAT and
  invested capital).
- The contrast company's most recent 10-K.
- An authoritative definition source for ROIC/NOPAT/invested capital and the
  value-creation test (e.g. Aswath Damodaran's materials; McKinsey's *Valuation*;
  a reputable finance reference) — read, not just cited.

## Relevant prior coverage / structures NOT to repeat
Prior lessons opened on a concrete company fact and taught one statement each.
Do not restage a full statement walkthrough. Do not default to quarterly
earnings. Vary the opener and headings from the three prior lessons; name
sections for the steps of THIS lesson's argument (invested capital → ROIC → the
cost-of-capital test), not a generic outline.

## Neighboring articles tonight
paper-of-the-day, tech-news, current-events, expert-tools, unbiased,
word-of-the-day. This is the edition's markets/finance teaching read.

## Harness / model (balanced profile)
coach sonnet/low; researcher sonnet/high; writer sonnet/medium; editor opus/high.
nb-meta `harness: "claude-code"`, `model: "claude-sonnet-5"`.

## Publication bar
6+ real read sources; a fully worked ROIC calculation with sourced real numbers
and a real contrast; honest treatment of invested-capital conventions; bookends
that set up and resolve THIS lesson; 1200-2200 words; `nb check` BLOCK: 0; editor
DONE.
