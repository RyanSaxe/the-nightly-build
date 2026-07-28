"""Search published coverage without exposing the raw library.

The site builder already turns article HTML into metadata and clean prose. This
module reuses those readers to provide small, predictable history results for
agents that need continuity or repetition checks without inviting a repository
tour or returning an earlier article's markup and ordered structure.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import os
import pathlib
import re
from collections.abc import Sequence
from dataclasses import dataclass

from nb.site.library import article_text, read_meta, scan_library

__all__ = (
    "HistoryEntry",
    "HistoryResult",
    "excerpt",
    "format_results",
    "load_entries",
    "main",
    "parser",
    "search",
)

DEFAULT_LIMIT = 8
MAX_LIMIT = 20
EXCERPT_LENGTH = 240


@dataclass(frozen=True)
class HistoryEntry:
    series: str
    slug: str
    title: str
    dek: str
    date: str
    tags: tuple[str, ...]
    text: str

    @property
    def reference(self) -> str:
        return f"{self.series}/{self.slug}"


@dataclass(frozen=True)
class HistoryResult:
    reference: str
    title: str
    dek: str
    date: str
    tags: tuple[str, ...]
    match: str | None


def _string(value: object, fallback: str = "") -> str:
    return value if isinstance(value, str) else fallback


def _tags(value: object) -> tuple[str, ...]:
    if not isinstance(value, list):
        return ()
    return tuple(tag for tag in value if isinstance(tag, str))


def load_entries(library: pathlib.Path) -> list[HistoryEntry]:
    entries: list[HistoryEntry] = []
    for series, slug, path in scan_library(str(library)):
        metadata = read_meta(path)
        if metadata is None:
            continue
        entries.append(
            HistoryEntry(
                series=series,
                slug=slug,
                title=_string(metadata.get("title"), slug),
                dek=_string(metadata.get("dek")),
                date=_string(metadata.get("date")),
                tags=_tags(metadata.get("tags")),
                text=article_text(path),
            )
        )
    return entries


def excerpt(text: str, terms: Sequence[str]) -> str | None:
    if not terms:
        return None
    folded = text.casefold()
    positions = [folded.find(term) for term in terms if folded.find(term) >= 0]
    if not positions:
        return None
    center = min(positions)
    start = max(0, center - EXCERPT_LENGTH // 3)
    end = min(len(text), start + EXCERPT_LENGTH)
    fragment = re.sub(r"\s+", " ", text[start:end]).strip()
    if start:
        fragment = f"…{fragment}"
    if end < len(text):
        fragment = f"{fragment}…"
    return fragment


def _score(entry: HistoryEntry, terms: Sequence[str]) -> int:
    title = entry.title.casefold()
    dek = entry.dek.casefold()
    tags = " ".join(entry.tags).casefold()
    text = entry.text.casefold()
    reference = entry.reference.casefold()
    return sum(
        (12 if term in title else 0)
        + (7 if term in dek else 0)
        + (5 if term in tags else 0)
        + (3 if term in reference else 0)
        + min(text.count(term), 4)
        for term in terms
    )


def search(
    entries: Sequence[HistoryEntry],
    query: Sequence[str],
    *,
    series: str | None = None,
    limit: int = DEFAULT_LIMIT,
) -> list[HistoryResult]:
    terms = tuple(term.casefold().strip() for term in query if term.strip())
    eligible = [entry for entry in entries if series is None or entry.series == series]
    if terms:
        eligible = [
            entry
            for entry in eligible
            if all(
                term
                in " ".join(
                    (
                        entry.reference,
                        entry.title,
                        entry.dek,
                        " ".join(entry.tags),
                        entry.text,
                    )
                ).casefold()
                for term in terms
            )
        ]
    eligible.sort(
        key=lambda entry: (_score(entry, terms), entry.date, entry.reference),
        reverse=True,
    )
    return [
        HistoryResult(
            reference=entry.reference,
            title=entry.title,
            dek=entry.dek,
            date=entry.date,
            tags=entry.tags,
            match=excerpt(entry.text, terms),
        )
        for entry in eligible[:limit]
    ]


def format_results(results: Sequence[HistoryResult]) -> str:
    if not results:
        return "No matching published coverage."
    lines: list[str] = []
    for result in results:
        date = f" · {result.date}" if result.date else ""
        lines.append(f"{result.reference}{date} · {result.title}")
        if result.dek:
            lines.append(f"  {result.dek}")
        if result.tags:
            lines.append(f"  tags: {', '.join(result.tags)}")
        if result.match:
            lines.append(f"  match: {result.match}")
    return "\n".join(lines)


def _limit(value: str) -> int:
    parsed = int(value)
    if not 1 <= parsed <= MAX_LIMIT:
        raise argparse.ArgumentTypeError(f"limit must be between 1 and {MAX_LIMIT}")
    return parsed


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(
        description="Search bounded, plain-text records of published coverage"
    )
    command.add_argument(
        "query",
        nargs="*",
        help="terms that must all occur; omit to list recent coverage",
    )
    command.add_argument(
        "--library",
        default=os.getenv("NB_LIBRARY", "."),
        type=pathlib.Path,
        help="library checkout (defaults to $NB_LIBRARY or the current directory)",
    )
    command.add_argument("--series", help="restrict results to one series")
    command.add_argument("--limit", type=_limit, default=DEFAULT_LIMIT)
    command.add_argument("--json", action="store_true")
    return command


def main(arguments: list[str] | None = None) -> None:
    options = parser().parse_args(arguments)
    results = search(
        load_entries(options.library),
        options.query,
        series=options.series,
        limit=options.limit,
    )
    if options.json:
        print(json.dumps([dataclasses.asdict(result) for result in results], indent=2))
    else:
        print(format_results(results))


if __name__ == "__main__":
    main()
