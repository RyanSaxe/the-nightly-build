# Evidence: Dependabot cooldown release path

The evidence supports a precise operational account: Dependabot checks routine version updates on the configured schedule, filters newly published versions by cooldown, and then applies the usual pull-request rules; security updates take a separate, advisory-triggered path that is not subject to cooldown, the version-update schedule, or the version-update open-PR limit. The current default for version updates is three days. A configured SemVer-specific delay overrides the general delay for that update type, and a cooldown `exclude` match overrides `include`. The recent adoption study shows that seven days was the most common explicit choice among early adopters, but neither that study nor the practitioner evidence establishes seven days as optimal or proves that cooldown improves security. The main thin points are runtime behavior for transitive dependencies, the absence of a live Dependabot run for the example below, and a mismatch between GitHub's documentation and the public SchemaStore schema on two validation bounds.

## Sources

### 1. GitHub Dependabot options reference

URL:         https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference
Kind:        Primary. GitHub owns Dependabot and specifies the service's current configuration behavior.
Establishes: The current three-day default for version updates; security-update bypass; order of schedule and cooldown checks; fallback from absent SemVer-specific keys to `default-days`; cooldown `exclude` precedence over `include`; and the separate purposes of `groups`, `open-pull-requests-limit`, and `schedule`.
Paraphrase:  Dependabot first checks for version updates according to `schedule.interval`, then applies cooldown. A release younger than its applicable cooldown is skipped. If a SemVer-level delay is absent, `default-days` supplies the delay. If a dependency matches both cooldown lists, `exclude` wins, removing that dependency from cooldown. Group rules combine matching updates into fewer PRs. The open-PR setting caps concurrent version-update PRs at five by default; security PRs neither count toward nor obey that limit. A daily schedule runs on weekdays.
Locators:    `cooldown`, lines 232-298; `groups`, lines 317-337; `open-pull-requests-limit`, lines 526-540; `schedule`, lines 700-726.
Quote:       None needed.

### 2. GitHub tutorial: Optimizing the creation of pull requests for Dependabot version updates

URL:         https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/optimizing-pr-creation-version-updates
Kind:        Primary. GitHub supplies the worked configuration and stated service limits.
Establishes: Cooldown applies to version updates and not security updates; omitting `include` applies cooldown to every dependency; `"*"` also includes every dependency; GitHub documents cooldown day values from 1 through 90 and up to 150 entries in each of `include` and `exclude`.
Paraphrase:  The tutorial's worked example assigns major, minor, and patch delays of 30, 7, and 3 days. It includes a wildcarded package family and then exempts one exact package through `exclude`. GitHub recommends using `exclude` for dependencies that should not inherit an otherwise broad cooldown.
Locators:    “Setting up a cooldown period for dependency updates,” lines 87-149; “Grouping related dependencies together,” lines 151-161.
Quote:       None needed.

### 3. GitHub Dependabot pull requests

URL:         https://docs.github.com/en/enterprise-cloud@latest/code-security/concepts/supply-chain-security/dependabot-pull-requests
Kind:        Primary. GitHub defines how its service triggers version and security pull requests.
Establishes: A security-update PR is triggered by a Dependabot alert for a dependency on the default branch when security updates are enabled. It is advisory-triggered rather than run on the version-update schedule. Version updates use the configured schedule and default to at most five open PRs.
Paraphrase:  The separate trigger is the reason an urgent security patch bypasses the release-age gate: it enters the security-update path rather than the scheduled version-update path. GitHub still recommends tests and acceptance checks before merge.
Locators:    “Pull requests for security updates,” lines 32-49; “Pull requests for version updates,” lines 50-55.
Quote:       None needed.

### 4. GitHub: Configuring Dependabot security updates

URL:         https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-security-updates
Kind:        Primary. GitHub owns the repository settings that enable the security-update path.
Establishes: Dependabot security updates are a repository or organization setting, not something the minimal `dependabot.yml` enables. Grouped security updates additionally require the dependency graph, Dependabot alerts, and Dependabot security updates.
Paraphrase:  A repository owner enables security updates under Settings → Advanced Security. A cooldown configuration alone cannot guarantee an urgent security PR; the alert and security-update features must be active.
Locators:    “Managing Dependabot security updates,” lines 28-42; “Grouping Dependabot security updates,” lines 43-59.
Quote:       None needed.

### 5. GitHub: Dependabot supported ecosystems and repositories

