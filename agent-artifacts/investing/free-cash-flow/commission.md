# Commission: investing/free-cash-flow

## Authorized work
Scheduled duty for UTC 2026-08-05 returned `investing` (open section, `lesson`
template). Publish exactly one lesson this run. Slug: `free-cash-flow`.

## Why this concept is next
The investing course is a cumulative syllabus; the archive is the curriculum.
Already taught (published lessons): what-a-company-owns-and-owes (the balance
sheet), how-a-business-earns-a-profit (the income statement), profit-versus-cash
(accrual profit vs. cash), present-value (time value of money), cost-of-capital
(the discount rate), return-on-capital (ROIC). The next load-bearing prerequisite
is **free cash flow**: the cash a business actually produces for the people who
funded it, after the spending needed to keep the business running and growing. It
sits exactly between what is taught and where the course is going: present-value +
cost-of-capital give the machinery to discount cash, and profit-versus-cash
established that profit is not cash — free cash flow is the cash number a
valuation discounts. It is the bridge to discounted-cash-flow valuation without
being valuation yet. Do not teach valuation here; teach the cash number itself.

## What to teach (keep it to 2-3 ideas, taught completely)
Decide the exact short list before drafting; a defensible set:
1. **What free cash flow is and why it is the number that matters** — cash from
   operations minus the investment needed to sustain/grow the business (capital
   expenditure), i.e. the cash left over for all capital providers. Contrast with
   accounting profit (build on profit-versus-cash) and say plainly what FCF
   answers that profit does not.
2. **How to build it from the statements**, with a worked example using real
   numbers: from operating cash flow (or from operating profit via the add-backs)
   to free cash flow; the role of capex, working-capital changes, and
   depreciation as a non-cash add-back. Show one concrete calculation the reader
   can follow line by line. If a real company makes it concrete, use it — but
   keep the lesson transferable, not a company walkthrough (series prompt warns
   against defaulting to a company).
3. (Only if it fits without shrinking 1-2) **The main variants and where they
   mislead** — free cash flow to the firm vs. to equity, and why a single year's
   FCF can be lumpy/negative for a healthy growing firm (so the number is
   judged over time and against what drives it). If this crowds the lesson, cut
   it to a future lesson rather than shrinking the core.

Use plain words; define every term in the sentence it first appears (capex,
working capital, operating cash flow, non-cash charge). Link earlier lessons in
Background instead of re-teaching them. Leave ground a later DCF-valuation lesson
can build on.

## Template shape (lesson)
Fixed order: **Why this matters** bookend → body → **The takeaway** bookend.
Write the body first; write both bookends after, describing the lesson actually
written. Bookends speak to the reader, resolve each other (opener sets up what
the takeaway resolves), and neither summarizes the body. Background = optional
prior reading (link earlier lessons); Go deeper = optional afterward reading
beyond this paper. The lesson must stand for a reader who opens none of them.

## Sourcing
`min_sources: 6`; word band 1200-2200. Ground definitions and any formula in
authoritative primaries: an accounting/finance authority for the definition and
the statement mechanics (e.g. FASB/IFRS on the statement of cash flows, a standard
corporate-finance text, SEC filing instructions), and — if a real company is used
for the worked numbers — that company's own 10-K/cash-flow statement as the
primary for every figure. Verify each number against the owning filing. Confirm
every URL resolves. Do not present a definition as universal when FCF has no
single GAAP definition — say plainly it is a constructed (non-GAAP) measure and
give the construction used.

## Boundaries — do not repeat
- Do not re-teach the balance sheet, income statement, accrual-vs-cash, present
  value, cost of capital, or ROIC; link them in Background. Use
  `nb history --structure investing/profit-versus-cash` (and return-on-capital)
  for continuity and to avoid inheriting a prior lesson's opener/closer/heading
  shapes.
- Non-overlap: no other edition piece is about finance.

## Template and policy
- Template: `lesson` (fixed).
- Production policy (balanced): editor required at high effort, model inherit.
  Researcher/writer models = capable. A chart or a small worked-calculation table
  is welcome if it carries reasoning (build only from verified numbers).

## Neighbors this edition
Full edition: current-events, tech-news, expert-tools/visidata, investing (this),
opinion/mandate-frontier-ai-disclosure, paper-of-the-day/denoising-diffusion,
word-of-the-day/ultracrepidarian.
