# researcher brief: feature/data-centers-electricity-prices (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/feature/data-centers-electricity-prices/agent-artifacts/feature/data-centers-electricity-prices/editorial-direction.md: the standing editorial direction
- /home/user/the-nightly-build/.nb-work/feature/data-centers-electricity-prices/agent-artifacts/feature/data-centers-electricity-prices/commission.md: the story, the angle to test and the decisions
Output: /home/user/the-nightly-build/.nb-work/feature/data-centers-electricity-prices/agent-artifacts/feature/data-centers-electricity-prices/researcher/01/evidence.md

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, record the question in Limits, decide it, and say so in your report.

Starting leads from the orchestrator's scouting, all unverified: Washington Post 2026-11-06 "Data centers may not be raising Americans' electricity bills that much" (403 to plain fetch); arxiv.org/abs/2606.19777 "Have Data Centers Raised Your Electric Bill? Causal Evidence from the United States"; cepr.org/voxeu/columns/how-data-centres-affect-electricity-prices-and-whom; datacentercoalition.org/cpages/e3-energy-white-paper (E3, industry-commissioned); energyanalytics.org/research/dont-blame-the-data-centers; a USC study (doubling capacity, +0.62% residential); a 2015-2024 paper (doubling capacity, -3.5% residential at fixed demand); a $2.59/MWh-per-GW decrease estimate. Identify which document owns each figure.

For the writer's visuals, record each estimate in a comparable form where the documents allow (effect, unit, price type, customer class, period, geography, design), and the components of a residential rate that a new load can move in each direction, each with its owner.

Run environment: web tools are WebSearch and WebFetch (WebFetch summarizes through a small model; for any figure, retrieve the raw PDF or HTML with curl via Bash, extract text with pdftotext or python, and read the table). Today is 6 November 2026.
