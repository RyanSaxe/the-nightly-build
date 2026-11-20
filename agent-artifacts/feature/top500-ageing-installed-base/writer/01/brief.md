# writer brief: feature/top500-ageing-installed-base (01)

Inputs:
- .nb-work/feature/top500-ageing-installed-base/agent-artifacts/feature/top500-ageing-installed-base/editorial-direction.md — standing directions, template contract and series prompt
- .nb-work/feature/top500-ageing-installed-base/agent-artifacts/feature/top500-ageing-installed-base/commission.md — read "Decisions after research" first: the angle was revised; also the recent-pattern notes
- .nb-work/feature/top500-ageing-installed-base/agent-artifacts/feature/top500-ageing-installed-base/writing-coach/01/voice-guide.md — voice guide
- .nb-work/feature/top500-ageing-installed-base/agent-artifacts/feature/top500-ageing-installed-base/researcher/01/evidence.md — evidence record; the computed series are in .nb-work/feature/top500-ageing-installed-base/data/ (series.csv, cohort_survival.csv, compute.py)
Output: .nb-work/feature/top500-ageing-installed-base/agent-artifacts/feature/top500-ageing-installed-base/writer/01/draft-handoff.md, and the article at .nb-work/feature/top500-ageing-installed-base/library/feature/top500-ageing-installed-base.html
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/top500-ageing-installed-base/library/feature/top500-ageing-installed-base.html --series feature --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

Run environment: charts with `nb chart` (see its --help and spec/charts.md via the editorial direction), built only from the verified series. Chromium and Playwright are pre-installed; do not run playwright install or scripts/install-figure-capture.sh. Use `nb preview` and look at each chart at phone and desktop width in light and dark. Strict 600–1200 word band. Prefix nb commands with `export UV_SYSTEM_CERTS=1; unset UV_NATIVE_TLS;`.
