"""Exercise first-time setup against a local Git remote.

Each run of scripts/setup.sh starts from a fresh fork. With the fake GitHub
CLI, setup must scaffold the press, create and seed the library branch, and
make the fork settings itself, never touching the Pages environment. Without a
signed-in CLI it must still do the git side and print the settings only an
admin can make.
"""

import os
import pathlib
import shutil
import subprocess
from dataclasses import dataclass

from press import REPO
from test_sync_script import WORKFLOWS, configure_author, git, write_fake_gh


@dataclass(frozen=True)
class SetupRepo:
    checkout: pathlib.Path
    origin: pathlib.Path
    gh_log: pathlib.Path
    fake_bin: pathlib.Path

    def run(self, *, gh_mode: str) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env.update(
            {
                "FAKE_GH_LOG": str(self.gh_log),
                "FAKE_GH_MODE": gh_mode,
                "FAKE_ORIGIN": str(self.origin),
                "PATH": f"{self.fake_bin}{os.pathsep}{env['PATH']}",
                "UV_PROJECT_ENVIRONMENT": str(REPO / ".venv"),
            }
        )
        return subprocess.run(
            [str(self.checkout / "scripts" / "setup.sh")],
            cwd=self.checkout,
            env=env,
            capture_output=True,
            text=True,
        )

    def library_files(self) -> set[str]:
        listing = subprocess.run(
            [
                "git",
                f"--git-dir={self.origin}",
                "ls-tree",
                "-r",
                "--name-only",
                "library",
            ],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        return set(listing.split())


def make_setup_repo(tmp_path: pathlib.Path) -> SetupRepo:
    source = tmp_path / "source"
    origin = tmp_path / "origin.git"
    checkout = tmp_path / "checkout"
    (source / "scripts").mkdir(parents=True)
    (source / ".github" / "workflows").mkdir(parents=True)
    for name in ("nb", "pyproject.toml", "uv.lock"):
        shutil.copy2(REPO / name, source / name)
    for name in ("setup.sh", "sync.sh"):
        shutil.copy2(REPO / "scripts" / name, source / "scripts" / name)
    for name in ("engine", "templates", "spec"):
        shutil.copytree(REPO / name, source / name)
    for path in WORKFLOWS:
        (source / path).write_text((REPO / path).read_text())
    git(source, "init", "-q", "-b", "main")
    configure_author(source)
    git(source, "add", "-A")
    git(source, "commit", "-qm", "engine")
    subprocess.run(
        ["git", "clone", "-q", "--bare", str(source), str(origin)], check=True
    )
    subprocess.run(["git", "clone", "-q", str(origin), str(checkout)], check=True)
    configure_author(checkout)
    fake_bin = tmp_path / "bin"
    gh_log = tmp_path / "gh.log"
    gh_log.write_text("")
    write_fake_gh(fake_bin)
    return SetupRepo(checkout, origin, gh_log, fake_bin)


def test_setup_scaffolds_a_press_with_dispatches(tmp_path: pathlib.Path) -> None:
    repo = make_setup_repo(tmp_path)

    result = repo.run(gh_mode="available")

    assert result.returncode == 0, result.stderr + result.stdout
    series = repo.checkout / "press" / "series" / "dispatches"
    assert "cadence: manual" in (series / "series.yaml").read_text()
    assert (series / "prompt.md").read_text().strip()
    assert "Ask for an article" in result.stdout


def test_setup_with_gh_makes_the_settings_and_skips_the_environment(
    tmp_path: pathlib.Path,
) -> None:
    repo = make_setup_repo(tmp_path)

    result = repo.run(gh_mode="available")

    assert result.returncode == 0, result.stderr + result.stdout
    assert {"library/.gitkeep", *WORKFLOWS} <= repo.library_files()
    assert "Not verified" not in result.stdout
    calls = repo.gh_log.read_text()
    assert "repos/example/nightly-build/pages" in calls
    assert "actions/permissions" in calls
    assert "branches/library/protection" in calls
    assert "allow_auto_merge" in calls
    assert "environments/github-pages" not in calls


def test_setup_is_idempotent_over_a_healthy_fork(tmp_path: pathlib.Path) -> None:
    repo = make_setup_repo(tmp_path)
    first = repo.run(gh_mode="available")
    assert first.returncode == 0, first.stderr + first.stdout

    second = repo.run(gh_mode="available")

    assert second.returncode == 0, second.stderr + second.stdout
    assert "library branch already exists" in second.stdout
