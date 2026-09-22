# Evidence: expert-tools/shadcn-ui (01)

The evidence supports a layered recommendation rather than a single winner. shadcn/ui is unusually strong as a visual starting point because it distributes component source into the application and now lets a project choose among Base UI, Radix and React Aria bases. Base UI, Radix, React Aria and Zag/Ark UI are behavior-oriented foundations with different API, accessibility, internationalization and framework tradeoffs. Catalyst, MUI, Mantine and Chakra reduce visual and implementation work further, but they leave more of the system's appearance or styling model in the library's hands. Storybook supplies the inspection surface that makes any chosen component system testable and understandable. The evidence is thin on independent comparisons of visual quality, long-term migration cost and accessibility in arbitrary applications, so the article must make conditional recommendations and not rank vendors by marketing claims.

## Sources

### 1. shadcn/ui introduction

URL: https://ui.shadcn.com/docs
Kind: primary, maintained project documentation and the project's own design philosophy.
Establishes: shadcn/ui describes itself as both a set of accessible components and a code-distribution platform. It explicitly distinguishes its approach from an npm dependency: “This is not a component library. It is how you build your component library.” It says the top component layer is open for modification, components share a composable interface, a flat-file schema and CLI distribute code, and the defaults are intentionally designed to work together.
Paraphrase: The relevant object is not a package that stays outside the application. It is a source payload that the team can inspect and change. The source also says the project is designed for AI tools to read and modify, but that is the project's stated design goal, not independent evidence of output quality.
Locators: Introduction, lines headed “Open Code,” “Composition,” “Distribution,” and “Beautiful Defaults,” retrieved 2026-09-22 through the page's rendered text.
Quote: “This is not a component library. It is how you build your component library.” This is short enough to quote and is the clearest statement of the ownership thesis.

### 2. shadcn/ui: Base UI as the default

URL: https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default
Kind: primary, project announcement by shadcn/ui.
Establishes: New shadcn projects default to Base UI as of July 2026. Radix remains fully supported. The announcement says shadcn originally used Radix and rebuilt its components for Base UI while preserving the same higher-level abstraction, rather than forcing existing projects to switch.
Paraphrase: “shadcn/ui” is no longer a single underlying behavior library. It is becoming a distribution and presentation layer that can target multiple bases. The article should call this a current status change, not a verdict that Base UI is universally better.
Locators: “Base UI as the Default,” lines 139–166.
Quote: The article need not quote the announcement; paraphrase the status and link the source.

### 3. shadcn/ui: React Aria base

URL: https://ui.shadcn.com/docs/changelog/2026-07-react-aria
Kind: primary, project announcement by shadcn/ui.
Establishes: React Aria became a first-class component base in shadcn/ui in July 2026. The CLI can initialize a project with `--base aria`, handles dependencies and registry resolution, and keeps Base UI as the default while Radix remains supported.
Paraphrase: The choice of behavior layer is now part of the shadcn setup rather than an afterthought. This supports a recommendation to choose a base according to interaction and accessibility needs instead of choosing by visual examples alone.
Locators: “What’s New” and “Start with React Aria,” lines 139–163.

### 4. shadcn/ui CLI and update model

URL: https://ui.shadcn.com/docs/changelog/2023-06-new-cli
Kind: primary, project changelog and CLI documentation.
Establishes: The CLI reads `components.json`, resolves components and dependencies, formats them for the project's configuration, and writes source into the application. The `diff` command shows upstream changes. The page states that, because the model is copy and paste, teams must manually update their projects.
Paraphrase: Source ownership removes the package's visual boundary but also removes automatic upgrades. A team should commit before applying updates and review the diff rather than treating the CLI as a package manager.
Locators: “add,” “diff,” and “Updating your project,” lines 194–241 and 386–390.
Quote: None required beyond source ownership; the manual-update caveat is more important than a slogan.

### 5. Base UI overview

