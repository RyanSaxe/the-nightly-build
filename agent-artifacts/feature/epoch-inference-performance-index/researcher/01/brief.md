# researcher brief: feature/epoch-inference-performance-index (01)

Inputs:
- editorial-direction.md: the standards and source policy
- commission.md: the story, the angle to test, what would break it
Output: researcher/01/evidence.md (beside this brief)

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

Download the Data Insight's CSV and any per-chip IPI table into
researcher/01/data/ and record the exact columns and units so the writer can
chart them with nb chart. Record the full series. Recompute any growth figure
you report and show the arithmetic. Get the 8-bit dense FLOP/s for each chip
from the vendor datasheet or Epoch's hardware database, not from coverage.
Find at least one independent inference benchmark (MLPerf Inference results,
SemiAnalysis InferenceMAX, or similar) that compares GB300 or B200 with H100 on
a named model, and record its exact ratio and conditions.
