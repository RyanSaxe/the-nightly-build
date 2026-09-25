# Editorial review: technical/multicancer-blood-test-metrics (editor/01)

## Correct
The thesis is that sensitivity, specificity, positive predictive value, origin accuracy, diagnostic burden, and clinical utility answer different questions because each uses its own population, assay version, endpoint, and denominator. Four claims support it. First, FDA's bridged NHS-Galleri estimates of 31.6% sensitivity and 99.74% specificity coexist because they condition on cancer and non-cancer groups, while PPV also depends on prevalence. Second, a positive result begins a sequence from signal detection through origin prediction and workup to diagnostic resolution. Third, the submitted Galleri assay has retrospective bridged effectiveness estimates, while the observed prospective workups followed the earlier MCED-V2 assay. Fourth, detection performance does not establish downstaging or mortality benefit.

I recomputed the 10,000-person examples. At 0.5% prevalence, the expected counts are 15.8 true positives, 34.2 false negatives, 25.87 false positives, and 9,924.13 true negatives, giving 37.9169% PPV. At 2.0% prevalence, 63.2 true positives and 25.48 false positives give 71.2675% PPV. The printed rounding is correct.

I also checked each ratio used to carry the argument: 238/259 is 91.9% origin accuracy; 173/287 is 60.3% PPV; 213/290 is 73.4% with an invasive procedure; 213/35,878 is 0.6% of enrolled participants; 35/92 is 38.0% in the first PATHFINDER cohort; and the procedure counts are 27/33 and 17/57 in its evaluated true- and false-positive groups. The annual-round PPV, episode-sensitivity, stage-sensitivity, and CCGA figures match their owning reports and retain the correct assay and study design.

The population-level PATHFINDER 2 burden sentence was the break. “Everyone screened” did not expose the 35,878-person denominator and sat next to a 32,007-person analysis set. I replaced it with the enrollment count. I also recast the randomized endpoint sentence so it states the prespecified comparison and the absence of a significant reduction without a rhetorical question. The headline, date, proposed population, advisory-panel status, and vote counts agree with the FDA and sponsor records. The source kinds correctly distinguish FDA, sponsor, and study authors from Reuters and the independent patient-safety comment.

## Reads well
I replaced “pivotal percentages” because it added weight without identifying anything. I split the dek's semicolon and named specificity and sensitivity, making the first distinction visible before the article begins. The randomized-trial question went because it performed a transition that the endpoint can state directly. The closing slogan “The denominator sets the inference” went because the ledger's four fields support a more exact final sentence.

The draft did not borrow the voice guide's quoted clauses or copy the commission's phrasing. Its opener also avoids the previous Technical article's antithesis, container framing, repeated code blocks, and command close. The short verdicts after calculations work because the preceding counts earn them.

## The experience
The equation, stat strip, four-step sequence, and closing ledger each do a different job. No table or chart would make the fixed-cohort calculation faster to read than the existing equation and three output values. The article's weight now moves from one calculation to observed workups, then to the assay-version split and the randomized endpoint.

The piece gives the reader a reusable audit: attach every performance claim to its population, assay version, endpoint, and denominator, then keep assay detection separate from what happened after a returned result. That survives comparison with the writer's original-work sentence and is not available from any one source alone.

## Edits
- Named specificity and sensitivity in the dek and replaced the semicolon with a period.
- Replaced “pivotal percentages” with “two percentages.”
- Made 35,878 enrolled participants the explicit denominator for the 0.6% PATHFINDER 2 burden figure.
- Split the population-burden comparison into shorter declarative sentences.
- Rewrote the randomized-trial passage around its prespecified endpoint and reported result.
- Replaced the slogan-like final sentence with the four fields that bound a reported percentage.
- Ran the exact proof command; it returned `BLOCK: 0`, `WARN: 0`, and `PUBLISHABLE`.

## Decision
approve — the claims, calculations, source classifications, assay versions, endpoints, and denominators are correct, and no required change remains.
