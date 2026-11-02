# Evidence record: feature/binance-hack-freeze (researcher 01)

Record date: 2 November 2026. Every figure below is days old and still moving. Times are UTC unless stated.

The evidence supports a narrower and more checkable version of the commission's angle than the commission states. Two analytics firms that read the chain independently (TRM Labs, Elliptic) put the stolen haul at $6.36B and $6.43B at theft-time prices. Elliptic reports $3.46B of that as stablecoins, and reports that 94% of the $2.85B frozen is stablecoin. Nothing stolen on Bitcoin, the XRP Ledger, Solana or NEAR has been frozen. The mechanism is checkable in contract source, and the 2025 Bybit theft (all ETH and staking derivatives) is a natural comparison: about 3 to 4% frozen. Four things in the evidence cut against the commission's wording and the writer should not draft around them. (1) The freeze did not catch all the freezable value. Elliptic says the attacker converted about $786M of stablecoins into ETH and TRX before the freezes landed, so a race, and not only the asset model, set the gap. (2) "Native assets cannot be frozen" has small documented exceptions: Arbitrum's Security Council and Optimism's governance moved about $36M of ETH, ARB and OP out of the attacker's reach by chain-level governance. (3) Frozen is not recovered. Binance says it is "working with partners and law enforcement to recover the frozen assets", and no source reports any frozen asset returned. (4) Ethereum's $3.8B is a chain total that includes about $2.8B of stablecoins, so it cannot be presented as ETH. The per-asset split of the frozen amount is sourced, by Elliptic (primary for its own analysis) and partly by TRM. The per-asset split of the stolen haul is sourced for stablecoins and BTC, and only partly for ETH. The FBI has since attributed the theft to TraderTraitor (31 October), but I could not open the FBI's own page, so that rests on two outlets quoting it.

## Sources

URL:         https://www.trmlabs.com/resources/blog/north-korea-steals-usd-6-36-billion-from-binance-in-the-largest-hack-in-history
Kind:        primary for TRM's tracing, TRM's per-chain and per-token figures, TRM's frozen tally and TRM's attribution. Secondary for everything Binance or issuers said (it relays them).
Establishes: firsthand: $6.36B traced out of Binance wallets on ten chains; TRM's high-confidence attribution; TRM's account of the EIP-7702 sweep and the "signing infrastructure" hypothesis; the freeze list by issuer with timestamps; the attacker's conversions during the freeze window. Repeats: Binance's $2.54B verified-frozen statement; Yi He's "about $200M" claim about Ripple.
Paraphrase:  About $6.36B moved out of Binance wallets on ten blockchains, most of it in about 20 minutes starting 20:05 UTC on 29 Oct, valued per transfer at the price at the moment taken. At prices when TRM wrote, the same assets are worth about $6.23B. A second wave at about 23:05 UTC hit Avalanche and Polygon. Ethereum about $3.79B, including 200,630 ETH and 185 other tokens, among them 1.875B USDT, 823M USDC and 88.5M RLUSD. Bitcoin 18,270 BTC (about $1.47B). Tron 612.7M USDT and 46.4M TRX (about $628M). XRP Ledger 233.46M XRP (about $296M). Solana 970,500 SOL (about $96M). Arbitrum, Optimism and Base about $39M combined. Avalanche about $28M. Polygon about $10M. TRM counts about $2.7B frozen: about $2.67B stablecoins (Tether about 1.77B USDT, Circle about 825M USDC, Ripple 40.5M RLUSD, World Liberty Financial 27.8M USD1) plus 8,426 ETH and 74.6M ARB (about $30M) moved by the Arbitrum Security Council. The attacker "converted freezable stablecoins into assets beyond any issuer's reach, at steep cost": about 325M USDT sold for about 122,300 ETH, 60M USDT supplied to Aave to borrow about 19,760 ETH, 300M USDT moved to JustLend, 48M RLUSD sold. TRM puts about $2.4B (more than 420,000 ETH and 18,270 BTC, "plus smaller amounts on other chains" per its FAQ) beyond issuer reach as of 00:30 UTC 30 Oct.
Locators:    Key takeaways (para 2, attribution and para 4, freezes); "How much was taken" (per-chain figures); "How the attack unfolded"; "Evidence points to Binance's signing infrastructure"; "Stablecoin freezes and conversion" (issuer list and conversions); FAQ "How much of the stolen crypto has been frozen?".
Quote:       "TRM attributes the attack to TraderTraitor, North Korea's elite hacking unit, based on robust on and off-chain intelligence. We make this judgment with high confidence." And on the breach: "In TRM's assessment, this points to a compromise of Binance's hot wallet signing infrastructure." And on the first hypothesis: "Early indicators on the Ethereum activity suggested the attacker had phished the authorizations. That explanation covers Ethereum and leaves the other chains unexplained."
Verified:    Fetched the page directly (HTTP 200). Figures are "as of October 30 at 00:30 UTC". The page header shows 29 October; page metadata (as returned by the fetch tool) gives datePublished 30 Oct 02:10 UTC and dateModified 30 Oct 19:41 UTC. Treat the figures as the 00:30 UTC 30 Oct snapshot.

