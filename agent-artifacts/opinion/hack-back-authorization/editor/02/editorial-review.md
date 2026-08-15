# Editorial review: opinion/hack-back-authorization (editor/02)

Confirmation read after the two-item citation/quotation repair routed in
editor/01. This round verifies only what changed and checks for regression; the
argument, legal spine, counter, position card, and slop pass were settled in
editor/01 and are not reopened.

## Skeptic

Two items were routed to the researcher in editor/01; both are now resolved and
land against the source.

1. **Wysopal line (s1, CNN).** editor/01 flagged that the "hospital" sentence
   was printed as a direct quotation the record did not pin down, with a search
   rendering reading "affect," not "hit." researcher/02 reopened the CNN page
   directly and found the sentence is CNN's own indirect reported speech, not a
   quotation, verb "affect." The writer dropped the quotation marks and recast
   it as reported speech. I reopened the CNN URL myself (HTTP 200, no redirect):
   the page reads "Hacking a data center in a foreign country to target scammers
   could, for example, inadvertently affect a hospital, he said," with no
   quotation marks anywhere around it, and identifies him as "Wysopal, co-founder
   of cybersecurity firm Veracode." The article now prints "hacking a data center
   to target scammers could, he said, inadvertently affect a hospital" — no
   marks, verb "affect," reported speech, title correct. Lands and matches. The
   marks-assert-a-verbatim-quote defect is gone.

2. **Active Cyber Defense Certainty Act (s7).** editor/01 flagged that the Act's
   name was cited to a CyberScoop piece that named only "prior proposals"
   generically. researcher/02 confirmed that (zero full-text matches on the old
   s7) and found TechTimes, which names the Act directly. The writer kept the
   Act's name and replaced the s7 slot with the TechTimes entry
   (`data-nb-kind="secondary"`). I reopened the TechTimes URL (HTTP 200, no
   redirect): it reads "most prominently the Active Cyber Defense Certainty Act,
   first introduced in 2017 — tried and failed to amend the Computer Fraud and
   Abuse Act" and "Congress rejected the approach twice." The article's clause —
   "Unlike the Active Cyber Defense Certainty Act, an earlier proposal that would
   have amended the CFAA directly and that Congress rejected twice" — is now
   carried verbatim in substance by its cited source. Lands and matches. The
   secondary kind is correct for news reporting.

**Regression check on the s7 swap.** `href="#s7"` is cited exactly once in the
body (the ACDC clause), so no renumbering was needed and none is missing. The
old CyberScoop URL is fully removed (zero occurrences) and was cited nowhere
else. The separate CyberScoop piece at s3 (critics-and-supporters) is a
different URL and is untouched. Source count holds at 10, matching nb-meta. The
data-nb-kind balance from editor/01 is unchanged (s7 secondary before and
after), and the central untested-exemption claim still rests on the two
independent legal analyses at s8/s9, so the swap moves nothing load-bearing.

**Prior direct edits, all still standing** (spot-checked in the article): dek
reads "can go after" with "now" removed (both nb-meta and dekline); § 1030(f)
quoted as "investigative, protective"; the "guardrails all rest on one point"
rewrite in place; the counter opens "The strongest case for the Program starts
with capacity" (no "not ideology"); Garcia's constitutional framing without
"rather than a legal technicality"; the merged "Capacity is real, and so is the
guardrail language, but neither reaches..."; and the Redbord-alone attribution
of the seized-assets/victim-compensation gap. The cut signposts have not
returned.

## Cut

No new slop pass this round — that read was completed and settled in editor/01,
and this is a confirmation read, not a fresh review. The two repairs changed one
body sentence (Wysopal, now reported speech and grammatical) and one source-list
entry; neither introduced a new sentence to test, and the recast Wysopal clause
reads clean. No regression to the edge sentences, furniture, or em-dash count.

## Reader

Unchanged from editor/01 and not reopened. The two repairs are wording- and
citation-accuracy fixes that do not touch the causal chain; the writer's
original-work sentence still describes the article the piece delivers. Nothing
in this round moves what the article gives beyond its sources.

## Edits

- None. Both fixes were the writer's to apply (a quotation the record could not
  pin down, and a citation needing a source that names the Act); the writer
  applied them and I confirmed them against the reopened sources. No further
  direct editing was needed.

## Required work

- None blocking. The proof was re-run by the writer after the fixes
  (`./nb check`, BLOCK 0 / WARN 0 / PUBLISHABLE; `./nb stamp` words=2076,
  reading_minutes=9, sources=10). The orchestrator stamps before the PR as usual.

## Decision

approve — both routed items are resolved and land against their reopened
sources, the s7 replacement is clean with no regression, all editor/01 direct
edits still stand, and the proof passes.
