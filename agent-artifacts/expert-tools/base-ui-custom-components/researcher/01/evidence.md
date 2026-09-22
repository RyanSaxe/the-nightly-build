# Evidence: a component stack for custom React interfaces

The checked evidence supports a layered recommendation, not a universal winner: use source-distributed components for a quick visual start, an unstyled behavior library for difficult interaction semantics, tokens and Storybook for coherence and regression coverage, and Motion or an AI generator only where they add specific leverage. Base UI is a strong default for new, highly custom React work because its public parts, render prop, state attributes, hidden native controls, and active release line expose both markup and behavior. The evidence is thinner where marketing claims stand in for comparative testing. Most importantly, Base UI cannot be called “accessible by default” without qualification: its own docs assign labels, contrast, and focus appearance to the implementer, while a current detailed issue reports a focusable toast hidden from the accessibility tree. React Aria can defeat the Base UI recommendation for data-heavy, international, or assistive-technology-sensitive products because it documents broader collection, date, locale, and low-level-hook capabilities.

## Working definition and decision frame

“Custom” should be treated as three separate freedoms: **skin** (tokens and CSS), **skeleton** (DOM, parts, and composition), and **behavior** (keyboard, focus, pointer/touch, form, and assistive-technology semantics). A tool starts fighting the team when a routine change requires unstable selectors, escalating specificity, wrapper components, or copied interaction code. The categories in the article should not be collapsed:

| Category | What it owns | Strong starting point | Main ownership cost |
|---|---|---|---|
| Styled suite | Visual language, behavior, theme/runtime | Material UI when Material Design is acceptable | Deep divergence moves into slots, specificity, and theme overrides |
| Source-distributed components | The application’s copied component source | shadcn/ui | The application owns review and merging of upstream changes |
| Unstyled behavior primitives | Semantics, state, focus, keyboard/pointer behavior | Base UI; React Aria for richer collections/i18n; Radix for existing systems | The team still owns visual states, labels, contrast, and integration QA |
| Token/style layer | Design constraints and CSS production | Tailwind theme variables | Does not supply behavior or a design language by itself |
| Component workshop | State catalog, docs, and test fixtures | Storybook | Stories and mocks require maintenance; automated a11y is incomplete |
| Motion layer | Transitions, layout animation, gestures | Motion | Extra runtime/API surface; CSS remains preferable for simple effects |
| AI generator | Exploration and first-pass code | v0 with an existing registry/tokens | Output inherits prompt/context gaps and still needs behavior/a11y review |

## Sources

### 1. Base UI: product scope and customization contract

URL:         https://base-ui.com/react/overview/about
Kind:        Primary; Base UI’s own product documentation owns its API and support claims.
Establishes: Base UI is an unstyled React component library from the team behind Radix, Material UI, and Floating UI; it bundles no CSS, is styling-engine agnostic, exposes each part, targets modern “Baseline Widely available” browsers, and supports React 17 and newer.
Paraphrase:  The library is explicitly a behavior-and-structure layer rather than a visual system. Its strongest “custom” evidence is direct access to each rendered node and permission to add, remove, or wrap parts, not merely a theme API. Accessibility and performance statements on this page are vendor claims, not comparative audit results.
Locators:    “About Base UI”; “Unstyled”; “Accessible”; “Customizable”; “Browser support”; “React”.
Quote:       None needed.

### 2. Base UI: accessibility division of responsibility

URL:         https://base-ui.com/react/overview/accessibility
Kind:        Primary; Base UI documents its intended behavior and the work left to consumers.
Establishes: Base UI says it supplies ARIA attributes, roles, pointer/keyboard behavior, and focus management, while implementers must still provide visible focus styling, sufficient contrast, and accessible names or labels where required.
Paraphrase:  “Accessible primitives” is not “the finished component is accessible.” The library handles much of the interaction machinery, but the product team retains visual and content responsibilities and must verify the assembled result.
Locators:    opening paragraphs; “Keyboard navigation”; “Focus management”; “Color contrast”; “Labelling”; “Accessibility testing”.
Quote:       None needed.

### 3. Base UI: composition API

