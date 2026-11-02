# Draft handoff: feature/binance-hack-freeze (writer 01)

## Original work

The piece sets the Binance haul beside Bybit's by asset type and splits Binance's stablecoin side into frozen and swapped-out-first, to show that how much a freeze can reach is fixed by the share of the haul in issuer-administered tokens and by how fast the thief leaves them (77% of stolen stablecoin frozen, about 6% of everything else, 44% of the Binance haul against 3% to 3.84% of Bybit's). Fig. 1 draws the mechanism, Fig. 2 is the derived split, Fig. 3 is the Bybit contrast.

## Proof

`nb stamp` then `nb check ... --series feature --repo /home/user/the-nightly-build` with links: BLOCK 0, WARN 0, PUBLISHABLE. Words 1182 (hard cap 1200; the count includes captions, SVG text and source titles, so a revision that adds words will need cuts elsewhere). 16 sources, 4 flex sections. No warning left on purpose. Both charts were rendered with `nb chart` and inspected, and the page was checked in Chrome through `nb preview` (SVG, both charts, table).

## Open evidence notes for the editor

- Fig. 2 values are derived, not sourced: frozen stablecoin = 94% x $2.85B = $2.68B; "everything else" = $6.43B - $3.46B = $2.97B, of which $0.17B frozen and $2.80B not. The 77% and 6% follow. They mix Elliptic's theft-time and 1 November prices (caption says so; about one point of rounding error). The $0.79B segment is Elliptic's $786M, so the bar sums to $3.47B against $3.46B stolen, within rounding.
- Bybit "3% to 3.84%": only the 3.84% (21 April 2025) is on the cited Decrypt page. The 3% (4 March) comes from other coverage listed in the evidence Numbers section, not an opened source. The share is of about 500,000 ETH, not dollars (caption says so). The Bybit 0% stablecoin share is Block Scholes' (secondary) reading of the chain. Chart 3's Bybit bar is drawn at 3.84%, labelled with the range.
- "Binance has not attributed" quotes Teng's post as the evidence Contradictions section records it; that sentence is not in the Teng source's own Quote line.
- The FBI row rests on BleepingComputer; the table says the FBI's own page could not be opened.
- Elliptic's "likely" attribution is carried from the evidence record without a verbatim quote; the table row paraphrases it.
- The $36M of ETH, ARB and OP is Elliptic's chart 2 (Arbitrum $31M, Optimism $5M). Optimism is worded "appears to have moved", as Elliptic words it. WBETH and tokenized gold are named but not sized.
- Circle's $1.1B is attributed to a spokesperson via American Banker and set against $823M to $825M; not adopted.
- Dropped: BNB, "recovered", "native assets cannot be frozen". The unsettled-figure point is stated in the orientation (days old, still moving).
- The USDT contract text I used says transfers from a blacklisted address revert (msg.sender and _from checks); I did not claim blocked receiving, since the Tether source read does not check the recipient.

## Voice

No open voice question. Headline and dek have no colon, no question mark and none of the three banned dek molds; the dek and rendered dekline are identical to nb-meta.
