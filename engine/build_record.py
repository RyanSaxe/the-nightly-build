#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Build the durable production record that accompanies an article PR.

Role artifacts are gitignored so a content PR remains an article bundle. This
module is the single serialization point that preserves those artifacts in the
review record without trusting an agent to copy or abbreviate them by hand.
"""

import argparse
import hashlib
import pathlib
import re

import yaml

from nb import meta as nb_meta

ARTIFACT_SECTIONS = (
    ("Task", "task.md"),
    ("Process", "requested-changes.md"),
    ("Voice brief", "voice.md"),
    ("Research", "research.md"),
)
DEFAULT_BODY_LIMIT = 60_000


def read_artifacts(work: pathlib.Path) -> dict[str, str]:
    artifacts = {}
    for _, filename in ARTIFACT_SECTIONS:
        path = work / filename
        if not path.is_file():
            raise ValueError(f"missing production artifact: {path}")
        artifacts[filename] = path.read_text(encoding="utf-8")
    return artifacts


def discarded(research: str) -> str:
    marker = re.search(r"^## Discarded\s*$", research, re.M)
    return research[marker.end() :].strip() if marker else "None."


def fenced_artifact(content: str) -> str:
    return f"<details><summary>Full artifact</summary>\n\n````text\n{content.rstrip()}\n````\n\n</details>"


def metadata(article: pathlib.Path) -> dict[str, object]:
    meta = nb_meta.read_meta(str(article))
    if meta is None:
        raise ValueError(f"article has no readable nb-meta block: {article}")
    return meta


def yaml_meta(meta: dict[str, object]) -> str:
    keys = ("series", "slug", "mode", "template", "date", "title", "order")
    return yaml.safe_dump({key: meta.get(key) for key in keys}, sort_keys=False).strip()


def full_record(meta: dict[str, object], artifacts: dict[str, str]) -> str:
    sections = [f"```nb-meta\n{yaml_meta(meta)}\n```"]
    for heading, filename in ARTIFACT_SECTIONS:
        sections.append(f"## {heading}\n\n{fenced_artifact(artifacts[filename])}")
    sections.append(f"## Also consulted\n\n{discarded(artifacts['research.md'])}")
    return "\n\n".join(sections) + "\n"


def digest(artifacts: dict[str, str]) -> str:
    joined = "".join(f"{name}\0{content}" for name, content in artifacts.items())
    return hashlib.sha256(joined.encode()).hexdigest()


def compact_record(
    meta: dict[str, object],
    artifacts: dict[str, str],
    *,
    spilled: set[str],
    record_digest: str,
) -> str:
    reference = (
        "Full artifact moved to the marked follow-up comment "
        f"(`nb-record-sha256: {record_digest}`)."
    )
    sections = [f"```nb-meta\n{yaml_meta(meta)}\n```"]
    for heading, filename in ARTIFACT_SECTIONS:
        content = (
            reference if heading in spilled else fenced_artifact(artifacts[filename])
        )
        sections.append(f"## {heading}\n\n{content}")
    consulted = (
        reference
        if "Also consulted" in spilled
        else discarded(artifacts["research.md"])
    )
    sections.append(f"## Also consulted\n\n{consulted}")
    return "\n\n".join(sections) + "\n"


def overflow_record(
    meta: dict[str, object], artifacts: dict[str, str], *, limit: int
) -> tuple[str, str]:
    record = full_record(meta, artifacts)
    record_digest = digest(artifacts)
    comment = f"<!-- nb-production-record {record_digest} -->\n\n{record}"
    spillable = {
        "Task": artifacts["task.md"],
        "Process": artifacts["requested-changes.md"],
        "Research": artifacts["research.md"],
        "Also consulted": discarded(artifacts["research.md"]),
    }
    spilled: set[str] = set()
    for heading, _content in sorted(
        spillable.items(), key=lambda item: len(item[1]), reverse=True
    ):
        spilled.add(heading)
        body = compact_record(
            meta, artifacts, spilled=spilled, record_digest=record_digest
        )
        if len(body) <= limit:
            return body, comment
    raise ValueError(
        "production-record index and voice brief exceed the PR-body limit; "
        "shorten voice.md"
    )


def build(
    article: pathlib.Path, work: pathlib.Path, *, limit: int = DEFAULT_BODY_LIMIT
) -> tuple[str, str | None]:
    artifacts = read_artifacts(work)
    record = full_record(metadata(article), artifacts)
    if len(record) <= limit:
        return record, None
    return overflow_record(metadata(article), artifacts, limit=limit)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("article", type=pathlib.Path)
    parser.add_argument("--work", type=pathlib.Path, required=True)
    parser.add_argument("--out", type=pathlib.Path, required=True)
    parser.add_argument("--comment-out", type=pathlib.Path)
    parser.add_argument("--limit", type=int, default=DEFAULT_BODY_LIMIT)
    args = parser.parse_args()
    body, comment = build(args.article, args.work, limit=args.limit)
    args.out.write_text(body, encoding="utf-8")
    if comment is not None:
        if args.comment_out is None:
            raise SystemExit(
                "record exceeds limit; pass --comment-out for the full comment"
            )
        args.comment_out.write_text(comment, encoding="utf-8")
    elif args.comment_out is not None:
        args.comment_out.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
