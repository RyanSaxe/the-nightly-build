"""Check what the series mode allows an article to publish.

The mode proof owns slug admission, ordering, configured commissions, and
published-state deduplication. Cadence normally belongs to the scheduler; the
manual-open exception is checked here because each manually commissioned slug
must be explicit configuration before CI accepts it.
"""

import datetime as _dt

from nb.proof.meta import DATE_RE

__all__ = (
    "check_mode",
    "check_open_slug",
    "check_ordered_mode",
    "check_rolling_mode",
    "check_sequence_slug",
)


def check_sequence_slug(meta, *, items, idx, slug, pub, revision, rep):
    if revision:
        if meta.get("order") != idx + 1:
            rep.block(
                "B-MODE",
                f"sequence order must be item position {idx + 1}; "
                f"nb-meta says {meta.get('order')}",
            )
        return
    if pub is None:
        if meta.get("order") != idx + 1:
            rep.block(
                "B-MODE",
                f"sequence order must be item position {idx + 1}; "
                f"nb-meta says {meta.get('order')}",
            )
        rep.notes.append(
            "library state not provided (--library); next-expected check skipped"
        )
        return
    expected = next(
        (i for i, it in enumerate(items) if it.get("slug") not in pub), None
    )
    if expected is None:
        rep.block("B-MODE", "sequence is complete; nothing to publish")
    elif idx != expected:
        rep.block(
            "B-MODE",
            f"next expected sequence item is "
            f"'{items[expected].get('slug')}' (#{expected + 1}), not '{slug}'",
        )
    elif meta.get("order") != expected + 1:
        rep.block(
            "B-MODE",
            f"nb-meta order must be {expected + 1}, got {meta.get('order')}",
        )


def check_ordered_mode(meta, *, series_id, items, slug, pub, mode, revision, rep):
    idx = next((i for i, it in enumerate(items) if it.get("slug") == slug), None)
    if idx is None:
        if revision:
            # published is a fact: revising never requires the item's config
            return None
        rep.block(
            "B-SLUG",
            f"slug '{slug}' is not a configured item of series '{series_id}'",
        )
        return None
    item_cfg = items[idx]
    if mode == "sequence":
        check_sequence_slug(
            meta,
            items=items,
            idx=idx,
            slug=slug,
            pub=pub,
            revision=revision,
            rep=rep,
        )
    elif not revision and pub is not None and slug in pub:
        rep.block("B-MODE", f"'{slug}' is already published")
    return item_cfg


def check_rolling_mode(meta, *, slug, pub, today, revision, rep):
    if not DATE_RE.match(slug):
        rep.block("B-SLUG", f"rolling slug must be YYYY-MM-DD, got '{slug}'")
    else:
        try:
            d = _dt.date.fromisoformat(slug)
            if d > today:
                rep.block("B-SLUG", f"rolling slug {slug} is in the future")
        except ValueError:
            rep.block("B-SLUG", f"rolling slug '{slug}' is not a real date")
        if meta.get("date") != slug:
            rep.block(
                "B-META-MATCH",
                f"rolling nb-meta date '{meta.get('date')}' must equal slug",
            )
        if not revision and pub is not None and slug in pub:
            rep.block("B-MODE", f"a brief for {slug} is already published")
    if pub is None:
        rep.notes.append(
            "library state not provided (--library); already-published check skipped"
        )


def check_open_slug(*, items, slug, pub, manual, revision, rep):
    item_cfg = next((it for it in items if it.get("slug") == slug), None)
    if revision:
        # published is a fact: revising never requires the item's config
        return item_cfg
    if manual and item_cfg is None:
        rep.block(
            "B-SLUG",
            f"manual open series requires '{slug}' to be a configured item",
        )
        return None
    if pub is None:
        rep.notes.append(
            "library state not provided (--library); "
            "open-mode dedupe and commission checks skipped"
        )
        return item_cfg
    if slug in pub:
        rep.block("B-MODE", f"'{slug}' is already published")
    pending = sorted(it.get("slug") for it in items if it.get("slug") not in pub)
    if pending and slug not in pending:
        rep.block(
            "B-MODE",
            f"commissioned items pending: {pending} — publish a "
            f"commission before an open pick",
        )
    return item_cfg


def check_mode(meta, *, series, series_id, slug, pub, today, revision=False, rep):
    mode = series.get("mode")
    items = series.get("items") or []
    if mode in ("collection", "sequence"):
        return check_ordered_mode(
            meta,
            series_id=series_id,
            items=items,
            slug=slug,
            pub=pub,
            mode=mode,
            revision=revision,
            rep=rep,
        )
    if mode == "rolling":
        check_rolling_mode(
            meta,
            slug=slug,
            pub=pub,
            today=today,
            revision=revision,
            rep=rep,
        )
        return None
    if mode == "open":
        return check_open_slug(
            items=items,
            slug=slug,
            pub=pub,
            manual=series.get("cadence") == "manual",
            revision=revision,
            rep=rep,
        )
    return None
