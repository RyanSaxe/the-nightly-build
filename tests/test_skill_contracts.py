"""Keep executable commands in the runtime instructions on the supported path.

The skills are operational inputs, not passive prose. This guard catches a raw
Python invocation before an agent copies it into a clean scheduled environment
where script-declared dependencies are available only through uv.
"""

import pathlib

REPO = pathlib.Path(__file__).parents[1]
RUNTIME_INSTRUCTIONS = (REPO / "PROTOCOL.md", *sorted((REPO / "skills").glob("*.md")))


def test_engine_commands_use_uv() -> None:
    offenders = [
        path.relative_to(REPO)
        for path in RUNTIME_INSTRUCTIONS
        if "python3 engine/" in path.read_text(encoding="utf-8")
    ]

    assert offenders == []
