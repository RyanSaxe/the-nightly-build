# Evidence record: expert-tools/beartype (01)

The evidence strongly supports the commission's core mechanism claim. beartype's
distinctive move is real, documented in its own primary sources, and confirmed in
the source tree: it type-checks one *randomly selected* item per nested container
level per call, giving O(1) non-amortized worst-case cost regardless of container
size. Its own default (and, decisively, its *only implemented*) strategy is this
constant-time random sample; the linear-time "check everything" strategy exists in
the enum as `On` but is explicitly unimplemented, so a user cannot ask beartype to
walk a whole container. The limitation the commission wants named is not something
the article must extract against resistance: beartype's own FAQ says the approach
"invites false negatives" and rests on an unproven assumption that real containers
are homogeneous. Where the evidence is *thin*: exact call-time overhead numbers
come from beartype's own micro-benchmarks (self-serving, no independent
reproduction found), the headline typeguard "107 minutes" figure is beartype's own
pathological-case benchmark of a competitor, and GitHub star/download counts read
inconsistently across fetches (recorded as approximate). The one real tension for
the *angle*: beartype is not the only runtime checker that samples containers per
call. typeguard converged on a similar idea in v3 (default = check the *first*
item). beartype's genuine differentiators are that the sample is *random* rather
than positional, that sampling is the only mode, and its decoration-time
code-generation architecture with zero dependencies and broad PEP coverage. The
piece should locate "distinctive" there, not in "checks a sample" alone. beartype
is popular (millions of downloads) but its mechanism is genuinely niche; it does
not read as a familiar default in the sense the series warns against.

## Sources

```text
URL:         https://github.com/beartype/beartype (README) / https://github.com/beartype/beartype/blob/main/README.rst
Kind:        primary. The project's own repository README, authored by the maintainer; owns the tool's self-description and headline claims.
Establishes: The tool's identity ("Unbearably fast near-real-time pure-Python runtime-static type-checker"), the O(1) claim, and a canonical call-boundary violation example.
Paraphrase:  beartype enforces type safety at the granularity of functions and methods against community-standardized type hints "in O(1) non-amortized worst-case time with negligible constant factors." A worked example decorates a function taking list[str]; passing a list whose item 0 is a bytes object raises a beartype violation naming the offending item.
Locators:    Repo tagline; "Synopsis"/quickstart code block; performance blurb.
Quote:       "enforcing type safety at the granular level of functions and methods against type hints standardized by the Python community in O(1) non-amortized worst-case time with negligible constant factors"
             Violation shown: "beartype.roar.BeartypeCallHintParamViolation: @beartyped quote_wiggum() parameter lines=[b'Oh, my God! A horrible plane crash!', ...] violates type hint list[str], as list item 0 value b'Oh, my God! A horrible plane crash!' not str."
```

```text
URL:         https://beartype.readthedocs.io/en/latest/faq/
Kind:        primary. beartype's official FAQ ("Ask a Bear Bro Anything"); the maintainer's own account of the algorithm and its costs.
Establishes: (a) exactly how the random sampling walk works; (b) beartype's own admission of the false-negative limitation and the assumption it rests on; (c) beartype's framed contrast with typeguard and with static checkers.
Paraphrase:  beartype performs "a one-way random tree walk over the expected nested structure" at call time. For a hint like list[tuple[Sequence[str]]] it checks (in order) that the object is a list, that a randomly selected item of that list is a tuple, that a randomly selected item of that tuple is a Sequence, and that a randomly selected item of that sequence is a str. It samples one item per nesting level, so it inspects h items for a container of height h. beartype states plainly that this "invites false negatives" because it checks only "a vertical slice of the full container structure each call," and that it claims false negatives are unlikely only "without evidence" under the "optimistic assumption that most real-world containers are homogeneous." Against typeguard it contrasts checking "every integer nested in that list" (typeguard, historically) versus "only a single random integer" (beartype). Against static checkers it notes those tools "enforce static typing and are thus strongly opinionated," emitting errors on dynamically-typed code, whereas beartype runs on the live objects.
Locators:    FAQ entries on the O(1) algorithm ("random tree walk"), on false negatives, and the typeguard/static-checker comparisons.
Quote:       "beartype performs a one-way random tree walk over the expected nested structure of those objects at call time."
             "beartype also invites false negatives, because this approach only checks a vertical slice of the full container structure each call, which is bad."
             "We claim without evidence that false negatives are unlikely under the optimistic assumption that most real-world containers are homogeneous (i.e., contain only items of the same type)."
```