URL:         https://www.elliptic.co/insights/binance-largest-hack-in-history/
Kind:        primary for Elliptic's tracing, its total, its asset and chain split, its frozen and unfreezable tallies, and its attribution reasoning. Secondary for the FBI's attribution and for Teng's video remarks. Elliptic is a commercial blockchain-analytics vendor whose product is screening for these funds, so it has a stake in the narrative of traceability.
Establishes: firsthand: $6.43B stolen; stablecoins $3.46B; $786M of stablecoins converted before the freezes; $2.85B frozen or seized (44%), 94% stablecoin; about $3.25B beyond issuer reach; chain-by-chain stolen and frozen amounts; the list of freezers. Repeats: Binance's laptop finding and its revision; the FBI attribution.
Paraphrase:  $6.43B stolen across 11 chains on 29 Oct (adds NEAR to TRM's ten), against Binance's "around $6.3B". The total excludes a further $169M that left Binance after withdrawals were paused, which Elliptic reads as Binance moving its own funds. Ethereum $3.80B across 186 tokens (including 1.9B USDT and 823M USDC), 18,270 BTC ($1.48B), 612.7M USDT on Tron. Four assets (USDT on Ethereum, BTC, USDC, USDT on Tron) are 74% of the theft. "Stablecoins made up $3.46 billion of the stolen funds." Tether froze the main Ethereum wallet 37 minutes after the USDT arrived, locking 1.18B USDT, then four more addresses within 17 minutes. Circle froze 823M USDC three minutes after that. Ripple, World Liberty Financial, Paxos and First Digital froze stablecoins. Tether froze tokenized gold. Binance froze WBETH, which it issues. Arbitrum's Security Council moved assets out of the attacker's reach, and on 31 Oct Optimism's governance "appears to have done the same", moving 44M OP (about $5M). Elliptic has verified $2.85B frozen or seized. "Stablecoins make up 94% of the frozen funds, almost entirely on Ethereum and Tron." "Nothing stolen on Bitcoin, the XRP Ledger, Solana or NEAR has been frozen, because native assets have no issuer that can freeze them." Before the freezes landed the attacker converted about $786M of stablecoins into ETH and TRX (434M USDT into 160,451 ETH at a 12% to 26% loss against market; 59.9M USDT as Aave collateral for 19,762 ETH, loan still open; 234M USDT into 638M TRX). At current prices the attacker controls about $3.25B that no issuer can freeze, across more than 800 addresses: about 584,000 ETH ($1.32B), 18,327 BTC ($1.42B), 233M XRP, with XRP, SOL and NEAR worth about $439M untouched since the theft.
Locators:    Key points; "How did the Binance attack unfold?"; "Following the stolen funds" (para on freezes, the 94% sentence, the $786M sentence, the $3.25B sentence); Charts 1 to 4 and captions; update log at top (last updated 1 Nov 08:00 UTC).
Quote:       "Before the freezes landed, the attacker converted around $786 million of stablecoins into ETH and TRX." And: "Arbitrum and Optimism are the only blockchains where everything stolen has been secured, in both cases by the network's own governance."
Verified:    Fetched the page directly (HTTP 200). Dated 30 Oct, updated through 1 Nov 08:00 UTC. Chart 3 is dated 05:50 UTC 1 Nov at current prices; Chart 2 freezes are at 04:20 UTC 31 Oct prices.

URL:         https://x.com/_RichardTeng/status/2116072080525656150
Kind:        primary for Binance's initial breach finding, its SAFU pledge and its first $6.3B and $3B statement. Posted by Richard Teng, whose X bio reads "Co-CEO | Formerly #Binance Head of Regional Markets, Former CEO of Financial Services Regulatory Authority". Posted 30 Oct 07:37 UTC.
Establishes: firsthand: Binance's wording of the laptop path and its hedge.
Paraphrase:  Binance's co-CEO says the incident "may have started with a compromised DevOps engineer's laptop", which gave an attacker access to a service container where they submitted unauthorized withdrawals, that the attacker did not simply use one engineer's permissions and it was not a single "one-click" action, that no wallet private-key leak had been found, and that a technical post-mortem will follow.
Locators:    Post body, paragraphs 3 to 5 and the "What you need to know" bullets.
Quote:       "Our initial investigation suggests this security incident may have started with a compromised DevOps engineer's laptop. That gave an attacker access to a service container, where they submitted unauthorized withdrawal transactions." "To be clear: the attacker did not simply use one engineer's permissions, and this was not a single 'one-click' action." "Estimated total impact: ~$6.3B, with ~$3B frozen on-chain so far, in coordination with our blockchain partners."
Verified:    Page returned HTTP 200 and the full post text was read from the page. The fetch tool returned 402 for the same URL, so it is login-gated for some clients.

URL:         https://x.com/binance/status/2116089661408108712
Kind:        primary (Binance's own account) for the revision of the breach finding. Posted 30 Oct 08:47 UTC.
Establishes: firsthand: Binance withdrew the single-laptop framing within about 70 minutes of Teng's post.
Paraphrase:  Binance says its initial investigation "suggested" a compromised laptop but a later one "has uncovered additional points of breach", describes a "complex attack", repeats the SAFU pledge, says outflows stopped when withdrawals were paused, and says it has frozen "around $3 billion thus far". It does not say what the additional points are.
Locators:    Post body, paragraphs 1, 3, 5.
Quote:       "Our initial investigation suggested that the security incident may have involved a compromised laptop, however our subsequent investigation has uncovered additional points of breach."
Verified:    HTTP 200, full text read.

URL:         https://www.binance.com/en/support/announcement/detail/c5a8729a97ac486d963784d96c5642d7
Kind:        primary (Binance announcement "Security Incident Update (2026-10-30)").
Establishes: firsthand: the same laptop finding, the $6.3B estimate, the "~$3 billion frozen on-chain so far", SAFU, the no-private-key-leak statement, in the company's announcement channel. Names no assets or chains frozen.
Paraphrase:  The announcement says the incident "may involve a compromised DevOps engineer's laptop, which allowed an attacker to gain access to a service container" and to "submit unauthorized withdrawal transactions". It states "The estimated total impact sits at around $6.3B", "with ~$3 billion frozen on-chain so far", "Binance will cover all losses from the SAFU fund and the company's funds", and "We have found no evidence of any wallet private key leak."
Locators:    Body, as extracted; listed as published 2026-10-30 02:23 and updated 2026-10-30 11:36 (update note clarifies deposits unaffected). The time zone is not shown in the extraction.
Verified:    A plain curl request returned a 405 bot-check page. The page was read through the fetch tool, which returned the text above as an extraction. The identical sentences appear verbatim in Teng's post, which I read directly, so the wording is double-checked. Gated to some clients, not dead.

URL:         https://x.com/binance/status/2115947325617299903 and https://x.com/binance/status/2115970069696217576
Kind:        primary (Binance) for its verified frozen totals and their growth. Posted 29 Oct 23:22 and 30 Oct 00:52.
Establishes: firsthand: Binance's total moved from $2.54B to "around $3 billion" in about 90 minutes.
Paraphrase:  First post: figures of $1.8B were circulating, "the current verified total frozen is $2.54 billion" and may rise. Second: "The current verified total frozen amount is around $3 billion."
Quote:       "For clarity, the current verified total frozen is $2.54 billion."
Verified:    HTTP 200, full text read.

URL:         https://x.com/binance/status/2116121748555153621
Kind:        primary (Binance) for the reserve and for the status of frozen assets. Posted 30 Oct 10:55 UTC.
Establishes: firsthand: Binance has reserved over $6.34B; $5B is held in the same tokens; frozen assets are not counted in that; recovery of frozen assets is still pending.
Paraphrase:  The $6.34B reserve "do[es] not include frozen or protected assets", "$3bn has been frozen", and "We are working with partners and law enforcement to recover the frozen assets."
Quote:       "These figures do not include frozen or protected assets, which remain subject to ongoing recovery and verification."
Verified:    HTTP 200, full text read.

URL:         https://x.com/paoloardoino/status/2115918000373346709
Kind:        primary for Tether's freeze (Paolo Ardoino's own account; the post does not give his title, and he is Tether's CEO per Tether's own April 2026 release below). Posted 29 Oct 21:25 UTC.
Establishes: firsthand: Tether's amount at that hour. Tether has no incident page on tether.io that I could find.
Paraphrase:  Tether froze more than 1.567B USDT related to a potential Binance exchange hack.
Quote:       "Tether froze more than 1.567B USDT related to a potential Binance exchange hack."
Verified:    HTTP 200, full text read. It is lower than TRM's later 1.77B because the freezes continued (see Contradictions).

URL:         https://x.com/jerallaire/status/2115916207463481846
Kind:        primary for Circle's freeze (Jeremy Allaire's own account; Circle's CEO per the cited press). Posted 29 Oct 21:18 UTC.
Establishes: firsthand: Circle froze "more than 800M USDC" and says it acted "in coordination with law enforcement". Names no agency or legal instrument.
Quote:       "In coordination with law enforcement, we have frozen more than 800M USDC associated with the incident and will continue supporting the investigation."
Verified:    HTTP 200, full text read. No circle.com announcement found.

URL:         https://x.com/cz_binance/status/2115915423174853077
Kind:        secondary for the freeze figures (Changpeng Zhao is a Binance founder and shareholder who says he no longer manages Binance.com, so he is not the issuer). Posted 29 Oct 21:15 UTC. It is the origin of the $971M and $823M figures in early coverage.
Quote:       "Appreciate the quick freeze from Tether (~$971m) and Circle (~$823m)."
Verified:    HTTP 200, full text read.

URL:         https://www.americanbanker.com/news/6b-binance-heist-provokes-stablecoin-freeze-dilemma
Kind:        secondary (Carter Pape, American Banker, 30 Oct 2026, 3:23 p.m. EDT). Useful for the Circle policy record and the Circle spokesperson's figure, which it quotes and I could not find elsewhere.
Establishes: reports (not firsthand): a Circle spokesperson said Circle "coordinated with law enforcement to freeze more than $1.1 billion in USDC associated with the incident", more than the $823M in the one wallet, without explaining the gap. Circle's policy acquired a third exception in May 2026, "certain urgent law enforcement requests pending a valid court order", acknowledged in a footnote to a 22 June court filing. In April 2026 Circle did not freeze about $230M of USDC stolen in the Drift exploit and said it freezes only when legally compelled.
Verified:    Read through the fetch tool. I did not open the court filing, so the policy-exception detail is the outlet's reading of it.

URL:         https://www.theblock.co/news/business/2026-04-13-circle-ceo-allaire-defends-decision-not-to-freeze-usdc-in-drift-exploit-citing-moral-quandary-397180
Kind:        secondary (The Block, 13 Apr 2026) reporting Allaire's remarks at a Seoul press conference.
Establishes: reports: about $280M stolen in the Drift exploit, about $230M USDC moved Solana to Ethereum through Circle's CCTP, Circle did not freeze it. Allaire: Circle "follows the rule of law, and we are able to undertake actions such as freezing a wallet" when directed by courts or law enforcement.
Verified:    Read through the fetch tool. The Drift loss figure differs from Elliptic's $286M headline for the same event.

URL:         https://eth.blockscout.com/address/0xdAC17F958D2ee523a2206206994597C13D831ec7?tab=contract
Kind:        primary for what the Tether USDT contract on Ethereum can do (verified source of `TetherToken`, compiler v0.4.18, verified 2019-04-18 per Blockscout).
Establishes: firsthand: the contract carries an owner-only blacklist and a function that burns a blacklisted balance.
Paraphrase:  `mapping (address => bool) public isBlackListed`; `function addBlackList (address _evilUser) public onlyOwner`; `function removeBlackList (address _clearedUser) public onlyOwner`; `function destroyBlackFunds (address _blackListedUser) public onlyOwner`, which requires the address to be blacklisted, sets its balance to zero and reduces `_totalSupply` by that amount. Transfer paths contain `require(!isBlackListed[...])` checks (read in the source: `require(!isBlackListed[msg.sender])` and `require(!isBlackListed[_from])`). The same file also has `issue`, `redeem` and `pause`, all `onlyOwner`.
Locators:    Source tab, contract `BlackList` and `TetherToken`.
Verified:    Blockscout page HTTP 200, and I read the source through Blockscout's API for the same address. The Etherscan page for the same address (`https://etherscan.io/address/0xdAC17F958D2ee523a2206206994597C13D831ec7#code`) returned 403, so it is gated, not dead. I did not read the Tron USDT contract, where 612.7M of the stolen USDT sat.

URL:         https://github.com/circlefin/stablecoin-evm/blob/master/contracts/v1/Blacklistable.sol
Kind:        primary for Circle's USDC contract design (Circle's own repository for the stablecoin contracts).
Establishes: firsthand: a `blacklist(address)` function restricted to a designated blacklister, and a modifier that reverts transfers involving a blacklisted address.
Paraphrase:  `function blacklist(address _account) external onlyBlacklister`; `function unBlacklist(address _account) external onlyBlacklister`; `function isBlacklisted(address _account) external view returns (bool)`; modifier `notBlacklisted(address _account)` reverts with "Blacklistable: account is blacklisted". In `FiatTokenV1.sol` the modifier is applied to the sender and recipient in `transfer`, `transferFrom`, `approve` and related paths. The repository README says the contract "can blacklist certain addresses which will prevent those addresses from transferring or receiving tokens."
Verified:    The GitHub blob page returned 403 to curl and was read through the fetch tool, which confirmed the signatures. I read the raw file separately. I also confirmed the deployed USDC proxy on Ethereum (0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48) points to implementation `FiatTokenV2_2` (0x43506849D7C04F9138D1A2050bbF3A0c054402dd), whose verified source on Blockscout contains `blacklist(address) onlyBlacklister` and `notBlacklisted`.

