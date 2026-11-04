# Draft handoff: daily-brief/2026-11-04 (writer 01)

Original work: the brief turns a fast-moving AP seat tally into a dated House call, bracketed between
two timed reads of AP's own data, and turns Hugging Face's testing post into the UMT5 date window a
fine-tuner can check against.

## AP House status recheck (the lead changed)

- foxnews.com/elections/2026/midterm-results/house (AP data, "Source: The Associated Press"), read
  via curl and the `__NUXT_DATA__` `bop.congress` object at 06:26:46 UTC and again at 06:29:54 UTC
  4 Nov. Both reads: House D 219 (flagged `isWinner: true`), R 126, 90 remaining, D gain 25. The
  race-call panel header reads "Democrats take the House". Newest race call in the list:
  "Nov 4 • 1:24 AM ET", AP calls Oregon District 5 for Janelle Bynum. Senate unchanged from the
  record: D 19 won + 34 not up = 53, R 41, 6 remaining, D gain 7, D flagged winner.
- The researcher's last read (06:22:58 UTC) had no House winner, so AP's House call falls between
  1:22 and 1:26 a.m. ET (EST, UTC-5). The page gives no minute for the control call itself, and the
  article prints the window, not a minute.
- PBS route: the PBS-hosted AP story still reads "The House remains too early to call" (unchanged
  since its 04:46 UTC modification). The PBS politics index at 06:27 UTC carried no AP House-control
  story. So AP's House call is established only through AP's data as rendered on Fox, and the editor
  should cite it that way (source 4). The figures may move again before publication.
- NBC's projection and NPR's reading are left out: with AP's call in hand, neither adds a fact.

## Proof

`nb check ... --series daily-brief --repo /home/user/the-nightly-build` with links:
BLOCK 0, WARN 0, PUBLISHABLE. 663 words, 11 sources.

## Choices the editor may question

- Second sources: the lead uses the PBS-hosted AP story (Senate call, Texas and Ohio wins, the net
  gain of three needed) beside AP's data; Missouri uses the separate STLPR Amendment 3 story;
  Israel uses CNN for the MOU and appropriation facts; StateBench uses the Ai2 blog for the
  training setup (275M, 256 to 64,000) and the paper for the proof and frontier result.
- Psephology: Hardie is left out per the commission. The card opens on Nuffield's "academic joke"
  line, not on the coiner's wish.
- The UMT5 item's last sentence ("worth rechecking") is the brief's own consequence, uncited.
- Senate figure 53 is AP's count; whether it includes Sanders and King is the researcher's
  inference, so the article does not say.

## Open questions

None blocking.