```text
URL:         https://beartype.readthedocs.io/en/latest/api_decor/  (BeartypeStrategy) ; source: https://github.com/beartype/beartype/blob/main/beartype/_conf/confenum.py
Kind:        primary. Official API docs plus the enum's own source definition.
Establishes: beartype exposes four strategies via BeartypeConf.strategy: O0 (no-op identity decorator), O1 (default, one random item per container), Ologn (log-many items), On (all items). Decisively: On and Ologn are NOT implemented. So random sampling is not merely the default, it is the only container-depth mode a user can actually select today.
Paraphrase:  The BeartypeStrategy enum defines O0, O1, Ologn, On. O1 is "the default O(1) strategy, type-checking a single randomly selected item of each container." On is "the O(n) strategy, type-checking all items of a container" and is "currently unimplemented" (docs add it is to be implemented "by a future beartype release"). Ologn is likewise reserved and unimplemented. A user changes strategy by passing BeartypeConf(strategy=...) as the conf parameter to @beartype.
Locators:    api_decor "BeartypeStrategy" section; confenum.py class BeartypeStrategy(Enum) with members O0/O1/Ologn/On and their docstrings.
Quote:       O1 docstring: "Constant-time strategy (i.e., the default O(1) strategy, type-checking a single randomly selected item of each container)."
             On docstring: "Linear-time strategy (i.e., the O(n) strategy, type-checking *all* items of a container). This strategy is **currently unimplemented.**"
```

```text
URL:         https://github.com/beartype/beartype/blob/main/beartype/_check/code/codemain.py
Kind:        primary. Source of the type-check code factory.
Establishes: The random index used to pick a container item is drawn from Python's standard-library random.getrandbits, injected into the generated wrapper only when a hint actually needs a random pick.
Paraphrase:  The module imports getrandbits from the random module and, when the generated hint tree "is_var_random_int_needed," binds getrandbits into the wrapper function's local namespace (ARG_NAME_GETRANDBITS). The per-item random selection expression itself is emitted by the container code-generation submodules under beartype._check.code, not this factory file.
Locators:    Import "from random import getrandbits"; conditional "if hint_tree.is_var_random_int_needed: hint_tree.func_wrapper_locals[ARG_NAME_GETRANDBITS] = getrandbits".
Quote:       "from random import getrandbits"
```

```text
URL:         https://beartype.readthedocs.io/en/latest/pep/
Kind:        primary. beartype's own PEP-compliance feature matrix.
Establishes: Where hint coverage is full, partial, or absent. Full support includes PEP 484 (type hints), 585 (builtin generics), 544 (Protocols), 586 (Literal), 593 (Annotated), 604 (X | Y unions), 673 (Self), 695 (type-parameter syntax). Partial support includes PEP 589 (TypedDict), 591 (Final), 612 (ParamSpec), 646 (TypeVarTuple, partial since 0.22.0), 557 (dataclasses), 435 (Enum). Listed with no support include PEP 698 (@override), 705 (ReadOnly TypedDict), 747 (TypeVar defaults / TypeForm).
Paraphrase:  beartype covers the mainstream annotation surface fully and marks several advanced constructs as partial or unimplemented. Variadic generics (PEP 646) are only partially supported; TypedDict and ParamSpec are partial; some newer PEPs are unsupported. This is the concrete "hint coverage thins" list the commission asks for, from the primary that owns it.
Locators:    "Full", "Partial", and "None/unsupported" rows of the PEP support table, each with the version the status began.
Quote:       (matrix statuses as above; e.g. PEP 646 TypeVarTuple listed "Partial support from 0.22.0-current"; PEP 589 TypedDict "Partial".)
```