URL:         https://docs.github.com/en/code-security/reference/supply-chain-security/supported-ecosystems-and-repositories
Kind:        Primary. GitHub states the service's ecosystem-specific support limits.
Establishes: Security-update coverage is not universal for transitive dependencies. GitHub's Gradle example says a transitive dependency uploaded to the dependency graph can generate an alert while Dependabot remains unable to locate it in the repository and therefore cannot create the security PR.
Paraphrase:  “Security updates bypass cooldown” does not mean every vulnerable transitive dependency receives an immediate PR. Detection and the ability to construct an update are separate conditions.
Locators:    “Gradle,” lines 129-148, especially the note at lines 146-148.
Quote:       None needed.

### 6. SchemaStore Dependabot 2.0 JSON Schema

URL:         https://json.schemastore.org/dependabot-2.0.json
Kind:        Secondary. SchemaStore publishes the machine-readable editor schema, but GitHub does not identify it as the runtime validator for the hosted Dependabot service.
Establishes: The public schema recognizes `cooldown`, `default-days`, all three SemVer-specific day keys, `include`, and `exclude`; it rejects unknown keys inside `cooldown`. It sets maximum day values to 90. It currently sets `include` and `exclude` to 100 items each and permits zero only for `semver-patch-days`, which conflicts with GitHub's prose documentation.
Paraphrase:  The tested YAML below is structurally valid against this schema. The schema should be used as a configuration-shape check, not as authority over GitHub's contradictory service documentation.
Locators:    JSON object `definitions.update.properties.cooldown`; `default-days`, `semver-major-days`, `semver-minor-days`, `semver-patch-days`, `include`, and `exclude` constraints.
Quote:       None needed.

### 7. Tanaka, Tsuchida, Shimari, Kula, and Matsumoto, “An Exploratory Study of Dependabot Cooldown Adoption in Open-Source GitHub Projects”

URL:         https://arxiv.org/html/2609.16605v1
Kind:        Primary research. The authors own the repository sample, configuration-history analysis, manual coding, statistical analysis, and stated limitations. It is a September 15, 2026 preprint marked for *Empirical Software Engineering*, with no accepted date shown.
Establishes: In a population of 1,462 active, non-fork, non-archived repositories drawn from the 10,000 most-starred GitHub repositories that had a Dependabot configuration, 135 had adopted cooldown by the April 30, 2026 cutoff. Among the 251 repository-ecosystem configurations retaining cooldown, 244 set `default-days`; 157 of those 244 used seven days. Security appeared in 83 of 92 adoption events with an identifiable motivation. The study explicitly does not test effectiveness or establish an optimal delay.
Paraphrase:  Early adoption was limited and concentrated in visible open-source projects. Most adopters used one general delay rather than SemVer- or package-specific tuning. Seven days is an observed convention: 64.3% of configurations that explicitly set `default-days` chose it. The observation window predates GitHub's July 2026 three-day platform default, so the study measures explicit early-adopter choices, not acceptance of today's default.
Locators:    Abstract, lines 57-60; data collection, lines 139-148; Tables 3-5, lines 300-349; Table 10 and RQ3 results, lines 403-433; implications and threats to validity, lines 436-475; conclusion, lines 476-482.
Quote:       “the common 7-day setting should not be interpreted as optimal” (Conclusion, line 481).

### 8. Gregor Ehrensperger, “Dependabot now applies a 3-day cooldown by default; I still suggest 7”

URL:         https://ehrensperger.dev/blog/dependabot-cooldown-three-days.html
Kind:        Primary for an independent practitioner's recommendation and reasoning; secondary for GitHub service facts and incident statistics that the post repeats from other sources.
Establishes: A practitioner recommends seven days while candidly calling that choice a “gut-feeling sweet spot,” and identifies two costs: the strategy depends on other users taking earlier exposure, and four extra days also postpone legitimate fixes and features.
Paraphrase:  Ehrensperger's case for seven days is a policy judgment: use the population on GitHub's three-day default as an earlier warning cohort, while maintaining a sufficiently fast vulnerability response. It is not measured proof that seven days is superior.
Locators:    Opening rationale, lines 7-17; “So, 3 days or 7?”, lines 18-30.
Quote:       “with 7 days as a gut-feeling sweet spot” (line 7).

### 9. Dependabot-core issue #14683, “npm: dependabot does not respect cooldown period for transitive dependencies”