URL:         https://www.circle.com/legal/usdc-terms
Kind:        primary (Circle's own terms; last updated 15 Oct 2026 per page).
Establishes: firsthand: Circle reserves the right to block addresses and freeze, and says it may be legally required to.
Quote:       "Circle reserves the right to “block” certain USDC addresses and, if such addresses are Circle custodied addresses, freeze associated USDC (temporarily or permanently)". Section 13, "Blocked Addresses & Forfeited Funds".
Verified:    Read through the fetch tool.

URL:         https://tether.io/news/tether-supports-freeze-of-more-than-344-million-in-usdt-in-coordination-with-ofac-and-u-s-law-enforcement/
Kind:        primary (Tether, 23 April 2026). The prior documented freeze.
Establishes: firsthand: Tether froze $344M USDT across two addresses in coordination with OFAC and US law enforcement. It names no chain or address.
Quote:       "The freeze was executed after the addresses were identified, preventing further movement of funds."
Verified:    Read through the fetch tool.

URL:         https://tether.io/news/tether-recognized-for-assisting-the-united-states-secret-service-in-23m-freeze-related-to-transfers-on-sanctioned-exchange-garantex/
Kind:        primary (Tether, 7 March 2025). A second prior freeze.
Establishes: firsthand: $23M frozen in assistance to the US Secret Service, linked to the sanctioned exchange Garantex; Tether says it "enforces a strict wallet-freezing policy".
Verified:    Read through the fetch tool.

URL:         https://www.ic3.gov/PSA/2025/PSA250226
Kind:        primary for the Bybit figure and the FBI's 2025 attribution (FBI, Internet Crime Complaint Center, 26 Feb 2025, "North Korea Responsible for $1.5 Billion Bybit Hack").
Establishes: firsthand: "approximately $1.5 billion USD in virtual assets" stolen from Bybit; the FBI calls the activity "TraderTraitor".
Quote:       "North Korea responsible for the theft of approximately $1.5 billion USD in virtual assets from cryptocurrency exchange, Bybit" (as returned by the fetch tool; the page title is "North Korea Responsible for $1.5 Billion Bybit Hack").
Verified:    Read through the fetch tool. The theft date (21 Feb 2025) comes from TRM's Bybit post, not this page.

URL:         https://blockscholes.com/research/bybit-eth-hack
Kind:        secondary (Block Scholes, a crypto research firm; updated 22 Feb 2025). It reports Bybit's stolen-asset list from on-chain data.
Establishes: reports: the Bybit haul was 401,346.7688 ETH, 90,375.5479 stETH, 8,000 mETH and 15,000 cmETH, about $1.46B, with no stablecoin; Tether froze 181K USDT (Ardoino's announcement), and no freeze of the stolen ETH or staking derivatives.
Verified:    Read through the fetch tool. Bybit's own announcement was not opened (see Limits).

URL:         https://decrypt.co/315593/bybit-ceo-two-thirds-of-funds-from-lazarus-group-hack-still-traceable
Kind:        secondary (Decrypt, Vismaya V, 21 Apr 2025) quoting Bybit CEO Ben Zhou's post, which owns the number.
Establishes: reports: as of 21 Apr 2025, "68.57% remain traceable, 27.59% have gone dark, 3.84% have been frozen" of roughly 500,000 ETH. Earlier snapshots in other coverage: 3% (4 Mar 2025), 3.54% (20 Mar 2025). I did not open Zhou's posts.
Verified:    Read through the fetch tool.

URL:         https://www.theblock.co/amp/post/342840/meth-protocol-announces-43-million-recovery-from-bybit-hack-while-tether-freezes-181000
Kind:        secondary (The Block, 22 Feb 2025).
Establishes: reports: Tether froze 181,000 USDT linked to Bybit ("Might not be much but it's honest work", Ardoino). mETH Protocol recovered 15,000 cmETH (about $43M) because an 8-hour withdrawal delay let its team pause a contract. This is a documented case of a non-issuer, protocol-level stop on a non-stablecoin token.
Verified:    Read through the fetch tool.

URL:         https://x.com/jony_levin/status/2116020833227587637
Kind:        primary for Chainalysis' stated assessment (Jonathan Levin's own account; coverage calls him Chainalysis's co-founder and CEO, which I did not verify from his bio). Posted 30 Oct 04:14 UTC.
Establishes: firsthand: a second analytics firm's attribution and figures, independent of TRM in method.
Quote:       "We assess @binance hack for $6.4B was likely done by DPRK group TraderTraitor due to links to previous hack. Industry partners have already frozen ~$3B and we @chainalysis continue to follow all of the funds"
Verified:    HTTP 200, full text read. Chainalysis' own blog post was not found; its $5.912B figure comes from Cointelegraph's live blog (secondary).

URL:         https://cointelegraph.com/news/live-updates-binance-63b-hack-linked-to-north-koreas-tradertraitor
Kind:        secondary (Cointelegraph live blog). Used as a timeline and as an index to primary posts, never for a number a primary owns.
Establishes: reports: timeline of Binance, Aave, World Liberty and Chainalysis posts; Arkham about $5.84B (wallet holdings, not a confirmed estimate); the list of frozen tokens USDT, USDC, RLUSD, USD1, XUSD, USDT0, WBETH, XAUT, PAXG, USDP and ARB.
Verified:    Read through the fetch tool.

URL:         https://www.bleepingcomputer.com/news/security/fbi-links-63-billion-binance-crypto-heist-to-north-korean-hackers/
Kind:        secondary for the FBI's attribution (BleepingComputer, 1 Nov 2026). The FBI's own page is the primary and I could not open it.
Establishes: reports: the FBI says North Korea "was responsible for the theft of more than $6 billion USD in virtual assets from cryptocurrency exchange Binance" on or about 29 Oct 2026, calls the actor TraderTraitor, has observed conversion "primarily into Ethereum (ETH)", and published 628 addresses (608 Ethereum, 19 Bitcoin, one Solana) with a request to block them. The FBI page does not give $6.3B or $6.36B. Elliptic independently reports the FBI attribution as dated 31 Oct.
Verified:    Read through the fetch tool. The FBI page `https://www.fbi.gov/investigate/cyber/alerts/2026/north-korea-responsible-for-6-billion-binance-attack` returned 403 (a Cloudflare "Just a moment" challenge) to the fetch tool and to curl with browser headers. Gated, not dead. I did not try further routes.

URL:         https://coindesk.com/markets/2026/11/01/binance-opens-crypto-withdrawals-in-phases-starting-with-bitcoin-following-usd6-3-billion-hack
Kind:        secondary (CoinDesk, 1 Nov 2026) for Binance's coverage and withdrawal status.
Establishes: reports: withdrawals began reopening 1 Nov 06:00 to 09:00 UTC; Binance says it has covered about 95% of the impacted amount; about $3B is immobilized; the article reports no frozen funds recovered or returned.
Verified:    Read through the fetch tool.

## Contradictions

1. **Total stolen.** Binance: "estimated total impact" about $6.3B (impact, not an audited loss). TRM: about $6.36B at theft-time prices, about $6.23B at its later prices. Elliptic: $6.43B at theft-time prices, $6.10B at 1 Nov prices, excluding $169M it reads as Binance's own transfers. Chainalysis: $5.912B "at the time of theft" (Cointelegraph), $6.4B (Levin). Arkham about $5.84B to $6.01B (secondary, not opened). The FBI says "more than $6 billion" (quoted by BleepingComputer). The spread is mostly valuation basis and scope (which transfers count). Give the range and its basis, not one number.
2. **Chains.** TRM: ten (Ethereum, Bitcoin, Tron, XRP Ledger, Solana, Arbitrum, Optimism, Base, Avalanche, Polygon). Elliptic: eleven (adds NEAR). Neither source lists BNB Chain or BNB.
3. **Frozen total.** Binance $2.54B (29 Oct 23:22) then "around $3 billion" (30 Oct 00:52). TRM about $2.7B (00:30 on 30 Oct). Chainalysis/Levin about $3B. Elliptic $2.85B (1 Nov 05:50; at current prices). Binance's method is not described, and it is the highest figure. Say "about $2.7B to $3B" and name the owners.
4. **Tether's amount.** CZ about $971M (29 Oct 21:15); Ardoino more than 1.567B USDT (21:25); TRM about 1.77B USDT (00:30 on 30 Oct); Elliptic's chart shows Tether $1.82B (1 Nov, which may include tokenized gold, which the text says Tether also froze). These are successive snapshots of a rising total, not rival claims, but only TRM and Elliptic give a reasoned account of what each includes.
5. **Circle's amount.** Allaire more than 800M USDC; TRM about 825M (823M main wallet plus 1.56M); Elliptic 823M and a chart figure of $825M. A Circle spokesperson, quoted by American Banker, said more than $1.1B. No other source supports $1.1B and neither the outlet nor I could reconcile it. Use $823M to $825M from the on-chain owners and mention the $1.1B as an unreconciled company statement, or leave it out.
6. **What remains beyond reach.** TRM: about $2.4B (420,000+ ETH, 18,270 BTC; 30 Oct). Elliptic: about $3.25B (584,000 ETH, 18,327 BTC, plus $502M of XRP, TRX, SOL, NEAR and other; 1 Nov). Elliptic's figure includes ETH created by converting TRX and tokens after TRM's snapshot, and counts the XRP and SOL that TRM files under "smaller amounts". The two do not conflict on direction. Do not state one number without its date and owner.
7. **Breach path.** Binance's first finding (laptop to container) was revised by Binance itself 70 minutes after Teng's post ("additional points of breach"). TRM's reading is a compromise of Binance's signing infrastructure across chains. Elliptic reports (relaying Teng's video update, which I did not watch) that the attacker used a self-destruct mechanism and that EIP-7702 delegation "did not pass through our normal approval controls". Binance has not said what the additional points are. The mechanism diagram the commission wants (laptop to container to withdrawals) is Binance's initial finding only.
8. **"Native assets have no switch" versus governance freezes.** Elliptic: Arbitrum and Optimism are the only chains where everything stolen was secured, by the network's governance (Arbitrum Security Council 8,426 ETH and 74.6M ARB, about $30M; Optimism 44M OP, about $5M). Elliptic's chart 2 shows Arbitrum $31M of $32M frozen and Optimism $5M of $5M. Binance froze its own WBETH. Paxos and Tether froze tokenized gold (Cointelegraph list names PAXG, XAUT). So the dividing line in the evidence is "has an issuer or administrator who can act", which covers stablecoins and some other tokens, and which BTC, ETH on Ethereum, XRP, SOL and NEAR do not have. This is small in dollars (about $36M of ETH, ARB and OP) and does not change the main split.
9. **"The freeze recovered close to all it ever could".** Elliptic's own numbers cut against this. Stablecoins stolen $3.46B. Frozen stablecoin about $2.68B (derived below). About $786M converted before the freezes. The attacker's conversion race lost value (12% to 26% discounts) but moved that value beyond reach. The freezes did capture almost everything that had not already been swapped (derived: $3.46B minus $0.786B is about $2.67B, against about $2.68B frozen, so the figures reconcile within rounding). So the claim holds only as "the issuers froze nearly all the stablecoin still in place when they acted", not as "froze all the freezable value".
10. **"Recovered ~$3B".** Binance says "frozen", and says it is working "to recover the frozen assets". CoinDesk (1 Nov) reports nothing returned. Binance's 95% coverage figure is Binance buying replacement tokens with its own funds, not frozen funds coming back.
11. **BNB.** The commission lists "Binance's own BNB on most paths" among the unfreezable assets. Neither TRM nor Elliptic lists any BNB or BNB Chain theft. Drop BNB from the haul.
12. **Attribution.** TRM: high confidence, TraderTraitor. Chainalysis (Levin): "likely". Elliptic: "likely" before the FBI, then confirmed. FBI: attribution to North Korea (31 Oct, per Elliptic; BleepingComputer dates it "Saturday", 31 Oct). Binance: "Our investigation has not attributed responsibility to any individual" (Teng, Oct 30), and has not confirmed the attribution (IBTimes, as read, reports no Binance response). North Korea has previously denied such thefts and did not respond to Reuters in this case (IBTimes, relaying Reuters). A search summary attributed a Trump quote "We don't know if it's North Korea" to coverage. I could not find it in the cited article, so it is not recorded as fact. The FBI's alert names no individuals and no charges, and TraderTraitor is a group label for an activity cluster, not an indicted defendant. The earlier Bybit attribution does not prove the same individuals were responsible here (IBTimes).

## Numbers

Figure: about $6.3B "estimated total impact"
Owner:  Binance (announcement and Teng's post, 30 Oct)
Scope:  Binance's own estimate; method not stated; not an audited loss.

Figure: about $6.36B stolen across ten chains (about $6.23B at TRM's later prices)
Owner:  TRM Labs
Scope:  transfers from Binance-attributed wallets to attacker addresses, valued at transfer time; snapshot 30 Oct 00:30 UTC.

Figure: $6.43B stolen across eleven chains ($6.10B at 1 Nov prices); excludes $169M
Owner:  Elliptic
Scope:  theft-time prices, cross-checked with block explorers and DefiLlama; 11 chains; updated 1 Nov.

Figure: most of the haul left in about 20 minutes starting 20:05 UTC on 29 Oct; a second wave about 23:05 UTC (Avalanche, Polygon). Elliptic: $2.53B of Ethereum losses in one transaction at 20:24 UTC.
Owner:  TRM Labs (timing); Elliptic (single transaction)
Scope:  29 Oct 2026.

Figure: stolen by chain (theft-time) with frozen amount, Elliptic chart 2, frozen at 04:20 UTC 31 Oct prices: Ethereum $3,798M stolen, $2,417M frozen (64%); Bitcoin $1,476M, none; Tron $627M, $379M (60%); XRP Ledger $300M, none; Solana $97M, none; NEAR $54M, none; Arbitrum $32M, $31M (96%); Avalanche $28M, $8M (30%); Polygon $10M, $6M (60%); Optimism $5M, $5M (all); Base $3M, none.
Owner:  Elliptic
Scope:  chain totals, not asset totals. Ethereum's $3.8B contains stablecoins (1.9B USDT and 823M USDC per Elliptic; 1.875B USDT, 823M USDC, 88.5M RLUSD per TRM). It must not be labelled "ETH". TRM's chain figures (Ethereum $3.79B, Bitcoin $1.47B, Tron $628M, XRPL $296M, Solana $96M, Arbitrum/Optimism/Base $39M combined, Avalanche $28M, Polygon $10M) agree within rounding.

Figure: stablecoins stolen, $3.46B (about 54% of $6.43B)
Owner:  Elliptic ("Stablecoins made up $3.46 billion of the stolen funds"). TRM's token counts are consistent: 1.875B + 612.7M USDT, 823M USDC, 88.5M RLUSD sum to about $3.40B before USD1 and other stablecoins (my addition).
Scope:  theft-time.

Figure: BTC stolen, 18,270 BTC ($1.47B to $1.48B)
Owner:  TRM Labs; Elliptic
Scope:  theft-time. Elliptic counts 18,327 BTC held on 1 Nov (different count, not explained).

Figure: ETH stolen on Ethereum, 200,630 ETH (TRM); USD value at theft not given by either owner. Elliptic does not give a stolen-ETH total.
Owner:  TRM Labs
Scope:  Ethereum chain only; ETH on Arbitrum, Optimism and Base is not itemized. The ETH-to-USD conversion at theft is the writer's to avoid or to derive with a stated price; TRM states ETH traded "around USD 2,300 to 2,350" in the freeze window.

Figure: frozen, about $2.7B (about $2.67B stablecoins plus about $30M ETH and ARB)
Owner:  TRM Labs
Scope:  30 Oct 00:30 UTC. By issuer: Tether about 1.77B USDT; Circle about 825M USDC; Ripple 40.5M RLUSD (of 88.5M stolen); World Liberty Financial 27.8M USD1; Arbitrum Security Council 8,426 ETH and 74.6M ARB. TRM confirmed Ripple's 40.5M on-chain and notes Yi He's claim that Ripple helped stop about $200M from moving.

Figure: frozen or seized, $2.85B (44% of $6.43B); 94% stablecoin
Owner:  Elliptic
Scope:  1 Nov 05:50 UTC at current prices; chart 3 split: Tether $1.82bn, Circle $825m, "Binance, Ripple, Arbitrum, Optimism and others" $200m.

Figure: frozen, "around $3 billion", "verified"
Owner:  Binance (30 Oct 00:52 UTC; repeated 10:55 and in Teng's post)
Scope:  Binance's verified count; asset split and method not given. Binance's $6.34B reserve post says it does not count frozen or protected assets.

Figure: derived split (my arithmetic from Elliptic's figures, to be treated as derived): frozen stablecoin about $2.68B (94% of $2.85B), which is about 77% of the $3.46B stolen in stablecoins. Non-stablecoin stolen about $2.97B ($6.43B minus $3.46B), of which about $0.17B was frozen (6% of $2.85B), about 6%. The 94% is rounded, so these carry roughly plus or minus $0.03B.
Owner:  derived from Elliptic; the 94% and $3.46B are Elliptic's.
Scope:  theft-time stolen, 1 Nov frozen at current prices, so the ratios mix two price dates.

Figure: converted before the freezes, about $786M of stablecoins into ETH and TRX
Owner:  Elliptic. TRM's own list (about 325M USDT for about 122,300 ETH, 60M USDT to borrow about 19,760 ETH, 300M USDT to JustLend, 48M RLUSD sold) is a different cut and does not total to $786M on its face.
Scope:  29 to 30 Oct, before freezes landed at each venue.

Figure: beyond issuer reach, about $2.4B (TRM, 30 Oct 00:30) and about $3.25B (Elliptic, 1 Nov 05:50); Elliptic split: BTC $1.42bn, ETH $1.32bn, Other $502m (XRP, TRX, SOL, NEAR and other tokens)
Owner:  TRM Labs; Elliptic
Scope:  current prices on each date. Elliptic's frozen $2.85B plus beyond-reach $3.25B equals its $6.10B current value of the haul.

Figure: freeze speed, Tether froze 971.1M USDT at 21:01 UTC, 37 minutes after the 20:24 sweep; Circle froze 823M USDC at 21:04; Ripple 22:01; World Liberty Financial 22:10; Arbitrum Security Council 00:08 (30 Oct)
Owner:  TRM Labs (timestamps); Elliptic gives the same 37 minutes.
Scope:  29 to 30 Oct.

Figure: Bybit 2025 theft, "approximately $1.5 billion USD in virtual assets" (FBI); $1.46B (Elliptic, Block Scholes); about 401,347 ETH plus 90,376 stETH, 8,000 mETH and 15,000 cmETH
Owner:  FBI (the $1.5B and attribution); on-chain composition from Block Scholes (secondary)
Scope:  21 Feb 2025. Binance 2026 is about four times larger (TRM) or "more than four times" (Elliptic).

Figure: Bybit frozen share, 3% (4 Mar 2025), 3.54% (20 Mar), 3.84% (21 Apr 2025)
Owner:  Bybit CEO Ben Zhou's posts (read only through Decrypt and The Defiant summaries)
Scope:  share of about 500,000 ETH; Tether's 181,000 USDT freeze is a separate, small item.

Figure: Tether prior freezes, $344M (23 Apr 2026, OFAC and US law enforcement) and $23M (7 Mar 2025, US Secret Service, Garantex)
Owner:  Tether
Scope:  two addresses (the $344M freeze); chain not stated.

Figure: FBI-published address list, 628 addresses (608 Ethereum, 19 Bitcoin, one Solana)
Owner:  FBI (via BleepingComputer; not opened)
Scope:  alert of 31 Oct to 1 Nov.

## Limits

- The FBI's own alert could not be opened (403 challenge). The attribution rests on BleepingComputer and Elliptic quoting it. A writer who cites the FBI should have the editor or the owner open the page, or cite those two as reporting the FBI.
- Binance has no per-asset breakdown of what it froze, and its $3B is higher than the two analysts' tallies at similar times (TRM $2.7B, Elliptic $2.85B). The per-asset split of the frozen amount rests on Elliptic (94% stablecoin; chart 3: Tether $1.82bn, Circle $825m, others $200m) and TRM's issuer list. The $0.17B non-stablecoin remainder is not itemized by either owner beyond a list of names (WBETH, tokenized gold, ARB, ETH on Arbitrum, OP).
- The USD value of ETH stolen is not stated by either owner. Only the count (200,630 ETH on Ethereum, per TRM) is firm. The stolen composition is firm for stablecoins ($3.46B), Bitcoin and XRP, and thin for ETH, so a "stolen by asset" chart needs the writer to state the ETH price used or to show chains and tokens separately.
- Two different ETH balances (420,000 and 584,000) and two beyond-reach totals ($2.4B and $3.25B) sit in the record. Neither owner reconciles them. The difference is explained by timing and by conversion after TRM's snapshot, which is my reading and not either owner's sentence.
- The cause is Binance's initial finding, revised. Binance has not published a post-mortem, and no source says what the additional points of breach are. The laptop-to-container path is a hypothesis Binance has already partly withdrawn.
- No frozen funds are reported returned. Whether Tether and Circle will release frozen balances to Binance, and on what legal process, is not stated in any source I read. The piece cannot say "recovered".
- Whether Circle's freeze was a policy decision or a legal one is open: Allaire says "in coordination with law enforcement", names no agency or order, and a Circle spokesperson's $1.1B figure is unreconciled. American Banker's account of Circle's May 2026 policy exception rests on a court-filing footnote I did not open.
- I read the Ethereum USDT and USDC contracts and Circle's reference code. I did not read the Tron USDT contract, though 612.7M of the stolen USDT was on Tron and Tether froze 378.7M of it (TRM) or $379M (Elliptic chart 2). I did not verify that Bybit-era freeze functions were used the same way. The statement that Bitcoin, XRP and Solana have no equivalent function rests on Elliptic's sentence ("no issuer that can freeze them") and not on protocol documentation I opened.
- Bybit's own announcement and Zhou's posts were not opened. The $1.5B figure is the FBI's, and the frozen share of 3% to 3.84% is Zhou's, read through Decrypt.
- Chainalysis' own blog post, Arkham's page and the Reuters story were not opened. Their figures appear only as secondary reporting.
- The title "Co-CEO" is taken from Teng's X bio as returned on his post page. Yi He's title ("co-CEO") comes from TRM's and Cointelegraph's text, and I did not see her bio.
- Everything here moves. Elliptic's page says it will be followed by a new laundering article, and the unfreezable total changes each time the attacker converts.

## Source assets

Asset: Elliptic chart 3, "$2.85 billion of the stolen funds has been frozen or seized", a two-part bar at 05:50 UTC, 1 Nov 2026, current prices. Left bar "Frozen $2.85bn" split Tether $1.82bn, Circle $825m, "Binance, Ripple, Arbitrum, Optimism and others $200m". Right bar "Beyond issuers' reach $3.25bn" split BTC $1.42bn, ETH $1.32bn, Other $502m. Subtitle: "Current value of stolen funds: $6.10bn ($6.43bn when stolen)". Footnote: "Other includes XRP, TRX, SOL, NEAR and other tokens." Lives in "Following the stolen funds" on the Elliptic article. Image file: https://d13k95gd4bp92z.cloudfront.net/images/binance-hack-chart-3-frozen-vs-beyond-reach_0550utc-1nov.png
Shows:  the whole current haul split into what issuers froze and what they cannot reach, by holder asset. It is the single closest visual to the commission's finding.
Crop:   must keep the headline, the $6.10bn current and $6.43bn theft-time subtitle, both bar labels, the date and price-basis footnote, and the Elliptic credit. It may omit nothing from the bars. It does not split the frozen side by asset type beyond issuer, so a caption must not claim a stablecoin share from the image alone.

Asset: Elliptic chart 2, "82% of the stolen funds were taken on Ethereum and Bitcoin", a bar chart of stolen amount by chain with a frozen overlay and a table (Ethereum $3,798m stolen and $2,417m (64%) frozen; Bitcoin $1,476m none; Tron $627m and $379m (60%); XRP Ledger $300m none; Solana $97m none; NEAR $54m none; Arbitrum $32m and $31m (96%); Avalanche $28m and $8m (30%); Polygon $10m and $6m (60%); Optimism $5m all; Base $3m none). Footnote: "Stolen at time of theft; frozen at 04:20 UTC, 31 Oct 2026 prices." Image file: https://d13k95gd4bp92z.cloudfront.net/images/binance-hack-chart-2-stolen-by-blockchain_0420utc.png
Shows:  that freezing happened only on chains where tokens with issuers were present, with none on Bitcoin, the XRP Ledger, Solana or NEAR.
Crop:   must keep the title, the stolen and frozen columns, the "None" entries and the price-basis footnote. A caption must say this is by chain, not by asset (Ethereum includes stablecoins). The frozen column mixes prices from a different date than the stolen column.

Asset: TRM "overview of the October 29, 2026 Binance hack" graphic, a transaction graph with one Binance node (BINANCE (BINANCE.COM), Exchange) and eleven red "Binance Exploiter October 2026" nodes labelled "Hacked or Exploited Funds", with edge labels showing amounts (for example $627.5M, $1.49B, $3.74B, $10.3M as legible in the image). Lives in "What happened" and "How much was taken" on the TRM post. Image file: https://cdn.prod.website-files.com/6082dc5b670562507b3587b4/6ae3fcce33b01dca39613694_834d44b2.jpeg ; a second graph image in the same post (https://cdn.prod.website-files.com/6082dc5b670562507b3587b4/6ae3fcce33b01dca39613691_2abacf22.png) shows a large fan of about 50 parallel arcs between two nodes with side branches.
Shows:  the single-source-to-many-attacker-addresses fan-out; the second graph appears to show the 50 pre-signed EIP-7702 authorizations (my reading, not labelled in the image or caption).
Crop:   keep the TRM mark and the "© TRM Labs" line. The edge labels are small, so a crop of the first graph that keeps them needs the full width. These are TRM's images and need a stated licence before reuse. A diagram the paper draws itself from TRM's text may serve better.

Asset: the posts by Tether's CEO (https://x.com/paoloardoino/status/2115918000373346709) and Circle's CEO (https://x.com/jerallaire/status/2115916207463481846), and Binance's three frozen-total posts.
Shows:  each issuer's own wording at the time, with timestamps.
Crop:   keep the account name, the full text and the timestamp. Screenshot reuse of X posts needs the editor's decision, so quoting the exact sentence is the alternative.

Asset: the Tether `TetherToken` source on Blockscout, the functions `addBlackList`, `removeBlackList`, `destroyBlackFunds` and the `isBlackListed` mapping; and Circle's `Blacklistable.sol` (`blacklist`, `onlyBlacklister`, `notBlacklisted`).
Shows:  the freeze capability as eight to fifteen lines of code, including that Tether's function can also burn the balance. This is the mechanism that does not depend on this incident's numbers.
Crop:   keep the function signatures and modifiers, the contract name and the address. Omit the rest of the file.

Asset: FBI alert (address list of 628 addresses, 608 Ethereum, 19 Bitcoin, one Solana).
Shows:  the official block list.
Crop:   not inspected, because the page was gated.

## Discarded

https://www.wealthprofessional.ca/news/industry-news/binance-hack-63-billion-stolen-in-largest-crypto-heist-in-history/393908: a search summary said it claims the attacker still holds specific ETH and BTC balances. I did not open it, and the figures come from TRM and Elliptic, which own the tracing.
https://ambcrypto.com/binance-investigates-security-reports-as-tether-says-it-froze-over-1-567b-usdt/: read; it only paraphrases Ardoino's post (which I read directly) and contains CZ's figures without a link, so it adds nothing a primary does not.
https://cryptobriefing.com/circle-freezes-usdc-binance-breach/: read; it repeats Allaire's post (read directly) and says Ripple froze "about $200 million in RLUSD", which TRM contradicts (TRM confirms 40.5M RLUSD frozen and attributes the $200M to Yi He's claim about funds stopped from moving).
https://www.ibtimes.co.uk/fbi-binance-theft-tradertraitor-north-korea-1829324: read for caveats only; it does not contain the Trump quote a search summary attributed to coverage, and it gives no frozen or composition figure. Used only for North Korea's prior denials and Binance's non-response.
https://thehackernews.com/2026/11/fbi-links-north-koreas-tradertraitor-to.html: read; its "82% on Ethereum and Bitcoin" is Elliptic's chart 2 headline, its $2.85B is Elliptic's, and it quotes the FBI only partially, so it is a retelling of sources I hold directly.
https://www.nbcnews.com/business/markets/binance-hack-tether-circle-stablecoins-rcna606445: read; dated 29 Oct, it predates the frozen figures that matter, and it does not explain why BTC and ETH cannot be frozen.
https://www.bankless.com/read/binance-just-suffered-the-biggest-hack-in-crypto-history-what-now.md: read for links only; its summary-level statements ("no issuer that can freeze them") duplicate Elliptic's.
https://decrypt.co/382203/binance-finds-additional-points-of-breach-in-6-3b-hack: read; it relays the Binance posts I read directly.
https://www.mexc.com/ and other aggregator pages returned by search for Circle's freeze policy: not opened; syndicated copies of The Block and Crypto Briefing.
Search snippets on a "Circle bridged USDC cannot be frozen" term and a Korean wikidocs page on Tether: not opened or not reliable (the wikidocs summary was flagged as describing the upgrade mechanism wrongly), so not used.
https://www.trmlabs.com/resources/blog/the-bybit-hack-following-north-koreas-largest-exploit: read; says only "approximately USD 1.5 billion in Ethereum tokens", gives no freeze figure and no composition beyond that, so it is not used for composition or freezes.