```text
URL:         https://beartype.readthedocs.io/en/latest/eli5/
Kind:        primary. beartype's "explain like I'm five" positioning doc.
Establishes: Zero dependencies; the runtime-vs-static positioning; decoration-time code generation as the cost model; a second violation example.
Paraphrase:  "Beartype has no install-time or runtime dependencies." Unlike static checkers, beartype "operates exclusively at the fine-grained callable level of pure-Python functions and methods via the standard decorator design pattern" and "enjoys deterministic Turing-complete access to the actual callables, objects, and types being type-checked." Cost is front-loaded: "Thanks to aggressive memoization and dynamic code generation at decoration time, beartype guarantees O(1) non-amortized worst-case runtime complexity with negligible constant factors." A shown example: calling a function with a bytes argument where str is annotated raises BeartypeCallHintPepParamException naming the offending value.
Locators:    eli5 dependency statement; "Unlike static type-checkers" contrast; decoration/memoization statement; violation code block.
Quote:       "Beartype has no install-time or runtime dependencies."
             "Beartype enjoys deterministic Turing-complete access to the actual callables, objects, and types being type-checked."
```

```text
URL:         https://beartype.readthedocs.io/en/latest/api_roar/
Kind:        primary. beartype's exception/warning reference.
Establishes: The exception hierarchy beartype raises at a failed call-boundary check. Root BeartypeException; call-time failures are BeartypeCallHintViolation subclasses (the docs call BeartypeCallHintViolation "the most important beartype exception"). Parameter vs return violations follow the naming pattern BeartypeCallHintParamViolation / BeartypeCallHintReturnViolation.
Paraphrase:  All beartype exceptions subclass BeartypeException. Decoration-time errors subclass BeartypeDecorException; call-time type-check failures subclass BeartypeCallException -> BeartypeCallHintException -> BeartypeCallHintViolation. The violation object names the object, the hint, and the specific failing item.
Locators:    Class descriptions for BeartypeException, BeartypeCallHintViolation, BeartypeCallHintForwardRefException, and the PEP585 deprecation warning.
Quote:       BeartypeCallHintViolation: "This is the most important beartype exception. Beartype type-checkers raise an instance of this exception class when an object to be type-checked violates the type hint annotating that object."
```

```text
URL:         https://beartype.readthedocs.io/en/latest/api_claw/
Kind:        primary. beartype's import-hook ("claw") API reference.
Establishes: How beartype enters a codebase without hand-decorating every function, i.e. the realistic adoption path. beartype_this_package() type-checks all annotated callables, classes, and variable assignments across the current package's submodules; beartype_package()/beartype_packages() target named packages; beartype_all() covers everything and is discouraged.
Paraphrase:  Import hooks "implicitly decorate all callables and classes" at import time and add checks to annotated variable assignments, so a single call in a package __init__.py enforces hints project-wide. beartype_all() "type-checks all callables, classes, and variable assignments across all submodules of all packages," and the docs warn "most codebases should not call this hook."
Locators:    claw API entries for beartype_this_package, beartype_package, beartype_packages, beartype_all.
Quote:       beartype_this_package example: "from beartype.claw import beartype_this_package\nbeartype_this_package()"
             "most codebases should not call this hook" (re: beartype_all).
```

```text
URL:         https://pypi.org/project/beartype/
Kind:        primary. The package's own PyPI listing (release/packaging metadata).
Establishes: Current stable version, release date, minimum Python, license, maintainer.
Paraphrase:  Latest stable release is beartype 0.22.9, released 2025-12-13. requires-python is ">=3.10". License is MIT. Maintainer/author listed as Cecil Curry. (Note: docs at readthedocs "latest" are built from the 0.23.0 line, which is in release-candidate, see releases below.)
Locators:    PyPI project header (version + date); "Requires: Python >=3.10"; license classifier; author field.
Quote:       "0.22.9" ; "released December 13, 2025" ; "Requires: Python >=3.10" ; MIT.
```