URL:         https://base-ui.com/react/handbook/composition
Kind:        Primary; Base UI owns the render-prop composition contract.
Establishes: A `render` prop can replace a primitive’s rendered element with another element or component. A custom component used there must forward the ref and spread incoming props. A render function receives internal state and permits state-dependent markup.
Paraphrase:  This is the mechanism that gives Base UI more structural freedom than a styled suite, but it transfers a concrete obligation: dropping forwarded props or refs can break behavior. Nested render props are supported, though they can make ownership harder to see.
Locators:    “Custom components”; “Nested components”; “Elements”; “Render functions”.
Quote:       None needed.

### 4. Base UI: Switch documentation and implementation

URL:         https://base-ui.com/react/components/switch
Kind:        Primary; official component documentation owns the public anatomy and usage contract.
Establishes: The documented Switch anatomy is `Switch.Root` plus `Switch.Thumb`; it requires an accessible name, supports an associated `Field.Label`, and renders a hidden checkbox so the value participates in forms. State is available to styles through data attributes and function-valued class names.
Paraphrase:  A compact article example can show `Field.Root`, `Field.Label`, `Switch.Root`, and `Switch.Thumb`, then style checked state with `[data-checked]`. Preserve the label and do not present the visual track alone as a complete accessible example.
Locators:    first code sample; “Anatomy”; “ARIA labelling”; “Native button”; Root API; styling examples.
Quote:       None needed.

URL:         https://github.com/mui/base-ui/blob/master/packages/react/src/switch/root/SwitchRoot.tsx
Kind:        Primary; this is the maintained source implementation, inspected beyond the README/landing page.
Establishes: `SwitchRoot` uses the shared button behavior, sets `role="switch"` and `aria-checked`, carries read-only/required/label relationships, delegates clicks to a hidden checkbox, and merges state through `useRenderElement`.
Paraphrase:  The implementation supports the key architectural claim: the app may replace or style the visible element while Base UI retains the nontrivial switch and form behavior. This also shows why replacing parts carelessly is unsafe—the accessibility and event props must survive composition.
Locators:    `SwitchRoot` implementation; calls to `useButton`, `useFieldRootContext`, `useRenderElement`; hidden input and click/change handling.
Quote:       None needed.

### 5. Base UI: current release activity

URL:         https://base-ui.com/react/overview/releases/v1-8-0
Kind:        Primary; Base UI’s release notes own version/date/change claims.
Establishes: Base UI 1.8.0 was released September 4, 2026. The release includes label association fixes, roving-focus and hover/focus fixes, animation changes, ref/prop fixes, and trigger-performance work.
Paraphrase:  The project has a recent stable release and is still fixing behavior at the interaction layer. That is evidence of maintenance, but also evidence that component semantics continue to evolve and upgrades need tests.
Locators:    page heading and release date; “Fixes and enhancements”.
Quote:       None needed.

### 6. Evidence against “Base UI makes the result accessible”

URL:         https://github.com/mui/base-ui/issues/5659
Kind:        Primary for the reporter’s reproduction, not for a maintainer-confirmed diagnosis; the issue body records a specific test against Base UI 1.8.0 and is labeled “waiting for maintainer.”
Establishes: An open September 10, 2026 report says a high-priority `Toast.Root` can simultaneously be keyboard-focusable and `aria-hidden`; axe flags `aria-hidden-focus`, and the reporter documents the conditions and relevant attributes. The report also says the toast message is still announced by sibling live regions, limiting the severity.
Paraphrase:  This does not prove the entire library inaccessible, and the issue was not yet maintainer-verified when checked. It does defeat any blanket claim that adopting Base UI removes the need for keyboard, accessibility-tree, and screen-reader testing of real composed states.
Locators:    issue state and labels; “Description”; “Reproduction”; “What we expected”; “Notes that may save you time”; “Related”.
Quote:       None needed.

### 7. shadcn/ui: source ownership, Base UI default, and migration warning