URL: https://base-ui.com/react/overview/about
Kind: primary, project documentation from the Base UI maintainers.
Establishes: Base UI is an unstyled React component library from the creators of Radix, Material UI and Floating UI. It says it does not bundle CSS or prescribe a styling solution, adheres to WAI-ARIA design patterns, and exposes open component APIs with direct access to nodes so teams can add or remove parts.
Paraphrase: Base UI is a behavior foundation. It is a strong choice when the team wants to own CSS and DOM structure but does not want to implement common interaction behavior from scratch. The WAI-ARIA statement describes the library's intent and testing scope, not the accessibility of an application built on top of it.
Locators: “About Base UI,” “Headless,” “Accessible,” and “Composable,” lines 84–101.

### 6. Radix Primitives introduction

URL: https://www.radix-ui.com/primitives/docs/overview/introduction
Kind: primary, project documentation from Radix maintainers.
Establishes: Radix is a low-level library focused on accessibility, customization and developer experience. It handles aria and role attributes, focus management and keyboard navigation, ships without styles, exposes component parts, and recommends incremental adoption through the tree-shakeable `radix-ui` package or individual packages.
Paraphrase: Radix remains a credible choice for a team with an existing Radix system or one that values its mature vocabulary and wants to adopt primitives one at a time. The article should not imply that the July 2026 shadcn default makes Radix obsolete.
Locators: “Introduction,” “Key Features,” and “Incremental adoption,” lines 32–65.

### 7. React Aria getting started

URL: https://react-aria.adobe.com/getting-started
Kind: primary, Adobe's official React Aria documentation.
Establishes: React Aria provides unstyled React components and hooks with accessibility, internationalization, interactions and behavior built in. Its component API is designed around composition, generally keeping a 1:1 relationship with DOM elements so developers can control styling, layout and DOM order. Components have no default styles and the library offers a lower-level hooks API when more control is needed. A starter kit includes a configured Storybook.
Paraphrase: React Aria is the better fit when internationalization and assistive-technology behavior are core requirements or when the developer wants to move between components and lower-level hooks. It can require more understanding of the library's composition model than a pre-styled kit.
Locators: “What is React Aria?,” “Building a component,” “Styling,” “Starter kit,” and “Hooks,” lines 213–235, 314–344 and 731–743.

### 8. Ark UI and Zag

URL: https://ark-ui.com/docs/overview/about
Kind: primary, project documentation from the Chakra UI team.
Establishes: Ark UI targets multiple JavaScript frameworks and is built on Zag.js, whose component logic is modeled as finite state machines. Ark documents support for React, Solid, Vue and Svelte and describes more than 40 components and tools for accessible, complex interfaces.
Paraphrase: Ark/Zag is the relevant escape hatch when the same component behavior must be shared across framework adapters. The article should present the state-machine layer as an architectural choice with possible adapter and ecosystem costs, not as a free performance guarantee.
Locators: “Motivation,” “Solution,” FAQ entries “What is Ark UI?” and “Which JavaScript frameworks are supported?,” lines 231–265.

URL: https://zagjs.com/
Kind: primary, project documentation from Zag maintainers.
Establishes: Zag's machine APIs are headless and unstyled. The documented flow is to install a machine, consume it, connect it to a framework adapter, and render the DOM props it supplies. The page gives a React number-input example and describes accessible DOM semantics through adapters.
Paraphrase: Zag shows the lowest-level version of the behavior/surface split. It is useful to explain what “borrow the behavior, own the UI” means in code, but the article should not turn the example into an installation tutorial.
Locators: “Machines handle the logic. You handle the UI,” lines 30–52 and the framework-agnostic overview, lines 10–32.

### 9. Tailwind CSS utility classes

URL: https://tailwindcss.com/docs/styling-with-utility-classes
Kind: primary, Tailwind CSS documentation.
Establishes: Tailwind's utility classes keep structure and styling together, make UI chunks portable, constrain values to a design system, and support states and responsive variants. Tailwind generates CSS by scanning source files and emitting the utilities used.
Paraphrase: Tailwind is not the component layer. Its value in this article is that it makes owned component source compact, local and governed by tokens and variants. The article should not claim that utility classes automatically create a good design system; the constraint still has to be chosen well.
Locators: “The benefits of this approach,” “Designing with constraints,” and “How does this even work?,” lines 268–280 and 410–420.

### 10. Tailwind Catalyst

