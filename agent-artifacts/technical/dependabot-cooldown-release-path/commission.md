# Commission: technical/dependabot-cooldown-release-path

Explain GitHub Dependabot's cooldown controls through one realistic repository and one dependency release moving from registry publication to a pull request. Ground the reason to care in the recent large-scale adoption study, but do not treat adoption or reduced pull-request volume as proof of better security. Seven days is a common observed choice, not an established optimum.

Use current GitHub documentation and schema as the authority for configuration. Include one complete, minimal YAML example that a reader could adapt. Walk through default delay, semver-specific delays, include/exclude behavior, and the boundary between version updates and security updates. Verify current precedence and bypass behavior from primary documentation before stating it. Distinguish what cooldown schedules from what grouping, open-pull-request limits, and update intervals control.

Original work: trace a normal patch, an urgent security patch, and an excluded dependency through the same configuration. The comparison should reveal which gate delayed or bypassed each update and what operational policy must sit outside Dependabot.

Use a code listing and a small release-path table or ordered sequence if useful. Recent Technical patterns to avoid: September 25 opened with percentages, introduced an equation/stat strip, followed a diagnostic sequence, and ended with a four-field ledger; September 24 opened with an antithesis and advanced through several code-heavy API sections before a device-test conclusion. Do not copy either shape. Avoid presenting a YAML tour as the article's entire argument.

The Daily Brief owns same-day technology news. The Feature owns appropriations law. This piece stays on dependency-update operations.
