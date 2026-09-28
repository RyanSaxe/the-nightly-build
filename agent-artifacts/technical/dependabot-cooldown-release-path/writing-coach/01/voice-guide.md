# Voice guide

## How this piece should sound

Write as an engineer walking another engineer through an update queue that is actually moving. Begin with the repository and a dependency release appearing in the registry, then follow what Dependabot does next. Julia Evans's first passage shows the useful register: plain technical language, a concrete cost, and enough personality to sound like a practitioner without turning the walkthrough into a memoir.

Let configuration enter when it changes the fate of a release. Brandur Leach's passages move from an action to its exact command and then state the operational consequence in one clean sentence. The YAML should work the same way: show the complete small configuration, but explain `default-days`, semver-specific delays, include and exclude rules, and security-update bypasses at the point where each one delays, admits, or diverts an update.

Keep judgments proportional to what the controls establish. Fred Hebert's passages distinguish an observable event from the interpretation laid over it, and direct attention to the information available at the time. Treat the adoption study and seven-day setting that way: useful evidence about practice, not proof that cooldown improves security or that seven days is optimal. When the three release paths diverge, name the gate responsible and say plainly which urgent-response decision still belongs to repository policy outside Dependabot.

## Julia Evans, "What does debugging a program look like?"

Source: https://jvns.ca/blog/2019/06/23/a-few-debugging-resources/

> "Everybody also agrees that it’s extremely useful be able to reproduce the bug quickly."

Checked: https://jvns.ca/blog/2019/06/23/a-few-debugging-resources/, retrieved 2026-09-27

The sentence names the practical condition before explaining technique, and "extremely useful" gives it the pressure of lived work. Evans is visible in the directness: she sounds like someone impatient with a slow feedback loop, not like a manual defining debugging.

> "repeat until you understand what’s going on"

Checked: https://jvns.ca/blog/2019/06/23/a-few-debugging-resources/, retrieved 2026-09-27

This closes a small experimental loop with ordinary words instead of dressing it up as a methodology. The unceremonious phrasing makes the technical process feel usable and leaves the reader with the actual stopping condition.

## Brandur Leach, "Development log: Deploying Google Cloud Run from GitHub Actions"

Source: https://www.brandur.org/fragments/google-cloud-run-deploy

> "It’s the exact command I used to run manually whenever I wanted to deploy."

Checked: https://www.brandur.org/fragments/google-cloud-run-deploy, retrieved 2026-09-27

Leach connects the displayed configuration to a real previous operation, which tells the reader why the command belongs there. "Whenever I wanted to deploy" keeps the author present as an operator without making his experience the subject.

> "It now happens automatically from GitHub Actions."

Checked: https://www.brandur.org/fragments/google-cloud-run-deploy, retrieved 2026-09-27

The second sentence states the changed behavior immediately after the command. Its brevity makes the result easy to verify and shows Leach's preference for reporting what the machinery now does over celebrating the automation.

## Fred Hebert, "Errors are constructed, not discovered"

Source: https://ferd.ca/errors-are-constructed-not-discovered.html

> "Large systems are always in some weird degraded state."

Checked: https://ferd.ca/errors-are-constructed-not-discovered.html, retrieved 2026-09-27

The claim is compact and technically recognizable, while "some weird" gives it the voice of somebody who has operated such systems. Hebert uses informality to sharpen a limitation, not to soften or inflate it.

> "The labels we use, the lens through which we look at the incident, influence the way we build our explanations."

Checked: https://ferd.ca/errors-are-constructed-not-discovered.html, retrieved 2026-09-27

Hebert separates events from the account built around them without pretending interpretation can be removed. The first-person plural includes the writer among the people capable of imposing a convenient explanation, which gives the caution credibility.
