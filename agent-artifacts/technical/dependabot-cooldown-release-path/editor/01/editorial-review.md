# Editorial review: technical/dependabot-cooldown-release-path (editor/01)

## Correct
The article argues that cooldown is a release-age gate for Dependabot version updates, then traces a routine patch, an alert-triggered security patch, and an excluded dependency through one configuration. Its supporting claims are that SemVer-specific values override the general delay, `exclude` overrides `include`, security updates do not follow the version-update schedule or cooldown and do not obey the version-update PR limit, and repository policy still controls merge and urgent fallback.

GitHub's current options reference supports the three-day default, schedule-before-cooldown order, SemVer fallback, `exclude` precedence, five-PR default, and security-update exception. GitHub's current pull-request and security-update documentation supports the alert trigger, default-branch requirement, separate enablement, and version-update schedule bypass. The tutorial and live SchemaStore schema still disagree at 150 versus 100 package-list entries and on whether `semver-patch-days` may be zero; the article identifies that conflict and keeps its example inside both bounds. The study denominators recompute: 135 of 1,462 repositories adopted cooldown, and 157 of the 244 retained ecosystem configurations with `default-days` chose seven days. The article correctly says this is observed practice rather than an effectiveness result or optimum. Gregor Ehrensperger's account supports the added operational tradeoff: he recommends seven days as a judgment call and identifies four additional days of delay for legitimate fixes and features relative to GitHub's default.

The transitive-dependency paragraph failed current-source review. Dependabot-core issue #14683 now appears as Closed with project status Done, and the current dependabot-core release record identifies a fix for transitive npm, pnpm, and Yarn cooldown handling. I removed the paragraph and its source instead of presenting the reproduction as an unresolved current limitation. I also changed “internal” to “team-maintained,” because the complete example contains no private-registry configuration, and separated proposal timing from merge behavior in the final section.

Every remaining source URL lands on the printed source. The `data-nb-kind` labels are correct: GitHub documentation and the authors' study are primary for their claims, Ehrensperger's post is primary for his own recommendation and reasoning, and SchemaStore is secondary for hosted Dependabot behavior.

## Reads well
The opening moves from a Monday registry release to the scheduled run before introducing configuration, and the headings reconstruct the argument in order. The code block changes the fate of the three releases instead of becoming a YAML reference tour. The comparison table carries the timing and policy distinctions without repeating the surrounding prose.

I cut the resolved transitive-dependency detour because its factual premise no longer held, not for polish. I rewrote the update-route sentence because the original grouped auto-merge with mechanisms that can adopt a release before Dependabot proposes it. I added one concise practitioner-backed tradeoff after the adoption figures so the seven-day setting has an operating cost as well as a frequency count. I found no sentence borrowed from the commission or the voice-guide excerpts, and the piece does not repeat the recent percentage-led or code-heavy Technical structures named in the commission.

## The experience
The page lost one stale paragraph while retaining the compact YAML listing and three-row release-path table. Its eighth source now adds a concrete cost to the seven-day choice instead of padding the bibliography. No additional component would show the sequence more quickly than the table already does. The article gives readers a timed comparison that GitHub's separate reference pages do not: each release meets a named gate, and each row states the operational decision Dependabot cannot make.

The local article could not be opened in the managed browser because that browser rejects `file:` URLs. The HTML structure and visible text were inspected directly, and the repository proof completed successfully.

## Edits
- Changed the metadata and displayed dek from “internal package” to “team-maintained package.”
- Changed the first section's package description from “internal” to “team-maintained.”
- Rewrote the final section's first paragraph to distinguish adoption routes and merge policy from Dependabot proposal timing.
- Removed the stale npm transitive-dependency paragraph.
- Removed the issue #14683 source.
- Added Ehrensperger's documented seven-day tradeoff and cited his practitioner account.
- Renumbered sources by first appearance.
- Ran `nb stamp`, which set the article to 978 words, four reading minutes, and eight sources.

## Decision
approve — The current sources support every claim, no required changes remain, and the exact proof returns `BLOCK: 0`, `WARN: 0`, and a publishable verdict.