URL:         https://github.com/dependabot/dependabot-core/issues/14683
Kind:        Primary for the reporter's reproducible observation and linked artifacts; not an authoritative statement of intended behavior, and no maintainer resolution was visible in the retrieved issue.
Establishes: In the reporter's npm reproduction, a seven-day cooldown selected a direct dependency version seven days old but also updated a transitive dependency to a release less than one day old, even though older eligible versions existed.
Paraphrase:  The report is evidence against saying a Dependabot cooldown necessarily age-gates every resolved transitive package in a lockfile. It does not prove the behavior for every ecosystem or current future release.
Locators:    “Updated dependency,” lines 188-190; “What you expected to see,” lines 191-206; linked smallest manifest, lines 215-217.
Quote:       None needed.

### 10. Gradle repository `.github/dependabot.yml`

URL:         https://github.com/gradle/gradle/blob/master/.github/dependabot.yml
Kind:        Primary artifact for one project's current configuration practice; it does not establish Dependabot semantics.
Establishes: The Gradle project uses daily checks and a seven-day `default-days` cooldown for its Maven ecosystem entry, while its separate Gradle entry sets `open-pull-requests-limit: 0`. This is a concrete example of cooldown, schedule, and PR-limit controls serving different purposes in one repository.
Paraphrase:  A prominent project has adopted seven days for one ecosystem, but does not apply the same policy uniformly across all ecosystem entries. The file supports “observed choice,” not “optimum.”
Locators:    File lines 268-315, especially Maven entry lines 306-315 and Gradle entry lines 288-296.
Quote:       “don't immediately create PRs for available updates” (inline comment on `default-days: 7`).

## Tested minimal example

Assumed repository: an npm service whose root `package.json` has ordinary public dependencies plus an internal incident client. Dependabot security updates are separately enabled in repository settings. The dependency graph and Dependabot alerts are active, the dependencies are on the default branch, and a security fix is available when the security scenario begins.

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "daily"
      time: "09:00"
    cooldown:
      default-days: 7
      semver-patch-days: 3
      include:
        - "*"
      exclude:
        - "@acme/incident-client"
```

Test performed September 27, 2026: parsed with PyYAML `safe_load`, then validated with Python `jsonschema.Draft7Validator` against the live schema at `https://json.schemastore.org/dependabot-2.0.json`. Result: zero validation errors. This proves YAML parsing and conformance to that public schema. It is not a live hosted-Dependabot test.

The sequence below is documentation-backed original analysis, not observed output from a test repository. “Immediately” for an excluded dependency means “without a cooldown”; because GitHub documents the version-update process as schedule check first and cooldown check second, the table treats the first eligible moment as the next scheduled run.

| Release through the same configuration | Trigger and gate | Earliest PR path under the stated times | Control outside cooldown |
|---|---|---|---|
| Ordinary patch for `public-parser`, published Monday 08:00 UTC | Version update. `include: "*"` puts it in cooldown; `semver-patch-days: 3` is more specific than the seven-day default. | Monday, Tuesday, and Wednesday 09:00 runs skip the release because it is younger than three days. Thursday 09:00 is the first scheduled run after the three-day age is reached. With no group rule, it gets an individual PR if the default five-open-version-PR limit has room. | CI, compatibility review, release notes, and merge policy decide whether and when it enters the codebase. |
| Urgent security patch for `public-parser`, with an alert and fix available Tuesday 14:00 UTC | Security update. The advisory triggers this path; the version-update schedule, three-day patch cooldown, and version-update open-PR limit do not apply. | Dependabot attempts the security PR when the alert-triggered security update runs, rather than waiting for Wednesday 09:00 or for three days of package age. GitHub documents no exact service-latency guarantee. | The repository must have security updates enabled. Humans or automation still need severity triage, tests, review, merge, deployment, and a manual fallback if Dependabot cannot construct the fix. |
| Routine update for `@acme/incident-client`, published Monday 08:00 UTC | Version update. It matches `include: "*"` and exact `exclude`; `exclude` wins, so no cooldown applies. | It is eligible at Monday's 09:00 scheduled run, subject to the version-update open-PR limit. Exclusion does not turn the update into an event-triggered security PR. | The team needs an explicit trust and emergency policy for the internal package; exclusion trades the observation window for faster uptake. |

For a major or minor version update in this example, the omitted SemVer-specific key falls back to `default-days: 7`. No `groups` rule is present, so dependencies are not consolidated. The `schedule` decides when Dependabot looks, cooldown decides which release ages are eligible at that run, grouping decides which eligible updates share a PR, and the open-PR limit decides whether another version-update PR may be opened.

## Contradictions