URL:         https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default
Kind:        Primary; Shadcn’s official changelog owns the distribution default and the creator’s recommendation.
Establishes: In July 2026 shadcn/ui made Base UI the default primitive for new projects, while retaining Radix as a supported option. The page says Radix is mature and tested, that shadcn still runs it in production, and that existing applications should not migrate merely because the default changed. It also explains that source ownership makes automatic migration unsafe because customized files and behavior differences require review.
Paraphrase:  This is both support and counterevidence. It validates Base UI as a current starting point for new shadcn projects, while explicitly rejecting churn in a working Radix system. Source distribution buys editability at the cost of becoming the maintainer of the copied integration.
Locators:    “Why Base UI”; “What about Radix?”; “Which one should I choose?”; migration discussion.
Quote:       Shadcn, creator of shadcn/ui: “the worst thing you can do for your production app is switch component libraries”. Exact wording and capitalization checked on the official changelog.

### 8. React Aria: the strongest alternative for complex products

URL:         https://react-aria.adobe.com/
Kind:        Primary; Adobe’s React Aria product documentation owns its API surface and vendor testing claims.
Establishes: React Aria documents more than 50 style-free components, individual parts, render props, slots, contexts, and lower-level hooks. It specifically covers drag and drop, keyboard multi-selection, validation, table resizing, adaptive interaction across mouse/touch/keyboard/screen readers, more than 30 languages, 13 calendars, five numbering systems, and RTL.
Paraphrase:  React Aria can be the better behavioral foundation when “custom” includes data-heavy collections, date/calendar work, internationalization, or unusual interaction composition. Its high-level components build a DOM structure; contexts can replace parts; hooks provide the escape hatch with a larger conceptual/API surface.
Locators:    homepage opening and component list; “Customizable”; “Built-in behavior”; “Adaptive interactions”; “International”; “Components”; “Hooks”.
Quote:       None needed.

### 9. Radix Primitives: mature, composable incumbent

URL:         https://www.radix-ui.com/primitives/docs/overview/introduction
Kind:        Primary; Radix’s official documentation owns its API and packaging claims.
Establishes: Radix describes low-level, accessible, unstyled primitives with exposed parts and `asChild` composition. Its unified package is tree-shakeable, and separately versioned packages are released together to avoid duplicate dependencies.
Paraphrase:  Radix remains a credible behavior layer and is especially rational for systems already built on it. `asChild` offers structural control, though Radix’s composition documentation separately makes developers responsible for preserving accessibility when changing the underlying element. Shadcn’s official position is to keep working Radix apps rather than migrate for fashion.
Locators:    “Introduction”; “Accessible”; “Unstyled”; “Open”; “Composition”; “Package structure”.
Quote:       None needed.

### 10. Tailwind: tokens and styling, not behavior

URL:         https://tailwindcss.com/docs/theme
Kind:        Primary; Tailwind’s official v4.3 documentation owns theme-variable behavior.
Establishes: `@theme` variables are design tokens that generate utilities and ordinary CSS variables. Namespaces map tokens to utility families; teams can extend, override, or replace defaults and share a theme CSS file across projects.
Paraphrase:  Tailwind is the constraint and styling layer in the recommended stack. It makes spacing, color, typography, breakpoints, and motion tokens reusable, but supplies none of the focus, keyboard, form, or screen-reader behavior handled by Base UI, React Aria, or Radix.
Locators:    version marker; “What are theme variables?”; “Theme variable namespaces”; “Customizing your theme”; “Sharing across projects”; “Using your theme variables”.
Quote:       None needed.

### 11. Adam Wathan: exact practitioner quotation on composition

URL:         https://adamwathan.me/css-utility-classes-and-separation-of-concerns/
Kind:        Primary; this is Adam Wathan’s own essay and the original text of the quotation.
Establishes: Wathan argues that reusable CSS should be evaluated by dependency direction and by the scope of the component abstraction; highly specific, do-everything components become less reusable.
Paraphrase:  The quotation supports building a system from small behavior primitives, tokens, and product-owned compositions rather than expecting one maximally configurable component to encode every variation.
Locators:    “Extracting components”; paragraph beginning “While these components might be reusable…”. Role verification: https://tailwindcss.com/course identifies “Adam Wathan, Creator of Tailwind CSS.”
Quote:       Adam Wathan, creator of Tailwind CSS: “The more a component does, or the more specific a component is, the harder it is to reuse.” Exact wording and punctuation checked against the first-party essay.