```text
URL:         https://github.com/beartype/beartype/releases
Kind:        primary. The project's release history.
Establishes: Release cadence and maintenance activity, and that 0.23.0 is a release candidate. 0.20.0 (Feb 2025), 0.20.1/0.20.2 (Mar 2025), 0.21.0 (May 2025), then the 0.22.x line through 0.22.9 (Dec 2025), plus 0.23.0rc0 as a pre-release. Roughly monthly point releases across 2025.
Paraphrase:  Many point releases within a single year indicate active maintenance. Recent notes: 0.22.9 marks a "one million daily downloads" milestone and adds PyInstaller bundling support plus preliminary compatibility with Astral's "ty" type-checker; 0.22.8 fixes a synchronous-generator return regression introduced in 0.22.6; 0.23.0rc0 adds warn_if_beartype_claw_inactive() to detect when import hooks are silently disabled by tools like PyInstaller/jaxtyping. (Some month/year labels in the rendered release page were unreliable in fetch; the 0.22.9 date is taken from PyPI, above.)
Locators:    Releases list; individual release note bodies for 0.22.6-0.22.9 and 0.23.0rc0.
Quote:       Milestone described in 0.22.9 notes: "one million daily downloads."
```

```text
URL:         https://github.com/beartype/beartype/issues
Kind:        primary. The project's issue tracker; primary for real limitations and maintenance signal.
Establishes: ~108 open issues at time of reading; the themes are advanced-hint gaps and edge cases, not the tool being broken for mainstream use. Concrete limitation examples: #641 @dataclass descriptor-typed fields raise errors despite passing pyright; #644 class-variable defaults are not runtime type-checked; #628 PEP 747 support requested for mypy compatibility; #639 request for a context manager to temporarily disable checks; #636 recursion guards for recursive type-checking.
Paraphrase:  Open issues cluster on expanded hint support, edge-case correctness, and ergonomics rather than core failure. This corroborates the "handles standard cases; struggles at advanced/edge constructs" reading from the PEP matrix.
Locators:    Open issues #641, #644, #628, #639, #636, plus documentation issues #657/#664.
Quote:       (issue titles as paraphrased; e.g. #641 concerns dataclass descriptor-typed fields erroring though pyright passes.)
```

```text
URL:         https://typeguard.readthedocs.io/en/stable/userguide.html  and  https://typeguard.readthedocs.io/en/latest/versionhistory.html
Kind:        primary (for typeguard). typeguard's own user guide and changelog; owns typeguard's runtime behavior.
Establishes: The precise typeguard comparison. typeguard instruments code by rewriting the AST (it "fetches the source code, parsing it to an abstract syntax tree using ast.parse()"), applied via @typechecked, the check_type() function, or an install-time import hook. Since typeguard 3.x, collection checking defaults to CollectionCheckStrategy.FIRST_ITEM (check only the first item); CollectionCheckStrategy.ALL_ITEMS restores exhaustive checking. So typeguard, like beartype, samples per call by default, but its sample is the deterministic first item, not a random item, and ALL_ITEMS is available (beartype's On is not).
Paraphrase:  typeguard's default is to check a container's first item only; the old exhaustive behavior is opt-in via ALL_ITEMS. typeguard rewrites the AST rather than generating a wrapper by string code-gen, and its decorator "will not work when there is another decorator wrapping the function" (must be innermost). An open typeguard PR (#516) proposes restoring ALL_ITEMS as the default.
Locators:    userguide: "@typechecked", "check_type", AST-parse description, innermost-decorator warning; versionhistory: 3.0 note introducing CollectionCheckStrategy with FIRST_ITEM default.
Quote:       userguide: check_type described as "a beefed-up version of isinstance()"; decorator warning: "You should always place this decorator closest to the original function, as it will not work when there is another decorator wrapping the function."
             versionhistory (paraphrase): collection checking changed to check only the first item by default; set collection_check_strategy to CollectionCheckStrategy.ALL_ITEMS for the old behavior.
```

