# Commission: expert-tools/base-ui-custom-components

## Authorization

The paper owner asked for an independently researched article on the best tooling for designing beautiful, custom UI components and explicitly authorized publication. The existing article produced from the same prompt is excluded from every role's inputs and must not be opened, searched, quoted, or used for structure. Its filename was observed only to prevent a path collision.

## Home

- Series: `expert-tools`
- Template: `article`
- Slug: `base-ui-custom-components`
- Publication: prepare an ordinary Article PR after approval; do not hold it for review unless the owner changes the instruction.

Expert Tools is the closest configured home because the piece makes a developer-tooling recommendation and must show where the tools enter a real component workflow. Base UI is the center of the technical evaluation. The surrounding libraries are compared where they solve a different layer of the same job.

## Question and contribution

Question: Which current tools let a React team reach a distinctive, polished interface quickly without giving up accessibility, control, or the ability to change the design later?

The article must distinguish three jobs that are often collapsed into “a component library”: visual starting points, accessible interaction primitives, and the environment that keeps custom components coherent. It should make a concrete recommendation for each job, explain when a different choice wins, and demonstrate the recommendation with a small Base UI example whose value is visible in the code.

Provisional angle to test, not a conclusion to preserve: source-distributed components are the fastest visual start, Base UI or React Aria should own difficult behavior when a design departs from the starter, and Storybook plus tokens protects coherence after the first screen. AI generators can accelerate exploration but do not replace the behavior layer or the design system.

## The article must establish

- A usable meaning of “custom”: how far a team can move from the default appearance and composition before it starts fighting the tool.
- The architectural difference among styled suites, source-distributed components, unstyled behavior primitives, visual catalogs, and AI generators.
- Why Base UI is a strong center for a highly custom React interface, including its composition model, accessibility claims, styling surface, project history, and current maintenance state.
- Where shadcn/ui, React Aria Components, Radix Primitives, Tailwind CSS, Storybook, Motion, and v0 fit. Add or remove a candidate only when the evidence changes the decision.
- The adoption cost: code ownership, upgrade work, accessibility verification, bundle/runtime tradeoffs where documented, and the engineering skill the approach assumes.
- Exact, checked quotations from at least two widely followed public practitioners or creators. Prefer remarks that sharpen the decision, not endorsements. Every quotation must be verified against raw first-party text.
- A small code listing that proves how a team can preserve Base UI's interaction behavior while replacing its visual grammar. It must illuminate the workflow and must not become an installation tutorial.
- A compact comparison or decision table supported by the cited documentation.

## Boundaries

- Do not read or cite the existing `library/expert-tools/shadcn-ui.html` article or any artifact from its production branch.
- Do not rank tools by GitHub stars, social-media attention, or screenshot beauty.
- Do not claim that visual taste is objective. Judge control, behavior coverage, accessibility support, ownership, maintenance, and speed to a custom result.
- Do not treat an official demo as independent proof that a component is accessible. State the scope of vendor claims and the testing burden that remains.
- Do not turn the piece into a directory. Every named tool must change a decision.
- Use current information retrieved on 2026-09-22. Record release or maintenance facts with dates.

## Research still required

- Read official architecture, accessibility, styling, and release documentation for the shortlisted tools.
- Inspect Base UI's implementation and repository history beyond its landing page.
- Find independent practitioner evidence about the ownership-versus-abstraction tradeoff and any credible accessibility or maintenance concerns.
- Verify popular-person quotations word for word from first-party pages or raw social posts.
- Search for facts that would defeat Base UI as the recommended behavior substrate, including missing components, unstable APIs, maintenance gaps, or poor real-world accessibility.

## Shape

The reasoning should move from the decision teams actually face to the layers hidden inside “component library,” then test the leading options against one deliberately customized interaction. A table should carry the layer-by-layer choice. A code listing should carry the implementation claim. Quotation furniture should be used only when a practitioner's exact wording clarifies the tradeoff. End with an adoption rule concrete enough to use on a new React project.

## Recent-pattern notes

The excluded comparison article was not read. Three older, unrelated Expert Tools structures were checked only for repetition risk.

- Avoid the recent headline mold “Tool does X, and Y.”
- Do not build successive headings from the same “What…” or “Where…” construction.
- Do not reserve maintenance for a perfunctory last section; maintenance belongs beside the recommendation it changes.
- Do not repeat the older pieces' sequence of mechanism, example, limitation, benchmark, maintenance. Let the selection decision determine the order.

## Runtime record

- Harness: ChatGPT Work / Codex
- Orchestrator model: inherited GPT-5 runtime
- Writing coach: capable model, low-effort policy target
- Researcher: capable model, high-effort policy target
- Writer: capable model, medium-effort policy target
- Editor: inherited model with high-effort review required by policy
