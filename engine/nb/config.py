"""Read the press configuration used by the engine.

This module owns the shared configuration readers and the small amount of
normalization needed before validation, proof, duty tooling, or site building
consumes a series and its selected template. Keeping template choice and band
precedence here prevents those consumers from silently implementing different
interpretations of the same press configuration.
"""

import os
import sys
from collections.abc import Mapping

from nb import meta as nb_meta
from nb.site.assets import template_dirs

try:
    import yaml
except ImportError:
    sys.stderr.write("check.py requires PyYAML (pip install pyyaml)\n")
    sys.exit(2)


TEMPLATE_BAND_KEYS = ("words", "items", "flex_sections")

__all__ = (
    "TEMPLATE_BAND_KEYS",
    "apply_template_bands",
    "find_template",
    "load_banned_terms",
    "load_registry",
    "load_series",
    "load_yaml",
    "published_slugs",
    "template_choices",
)


def load_yaml(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_registry(repo):
    """Load every template's manifest, press packages shadowing shipped.

    template_dirs owns what counts as a template package and how press/
    shadows shipped; the manifests it finds carry the geometry the proof
    enforces.
    """
    return {
        tid: load_yaml(os.path.join(folder, "manifest.yaml")) or {}
        for tid, folder in template_dirs(repo).items()
    }


def template_choices(series: Mapping) -> list[str]:
    """Return the series' allowed template IDs in one normalized shape.

    A valid series declares either one ``template`` string or a non-empty
    ``templates`` list.  This helper remains defensive for proof runs against
    a press that skipped configuration validation: malformed values produce an
    empty or partially usable choice list instead of an unhashable registry
    lookup.
    """
    choices = series.get("templates")
    if isinstance(choices, list):
        return [choice for choice in choices if isinstance(choice, str)]
    template = series.get("template")
    return [template] if isinstance(template, str) else []


def apply_template_bands(template: Mapping, *, series: Mapping) -> dict:
    """Layer series policy bands over one template's defaults.

    Only the three public geometry bands are copied.  Structural manifest
    fields remain owned by the template package, while an absent template band
    simply means that no default exists until the series supplies one.
    """
    effective = dict(template)
    template_bands = template.get("bands")
    bands = dict(template_bands) if isinstance(template_bands, Mapping) else {}
    series_bands = series.get("bands")
    if isinstance(series_bands, Mapping):
        bands.update(
            {
                key: series_bands[key]
                for key in TEMPLATE_BAND_KEYS
                if key in series_bands
            }
        )
    effective["bands"] = bands
    return effective


def find_template(repo, template_id):
    for base in (
        os.path.join(repo, "press", "templates"),  # press/ shadows shipped templates/
        os.path.join(repo, "templates"),
    ):
        path = os.path.join(base, template_id, "skeleton.html")
        if os.path.isfile(path):
            return path
    return None


def load_banned_terms(repo):
    """Merge the engine's banned-terms list with the press's.

    spec/banned-terms.yaml seeds the list; press/banned-terms.yaml layers
    over it by id — a new id adds a ban, a repeated id updates only the
    fields it states, and enabled false retires an entry. Malformed entries
    are skipped here; validate_config.py is where authors hear about them.
    """
    merged = {}
    for path in (
        os.path.join(repo, "spec", "banned-terms.yaml"),
        os.path.join(repo, "press", "banned-terms.yaml"),
    ):
        if not os.path.isfile(path):
            continue
        entries = load_yaml(path) or []
        if not isinstance(entries, list):
            continue
        for entry in entries:
            if not isinstance(entry, dict) or not entry.get("id"):
                continue
            merged.setdefault(entry["id"], {}).update(entry)
    return [e for e in merged.values() if e.get("enabled", True) and e.get("terms")]


def load_series(repo, series_id) -> tuple[dict | None, str]:
    path = os.path.join(repo, "press", "series", series_id, "series.yaml")
    if not os.path.isfile(path):
        return None, path
    return load_yaml(path), path


def published_slugs(library_dir, series_id) -> set[str] | None:
    """Return the set of published slugs for a series.

    Returns None when no library checkout was provided, which callers
    must treat as unknowable rather than empty: dedupe and sequence
    checks are skipped with a note instead of firing falsely.
    """
    if not library_dir:
        return None
    base = nb_meta.series_dir(library_dir, series_id)
    if base is None:
        return set()  # library exists but series dir doesn't => nothing published
    return {f[:-5] for f in os.listdir(base) if f.endswith(".html")}
