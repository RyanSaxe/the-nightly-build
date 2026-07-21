"""A retired component renders the back-catalog but never a new article.

When a component leaves the live catalog its CSS stays in the sheet so frozen
articles keep rendering, and an `@deprecated` marker beside that CSS names its
replacement. The proof reads those markers and blocks a new article that reaches
for retired markup, so a stale shape cannot be copied forward out of the
library. The proof only ever runs on the article being authored, so the block
never touches what is already published.
"""

from collections.abc import Callable

import check
from findings import Findings, findings_of
from press import REPO, mut


def test_a_retired_component_blocks_as_deprecated() -> None:
    rep = check.Report()
    check.check_deprecated(
        '<body class="nb-article"><div class="nb-verdict">x</div></body>',
        repo=str(REPO),
        rep=rep,
    )
    result = findings_of(rep)

    assert "B-DEPRECATED" in result.blocks
    # The block points the author at the live replacement, not just the retiree.
    assert result.blocks.saying("nb-note")


def test_a_retired_subpart_blocks_as_deprecated() -> None:
    rep = check.Report()
    check.check_deprecated(
        '<body class="nb-article"><p class="nb-verdict-title">x</p></body>',
        repo=str(REPO),
        rep=rep,
    )

    assert "B-DEPRECATED" in findings_of(rep).blocks


def test_a_retirement_with_no_replacement_says_remove_it() -> None:
    rep = check.Report()
    check.check_deprecated(
        '<body class="nb-article"><ul class="nb-paper-map">x</ul></body>',
        repo=str(REPO),
        rep=rep,
    )
    result = findings_of(rep)

    assert "B-DEPRECATED" in result.blocks
    assert result.blocks.saying("remove it")


def test_live_components_are_not_deprecated() -> None:
    rep = check.Report()
    check.check_deprecated(
        '<body class="nb-article">'
        '<section class="nb-bookend"><p class="nb-bookend-name">x</p></section>'
        '<div class="nb-note">y</div></body>',
        repo=str(REPO),
        rep=rep,
    )

    assert "B-DEPRECATED" not in findings_of(rep).codes


def test_the_full_proof_blocks_an_article_reaching_for_retired_markup(
    run_local: Callable[..., Findings],
) -> None:
    result = run_local(
        mut("</article>", '<div class="nb-verdict">stale shape</div></article>'),
        "semiconductors",
    )

    assert "B-DEPRECATED" in result.blocks
