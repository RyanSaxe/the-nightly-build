# Editorial review: daily-brief/2026-11-10 (editor/01)

## Correct

The brief has no single thesis. Its working claim, from the draft alone, is
that each of six items states what its owner says and sets beside it the fact
in the same record that limits it. Under that claim:

1. The Court stayed the Big Bend injunction because a major-questions claim is
   statutory and IIRIRA §102(c)(2)(A) admits only constitutional claims.
2. Trump calls the Iran war militarily over while the blockade continues and
   US forces keep striking.
3. France attributes the October refrigeration attacks to an IRGC-linked unit
   and Paris prosecutors seek warrants, after earlier suspicion fell on
   pro-Russian groups.
4. Anthropic's and Google's figures are their own, with the limits their own
   pages print.

How each held, against the documents reopened today:

- Word card. Merriam-Webster gives the adjective, the respelling, "composed of
  both good and evil", agath- + kako- + -logical, and first known use 1834.
  The Gutenberg HTML of *The Doctor*, vol. II, has a title page with no author,
  the London 1834 imprint, and the quoted sentence in ch. LIII. One break: the
  draft said the sentence comes "after a page on writers who misuse words".
  It comes after a single paragraph. Fixed.
- Big Bend. The per curiam order (No. 26A560, 9 November) supports every
  phrase I tested: the 2 October injunction, "exceedingly likely", the
  §102(c)(2)(A) limit, the quoted line on p. 3, the CBP declaration of
  "nearly half a million dollars in costs per day", and "JUSTICE JACKSON would
  deny the application for stay." One narrowing: the order says the injunction
  blocked the waivers and "all associated construction", and the draft said
  "all construction in the Big Bend Sector". Now "the waivers in the Big Bend
  Sector and the construction under them". The order also says the stay runs
  until the certiorari petition is disposed of, which the item lacked and a
  reader needs to know what follows. Added as "pending a certiorari petition".
- Iran. The AP story on WLKY carries every quote. AP calls the strikes
  "limited strikes ... at least twice over the past week". The draft dropped
  "limited". Restored.
- France. NPR attributes the 700 sites and the spoiled food to ANSSI. France 24
  carries the prosecutor's judicial investigation of the Shahid Kaveh chief and
  two deputies, the warrant request, Farsi and the Iranian IP addresses, the
  pro-Russian first suspicion, and the Kremlin's 5 November denial. France 24
  dates the assignment of investigating judges to Monday 9 November; its
  cybercrime section had taken the case on 12 October. The item's "On 9
  November ... opened an investigation" matches. No break.
- Anthropic. The page says the two are the same underlying model, Mythos is
  reached through the Cyber and Life Sciences Verification Programs, and the
  price is $8/$40. The Fermat passage says the first formalization, by an
  unreleased research model, used a purpose-built harness and a human
  researcher's guidance. The draft gave the 11 days without that, which made
  the 30 hours read as a like-for-like comparison. Narrowed to "its first,
  human-guided formalization". AutomationBench is 51.4% against Gemini 4
  Carbon's 53.9%. Confirmed. "All of it is self-reported" covered the prices,
  which are Anthropic's list, not a claim. Narrowed to "every capability
  figure".
- Google. The post says TPU 8i Max has double the compute, SRAM and HBM
  bandwidth *of TPU 8i*, and separately that it fits twice the silicon in the
  existing rack footprint. The draft fused these into "twice the compute, SRAM
  and HBM bandwidth in the existing rack footprint". Separated. The 8tx
  pairing, the AMD EPYC hosts and "up to 2x lower latency" are on the page,
  and the post gives no availability date or prices.

Headline, dek and item headings checked against the documents: the order is
per curiam and the petitioner is the Homeland Security Secretary; Trump's
"effectively over" is AP's quotation; Barrot names the Revolutionary Guards
(France 24); the attacks were 11 and 12 October; the Mythos access route is the
Verification Programs; the TPU 8i Max package holds two TPU 8i chips.

Every printed href, opened as printed:

- s1 Merriam-Webster: 200, lands on the entry.
- s2 Gutenberg: the draft printed the catalog page (`/ebooks/69534`), a
  summary page with download buttons. It did not land on the words. Replaced
  with the HTML text anchored at ch. LIII
  (`/cache/epub/69534/pg69534-images.html#sect25`), 200 in curl and Chromium.
  Same document, same locator, same claim.
