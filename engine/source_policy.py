#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Print the resolved source obligations for a commissioned series.

Desks use this before writing task.md so every role sees the real source floor,
including a template default that is intentionally absent from series.yaml.
It writes JSON only, which makes the result safe to copy into a commission card
without asking an agent to recreate source-policy logic from configuration prose.
"""

import argparse
import json

from nb.config import load_registry, load_series
from nb.source_policy import resolve


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".")
    parser.add_argument("--series", required=True)
    args = parser.parse_args()
    series, path = load_series(args.repo, args.series)
    if not isinstance(series, dict):
        raise SystemExit(f"configured series not found: {path}")
    template_id = series.get("template")
    if not isinstance(template_id, str):
        raise SystemExit(f"series has no single template: {path}")
    template = load_registry(args.repo).get(template_id)
    if not isinstance(template, dict):
        raise SystemExit(f"unknown template '{template_id}'")
    print(json.dumps(resolve(series, template), sort_keys=True))


if __name__ == "__main__":
    main()
