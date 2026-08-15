# Evidence: opinion/hack-back-authorization (researcher/02)

This is a targeted second pass on the two confirmations the editor routed
(editor/01/editorial-review.md, "Required work"). It does not repeat
researcher/01/evidence.md, which stands and is preserved in full; both records
apply together. Both source URLs were reopened directly (curl with a
browser-style user agent, HTTP 200, no redirect) and read as raw page text, not
through a summarizing fetch, specifically so the exact wording could be checked
character for character. Result: (1) the CNN piece never puts Wysopal's
"hospital" sentence in quotation marks in the first place — it is the
reporter's own reported speech, and the verb is "affect," not "hit," so there
is nothing verbatim to quote and the marks must come out; (2) s7 does not name
the Active Cyber Defense Certainty Act — it describes "prior proposals" only in
the generic, exactly as the editor suspected — but a new, independent source
found in this pass (TechTimes) does name the Act by name in direct connection
with this memo, so the writer has a real choice between generalizing (s7
supports it verbatim in spirit) or citing the Act by name to the new source.

## Sources

```text
URL:         https://www.cnn.com/2026/08/13/politics/cyber-privateers-trump-order-overseas-groups-hacking
Kind:        Secondary — CNN reporting (same source as researcher/01's s1;
             reopened here specifically for exact wording).
Establishes: The precise sentence structure CNN uses for the Wysopal
             "hospital" material: indirect reported speech, not a direct
             quotation. No quotation marks appear around any part of this
             sentence in the source.
Paraphrase:  The full sentence, exactly as it appears on the page: "Hacking a
             data center in a foreign country to target scammers could, for
             example, inadvertently affect a hospital, he said." This is
             reported/indirect speech (subject "Hacking...", not "I" or a
             quoted first-person construction) closed with "he said," and nCNN
             does not set any part of it off in quotation marks. The verb is
             "affect," not "hit." A second, separate sentence in the same
             paragraph — also indirect, also unquoted — carries Wysopal's
             point about employees of participating firms being treated as
             legitimate targets for detention abroad.
Locators:    Fetched directly via HTTP (browser user-agent, HTTP 200, final
             URL unchanged, no redirect) and read as raw page text on
             2026-08-15; archived at
             /tmp/claude-0/-home-user-the-nightly-build/50965123-8347-5b00-8e08-9db91a08ee75/scratchpad/cnn.html.
             The sentence appears once in the article body, in the paragraph
             introducing Wysopal by name and title ("co-founder of
             cybersecurity firm Veracode").
Quote:       None available as a direct quotation — this is the finding.
             Verbatim page text, for the record: "Hacking a data center in a
             foreign country to target scammers could, for example,
             inadvertently affect a hospital, he said."
```

```text
URL:         https://cyberscoop.com/trump-memo-private-sector-offensive-hacking/
Kind:        Secondary — CyberScoop reporting (same source as researcher/01's
             s7 on the CFAA/prior-proposals point; reopened here for the
             specific Act-naming question). Headline on the page itself:
             "Trump turns to private sector in offensive hacking operations
             memo," byline Tim Starks — this is researcher/01's first
             CyberScoop entry (URL matches exactly); it is the only opened
             source that carries the "prior proposals... would have amended"
             sentence the draft's ACDC Act reference traces to.
Establishes: That s7 does not name the Active Cyber Defense Certainty Act (or
             any other bill) by name anywhere in the article. It describes
             the category only, generically, as "prior proposals."
Paraphrase:  Full sentence, verbatim from the page: "The program would have to
             adhere to existing laws, according to the memo. That includes the
             Computer Fraud and Abuse Act, the main federal anti-hacking
             statute that prior proposals to open private sector
             participation in hacking operations would have amended." No bill
             name, sponsor, or year appears anywhere in the piece — confirmed
             by a full-text search of the fetched page for "Active Cyber
             Defense," "ACDC," and "Certainty Act" (zero matches on all
             three).
Locators:    Fetched directly via HTTP (browser user-agent, HTTP 200, final
             URL unchanged, no redirect) and read as raw page text on
             2026-08-15; archived at
             /tmp/claude-0/-home-user-the-nightly-build/50965123-8347-5b00-8e08-9db91a08ee75/scratchpad/cs1.html.
             The sentence is in the article's second paragraph.
Quote:       "That includes the Computer Fraud and Abuse Act, the main federal
             anti-hacking statute that prior proposals to open private sector
             participation in hacking operations would have amended."
```