URL: https://tailwindcss.com/blog/introducing-catalyst
Kind: primary, Tailwind CSS team announcement.
Establishes: Catalyst is a source-based React UI kit built to be copied into the application, not installed as a dependency. The announcement says the components are intended as a starting point for a team's own component system and calls Catalyst a “disappearing UI kit.” The current getting-started documentation says it is designed for React projects using Tailwind and depends on Headless UI, Motion and `clsx`.
Paraphrase: Catalyst is the polished, curated option for a team that wants source ownership but does not want to design every default from zero. It is a paid starting point, tied to Tailwind's theme assumptions, and still leaves the team with source and dependency maintenance.
Locators: “Your components, not ours” and “Design is in the details” in the announcement; “Getting started” lines 34–68 in https://catalyst.tailwindui.com/docs.
Quote: “disappearing UI kit” is a short exact phrase that names the intended ownership outcome.

### 11. Material UI

URL: https://mui.com/material-ui/getting-started/
Kind: primary, MUI documentation.
Establishes: Material UI provides comprehensive prebuilt React components with Material Design defaults and a customization system. The documentation distinguishes it from MUI Base, which has no default styles or styling solution.
Paraphrase: MUI is the sensible speed-and-breadth choice when complex components and production defaults matter more than starting with a blank visual surface. The article should not describe it as impossible to customize; its own docs make customization a core feature. The cost is that the team is customizing a system with a strong existing visual and styling model.
Locators: “Material UI – Overview,” lines 29–48.

### 12. Mantine

URL: https://mantine.dev/
Kind: primary, Mantine project documentation.
Establishes: Mantine describes itself as a fully featured React component library with more than 120 customizable components and 70 hooks. It includes complex inputs, overlays and navigation, and offers hooks such as `use-move` for building custom controls. Its current documentation also exposes LLM-oriented docs and an MCP server.
Paraphrase: Mantine is useful when the goal is to ship a rich application quickly and the team is willing to live inside its component and styling vocabulary. Its breadth makes it a productive starting point; it does not prove that its visual language is the right foundation for a bespoke system.
Locators: homepage introduction and “Hooks library,” lines 7–12 and 49–112.

### 13. Chakra UI

URL: https://chakra-ui.com/docs/styling/overview
Kind: primary, Chakra UI documentation.
Establishes: Chakra says all components are styled using props and that style props are CSS styles expressed as props. Its docs also describe compositions, CSS variables, dark mode and conditional styles.
Paraphrase: Chakra makes rapid visual iteration easy when its prop-driven styling model fits the team. It is a different ownership boundary from copied source: a team works through the library's styling API and compositions rather than directly editing every component file.
Locators: “Styling,” lines 22–51.

### 14. Storybook

URL: https://storybook.js.org/
Kind: primary, Storybook project documentation.
Establishes: Storybook is a frontend workshop for building components and pages in isolation. It emphasizes hard-to-reach states and edge cases, testing, visual testing and documentation. It describes itself as incrementally adoptable and says its UI, examples and documentation help teams and AI agents reuse patterns.
Paraphrase: Storybook is not a styling library. It is the feedback and documentation surface that stops a copied component from becoming an undocumented local fork. The recommendation should be incremental: use it when a component has states worth inspecting, not as a mandatory ceremony for a one-button prototype.
Locators: “Build, test & document components,” “Develop durable user interfaces,” and “Document UI for your team to reuse,” lines 15–17, 119–147 and 243–249.
Quote: The page reproduces Brad Frost calling Storybook “a powerful frontend workshop environment tool”; use the shorter project description in the article unless a direct persona quotation is necessary.

### 15. Brad Frost on extending Atomic Design

URL: https://bradfrost.com/blog/post/extending-atomic-design/
Kind: primary, Brad Frost's own writing.
Establishes: Frost describes design tokens as ingredients that become functional when applied to a component, and says Atomic Design is a methodology rather than a rigid taxonomy. He writes that whatever taxonomy a team chooses should help it communicate and craft an effective design system.
Paraphrase: The recommendation should not turn “atoms,” “molecules” or any library's names into law. The useful unit is a shared vocabulary the team can change when it stops describing the product.
Locators: lines 27–35 and 43–48.
Quote: “atomic design is not rigid dogma.” Exact wording confirmed in the source.

### 16. Adam Wathan on Tailwind and Catalyst