- s3 Supreme Court PDF: 200, the order.
- s4 WLKY: 200, the AP story.
- s5 NPR: 200, the story.
- s6 France 24: 403 to curl from the site's France Médias Monde gate; 200 with
  the article title in headless Chromium, and readable through WebFetch. A
  reader's browser lands on it.
- s7 Anthropic: 200, the release page.
- s8 Google: 200, the post.

`data-nb-kind`: Merriam-Webster, AP, NPR and France 24 are secondary; the
order, the 1834 text, Anthropic's page and Google's post are primary to the
claims they carry. NPR and France 24 are separate newsrooms both reporting
French statements, so the France item claims no independent primary it does
not have. No change.

## Reads well

- The dek was the comma triad `spec/headlines.md` bans ("A major-questions
  claim is statutory, the order holds, and the waiver statute allows only
  constitutional claims"), and its middle clause said nothing a reader could
  use. Rewritten as one clause that gives the holding and why it ends the
  case: "An unsigned order holds that a major-questions claim is statutory and
  so outside the only suits the waiver law allows." It avoids the recent
  procedural-consequence and counted-contrast molds.
- The word card's last sentence went. Its clause "'first recorded in' is as far
  as the record goes" came from the commission's decision line, quoted marks
  and all, and talks about the reporting instead of the word. The rest of the
  sentence repeated the earlier "anonymous miscellany that Gutenberg's catalog
  credits to Robert Southey". In its place the card now closes on a fact that
  ties the dictionary to the text: the volume's 1834 imprint matches
  Merriam-Webster's first-known-use year. That also changes the close from the
  recent run of cards ending on the coiner's quotation.
- "According to ANSSI, France's cybersecurity agency, as NPR reports it" stacked
  two attributions in front of the news. Now "France's cybersecurity agency,
  ANSSI, says". The citation to NPR carries the route.
- The Google item opened by repeating its own heading word for word ("puts two
  TPU 8i chips on one package"). Cut, and the sentence now gives the figures.
  Its closer "The figures are Google's" sat beside the Anthropic item's
  self-reported line and would have made two consecutive items end on the same
  shape. Cut; attribution is in "Google says" and "Google claims".
- The headings' verbs (clears, calls, blames, releases, puts) avoid the
  recent "says", "backs" and "orders". No change.

The draft was not running flat. The items state actions with the actor as
subject and give figures in the sources' units, as the voice guide asks.

## The experience

At 1280px and 390px, in both themes, the page renders without horizontal
scroll or console errors. At desktop width the word card breaks the term as
"agathokako / logical" with no hyphen. It reads, and the break falls between
morphemes. Fixing it belongs to the card's CSS, not to the article, so I left
the text alone rather than plant soft hyphens in the term. No component was
added. At two or three sentences an item, a table or stat strip would repeat
the prose.

What the piece gives beyond its sources: each item puts the owner's claim and
the limiting fact from the same record side by side (Jackson's recorded vote,
the strikes beside "effectively over", the pro-Russian first suspicion, the
human-guided first formalization and the AutomationBench deficit, no TPU
dates), and the word card links the dictionary's date to the text that
supplies it. That matches the writer's original-work sentence.

## Edits

- Dek (header and nb-meta): replaced the comma triad with the one-clause holding.
- Word card: "and dates its first known use to 1834" cut from the first sentence.
- Word card: "It appears in" became "It appears in the second volume of".
- Word card: "a page" became "a paragraph".
- Word card: last sentence replaced with the 1834 imprint / first-known-use sentence, cited to s1 and s2.
- Big Bend: added "pending a certiorari petition"; "and all construction in the Big Bend Sector" became "in the Big Bend Sector and the construction under them".
- Iran: "struck Iran" became "made limited strikes on Iran".
- France: opening attribution became "France's cybersecurity agency, ANSSI, says".
- Anthropic: "the first formalization" became "its first, human-guided formalization"; "All of it is self-reported, and its table has" became "Every capability figure is self-reported, and Anthropic's own table puts".
- Google: first sentence rewritten to separate the per-chip doubling from the rack footprint; "The figures are Google's, and" cut.
- Sources: s2 href moved from the Gutenberg catalog page to the ch. LIII anchor of the HTML text.
- `nb stamp`: 691 words became 679, 3 min, 8 sources.

Proof after the edits, links on: BLOCK 0, WARN 0, PUBLISHABLE.

## Decision

approve: the claims hold against the reopened documents, the banned dek mold
and the briefing leak are gone, and the proof passes.