- GitHub's current tutorial says all cooldown day values must be 1-90 and each cooldown list may contain 150 entries. The current public SchemaStore schema allows `semver-patch-days: 0`, rejects zero for the other day keys, and caps each list at 100. For hosted-service claims, use GitHub's prose documentation; record the schema mismatch as a tooling risk. The example stays within both sets of bounds.
- GitHub's reference says a dependency in cooldown `exclude` “will be updated immediately,” while the same reference orders `schedule.interval` before the cooldown check. The safest reading is “immediately eligible without release-age delay at the next version-update run,” not “an event-triggered PR at publication.” No live test here resolves finer service timing.
- Some practitioner posts describe a seven-day Dependabot cooldown as covering “every dependency.” Issue #14683 supplies a concrete npm counterexample for a transitive package. The issue is a reporter's observation, not a documented guarantee or a maintainer-confirmed universal defect.
- Ehrensperger recommends seven days, but labels the original choice a gut feeling. The adoption study expressly says the common seven-day setting is not evidence of an optimum and does not demonstrate incident prevention.
- The adoption study's April 30, 2026 cutoff predates GitHub's July 2026 three-day default. Its adoption percentages describe explicit early-adopter configurations, not all repositories operating under the current default.

## Numbers

Figure: 3 days, current default cooldown for version updates even when `cooldown` is absent.
Owner:  GitHub Dependabot options reference.
Scope:  Newly released versions considered for version-update PRs on github.com; security updates are excluded from this delay.

Figure: 1-90 days, documented configurable cooldown range.
Owner:  GitHub tutorial on optimizing version-update PR creation.
Scope:  Each configured cooldown day value. The SchemaStore exception for patch value zero is a contradiction, not a hosted-service claim.

Figure: 150 entries per `include` list and 150 per `exclude` list.
Owner:  GitHub tutorial on optimizing version-update PR creation.
Scope:  Cooldown dependency-name lists. The current public schema instead caps each at 100.

Figure: 5 open version-update PRs by default.
Owner:  GitHub Dependabot options reference.
Scope:  Concurrent version-update PRs for a configured package ecosystem; security PRs do not count and have no such limit.

Figure: 1,462 repositories in the final study population; 135 adopters and 1,327 non-adopters.
Owner:  Tanaka et al.
Scope:  Active, non-fork, non-archived repositories with a Dependabot configuration, filtered from the 10,000 most-starred GitHub repositories; observation window July 1, 2025-April 30, 2026.

Figure: 251 repository-ecosystem configurations retained cooldown at the cutoff.
Owner:  Tanaka et al.
Scope:  Ecosystems inside the 135 adopter repositories, excluding one ecosystem that had abandoned cooldown.

Figure: 244 of 251 retained configurations set `default-days` (97.2%); 157 of those 244 set seven days (64.3%).
Owner:  Tanaka et al.
Scope:  Explicit settings at the April 30, 2026 cutoff. Seven days is the mode and median among configurations setting `default-days`, not an effectiveness result.

Figure: `semver-major-days` 23 of 251 (9.2%); `semver-minor-days` 20 of 251 (8.0%); `semver-patch-days` 19 of 251 (7.6%); `include` 3 of 251 (1.2%); `exclude` 5 of 251 (2.0%).
Owner:  Tanaka et al.
Scope:  Explicit key use among retained repository-ecosystem cooldown configurations at the cutoff.

Figure: Security was present in 83 of 92 first-adoption events with an identified motivation; linters triggered 43 of 75 security-only adoptions (57.3%).
Owner:  Tanaka et al.
Scope:  Manual coding of commits, PRs, and issues for the 135 first-time adopter repositories; 43 events had unknown motivation.

Figure: In issue #14683, the selected direct dependency release was 7 days old while one updated transitive dependency release was 0 days old under a 7-day cooldown.
Owner:  The issue reporter and linked reproduction artifacts.
Scope:  One npm reproduction reported in May 2026; not a cross-ecosystem measurement or a documented service guarantee.

## Limits

- No live GitHub Dependabot run was performed. The minimal YAML passed parsing and the public JSON Schema only; all release-path behavior in the table is derived from current documentation.
- No source establishes three days, seven days, or another interval as the optimal security/latency tradeoff. The study measured adoption and configuration, not attack prevention or vulnerability exposure.
- Cooldown delays Dependabot's proposal of version updates. It does not stop direct installs, package-manager lockfile refreshes, other bots, manual updates, auto-merge, or deployment from adopting a fresh release.
- A security bypass requires an enabled and functioning security-update path, a Dependabot alert on the default branch, and a fix that Dependabot can construct. Unsupported or unresolved transitive cases can leave an alert without an automatic PR.
- GitHub's documentation does not state exact hosted-service latency, registry timestamp rounding, or whether an eligible release is always proposed in the first run after its cooldown expires.
- Issue #14683 is useful practitioner evidence but had no visible maintainer resolution in the retrieved page. It should qualify claims about transitive coverage, not be generalized as settled behavior for every ecosystem.
- The adoption study does not generalize to private repositories, enterprise repositories, smaller open-source projects, other hosting platforms, Renovate, or package-manager-native cooldowns. Its ten-month window ended before the current default changed.
- The SchemaStore file is a third-party public schema. Its conflicts with GitHub's prose docs prevent treating it as the hosted service's final validation authority.

