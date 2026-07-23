"""The article copies the builder dresses, and the assets they link.

These tests keep generated article pages aligned with the rest of the site.
They also protect canonical library files from build-time changes and verify
that shared assets use one cache stamp at every page depth.
"""

import pathlib

import pytest

import build_site
from pages import Site, asset_stamp_of, undress
from press import article


@pytest.fixture
def micron_copy(full_site: Site) -> str:
    return full_site.read("library", "semiconductors", "micron.html")


@pytest.mark.parametrize(
    "asset",
    [
        "apple-touch-icon.png",
        "favicon-32.png",
        "favicon-64.png",
        "nb.js",
        "nb.css",
        "theme.css",
        "themes/newspaper.css",
    ],
)
def test_the_assets_are_copied(full_site: Site, asset: str) -> None:
    assert pathlib.Path(full_site.out, "assets", asset).is_file()


def test_an_article_copy_gets_a_cache_busting_stamp(micron_copy: str) -> None:
    assert asset_stamp_of(micron_copy)


def test_chrome_pages_carry_the_same_stamp(full_site: Site, micron_copy: str) -> None:
    assert f"assets/nb.css?v={asset_stamp_of(micron_copy)}" in full_site.index


@pytest.mark.parametrize(
    ("relation", "type_attr", "size", "filename"),
    [
        ("icon", ' type="image/png"', "32x32", "favicon-32.png"),
        ("icon", ' type="image/png"', "64x64", "favicon-64.png"),
        ("apple-touch-icon", "", "180x180", "apple-touch-icon.png"),
    ],
)
def test_generated_pages_and_articles_use_the_site_icons(
    full_site: Site,
    micron_copy: str,
    *,
    relation: str,
    type_attr: str,
    size: str,
    filename: str,
) -> None:
    stamp = asset_stamp_of(micron_copy)

    root_tag = (
        f'<link rel="{relation}"{type_attr} sizes="{size}" '
        f'href="assets/{filename}?v={stamp}">'
    )
    article_tag = root_tag.replace('href="assets/', 'href="../../assets/')

    assert root_tag in full_site.index
    assert article_tag in micron_copy


def test_an_article_copy_wears_the_site_bar(micron_copy: str) -> None:
    assert '<header class="nb-bar">' in micron_copy
    assert '<a href="../../series/">Sections</a>' in micron_copy
    assert "The whole newspaper" in micron_copy


def test_an_article_copy_wears_the_footer_and_the_appearance_toggle(
    micron_copy: str,
) -> None:
    assert '<footer class="nb-footer">' in micron_copy
    assert 'class="nb-imprint"' in micron_copy
    assert 'class="nb-appearance"' in micron_copy


def test_the_canonical_library_file_stays_chrome_free(full_site: Site) -> None:
    canonical = full_site.read_library("library", "semiconductors", "micron.html")

    assert "nb-bar" not in canonical


def test_an_article_copy_is_otherwise_untouched(micron_copy: str) -> None:
    stamp = asset_stamp_of(micron_copy)

    assert undress(micron_copy).replace(f"?v={stamp}", "") == article()


def test_dressing_a_dressed_article_does_not_double_the_bar(micron_copy: str) -> None:
    site = {
        "title": "Fixture Press",
        "stamp": asset_stamp_of(micron_copy),
        "assets_html": "",
        "footer": None,
        "repository": None,
        "upstream": build_site.UPSTREAM_REPOSITORY,
    }

    dressed = build_site.dress_article(micron_copy, site)

    assert dressed.count('<header class="nb-bar">') == 1
    assert dressed.count('rel="icon"') == 2
    assert dressed.count('rel="apple-touch-icon"') == 1
