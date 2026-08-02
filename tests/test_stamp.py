"""nb stamp owns the computable nb-meta counts.

words, sources, and reading_minutes are properties of the article text; no
agent hand-declares them. Stamping writes the same numbers the proof counts,
touches nothing outside the nb-meta block, and refuses files it cannot
stamp precisely.
"""

import pytest

import stamp
from nb import meta as nb_meta
from press import article


def test_stamp_writes_the_counted_totals() -> None:
    stamped, counts = stamp.stamp_source(article())

    meta = nb_meta.parse_meta(stamped)
    assert meta is not None
    assert meta["words"] == counts["words"] > 0
    assert meta["sources"] == counts["sources"] == 8
    assert meta["reading_minutes"] == counts["reading_minutes"] >= 1


def test_stamp_is_idempotent_and_touches_only_the_meta_block() -> None:
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