URL: https://adamwathan.me/going-full-time-on-tailwind-css/
Kind: primary, Adam Wathan's own writing.
Establishes: Wathan describes Tailwind as a utility-first framework for rapidly developing custom user interfaces and describes its origin as reusable boilerplate copied between projects. His team's Catalyst announcement makes the ownership model explicit: source is copied into the application and is intended to become the team's component system.
Paraphrase: Tailwind's creator frames the tool around custom interfaces rather than a pre-designed component catalog. The article can use the shorter Catalyst phrase “disappearing UI kit” without making the older blog prove a current ecosystem ranking.
Locators: lines 0–16 in the Tailwind essay; https://tailwindcss.com/blog/introducing-catalyst, “Your components, not ours,” lines 22–31.

### 17. Mitchell Hashimoto on feedback loops

URL: https://mitchellh.com/writing/building-large-technical-projects
Kind: primary, Mitchell Hashimoto's own writing.
Establishes: Hashimoto describes a practical loop for large technical projects: keep a usable demo available and work on a problem the builder is experiencing. The piece is not a UI-specific source, but the feedback-loop principle applies directly to component states and interaction demos.
Paraphrase: A component library should have a runnable surface where its states can be inspected, not only source files that look plausible in review. Storybook is one way to create that surface; the point is the loop, not the brand.
Quote: “The goal is to always give yourself a good demo.” This is short enough to quote and is used as a workflow rule, not as evidence about Storybook's product capabilities.
Locators: “The goal is to always give yourself a good demo” and the surrounding discussion of feedback loops, retrieved 2026-09-22.

## Contradictions

- Copy-and-own is the article's preferred default, but shadcn's own documentation says projects must manually update copied components. Source ownership buys control by transferring merge and drift work to the application.
- Headless does not mean finished. Base UI, Radix, React Aria and Zag document accessibility behavior and customization boundaries, but none of those documents proves that an arbitrary application has correct labels, focus order, contrast, semantics or interaction tests.
- Styled libraries are not merely traps. MUI documents a broad customization system, Mantine and Chakra expose extensive customization and hooks, and those options can be rational when time-to-product or complex component breadth dominates visual ownership.
- “Beautiful” is a judgment, not a benchmark. First-party pages show the projects' design intent and examples; no independent source in this set establishes that one default visual language is objectively better.
- Cross-framework behavior is attractive in Ark/Zag, but the evidence is project-owned. Avoid claiming that the adapter architecture is always faster or easier than a React-only primitive.
- Storybook describes strong isolation and testing use cases, but its documentation is not evidence that every team should adopt it. The article should recommend it where component state and reuse justify the extra surface.

## Numbers

No numerical comparison carries the thesis. The article may mention Mantine's documented “more than 120” components and “70” hooks as evidence of breadth, but it should not use download counts, stars or vendor-reported adoption as a quality ranking.

## Limits

- There is no independent benchmark comparing the visual quality, accessibility outcomes or long-term maintenance cost of these libraries in the same application.
- The article is React-centered because shadcn/ui, Base UI, Radix, React Aria, MUI, Mantine and Chakra are React ecosystems. Ark/Zag is the cross-framework counterexample; this is not a survey of Vue, Svelte or Web Components tooling.
- The article does not establish a license or commercial procurement comparison for every option. Catalyst's current access model should be described only as a paid Tailwind Plus starting point if that detail is included.
- The research does not establish that AI-generated UI is reliable. It establishes only that open source and registry schemas make code available to AI tools.

## Source assets

None found. The argument is about code ownership and workflow, so an external screenshot would be decorative. The comparison table and command listing are authored from the documented behaviors and do not require a captured visual.

## Discarded

URL: https://x.com/adamwathan/status/1226511611592085504 — the indexed search result contains a relevant quote about `@apply`, but the canonical X page returned 403 to the research fetch. It is not needed because Wathan's own Tailwind/Catalyst writing supplies a verifiable first-party statement.

URL: https://ui.shadcn.com/ — the homepage is useful for visual examples but adds no evidence beyond the introduction and changelog, so it is not cited separately.

Third-party “best React component library” roundups — not opened or used because they repeat vendor descriptions and would not improve the ownership comparison.
