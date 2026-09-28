# Editorial review: technical/dependabot-cooldown-release-path (editor/02)

## Correct
The article argues that Dependabot cooldown is a release-age gate for version updates, not a complete dependency-response policy. Its supporting claims are that the schedule determines when Dependabot checks, SemVer-specific values and include/exclude precedence determine which releases are eligible, security updates follow an alert-triggered path outside cooldown and the version-update PR limit, and the repository retains merge and emergency-response decisions.

The current GitHub options reference supports the three-day default, schedule-before-cooldown order, SemVer fallback, `exclude` precedence, and five-PR default. GitHub's pull-request and security-update pages support the default-branch alert trigger, schedule bypass, separate enablement, and absence of the version-update PR limit on security updates. The SchemaStore endpoint lands after a redirect and its current schema still validates the six cooldown keys while differing from GitHub's documentation on the 100-versus-150 list cap and whether `semver-patch-days` may be zero. The example remains inside both sets of bounds.

The study figures hold against their denominators and period: the final population is 1,462 repositories at the April 30, 2026 cutoff, 135 are adopters, 244 retained repository-ecosystem configurations set `default-days`, and 157 of those 244 use seven days. The article correctly treats seven days as observed practice rather than an optimum or evidence of incident prevention. Ehrensperger's post supports both his seven-day recommendation and the four-day cost relative to GitHub's default; I narrowed that cost to legitimate version-update fixes and features so it cannot be mistaken for the security-update path.

The eighth source is substantive. GitHub's current Gradle documentation says an uploaded transitive dependency can produce an alert while leaving Dependabot unable to locate the dependency and create a security update. The article uses that documented case to establish the constructability boundary on its security-bypass claim. It is not bibliography padding. Every printed source URL lands on the named source. The `data-nb-kind` labels are accurate: GitHub documentation and the authors' study are primary for their claims, Ehrensperger is primary for his recommendation, and SchemaStore is secondary for hosted Dependabot behavior.

## Reads well
No paragraph needed removal. The draft follows one queue from publication through eligibility and separates observed behavior, documented behavior, and repository policy. It does not borrow a sentence from the commission or the voice-guide passages, and it avoids the recent Technical structures named in the commission.

I removed the metaphorical closing that said the repository “owns the exit.” It reduced to a portable slogan at the most sensitive edge of the piece. The replacement names the two decisions that remain: when to merge routine updates and what to do when an urgent security PR does not appear. I also qualified “fixes and features” as version-update fixes and features, keeping the practitioner tradeoff on the path the source discusses.

## The experience
The compact YAML listing changes the fate of the example releases, and the table lets the reader compare trigger, gate, earliest documented path, and outside policy without reconstructing those relationships from three documentation pages. The added Gradle limitation earns its place after the table because it shows why even the bypass path needs a fallback.

The local page could not be opened in the managed browser because that browser blocks `file:` URLs. I did not bypass the restriction. I inspected the HTML structure and visible text directly: the headline and dek agree with the body, the four argument sections arrive in a useful order, the code block precedes the trace that uses it, and the eight-item source list follows the conclusion. The piece's original work is the timed comparison of three releases under one configuration, with each gate paired to the repository decision Dependabot cannot make.

## Edits
- Narrowed Ehrensperger's four-day tradeoff to legitimate version-update fixes and features.
- Replaced the slogan-like final sentence with the repository's concrete merge and urgent-fallback decisions.
- Ran `nb stamp`, which set the article to 992 words, four reading minutes, and eight sources.
- Reopened all eight printed source URLs and confirmed the eighth source supports a relevant security-update limitation.

## Decision
approve — All claims survive current-source review, the eight-source floor is met by a relevant source and claim, and the exact proof returns `BLOCK: 0`, `WARN: 0`, and `verdict: PUBLISHABLE`.
