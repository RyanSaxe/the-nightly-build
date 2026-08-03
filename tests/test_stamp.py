"""nb stamp owns the computable nb-meta counts.

words, sources, and reading_minutes are properties of the article text; no
agent hand-declares them. Stamping writes the same numbers the proof counts,
projects reading time into the standard byline, and refuses files it cannot
stamp precisely.
"""

import pathlib

import pytest

import stamp
from nb import meta as nb_meta
from press import article

TEMPLATES = sorted(
    (pathlib.Path(__file__).parents[1] / "templates").glob("*/skeleton.html")
)


def test_stamp_writes_the_counted_totals() -> None:
    stamped, counts = stamp.stamp_source(article())

    meta = nb_meta.parse_meta(stamped)
    assert meta is not None
    assert meta["words"] == counts["words"] > 0
    assert meta["sources"] == counts["sources"] == 8
    assert meta["reading_minutes"] == counts["reading_minutes"] >= 1


@pytest.mark.parametrize("template", TEMPLATES, ids=lambda path: path.parent.name)
def test_stamp_writes_shipped_template_reading_time(template: pathlib.Path) -> None:
    stamped, counts = stamp.stamp_source(template.read_text(encoding="utf-8"))

    assert "N min read" not in stamped
    assert f"<span>{counts['reading_minutes']} min read</span>" in stamped


def test_stamp_refreshes_reading_time_after_the_article_changes() -> None:
    source = article().replace(
        "</header>",
        "<p>N min read outside the byline.</p>\n"
        '<div class="nb-byline">\n<span>N min read</span>'
        "<span>2026-07-06</span>\n</div>\n</header>",
        1,
    )
    stamped, before = stamp.stamp_source(source)
    expanded = stamped.replace("</article>", f"<p>{'word ' * 1000}</p></article>", 1)

    restamped, after = stamp.stamp_source(expanded)

    assert after["reading_minutes"] > before["reading_minutes"]
    assert f"<span>{after['reading_minutes']} min read</span>" in restamped
    assert "<p>N min read outside the byline.</p>" in restamped


def test_stamp_is_idempotent_and_preserves_unrelated_markup() -> None:
    source = article()
    stamped, _ = stamp.stamp_source(source)

    again, _ = stamp.stamp_source(stamped)
    assert again == stamped

    m_before = nb_meta.META_RE.search(source)
    m_after = nb_meta.META_RE.search(stamped)
    assert m_before is not None and m_after is not None
    assert source[: m_before.start(1)] == stamped[: m_after.start(1)]
    assert source[m_before.end(1) :] == stamped[m_after.end(1) :]


def test_stamp_refuses_an_article_without_nb_meta() -> None:
    with pytest.raises(ValueError, match="no readable nb-meta block"):
        stamp.stamp_source("<html><body><p>plain page</p></body></html>")


def test_stamp_names_missing_count_keys() -> None:
    source = article().replace('"words":', '"weight":', 1)

    with pytest.raises(ValueError, match="words"):
        stamp.stamp_source(source)


def test_stamp_cli_writes_in_place(tmp_path) -> None:
    target = tmp_path / "piece.html"
    target.write_text(article(), encoding="utf-8")

    assert stamp.main([str(target)]) == 0
    meta = nb_meta.read_meta(str(target))
    assert meta is not None and meta["sources"] == 8