```text
URL:         https://docs.pydantic.dev/latest/concepts/validation_decorator/  (redirects to https://pydantic.dev/docs/validation/latest/concepts/validation_decorator/)
Kind:        primary (for pydantic). pydantic's official docs; owns pydantic's runtime behavior.
Establishes: The precise pydantic comparison. pydantic's @validate_call coerces before it checks and validates every item, not a sample. It is a data-validation/parsing library, not a type sampler.
Paraphrase:  "types are by default coerced by the decorator before they're passed to the actual function," e.g. '2000-01-01' becomes a date, '4' becomes int 4. Each argument (including each variadic item) is validated individually, not sampled. This is categorically different work from beartype: pydantic parses and transforms untrusted input (and, for models, requires defining a BaseModel or using validate_call); beartype asserts that in-program values already match hints and changes nothing.
Locators:    validation_decorator page: coercion statement; *args: int example validating each of 1, 2, 3.
Quote:       "types are by default coerced by the decorator before they're passed to the actual function"
```

## Contradictions

- Beartype is not uniquely a per-call sampler. The commission frames "checks a
  random sample rather than walking the whole structure" as the distinctive
  mechanism. typeguard's own docs show that since v3 it also checks only one item
  per collection by default (`CollectionCheckStrategy.FIRST_ITEM`). The honest
  distinction is narrower and sharper: beartype samples a *random* item (typeguard
  the *first*), beartype's whole-container mode (`On`) is *unimplemented* so
  sampling is the only option (typeguard offers `ALL_ITEMS`), and beartype
  generates a wrapper by string code-gen at decoration time (typeguard rewrites the
  AST). The article's "distinctive" should sit on random-only sampling plus the
  code-generation/zero-dependency architecture, not on "samples instead of walks."

- Self-serving benchmarks. The dramatic figures (beartype ~1µs to "type-check"
  a million-item list; typeguard "107 minutes" worst case; beartype 13.8µs on the
  same pathological input) all originate in beartype's own README/FAQ. They compare
  a single random-sample check against typeguard's exhaustive walk of a
  deliberately pathological triply-nested structure. They are directionally
  informative but are beartype marketing its own competitor comparison; no
  independent reproduction was found. Treat as beartype's claim, not settled fact.

- "O(1)" describes per-call container-depth cost, not zero cost and not whole-
  program guarantee. beartype front-loads work to decoration time (code-gen +
  memoization) and still executes a real wrapper on every call. The O(1) refers to
  independence from container *size*, not the absence of overhead; nested depth h
  still costs h checks per call.

- Marketing vs. self-documented limitation. The tagline "runtime-static
  type-checker" and "type safety" could read as a guarantee. beartype's own FAQ
  contradicts an over-read: random sampling "invites false negatives" and the
  claim that they are rare is made "without evidence." The overstatement and its
  correction live in the same project's primary sources; the piece should quote the
  FAQ against the tagline rather than sourcing the caveat to a third party.

- Version/Python-support drift in secondary summaries. Some older README code
  examples reference Python 3.9; the current packaging metadata requires >=3.10.
  Use the PyPI/pyproject figure (>=3.10). Rendered GitHub star counts and the
  readthedocs "live version" both read inconsistently across fetches (see Numbers);
  do not cite a precise star count as fact.

- "Too mainstream" test. beartype has millions of downloads and its own release
  notes claim a "one million daily downloads" milestone, which is not obscure. But
  the series bar is about *mechanism distinctiveness*, and random-only O(1)
  sampling with decoration-time code-gen is genuinely niche work most practitioners
  have never adopted. The evidence does not undermine the commission on this axis;
  it does mean the piece should not sell beartype as unknown.

## Numbers

```text
Figure: 0.22.9 (current stable release)
Owner:  PyPI project page for beartype (project's own release metadata)
Scope:  Latest stable as of 2025-12-13; 0.23.0 is in release-candidate (0.23.0rc0).
```

```text
Figure: Released 2025-12-13 (0.22.9)
Owner:  PyPI project page for beartype
Scope:  Release date of current stable.
```

```text
Figure: requires-python >= 3.10
Owner:  beartype pyproject.toml / PyPI "Requires" field
Scope:  Minimum supported CPython for the current line; 3.10 through current releases.
```

