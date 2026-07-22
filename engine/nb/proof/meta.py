"""Parse article metadata and bind it to the configured series contract.

The metadata block is intentionally a small, explicit boundary between an
article and the engine. This module validates its primitive fields, resolves a
series' allowed template choices, and applies only the series-owned policy
bands after one template has been selected.
"""

import json
import os
import re

import yaml

from nb import meta as nb_meta
from nb.article import collapse_space
from nb.config import apply_template_bands, load_registry, load_series, template_choices

PROTOCOL_MAJOR = "1"
MAX_BYTES = 2 * 1024 * 1024
SLUG_RE = nb_meta.SLUG_RE
SERIES_RE = nb_meta.SERIES_RE
TAG_RE = nb_meta.TAG_RE
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

__all__ = (
    "bind_template",
    "check_meta_agreement",
    "parse_meta",
    "read_article_source",
    "resolve_series_and_template",
    "validate_meta_fields",
)

_META_TYPE_NAMES = {
    str: "a string",
    int: "an integer",
    list: "a list",
    bool: "true or false",
}


def validate_meta_fields(meta, rep):
    def need(field, typ, *, pattern=None, enum=None):
        v = meta.get(field)
        if v is None:
            rep.block("B-META-PARSE", f"nb-meta missing required field '{field}'")
            return None
        if typ and not isinstance(v, typ):
            rep.block(
                "B-META-PARSE",
                f"nb-meta field '{field}' must be {_META_TYPE_NAMES.get(typ, 'the right type')}",
            )
            return None
        if pattern and not re.match(pattern, str(v)):
            rep.block(
                "B-META-PARSE", f"nb-meta field '{field}' fails pattern {pattern}"
            )
        if enum and v not in enum:
            rep.block("B-META-PARSE", f"nb-meta field '{field}' must be one of {enum}")
        return v

    need("protocol", str)
    if (
        isinstance(meta.get("protocol"), str)
        and meta["protocol"].split(".")[0] != PROTOCOL_MAJOR
    ):
        rep.block(
            "B-META-PARSE",
            f"protocol major must be {PROTOCOL_MAJOR}, got {meta.get('protocol')}",
        )
    need("series", str, pattern=SERIES_RE.pattern)
    need("slug", str, pattern=SLUG_RE.pattern)
    # template membership is validated against the merged registry (B-SERIES /
    # B-META-MATCH) — user templates in press/templates/ are first-class
    need("template", str)
    need("title", str)
    need("mode", str, enum=list(nb_meta.MODES))
    need("date", str, pattern=DATE_RE.pattern)
    need("dek", str)
    need("sources", int)
    need("harness", str)
    need("model", str)
    order = meta.get("order")
    if order is not None and (not isinstance(order, int) or order < 1):
        rep.block("B-META-PARSE", "nb-meta 'order' must be a positive integer or null")
    tags = meta.get("tags")
    if tags is not None:
        if not isinstance(tags, list):
            rep.block("B-META-PARSE", "nb-meta field 'tags' must be a list")
        else:
            for tag in tags:
                if not isinstance(tag, str) or not nb_meta.is_safe_tag(tag):
                    rep.block(
                        "B-META-PARSE",
                        f"nb-meta tag {tag!r} must match {TAG_RE.pattern} "
                        "(lowercase slug: a-z, 0-9, hyphen)",
                    )


def resolve_series_and_template(repo, series_id, rep):
    """B-SERIES: load the series config and resolve its template choices.

    Returns ``(series, registry, allowed_templates)`` or None when a blocking
    failure means the check cannot continue. The manifest is bound only after
    article metadata names one choice from the series' list, regardless of
    scheduling mode.
    """
    series, spath = load_series(repo, series_id)
    if series is None:
        rep.block("B-SERIES", f"series '{series_id}' not found at {spath}")
        return None
    if not isinstance(series, dict):
        rep.block("B-SERIES", f"series '{series_id}' config must be a mapping")
        return None
    if series.get("paused"):
        rep.block(
            "B-SERIES",
            f"series '{series_id}' is paused — remove "
            f"'paused: true' from series.yaml to publish",
        )
    try:
        registry = load_registry(repo)
    except (OSError, yaml.YAMLError, TypeError, ValueError) as e:
        rep.block("B-SERIES", f"template manifests unreadable: {e}")
        return None

    allowed_templates = template_choices(series)
    unknown = [
        t for t in allowed_templates if not isinstance((registry or {}).get(t), dict)
    ]
    if not allowed_templates or unknown:
        rep.block(
            "B-SERIES",
            f"series templates {unknown or 'missing'} are not known templates",
        )
        return None
    return series, registry, allowed_templates


