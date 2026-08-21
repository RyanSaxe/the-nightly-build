# Writer draft-handoff — current-events/2026-08-21

## Items shipped (5 of the 4–6 band)

1. $40 trillion in federal debt arrives five months early — National debt
2. A shield from ICE, but only for the plaintiffs — Immigration
3. A federal judge voids the ATF's ghost-gun rule, for four products —
   Second Amendment
4. What Indiana couldn't stop Planned Parenthood from telling minors —
   Reproductive rights
5. A Census Bureau fraud finding, unsigned — Elections

10 sources total (5 primary, 5 secondary), one primary and at least one
secondary per item, matching the template contract.

## Decisions made during drafting

- **Dropped a sixth candidate** (Missouri's Cole County Circuit Court ruling
  upholding the blocked redistricting referendum) after its only available
  court order lived behind `courts.mo.gov`, which returned HTTP 403 on every
  fetch attempt, including a plain `curl` with a standard browser
  user-agent. No resolving primary document could be produced, so the item
  was cut rather than shipped with a news article standing in for the
  primary record. Five items, both within the template's 4–6 band and
  selected purely on significance, covered the night without it.
- **Swapped one gun-rights source for a hosted mirror of the actual filed
  order** after the manufacturer-affiliated organization's own press
  release page (`saf.org`) returned HTTP 403 to both WebFetch and curl. A
  firearms-news outlet's hosted copy of the same court document (PACER Doc.
  330) resolves at HTTP 200 and was verified against the case caption,
  docket number, and judge's signature on every page before use.
- **Rewrote the Fourth Circuit item's headline** from "...for eight
  congregations only" to "...but only for the plaintiffs" mid-draft: the
  eight named plaintiffs include the Cooperative Baptist Fellowship, a
  network representing roughly 1,400 individual congregations, so
  "eight congregations" would have understated the plaintiff count's actual
  composition and overstated how narrow "eight" sounds next to "1,400."
- **Held the Iran/Hezbollah sanctions story out** as a deliberate choice, not
  an oversight — it's a real escalation but doesn't carry a distinct
  domestic law/policy/material-conditions hook beyond what the paper has
  already been covering in the Iran-conflict thread, so it failed the
  "omitting it would mislead the US reader" bar for an international item in
  this template.
- **Held the Maryland data-broker item out entirely** — Unbiased's
  two-position piece owns it, and none of the other four candidates
  underperformed badly enough to need a sixth, lower-priority item just to
  reach the band's top end.

## Proof result

`./nb stamp` then `./nb check --series current-events --library
/home/user/library-checkout`:

- First pass: 0 blocking errors, 2 `W-SENTENCE-DENSITY` warnings (two
  sentences at 40 and 42 words with 2 clause joins each).
- Fixed by splitting the flagged sentences at their natural clause breaks
  (no content cut, no citations moved) across three edit/re-stamp/re-check
  cycles as new 40–42-word sentences surfaced.
- Final pass: **0 blocking errors, 0 warnings, verdict PUBLISHABLE.**
- All ten source URLs were fetched directly (not taken on search-snippet
  faith) and confirmed to resolve at HTTP 200 before being cited; two
  candidate URLs that returned 403 (`courts.mo.gov`, `saf.org`) were
  replaced or the item they supported was dropped rather than cited anyway.

Final word count 1,279; reading time 6 minutes; both written by `nb stamp`,
not hand-set.