```text
Figure: 4 strategies defined (O0, O1, Ologn, On); only O0 and O1 usable, On and Ologn unimplemented
Owner:  beartype/_conf/confenum.py (BeartypeStrategy) and api_decor docs
Scope:  Container-depth checking modes; O1 (random single item) is default and the only container-sampling mode implemented.
```

```text
Figure: h checks per call for a container of nesting height h
Owner:  beartype FAQ ("one-way random tree walk"; one random item per nesting level)
Scope:  Per-call cost is independent of the number of items at each level (O(1) in width), linear only in nesting depth.
```

```text
Figure: ~1 microsecond claimed; 36.7 microseconds measured wall time
Owner:  beartype README/FAQ self-benchmark
Scope:  Time to type-check one access into a list of one million 2-tuples of NumPy arrays; beartype's own micro-benchmark, unreplicated independently.
```

```text
Figure: typeguard ~6420 s (about 107 minutes) worst case vs beartype 13.8 microseconds, same input
Owner:  beartype FAQ self-benchmark (comparison of a competitor)
Scope:  A deliberately pathological deeply/widely nested list; typeguard walking all items exhaustively vs beartype's single random-path check. Self-serving; not independent.
```

```text
Figure: ~108 open issues
Owner:  beartype GitHub issue tracker
Scope:  Open issues at time of reading; themes are advanced-hint support and edge cases, not core breakage.
```

```text
Figure: "one million daily downloads" (milestone claim); ~46M total PyPI downloads (secondary analytics)
Owner:  beartype 0.22.9 release notes (daily-downloads claim, primary); ClickPy analytics (total, secondary, page returned 403 on direct fetch)
Scope:  Adoption signal. Daily figure is the project's own claim; total is from a third-party analytics dashboard not directly verifiable in this pass.
```

```text
Figure: GitHub stars ~3.5k (approximate; read as 1.9k in one fetch, 3.5k in another); ~81 forks
Owner:  beartype GitHub repository header
Scope:  Popularity signal only. Recorded as approximate because rendered counts were inconsistent across fetches; do not cite a precise figure.
```

```text
Figure: Single primary maintainer (Cecil Curry, GitHub @leycec); zero install/runtime dependencies; MIT license
Owner:  PyPI author field; beartype eli5 docs (dependencies); LICENSE/classifier (MIT)
Scope:  Bus-factor and trust assessment: active but concentrated on one maintainer; no dependency supply-chain surface.
```

## Runnable example material

All examples target beartype on Python 3.10+. Outputs marked "quoted" are from
beartype's own docs; outputs marked "illustrative" describe documented behavior
for an example constructed here (not a captured REPL session).

Example A - a bug static typing misses at runtime, caught at the call boundary.
mypy/pyright check this at author time only; if the bad value arrives from
untyped data (JSON, a DB row, a third-party return), no static checker fires at
runtime. beartype does.

```python
from beartype import beartype

@beartype
def total_words(lines: list[str]) -> int:
    return sum(len(line.split()) for line in lines)

# Comes from an untyped boundary (e.g. json.load), so mypy saw nothing wrong here:
payload = [b"first line", "second line"]   # a bytes slipped in at index 0
total_words(payload)
# illustrative (matches documented violation shape):
# beartype.roar.BeartypeCallHintParamViolation: Function total_words()
# parameter lines=[b'first line', 'second line'] violates type hint list[str],
# as list index 0 item b'first line' not instance of str.
```

The canonical README violation (quoted, verbatim shape) makes the same point:

```text
beartype.roar.BeartypeCallHintParamViolation: @beartyped quote_wiggum()
parameter lines=[b'Oh, my God! A horrible plane crash!', ...] violates type
hint list[str], as list item 0 value b'Oh, my God! A horrible plane crash!'
not str.
```

Example B - what random sampling can and cannot promise. beartype checks one
random item per level per call. A single bad item in a large otherwise-valid
list is caught only if that item is the one sampled on a given call, so it may
pass some calls and fail others; a fully homogeneous-but-wrong list is caught
every call.