```text
URL:         https://www.techtimes.com/articles/324283/20260813/trump-authorizes-private-firms-hack-foreign-criminals-legal-basis-untested-courts.htm
Kind:        Secondary — TechTimes news reporting, named byline, dated the
             same day as the memo's coverage cycle. New source, not in
             researcher/01.
Establishes: A source that does name the Active Cyber Defense Certainty Act
             by name, its 2017 introduction, and its sponsor's chamber
             context, explicitly contrasted against this August memo's
             narrower legal theory (no statutory amendment, an existing-
             exemption reading instead). If the writer wants to keep the Act's
             name in the piece rather than generalize, this is the source to
             cite for it — s7 will not support the name.
Paraphrase:  By Ryan Cook, published Aug. 13, 2026, 10:11 AM EDT. States that
             "a decade of legislative proposals — most prominently the Active
             Cyber Defense Certainty Act, first introduced in 2017 — tried and
             failed to amend the Computer Fraud and Abuse Act (CFAA) to permit
             private-sector offensive cyber operations," that "Congress
             rejected the approach twice," and that this August memorandum
             "does not amend anything" but instead relies on CFAA Section
             1030(f)'s existing law-enforcement exemption — the same
             exemption-vs-amendment distinction the draft argues, independent
             of the article under review. Consistent with the general-
             knowledge fact pattern (ACDC Act, Rep. Tom Graves, R-Ga.,
             introduced 2017 and reintroduced 2019, never received a floor
             vote) but the article itself does not name Graves or the 2019
             reintroduction; cite only what it states.
Locators:    Fetched directly via HTTP (browser user-agent, HTTP 200) and read
             as raw page text on 2026-08-15; archived at
             /tmp/claude-0/-home-user-the-nightly-build/50965123-8347-5b00-8e08-9db91a08ee75/scratchpad/tt.html.
             Second paragraph of the article body.
Quote:       "A decade of legislative proposals — most prominently the Active
             Cyber Defense Certainty Act, first introduced in 2017 — tried and
             failed to amend the Computer Fraud and Abuse Act (CFAA) to permit
             private-sector offensive cyber operations. Congress rejected the
             approach twice, citing misattribution risks, foreign policy
             complications, and the specter of uncoordinated private hacking
             cascading across international infrastructure."
```

## Contradictions

None found between this pass and researcher/01, and none between the two
sources reopened here. TechTimes' account of the ACDC Act's history (2017,
never passed) matches general subject-matter knowledge and does not conflict
with CyberScoop's silence on the name — CyberScoop simply describes the
category without naming an instance, which TechTimes does name. No source
disputes that this August memorandum does not itself amend the CFAA.

## Numbers

None — this pass verifies wording, not figures. See researcher/01 for the
article's numeric evidence, unchanged by this round.

## Source assets

None found — both items are wording-verification questions, not visual
evidence.

## Discarded

```text
URL: https://cyberscoop.com/private-sector-hacking-presidential-memo-cybersecurity/
Reason: Re-checked as a candidate for s7 alongside the CyberScoop URL above
        (both are CyberScoop, both discuss the memo, and the brief's
        description of s7 was not an exact headline match to either). This
        one does not contain the CFAA/"prior proposals would have amended"
        sentence at all — that sentence is unique to the other CyberScoop URL
        — so it is not the source the ACDC Act reference could trace to.
        Confirmed via full-text search of the fetched page: zero matches for
        "Active Cyber Defense," "ACDC," "amended," or "prior proposals."
        Ruled out as s7; not used in this record beyond this check.
```

## Report to orchestrator/editor

1. **Wysopal quotation.** Not verbatim, and not a quotation at all in the CNN
   source — it is indirect reported speech ("...could, for example,
   inadvertently affect a hospital, he said"), with "affect," not "hit." The
   writer must drop the quotation marks entirely and render it as reported
   speech/paraphrase in the article's own words, keeping "affect" (or a
   synonym that does not overstate CNN's own verb) rather than "hit."
2. **Active Cyber Defense Certainty Act.** s7 (CyberScoop,
   cyberscoop.com/trump-memo-private-sector-offensive-hacking/) does not name
   the Act — confirmed by full-text search, zero matches. Two paths, writer's
   choice: (a) generalize to "earlier congressional proposals... that would
   have amended the statute," which s7 supports verbatim; or (b) keep the
   Act's name and re-cite that clause to the new source found in this pass,
   https://www.techtimes.com/articles/324283/20260813/trump-authorizes-private-firms-hack-foreign-criminals-legal-basis-untested-courts.htm,
   which names it directly and states it "first introduced in 2017" and
   "rejected... twice."

Both URLs (CNN and CyberScoop s7) resolve cleanly: HTTP 200, no redirect, page
content matches the URL's own topic and dateline.