### 12. Storybook: the state catalog and an explicitly incomplete test layer

URL:         https://storybook.js.org/docs
Kind:        Primary; Storybook’s official documentation owns the workflow description.
Establishes: Storybook 10.6 describes itself as an isolated frontend workshop for hard-to-reach states and edge cases; a story captures one rendered component state, can feed documentation, and is a starting point for testing and sharing.
Paraphrase:  A durable custom system needs the states outside the happy-path page: loading, disabled, invalid, focus-visible, long text, reduced motion, RTL, and narrow viewports. Storybook gives those states names and stable fixtures; it does not make the component correct by itself.
Locators:    version marker; “Get started with Storybook”; “Main concepts”.
Quote:       None needed.

URL:         https://storybook.js.org/docs/writing-tests/accessibility-testing
Kind:        Primary for Storybook behavior; it accurately attributes the “up to 57%” figure to Deque, so that figure is not treated as Storybook-owned evidence here.
Establishes: The a11y addon runs axe-core against rendered stories, reports violations, passes, and incomplete checks, can integrate with Vitest, and can fail CI. The docs call automated checks a first line of QA and explicitly identify items that need manual confirmation.
Paraphrase:  Put automated checks in the component loop, but do not equate a green axe panel with screen-reader or keyboard-path verification. The tool’s own results model has an “Incomplete” bucket for manual review.
Locators:    opening explanation; “Install the addon”; “Check for violations”; results sub-tabs; “Test behavior”.
Quote:       None needed.

### 13. Motion: optional polish with a cost boundary

URL:         https://motion.dev/docs/react
Kind:        Primary; Motion’s official documentation owns its animation-engine and API claims.
Establishes: Motion for React covers prop animation, layout, gestures, scrolling, springs, interruptible keyframes, and gesture tracking. Its hybrid engine uses WAAPI and ScrollTimeline when possible and falls back to JavaScript for capabilities native APIs do not provide.
Paraphrase:  Motion belongs after behavior and state architecture, not before it. Use it where interruption, layout, exit orchestration, springs, or gestures justify the dependency; keep simple hover/focus/opacity effects in CSS, and honor reduced-motion settings.
Locators:    “Get started with Motion for React”; “Why Motion for React?”; feature overview; accessibility/reduced-motion navigation.
Quote:       None needed.

### 14. v0: rapid exploration that improves with system context

URL:         https://vercel.com/blog/working-with-figma-and-custom-design-systems-in-v0
Kind:        Primary for Vercel’s product workflow and recommendations; performance claims are vendor claims, not independent benchmarks.
Establishes: Vercel recommends breaking Figma work into smaller components, iterating and testing each part, then composing the pieces. The article says v0 uses shadcn/ui as its default design system, accepts custom Tailwind configuration, and can use public npm packages such as Material UI and React Aria.
Paraphrase:  v0 is most useful after a team can give it primitives, tokens, and examples. Its own guidance favors staged generation and refinement, which supports positioning AI as an exploration/implementation accelerator rather than a substitute for a behavior library or component QA.
Locators:    “Take the iterative approach”; “Working with existing design systems”; captions for the Tailwind configuration example.
Quote:       None needed.

### 15. Empirical check on AI-generated accessibility

URL:         https://arxiv.org/abs/2503.15885
Kind:        Primary research; the four authors own the described comparative experiments, though the arXiv preprint is not evidence of peer review.
Establishes: The study compares GPT-4o and Qwen-generated UI code with human-authored code. It reports strength on basic cases such as contrast and alternative text but persistent difficulty with complex ARIA and dynamic interaction; zero-shot, few-shot, and self-criticism prompting brought limited gains, while an accessibility-feedback loop performed better.
Paraphrase:  Generated markup should enter the same story, interaction, automated-audit, keyboard, and assistive-technology review loop as human code. Better prompts help, but feedback and tests are the mechanism—not model output alone.
Locators:    abstract; submission history; experimental-method sections in the linked HTML/PDF.
Quote:       None needed.