```python
from beartype import beartype

@beartype
def mean(xs: list[float]) -> float:
    return sum(xs) / len(xs)

good = [1.0, 2.0, 3.0]
mean(good)                      # passes: sampled item is a float

one_bad = [1.0, 2.0, "3.0"] + [0.0]*10_000   # one str hidden among floats
mean(one_bad)                   # illustrative: MAY pass on calls that sample a
                                # float; raises only when the random sample lands
                                # on the str. This is the documented false
                                # negative: "checks a vertical slice ... each call".
```

This is the concrete anchor for the commission's "where the guarantee thins":
beartype's default and only container mode trades completeness for O(1) cost, and
its own FAQ says so.

Example C - the whole-codebase entry point (not a setup tutorial, one line).
Instead of decorating every function, a package enforces hints project-wide from
its __init__.py:

```python
# yourpackage/__init__.py
from beartype.claw import beartype_this_package
beartype_this_package()   # every annotated callable/class in this package is now checked
```

Example D - the three tools doing three different jobs at runtime, on the same
annotation `x: int`:

```text
static (mypy/pyright): checks nothing at runtime; flags mismatches only when you run the checker at author time.
beartype     @beartype:      asserts x is already an int; passing "3" raises BeartypeCallHintParamViolation; value unchanged.
typeguard    @typechecked:   asserts x is an int (first item only for collections by default); passing "3" raises TypeCheckError; value unchanged.
pydantic     @validate_call: COERCES "3" -> 3 and passes it on; validates/parses every item; a genuine non-int raises ValidationError.
```

## Source assets

```text
Asset: The BeartypeStrategy enum block in beartype/_conf/confenum.py showing O0/O1/Ologn/On with the "currently unimplemented" docstring on On.
Shows: That random O(1) sampling is not just the default but the only implemented container mode; the "walk everything" option does not exist yet.
Crop:  Must retain the O1 docstring line and the On "currently unimplemented" line together. Omit surrounding enum-machinery imports.
```

```text
Asset: The FAQ paragraph pairing the "one-way random tree walk" description with the "invites false negatives ... homogeneous ... without evidence" admission.
Shows: The mechanism and its self-documented limitation in the project's own words, side by side.
Crop:  Keep both the walk description and the false-negative admission; do not crop to only the flattering half.
```

```text
Asset: A beartype violation traceback (README/eli5), e.g. the list[str]/bytes example.
Shows: What a caught call-boundary bug actually looks like to a developer, including that the message names the specific failing item.
Crop:  Retain the hint (list[str]) and the offending item identifier; the fictional function name is incidental.
```

```text
Asset: The PEP support matrix rows (pep.md) segmented Full / Partial / None.
Shows: Exactly where hint coverage is complete versus thin (e.g. TypedDict/ParamSpec/TypeVarTuple partial; some newer PEPs absent).
Crop:  A table is better than prose here. Keep the status and the PEP number/name columns; the "since version" column is optional context.
```

```text
Asset: The releases timeline across 2025 (0.20.0 -> 0.22.9, plus 0.23.0rc0).
Shows: Active, roughly monthly maintenance from a single maintainer - the trust signal.
Crop:  Keep version + date; if a chart, label the axis and note the source is the GitHub releases page.
```

## Discarded

```text
URL: https://www.pistack.xyz/posts/2026-07-02-python-type-checkers-mypy-pyright-pyre-pytype-beartype/  -> secondary blog roundup; useful orientation but owns none of the claims; superseded by beartype's own docs and source.
URL: https://github.com/yyolk/beartype  -> a fork/mirror, not the canonical repo; identity claims belong to beartype/beartype.
URL: https://pypi.org/project/beartype/0.10.1/ , /0.7.1/ , /0.9.1/  -> stale version pages; current version taken from the main PyPI project page.
URL: https://clickpy.clickhouse.com/dashboard/beartype  -> third-party download analytics; returned HTTP 403 on direct fetch, total-downloads figure not primary-verifiable, recorded only as a soft secondary signal.
URL: https://github.com/beartype/beartype/issues/7  ("The Future Sound of Beartype")  -> historical design-vision thread; interesting but not needed to establish current mechanism or limitations, which the docs/source settle directly.
```
