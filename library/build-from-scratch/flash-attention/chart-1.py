"""Peak buffer memory vs sequence length N, float32, head dim d=64.

naive:     the full N x N score matrix S = QK^T, held in memory at once.
streaming: one K/V block's (N x block_size) score buffer plus the three
           running per-query accumulators (m, l, o), block_size=64.

The byte counts below are the closed-form version of the same accounting
attention_core.py performs empirically via ndarray.nbytes while it runs
naive_attention() and streaming_attention() -- confirmed to match exactly at
every N in this article's own measured run (e.g. N=8192: naive 268,435,456 B,
streaming 4,259,840 B, both reproduced here).

Provenance for chart-1.png."""
import numpy as np
import plotly.graph_objects as go

ITEMSIZE = np.dtype(np.float32).itemsize  # 4


def naive_peak_bytes(n):
    return n * n * ITEMSIZE


def streaming_peak_bytes(n, d, block_size):
    score_block = n * block_size * ITEMSIZE
    running_m = n * ITEMSIZE
    running_l = n * ITEMSIZE
    running_o = n * d * ITEMSIZE
    return score_block + running_m + running_l + running_o


d = 64
block_size = 64
Ns = [64, 128, 256, 512, 1024, 2048, 4096, 8192]
naive = [naive_peak_bytes(n) for n in Ns]
stream = [streaming_peak_bytes(n, d, block_size) for n in Ns]

fig = go.Figure()
fig.add_trace(
    go.Scatter(name="naive: full N×N score matrix", x=Ns, y=naive, mode="lines+markers")
)
fig.add_trace(
    go.Scatter(
        name="streaming: one block + running (m, l, o)",
        x=Ns,
        y=stream,
        mode="lines+markers",
    )
)
fig.update_layout(
    xaxis_title="sequence length N (log scale)",
    yaxis_title="peak buffer bytes (log scale, float32, d=64, block=64)",
    xaxis_type="log",
    yaxis_type="log",
)