## Contradictions

- Base UI’s about/accessibility pages say the library adheres to WAI-ARIA guidance and is tested across assistive technologies. The current Toast issue reports a specific 1.8.0 state that axe identifies as hiding a focusable element. The issue is still awaiting maintainer review, so report it as an open, reproducible allegation rather than a confirmed systemic defect. The safe conclusion is mandatory product-level testing, not rejection of Base UI.
- The provisional “Base UI is the best foundation” claim fails for some products. React Aria’s documented coverage of rich collections, table resizing, drag and drop, 30+ languages, 13 calendars, and low-level hooks is materially broader. For global, data-dense, or assistive-technology-critical applications, React Aria may be the better default despite its larger conceptual surface.
- shadcn/ui now defaults new projects to Base UI, but its creator explicitly advises against migrating a working Radix application. The article should recommend Base UI for new work only after requirements fit, not manufacture a universal migration story.
- Source-distributed components reduce abstraction lock-in but increase maintenance ownership. The same shadcn changelog says a codemod cannot safely update heavily customized source and that behavior differences need human review. “You own the code” is an advantage and a bill.
- Storybook plus axe provides fast regression feedback, yet Storybook’s own documentation calls it a first line and exposes “Incomplete” checks for manual confirmation. It cannot substantiate a claim of conformance by itself.
- v0’s official workflow recommends small generations, iterative testing, and design-system context. That contradicts any framing of a one-shot generator as a design system or behavior-quality guarantee.

## Numbers

Figure: Base UI 1.8.0 released September 4, 2026.
Owner:  Base UI release notes.
Scope:  The current stable release page checked for this record.

Figure: More than 50 React Aria components.
Owner:  Adobe React Aria homepage.
Scope:  Current component suite claimed on the homepage, not an independently counted audit.

Figure: More than 30 languages, 13 calendar systems, and five numbering systems.
Owner:  Adobe React Aria homepage.
Scope:  React Aria’s current internationalization support claims.

Figure: Storybook documentation version 10.6.
Owner:  Storybook documentation.
Scope:  Version displayed on the docs checked September 22, 2026.

Figure: Automated axe-core checks catch “up to 57%” of WCAG issues.
Owner:  Deque, linked by Storybook; Storybook does not own the underlying test result.
Scope:  Maximum stated by the linked axe-core documentation, not a guarantee for every component. Avoid using unless the Deque source is separately opened for publication.

## Limits

- No independent head-to-head benchmark establishes one overall “best” React UI library. The recommendation is a requirements fit derived from documented capabilities and costs.
- Base UI’s broad accessibility and performance claims are vendor claims. One open issue supplies counterevidence, but this research did not run the reproductions or conduct an independent assistive-technology audit.
- Exact bundle-size comparisons were not established on a common version, bundler, import pattern, and minification/gzip basis. Prefer structural wording: Base UI and Radix advertise tree shaking; Motion adds a runtime when used; Tailwind emits CSS; source-distributed shadcn components still depend on the selected primitives.
- “Beautiful” has no objective metric. Treat shadcn/ui and v0 as visual starting points, then judge against product-specific art direction, content, states, and brand constraints.
- Popularity was established by public roles and official ecosystem position, not ranked by social-follower count. The two exact quotations are first-party text from Shadcn and Adam Wathan.
- Current product/version facts are a September 22, 2026 snapshot and should be rechecked close to publication if publication is delayed.

## Source assets

Asset: Base UI Switch live demo, anatomy diagram/code sample, and state-styling snippets on https://base-ui.com/react/components/switch.
Shows: A minimal primitive has visual parts, accessible labeling, form participation, and styleable state.
Crop:  Retain the rendered switch, label, relevant JSX, and checked-state selector; omit site navigation.

Asset: `SwitchRoot.tsx` source around `useButton`, ARIA props, hidden-checkbox delegation, and `useRenderElement`.
Shows: The behavior underneath the small public API and why refs/props must be preserved.
Crop:  Retain function names and the connected block of implementation; omit unrelated imports and license boilerplate.