def read_article_source(html_path, rep):
    if not os.path.isfile(html_path):
        rep.block("B-HTML", f"file not found: {html_path}")
        return None
    size = os.path.getsize(html_path)
    if size > MAX_BYTES:
        rep.block("B-HTML", f"file is {size} bytes; limit is {MAX_BYTES}")
    with open(html_path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def parse_meta(ed, rep):
    if not ed.meta_raw:
        rep.block(
            "B-META-PARSE", 'no <script type="application/json" id="nb-meta"> block'
        )
        return None
    if ed.meta_count > 1:
        # The browser + build read the first #nb-meta; validating a second one
        # would let the proof approve metadata that never ships. One only.
        rep.block(
            "B-META-PARSE", f"exactly one #nb-meta block allowed, found {ed.meta_count}"
        )
        return None
    try:
        meta = json.loads(ed.meta_raw)
        if not isinstance(meta, dict):
            raise ValueError("nb-meta must be a JSON object")
    except ValueError as e:
        rep.block("B-META-PARSE", f"nb-meta JSON invalid: {e}")
        return None
    validate_meta_fields(meta, rep)
    return meta


def bind_template(meta, registry, *, allowed_templates, series, rep):
    template_id = meta.get("template")
    treg = (registry or {}).get(template_id) if isinstance(template_id, str) else None
    if not isinstance(treg, dict):
        rep.block(
            "B-META-MATCH",
            f"nb-meta template '{template_id}' is not a known template",
        )
        return None
    if template_id not in allowed_templates:
        rep.block(
            "B-META-MATCH",
            f"nb-meta template '{template_id}' is not one of the "
            f"series' allowed templates {allowed_templates}",
        )
    return template_id, apply_template_bands(treg, series=series)


def check_meta_agreement(
    meta,
    *,
    series,
    series_id,
    template_id,
    slug_from_path,
    parent,
    dekline,
    pr_body_meta,
    rep,
):
    if meta.get("slug") != slug_from_path:
        rep.block(
            "B-META-MATCH",
            f"path slug '{slug_from_path}' != nb-meta slug '{meta.get('slug')}'",
        )
    if parent and parent != series_id:
        rep.block(
            "B-META-MATCH", f"file sits under '{parent}/' but series is '{series_id}'"
        )
    if meta.get("series") != series_id:
        rep.block(
            "B-META-MATCH",
            f"nb-meta series '{meta.get('series')}' != declared series '{series_id}'",
        )
    if meta.get("mode") != series.get("mode"):
        rep.block(
            "B-META-MATCH",
            f"nb-meta mode '{meta.get('mode')}' != series mode '{series.get('mode')}'",
        )
    if meta.get("template") != template_id:
        rep.block(
            "B-META-MATCH",
            f"nb-meta template '{meta.get('template')}' is not the selected "
            f"series template '{template_id}'",
        )
    # The index card and the RSS summary are built from nb-meta's dek, so an
    # article whose body was fixed and whose meta was not ships the abandoned dek
    # on the front page and the feed. Nothing to compare against is nothing to say.
    dek = collapse_space(str(meta.get("dek", "")))
    if dekline and dek != dekline:
        rep.block(
            "B-META-MATCH",
            f"nb-meta dek {dek!r} != the rendered dekline {dekline!r}",
            suggestion="the front page and the feed render nb-meta's dek, not "
            "the body's; carry every dek edit back into nb-meta",
        )
    if pr_body_meta is not None:
        for field in ("series", "slug", "mode", "template", "date", "title"):
            if field in pr_body_meta and pr_body_meta.get(field) != meta.get(field):
                rep.block(
                    "B-META-MATCH",
                    f"PR body '{field}'={pr_body_meta.get(field)!r} disagrees "
                    f"with embedded nb-meta {meta.get(field)!r}",
                )
        b_order = pr_body_meta.get("order", meta.get("order"))
        if b_order != meta.get("order"):
            rep.block("B-META-MATCH", "PR body 'order' disagrees with embedded nb-meta")