## Source assets

### GitHub Dependabot options reference

Asset: The numbered five-step process under `cooldown`, followed by the cooldown parameter table and the two-item precedence note.
Shows: Schedule is evaluated before cooldown; SemVer fallback and `exclude` precedence can be read in one source.
Crop:  Retain the `cooldown` heading, steps 1-5, parameter rows, and both note bullets. Omit the long supported-package-manager table unless ecosystem coverage is discussed.

### GitHub optimizing-PR tutorial

Asset: The complete pip YAML example under “Setting up a cooldown period,” plus the range and list-size bullets immediately below it.
Shows: How general, SemVer-specific, include, and exclude controls fit into one valid update block.
Crop:  Retain the whole update block and the 1-90/150-item notes. Omit duplicated rendered code and the following grouping section.

### GitHub Dependabot pull requests

Asset: None found.

### GitHub configuring security updates

Asset: Screenshot under “Enabling or disabling Dependabot security updates for an individual repository.”
Shows: The repository Settings location where the bypass path is enabled.
Crop:  Retain the “Security and quality”/Advanced Security context and the Dependabot security updates control; omit unrelated settings.

### GitHub supported ecosystems and repositories

Asset: None found.

### SchemaStore Dependabot 2.0 JSON Schema

Asset: The `cooldown` object definition with its six property constraints.
Shows: The exact machine-readable bounds used by editor validation and the two points that diverge from GitHub prose.
Crop:  Retain the `cooldown` property name through `additionalProperties: false`; omit unrelated schema definitions.

### Tanaka et al. adoption study

Asset: Table 10, “Set rate, median, most common value, and maximum of each cooldown key.”
Shows: General seven-day delays dominate while SemVer and package-list customization are uncommon.
Crop:  Retain the table title, all six key rows, and the paragraph giving 157 of 244/64.3%. Do not detach the table from its 251-configuration denominator.

Asset: Figure 1, repository filtering stages.
Shows: How the initial 10,000 most-starred repositories became the 1,462-repository analysis population.
Crop:  Retain every filtering stage and exclusion count; omit surrounding related-work text.

### Ehrensperger practitioner post

Asset: None found.

### Dependabot-core issue #14683

Asset: The linked PR's package-age list in the issue body.
Shows: The direct dependency respected the seven-day choice while a transitive dependency moved to a release less than one day old.
Crop:  Retain the configured seven-day expectation, direct and transitive age bullets, and the note that an older transitive release existed. Omit GitHub navigation and reactions.

### Gradle `dependabot.yml`

Asset: The Gradle and Maven update blocks in the configuration file.
Shows: `open-pull-requests-limit: 0` and `cooldown.default-days: 7` are independent controls attached to different ecosystem entries.
Crop:  Retain both ecosystem names, directories, limits/cooldown, and schedules. Omit labels and boilerplate comments.

## Discarded

URL: https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/ — Correct primary announcement, but the live options reference is more complete and current for configuration claims.
URL: https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-version-updates — Duplicates the three-day default and security exception without adding the precedence or control boundaries needed here.
URL: https://docs.github.com/en/code-security/concepts/supply-chain-security/about-the-dependabot-yml-file — Useful orientation, but the options and security-update references establish the needed claims more directly.
URL: https://mattsch.com/blog/2026/03/28/harden-your-github-actions-workflows-with-zizmor-dependency-pinning-and-dependency-cooldowns/ — Independent practitioner context, but its statement that “every dependency” must be seven days old is too broad in light of the npm transitive-dependency reproduction.
URL: https://tosbourn.com/dependabot-cooldown/ — Treats a Dependabot proposal delay as though a fresh dependency cannot enter the codebase by any route; that overstates what cooldown controls.
URL: https://dylanbochman.com/blog/2026-04-30-two-supply-chain-attacks-in-one-day — Valuable account of testing a security control, but its seven-day effectiveness claim is speculative and its configuration discussion adds no authoritative Dependabot semantics.
URL: https://nesbitt.io/2026/01/02/how-dependabot-actually-works.html — Strong architecture background, but it does not establish cooldown release-path behavior.
