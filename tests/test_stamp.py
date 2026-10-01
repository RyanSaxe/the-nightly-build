"""nb stamp owns the publication date and computable nb-meta counts.

words, sources, and reading_minutes are properties of the article text; no
agent hand-declares them. Stamping writes the same numbers the proof counts,
projects reading time into the standard byline, and refuses files it cannot
stamp precisely.
"""

import datetime as dt
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


@pytest.mark.parametrize(
    "old_date", ["2026-01-01", "2099-12-31", "wrong-date", "2026-02-30"]
)
def test_stamp_overwrites_agent_supplied_publication_date(old_date) -> None:
    source = article().replace('"date": "2026-07-06"', f'"date": "{old_date}"')

    stamped, counts = stamp.stamp_source(source, today=dt.date(2026, 10, 1))

    metadata = nb_meta.parse_meta(stamped)
    assert metadata is not None and metadata["date"] == "2026-10-01"
    assert counts == stamp.computed_counts(stamped)
    original = nb_meta.parse_meta(source)
    assert original is not None and original["date"] == old_date


@pytest.mark.parametrize("template", TEMPLATES, ids=lambda path: path.parent.name)
def test_stamp_sets_the_template_metadata_and_byline_date(template) -> None:
    source = template.read_text()
    source = source.replace(
        "</header>", "<p>2026-01-01 outside the byline.</p></header>", 1
    )

    stamped, counts = stamp.stamp_source(source, today=dt.date(2026, 10, 1))

    metadata = nb_meta.parse_meta(stamped)
    assert metadata is not None and metadata["date"] == "2026-10-01"
    assert "<span>2026-10-01</span>" in stamped
    assert "<p>2026-01-01 outside the byline.</p>" in stamped
    assert "YYYY-MM-DD</span>" not in stamped
    assert counts == stamp.computed_counts(stamped)


def test_stamp_uses_the_utc_clock(monkeypatch) -> None:
    class Clock(dt.datetime):
        @classmethod
        def now(cls, tz=None):
            assert tz is dt.timezone.utc
            # UTC has advanced to tomorrow while New York is still September 30.
            return cls(2026, 10, 1, 0, 30, tzinfo=tz)

    monkeypatch.setattr(stamp.dt, "datetime", Clock)

    stamped, _ = stamp.stamp_source(article())

    metadata = nb_meta.parse_meta(stamped)
    assert metadata is not None and metadata["date"] == "2026-10-01"


def test_revision_preserves_original_date_and_refreshes_counts() -> None:
    source = article().replace(
        "</header>",
        '<div class="nb-byline"><span>N min read</span><span>YYYY-MM-DD</span></div></header>',
        1,
    )

    stamped, counts = stamp.stamp_source(
        source, today=dt.date(2026, 10, 1), revision=True
    )

    metadata = nb_meta.parse_meta(stamped)
    assert metadata is not None and metadata["date"] == "2026-07-06"
    assert "<span>2026-07-06</span>" in stamped
    assert counts == stamp.computed_counts(stamped)


def test_stamp_refreshes_date_when_restamped_on_a_later_day() -> None:
    first, _ = stamp.stamp_source(article(), today=dt.date(2026, 9, 30))
    second, _ = stamp.stamp_source(first, today=dt.date(2026, 10, 1))
    same_day, _ = stamp.stamp_source(second, today=dt.date(2026, 10, 1))

    metadata = nb_meta.parse_meta(second)
    assert metadata is not None and metadata["date"] == "2026-10-01"
    assert same_day == second


@pytest.mark.parametrize("date", ["not-a-date", "2026-02-30", "20260706"])
def test_revision_refuses_an_invalid_original_date(date) -> None:
    source = article().replace('"date": "2026-07-06"', f'"date": "{date}"')

    with pytest.raises(ValueError, match="revision nb-meta date"):
        stamp.stamp_source(source, revision=True)


def test_stamp_cli_prints_the_written_date(tmp_path, capsys) -> None:
    target = tmp_path / "piece.html"
    target.write_text(article())

    assert stamp.main([str(target), "--today", "2026-10-01"]) == 0

    assert "date=2026-10-01" in capsys.readouterr().out
    metadata = nb_meta.read_meta(str(target))
    assert metadata is not None and metadata["date"] == "2026-10-01"


def test_revision_cli_preserves_the_publication_date(tmp_path) -> None:
    target = tmp_path / "piece.html"
    target.write_text(article())

    assert stamp.main([str(target), "--revision", "--today", "2026-10-01"]) == 0

    metadata = nb_meta.read_meta(str(target))
    assert metadata is not None and metadata["date"] == "2026-07-06"


def test_stamp_refuses_a_missing_date_without_writing(tmp_path) -> None:
    target = tmp_path / "piece.html"
    source = article().replace('"date":', '"event_date":', 1)
    target.write_text(source)

    assert stamp.main([str(target)]) == 2
    assert target.read_text() == source
