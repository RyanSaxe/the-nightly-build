"""Keep one managed checkout of ``origin/library`` for commands that read it.

``nb duty``, ``nb history``, and ``nb prepare-pr`` read the published branch
beside the engine. A runtime may hand them a checkout it manages; when none is
given, the engine keeps a detached worktree under ``.nb-work/``, which is never
published, and moves it to current ``origin/library`` on every use.
"""

from __future__ import annotations

import os
import pathlib
import subprocess

__all__ = ("LibraryCheckoutError", "ensure_library", "repo_root")

MANAGED = pathlib.Path(".nb-work", "library")


class LibraryCheckoutError(RuntimeError):
    pass


def repo_root() -> pathlib.Path:
    return pathlib.Path(os.environ.get("NB_ROOT", pathlib.Path(__file__).parents[2]))


# Git's argv is naturally variadic.
# ast-grep-ignore: keyword-only-args
def _git(cwd: pathlib.Path, *arguments: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(cwd), *arguments], capture_output=True, text=True
    )
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise LibraryCheckoutError(f"git {' '.join(arguments)} failed: {detail}")
    return result.stdout.strip()


def ensure_library(root: pathlib.Path | None = None) -> pathlib.Path:
    base = (root or repo_root()).resolve()
    checkout = base / MANAGED
    fetched = subprocess.run(
        ["git", "-C", str(base), "fetch", "-q", "origin", "library"],
        capture_output=True,
        text=True,
    )
    if fetched.returncode:
        detail = fetched.stderr.strip() or fetched.stdout.strip()
        raise LibraryCheckoutError(
            f"cannot fetch origin/library ({detail}); "
            "if the branch does not exist yet, run nb setup"
        )
    if checkout.exists():
        if not (checkout / ".git").exists():
            raise LibraryCheckoutError(
                f"{checkout} exists and is not a git checkout; move it aside"
            )
        _git(checkout, "checkout", "-q", "--detach", "origin/library")
        return checkout
    checkout.parent.mkdir(parents=True, exist_ok=True)
    _git(base, "worktree", "add", "-q", "--detach", str(checkout), "origin/library")
    return checkout
