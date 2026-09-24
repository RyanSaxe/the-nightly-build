# Furniture

Furniture is reusable article markup with a defined communicative purpose: a
timeline, table, figure, pull quote, rubric, or other reading aid. A component
belongs in an article when it makes specific information easier to understand
than prose would. Start with `templates/FURNITURE.md`, the shipped catalog. Its
components work in every template, and most papers never need more.

Templates, themes, and furniture divide the visual work. The template fixes an
article's structure, the theme sets the paper-wide color tokens, and furniture
supplies the reusable components inside the structure. All three are yours to
define in `press/`.

When your paper does need its own component, decide the scope first. Shared
press furniture under `press/furniture/` serves several series. A component
whose meaning depends on one template belongs inside that template's package.

Design furniture with your assistant from the information readers need. Check
the shared catalog before adding a new component. Compare candidates with real
article content in the browser, including a phone width and both themes. A
finished component gets a catalog entry, a stylesheet, and a sample page, and
holds up without JavaScript, on a phone, in both themes, and for screen readers.

The [Furniture reference](../../reference/furniture.md) has the package layout,
the catalog contract, the gallery command, external libraries with Subresource
Integrity, and the class-inventory check.