Asset: React Aria homepage interaction/device illustrations and component examples.
Shows: The same component adapting across mouse, touch, keyboard, and screen reader plus the breadth of collections and date controls.
Crop:  Retain captions or adjacent headings that identify what the image demonstrates; do not use a decorative device image without the explanatory text.

Asset: Storybook accessibility-panel screenshot in the a11y testing documentation.
Shows: Violations, passes, incomplete results, and component-state testing in the workshop.
Crop:  Retain the panel labels and component under test; omit unrelated browser chrome.

Asset: Tailwind theme documentation code mapping `@theme` variables to generated utilities and CSS custom properties.
Shows: One token definition serving utility classes and ordinary CSS.
Crop:  Retain both the theme declaration and the generated/usage side; omit navigation.

Asset: v0 article diagram showing a large Figma design split into smaller components and the custom Tailwind configuration screenshots.
Shows: Why AI output improves when generation is constrained by modular inputs and system tokens.
Crop:  Retain labels and the full transformation relationship; do not isolate a decorative fragment.

Asset: Base UI 1.8.0 release-note list.
Shows: Recent maintenance concentrated on interaction, focus, labeling, and performance details.
Crop:  Retain release number/date and a representative contiguous fix list.

Asset: None found for the Base UI accessibility overview; the prose division of responsibility is the evidence.
Shows: N/A.
Crop:  N/A.

Asset: None found for the shadcn migration warning; the exact creator quotation and surrounding Radix guidance are the evidence.
Shows: N/A.
Crop:  N/A.

Asset: None found for Adam Wathan’s essay that would carry the argument better than the short exact quotation.
Shows: N/A.
Crop:  N/A.

Asset: None found for the Motion overview that improves on a small live interaction example built for the article.
Shows: N/A.
Crop:  N/A.

Asset: Tables/figures in the linked accessibility-generation paper.
Shows: Experimental comparison of human and model-generated accessibility and the effect of feedback.
Crop:  Retain table/figure number, legend, model/task scope, and metric definitions; do not crop to an isolated favorable score.

## Discarded

URL: https://www.npmjs.com/package/@base-ui/react — rejected for adoption/dependent counts because these are live, unstable snapshots and not needed for the recommendation.

URL: https://github.com/mui/base-ui/issues/3579 — rejected as evidence against adoption because it is a user’s strategic concern about MUI/Joy history, not a maintainer commitment or a demonstrated product defect.

URL: https://github.com/mui/base-ui/issues/5726 — read after a search snippet described a different problem; the actual current issue is an SSR disabled-attribute hydration mismatch and was not the strongest evidence for the accessibility argument.

URL: https://github.com/mui/base-ui/issues/4184 — relevant screen-reader report, but rejected in favor of the newer, more self-contained 1.8.0 Toast reproduction; it also notes that inconsistent NVDA/JAWS behavior may be outside Base UI.

URL: https://github.com/mui/base-ui/issues/4253 — relevant timed-toast concern, but redundant once the current 1.8.0 Toast issue and Base UI’s own division-of-responsibility documentation were recorded.

URL: https://mui.com/blog/base-ui-2024-plans/ — useful project history, rejected because tentative 2024 timing was superseded and does not decide the current recommendation.

URL: https://storybook.js.org/blog/storybook-10-4/ — read for currency, rejected from core evidence because the current docs already display 10.6 and explain the stable workflow; the older release post is useful only for transient agent-setup features.

URL: https://v0.dev/docs/design-systems — fetch failed during this research; the accessible first-party Vercel article supplied the relevant design-system workflow instead.

URL: https://mui.com/material-ui/customization/how-to-customize/ — confirms four override layers, nested slot selectors, state specificity, reusable styled components, and theme overrides, but omitted from the core set to keep the comparison focused. It remains the best primary source if the draft makes detailed claims about styled-suite override friction.

URL: https://mui.com/material-ui/customization/theme-components/ — confirms that the theme is not tree-shakeable and recommends creating new components for heavy customization; omitted unless the final draft specifically contrasts runtime/theme costs.

URL: https://base-ui.com/react/handbook/customization — largely duplicates the more specific composition and styling evidence above.

